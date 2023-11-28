# **user_info passes in a keyword argument, it takes a key value pair as a
# parameter
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info


# When passing in a key value pair for a keyword argument, do not add quotes
# to the key
# user_profile = build_profile('albert', 'einstein', location='princeton',
# 							 field='physics')
# print(user_profile)

# Creating my own profile
user_profile = build_profile('rein', 'solis', location='dagupan city',
							 gender='male', course='information technology')
print(user_profile)
