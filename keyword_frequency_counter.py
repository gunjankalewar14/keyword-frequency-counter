"""Interactive keyword frequency counter using a hash table and JSON storage."""

import json
import re
from pathlib import Path

DATA_FILE = Path(__file__).with_name("keyword_frequencies.json")


def count_words(text):
    """Return a hash table mapping normalized words to their counts in text."""
    frequencies = {}
    words = re.findall(r"[\w']+", text.casefold())
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def load_frequencies():
    """Load accumulated counts from JSON, or start with an empty hash table."""
    if not DATA_FILE.exists():
        save_frequencies({})
        return {}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            frequencies = json.load(file)
        if not isinstance(frequencies, dict) or not all(
            isinstance(word, str)
            and isinstance(count, int)
            and count >= 0
            for word, count in frequencies.items()
        ):
            raise ValueError("The JSON file must contain word counts.")
        return frequencies
    except (json.JSONDecodeError, ValueError) as error:
        print(f"Could not read saved frequencies ({error}). Starting with an empty table.")
        return {}


def save_frequencies(frequencies):
    """Save the hash table to JSON."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(frequencies, file, indent=2, ensure_ascii=False, sort_keys=True)
        file.write("\n")


def show_menu():
    print("\n--- Keyword Frequency Counter ---")
    print("1. Enter text and count its words")
    print("2. Show saved word frequencies")
    print("3. Exit")


def main():
    frequencies = load_frequencies()
    if frequencies:
        print(f"Loaded saved word frequencies from {DATA_FILE.name}.")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            text = input("Enter text: ").strip()
            if not text:
                print("Please enter some text.")
                continue

            new_counts = count_words(text)
            for word, count in new_counts.items():
                frequencies[word] = frequencies.get(word, 0) + count
            save_frequencies(frequencies)
            print("Word counts added and saved:")
            for word in sorted(new_counts):
                print(f"{word}: {new_counts[word]}")

        elif choice == "2":
            if frequencies:
                print("Saved word frequencies:")
                for word in sorted(frequencies):
                    print(f"{word}: {frequencies[word]}")
            else:
                print("No words have been counted yet.")

        elif choice == "3":
            print("Exiting. Your word frequencies are saved in keyword_frequencies.json.")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
