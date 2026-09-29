"""
FRED Economic Dashboard
Author: Dora Ayan

This project retrieves economic data from the Federal Reserve
Economic Data (FRED) database and visualizes key U.S. economic
indicators using Python.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from pandas_datareader import data as web


# -----------------------------
# Date Range
# -----------------------------

start_date = "2015-01-01"
end_date = datetime.today()

# -----------------------------
# Retrieve Data from FRED
# -----------------------------

inflation = web.DataReader(
    "CPIAUCSL",
    "fred",
    start_date,
    end_date
)

unemployment = web.DataReader(
    "UNRATE",
    "fred",
    start_date,
    end_date
)

fed_funds = web.DataReader(
    "FEDFUNDS",
    "fred",
    start_date,
    end_date
)

# -----------------------------
# Create Dashboard
# -----------------------------

fig, axs = plt.subplots(
    3,
    1,
    figsize=(12, 10)
)

# Inflation

axs[0].plot(
    inflation.index,
    inflation["CPIAUCSL"],
    color="blue",
    linewidth=2
)

axs[0].set_title(
    "Consumer Price Index (Inflation Proxy)"
)

axs[0].set_ylabel("CPI")
axs[0].grid(True)

# Unemployment

axs[1].plot(
    unemployment.index,
    unemployment["UNRATE"],
    color="green",
    linewidth=2
)

axs[1].set_title(
    "U.S. Unemployment Rate"
)

axs[1].set_ylabel("%")
axs[1].grid(True)

# Federal Funds Rate

axs[2].plot(
    fed_funds.index,
    fed_funds["FEDFUNDS"],
    color="red",
    linewidth=2
)

axs[2].set_title(
    "Federal Funds Rate"
)

axs[2].set_ylabel("%")
axs[2].set_xlabel("Year")
axs[2].grid(True)

# -----------------------------
# Save and Display
# -----------------------------

plt.tight_layout()

plt.savefig(
    "fred_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("Dashboard saved as fred_dashboard.png")

plt.show()
