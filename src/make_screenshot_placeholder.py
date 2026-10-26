"""Draw the "YOUR screenshot here" image used in the fictional sample entries.

The sample entries show where each run screenshot goes. Your own log uses a
real screenshot of the program running on your own computer instead.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
# In the repository the image goes in report/; copied on its own, next to the script.
REPORT = HERE.parent / "report" if (HERE.parent / "report").is_dir() else HERE
OUTPUT = REPORT / "screenshot-placeholder.png"

fig = plt.figure(figsize=(6.4, 2.4), dpi=150)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.add_patch(plt.Rectangle((0.01, 0.02), 0.98, 0.96, facecolor="#f2f2f2",
                           edgecolor="#555555", linewidth=2, linestyle=(0, (6, 4))))
ax.text(0.5, 0.62, "YOUR screenshot here", ha="center", va="center",
        fontsize=24, fontweight="bold", color="#222222")
ax.text(0.5, 0.33, "Run the program on your own computer and show its output.",
        ha="center", va="center", fontsize=11, color="#333333")
fig.savefig(OUTPUT)
plt.close(fig)
print(f"Saved {OUTPUT.parent.name}/{OUTPUT.name}")
