from algorithms.fifo import simulate as fifo_sim
from algorithms.lru import simulate as lru_sim
from algorithms.mru import simulate as mru_sim
from algorithms.optimal import simulate as opt_sim
from algorithms.second_chance import simulate as sc_sim

ref = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
frames = 3

for fn, name in [(fifo_sim,'FIFO'),(lru_sim,'LRU'),(mru_sim,'MRU'),(opt_sim,'OPT'),(sc_sim,'2ND')]:
    r = fn(ref, frames)
    print(name.ljust(12), "Faults=" + str(r["total_faults"]).rjust(2),
          "Hits=" + str(r["total_hits"]).rjust(2),
          "FaultRate=" + str(r["fault_rate"]) + "%",
          "HitRate=" + str(r["hit_rate"]) + "%")
