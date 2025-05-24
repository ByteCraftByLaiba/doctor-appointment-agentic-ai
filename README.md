### ✅ **Step-by-Step: Create Python Virtual Environment in VS Code (Windows)**

### 🔁 **Steps**

#### **1. Open VS Code**

* Open your project folder in VS Code (or create a new one).

#### **2. Open Terminal in VS Code**

* Press `Ctrl + ` (backtick) OR go to `Terminal > New Terminal`.

#### **3. Choose Python Version**

Check available Python versions on your system:

```bash
py -0
```

Example output:

```
 -3.11-64
 -3.10-64
```

To use Python 3.10:

```bash
py -3.10 -m venv venv
```

✅ This creates a virtual environment named `venv` using Python 3.10 in your current directory.

---

#### **4. Activate the Virtual Environment**

In the terminal (Command Prompt or PowerShell):

```bash
.\venv\Scripts\activate
```

Once activated, you’ll see:

```
(venv) C:\your\project\path>
```

---

#### **5. Select Interpreter in VS Code**

* Press `Ctrl+Shift+P` → type **"Python: Select Interpreter"**
* Choose the one with path like:

  ```
  .\venv\Scripts\python.exe
  ```

VS Code will now use this virtual environment.

---

#### **6. Install Packages**

You can now install packages like Pydantic:

```bash
pip install pydantic
```

---

#### **7. Create `requirements.txt` (optional)**

```bash
pip freeze > requirements.txt
```

