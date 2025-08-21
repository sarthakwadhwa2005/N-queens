♛ N-Queens Solver GUI (Python + Tkinter)
📌 Overview
The N-Queens Solver GUI is a Python application that visually solves the classic N-Queens problem — placing N queens on an N×N chessboard so that no two queens threaten each other.
Built with Tkinter for the interface and Pillow (PIL) for image handling, it offers an interactive and visual experience of how solutions are generated.

🎯 Features
Interactive GUI using Tkinter.

Dynamic board size — solve for any N × N chessboard.

Real-time visualization of solutions with a chessboard graphic.

Click-based analysis — click on a square to highlight possible placements and calculate the number of valid queen placements from that position.

Solution counter — displays the total number of solutions for the given board size.

Custom background image for an engaging interface.

📸 How It Works
Enter board size (N) in the input box.

Click "Solve" to generate and visualize the solution.

Click on any square to highlight possible moves and see how many solutions start from that position.

🛠 Technologies Used
Python 3

Tkinter – GUI framework

Pillow (PIL) – Image processing

ttk – Themed Tkinter widgets

📂 Project Structure
bash
Copy
Edit
NQueensSolverGUI/
│-- n_queens_solver.py       # Main application file
│-- queenbg.jpg              # Background image
│-- README.md                # Project documentation
🚀 Getting Started
1. Install dependencies:

bash
Copy
Edit
pip install pillow
2. Run the application:

bash
Copy
Edit
python n_queens_solver.py
📚 About the N-Queens Problem
The N-Queens problem is a famous computer science challenge that explores backtracking algorithms. The objective is to place N queens on an N×N chessboard so that no two queens share the same row, column, or diagonal. This project not only finds solutions but also visualizes the process.

👥 Contributors
Shashwat Solanki

Sarthak Garg

Shrish Singh Thakur

Sarthak Dhamija

Sarthak Wadhwa

Do you want me to also add GitHub badges, screenshots, and an animated GIF demo so it looks more professional? That would make the README look much more appealing on GitHub.
