"""
Second Chance (Clock) Page Replacement Algorithm
--------------------------------------------------
An improved version of FIFO that gives pages a "second chance" before eviction.
Each page has a reference bit (R). When a page is accessed, R=1.
On page fault, scan clock hand:
  - If R=1: clear it (give second chance), advance hand
  - If R=0: evict this page, replace with new page

Reference:
    Tanenbaum, A. S., & Bos, H. (2014).
    Modern Operating Systems (4th ed.). Pearson.
    Chapter 3: Memory Management, pp. 213-215.

    Silberschatz, A., Galvin, P. B., & Gagne, G. (2018).
    Operating System Concepts (10th ed.). Wiley.
    Chapter 10: Virtual Memory, pp. 451-452.
"""


def simulate(reference_string: list, num_frames: int) -> dict:
    """
    Simulate the Second Chance (Clock) page replacement algorithm.

    Args:
        reference_string: List of page numbers to reference.
        num_frames: Number of available page frames.

    Returns:
        A dict with simulation results including frame history and statistics.
    """
    frames = [None] * num_frames      # page stored in each frame slot
    ref_bits = [0] * num_frames       # reference bit for each frame slot
    clock_hand = 0                    # current position of the clock hand
    frames_history = []
    fault_flags = []
    evicted_pages = []
    ref_bits_history = []

    for page in reference_string:
        is_fault = page not in frames
        evicted = None

        if is_fault:
            # Find a slot (empty slots first, then use clock algorithm)
            if None in frames:
                # Fill an empty slot
                idx = frames.index(None)
                frames[idx] = page
                ref_bits[idx] = 1
            else:
                # Clock algorithm: find a frame with R=0
                while True:
                    if ref_bits[clock_hand] == 0:
                        # Evict this page
                        evicted = frames[clock_hand]
                        frames[clock_hand] = page
                        ref_bits[clock_hand] = 1
                        clock_hand = (clock_hand + 1) % num_frames
                        break
                    else:
                        # Give second chance: clear reference bit
                        ref_bits[clock_hand] = 0
                        clock_hand = (clock_hand + 1) % num_frames
        else:
            # Page hit — set reference bit to 1
            idx = frames.index(page)
            ref_bits[idx] = 1

        fault_flags.append(is_fault)
        evicted_pages.append(evicted)
        frames_history.append(list(frames))
        ref_bits_history.append(list(ref_bits))

    total_faults = sum(fault_flags)
    total_hits = len(reference_string) - total_faults
    total = len(reference_string)

    return {
        "algorithm": "SECOND CHANCE",
        "reference_string": reference_string,
        "num_frames": num_frames,
        "frames_history": frames_history,
        "fault_flags": fault_flags,
        "evicted_pages": evicted_pages,
        "ref_bits_history": ref_bits_history,
        "total_faults": total_faults,
        "total_hits": total_hits,
        "fault_rate": round(total_faults / total * 100, 2) if total > 0 else 0.0,
        "hit_rate": round(total_hits / total * 100, 2) if total > 0 else 0.0,
    }
