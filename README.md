Python Weekly Assignment – 20-Oct-24

1. Analyzing Student Performance
A school administrator wants to analyze students&#39; scores from a file that contains
records of students and their exam results in the format name,score. Unfortunately,
sometimes the file might be missing, corrupted, or contain invalid data. Write a
program that reads the file, calculates the average score, and lists students who scored
above average. Ensure proper handling of missing files and malformed data.

2. Product Availability in a Store
You work for an online store, and you need to help the operations team clean up their
product list. They have a list of product IDs that contains duplicates due to system
errors. Write a function that takes this list, removes duplicates, sorts the product IDs,
and returns the cleaned list. Make sure your function can handle an empty product list
input.

3. Organizing Sales Data
A small business owner has sales data in the form of tuples, each containing the
customer’s name and the amount they spent (e.g., (&#39;Alice&#39;, 200)). Write a program
that stores this data in a dictionary, where the customer’s name is the key and the
amount spent is the value. If a customer appears more than once, update their total
spending. Print the customer data sorted by their names.

4. Saving User Preferences
A mobile app allows users to customize settings like theme (dark/light mode),
language, and notification preferences. Write a program that saves a user&#39;s preferences
using the pickle module and retrieves them when needed. Handle cases where the
preferences file is missing or corrupted.

5. Analyzing Employee Salaries
A company’s HR department maintains employee records in a CSV file, which
includes details like employee name, department, and salary. You’ve been tasked with
analyzing this data to calculate the total and average salary per department. Write a
program that reads the CSV using pandas, computes the required data, and saves the
results to a new CSV. Handle situations where the file is missing or contains invalid
data.

6. Validating User Signups

Your company’s website allows users to sign up with their email addresses. Write a
Python program that checks if the provided email addresses are valid using regular
expressions. Make sure the emails follow the proper format (e.g.,
username@domain.com). Your program should filter out invalid emails from a given
list of signups.

7. Currency Conversion Calculator
You’re building a currency conversion tool for a travel website. The tool should take
two user inputs: the amount to convert and the conversion rate. Implement a program
that handles cases where the user enters invalid data, such as non-numeric input or a
conversion rate of zero, and provides appropriate error messages.

8. Movie Ratings Aggregation
A movie streaming service collects user ratings for movies. Each movie can be rated
on a scale of 1 to 10. Write a program that takes a list of movie ratings and uses list
comprehension to filter out ratings below 5 (bad ratings) and return a new list of good
ratings squared. Handle cases where no ratings are provided.

9. Extracting Contact Information
A company stores client data in text files, and some of the records contain phone
numbers in inconsistent formats, such as (123) 456-7890 or 123-456-7890. Write a
program that reads a text file, uses regular expressions to extract all phone numbers in
either format, and prints the list of valid phone numbers.

10. Removing Duplicate User Data
A loyalty program has a list of customer records, each stored as a tuple with the
customer’s name and email address (e.g., (&#39;John Doe&#39;, &#39;john@example.com&#39;)).
Due to an import error, some customers are listed multiple times. Write a Python
program that removes duplicate entries using a set and prints the unique list of
customers.

11. Product Inventory Analysis
Your company manages product inventory through a CSV file that contains product
ID, name, and quantity available. Write a program using pandas to filter products
with low stock (less than 10 units). Handle potential issues like a missing or
malformed CSV file, or missing columns in the data.

12. Statistical Analysis for a Sports Team

A sports analyst wants to analyze the performance statistics of players on a team.
Each player’s performance over the season is recorded as an array of scores. Write a
program that generates a large array of player scores using numpy, and calculates the
mean, median, variance, and standard deviation of the players’ performance.

13. Managing Task Lists
A task management system allows users to create and store to-do lists. Write a Python
program that stores a user&#39;s list of tasks using pickle, allowing them to save and
retrieve their tasks later. Ensure proper exception handling if the data file becomes
corrupted or is missing.

14. Social Media Post Analysis
A social media platform needs to analyze hashtags used in posts. Write a Python
program that extracts all unique hashtags from a given post using regular expressions.
Ensure that the hashtags only contain letters and numbers (e.g., #Python3) and print
them in a sorted list.
