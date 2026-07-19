
# Resource Allocator
# Design a system to assign incoming jobs to a fixed pool of workers, where workers come in different "tiers" (some can only handle small jobs, some can handle any size), and a job releases its worker back to the pool when done.
# Design 3 apis: assignJob, releaseWorker, getAvailableCapacity



# EDGE CASES
# worker = (max_job_memory: int, max_job_cpu: int)


# worker1 = cap 8, curr cap 7
# worker2 = cap 3, curr cap 0
# job queue = [("job a", size=8), ("job b", size=2), ("job a", size=2), ("job a", size=3)]



# job is too big = <drop>

# cases:
# if worker cap is 0 or negative