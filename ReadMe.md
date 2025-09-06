# 🐠 WikiDive

### A simple command-line tool to search, read, and explore Wikipedia right from your terminal.

---

## 📖 What is WikiDive?

**WikiDive** is a beginner-friendly Python program that lets you:

* Search for topics on Wikipedia 🧠
* View a list of related results 🔍
* Read a short summary of the selected topic 📄
* Open the full article in your web browser if you want to dive deeper 🌐

---

## 🛠️ Requirements

Before running WikiDive, make sure you have:

* Python **3.x** installed ([Download Python](https://www.python.org/downloads/))
* An internet connection 🌐

---

## 📦 Installation

1. **Clone or download this repository**

If you're using Git:

```bash
git clone https://github.com/hassaanabdullah1/wikidive.git
cd wikidive
```

Or just [download the ZIP](https://github.com/hassaanabdullah1/wikidive/archive/refs/heads/main.zip) and extract it.

2. **Install required packages**

Open your terminal/command prompt and run:

```bash
pip install wikipedia requests
```

> `wikipedia` – to fetch article data
> `requests` – to check for internet connection

---

## ▶️ How to Run

Once you're in the project folder, just run the script:

```bash
python main.py
```

You'll see something like:

```
---WikiDive v1.0---
Enter topic to search for:
```

---

## 🧠 How It Works

1. **You enter a topic**
   → The program searches Wikipedia for matches.

2. **You choose from a list of results**
   → You can type the number or the topic name.

3. **You see a summary**
   → A short explanation of the topic.

4. **Optional: Open full article**
   → Type `Y` if you want to open the full article in your browser.

5. **Search again or exit**
   → Choose whether to keep diving or quit.

---

## ❓ Example

```
---WikiDive v1.0---
Enter topic to search for: python

Search results:
1. Python
2. Python (programming language)
3. Python ide
4. Monty Python
...

Select the topic you want to view: 2

'Python (programming language)' summary:

Python is an interpreted, high-level, general-purpose programming language...
```

---

## 🧰 Features

* ✅ Wikipedia topic search
* ✅ Summary preview
* ✅ Open full article in browser
* ✅ Works in any terminal (Linux, Mac, Windows)

---

## 🐞 Troubleshooting

### ❌ *“Page Not Found”*

The selected topic may not have a Wikipedia page — try another one!

### ❌ *“Please connect to the internet!”*

WikiDive needs an internet connection to fetch results.

---

## 📄 License

MIT License.
Feel free to modify, share, and learn from this code!

---

## 💬 Feedback

If you found this helpful or have ideas to improve it, feel free to open an issue or pull request. Learning is better together! 🚀
