import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult_data.csv")

    # 1. 人種人數
    race_count = df['race'].value_counts()

    # 2. 男性人數
    men_count = df['sex'].value_counts()['Male']

    # 3. 學士學位比例 (%)
    bachelors_percentage = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. 高學歷收入比例 (>50K)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. 最少工時
    min_work_hours = df['hours-per-week'].min()

    # 6. 最少工時者 >50K 百分比
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. 哪個國家 >50K 比例最高
    country_rich = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean())
    highest_earning_country = country_rich.idxmax()
    highest_earning_country_percentage = round(country_rich.max() * 100, 1)

    # 8. 印度 >50K 最常見的職業
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Number of men:", men_count)
        print("Percentage with Bachelors degrees:", bachelors_percentage)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'men_count': men_count,
        'bachelors_percentage': bachelors_percentage,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()