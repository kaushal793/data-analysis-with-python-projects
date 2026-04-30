import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Load data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="black")

    # 3. First line of best fit (entire dataset)
    slope, intercept, _, _, _ = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )

    years_extended = pd.Series(range(df["Year"].min(), 2051))
    ax.plot(
        years_extended,
        intercept + slope * years_extended,
        "r",
        label="Best fit (all data)"
    )

    # 4. Second line of best fit (from year 2000)
    df_2000 = df[df["Year"] >= 2000]

    slope_2000, intercept_2000, _, _, _ = linregress(
        df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"]
    )

    years_2000_extended = pd.Series(range(2000, 2051))
    ax.plot(
        years_2000_extended,
        intercept_2000 + slope_2000 * years_2000_extended,
        "green",
        label="Best fit (2000+)"
    )

    # 5. Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Optional legend (not required but helpful)
    ax.legend()

    # Save and return figure
    fig.savefig("sea_level_plot.png")

    return fig
