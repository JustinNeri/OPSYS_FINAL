"""
Optimal (OPT / Bélády's) Page Replacement Algorithm
------------------------------------------------------
Replaces the page that will not be used for the longest period in the future.
This is a theoretical best-case algorithm — it requires future knowledge.

Reference:
    Bélády, L. A. (1966). A study of replacement algorithms for a virtual-storage
    computer. IBM Systems Journal, 5(2), 78-101. https://doi.org/10.1147/sj.52.0078

    Silberschatz, A., Galvin, P. B., & Gagne, G. (2018).
    Operating System Concepts (10th ed.). Wiley.
    Chapter 10: Virtual Memory, pp. 436-437.
"""


def simulate(reference_string: list, num_frames: int) -> dict:
    """
    Simulate the Optimal page replacement algorithm.

    Args:
        reference_string: List of page numbers to reference.
        num_frames: Number of available page frames.

    Returns:
        A dict with simulation results including frame history and statistics.
    """
    frames = []
    frames_history = []
    fault_flags = []
    evicted_pages = []
    insertion_time = {}                    # page -> time step when it was loaded (for FIFO tiebreak)

    for i, page in enumerate(reference_string):
        is_fault = page not in frames
        evicted = None

        if is_fault:
            if len(frames) < num_frames:
                frames.append(page)
                insertion_time[page] = i
            else:
                # Look ahead: find which page in frames will be used furthest in future
                future = reference_string[i + 1:]
                farthest_idx = -1
                page_to_evict = None
                no_future_pages = []

                for p in frames:
                    if p not in future:
                        # This page is never used again — collect for FIFO tiebreak
                        no_future_pages.append(p)
                    else:
                        next_use = future.index(p)
                        if next_use > farthest_idx:
                            farthest_idx = next_use
                            page_to_evict = p

                if no_future_pages:
                    # FIFO among pages with no future use: evict the one loaded earliest
                    page_to_evict = min(no_future_pages, key=lambda p: insertion_time[p])

                evicted = page_to_evict
                idx = frames.index(page_to_evict)
                frames[idx] = page
                del insertion_time[page_to_evict]
                insertion_time[page] = i

        fault_flags.append(is_fault)
        evicted_pages.append(evicted)
        frames_history.append(list(frames) + [None] * (num_frames - len(frames)))

    total_faults = sum(fault_flags)
    total_hits = len(reference_string) - total_faults
    total = len(reference_string)

    return {
        "algorithm": "OPTIMAL",
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
