empty_dict = {}
empty_dict2 = dict()

grades = {"Joel": 80, "Tim": 95}

joels_grade = grades['Joel']
print(joels_grade)

try :
    kates_grade = grades["Kate"]
except KeyError :
    print("없는 값이면 키 에러!")

joels_has_grade = "Joel" in grades
kates_has_grade = "Kate" in grades

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No one")
print(joels_grade, kates_grade, no_ones_grade)

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
print(num_students)

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

"user" in tweet_keys
"user" in tweet
"joelgrus" in tweet_values

