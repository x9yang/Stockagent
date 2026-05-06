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

    def _set_work_style(self):
        self.root.configure(bg="#FFE4E4")
        self.status_label.config(text="工作中", bg="#FFE4E4")
        self.timer_label.config(bg="#FFE4E4")
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg="#FFE4E4")

    def _set_break_style(self):
        self.root.configure(bg="#E4FFE4")
        self.status_label.config(text="休息中", bg="#E4FFE4")
        self.timer_label.config(bg="#E4FFE4")
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg="#E4FFE4")

    def _tick(self):
        if not self.running:
            return
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self._update_display()
            self.after_id = self.root.after(1000, self._tick)
        else:
            self.running = False
            if self.is_work:
                messagebox.showinfo("番茄钟", "时间到！休息一下")
                self.is_work = False
                self.remaining_seconds = BREAK_MINUTES * 60
                self._set_break_style()
            else:
                messagebox.showinfo("番茄钟", "休息结束！开始工作")
                self.is_work = True
                self.remaining_seconds = WORK_MINUTES * 60
                self._set_work_style()
            self._update_display()

    def start(self):
        if not self.running:
            self.running = True
            self._tick()

    def pause(self):
        self.running = False
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None

    def reset(self):
        self.running = False
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.is_work = True
        self.remaining_seconds = WORK_MINUTES * 60
        self._set_work_style()
        self._update_display()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PomodoroApp()
    app.run()
