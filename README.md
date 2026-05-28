# Semester 1 assignment

Use this template to build your assignment. You'll need to add to the existing files and create new files to extend the project to meet the assignment requirements.

## Scenario

You are building a website to help students with studying. You'll need to find a way to help students revise definitions for different topics in a flashcard-style app.

## Assessment criteria

- The assessment is worth 20% of your final grade.
- There are some unit tests provided to go with the function stubs you have been given to fill out for the core part of your project. Your code must pass all of the unit tests.
- Make sure your code passes the linter too.
- Add more functions. Every function must have a unit test.

## How to work on this project

<details>
<summary><strong>Local development in VS Code</strong></summary>

### Set up

1. Open the project in VS Code.
2. Make sure you have the Python extension installed.
3. Open the Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Windows / Linux) → **Tasks: Run Task**.
4. Choose:
   - **Set up project (macOS/Linux)** on macOS or Linux, or
   - **Set up project (Windows)** on Windows.
5. Wait for the task to finish. It will print a `Setup complete!` banner with the next step.
6. **Select the new Python interpreter** so VS Code uses your project's `.venv`:
   - Look at the bottom-right corner of VS Code. You'll see the current Python version.
   - Click it → pick the entry labelled **`.venv`** (it's usually marked "Recommended").
   - If `.venv` doesn't appear, pick **Enter interpreter path** → **Find…** → browse to `.venv/bin/python` (macOS/Linux) or `.venv\Scripts\python.exe` (Windows).
7. Open a **new** terminal (`` Ctrl+` ``). The prompt should now start with `(.venv)` — VS Code activated the environment for you. You don't have to type `source .venv/bin/activate` yourself.

> **Why this matters**: the setup task creates the virtual environment on disk, but the Run ▶ button and integrated terminals only use it once you've *selected* it in step 6. After that it's automatic.

### Run the project

1. Open the **Run and Debug** panel (`Cmd+Shift+D` / `Ctrl+Shift+D`).
2. Pick **Run Flask app** from the dropdown.
3. Press the green ▶ (or `F5` to run with the debugger).
4. Open `http://127.0.0.1:8000` in your browser.

### Run tests

You have three ways — pick whichever you like:

- **Test Explorer**: click the beaker icon in the sidebar. You'll see every test with a green ▶ next to it. Click ▶ on a single test, a file, or the root to run all of them.
- **Run and Debug panel**: pick **Run tests (pytest)** and press ▶. Or pick **Debug current test file** to run only the test file you're currently looking at, with breakpoints.
- **Terminal**: in a `(.venv)`-activated terminal, run `pytest -v`.

</details>

<details>
<summary><strong>Using GitHub Codespaces</strong></summary>

### Set up

1. From the repository on GitHub, click the green **Code** button → **Codespaces** → **Create codespace on main**.
2. Wait for the Codespace to build. The `.devcontainer/devcontainer.json` in this project automatically:
   - installs Python and the VS Code Python extension,
   - creates the `.venv`,
   - installs everything from `requirements.txt`,
   - selects the venv as the active interpreter, and
   - enables the Test Explorer.
3. When the Codespace finishes building, you're ready. No setup task needed.

### Run the project

1. Open the **Run and Debug** panel.
2. Pick **Run Flask app** and press ▶.
3. Codespaces will auto-forward port `8000` and open the app in a preview tab. You can also find the link in the **Ports** tab.

### Run tests

Same as local development — use the Test Explorer (beaker icon) or the **Run tests (pytest)** entry in Run and Debug.

</details>

etc, etc, etc
