# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Entry: 120 chars](https://img.shields.io/badge/entry-120%20chars-brightgreen)](main.py)

One line of weather forecast (120 characters) for a city that does not exist — Snuzzleford — written for the make.fun bounty
[u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e).

## The entry

> In Snuzzleford, light snow spells out the train times in the sky — 7:42 on time, 8:15 delayed by a very polite blizzard.

## How it works

`main.py` writes that single line, deterministically, to `/output/entry.txt`. No network, no randomness, no time dependence — the same bytes on every run.

## Why this line

Chosen after three review rounds over ten candidates (see `REVIEW.md` in the work dir): the snow itself spells out the train times, so the weather is the whole point; the payoff — a *very polite blizzard* delaying the 8:15 — is a small joke a bored commuter smiles at on one reading; and it keeps the register of a real forecast (times, delay, a named invented city).

## License

MIT
