**LOG3000 – Simple Flask Calculator**

## Team
- Team 6
- Members: Alhassane Barry, Yanis Ould Mahammed

## Objective
Provide a simple, one-page calculator you can run locally to perform quick arithmetic without opening a spreadsheet or phone app. The Flask backend reads the expression you type, applies the selected operator, and returns the answer to the webpage immediately.

## Installation Prerequisites
- Python 3.9 or newer
- `pip` (bundled with recent Python installers)
- (Optional) `venv` or another virtual-environment tool
- Internet access to install PyPI packages

## Installation Instructions
1. Clone the repository and enter the project directory:
   ```bash
   git clone <your-repo-url>.git
   cd TP3-LOG3000
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. Install runtime dependencies (local `requirements.txt` includes Flask):
   ```bash
   pip install -r requirements.txt
   ```
4. Launch the development server:
   ```bash
   python app.py
   ```
5. Open your browser to http://127.0.0.1:5000 to use the calculator interface.

## Project Structure
- `app.py`: Flask application entry point and request handling.
- `operators.py`: Arithmetic helper functions used by the backend (documented with current behavior; logical issues will be addressed in later assignments).
- `templates/`: HTML templates rendered by Flask (`index.html` hosts the calculator UI).
- `static/`: Static assets such as CSS (`style.css` styles the calculator page).
- `requirements.txt`: Python dependencies required for local execution.

## Usage
1. Start the development server as described above.
2. Enter a simple expression using two operands and one operator in the on-screen calculator (e.g., `8 / 2`).
3. Press `=` to submit the expression; the result (or an error message) appears in the display field.
4. Use `C` to clear the display and type a new expression.

## Testing
- Test runner: `pytest`
- Layout: see the `tests/` directory (`test_app.py`, `test_operators.py`, and their README).
- Install the toolchain:
  ```bash
  pip install -r requirements.txt
  ```
- Execute the suite from the project root:
  ```bash
  py -m pytest
  ```

## Contribution Workflow
- **Branches:** create a feature branch per issue (e.g., `feature/docs-update`, `fix/bug-xyz`).
- **Commits:** prefer small, descriptive commit messages that explain *why* a change was made.
- **Pull Requests:** open a PR for each branch, link related GitHub issues, and request at least one teammate for review.
- **Issues:** document each discovered bug or enhancement with reproduction steps, expected behavior, and assignee.
- **Coding Standards:** keep documentation up to date, preserve existing behavior unless an issue explicitly states otherwise, and run the relevant tests (pytest once available) before requesting review.

