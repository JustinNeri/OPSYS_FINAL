"""
Virtual Paging Algorithm Simulation
=====================================
Holy Angel University — OPSYSFUN (Operating Systems Fundamentals)
Final Project

Group Members:
  • Cabutihan, Shawn Uriel S.
  • Centeno, Laurenzo S.
  • Garcia, Seane Karl S.
  • Pangilinan, Justin Neri A.
  • Villapaña, Neriah Faith L.

Description:
    This program simulates five classical page replacement algorithms:
      1. FIFO         — First-In, First-Out
      2. LRU          — Least Recently Used
      3. MRU          — Most Recently Used
      4. OPTIMAL      — Bélády's Optimal Algorithm
      5. SECOND CHANCE — Clock Algorithm (FIFO with Reference Bits)

    The user can select an algorithm, enter the number of frames and
    a page reference string, and view a detailed step-by-step simulation
    with hit/fault statistics.

Usage:
    python main.py

Requirements:
    Python 3.9+
    rich >= 13.0  (pip install rich)

References:
    See report or README.md for full APA citations.
"""

import sys
import os

# ── Path setup ─────────────────────────────────────────────────────────────
# Ensure the project root is on sys.path so imports work from any CWD
_DIR = os.path.dirname(os.path.abspath(__file__))
if _DIR not in sys.path:
    sys.path.insert(0, _DIR)

# ── Imports ─────────────────────────────────────────────────────────────────
try:
    from rich.prompt import Prompt
    from rich.console import Console
    from rich import print as rprint
except ImportError:
    print("ERROR: 'rich' library not found. Run:  pip install rich")
    sys.exit(1)

from algorithms import (
    fifo_simulate,
    lru_simulate,
    mru_simulate,
    optimal_simulate,
    second_chance_simulate,
)
from utils import (
    print_banner,
    print_main_menu,
    print_simulation_results,
    print_comparison_table,
    prompt_algorithm_choice,
    prompt_simulation_inputs,
    print_goodbye,
    console,
)
from utils.display import COLORS

# ── Algorithm Registry ──────────────────────────────────────────────────────
ALGORITHMS = {
    1: ("FIFO",          fifo_simulate),
    2: ("LRU",           lru_simulate),
    3: ("MRU",           mru_simulate),
    4: ("OPTIMAL",       optimal_simulate),
    5: ("SECOND CHANCE", second_chance_simulate),
}


# ─────────────────────────────────────────────────────────────────────────────
# SIMULATE SINGLE ALGORITHM
# ─────────────────────────────────────────────────────────────────────────────

def run_single_algorithm(algo_key: int):
    """Run one selected algorithm and display results."""
    name, func = ALGORITHMS[algo_key]
    num_frames, ref_string = prompt_simulation_inputs()

    console.print(f"  [bold {COLORS['secondary']}]⚙  Running {name} simulation...[/]")
    console.print()

    result = func(ref_string, num_frames)
    print_simulation_results(result)


# ─────────────────────────────────────────────────────────────────────────────
# COMPARE ALL ALGORITHMS
# ─────────────────────────────────────────────────────────────────────────────

def run_all_algorithms():
    """Run all 5 algorithms on the same input and display comparison."""
    num_frames, ref_string = prompt_simulation_inputs()

    results = []
    for key, (name, func) in ALGORITHMS.items():
        console.print(f"  [bold {COLORS['muted']}]  ↪  Simulating {name}...[/]")
        result = func(ref_string, num_frames)
        results.append(result)

    console.print()

    # Show each algorithm's detail
    for result in results:
        print_simulation_results(result)
        console.print()

        cont = Prompt.ask(
            f"  [dim {COLORS['muted']}]Press Enter for next algorithm, or 's' to skip to comparison[/]",
            default="",
            show_default=False,
        )
        if cont.strip().lower() == "s":
            break

    # Show comparison table
    print_comparison_table(results)


# ─────────────────────────────────────────────────────────────────────────────
# POST-RUN PROMPT
# ─────────────────────────────────────────────────────────────────────────────

def prompt_continue() -> str:
    """Ask user what to do after a simulation run."""
    console.print()
    options_text = (
        f"  [bold {COLORS['accent']}][M][/] Back to Menu    "
        f"[bold {COLORS['success']}][R][/] Run Again    "
        f"[bold {COLORS['danger']}][Q][/] Quit"
    )
    console.print(options_text)
    choice = Prompt.ask(
        f"  [bold {COLORS['secondary']}]❯  Your choice",
        default="M",
    )
    return choice.strip().upper()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────────────────────────────────────

def main():
    """Main entry point — drives the menu and simulation loop."""
    # Clear screen for a clean start
    os.system("cls" if os.name == "nt" else "clear")

    print_banner()

    last_algo = None   # remember last choice for "run again"

    while True:
        print_main_menu()
        choice = prompt_algorithm_choice()

        if choice == 0:
            print_goodbye()
            sys.exit(0)

        elif choice in ALGORITHMS:
            last_algo = choice
            run_single_algorithm(choice)

        elif choice == 6:
            last_algo = 6
            run_all_algorithms()

        # Post-run options
        while True:
            action = prompt_continue()
            if action == "M":
                console.print()
                break
            elif action == "R":
                console.print()
                if last_algo and last_algo in ALGORITHMS:
                    run_single_algorithm(last_algo)
                elif last_algo == 6:
                    run_all_algorithms()
                else:
                    break
            elif action == "Q":
                print_goodbye()
                sys.exit(0)
            else:
                console.print(f"  [bold {COLORS['danger']}]Invalid. Enter M, R, or Q.[/]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print()
        console.print(f"  [bold {COLORS['warning']}]Interrupted. Goodbye![/]")
        sys.exit(0)
