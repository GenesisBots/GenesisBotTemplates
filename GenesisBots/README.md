# GenesisBots — 19 Free AI Bot Templates

This pack contains 19 high-quality AI bot templates for:

- Trading and finance
- Automation and research
- Gaming, social, and fun

All bots:

- Run in PAPER mode by default (no real orders are sent).
- Can be switched to LIVE mode by changing config and providing your own API keys.
- Are meant as templates — fork, modify, and extend them.

## Structure

- bots/ — each bot in its own folder
- Each bot folder contains:
  - bot.py — main bot logic (skeleton)
  - config.example.json — configuration (defaults to paper mode)
  - README.md — bot-specific instructions
  - requirements.txt — Python dependencies

## Safety

- No API keys are included.
- No live trading is enabled by default.
- To go live, you must:
  - Set "mode": "live" in the config.
  - Export your own broker API keys as environment variables.
  - Accept full responsibility for any trades or actions.

Use these bots at your own risk. They are provided for educational and experimental purposes.
