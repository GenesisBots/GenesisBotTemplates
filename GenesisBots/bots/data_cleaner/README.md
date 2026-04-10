# Data Cleaner Bot

**Type:** Automation / AI

This is a template bot designed to be:

- Easy to read
- Easy to modify
- Safe by default (PAPER mode)

## Modes

This bot supports two modes:

- paper (default): no real orders are sent. Safe for testing.
- live: real orders are sent to your broker or service. Use at your own risk.

You control the mode in config.example.json:

    "mode": "paper"

To go live:

1. Change "mode" to "live".
2. Export your broker or API keys as environment variables.
3. Start with very small size and test carefully.

## Configuration

The config file config.example.json contains:

- name: human-readable bot name
- mode: "paper" or "live"
- broker or service: which backend to use
- Strategy- or task-specific parameters

Copy config.example.json to config.json and edit that file for your own use.

## API Keys

This template does not include any keys.

You are expected to set environment variables like:

- ALPACA_API_KEY, ALPACA_API_SECRET
- or other keys depending on the broker/service you integrate

## Running

Basic pattern:

    pip install -r requirements.txt
    python bot.py
