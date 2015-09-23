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
        self.assertEqual(1, 1)



