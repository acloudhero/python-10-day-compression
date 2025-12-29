# Day 9: Log Analyzer v1

def load_log_file(path):
    """Stream log lines without loading entire file into memory."""
    with open(path, "r") as f:
        for line in f:
            yield line.strip()


def analyze_logs(lines):
    """Analyze log content and compute summary statistics."""
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

        # Split into timestamp + level + message
        parts = line.split(" ", 2)
        timestamp = parts[0] + " " + parts[1]
        level = parts[2].split(" ")[0]

        # Track first + last timestamps
        if summary["first_timestamp"] is None:
            summary["first_timestamp"] = timestamp
        summary["last_timestamp"] = timestamp

        # Count levels
        if level == "INFO":
            summary["info"] += 1
        elif level == "WARN":
            summary["warn"] += 1
        elif level == "ERROR":
            summary["error"] += 1
            summary["error_timestamps"].append(timestamp)

    return summary


def main():
    lines = load_log_file("sample.log")
    summary = analyze_logs(lines)

    import json
    with open("summary.json", "w") as f:
        f.write(json.dumps(summary, indent=2))

    print("Log analysis complete. Summary written to summary.json")


if __name__ == "__main__":
    main()
