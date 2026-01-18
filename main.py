import json
import os
from datetime import datetime

LOG_FILE = "failure_log.json"


def load_failures():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)


def save_failures(failures):
    with open(LOG_FILE, "w") as f:
        json.dump(failures, f, indent=4)


def record_failure(failures):
    failure_type = input("Enter failure type (INPUT_ERROR / LOGIC_ERROR / STATE_ERROR): ").strip()
    source = input("Enter source (function or operation name): ").strip()
    detail = input("Enter failure description: ").strip()

    failure = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": failure_type,
        "source": source,
        "detail": detail
    }

    failures.append(failure)
    save_failures(failures)
    print("Failure recorded.\n")


def view_failures(failures):
    if not failures:
        print("No failures logged.\n")
        return

    for i, f in enumerate(failures, start=1):
        print(f"{i}. [{f['timestamp']}]")
        print(f"   TYPE   : {f['type']}")
        print(f"   SOURCE : {f['source']}")
        print(f"   DETAIL : {f['detail']}")
        print("-" * 40)
    print()


def analyze_failures(failures):
    if not failures:
        print("No data to analyze.\n")
        return

    summary = {}
    for f in failures:
        summary[f["type"]] = summary.get(f["type"], 0) + 1

    print("Failure Analysis Summary:")
    for failure_type, count in summary.items():
        print(f"{failure_type}: {count}")

    most_common = max(summary, key=summary.get)
    print(f"\nMost common failure type: {most_common}\n")


def menu():
    print("=== FAILURE LOG ENGINE ===")
    print("1. Record a failure")
    print("2. View failures")
    print("3. Analyze failures")
    print("4. Exit")


def main():
    failures = load_failures()

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            record_failure(failures)
        elif choice == "2":
            view_failures(failures)
        elif choice == "3":
            analyze_failures(failures)
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
