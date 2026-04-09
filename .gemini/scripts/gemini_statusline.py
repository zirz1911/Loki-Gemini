#!/usr/bin/env python3
import sys, json, time, os, tempfile

sys.stdout.reconfigure(encoding="utf-8")

try:
    # Gemini CLI passes state as JSON to the status line command
    data = json.loads(sys.stdin.read())
except Exception:
    data = {}

# --- Extract Gemini-specific fields ---
# Note: Gemini CLI's JSON structure might differ from Claude Code
# Let's use a robust extraction pattern
cwd       = data.get("cwd") or os.getcwd()
model     = (data.get("model") or {}).get("name", "Gemini")
used_pct  = (data.get("context") or {}).get("used_percent", 0)
total_tok = (data.get("context") or {}).get("total_tokens", 0)
cost      = (data.get("session") or {}).get("total_cost", 0.0)
agent     = (data.get("agent") or {}).get("name", "Loki")

# --- ANSI colors ---
RST = "\033[0m"; BOLD = "\033[1m"; DIM = "\033[2m"
CYN = "\033[36m"; GLD = "\033[33m"; GRN = "\033[32m"
YLW = "\033[93m"; RED = "\033[31m"; MAG = "\033[95m"
BLU = "\033[94m"; TEAL = "\033[96m"

SEP = f" {DIM}│{RST} "

# --- Rune (cycles per second) ---
RUNES = "ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛞᛟ"
rune = RUNES[int(time.time()) % len(RUNES)]

# --- Shorten cwd ---
parts = cwd.replace("\\", "/").rstrip("/").split("/")
short = "/".join(parts[-2:]) if len(parts) >= 2 else (parts[-1] if parts else "~")

# --- Context bar ---
u = int(float(used_pct))
filled = u // 10
bar = "█" * filled + "░" * (10 - filled)
col = RED if u >= 80 else (YLW if u >= 50 else GRN)
ctx = f"{col}{bar} {u}%{RST}"

# --- Tokens & Cost ---
tok_str = f"{total_tok/1000:.1f}k" if total_tok >= 1000 else str(total_tok)
tok_display = f"{TEAL}{tok_str} tok{RST}"

cost_col = RED if cost >= 1.0 else (YLW if cost >= 0.1 else GRN)
cost_display = f"{cost_col}${cost:.4f}{RST}"

# --- Agent Icon Mapping ---
AGENT_MAP = {
    "thor":     ("⚡", "Thor"),
    "loki":     ("🔮", "Loki"),
    "heimdall": ("🌈", "Heimdall"),
    "tyr":      ("⚔️", "Tyr"),
    "ymir":     ("🏔️", "Ymir"),
    "odin":     ("👁️", "Odin"),
}
icon, name = AGENT_MAP.get(agent.lower(), ("🎭", agent))
agent_display = f"{MAG}{BOLD}{icon} {name}{RST}"

# --- Assemble ---
line = (
    f"{GLD}{rune}{RST} "
    f"{BOLD}{CYN}Loki-Gemini{RST}"
    f"{SEP}{YLW}{short}{RST}"
    f"{SEP}{BLU}{model}{RST}"
    f"{SEP}{ctx}"
    f"{SEP}{tok_display}"
    f"{SEP}{cost_display}"
    f"{SEP}{agent_display}"
)

print(line)
