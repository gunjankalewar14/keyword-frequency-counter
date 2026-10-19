# Keyword Frequency Counter Using a Hash Table

An interactive Python program that counts words in text using a hash table (Python dictionary). Counts are saved in JSON and accumulate across runs.

## Requirements

- Python 3 (no extra packages needed)

## Run it

Open this folder in VS Code. In the VS Code terminal, run:

```bash
python3 keyword_frequency_counter.py
```

Choose an option:

1. **Enter text and count its words** adds each word's frequency to the saved totals.
2. **Show saved word frequencies** displays all accumulated totals.
3. **Exit** closes the program. Counts are saved after each text entry.

Words are case-insensitive and punctuation is ignored. For example, `Python` and `python` are counted as the same word.

## JSON storage

The `keyword_frequencies.json` file is stored beside the Python program. It contains a JSON object, for example:

```json
{
  "fun": 2,
  "python": 3
}
```

The program creates the file if it is missing. Avoid editing it while the program is running. If it contains invalid JSON or data in the wrong format, the program reports the problem and starts with an empty table.

## How the hash table works

The program uses a Python dictionary as its hash table. For each word, it checks the dictionary: if the word is already present, its count increases; otherwise, a new entry starts at one. Counting a text is typically O(n) for n words.
