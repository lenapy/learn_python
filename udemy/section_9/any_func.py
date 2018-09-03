lines  = ["trees are good", "pool is fresh", "face is round"]
website_list = ["face", "clock", "trend"]

for line in lines:
	any(website in line for website in  website_list)

# Result will be:
# False
# False
# True

"""So, we start iterating over the items of website_list using a for loop. In the first iteration we would have:
any(website in "trees are good" for website in website_list)

Inside the parenthesis of any() there's another loop that iterates over website_list:

("face" in "trees are good")
("clock" in "trees are good")
("trend" in "trees are good")
If any of these is True you get the expression evalueated to True. In this case none of them is True, so you get False.
 If you want to return True if all of them are True, you need to use all() instead of any().

So, the part any(website in line for website in website_list)will either be equal to True or False."""