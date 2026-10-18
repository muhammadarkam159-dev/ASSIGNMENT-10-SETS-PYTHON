# UNIQUE VALUES
numbers = [10, 20, 10, 30, 40, 20, 50]

unique_numbers = set(numbers)
count = len(unique_numbers)

print("Unique Values:", unique_numbers)
print("Total Unique Values:", count)


# SET OPERATION

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# ADD AND REMOVE

skills = {"Python", "SQL", "AWS"}

skills.add("Snowflake")
skills.add("Databricks")
skills.discard("AWS")

print("Updated Skills:", skills)

# COMMON STUDENTS

python_students = {"Ali", "Sara", "Ahmed", "Zain"}
sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}
both = python_students & sql_students
one_course = python_students ^ sql_students
print("Both Courses:", both)
print("Exactly One Course:", one_course)


# SUBSET AND SUPERSET

required_skills = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}
subset = required_skills.issubset(candidate_skills)
superset = candidate_skills.issuperset(required_skills)
print("Is Subset:", subset)
print("Is Superset:", superset)

# MISSING NUMBERS

numbers = {1, 2, 4, 6, 8, 10}
all_numbers = set(range(1, 11))
missing = all_numbers - numbers
print("Missing Numbers:", missing)

# THREE SETS ANALYSIS

python = {"Ali", "Sara", "Ahmed", "Zain"}
sql = {"Sara", "Ahmed", "Hamza"}
aws = {"Ahmed", "Zain", "Hamza"}
all_three = python & sql & aws
only_python_sql = (python & sql) - aws
at_least_two = (python & sql) | (python & aws) | (sql & aws)
print("All Three:", all_three)
print("Only Python and SQL:", only_python_sql)
print("At Least Two:", at_least_two)

# TRANSACTION ANALYSIS


day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
day3 = {104, 106, 107, 108}

all_days = day1 & day2 & day3

exactly_one = ((day1 - day2 - day3) |
               (day2 - day1 - day3) |
               (day3 - day1 - day2))

at_least_two = ((day1 & day2) |
                (day1 & day3) |
                (day2 & day3))

print("All Days:", all_days)
print("Exactly One Day:", exactly_one)
print("At Least Two Days:", at_least_two)


# ACCESS CONTROL

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write", "delete"}
missing = required_permissions - user_permissions
extra = user_permissions - required_permissions
full_authorization = required_permissions.issubset(user_permissions)
print("Missing Permissions:", missing)
print("Extra Permissions:", extra)
print("Full Authorization:", full_authorization)

# CUSTOMERS SEGMENTATION

website = {"C1", "C2", "C3", "C4", "C5"}
mobile = {"C3", "C4", "C6", "C7"}
store = {"C2", "C4", "C7", "C8"}
all_three = website & mobile & store
exactly_one = ((website - mobile - store) |
               (mobile - website - store) |
               (store - website - mobile))

exactly_two = (((website & mobile) - store) |
               ((website & store) - mobile) |
               ((mobile & store) - website))

print("Exactly One Platform:", exactly_one)
print("Exactly Two Platforms:", exactly_two)
print("All Three Platforms:", all_three)


