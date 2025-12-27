# Python 10-Day Compression Sprint

## Overview
This repository documents a 10-day Python compression sprint focused on building **practical fluency** as quickly as possible.

The objective is not academic mastery.  
The objective is functional competence — the ability to write, run, debug, and refactor Python scripts that resemble real-world automation, cloud, and systems work.

This repo intentionally preserves the learning trail.  
Commits are chronological, incremental, and reflect how understanding actually develops.

---

## Objectives
- Become dangerous fast with Python
- Build confidence through execution, not theory
- Prepare for the PCEP certification as a secondary outcome
- Create a public, timestamped record of working artifacts

---

## Repository Structure
Each day has a dedicated folder representing a focused learning goal.


Earlier days emphasize mechanics.  
Later days emphasize **design decisions and refactoring**.

---

## Progress Log

### **Day 1 — Core Runtime & Types**
**Focus**
- Python runtime
- Basic data types
- Arithmetic and printing output

**Built**
- Simple executable scripts
- Verified understanding of literals, variables, and expressions

---

### **Day 2 — Control Flow**
**Focus**
- `if / elif / else`
- Explicit decision boundaries

**Built**
- Scripts that encode rules through conditionals
- Clear branching logic based on user input

---

### **Day 3 — Loops & Iteration**
**Focus**
- `for` loops
- Iteration ranges
- Filtering values during iteration

**Built**
- A loop-based script that evaluates and prints even numbers
- Combined looping with conditional logic

---

### **Day 4 — Functions & Reuse**
**Focus**
- `def`
- Parameters
- Return values
- Separating logic into reusable units

**Built**
- Functions that accept inputs and return computed results
- Scripts that compose functions instead of duplicating logic

**Key Insight**
Return values enabled functions to feel *connected* rather than isolated.

---

### **Day 5 — Mini Program: Rules-Driven Access Checker (Imperative v1)**
**Focus**
- Combining functions, loops, and conditionals
- Managing program state
- Handling repeated user input

**Built**
- An interactive access checker that:
  - Accepts a role and environment
  - Determines access level
  - Tracks number of checks performed
  - Exits cleanly with a summary

**Design Characteristics**
- Rules encoded using explicit `if / elif` conditionals
- Logic is correct but verbose
- Adding new rules requires modifying control flow

This version serves as a **baseline implementation**.

---

### **Day 6 — Data-Driven Refactor (Rules as Data)**
**Focus**
- Dictionaries
- Tuples as composite keys
- Separating data from logic
- Input normalization

**Refactor**
- Replaced conditional chains with a dictionary-based rules engine
- Access rules expressed as data instead of control flow
- Simplified access evaluation to a single lookup
- Normalized user input to handle casing and unexpected values

**Outcome**
- Same behavior as Day 5
- Fewer lines of code
- Significantly easier to extend and reason about

---

### **Day 7 — Lists, Aggregation, and Rule Evaluation at Scale**

**Focus**
- Lists as collections of inputs
- Evaluating rules across multiple cases
- Aggregating outcomes instead of handling one input at a time

**Built**
- A batch rules evaluator that applies existing access logic across a list of requests
- A summary report that aggregates access outcomes by type

**Key Concepts**
- Separation of rules (data) from execution
- Reusing functions without modifying logic
- Deterministic evaluation across collections
- Moving from interactive programs to batch-style execution

---

### **Day 8 — Access Evaluator v4 (Validation + JSON + Logging)**

**Focus**
- Input normalization and validation  
- Clean separation between validation and rule evaluation  
- Generating structured JSON output  
- Writing append-only logs with timestamps  
- Producing explainable results (reason + valid fields)

**Built**
- Access Evaluator v4:
- Validates roles and environments before evaluation  
- Normalizes user input (case-insensitive handling)  
- Distinguishes between invalid input, no matching rule, and valid rule matches  
- Produces a consistent JSON schema for all results  
- Appends human-readable logs using portable ASCII (`->`)  
- Includes timestamped audit trails for each evaluation

**Technical Highlights**
- Introduced input validation using sets for O(1) membership checks  
- Added normalized input handling (`role_norm`, `env_norm`)  
- Encapsulated logic into clear branches:
- `invalid_request`
- `no_access`
- rule match  
- Added `valid` boolean flag for downstream filtering  
- Added `reason` field for explainability (critical in real-world automation tools)  
- Implemented UTF-8-safe logging  
- Ensured consistent JSON output via list of structured dictionaries

**Why This Matters**
This is the first step where Python moves beyond syntax exercises into
**production-style automation design**.

Evaluator v4 behaves like a simplified IAM/RBAC policy checker:
- validates input early,
- normalizes data,
- explains decision-making,
- logs actions,
- emits machine-readable output.

These skills translate directly to SE work involving Terraform, IAM, CI/CD validation, configuration linting, and log analysis.

**Artifact**
- `day-08-access-evaluator/`
- `evaluator_v4.py` — validation engine + JSON + logging  
- `output.json` — structured evaluation results  
- `log.txt` — append-only audit log  

## Notes
- All scripts are intended to be run directly via the command line
- Scratch files are excluded from commits
- The repo favors execution and iteration over polish
- Each day builds directly on the previous one
