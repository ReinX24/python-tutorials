import pytest

from employee import Employee


@pytest.fixture
def make_employee():
	"""To create an employee instance to be used by our tests."""
	employee = Employee('Rein', 'Solis', 0)
	return employee


def test_give_default(make_employee):
	"""Check if the default parameter in give_raise function works."""
	make_employee.give_raise()
	make_employee.annual_salary == 5000


def test_give_custom_raise(make_employee):
	"""Check if passing in a parameter value works properly."""
	make_employee.give_raise(1000)
	make_employee.annual_salary == 1000
