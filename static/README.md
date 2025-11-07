# Static Module

## Purpose
Store style sheets and other assets that Flask serves directly to the browser. These files control the look and feel of the calculator without changing server logic.

## Key Files
- `style.css`: Main stylesheet responsible for calculator layout, typography, and button styling.

## Dependencies & Assumptions
- Referenced by templates through `url_for('static', filename='style.css')`; file names must stay in sync.
- No build tooling (Webpack, Sass, etc.) is configured—assets should remain plain CSS/JS.
- Browser caches may need to be cleared when you change large styling elements.

## Usage Tips
- Keep selectors scoped to the calculator markup to avoid future conflicts.
- Add new static resources here and reference them in the relevant templates to ensure Flask can serve them.

