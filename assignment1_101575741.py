"""
Author: Harpreet Singh
Assignment: #1
"""

# Step b: Create 4 variables

gym_member = "Alex Alliton"   # str
preferred_weight_kg = 20.5    # float
highest_reps = 25             # int
membership_active = True      # bool


# Step c: Create a dictionary named workout_stats

# Dictionary (dict)
# Keys: friend names (str)
# Values: tuple of 3 integers (yoga, running, weightlifting)

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (50, 40, 40),   # total = 130 (>=120 to trigger condition)
    "Taylor": (25, 30, 45)
}


# Step d: Calculate total workout minutes using a loop and add to dictionary

for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes


# Step e: Create a 2D nested list called workout_list

# 2D list (list of lists)
workout_list = []

for friend in workout_stats:
    if "_Total" not in friend:
        workout_list.append(list(workout_stats[friend]))


# Step f: Slice the workout_list

print("Yoga and Running for all friends:")
for row in workout_list:
    print(row[0:2])

print("\nWeightlifting for last two friends:")
for row in workout_list[-2:]:
    print(row[2])


# Step g: Check if any friend's total >= 120

for friend in workout_stats:
    if "_Total" in friend:
        if workout_stats[friend] >= 120:
            name = friend.replace("_Total", "")
            print(f"Great job staying active, {name}!")


# Step h: User input to look up a friend

user_name = input("\nEnter a friend's name: ")

if user_name in workout_stats:
    print(f"\n{user_name}'s Workout Details:")
    print("Yoga:", workout_stats[user_name][0])
    print("Running:", workout_stats[user_name][1])
    print("Weightlifting:", workout_stats[user_name][2])
    print("Total Minutes:", workout_stats[user_name + "_Total"])
else:
    print(f"Friend {user_name} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes

totals = {}

for friend in workout_stats:
    if "_Total" in friend:
        name = friend.replace("_Total", "")
        totals[name] = workout_stats[friend]

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("\nFriend with Highest Total Workout Minutes:", highest_friend)
print("Friend with Lowest Total Workout Minutes:", lowest_friend)
