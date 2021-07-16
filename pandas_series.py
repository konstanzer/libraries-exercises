import pandas as pd
import numpy as np

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple",
		"gala apple", "honeycrisp apple", "tomato", "watermelon",
		"honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry",
		"blackberry", "gooseberry", "papaya"])
"""
Capitalize all the string values in fruits.
Count the letter "a" in all the string values (use string vectorization).
Output the number of vowels in each and every string value.
Write the code to get the longest string value from fruits.
Write the code to get the string values with 5 or more letters in the name.
Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
Write the code to get only the string values containing the substring "berry".
Write the code to get only the string values containing the substring "apple".
Which string value contains the most vowels?
"""
#are we really analyzing a random string of letters?
#any conclusion will be pointless a priori
#if it was an encoded message, that would be cool
s = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyf\
	fsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwej\
	ilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypu\
	lzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyec\
	uproguy'
"""
Which letter occurs the most frequently in the letters Series?
Which letter occurs the Least frequently?
How many vowels are in the Series?
How many consonants are in the Series?
Create a Series that has all of the same letters but uppercased.
Create a bar plot of the frequencies of the 6 most commonly occuring letters.
"""
n = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98',
	'$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45',
	'$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17',
	'$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54',
	'$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

"""
What is the data type of the numbers Series?
How many elements are in the number Series?
Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
Run the code to discover the maximum value from the Series.
Run the code to discover the minimum value from the Series.
What is the range of the values in the Series?
Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
"""

exam = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81,
		96, 80, 85, 92, 82, 78]

"""
How many elements are in the exam_scores Series?
Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
Use a method to convert each of the numeric values in the curved_grades Series into a categorical vale of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
"""


if __name__ == '__main__':
	print(fruits.index)
	print(fruits.values)
	#shows unique (7-10)
	print(fruits.value_counts())
	#shows total
	print(fruits.describe())
	print(fruits.dtypes)
	print(fruits[-3:])
	print([fruits[i] for i in np.random.choice(fruits.index, 2)])


