"""
Topic:
MLOps - Experiment Tracking with MLflow

Importance:
During model development, you train dozens of models with different algorithms and hyperparameters.
Exhaustively tracking these experiments manually is impossible.
MLflow is the industry standard to track training parameters, validation metrics, and save model artifacts,
guaranteeing model reproducibility and version lineage.

This file covers:
- Concept: Experiment tracking, parameters vs metrics, run registry
- Initializing MLflow client (with fallback local logger simulator)
- Logging training hyperparameters (e.g. learning_rate, n_estimators)
- Logging training epochs metrics (e.g. loss, accuracy)
- Logging/Registering model artifacts (saving model files)
"""

# ==========================================
# 1. Concept Explanation & Glossary
# ==========================================
# MLflow segregates experiment records into Runs:
#   - Experiment: A logical group of related runs (e.g. "student_churn_models").
#   - Run: A single execution of a machine learning model pipeline.
#   - Log Parameter: Stores key-value configuration values (e.g., `learning_rate: 0.05`).
#   - Log Metric: Stores scalar values computed during or after run updates (e.g., `accuracy: 0.92`).
#   - Log Artifact: Stores output files, charts, or serialized model weights (`.pkl` / `.h5`).

import os

import sys

# Check command line flags to prevent unexpected system DLL crashes on import
use_mlflow = False
if "--use-mlflow" in sys.argv:
    try:
        import mlflow
        use_mlflow = True
        print("Using active MLflow client.")
    except BaseException as e:
        use_mlflow = False
        print(f"MLflow library could not be loaded: {e}. Falling back to simulation.")
else:
    print("Running simulated MLflow logging client. Use '--use-mlflow' flag to bind active local servers.")

# ==========================================
# 2. Local Mock MLflow Client Simulator
# ==========================================
class SimulatedMLflowClient:
    def __init__(self):
        self.experiment_name = "default"
        self.active_run = None
        self.logged_params = {}
        self.logged_metrics = {}
        self.logged_artifacts = []
        
    def set_experiment(self, name):
        self.experiment_name = name
        print(f"[MLflow Sim] Switched to Experiment: '{name}'")
        
    def start_run(self, run_name=None):
        self.active_run = run_name or "run_01"
        self.logged_params = {}
        self.logged_metrics = {}
        self.logged_artifacts = []
        print(f"[MLflow Sim] Started Run: '{self.active_run}'")
        return self
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[MLflow Sim] Completed Run: '{self.active_run}'")
        print("Logged Parameters: ", self.logged_params)
        print("Logged Metrics:    ", self.logged_metrics)
        print("Logged Artifacts:   ", self.logged_artifacts)
        
    def log_param(self, key, value):
        self.logged_params[key] = value
        
    def log_metric(self, key, value):
        self.logged_metrics[key] = value
        
    def log_artifact(self, path):
        self.logged_artifacts.append(os.path.basename(path))

# ==========================================
# 3. Running Experiment Tracking Simulation
# ==========================================
def run_tracking_demonstration():
    # Setup hyperparameters to track
    learning_rate = 0.01
    n_estimators = 50
    final_test_accuracy = 0.925
    final_test_loss = 0.312
    
    # Create a dummy model file artifact to save
    artifact_filename = "trained_model_weights.txt"
    with open(artifact_filename, "w") as f:
        f.write("model_weights = [0.25, -0.42, 1.89, 0.05]")
        
    if use_mlflow:
        # Use native MLflow APIs
        mlflow.set_experiment("Student_Pass_Predictor")
        
        # Start logging context run
        with mlflow.start_run(run_name="random_forest_run_1"):
            # Log hyperparameters (fit configurations)
            mlflow.log_param("learning_rate", learning_rate)
            mlflow.log_param("n_estimators", n_estimators)
            
            # Log final metric performance values
            mlflow.log_metric("accuracy", final_test_accuracy)
            mlflow.log_metric("loss", final_test_loss)
            
            # Log model artifact file weights
            mlflow.log_artifact(artifact_filename)
            print("\nSuccessfully logged parameters and metrics to local MLflow registry.")
    else:
        # Fallback to local simulator
        client = SimulatedMLflowClient()
        client.set_experiment("Student_Pass_Predictor")
        
        with client.start_run(run_name="random_forest_run_1") as active_run:
            active_run.log_param("learning_rate", learning_rate)
            active_run.log_param("n_estimators", n_estimators)
            active_run.log_metric("accuracy", final_test_accuracy)
            active_run.log_metric("loss", final_test_loss)
            active_run.log_artifact(artifact_filename)
            
    # Cleanup temporary local test artifact file
    if os.path.exists(artifact_filename):
        os.remove(artifact_filename)

if __name__ == "__main__":
    run_tracking_demonstration()

"""
Key Takeaways:
- MLflow logs hyperparameters (inputs parameters setup) and metrics (model training evaluation outputs).
- Logging model artifacts (weights files or plots charts) guarantees run reproducibility.
- Experiment registries segregate different modeling tasks cleanly.

Interview Relevance:
- Explain Parameters vs Metrics in MLflow. (Parameters are the static hyperparameters configured before training, e.g. `n_estimators`, `learning_rate`; Metrics are scalar evaluation outputs calculated during/after training, e.g. `accuracy`, `loss`, which can update across training iterations/epochs).
- What is the MLflow Model Registry? (A centralized store to manage the lifecycle of an MLflow Model, supporting model versioning, state transitions from Staging to Production, and active model archiving).
- Why is experiment tracking important? (It allows teams to review historical training iterations, compare metrics across runs, and select the best version for deployment without manual record keeping).

AI/ML Relevance:
- MLOps Audit: Essential tool in enterprise MLOps pipelines to monitor drift, track active runs, and audit training runs history records.
"""
