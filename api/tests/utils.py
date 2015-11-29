from django.forms import model_to_dict
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase


class KrakSatAPITestCase(APITestCase):
    """
    APITestCase abstract subclass that provides a few utility functions to
    simplify testing API endpoints.
    """

    # Example fixed timestamp to be used in valid_data
    # Use timezone.now() to be settings.USE_TZ-independent
    TIMESTAMP = timezone.now().replace(year=2015, month=12, day=18,
                                       hour=12, minute=30, second=27,
                                       microsecond=0)

    # URL to 'list' API endpoint
    list_url = None
    # Model used by the endpoint
    model = None
    # Example valid data that can be sent to create new model instance
    valid_data = None

    def _test_create(self):
        """Ensure sending self.valid_data creates new record successfully.

        The function POSTs self.valid_data to self.list_url, expects
        201 CREATED HTTP response code, checks if new instance of self.model
        is created as well as compares data returned by the server to the data
        sent."""
        response = self.client.post(self.list_url, self.valid_data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.model.objects.count(), 1)
        result = model_to_dict(self.model.objects.get())
        for k in self.valid_data.keys():
            self.assertEqual(self.valid_data[k], result[k],
                             msg='\'{}\' values are not equal'.format(k))

    def _test_invalid_params(self, *l):
        """Ensure sending invalid parameters to self.list_url causes error 400.

        :param (str, dict) l: (message, param_to_replace) pairs to test.
            For instance, using ('Test', {'param': 'foo'}) will use message
            'Test' for a subtask that will send self.valid_data with 'param'
            replaced by 'foo'.
        """
        data_l = self.__generate_data_list(l)
        for msg, data in data_l:
            with self.subTest(msg=msg, data=data):
                # Ensure 0 model instances even after single sub-test failure
                self.model.objects.all().delete()
                response = self.client.post(self.list_url, data, format='json')
                self.assertEqual(response.status_code,
                                 status.HTTP_400_BAD_REQUEST)
                self.assertEqual(self.model.objects.count(), 0)

    def __generate_data_list(self, l):
        """Generate (message, data) tuples to be used by _test_invalid_params.

        :param l: list of (message, param_to_replace) pairs.
        """
        for msg, d in l:
            data_copy = self.valid_data.copy()
            data_copy.update(d)
            yield msg, data_copy
