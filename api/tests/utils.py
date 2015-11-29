from django.forms import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase


class KrakSatAPITestCase(APITestCase):
    """
    APITestCase abstract subclass that provides a few utility functions to
    simplify testing API endpoints.
    """

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
        self.assertTrue(all(self.valid_data[k] == result[k]
                            for k in self.valid_data.keys()))

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
