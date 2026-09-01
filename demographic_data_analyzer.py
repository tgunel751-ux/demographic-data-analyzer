import pandas as pd
def calculate_demografic_data(print_data=True):
df=pd.read_csv("adult.data.csv")
race_count=df["race"].value_counts()
average_age_man= round(df[(df["sex"]== "Male")]["age"].mean(),1)
percentage_of_Bachelors= round(df[df["edeucation"]=="Bachelors"].mean()*100,1)
higher_education=df["education"].isin(["Bachelors","Masters","Doctorate"])
lower_education= ~higher_education
higher_education_rich=round((df[higher_education]["salary"]==">50K").mean()*100,1)
lower_education_rich=round((df[lower_education]["salary"]==">50K").mean()*100,1)
num_min_work_hours=df["hours-per-week"].min()
num_min_workers1=df[df["hours-per-week"]==num_min_work_hours]
percentage_min_workers=round((df[num_min_workers1]["salary"]==">50K") .mean()*100,1)
country_counts=df["native-country"].value_counts()
rich_country_counts=df[df["salary"]==">50K"]["native-country"].value_counts()
highest_earning_country_percentage_series=(rich_country_counts/country_counts)*100
highest_earning_country=highest_earning_country_percentage_series.idxmax()
highest_earning_country_percentage=round(
    highest_earning_country_percentage_series.max(),1
)
top_IN_occupation=(
    df[(df["native-country"]=="India")&(df["salary"]==">50K")]["occupation"].value_counts().idxmax()
)
if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_man)
        print(f"Percentage with Bachelor's degrees: {percentage_of_Bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {num_min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {percentage_min_workers}%"
        )
        print(
            "Country with highest percentage of rich:", highest_earning_country
        )
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_man,
        "percentage_bachelors": percentage_of_Bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": num_min_work_hours,
        "rich_percentage": percentage_min_workers,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
