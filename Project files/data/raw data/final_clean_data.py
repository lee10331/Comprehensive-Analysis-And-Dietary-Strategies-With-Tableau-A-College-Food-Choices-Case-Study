import pandas as pd

# Load the dataset
df = pd.read_csv("cleaned_food_choices.csv")

# Define decoding dictionaries
fruit_day_map = {1: "1 or less", 2: "2", 3: "3", 4: "4", 5: "5 or more"}
grade_level_map = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior", 5: "Graduate"}
healthy_feeling_map = {1: "Very Unhealthy", 2: "Unhealthy", 3: "Neutral", 4: "Healthy", 5: "Very Healthy"}
income_map = {1: "Less than $20k", 2: "$20k–$40k", 3: "$40k–$60k", 4: "$60k–$80k", 5: "$80k–$100k", 6: "More than $100k"}
marital_status_map = {1: "Single", 2: "Married", 3: "Divorced", 4: "Widowed"}
education_map = {1: "No High School", 2: "High School", 3: "Some College", 4: "Bachelor", 5: "Postgrad"}
veggies_day_map = {1: "1 or less", 2: "2", 3: "3", 4: "4", 5: "5 or more"}
exercise_map = {1: "Every day", 2: "Few times a week", 3: "Once a week", 4: "Rarely", 5: "Never"}
employment_map = {1: "Unemployed", 2: "Part-time", 3: "Full-time", 4: "Self-employed", 5: "Student"}
eating_changes_map = {1: "No change", 2: "Healthier eating", 3: "Unhealthier eating"}
eating_out_map = {1: "Every day", 2: "4–5 times a week", 3: "1–3 times a week", 4: "Rarely", 5: "Never"}

# Decode by replacing the original columns
df['fruit_day1'] = df['fruit_day'].map(fruit_day_map)
df['grade_level1'] = df['grade_level'].map(grade_level_map)
df['healthy_feeling1'] = df['healthy_feeling'].map(healthy_feeling_map)
df['income1'] = df['income'].map(income_map)
df['marital_status1'] = df['marital_status'].map(marital_status_map)
df['mother_education1'] = df['mother_education'].map(education_map)
df['father_education1'] = df['father_education'].map(education_map)
df['veggies_day1'] = df['veggies_day'].map(veggies_day_map)
df['exercise1'] = df['exercise'].map(exercise_map)
df['employment1'] = df['employment'].map(employment_map)
df['eating_change1'] = df['eating_change'].map(eating_changes_map)
df['eating_ou1t'] = df['eating_out'].map(eating_out_map)

# Define likelihood scale
likelihood_map = {
    1: "Very Unlikely",
    2: "Unlikely",
    3: "Neutral",
    4: "Likely",
    5: "Very Likely"
}

# Apply to all specified columns
df['fav_food1'] = df['fav_food'].map(likelihood_map)
df['greek_food1'] = df['greek_food'].map(likelihood_map)
df['indian_food1'] = df['indian_food'].map(likelihood_map)
df['ethnic_food1'] = df['ethnic_food'].map(likelihood_map)
df['italian_food1'] = df['italian_food'].map(likelihood_map)
df['persian_food1'] = df['persian_food'].map(likelihood_map)
df['thai_food1'] = df['thai_food'].map(likelihood_map)

df.drop([
    'cook','cuisine','drink','eating_out','fruit_day','income','employment','exercise',
    'father_education','fries','grade_level','healthy_feeling','life_rewarding','marital_status',
    'mother_education','nutritional_check','parents_cook','pay_meal_out','soup',
    'self_perception_weight','veggies_day'
], axis=1, inplace=True, errors='ignore')

# Drop original coded columns we just decoded (food preference scale)
df.drop([
    'fav_food',
    'greek_food',
    'indian_food',
    'ethnic_food',
    'italian_food',
    'persian_food',
    'thai_food'
], axis=1, inplace=True)

# Save to a new cleaned file
df.to_csv("decoded_food_choices.csv", index=False)

print("✅ Fully decoded and replaced. Saved as 'decoded_food_choices.csv'")
