


# IMPORTS ----

import pandas as pd
import numpy as np






print("Forecast 1/4: Forecasting Total Revenue...\n")


forecast_1_df = forecast_1_df \
    .assign(id = "Total Revenue") \
    .prep_forecast_data_for_update(
        id_column   = "id",
        date_column = "order_date"
    )


