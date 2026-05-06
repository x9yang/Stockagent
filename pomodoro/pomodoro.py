"""极简桌面番茄钟 - 25分钟工作 + 5分钟休息"""
import tkinter as tk
from tkinter import messagebox

WORK_MINUTES = 25
BREAK_MINUTES = 5


class PomodoroApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("番茄钟")
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        self.root.configure(bg="#FFE4E4")

        self.remaining_seconds = WORK_MINUTES * 60
        self.running = False
        self.is_work = True
        self.after_id = None

        self._build_ui()
        self._center_window()

    def _build_ui(self):
        self.status_label = tk.Label(
            self.root, text="工作中", font=("Microsoft YaHei", 14),
            bg="#FFE4E4", fg="#333333"
        )
        self.status_label.pack(pady=(30, 10))

        self.timer_label = tk.Label(
            self.root, text="25 : 00", font=("Consolas", 48),
            bg="#FFE4E4", fg="#333333"
        )
        self.timer_label.pack(pady=10)

        btn_frame = tk.Frame(self.root, bg="#FFE4E4")
        btn_frame.pack(pady=20)

        self.start_btn = tk.Button(
            btn_frame, text="开始", command=self.start,
            width=8, font=("Microsoft YaHei", 10)
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.pause_btn = tk.Button(
            btn_frame, text="暂停", command=self.pause,
            width=8, font=("Microsoft YaHei", 10)
        )
        self.pause_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = tk.Button(
            btn_frame, text="重置", command=self.reset,
            width=8, font=("Microsoft YaHei", 10)
        )
        self.reset_btn.pack(side=tk.LEFT, padx=5)

    def _center_window(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"+{x}+{y}")

    def _update_display(self):
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        self.timer_label.config(text=f"{minutes:02} : {seconds:02}")

    def _tick(self):
        pass

    def start(self):
        pass

    def pause(self):
        pass

    def reset(self):
        pass

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PomodoroApp()
    app.run()
