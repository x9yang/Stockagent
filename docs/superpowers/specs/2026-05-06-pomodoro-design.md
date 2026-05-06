# Pomodoro Timer Design Spec

## Overview

极简桌面番茄钟，Python + tkinter 实现，单文件应用。放在项目根目录新建的 `pomodoro/` 文件夹内。

## Tech Stack

- Python 3.x（标准库即可）
- tkinter（Python 自带 GUI 库）
- 无第三方依赖

## File Structure

```
pomodoro/
├── pomodoro.py    # 主程序 (~130 行)
└── README.md      # 使用说明
```

## UI Layout

```
┌─────────────────────────┐
│      番茄钟              │
│                         │
│   ┌─────────────────┐   │
│   │   工作中/休息中    │   │   ← 状态标签 (Label)
│   └─────────────────┘   │
│                         │
│   ╔═════════════════╗   │
│   ║    25 : 00      ║   │   ← 大号计时器 (Label, 等宽字体)
│   ╚═════════════════╝   │
│                         │
│  [开始] [暂停] [重置]   │   ← 三个按钮 (Button)
│                         │
└─────────────────────────┘
```

- 窗口固定大小 300×250，居中屏幕
- 工作中：浅红背景 (#FFE4E4)
- 休息中：浅绿背景 (#E4FFE4)
- 计时器字体：等宽，size 48

## Behavior State Machine

```
         [开始]
           ↓
     ╔═══════════╗
     ║  工作中    ║  ← 25:00 倒计时，红底
     ╚══════╤════╝
            │ 到 00:00 → messagebox "时间到！休息一下"
            ↓
     ╔═══════════╗
     ║  休息中    ║  ← 5:00 倒计时，绿底
     ╚══════╤════╝
            │ 到 00:00 → messagebox "休息结束！开始工作"
            ↓
         (回到工作中)
```

**按钮行为：**
- 开始：从当前剩余秒数继续倒计时（用 `after(1000, ...)` 每秒更新）
- 暂停：取消 `after`，保留 `remaining_seconds`
- 重置：`remaining_seconds = 25 * 60`，状态回到"工作中"，停止倒计时

**状态变量：**
- `remaining_seconds`: int，当前剩余秒数
- `running`: bool，计时器是否在运行
- `is_work`: bool，当前是工作还是休息
- `after_id`: str，用于取消定时器

## Implementation Notes

- 全在一个 `PomodoroApp` 类中
- `__init__`: 创建 UI 组件
- `_update_display()`: 把秒数格式化成 "MM : SS" 更新 Label
- `_tick()`: 每秒减 1，到 0 触发切换
- `start()`, `pause()`, `reset()`: 按钮回调
- `messagebox.showinfo()` 弹提醒
- 窗口 title 设置 "番茄钟"
