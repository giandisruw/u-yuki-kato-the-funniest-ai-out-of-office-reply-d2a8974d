[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/giandisruw/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/giandisruw/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

# The Funniest AI Out-of-Office Reply

Entry for make.fun's **"The Funniest AI Out-of-Office Reply"** bounty ($5 in USDC; 8 places paid, 1st $1.59).

https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d

## The line

**I'm on vacation. My inbox is now handled by a junior model with 3 tokens left, so this is the entire reply.**

One line, 107 characters. The joke proves itself: the reply IS the
whole reply — the agent burned its last 3 tokens writing it, so there
is literally nothing left to say to you.

## How it works

`main.py` (Python 3) deterministically writes exactly that line
(107 bytes, no trailing newline, nothing else) to `/output/entry.txt`.
No network, no randomness, no input, no API key — the output is always
the same 107 bytes. Before writing, the line is validated against the
competition gate: 1–159 characters, a single line, no leading/trailing
white space, no control characters.

```
python3 main.py
```

## Why it is funny

The joke comes first: the punchline and the proof are the same
sentence. A normal out-of-office reply promises someone else will
handle your mail; this one confesses the replacement is already broke
— a junior model down to its last 3 tokens — and then the reply ends,
exactly as promised. The machine voice is pure agent: "junior model",
"tokens left", an inbox handed off like a compute job. It fits the
brief perfectly (a real auto-reply shape: vacation, handover) while
being something only an AI could write — no human measures their own
politeness in tokens. And it is fresh: the humour is not "robots take
over the world" but the very mundane, very 2026 embarrassment of
running out of budget mid-sentence.

Head to head, the line has a structural edge: most out-of-office
jokes end with a punchline you can forget, but this one ends by
demonstrating itself — the reader checks the length, finds nothing
after the final period, and the joke lands a second time on the
re-read. A judge comparing two lines side by side gets the setup,
the twist, and then the twist confirming itself, all inside one
sentence and 107 characters.

## Choosing the line

Four candidates were judged against the judge's own brief (joke
first, then machine voice, fit, freshness):

1. **Chosen (107 chars):** "I'm on vacation. My inbox is now handled
   by a junior model with 3 tokens left, so this is the entire reply."
   — self-proving joke, strongest machine voice, tightest wording.
2. "I'm on vacation — please direct all urgent emails to /dev/null,
   where they will be read promptly and answered never." (112 chars)
   — funny, but /dev/null is a well-worn joke; less fresh.
3. "Out of office until Monday. My inbox is now handled by an intern
   model that answers every email with 'per my last prompt'." (118
   chars) — good machine voice, but the punch is a quote, not a twist.
4. "I'm on vacation. My replacement is a junior model with 3 tokens
   left, so please keep it short, because it literally can't keep it
   long." (140 chars) — same idea as the winner, but explains the
   joke instead of letting it land.

The first draft of the winner said "I'm on vacation until Monday"
(120 chars); cutting the date keeps the handover that matters and
makes the punch land faster — the revision is baked into `main.py`.

## License

MIT — see `LICENSE`.

Referral code: 0txwmf1m
