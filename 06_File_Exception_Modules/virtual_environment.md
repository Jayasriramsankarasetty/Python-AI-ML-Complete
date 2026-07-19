# Python Virtual Environments

A virtual environment is a self-contained directory tree that contains a specific Python installation and a set of additional packages. It isolates project-specific dependencies, preventing conflicts between globally installed libraries.

---

## Why Use Virtual Environments?

1. **Dependency Isolation**: Project A might require `scikit-learn==0.24`, while Project B requires `scikit-learn==1.0`. A virtual environment allows you to run both projects on the same machine without conflict.
2. **Permission Safety**: Installing packages globally (using `pip install`) requires root/administrator privileges and can break system-level Python scripts.
3. **Reproducibility**: Generating a `requirements.txt` file within an active environment allows other developers (and production servers) to install the exact same library versions.

---

## Step-by-Step Environment Management

### 1. Creation
Python includes a built-in module called `venv` to create environments. Run this command inside your project's root directory:

```bash
# Syntax: python -m venv <environment_name>
# Commonly named 'env', '.env', or 'venv'
python -m venv venv
```

This creates a folder named `venv/` containing local Python executables and libraries folders.

### 2. Activation
To start using the environment, you must activate it. The command depends on your Operating System and shell:

* **Windows (Command Prompt - cmd)**:
  ```cmd
  venv\Scripts\activate.bat
  ```
* **Windows (PowerShell)**:
  ```powershell
  venv\Scripts\Activate.ps1
  ```
  *(Note: If you receive a script execution policy error in PowerShell, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first)*
* **macOS / Linux (Bash/Zsh)**:
  ```bash
  source venv/bin/activate
  ```

Once activated, your terminal prompt will display the environment's name in parentheses, e.g., `(venv) C:\project>`.

### 3. Managing Packages (pip)
When the environment is active, running `pip` installs packages locally into the `venv/` directory, rather than globally.

* **Installing a package**:
  ```bash
  pip install numpy
  pip install pandas==1.3.3  # Install a specific version
  ```
* **Exporting dependencies** (creating a package snapshot):
  ```bash
  pip freeze > requirements.txt
  ```
* **Installing from requirements.txt** (restoring a snapshot):
  ```bash
  pip install -r requirements.txt
  ```

### 4. Deactivation
To exit the active virtual environment and return to global system Python, simply run:

```bash
deactivate
```

---

## Interview Questions & Answers

### Q1. What is the difference between `pip` and `conda`?
* **`pip`**: The official Python package manager. It installs Python packages from the Python Package Index (PyPI).
* **`conda`**: A cross-platform package and environment manager. It handles both Python packages and low-level system binary dependencies (like C++ compiler libraries, CUDA libraries for GPUs) that `pip` cannot install directly.

### Q2. Should you commit the virtual environment folder (`venv/`) to git repository?
* **No**. You should add the `venv/` folder name to your `.gitignore` file. Committing the environment is bad practice because it contains compiled binary executables specific to your OS, makes the repository extremely large, and can easily be rebuilt on other platforms using the `requirements.txt` file.

### Q3. How does Python find imports inside a virtual environment?
* When activated, the path to the environment's `bin` (or `Scripts` on Windows) folder is prepended to the system's `PATH` environment variable. Python updates `sys.path`, pointing its search locations to the local `site-packages` directory instead of the system global installation.
