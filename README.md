# 🐾 Virtual Pet Text Simulator

Welcome to the **Virtual Pet Simulator** — a fun and interactive Python game where you raise your own digital pet through the terminal!  
Feed it, play with it, give it medicine, and watch out for random events that make pet care even more engaging!

Made with 💙 by **Gyanankur Baruah**

---

## ✨ Features

- 🐶 Name your own pet(s)
- 🧸 Feed your pet and give it toys
- 💊 Heal your pet with medicine
- 🐾 Handle multiple pets at once
- 🎲 Random events like getting sick or finding snacks
- 🧠 Easy-to-follow menu system
- ❗ Automatic hunger and happiness changes over time
- 💔 Game over scenarios if your pet becomes too sad, sick, or hungry

---

## 🧠 How It Works

The simulation revolves around **taking care of one or more pets** using a **menu-based loop**. Here's what each feature does:

### 🐕 Pet Attributes:
Each pet has:
- **Happiness**: Ranges from 0 to 100. Increases with play and toys.
- **Hunger**: Ranges from 0 to 100. Increases with time. Feed to lower it.
- **Health**: Ranges from 0 to 100. Decreases if the pet gets sick.

### ⚙️ Actions:
- **Feed**: Reduces hunger but lowers happiness a bit.
- **Play**: Increases happiness but makes the pet slightly hungrier.
- **Give Toy**: Boosts happiness with no side effects.
- **Give Medicine**: Helps the pet recover health.
- **Check Status**: See all current stats for your pet.
- **Switch Pet**: If you’re managing multiple pets, jump between them.

### ⏳ Time Passage:
After every 3 actions, time passes:
- Hunger increases
- Happiness and health decrease slightly

### 🎲 Random Events:
- **Snack Found**: Hunger decreases
- **Caught a Cold**: Health decreases
- **No Event**: Sometimes, nothing happens!

### ☠️ Game Over Conditions:
- Hunger hits 100 → too hungry to survive
- Happiness drops to 0 → too sad to go on
- Health drops to 0 → pet is too sick

---

## 🖥️ How to Use

1. Clone the repository:
2. Run the Python file in your terminal

```bash
git clone https://github.com/Gyanankur23/Virtual-Pet-Text-Simulator-.git
cd Virtual-Pet-Text-Simulator-
python VirtualPetSimulator.py


---

🗂️ File Structure

Virtual-Pet-Text-Simulator-/
│
├── VirtualPetSimulator.py   # Full game code with bonus features
├── README.md                # You're reading it!


---

⚖️ License

Licensed under Gyanankur Baruah.
You are free to use, modify, and share this project with proper credit.


---

🤝 Contributions

Ideas, feedback, and PRs are welcome!
Want to add new features or fix bugs? Fork and go for it!


---

🔗 GitHub Clone Link

https://github.com/Gyanankur23/Virtual-Pet-Text-Simulator-.git


---

Thanks for visiting! Enjoy raising your virtual pet!
Stay playful! 🐾🐶💻

---


