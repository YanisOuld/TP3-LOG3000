# Templates Module

## Purpose
Explain the HTML views that Flask renders to present the calculator interface. Everything in this folder defines what users see when they interact with the app.

## Key Files
- `index.html`: Single-page calculator layout with buttons, display field, and small inline JavaScript helpers to append digits/operators.

## Dependencies & Assumptions
- Served through Flask's `render_template` in `app.py`; any new template must be referenced there.
- Relies on assets from `static/` (for example, `style.css`) via `url_for('static', filename=...)`.
- Written in plain HTML; no template inheritance or frameworks are configured yet.

## Usage Tips
- When you add a new page, mirror the existing structure and update `app.py` to map a route to it.
- Keep inline scripts minimal; move reusable logic to dedicated static files if they grow.

