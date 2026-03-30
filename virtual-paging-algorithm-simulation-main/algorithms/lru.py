"""
LRU (Least Recently Used) Page Replacement Algorithm
------------------------------------------------------
Replaces the page that has not been used for the longest period of time.
Frames stay in fixed positions — only the number in the evicted slot changes.

Reference:
    Silberschatz, A., Galvin, P. B., & Gagne, G. (2018).
    Operating System Concepts (10th ed.). Wiley.
    Chapter 10: Virtual Memory, pp. 440-443.
"""


def simulate(reference_string: list, num_frames: int) -> dict:
    """
    Simulate the LRU page replacement algorithm.

    Args:
        reference_string: List of page numbers to reference.
        num_frames: Number of available page frames.

    Returns:
        A dict with simulation results including frame history and statistics.
    """
    frames = [None] * num_frames          # Fixed-position frame slots
    last_used_time = {}                    # page -> time step when it was last accessed
    frames_history = []
    fault_flags = []
    evicted_pages = []

    for step, page in enumerate(reference_string):
        is_fault = page not in frames
        evicted = None

        if is_fault:
            if None in frames:
                # Use the first empty slot
                idx = frames.index(None)
            else:
                # Find the least recently used page (oldest last_used_time)
                lru_page = min(
                    (p for p in frames if p is not None),
                    key=lambda p: last_used_time[p],
                )
                idx = frames.index(lru_page)
                evicted = lru_page
                del last_used_time[lru_page]

            # Place the new page in that same slot
            frames[idx] = page
            last_used_time[page] = step
        else:
            # HIT — update recency but don't change frame positions
            last_used_time[page] = step

        fault_flags.append(is_fault)
        evicted_pages.append(evicted)
        frames_history.append(list(frames))

    total_faults = sum(fault_flags)
    total_hits = len(reference_string) - total_faults
    total = len(reference_string)

    return {
        "algorithm": "LRU",
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
