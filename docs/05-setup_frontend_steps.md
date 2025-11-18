# 05 - Setup Frontend Steps for OctoFit Tracker

This document describes the steps to set up, update, and style the OctoFit Tracker frontend React application.

## 1. Create the React App
- Ensure the directory `octofit-tracker/frontend` exists.
- Create a new React app in this directory using Create React App with npm and the `--prefix` option.
- Install the required packages: `react`, `bootstrap`, and `react-router-dom`.
- Import Bootstrap CSS in `src/index.js` for global styles.

## 2. Update and Connect Components
- Create the following components in `src/components/`:
  - `Activities.js`
  - `Leaderboard.js`
  - `Teams.js`
  - `Users.js`
  - `Workouts.js`
- In each component, fetch data from the backend REST API using the Codespace URL:
  `https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/[component]/`
- Log the API endpoint and fetched data in each component.
- Ensure compatibility with both paginated (`.results`) and plain array responses.

## 3. Setup Navigation and Routing
- Update `src/App.js` to:
  - Use `react-router-dom` for navigation.
  - Add a Bootstrap-styled navigation bar with links to all main components.
  - Render each component at its route.
  - Show a welcome card on the home route.
  - Your React frontend is now fully integrated with the backend REST API and ready for use!

## 4. Style the App
- Use Bootstrap for all tables, buttons, headings, links, navigation, and cards.
- Customize `App.css` to:
  - Add a gradient background and modern color palette.
  - Style tables, buttons, headings, links, and navigation for a consistent look.
- Add the OctoFit logo to the navigation bar, justified left, and style it.
- Add a favicon and set a theme color for the app.

## 5. Fixes and Improvements
- Fixed logo import to use the public directory path in JSX.
- Added missing imports for React and `react-router-dom` in `App.js` to resolve runtime errors.

## 6. Result
- The OctoFit Tracker frontend is now visually appealing, fully functional, and integrated with the backend REST API.
- All documentation files in the `docs` directory are now numbered for clarity and sequence.

---
This document is part of the OctoFit Tracker documentation series.
