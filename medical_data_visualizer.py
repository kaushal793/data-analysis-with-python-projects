import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def draw_cat_plot():
    # 1. Load data
    df = pd.read_csv("medical_examination.csv")

    # 2. Add overweight column
    df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

    # 3. Normalize cholesterol and gluc
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
    df["gluc"] = (df["gluc"] > 1).astype(int)

    # 4. Melt data
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # 5. Group and count
    df_cat = df_cat.groupby(
        ["cardio", "variable", "value"]
    ).size().reset_index(name="total")

    # 6. Draw cat plot
    fig = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="bar"
    ).fig

    return fig


def draw_heat_map():
    # 1. Load data
    df = pd.read_csv("medical_examination.csv")

    # 2. Clean data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 3. Correlation matrix
    corr = df_heat.corr()

    # 4. Mask upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 5. Plot heatmap
    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5
    )

    return fig