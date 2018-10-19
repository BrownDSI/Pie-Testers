import pandas as pd
% matplotlib inline

# plt.style.use('seaborn-whitegrid')

play = pd.read_csv('/Users/chuwu/Desktop/project1/play_sample_data.csv')

growth_rate = pd.read_csv(
    '/Users/chuwu/Desktop/project1/datasets/population_growth_annual_percent.csv')
mortality = pd.read_csv(
    '/Users/chuwu/Desktop/project1/datasets/child_mortality_0_5_year_olds_dying_per_1000_born.csv')
food = pd.read_csv(
    '/Users/chuwu/Desktop/project1/datasets/food_supply_kilocalories_per_person_and_day.csv')
income = pd.read_csv(
    '/Users/chuwu/Desktop/project1/datasets/income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
gdp = pd.read_csv(
    '/Users/chuwu/Desktop/project1/datasets/gdppercapita_us_inflation_adjusted.csv')
hdi = pd.read_csv(
    '/Users/chuwu/Desktop/project1/datasets/hdi_human_development_index.csv')
unemployment = pd.read_csv(
    '/Users/chuwu/Desktop/project1/datasets/long_term_unemployment_rate_percent.csv')
policy = pd.read_csv(
    '/Users/chuwu/Desktop/project1/datasets/population_policies_aid_given_percent_of_aid.csv')
