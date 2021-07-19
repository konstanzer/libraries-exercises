"""
Run python -m pip install mysqlclient pymysql from your terminal to install pymysql and the mysqlclient.
Create a notebook or python script named advanced_dataframes to do your work in for these exercises.
Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.
Use your function to obtain a connection to the employees database.
Once you have successfully run a query:
a. Intentionally make a typo in the database url. What kind of error message do you see?
b. Intentionally make an error in your SQL query. What does the error message look like?
Read the employees and titles tables into two separate DataFrames.
How many rows and columns do you have in each DataFrame? Is that what you expected?
Display the summary statistics for each DataFrame.
How many unique titles are in the titles DataFrame?
What is the oldest date in the to_date column?
What is the most recent date in the to_date column?
"""


# Create the users DataFrame.
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

# Create the roles DataFrame
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

"""
Copy the users and roles DataFrames from the examples above.
What is the result of using a right join on the DataFrames
What is the result of using an outer join on the DataFrames?
What happens if you drop the foreign keys from the DataFrames and try to merge them?
Load the mpg dataset from PyDataset.
Output and read the documentation for the mpg dataset.
How many rows and columns are in the dataset?
Check out your column names and perform any cleanup you may want on them.
Display the summary statistics for the dataset.
How many different manufacturers are there?
How many different models are there?
Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
Do automatic or manual cars have better miles per gallon?
"""

"""
Use your get_db_url function to help you explore the data from the chipotle database.
What is the total price for each order?
What are the most popular 3 items?
Which item has produced the most revenue?
Using the titles DataFrame, visualize the number of employees with each title.
Join the employees and titles DataFrames together.
Visualize how frequently employees change titles.
For each title, find the hire date of the employee that was hired most recently with that title.
Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform the manipulations.)

"""

