# Tests Module

## Purpose
Centralize automated checks that validate the calculator's behavior. These tests help detect regressions and highlight known issues before changes are merged.

## Structure
- `test_app.py`: Exercises the Flask endpoint using its test client.
- `test_operators.py`: Verifies arithmetic helpers exposed by `operators.py`.

## Running the Tests
1. Install dependencies (Flask and pytest are already in `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```
2. Execute the suite from the project root:
   ```bash
   py -m pytest
   ```

