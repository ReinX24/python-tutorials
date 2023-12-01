# from users import Admin

# Importing the Admin class from the admin module
from admin import Admin

my_admin = Admin('rein', 'solis', 20,
				 'information technology')
my_admin.describe_user()
my_admin.privileges.show_privileges()

# my_admin = Admin('rein', 'solis', 20,
# 				 'information technology')
# my_admin.privileges.show_privileges()
