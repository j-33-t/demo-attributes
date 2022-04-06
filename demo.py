print("Hello World")


# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 9 (Jupyter Automated Reporting): Update Database ----

# IMPORTS ----

import pandas as pd
import numpy as np

from my_pandas_extensions.database import (
    collect_data,
    write_forecast_to_database,
    read_forecast_from_database,
    prep_forecast_data_for_update
)

from my_pandas_extensions.timeseries import summarize_by_time
from my_pandas_extensions.forecasting import arima_forecast, plot_forecast

df = collect_data()


# 1.0 SUMMARIZE AND FORECAST ----


# 1.1 Total Revenue ----

print("Forecast 1/4: Forecasting Total Revenue...\n")

forecast_1_df = df \
    .summarize_by_time(
        date_column  = "order_date",
        value_column = "total_price",
        rule         = "M",
        kind         = "period"
    ) \
    .arima_forecast(
        h  = 12,
        sp = 12
    )

forecast_1_df = forecast_1_df \
    .assign(id = "Total Revenue") \
    .prep_forecast_data_for_update(
        id_column   = "id",
        date_column = "order_date"
    )

print("Forecast 1/4: Forecasting Total Revenue Complete\n")

