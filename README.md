# 🏢 Elevator Management System (Python Simulation)

A console-based **Elevator Management System** built in Python to simulate the behavior of multiple elevators in a building.

---

## 🚀 Features

- 🛗 **Multiple Elevators** – Simulate any number of elevators and floors.  
- 📞 **Floor Requests** – Request elevators to move between floors.  
- 🚪 **Door Logic** – Must close elevator doors before moving again.  
- ⚙️ **State Tracking** – Elevators transition between:
  - `idle`
  - `moving_up`
  - `moving_down`
  - `doors_open`
- 🧭 **Independent Operation** – Each elevator works independently (manual control).

---

## 💻 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AdityaZala3919/Elevator-Management-System.git
cd Elevator-Management-System
````

### 2️⃣ Run the Program

```bash
python elevator_system.py
```

---

## 🧠 Commands

| Command                                   | Description                 | Example          |
| ----------------------------------------- | --------------------------- | ---------------- |
| `request <elevator_id> <floor> <up/down>` | Request a specific elevator | `request 1 5 up` |
| `close <elevator_id>`                     | Close elevator doors        | `close 1`        |
| `status`                                  | Show elevator status        | `status`         |
| `quit`                                    | Exit the simulation         | `quit`           |

---

## 🧾 Example Output

```
Enter Desired Number of Elevators: 2
Enter total number of floors in the building: 8

=== Elevator Management System — Simulation ===

Available commands:
  request <elevator_id> <floor> <up/down>
  status
  close <elevator_id>
  quit

Enter command: request 1 5 up
Elevator 1 moving from 1 to 5...
Doors Opening: Lift-1
Elevator 1 doors opened at floor 5

Enter command: close 1
Elevator 1 doors closing...
Elevator 1 doors closed at floor 5

Enter command: status
Elevator 1: Floor 5, State: idle
Elevator 2: Floor 1, State: idle
```
---
## 🧑‍💻 Author <br>

**Adityasinh Zala** <br>
AI/ML Engineer | Tech Explorer | Curious Learner   <br>
[GitHub](https://github.com/AdityaZala3919) • [LinkedIn](https://www.linkedin.com/in/adityasinh-zala-1bbb42258/)
---

⭐ *If you found this project interesting, give it a star on GitHub!* <br>
🌐 *Built with ❤️ using Google Gemini SDK and Streamlit.*  
