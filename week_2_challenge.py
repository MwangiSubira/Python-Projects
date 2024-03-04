#List
# Initialize an empty list
numbers = []

# Get user input until they enter "q"
while True:
  user_input = input("Enter an integer (q to quit): ")
  if user_input.lower() == "q":
    break

  # Split the input string into individual values
  values = user_input.split(",")

  # Process each value
  for value in values:
    try:
      # Try converting to integer and append to list
      numbers.append(int(value.strip()))
    except ValueError:
      # Handle non-numeric values (e.g., print an error message)
      print(f"Invalid input: {value}")

# Calculate and print the sum
total_sum = sum(numbers)
print("The sum of the numbers is:", total_sum)


#Tuple
# Create a tuple of book names
favorite_books = ("The Hitchhiker's Guide to the Galaxy",
                  "The Lord of the Rings",
                  "Pride and Prejudice",
                  "To Kill a Mockingbird",
                  "The Martian")

# Print each book name on a new line
for book in favorite_books:
  print(book)


#Dictionary
# Define an empty dictionary for user information
person_info = {}

# Get user input for name, age, and favorite color
person_info["name"] = input("Enter your name: ")
person_info["age"] = int(input("Enter your age: "))
person_info["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary contents
print("Person information:", person_info)


#Sets
# Create empty sets for user input
set1 = set()
set2 = set()

# Get user input for elements in each set
while True:
  user_input = input("Enter an integer for set 1 (q to quit): ")
  if user_input.lower() == "q":
    break
  # Convert user input to integer and add to set
  try:
    set1.add(int(user_input))
  except ValueError:
        print("Invalid input: Please enter an integer or 'q' to quit.")

# Get user input for elements in set 2
while True:
  user_input = input("Enter an integer for set 2 (q to quit): ")
  if user_input.lower() == "q":
    break
  # Convert user input to integer and add to set
  try:
     set2.add(int(user_input))
  except ValueError:
        print("Invalid input: Please enter an integer or 'q' to quit.")


# Find the intersection of sets and print
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)


# Find the intersection of sets and print
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)


#Odd character count using list comprehension
# Create a list of words
words = ["apple", "banana", "orange", "grapefruit", "mango"]

# Use list comprehension to filter words with odd character count
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the list of words with odd character count
print("Words with odd character length:", odd_length_words)
