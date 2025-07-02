#!/usr/bin/env python3

import json
import os

DATA_FILE = "easyfto_data.json"
DEFAULT_GOAL = 200.0

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"goal": DEFAULT_GOAL, "entries": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 40)
    print("           Welcome to Easy FTO")
    print("=" * 40)

def show_summary(data):
    total = sum(entry["hours"] for entry in data["entries"])
    remaining = data["goal"] - total
    print("\n=== Current Easy FTO Summary ===")
    print(f"Annual Goal: {data['goal']:.1f} hours")
    print(f"Total FTO used: {total:.1f} hours")
    print(f"Remaining balance: {remaining:.1f} hours")
    print("============================\n")

def add_entry(data):
    try:
        hours = float(input("Enter hours taken: ").strip())
        note = input("Enter a note/description: ").strip()
        data["entries"].append({"hours": hours, "note": note})
        save_data(data)
        print(f"\n✅ Added: {hours} hours — {note}\n")
    except ValueError:
        print("⚠️  Invalid input. Please enter a numeric value.")

def view_history(data):
    if not data["entries"]:
        print("\n(No entries yet.)\n")
        return
    print("\n=== Easy FTO Usage History ===")
    for idx, entry in enumerate(data["entries"], 1):
        print(f"{idx}) {entry['hours']:.1f} hours — {entry['note']}")
    total = sum(entry["hours"] for entry in data["entries"])
    remaining = data["goal"] - total
    print("----------------------------")
    print(f"Total FTO used: {total:.1f} hours")
    print(f"Remaining balance: {remaining:.1f} hours")
    print("============================\n")

def delete_entry(data):
    if not data["entries"]:
        print("\n(No entries to delete.)\n")
        return
    view_history(data)
    try:
        index = int(input("Enter entry number to delete: ").strip())
        if 1 <= index <= len(data["entries"]):
            removed = data["entries"].pop(index - 1)
            save_data(data)
            print(f"\n✅ Deleted: {removed['hours']} hours — {removed['note']}\n")
        else:
            print("⚠️  Invalid entry number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")

def reset_data():
    save_data({"goal": DEFAULT_GOAL, "entries": []})
    print("\n✅ All Easy FTO data has been reset to default.\n")

def set_goal(data):
    try:
        new_goal = float(input("Enter new annual goal (hours): ").strip())
        data["goal"] = new_goal
        save_data(data)
        print(f"\n✅ Annual goal updated to {new_goal} hours.\n")
    except ValueError:
        print("⚠️  Please enter a numeric value.")

def main_menu():
    while True:
        clear_screen()
        data = load_data()
        print_header()
        show_summary(data)

        print("Please choose an option:")
        print("1) Add new FTO entry")
        print("2) View history")
        print("3) Delete an entry")
        print("4) Reset all data")
        print("5) Set annual goal")
        print("6) Exit")

        choice = input("> ").strip()
        if choice == "1":
            add_entry(data)
            input("Press Enter to continue...")
        elif choice == "2":
            view_history(data)
            input("Press Enter to continue...")
        elif choice == "3":
            delete_entry(data)
            input("Press Enter to continue...")
        elif choice == "4":
            confirm = input("Are you sure you want to reset all data? (y/n): ").strip().lower()
            if confirm == "y":
                reset_data()
            input("Press Enter to continue...")
        elif choice == "5":
            set_goal(data)
            input("Press Enter to continue...")
        elif choice == "6":
            print("\nGoodbye!\n")
            break
        else:
            print("\n⚠️  Invalid choice. Please enter a number 1-6.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()