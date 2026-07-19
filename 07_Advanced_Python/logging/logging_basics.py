"""
Topic:
Logging Basics in Python

Importance:
Print statements are temporary and dump text unstructured to standard output.
Standard logging writes timestamped messages with severity levels (DEBUG, INFO, WARNING, etc.)
to files or remote servers. This is critical to monitor training loops, pipeline warnings, and API exceptions.

This file covers:
- Why print is not suitable for production
- Severity Levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Basic configuration (filename, levels, formatting)
- Adding File and Stream handlers
- Practical ML application: Logging model training progress, parameter warnings, and OOM errors
"""

import logging

# ==========================================
# 1. Understanding Logging Levels
# ==========================================
# Levels represent severity (ascending order):
# - DEBUG (10): Detailed diagnostic info.
# - INFO (20): General confirmations of success.
# - WARNING (30): Indications of unexpected issues/deprecation warning.
# - ERROR (40): Failures causing issues in execution, but program can recover.
# - CRITICAL (50): Severe crashes where execution cannot proceed.

# ==========================================
# 2. Basic Configuration Setup
# ==========================================
# We configure format patterns, base level threshold, and file outputs.

log_filepath = "ml_execution.log"

logging.basicConfig(
    # Set threshold: logging calls below INFO (i.e. DEBUG) will be ignored by default
    level=logging.DEBUG,
    # Format: [TIMESTAMP] [SEVERITY_LEVEL] - [MESSAGE]
    format="%(asctime)s [%(levelname)s] - %(message)s",
    handlers=[
        # Writes logs to a file
        logging.FileHandler(log_filepath, mode="w"),
        # Also dumps logs to console standard output
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ML_Logger")

# ==========================================
# 3. Simulating Logging Execution (ML Use-Case)
# ==========================================
print("--- Logging Activity Started ---")

logger.debug("Parsing hyperparameters dictionary: learning_rate=0.005, optimizer=Adam")
logger.info("Dataset 'housing.csv' loaded successfully with size 15000 rows.")

# Simulate warning condition
val_loss = 0.56
patience = 3
logger.warning(f"Validation loss did not improve for {patience} epochs. Current Val Loss: {val_loss}")

# Simulate model exception recovery
try:
    # Intentionally trigger an error (e.g. invalid array slice)
    assert 1 == 0
except AssertionError:
    logger.error("Failed to extract validation metric slices. Re-attempting partition calculations.")

# Simulate severe crash (OOM)
gpu_memory_available = 0.05  # 5%
if gpu_memory_available < 0.10:
    logger.critical("CUDA OUT OF MEMORY (OOM) error detected. Halting GPU training loop to prevent node lockup.")

print(f"\nAll logs recorded. Inspect the generated file at: '{log_filepath}'")

"""
Key Takeaways:
- Logging is preferred over print statements in production because it categorizes errors, provides timestamps, and routes outputs.
- Logging levels filter messages (e.g. set level to WARNING to hide INFO and DEBUG logs).
- Handlers (StreamHandler, FileHandler) send logs to multiple destinations concurrently.

Interview Relevance:
- Why should you use logging instead of print statements? (Logging provides timestamps, module names, thread IDs, log levels, and handles output redirection to files or database networks without changing code).
- What are the standard logging levels in Python? (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- How do you configure logging to print to both console and a file? (Create a logger and add a `StreamHandler` and a `FileHandler` to it).

AI/ML Relevance:
- Production Audit: Deployed inference microservices log request shapes and prediction outputs to help track model drift.
- Remote telemetry: Large models training on distributed clusters pipe logs to tools like Weights & Biases or Elasticsearch to track epochs progress.
"""
