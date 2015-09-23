"""Tests for the models of the forex app."""

# Import Django libraries
from django.test import TestCase
from django.core.validators import ValidationError

# Import Valuehorizon libraries
from ..models import Person

# Import other libraries
from datetime import date
from decimal import Decimal
import pandas as pd

class PersonModelTests(TestCase):
    def setUp(self):
        Person.objects.create(gender="M", 
        	title="MR",
        	first_name='Michael',
        	last_name="Key",
        	other_names="Patrick Alan",
        	profile="Michael Key is just a test model.")
        test_person1 = Person.objects.get(first_name="Michael")



    def field_tests(self):
    	"""
    	Ensure all fields in _meta.fields are included and correctly named
    	"""
        required_fields = [u'id', 'gender', 'title', 'first_name', 'last_name', 'other_names', 'date_of_birth', 'date_of_death', 'profile',
        'is_deceased', 'date_modified', 'date_created']
        actual_fields = [field.name for field in Person._meta.fields]
        self.assertEqual(set(required_fields), set(actual_fields))

    def m2m_field_tests(self):
	"""
    	Ensure all fields in _meta.many_to_many are included and correctly named
    	"""
    	required_fields = ['nationalities']
        actual_fields = [field.name for field in Person._meta.many_to_many]
        self.assertEqual(set(required_fields), set(actual_fields))



