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

