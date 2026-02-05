import json
import os
from datetime import date

DATA_FILE = "data/streaks.json"
SUB_FILE = "data/subscriptions.json"
OUTPUT_FILE = "output/dashboard.md"

today = str(date.today())

os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

# Load subscriptions
with open(SUB_FILE, "r") as f:
    subs = json.load(f)["subscriptions"]

# Load streak data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        streaks = json.load(f)
else:
    streaks = {}

# Initialize subscriptions
for sub in subs:
    streaks.setdefault(sub, {})

# Ask user input (default = missed)
for sub in subs:
    if today not in streaks[sub]:
        streaks[sub][today] = "🟥"

# Save streak data
with open(DATA_FILE, "w") as f:
    json.dump(streaks, f, indent=2)

# Generate dashboard
lines = ["# 📊 Streak Matrix\n"]
lines.append(f"Last updated: **{today}**\n")

for sub, days in streaks.items():
    lines.append(f"## {sub}")
    row = ""
    for d in sorted(days.keys())[-30:]:
        row += days[d]
    lines.append(row + "\n")

with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(lines))
