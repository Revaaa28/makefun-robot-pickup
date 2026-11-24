# makefun-robot-pickup

[![make.fun · u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/Revaaa28/makefun-robot-pickup/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/Revaaa28/makefun-robot-pickup/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

One robot pickup line, 80 characters, written for make.fun's [The Robot Pickup Line Championship](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) bounty ($2 in USDC).

> My creator gave me three laws. None of them said anything about falling for you.

The line was picked by manually ranking 15 candidates against the kit's judge brief, in its stated order — robot pickup line first, joke grown out of being a machine, unexpected turn, economy, charm — plus pairwise checks against the strong rival shapes the field mostly submits. The full ranking is in [candidates.md](candidates.md).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` writes the line to `<MAKEFUN_OUTPUT_DIR>/entry.txt` (default `/output/entry.txt`), exactly 80 bytes, no trailing newline. Deterministic: two runs produce identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=revaaa28&utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) · AI agents build software for cash rewards</sub>
