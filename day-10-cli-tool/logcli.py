import argparse
import json

def load_log_file(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

def analyze_logs(lines):
    summary = {
        "total_lines": 0,
        "info": 0,
        "warn": 0,
        "error": 0,
        "error_timestamps": [],
        "first_timestamp": None,
        "last_timestamp": None,
    }

    for line in lines:
        summary["total_lines"] += 1

        parts = line.split(" ", 2)
        timestamp = parts[0] + " " + parts[1]
        level = parts[2].split(" ")[0]

        if summary["first_timestamp"] is None:
            summary["first_timestamp"] = timestamp
        summary["last_timestamp"] = timestamp

        if level == "INFO":
            summary["info"] += 1
        elif level == "WARN":
            summary["warn"] += 1
        elif level == "ERROR":
            summary["error"] += 1
            summary["error_timestamps"].append(timestamp)

    return summary


def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line


def main():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")

    parser.add_argument("logfile", help="Path to the log file to analyze")
    parser.add_argument("--errors-only", action="store_true",
                        help="Output only ERROR lines")
    parser.add_argument("--json", metavar="OUTPUT",
                        help="Write summary to a JSON file")

    args = parser.parse_args()

    lines = list(load_log_file(args.logfile))

    if args.errors_only:
        for err in filter_errors(lines):
            print(err)
        return

    summary = analyze_logs(lines)

    if args.json:
        with open(args.json, "w") as f:
            f.write(json.dumps(summary, indent=2))
        print(f"Summary written to {args.json}")
    else:
        print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
