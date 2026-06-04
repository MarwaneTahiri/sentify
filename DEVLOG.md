## Day 1 - 20/05/26
- Set up Flask server
- Created HTML form with textarea
- Added POST route to receive form data

## Day 2 - 21/05/26
- Integrated HuggingFace distilbert sentiment model
- Core pipeline working end to end: 
  user text → Flask → model → result displayed
- Created DEVLOG.md to track development progress
- Discussed finished product scope and roadmap
- Decided to keep positive/negative for now and upgrade to emotion detection in Phase 2

## Day 3 - 02/06/26
- Extracted label and score from HuggingFace model output
- Created result.html template to display sentiment result
- Result now shows label and rounded confidence percentage

## Day 4 - 04/06/26
- Added "Analyse another text" link on result page
- Added empty text validation — redirects to home if empty or whitespace only
- Model now only runs on valid input

## Day 5 - 05/06/26
- Added CSS styling to both pages
- Centred layout, accent button colour, clean typography
- Result page styled to match home page