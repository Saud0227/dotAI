import tkinter as tk

def main():
    root = tk.Tk()
    cv=tk.Canvas(root)
    cv.pack(fill=tk.BOTH, expand=1)
    root.geometry("300x500+300+300")

    root.mainloop()


if __name__ == "__main__":
    main()
