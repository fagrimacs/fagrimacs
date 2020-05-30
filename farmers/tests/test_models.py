from django.test import TestCase

from accounts.models import CustomUser
from farmers.models import FarmerProfile


class TestFarmersModels(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(name='Innocent', email='farmer@fagrimacs.com', password='idfsoiudiudf')


    def test_string_representation(self):
        # farmer_profile = FarmerProfile.objects.create(user=self.user)

        # self.assertEqual(str(farmer_profile), 'Innocent Profile')
        pass