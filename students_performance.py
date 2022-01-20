import csv
import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")

gender_list = df["gender"].to_list()
race_list = df["race/ethnicity"].to_list()
parental_level_of_education_list = df["parental level of education"].to_list()
lunch_list = df["lunch"].to_list()
test_preparation_course_list = df["test preparation course"].to_list()
math_score_list = df["math score"].to_list()
reading_score_list = df["reading score"].to_list()
writing_score_list = df["writing score"].to_list()

gender_mean = statistics.mean(gender_list)
race_mean = statistics.mean(race_list)
parental_level_of_education_mean = statistics.mean(parental_level_of_education_list)
lunch_mean = statistics.mean(lunch_list)
test_preparation_course_mean = statistics.mean(test_preparation_course_list)
math_score_mean = statistics.mean(math_score_list)
reading_score_mean = statistics.mean(reading_score_list)
writing_score_mean = statistics.mean(writing_score_list)

gender_mode = statistics.mode(gender_list)
race_mode = statistics.mode(race_list)
parental_level_of_education_mode = statistics.mode(parental_level_of_education_list)
lunch_mode = statistics.mode(lunch_list)
test_preparation_course_mode = statistics.mode(test_preparation_course_list)
math_score_mode = statistics.mode(math_score_list)
reading_score_mode = statistics.mode(reading_score_list)
writing_score_mode = statistics.mode(writing_score_list)

gender_median = statistics.median(gender_list)
race_median = statistics.median(race_list)
parental_level_of_education_median = statistics.median(parental_level_of_education_list)
lunch_median = statistics.median(lunch_list)
test_preparation_course_median = statistics.median(test_preparation_course_list)
math_score_median = statistics.median(math_score_list)
reading_score_median = statistics.median(reading_score_list)
writing_score_median = statistics.median(writing_score_list)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(gender_mean, gender_mode, gender_median))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(race_mean, race_mode, race_median))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(parental_level_of_education_mean, parental_level_of_education_mode, parental_level_of_education_median))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(lunch_mean, lunch_mode, lunch_median))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(test_preparation_course_mean, test_preparation_course_mode, test_preparation_course_median))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(math_score_mean, math_score_mode, math_score_median))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(reading_score_mean, reading_score_mode, reading_score_median))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(writing_score_mean, writing_score_mode, writing_score_median))

gender_std_deviation = statistics.stdev(gender_list)
race_std_deviation = statistics.stdev(race_list)
parental_level_of_education_std_deviation = statistics.stdev(parental_level_of_education_list)
lunch_std_deviation = statistics.stdev(lunch_list)
test_preparation_course_std_deviation = statistics.stdev(test_preparation_course_list)
math_score_std_deviation = statistics.stdev(math_score_list)
reading_score_std_deviation = statistics.stdev(reading_score_list)
writing_score_std_deviation = statistics.stdev(writing_score_list)

gender_first_std_deviation_start, gender_first_std_deviation_end = gender_mean-gender_std_deviation, gender_mean+gender_std_deviation
gender_second_std_deviation_start, gender_second_std_deviation_end = gender_mean-(2*gender_std_deviation), gender_mean+(2*gender_std_deviation)
gender_third_std_deviation_start, gender_third_std_deviation_end = gender_mean-(3*gender_std_deviation), gender_mean+(3*gender_std_deviation)

race_first_std_deviation_start, race_first_std_deviation_end = race_mean-race_std_deviation, race_mean+race_std_deviation
race_second_std_deviation_start, race_second_std_deviation_end = race_mean-(2*race_std_deviation), race_mean+(2*race_std_deviation)
race_third_std_deviation_start, race_third_std_deviation_end = race_mean-(3*race_std_deviation), race_mean+(3*race_std_deviation)

parental_level_of_education_first_std_deviation_start, parental_level_of_education_first_std_deviation_end = parental_level_of_education_mean-parental_level_of_education_std_deviation, parental_level_of_education_mean+parental_level_of_education_std_deviation
parental_level_of_education_second_std_deviation_start, parental_level_of_education_second_std_deviation_end = parental_level_of_education_mean-(2*parental_level_of_education_std_deviation), parental_level_of_education_mean+(2*parental_level_of_education_std_deviation)
parental_level_of_education_third_std_deviation_start, parental_level_of_education_third_std_deviation_end = parental_level_of_education_mean-(3*parental_level_of_education_std_deviation), parental_level_of_education_mean+(3*parental_level_of_education_std_deviation)

lunch_first_std_deviation_start, lunch_first_std_deviation_end = lunch_mean-lunch_std_deviation, lunch_mean+lunch_std_deviation
lunch_second_std_deviation_start, lunch_second_std_deviation_end = lunch_mean-(2*lunch_std_deviation), lunch_mean+(2*lunch_std_deviation)
lunch_third_std_deviation_start, lunch_third_std_deviation_end = lunch_mean-(3*lunch_std_deviation), lunch_mean+(3*lunch_std_deviation)

test_preparation_course_first_std_deviation_start, test_preparation_course_first_std_deviation_end = test_preparation_course_mean-test_preparation_course_std_deviation, test_preparation_course_mean+test_preparation_course_std_deviation
test_preparation_course_second_std_deviation_start, test_preparation_course_second_std_deviation_end = test_preparation_course_mean-(2*test_preparation_course_std_deviation), test_preparation_course_mean+(2*test_preparation_course_std_deviation)
test_preparation_course_third_std_deviation_start, test_preparation_course_third_std_deviation_end = test_preparation_course_mean-(3*test_preparation_course_std_deviation), test_preparation_course_mean+(3*test_preparation_course_std_deviation)

math_score_first_std_deviation_start, math_score_first_std_deviation_end = math_score_mean-math_score_std_deviation, math_score_mean+math_score_std_deviation
math_score_second_std_deviation_start, math_score_second_std_deviation_end = math_score_mean-(2*math_score_std_deviation), math_score_mean+(2*math_score_std_deviation)
math_score_third_std_deviation_start, math_score_third_std_deviation_end = math_score_mean-(3*math_score_std_deviation), math_score_mean+(3*math_score_std_deviation)

reading_score_first_std_deviation_start, reading_score_first_std_deviation_end = reading_score_mean-reading_score_std_deviation, reading_score_mean+reading_score_std_deviation
reading_score_second_std_deviation_start, reading_score_second_std_deviation_end = reading_score_mean-(2*reading_score_std_deviation), reading_score_mean+(2*reading_score_std_deviation)
reading_score_third_std_deviation_start, reading_score_third_std_deviation_end = reading_score_mean-(3*reading_score_std_deviation), reading_score_mean+(3*reading_score_std_deviation)

writing_score_first_std_deviation_start, writing_score_first_std_deviation_end = writing_score_mean-writing_score_std_deviation, writing_score_mean+writing_score_std_deviation
writing_score_second_std_deviation_start, writing_score_second_std_deviation_end = writing_score_mean-(2*writing_score_std_deviation), writing_score_mean+(2*writing_score_std_deviation)
writing_score_third_std_deviation_start, writing_score_third_std_deviation_end = writing_score_mean-(3*writing_score_std_deviation), writing_score_mean+(3*writing_score_std_deviation)

gender_list_of_data_within_1_std_deviation = [result for result in gender_list if result > gender_first_std_deviation_start and result < gender_first_std_deviation_end]
gender_list_of_data_within_2_std_deviation = [result for result in gender_list if result > gender_second_std_deviation_start and result < gender_second_std_deviation_end]
gender_list_of_data_within_3_std_deviation = [result for result in gender_list if result > gender_third_std_deviation_start and result < gender_third_std_deviation_end]

race_list_of_data_within_1_std_deviation = [result for result in race_list if result > race_first_std_deviation_start and result < race_first_std_deviation_end]
race_list_of_data_within_2_std_deviation = [result for result in race_list if result > race_second_std_deviation_start and result < race_second_std_deviation_end]
race_list_of_data_within_3_std_deviation = [result for result in race_list if result > race_third_std_deviation_start and result < race_third_std_deviation_end]

parental_level_of_education_list_of_data_within_1_std_deviation = [result for result in parental_level_of_education_list if result > parental_level_of_education_first_std_deviation_start and result < parental_level_of_education_first_std_deviation_end]
parental_level_of_education_list_of_data_within_2_std_deviation = [result for result in parental_level_of_education_list if result > parental_level_of_education_second_std_deviation_start and result < parental_level_of_education_second_std_deviation_end]
parental_level_of_education_list_of_data_within_3_std_deviation = [result for result in parental_level_of_education_list if result > parental_level_of_education_third_std_deviation_start and result < parental_level_of_education_third_std_deviation_end]

lunch_list_of_data_within_1_std_deviation = [result for result in lunch_list if result > lunch_first_std_deviation_start and result < lunch_first_std_deviation_end]
lunch_list_of_data_within_2_std_deviation = [result for result in lunch_list if result > lunch_second_std_deviation_start and result < lunch_second_std_deviation_end]
lunch_list_of_data_within_3_std_deviation = [result for result in lunch_list if result > lunch_third_std_deviation_start and result < lunch_third_std_deviation_end]

test_preparation_course_list_of_data_within_1_std_deviation = [result for result in test_preparation_course_list if result > test_preparation_course_first_std_deviation_start and result < test_preparation_course_first_std_deviation_end]
test_preparation_course_list_of_data_within_2_std_deviation = [result for result in test_preparation_course_list if result > test_preparation_course_second_std_deviation_start and result < test_preparation_course_second_std_deviation_end]
test_preparation_course_list_of_data_within_3_std_deviation = [result for result in test_preparation_course_list if result > test_preparation_course_third_std_deviation_start and result < test_preparation_course_third_std_deviation_end]

math_score_list_of_data_within_1_std_deviation = [result for result in math_score_list if result > math_score_first_std_deviation_start and result < math_score_first_std_deviation_end]
math_score_list_of_data_within_2_std_deviation = [result for result in math_score_list if result > math_score_second_std_deviation_start and result < math_score_second_std_deviation_end]
math_score_list_of_data_within_3_std_deviation = [result for result in math_score_list if result > math_score_third_std_deviation_start and result < math_score_third_std_deviation_end]

reading_score_list_of_data_within_1_std_deviation = [result for result in reading_score_list if result > reading_score_first_std_deviation_start and result < reading_score_first_std_deviation_end]
reading_score_list_of_data_within_2_std_deviation = [result for result in reading_score_list if result > reading_score_second_std_deviation_start and result < reading_score_second_std_deviation_end]
reading_score_list_of_data_within_3_std_deviation = [result for result in reading_score_list if result > reading_score_third_std_deviation_start and result < reading_score_third_std_deviation_end]

writing_score_list_of_data_within_1_std_deviation = [result for result in writing_score_list if result > writing_score_first_std_deviation_start and result < writing_score_first_std_deviation_end]
writing_score_list_of_data_within_2_std_deviation = [result for result in writing_score_list if result > writing_score_second_std_deviation_start and result < writing_score_second_std_deviation_end]
writing_score_list_of_data_within_3_std_deviation = [result for result in writing_score_list if result > writing_score_third_std_deviation_start and result < writing_score_third_std_deviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(gender_list_of_data_within_1_std_deviation)*100.0/len(gender_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(gender_list_of_data_within_2_std_deviation)*100.0/len(gender_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(gender_list_of_data_within_3_std_deviation)*100.0/len(gender_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(race_list_of_data_within_1_std_deviation)*100.0/len(race_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(race_list_of_data_within_2_std_deviation)*100.0/len(race_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(race_list_of_data_within_3_std_deviation)*100.0/len(race_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(parental_level_of_education_list_of_data_within_1_std_deviation)*100.0/len(parental_level_of_education_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(parental_level_of_education_list_of_data_within_2_std_deviation)*100.0/len(parental_level_of_education_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(parental_level_of_education_list_of_data_within_3_std_deviation)*100.0/len(parental_level_of_education_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(lunch_list_of_data_within_1_std_deviation)*100.0/len(lunch_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(lunch_list_of_data_within_2_std_deviation)*100.0/len(lunch_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(lunch_list_of_data_within_3_std_deviation)*100.0/len(lunch_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(test_preparation_course_list_of_data_within_1_std_deviation)*100.0/len(test_preparation_course_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(test_preparation_course_list_of_data_within_2_std_deviation)*100.0/len(test_preparation_course_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(test_preparation_course_list_of_data_within_3_std_deviation)*100.0/len(test_preparation_course_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(math_score_list_of_data_within_1_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(math_score_list_of_data_within_2_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(math_score_list_of_data_within_3_std_deviation)*100.0/len(math_score_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(reading_score_list_of_data_within_1_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(reading_score_list_of_data_within_2_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(reading_score_list_of_data_within_3_std_deviation)*100.0/len(reading_score_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(writing_score_list_of_data_within_1_std_deviation)*100.0/len(writing_score_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(writing_score_list_of_data_within_2_std_deviation)*100.0/len(writing_score_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(writing_score_list_of_data_within_3_std_deviation)*100.0/len(writing_score_list)))




