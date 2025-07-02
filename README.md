# Easy FTO

A simple, cross-platform, command-line tool for tracking Flexible Time Off (FTO) balances over the year.

- **Written in Python 3**
- Works on **Windows**, **macOS**, and **Linux**
- Stores your entries locally in a JSON file
- Fully interactive text-based menu
- No internet required

---

## 📸 Features

✅ Interactive menu—no command-line arguments needed  
✅ Add FTO entries with notes  
✅ View your entire history  
✅ Delete incorrect entries  
✅ Reset data for a new year  
✅ Set a custom annual goal  

---

## ⚙️ Prerequisites

- Python 3 installed

Check with:

```bash
python3 --version
```

If you don't have it installed:

- **macOS**:  
  ```bash
  brew install python
  ```

- **Linux (Debian/Ubuntu):**  
  ```bash
  sudo apt install python3
  ```

- **Windows:**  
  - Download from [python.org](https://www.python.org/downloads/)
  - Check **Add to PATH** during install

---

## 📦 Installation

Clone or download this repo:

```bash
git clone https://github.com/yourusername/easyfto.git
cd easyfto
```

Or simply save **easyfto.py** anywhere you like.

---

## 🚀 How to Run

From the folder where `easyfto.py` is saved, run:

### ✅ macOS / Linux

```bash
python3 easyfto.py
```

### ✅ Windows

```powershell
python easyfto.py
```

---

## 💻 Example Session

```
========================================
           Welcome to Easy FTO
========================================

=== Current Easy FTO Summary ===
Annual Goal: 200.0 hours
Total FTO used: 16.0 hours
Remaining balance: 184.0 hours
============================

Please choose an option:
1) Add new FTO entry
2) View history
3) Delete an entry
4) Reset all data
5) Set annual goal
6) Exit
> 
```

---

## 🗂️ Stored Data

All your entries are saved in **easyfto_data.json** in the same folder.

Example format:

```json
{
  "goal": 200.0,
  "entries": [
    {
      "hours": 8.0,
      "note": "7/2 FedEx delivery"
    },
    {
      "hours": 4.0,
      "note": "Doctor appointment"
    }
  ]
}
```

---

## 🛠️ Features Explained

### Add new FTO entry
Log hours with a note:
```
> 1
Enter hours taken: 8
Enter a note/description: 7/2 FedEx delivery
```

### View history
See all logged entries, total used, and remaining balance.

### Delete an entry
Remove an entry by its number in the history list.

### Reset all data
Clear all entries and start over (for new year).

### Set annual goal
Change the default annual FTO allowance (default is 200 hours).

---

## 🤝 Contributing

- Fork the repo
- Make changes
- Submit a pull request

Suggestions welcome!

---

## 📄 License

MIT License. Free to use and share.