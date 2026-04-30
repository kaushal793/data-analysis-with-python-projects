import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelors
    total_people = len(df)
    bachelors_percentage = round(
        (df[df["education"] == "Bachelors"].shape[0] / total_people) * 100, 1
    )

    # 4. Advanced education >50K
    advanced_edu = df["education"].isin(["Bachelors", "Masters", "Doctorate"])

    higher_edu_rich = round(
        (df[advanced_edu & (df["salary"] == ">50K")].shape[0] /
         df[advanced_edu].shape[0]) * 100,
        1
    )

    # 5. No advanced education >50K
    lower_edu = ~advanced_edu

    lower_edu_rich = round(
        (df[lower_edu & (df["salary"] == ">50K")].shape[0] /
         df[lower_edu].shape[0]) * 100,
        1
    )

    # 6. Minimum hours worked
    min_work_hours = df["hours-per-week"].min()

    # 7. Rich among min workers
    min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage_min_workers = round(
        (min_workers[min_workers["salary"] == ">50K"].shape[0] /
         min_workers.shape[0]) * 100,
        1
    )

    # 8. Country with highest % rich
    country_counts = df["native-country"].value_counts()
    rich_by_country = df[df["salary"] == ">50K"]["native-country"].value_counts()

    country_rich_percentage = (rich_by_country / country_counts) * 100
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. Top occupation in India for rich
    top_IN_occupation = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    # DO NOT CHANGE BELOW (FCC checks)
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", bachelors_percentage)
        print("Higher education rich percentage:", higher_edu_rich)
        print("Lower education rich percentage:", lower_edu_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage among min workers:", rich_percentage_min_workers)
        print("Country with highest percentage rich:", highest_earning_country)
        print("Highest percentage:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "bachelors_percentage": bachelors_percentage,
        "higher_education_rich": higher_edu_rich,
        "lower_education_rich": lower_edu_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage_min_workers": rich_percentage_min_workers,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }