"""
FIFO (First-In, First-Out) Page Replacement Algorithm
------------------------------------------------------
Replaces the page that has been in memory the longest (oldest page).
Uses a queue to track insertion order.

Reference:
    Silberschatz, A., Galvin, P. B., & Gagne, G. (2018).
    Operating System Concepts (10th ed.). Wiley.
    Chapter 10: Virtual Memory, pp. 437-440.
"""

from collections import deque


def simulate(reference_string: list, num_frames: int) -> dict:
    """
    Simulate the FIFO page replacement algorithm.

    Args:
        reference_string: List of page numbers to reference.
        num_frames: Number of available page frames.

    Returns:
        A dict with simulation results including frame history and statistics.
    """
    frames = []               # current pages in memory
    queue = deque()           # tracks insertion order (oldest at left)
    frames_history = []       # snapshot of frames at each step
    fault_flags = []          # True = page fault, False = page hit
    evicted_pages = []        # which page was evicted at each step (None if no eviction)

    for page in reference_string:
        is_fault = page not in frames
        evicted = None

        if is_fault:
            if len(frames) < num_frames:
                # There's still an empty frame slot
                frames.append(page)
                queue.append(page)
            else:
                # Evict the oldest page (FIFO order)
                oldest = queue.popleft()
                evicted = oldest
                idx = frames.index(oldest)
                frames[idx] = page
                queue.append(page)

        fault_flags.append(is_fault)
        evicted_pages.append(evicted)
        frames_history.append(list(frames) + [None] * (num_frames - len(frames)))

    total_faults = sum(fault_flags)
    total_hits = len(reference_string) - total_faults
    total = len(reference_string)

    return {
        "algorithm": "FIFO",
        "reference_string": reference_string,
        "num_frames": num_frames,
        "frames_history": frames_history,
        "fault_flags": fault_flags,
        "evicted_pages": evicted_pages,
        "total_faults": total_faults,
        "total_hits": total_hits,
        "fault_rate": round(total_faults / total * 100, 2) if total > 0 else 0.0,
        "hit_rate": round(total_hits / total * 100, 2) if total > 0 else 0.0,
    }
