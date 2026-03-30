"""
Display / UI Module
--------------------
Handles all terminal output using the `rich` library for a modern,
colorful, and well-structured interface.

All styling, tables, panels, and prompts are defined here.
"""

import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.align import Align
from rich.prompt import Prompt, IntPrompt
from rich.rule import Rule
from rich.padding import Padding
from rich import box
from rich.style import Style
from rich.progress import Progress, SpinnerColumn, TextColumn
import time

# ─── Global Console ─────────────────────────────────────────────────────────
console = Console()

# ─── Color Palette ──────────────────────────────────────────────────────────
COLORS = {
    "primary":    "#7C3AED",   # vivid violet
    "secondary":  "#06B6D4",   # cyan
    "accent":     "#F59E0B",   # amber
    "success":    "#10B981",   # emerald
    "danger":     "#EF4444",   # red
    "warning":    "#F97316",   # orange
    "muted":      "#6B7280",   # gray
    "bg_dark":    "#1E1B4B",   # deep indigo
    "text_light": "#E0E7FF",   # light indigo-white
    "hit":        "#059669",   # dark green
    "fault":      "#DC2626",   # dark red
    "empty":      "#374151",   # dark gray
}

# Algorithm info: name, icon, description, color
ALGO_INFO = {
    "FIFO": {
        "icon": "⏳",
        "color": "#60A5FA",  # blue-400
        "desc": "First-In, First-Out — Evicts the oldest page in memory",
        "abbr": "FIFO",
    },
    "LRU": {
        "icon": "🕐",
        "color": "#34D399",  # emerald-400
        "desc": "Least Recently Used — Evicts the page unused for longest time",
        "abbr": "LRU",
    },
    "MRU": {
        "icon": "🔥",
        "color": "#F59E0B",  # amber-400
        "desc": "Most Recently Used — Evicts the most recently accessed page",
        "abbr": "MRU",
    },
    "OPTIMAL": {
        "icon": "🎯",
        "color": "#A78BFA",  # violet-400
        "desc": "Optimal (Bélády's) — Evicts page used furthest in the future",
        "abbr": "OPT",
    },
    "SECOND CHANCE": {
        "icon": "🔄",
        "color": "#FB923C",  # orange-400
        "desc": "Second Chance (Clock) — FIFO with a reference bit grace period",
        "abbr": "2ND",
    },
}

GROUP_MEMBERS = [
    "Cabutihan, Shawn Uriel S.",
    "Centeno, Laurenzo S.",
    "Garcia, Seane Karl S.",
    "Pangilinan, Justin Neri A.",
    "Villapaña, Neriah Faith L.",
]

COURSE = "OPSYSFUN — Operating Systems Fundamentals"
SECTION = "Final Project: Virtual Paging Algorithm Simulation"
SCHOOL  = "Holy Angel University — College of Computer Studies"


# ─────────────────────────────────────────────────────────────────────────────
# BANNER
# ─────────────────────────────────────────────────────────────────────────────

def print_banner():
    """Print the full welcome banner with group info."""
    console.print()

    # ASCII art header
    art_lines = [
        "  ██████╗  █████╗  ██████╗ ██╗███╗   ██╗ ██████╗ ",
        "  ██╔══██╗██╔══██╗██╔════╝ ██║████╗  ██║██╔════╝ ",
        "  ██████╔╝███████║██║  ███╗██║██╔██╗ ██║██║  ███╗",
        "  ██╔═══╝ ██╔══██║██║   ██║██║██║╚██╗██║██║   ██║",
        "  ██║     ██║  ██║╚██████╔╝██║██║ ╚████║╚██████╔╝",
        "  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ",
    ]
    art_sub = [
        "  ██████╗ ███████╗██████╗ ██╗      █████╗  ██████╗███████╗███╗   ███╗███████╗███╗   ██╗████████╗",
        "  ██╔══██╗██╔════╝██╔══██╗██║     ██╔══██╗██╔════╝██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝",
        "  ██████╔╝█████╗  ██████╔╝██║     ███████║██║     █████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   ",
        "  ██╔══██╗██╔══╝  ██╔═══╝ ██║     ██╔══██║██║     ██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ",
        "  ██║  ██║███████╗██║     ███████╗██║  ██║╚██████╗███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ",
        "  ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ",
    ]

    # Title panel
    title_text = Text(justify="center")
    title_text.append("  VIRTUAL MEMORY  ", style=f"bold {COLORS['primary']} on #1E1B4B")
    title_text.append(" PAGE REPLACEMENT ", style=f"bold {COLORS['secondary']} on #1E1B4B")
    title_text.append("SIMULATOR  \n", style=f"bold {COLORS['accent']} on #1E1B4B")
    title_text.append("  FIFO  •  LRU  •  MRU  •  OPTIMAL  •  SECOND CHANCE  ",
                       style=f"italic {COLORS['text_light']}")

    console.print(
        Panel(
            Align.center(title_text),
            border_style=f"bold {COLORS['primary']}",
            padding=(1, 4),
            box=box.DOUBLE_EDGE,
        )
    )
    console.print()

    # Group info table
    info_table = Table(
        box=box.ROUNDED,
        border_style=COLORS["secondary"],
        show_header=False,
        padding=(0, 2),
        expand=False,
    )
    info_table.add_column("Label", style=f"bold {COLORS['accent']}", no_wrap=True)
    info_table.add_column("Value", style=COLORS["text_light"])

    info_table.add_row("📚  Course", COURSE)
    info_table.add_row("🎓  Project", SECTION)
    info_table.add_row("🏫  School", SCHOOL)
    info_table.add_row("", "")
    for i, member in enumerate(GROUP_MEMBERS, 1):
        icon = "👤" if i > 1 else "👥"
        label = f"{icon}  Member {i}" if i > 1 else f"{icon}  Members"
        info_table.add_row(label, member)

    console.print(Align.center(info_table))
    console.print()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────────────────────────────────────

def print_main_menu():
    """Print the algorithm selection menu."""
    console.print(Rule(f"[bold {COLORS['primary']}]  ALGORITHM SELECTION  ", style=COLORS["primary"]))
    console.print()

    algo_panels = []
    menu_items = list(ALGO_INFO.items())

    for idx, (key, info) in enumerate(menu_items, 1):
        content = Text()
        content.append(f"  {info['icon']}  ", style="bold")
        content.append(f"{key}\n", style=f"bold {info['color']}")
        content.append(f"  {info['desc']}\n", style=f"dim {COLORS['text_light']}")

        panel = Panel(
            content,
            title=f"[bold white] [{idx}] [/bold white]",
            title_align="left",
            border_style=info["color"],
            padding=(0, 1),
            width=42,
        )
        algo_panels.append(panel)

    # Compare All option
    compare_content = Text()
    compare_content.append("  📊  ", style="bold")
    compare_content.append("RUN ALL & COMPARE\n", style=f"bold {COLORS['accent']}")
    compare_content.append("  Simulate all algorithms with the same\n  input and display a comparison table",
                           style=f"dim {COLORS['text_light']}")
    algo_panels.append(
        Panel(
            compare_content,
            title=f"[bold white] [6] [/bold white]",
            title_align="left",
            border_style=COLORS["accent"],
            padding=(0, 1),
            width=42,
        )
    )

    # Exit option
    exit_content = Text()
    exit_content.append("  🚪  ", style="bold")
    exit_content.append("EXIT\n", style=f"bold {COLORS['danger']}")
    exit_content.append("  Quit the simulation", style=f"dim {COLORS['muted']}")
    algo_panels.append(
        Panel(
            exit_content,
            title=f"[bold white] [0] [/bold white]",
            title_align="left",
            border_style=COLORS["danger"],
            padding=(0, 1),
            width=42,
        )
    )

    # Print in rows of 2
    for i in range(0, len(algo_panels), 2):
        row = algo_panels[i: i + 2]
        console.print(Columns(row, equal=False, expand=False, padding=(0, 1)))

    console.print()


# ─────────────────────────────────────────────────────────────────────────────
# INPUT PROMPTS
# ─────────────────────────────────────────────────────────────────────────────

def prompt_algorithm_choice() -> int:
    """Prompt user to choose an algorithm. Returns 0-6."""
    while True:
        choice = Prompt.ask(
            f"[bold {COLORS['secondary']}]  ❯  Enter choice",
            default="1",
        )
        if choice.strip() in {"0", "1", "2", "3", "4", "5", "6"}:
            return int(choice.strip())
        console.print(f"  [bold {COLORS['danger']}]Invalid choice. Enter 0–6.[/]")


def prompt_simulation_inputs() -> tuple:
    """
    Prompt user for number of frames and reference string.
    Returns (num_frames: int, reference_string: list[int])
    """
    console.print()
    console.print(Rule(f"[bold {COLORS['secondary']}]  SIMULATION INPUTS  ", style=COLORS["secondary"]))
    console.print()

    # Number of frames
    while True:
        try:
            frames_input = Prompt.ask(
                f"  [bold {COLORS['accent']}]🖼  Number of Frames[/] [dim](e.g. 3)[/]",
            )
            num_frames = int(frames_input.strip())
            if num_frames < 1:
                console.print(f"  [bold {COLORS['danger']}]Frames must be ≥ 1.[/]")
                continue
            if num_frames > 10:
                console.print(f"  [bold {COLORS['warning']}]⚠ Large frame count may produce very wide tables.[/]")
            break
        except ValueError:
            console.print(f"  [bold {COLORS['danger']}]Please enter a valid integer.[/]")

    # Reference string
    while True:
        ref_input = Prompt.ask(
            f"  [bold {COLORS['accent']}]📋  Reference String[/] [dim](space-separated, e.g. 7 0 1 2 0 3  or  A B C D)[/]",
        )
        tokens = ref_input.strip().split()
        if len(tokens) < 1:
            console.print(f"  [bold {COLORS['danger']}]Reference string cannot be empty.[/]")
            continue
        # Accept both numbers and strings: convert to int if possible, else keep as string
        ref_string = []
        for token in tokens:
            try:
                ref_string.append(int(token))
            except ValueError:
                ref_string.append(token)
        if len(ref_string) > 50:
            console.print(f"  [bold {COLORS['warning']}]⚠ Long strings (>50) may produce very wide tables.[/]")
        break

    console.print()
    return num_frames, ref_string


# ─────────────────────────────────────────────────────────────────────────────
# SIMULATION RESULTS
# ─────────────────────────────────────────────────────────────────────────────

def _make_label(page, is_fault: bool) -> Text:
    """Create a colored cell text for a page value."""
    if page is None:
        t = Text("  —  ", style=COLORS["empty"], justify="center")
    elif is_fault:
        t = Text(f"  {page}  ", style=f"bold white on {COLORS['fault']}", justify="center")
    else:
        t = Text(f"  {page}  ", style=f"bold white on {COLORS['hit']}", justify="center")
    return t


def print_simulation_results(result: dict):
    """Render full simulation results: header, step table, and summary."""
    algo = result["algorithm"]
    info = ALGO_INFO.get(algo, {"icon": "📄", "color": COLORS["primary"], "desc": ""})
    ref_str = result["reference_string"]
    num_frames = result["num_frames"]
    frames_history = result["frames_history"]
    fault_flags = result["fault_flags"]
    evicted = result["evicted_pages"]
    has_ref_bits = "ref_bits_history" in result

    console.print()
    console.print(Rule(
        f"[bold {info['color']}]  {info['icon']}  {algo} — Simulation Results  ",
        style=info["color"],
    ))
    console.print()

    # ── Input summary ────────────────────────────────────────────────────────
    summary_text = Text()
    summary_text.append("  Frames: ", style=f"bold {COLORS['accent']}")
    summary_text.append(str(num_frames), style=f"bold white")
    summary_text.append("     Reference String: ", style=f"bold {COLORS['accent']}")
    summary_text.append(" ".join(str(p) for p in ref_str), style=f"bold {COLORS['secondary']}")
    summary_text.append(f"     Length: {len(ref_str)}", style=f"dim {COLORS['muted']}")
    console.print(Padding(summary_text, (0, 2)))
    console.print()

    # ── Step-by-step table ───────────────────────────────────────────────────
    # Limit columns for readability; if too long, show in chunks of 25
    CHUNK = 25
    n = len(ref_str)
    chunks = [range(i, min(i + CHUNK, n)) for i in range(0, n, CHUNK)]

    for chunk_idx, chunk_range in enumerate(chunks):
        if len(chunks) > 1:
            console.print(
                f"  [dim {COLORS['muted']}]Steps {chunk_range.start + 1}–{chunk_range.stop}[/]"
            )

        tbl = Table(
            box=box.SIMPLE_HEAD,
            border_style=info["color"],
            show_edge=True,
            padding=(0, 0),
            expand=False,
        )

        # Headers: Step row label + step numbers
        tbl.add_column(
            Text("Frame / Step", style=f"bold {COLORS['accent']}", justify="center"),
            style="bold",
            no_wrap=True,
            width=14,
        )
        for step_i in chunk_range:
            page = ref_str[step_i]
            header_text = Text(str(page), justify="center")
            if fault_flags[step_i]:
                header_text.stylize(f"bold {COLORS['fault']}")
            else:
                header_text.stylize(f"bold {COLORS['hit']}")
            tbl.add_column(header_text, justify="center", width=5, no_wrap=True)

        # Frame rows
        for frame_idx in range(num_frames):
            row_label = Text(f"  Frame {frame_idx + 1}  ", style=f"bold {COLORS['text_light']}", justify="left")
            row_cells = [row_label]
            for step_i in chunk_range:
                page_val = frames_history[step_i][frame_idx]
                is_fault = fault_flags[step_i]
                cell = _make_label(page_val, is_fault)
                row_cells.append(cell)
            tbl.add_row(*row_cells)

        # Reference bit row (Second Chance only)
        if has_ref_bits:
            ref_bits_hist = result["ref_bits_history"]
            rb_label = Text("  Ref Bit  ", style=f"bold {COLORS['warning']}", justify="left")
            rb_cells = [rb_label]
            for step_i in chunk_range:
                bits = ref_bits_hist[step_i]
                bits_str = "/".join(str(b) for b in bits)
                rb_cells.append(Text(bits_str, style=f"{COLORS['warning']}", justify="center"))
            tbl.add_row(*rb_cells)

        # Fault / Hit row
        status_label = Text("  Status  ", style=f"bold {COLORS['muted']}", justify="left")
        status_cells = [status_label]
        for step_i in chunk_range:
            if fault_flags[step_i]:
                status_cells.append(Text("FAULT", style=f"bold {COLORS['fault']}", justify="center"))
            else:
                status_cells.append(Text("HIT", style=f"bold {COLORS['hit']}", justify="center"))
        tbl.add_row(*status_cells)

        # Evicted row
        evict_label = Text("  Evicted  ", style=f"bold {COLORS['muted']}", justify="left")
        evict_cells = [evict_label]
        for step_i in chunk_range:
            ev = evicted[step_i]
            if ev is not None:
                evict_cells.append(Text(str(ev), style=f"bold {COLORS['warning']}", justify="center"))
            else:
                evict_cells.append(Text("—", style=f"dim {COLORS['muted']}", justify="center"))
        tbl.add_row(*evict_cells)

        console.print(Padding(tbl, (0, 2)))
        console.print()

    # ── Legend ───────────────────────────────────────────────────────────────
    legend = Text()
    legend.append("  Legend:  ", style=f"bold {COLORS['muted']}")
    legend.append("  FAULT  ", style=f"bold white on {COLORS['fault']}")
    legend.append(" = Page Fault (miss)   ", style=COLORS["muted"])
    legend.append("  HIT  ", style=f"bold white on {COLORS['hit']}")
    legend.append(" = Page Hit   ", style=COLORS["muted"])
    legend.append("  —  ", style=f"{COLORS['empty']}")
    legend.append(" = Empty Frame", style=COLORS["muted"])
    console.print(legend)
    console.print()

    # ── Statistics panel ─────────────────────────────────────────────────────
    _print_stats_panel(result, info)
    console.print()


def _print_stats_panel(result: dict, info: dict):
    """Print a styled statistics summary panel."""
    total = len(result["reference_string"])
    faults = result["total_faults"]
    hits = result["total_hits"]
    fault_rate = result["fault_rate"]
    hit_rate = result["hit_rate"]

    # Build stats grid
    stats_table = Table(
        box=box.SIMPLE,
        show_header=False,
        padding=(0, 3),
        expand=False,
        border_style=info["color"],
    )
    stats_table.add_column("Metric", style=f"bold {COLORS['accent']}", no_wrap=True)
    stats_table.add_column("Value", style="bold white", justify="right")
    stats_table.add_column("Bar", no_wrap=True)

    def _bar(pct: float, color: str, width: int = 20) -> Text:
        filled = int(pct / 100 * width)
        bar = Text()
        bar.append("█" * filled, style=f"bold {color}")
        bar.append("░" * (width - filled), style=COLORS["empty"])
        bar.append(f"  {pct:.1f}%", style=f"{color}")
        return bar

    stats_table.add_row(
        "  📄  Total References",
        str(total),
        Text(""),
    )
    stats_table.add_row(
        "  ❌  Page Faults",
        f"[bold {COLORS['fault']}]{faults}[/]",
        _bar(fault_rate, COLORS["danger"]),
    )
    stats_table.add_row(
        "  ✅  Page Hits",
        f"[bold {COLORS['hit']}]{hits}[/]",
        _bar(hit_rate, COLORS["success"]),
    )
    stats_table.add_row(
        "  📊  Fault Rate",
        f"[bold {COLORS['danger']}]{fault_rate}%[/]",
        Text(""),
    )
    stats_table.add_row(
        "  📈  Hit Rate",
        f"[bold {COLORS['success']}]{hit_rate}%[/]",
        Text(""),
    )

    panel = Panel(
        Align.center(stats_table),
        title=f"[bold {info['color']}]  {info['icon']}  {result['algorithm']}  — Statistics  ",
        border_style=info["color"],
        padding=(1, 2),
        box=box.ROUNDED,
    )
    console.print(Padding(panel, (0, 2)))


# ─────────────────────────────────────────────────────────────────────────────
# COMPARISON TABLE
# ─────────────────────────────────────────────────────────────────────────────

def print_comparison_table(results: list):
    """Print a side-by-side comparison of multiple algorithm results."""
    if not results:
        return

    console.print()
    console.print(Rule(
        f"[bold {COLORS['accent']}]  📊  ALL ALGORITHMS — COMPARISON  ",
        style=COLORS["accent"],
    ))
    console.print()

    tbl = Table(
        title="Page Replacement Algorithm Comparison",
        title_style=f"bold {COLORS['accent']}",
        box=box.DOUBLE_EDGE,
        border_style=COLORS["primary"],
        show_lines=True,
        padding=(0, 2),
        header_style=f"bold {COLORS['text_light']} on {COLORS['bg_dark']}",
    )

    tbl.add_column("Metric", style=f"bold {COLORS['accent']}", no_wrap=True, width=22)

    algo_colors = []
    for r in results:
        algo = r["algorithm"]
        info = ALGO_INFO.get(algo, {"icon": "📄", "color": COLORS["primary"]})
        tbl.add_column(
            f"{info['icon']} {algo}",
            justify="center",
            style=info["color"],
            width=18,
        )
        algo_colors.append(info["color"])

    # Rows
    tbl.add_row("Total References", *[str(len(r["reference_string"])) for r in results])
    tbl.add_row("Number of Frames", *[str(r["num_frames"]) for r in results])
    tbl.add_row(
        "Page Faults",
        *[f"[bold {COLORS['fault']}]{r['total_faults']}[/]" for r in results],
    )
    tbl.add_row(
        "Page Hits",
        *[f"[bold {COLORS['hit']}]{r['total_hits']}[/]" for r in results],
    )
    tbl.add_row(
        "Fault Rate",
        *[f"[bold {COLORS['danger']}]{r['fault_rate']}%[/]" for r in results],
    )
    tbl.add_row(
        "Hit Rate",
        *[f"[bold {COLORS['success']}]{r['hit_rate']}%[/]" for r in results],
    )

    # Best algorithm (fewest faults)
    min_faults = min(r["total_faults"] for r in results)
    best = [r["algorithm"] for r in results if r["total_faults"] == min_faults]
    best_str = " & ".join(best)
    tbl.add_row(
        "🏆 Best Performer",
        *[
            (f"[bold {COLORS['accent']}]★ BEST[/]"
             if r["algorithm"] in best else f"[dim {COLORS['muted']}]—[/]")
            for r in results
        ],
    )

    console.print(Align.center(tbl))
    console.print()

    # Best performer callout
    console.print(
        Panel(
            f"  [bold {COLORS['accent']}]🏆  Best Performer:[/]  "
            f"[bold white]{best_str}[/]  with only  "
            f"[bold {COLORS['success']}]{min_faults}[/] page fault(s).",
            border_style=COLORS["accent"],
            box=box.ROUNDED,
            padding=(0, 2),
        )
    )
    console.print()


# ─────────────────────────────────────────────────────────────────────────────
# GOODBYE
# ─────────────────────────────────────────────────────────────────────────────

def print_goodbye():
    """Print goodbye message."""
    console.print()
    console.print(
        Panel(
            Align.center(
                Text(
                    "\n  Thanks for using the Virtual Paging Simulator!  \n"
                    "         Holy Angel University — OPSYSFUN         \n",
                    style=f"bold {COLORS['text_light']}",
                    justify="center",
                )
            ),
            border_style=COLORS["primary"],
            box=box.DOUBLE_EDGE,
            padding=(1, 4),
        )
    )
    console.print()
