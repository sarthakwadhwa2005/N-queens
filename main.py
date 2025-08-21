import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class NQueensSolverGUI:
    def __init__(self, master):
        self.master = master
        master.title("N-Queens Solver")

        self.create_disclaimer_popup()
        self.create_widgets()

    def create_disclaimer_popup(self):
        disclaimer_text = (
            "N-Queens Solver GUI\n\n"
            "Disclaimer:\n"
            "A Python program that tackles the classic N-Queens problem..."
'''A Python program that tackles the classic N-Queens problem.
This project aims to find a solution for placing N chess queens on an N×N chessboard
in a way that no two queens threaten each other. This program provides a solution for various board sizes.
It Looks into account the Space and Time Complexity and Shows the most Ideal Solution as the First output
Group Members:
                Shashwat Solanki
                Sarthak Garg
                Shrish Singh Thakur
                Sarthak Dhamija
                Sarthak Wadhwa'''        )
        messagebox.showinfo("Disclaimer", disclaimer_text)

    def create_widgets(self):
        # Load the background image
        background_image = self.load_resized_image("D:\codes\python\project\quennbg.jpg", (600, 1080))
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label for the background image
        background_label = ttk.Label(self.master, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Helvetica', 12))
        style.configure("TLabel", font=('Helvetica', 12))

        self.size_label = ttk.Label(self.master, text="Enter the size of the chessboard (N):")
        self.size_label.pack(pady=10)

        self.size_entry = ttk.Entry(self.master, font=('Helvetica', 12))
        self.size_entry.pack(pady=5)

        self.solve_button = ttk.Button(self.master, text="Solve", command=self.solve_n_queens)
        self.solve_button.pack(pady=10)

        self.solution_count_label = ttk.Label(self.master, text="")
        self.solution_count_label.pack(pady=10)

        self.canvas_frame = ttk.Frame(self.master)
        self.canvas_frame.pack(pady=10)

        self.canvas = tk.Canvas(self.canvas_frame, bg="black", highlightthickness=0)
        self.canvas.pack()

        # Bind the click event on the canvas
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # # Adding an attractive title image
        # title_image = self.load_resized_image("D:\Codes-_-\Python Mini project\queen.png", (50, 50))
        # self.title_icon = ImageTk.PhotoImage(title_image)
        # title_label = ttk.Label(self.master, image=self.title_icon)
        # title_label.image = self.title_icon
        # title_label.pack()

    def load_resized_image(self, path, size):
        image = Image.open(path)
        image = image.resize(size, Image.LANCZOS)
        return image

    def print_solution(self, board):
        image = self.create_chessboard_image(board)
        self.canvas.config(width=image.width, height=image.height)
        tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image

    def on_canvas_click(self, event):
        # Get the square size and clicked row and column
        square_size = 50
        col = event.x // square_size
        row = event.y // square_size

        # Highlight possible positions and display the number of possibilities
        self.highlight_possible_positions(row, col)
        
    def highlight_possible_positions(self, row, col):
        n = int(self.size_entry.get())
        if n <= 0:
            return

        # Create an empty board
        board = [[0] * n for _ in range(n)]

        # Highlight the selected box
        image = self.create_chessboard_image(board)
        draw = ImageDraw.Draw(image)
        square_size = image.width // n
        draw.rectangle(
            [col * square_size, row * square_size, (col + 1) * square_size, (row + 1) * square_size],
            outline="blue", width=3
        )

        # Count and display the number of possibilities
        count = self.count_n_queens_possibilities(board, row, col)
        self.solution_count_label.config(text=f"Number of Possibilities: {count}")

        # Display the highlighted board
        tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image

    def count_n_queens_possibilities(self, board, row, col):
        n = len(board)
        count = 0

        # Iterate through each column in the selected row
        for j in range(n):
            if self.is_safe(board, row, j, n):
                temp_board = [row[:] for row in board]  # Create a copy of the board
                temp_board[row][j] = 1  # Place a queen in the selected block
                count += self.count_n_queens_solutions(temp_board, row + 1, n)

        return count

    def count_n_queens_solutions(self, board, row, n):
        if row == n:
            return 1

        count = 0
        for col in range(n):
            if self.is_safe(board, row, col, n):
                board[row][col] = 1
                count += self.count_n_queens_solutions(board, row + 1, n)
                board[row][col] = 0

        return count

    def is_safe(self, board, row, col, n):
        for i in range(row):
            if board[i][col]:
                return False

            if col - (row - i) >= 0 and board[i][col - (row - i)]:
                return False

            if col + (row - i) < n and board[i][col + (row - i)]:
                return False

        return True

    def solve_n_queens_util(self, board, row, n, count):
        if row == n:
            self.print_solution(board)
            count[0] += 1
            return True

        res = False
        for col in range(n):
            if self.is_safe(board, row, col, n):
                board[row][col] = 1
                res = self.solve_n_queens_util(board, row + 1, n, count) or res
                board[row][col] = 0

        return res

    def solve_n_queens(self):
        try:
            n = int(self.size_entry.get())
            if n <= 0:
                raise ValueError("Size of the chessboard must be a positive integer.")

            board = [[0] * n for _ in range(n)]
            count = [0]
            success = self.solve_n_queens_util(board, 0, n, count)

            if not success:
                messagebox.showinfo("Solution", "No solution found for the given size.")
            else:
                self.solution_count_label.config(text=f"Number of Solutions: {count[0]}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_chessboard_image(self, board):
        square_size = 50
        image_size = len(board) * square_size
        image = Image.new("RGB", (image_size, image_size), "white")
        draw = ImageDraw.Draw(image)

        for i in range(len(board)):
            for j in range(len(board[i])):
                color = "white" if (i + j) % 2 == 0 else "#D2B48C"
                draw.rectangle(
                    [j * square_size, i * square_size, (j + 1) * square_size, (i + 1) * square_size],
                    fill=color
                )

                if board[i][j]:
                    draw.text(
                        ((j + 0.5) * square_size, (i + 0.5) * square_size),
                        "Q",
                        fill="blue",
                        font=ImageFont.load_default()
                    )

        return image


if __name__ == "__main__":
    root = tk.Tk()
    app = NQueensSolverGUI(root)
    root.geometry("600x600")  # Set initial window size
    root.resizable(False, True)  # Disable window resizing
    root.mainloop()