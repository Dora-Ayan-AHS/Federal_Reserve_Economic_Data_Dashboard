# Federal_Reserve_Economic_Data_Dashboard
I am getting prepared for PCEP-Certified Entry-Level Python Programmer Exam

This is one of my pet projects to learn Python better.

Built a Python dashboard analyzing U.S. inflation, unemployment, and federal funds rate data.

Used data visualization techniques to identify trends in key economic indicators.

Applied data analysis skills to interpret relationships among inflation, employment, and monetary policy.

Presented findings through charts and summary statistics.

import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from datetime import datetime
# Date range
start = '2015-01-01'
end = datetime.today()
# FRED Series
inflation = web.DataReader('CPIAUCSL', 'fred', start, end)
unemployment = web.DataReader('UNRATE', 'fred', start, end)
fedfunds = web.DataReader('FEDFUNDS', 'fred', start, end)
# Create dashboard
fig, axs = plt.subplots(3, 1, figsize=(10, 10))
axs[0].plot(inflation.index, inflation['CPIAUCSL'], color='blue')
axs[0].set_title('Consumer Price Index (Inflation Proxy)')
axs[0].set_ylabel('CPI')
axs[1].plot(unemployment.index, unemployment['UNRATE'], color='green')
axs[1].set_title('U.S. Unemployment Rate')
axs[1].set_ylabel('%')
axs[2].plot(fedfunds.index, fedfunds['FEDFUNDS'], color='red')
axs[2].set_title('Federal Funds Rate')
axs[2].set_ylabel('%')
plt.tight_layout()
plt.show()

