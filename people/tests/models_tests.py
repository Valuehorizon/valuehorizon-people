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

        Person.objects.create(gender="M", 
            title="LORD",
            first_name='Monty',
            last_name="Montagu",
            other_names="Nigel Leslie",
            profile="This model is used for testing names.")

        Person.objects.create(gender="M", 
            title="MR",
            first_name='Age',
            last_name="Tester",
            profile="This Model is used for testing age.")
        



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

    def age_tests(self):
        """
        Ensure that age is correctly computed
        """

        # Cannot calculate age with no date of birth
        test_person1 = Person.objects.get(first_name="Michael")
        test_person1.date_of_birth = None
        test_person1.date_of_death = None
        test_person1.save()
        self.assertEqual(test_person1.age(), None)

        # Cannot calculate age if deceased (is_deceased flag is True)
        test_person1.date_of_death = None
        test_person1.is_deceased = True
        test_person1.save()
        self.assertEqual(test_person1.age(), None)

        # Cannot calculate age if deceased (date_of_death is set)
        test_person1.date_of_death = date(2012,1,1)
        test_person1.is_deceased = False
        test_person1.save()
        self.assertEqual(test_person1.age(), None)

        # Compute date without as_at_date specification
        test_person1.date_of_death = None
        test_person1.is_deceased = False
        test_person1.date_of_birth = date(2000, 2, 15)
        test_person1.save()
        self.assertEqual(test_person1.age(as_at_date=date(2015,5,31)), 15)
        self.assertEqual(test_person1.age(as_at_date=date(2015,1,15)), 14)


    def short_name_tests(self):
        """
        Ensure that short_name is correctly computed
        """
        test_person1 = Person.objects.get(first_name="Monty")
        self.assertEqual(test_person1.short_name, "Lord Montagu")

    def name_tests(self):
        """
        Ensure that name is correctly computed
        """
        test_person1 = Person.objects.get(first_name="Michael")
        self.assertEqual(test_person1.name, "Michael Key")

        test_person2 = Person.objects.get(first_name="Monty")
        self.assertEqual(test_person2.name, "Lord Monty Montagu")

    def full_name_tests(self):
        """
        Ensure that name is correctly computed
        """
        test_person1 = Person.objects.get(first_name="Michael")
        self.assertEqual(test_person1.full_name, "Mr. Michael Patrick Alan Key")


