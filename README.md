# Virtual Paging Algorithm Simulation

**OPSYSFUN — Operating Systems Fundamentals | Final Project**

Holy Angel University — School of Computing
## Group Members
- Cabutihan, Shawn Uriel S.
- Centeno, Laurenzo S.
- Garcia, Seane Karl S.
- Pangilinan, Justin Neri A.
- Villapaña, Neriah Faith L.

## Algorithms Implemented
| # | Algorithm | Description |
|---|-----------|-------------|
| 1 | **FIFO** | First-In, First-Out — evicts the oldest page |
| 2 | **LRU** | Least Recently Used — evicts least recently accessed page |
| 3 | **MRU** | Most Recently Used — evicts most recently accessed page |
| 4 | **OPTIMAL** | Bélády's algorithm — evicts page used furthest in future |
| 5 | **SECOND CHANCE** | Clock algorithm — FIFO with reference bit grace period |

## Requirements
- Python 3.9+
- rich library

`Bash
pip install rich
`

## How to Run
`Bash
python main.py
`

## Project Structure
`
Final_Project/
├── main.py                  # Main entry point
├── algorithms/
│   ├── fifo.py              # FIFO algorithm
│   ├── lru.py               # LRU algorithm
│   ├── mru.py               # MRU algorithm
│   ├── optimal.py           # Optimal algorithm
│   └── second_chance.py     # Second Chance algorithm
├── utils/
│   └── display.py           # UI / display using rich
├── requirements.txt
└── README.md
`

## Features
- Interactive menu-driven interface
- Step-by-step frame state tables (color-coded hits/faults)
- Hit rate & fault rate statistics with bar charts
- Compare all algorithms side-by-side
- Second Chance reference bit display

## References (APA)
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
- Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson.
- Bélády, L. A. (1966). A study of replacement algorithms for a virtual-storage computer. *IBM Systems Journal, 5*(2), 78–101. https://doi.org/10.1147/sj.52.0078
- GeeksforGeeks. (2024, November 19). *Program for FIFO page replacement algorithm*. https://www.geeksforgeeks.org/dsa/program-page-replacement-algorithms-set-2-fifo/
- GeeksforGeeks. (2024, November 19). *Program for Least Recently Used (LRU) page replacement algorithm*. https://www.geeksforgeeks.org/dsa/program-for-least-recently-used-lru-page-replacement-algorithm/
- GeeksforGeeks. (2024, November 19). *Page replacement algorithms in operating systems*. https://www.geeksforgeeks.org/operating-systems/page-replacement-algorithms-in-operating-systems/
- GeeksforGeeks. (2024, November 19). *Optimal page replacement algorithm*. https://www.geeksforgeeks.org/dsa/optimal-page-replacement-algorithm/
- GeeksforGeeks. (2024, November 19). *Second chance (clock) page replacement policy*. https://www.geeksforgeeks.org/operating-systems/second-chance-or-clock-page-replacement-policy/
- GeeksforGeeks. (2024, November 19). *Most Recently Used (MRU) page replacement algorithm*. https://www.geeksforgeeks.org/dsa/most-recently-used-mru-page-replacement-algorithm/
