"""
Topic:
Multithreading in Python

Importance:
Threads allow concurrent execution of code. They are highly efficient for I/O-bound tasks
(like downloading text resources, web scraping, reading images from disk).
However, due to Python's Global Interpreter Lock (GIL), multithreading cannot achieve
parallelism on CPU-bound computations (like matrix multiplication).

This file covers:
- What is a thread
- Creating and starting threads using the threading module
- Joining threads (waiting for completion)
- Understanding the GIL (Global Interpreter Lock) limitations
- Practical ML application: Concurrently simulating downloading multiple image dataset URLs (I/O-bound)
"""

import threading
import time

# ==========================================
# 1. Thread Creation & Execution Basics
# ==========================================
# We define a function, create a Thread object pointing to it, and call start().
# Use join() to block execution until the thread terminates.

def download_batch_images(batch_id, duration):
    print(f"[THREAD START] Thread-{batch_id}: Downloading batch {batch_id}...")
    # Simulate I/O latency (web request delay)
    time.sleep(duration)
    print(f"[THREAD END] Thread-{batch_id}: Finished downloading batch {batch_id}.")

print("--- Thread Execution ---")
start_time = time.time()

# Creating Thread objects
# target: function to run
# args: tuple of positional arguments passed to the function
thread1 = threading.Thread(target=download_batch_images, args=(1, 0.4))
thread2 = threading.Thread(target=download_batch_images, args=(2, 0.2))

# Starting threads
thread1.start()
thread2.start()

# Joining threads: Main execution waits until thread1 and thread2 are completed
thread1.join()
thread2.join()

elapsed = time.time() - start_time
# The total time is approximately max(0.4, 0.2) rather than sum(0.4 + 0.2) = 0.6
print(f"Total concurrent download duration: {elapsed:.4f} seconds.")

# ==========================================
# 2. Sequential vs Multithreaded I/O Benchmarking
# ==========================================
# Let's write a loop to download 4 batches of data.

batches = [1, 2, 3, 4]
def simulated_download(batch):
    # Simulate network wait
    time.sleep(0.1)

print("\n--- Sequential vs Multithreaded benchmark ---")

# A. Sequential
start = time.time()
for b in batches:
    simulated_download(b)
print(f"Sequential duration: {time.time() - start:.4f} seconds.")

# B. Multithreaded
start = time.time()
active_threads = []
for b in batches:
    t = threading.Thread(target=simulated_download, args=(b,))
    active_threads.append(t)
    t.start()

# Wait for all threads
for t in active_threads:
    t.join()
print(f"Multithreaded duration: {time.time() - start:.4f} seconds.")

# ==========================================
# 3. Global Interpreter Lock (GIL) Warning
# ==========================================
# Python's GIL ensures only one native thread executes Python bytecodes at any time.
# This prevents race conditions in CPython memory management.
# Consequence: CPU-bound math calculations (e.g. nested loop computations) gain NO speedup from multithreading.
# To speed up CPU calculations, we use Multiprocessing (which allocates separate CPU cores).

"""
Key Takeaways:
- Multithreading works well for concurrent I/O-bound tasks (waiting on disks or network resources).
- `thread.start()` spawns the thread; `thread.join()` blocks the main program until that thread finishes.
- Python's GIL blocks concurrent execution of multiple CPU-bound threads inside a single process.

Interview Relevance:
- What is the Global Interpreter Lock (GIL)? (A mutex lock in the CPython interpreter that ensures only one thread executes Python bytecodes at a time, protecting memory safety).
- When is multithreading preferred over multiprocessing? (For I/O-bound tasks like web scraping or database requests where threads spend most of their time waiting for responses).
- What does `thread.join()` do? (It blocks the calling thread, usually the main process thread, until the target thread finishes execution).

AI/ML Relevance:
- Data Ingestion: Loading image folders from disk while a GPU is training the current batch is run on separate background threads to prevent CPU bottleneck starvation.
- Real-time APIs: Web frameworks handle incoming query requests concurrently using threads while waiting on database operations.
"""
