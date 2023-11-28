def make_car(car_manufacturer, car_model, **misc_info):
	"""Adding key value pairs to our misc_info dictionary"""
	misc_info['manufacturer'] = car_manufacturer
	misc_info['model'] = car_model
	return misc_info


car = make_car('subaru', 'outback', color='blue',
			   tow_package=True)
print(car)
