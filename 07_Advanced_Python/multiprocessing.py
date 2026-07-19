"""
Topic:
Multiprocessing in Python

Importance:
CPU-bound calculations (like mathematical matrix multiplications or preprocessing raw files)
spend all their time computing numbers rather than waiting for resource events.
Multiprocessing bypasses the Global Interpreter Lock (GIL) by allocating separate CPU cores,
each with its own independent Python interpreter and memory space.

This file covers:
- Creating separate processes (multiprocessing.Process)
- Utilizing process pools (multiprocessing.Pool)
- Bypassing the GIL for CPU-bound performance speedups
- Windows compatibility warning: the requirement of 'if __name__ == "__main__":'
- Practical ML application: Parallelizing heavy feature transformations (data scaling) across processes
"""

import sys
import os

# --- PATH HACK TO PREVENT LOCAL FILE SHADOWING COLLISION ---
# Because this file is named 'multiprocessing.py', standard imports of 'import multiprocessing'
# would try to import this file itself. We remove the local folder path from sys.path temporarily.
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir in sys.path:
    sys.path.remove(current_dir)

import multiprocessing

# Restore path
sys.path.insert(0, current_dir)

import time
import math

# ==========================================
# 1. CPU-Bound Task Definition
# ==========================================
# A computation-heavy task (e.g. calculating square root sums of many numbers)

def perform_heavy_computations(task_id, range_limit):
    print(f"[PROCESS START] Process-{task_id}: Computing sum of roots up to {range_limit}...")
    total_sum = 0
    for val in range(range_limit):
        total_sum += math.sqrt(val)
    print(f"[PROCESS END] Process-{task_id}: Calculation completed.")
    return total_sum

# A helper task function to run inside the pool map (defined at module level so child processes can import it)
def square_root_sum(n):
    return sum(math.sqrt(i) for i in range(n))

# ==========================================
# 2. Main Entry Point (Windows Multiprocessing Constraint)
# ==========================================
# WARNING: On Windows, child processes import the main module to load definitions.
# If you don't wrap execution in 'if __name__ == "__main__":', it triggers an infinite loop of process spawn crashes.

if __name__ == "__main__":
    print("--- 1. Basic Process Spawning ---")
    start_time = time.time()
    
    # Instantiate two separate processes
    p1 = multiprocessing.Process(target=perform_heavy_computations, args=(1, 5000000))
    p2 = multiprocessing.Process(target=perform_heavy_computations, args=(2, 5000000))
    
    # Start processes (they run in parallel on separate CPU cores!)
    p1.start()
    p2.start()
    
    # Wait for processes to finish
    p1.join()
    p2.join()
    
    print(f"Total basic parallel execution duration: {time.time() - start_time:.4f} seconds.")
    
    # ==========================================
    # 3. Process Pools (multiprocessing.Pool)
    # ==========================================
    # Pool divides a collection of inputs across multiple workers automatically.
    # E.g. Applying feature transformations to four dataset segments concurrently.
    
    print("\n--- 2. Process Pool (Mapping Tasks) ---")
    
    # Mock data slices
    dataset_segments = [1000000, 2000000, 3000000, 4000000]
    
    # Using the module-level square_root_sum function defined above
        
    start_pool = time.time()
    
    # Determine the number of CPU cores available
    available_cores = multiprocessing.cpu_count()
    print(f"Detected CPU Cores: {available_cores}")
    
    # Create a pool of workers matching available cores
    with multiprocessing.Pool(processes=available_cores) as pool:
        # pool.map distributes list inputs across processes and returns consolidated results list
        results = pool.map(square_root_sum, dataset_segments)
        
    print(f"Segment calculation results: {results}")
    print(f"Process Pool duration: {time.time() - start_pool:.4f} seconds.")

"""
Key Takeaways:
- Multiprocessing runs tasks in parallel on separate CPU cores, bypassing Python's GIL.
- On Windows, always protect script entry execution with `if __name__ == '__main__':`.
- `multiprocessing.Pool` distributes map tasks automatically across worker processes.
- Each process has its own memory space; variables are not shared implicitly between processes like they are with threads.

Interview Relevance:
- What is the difference between Multithreading and Multiprocessing? (Threads share the same memory space and run concurrently inside one process, limited by the GIL; processes run in independent memory spaces on separate CPU cores in parallel, bypassing the GIL).
- Why is `if __name__ == '__main__':` required for Windows multiprocessing? (Windows spawns child processes by importing the main script, so this wrapper prevents child processes from executing setup code recursively).
- How do processes share data in Python? (Since they have separate memory, data sharing requires specific structures like `Queue`, `Pipe`, or `Value`/`Array` shared memory objects).

AI/ML Relevance:
- Feature Engineering: Slicing a tabular database of 50 million rows and applying transformations (like scaling or parsing string dates) is parallelized across CPU processes.
- Model Ensembles: Hyperparameter grids (grid search) run combinations of training tasks in parallel across CPU pool processes to save search time.
"""
