# Write your in_range function here:
def in_range(num, lower, upper):
    return True if num >= lower and num <= upper else False


print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
