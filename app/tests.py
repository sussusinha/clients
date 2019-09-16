
import rest_framework.status
import rest_framework.test


class ClientTests(rest_framework.test.APITestCase):

    def test_create_client(self):
        payload = {
            'email': 'client@test.com',
            'name': 'Client Test'
        }
        response = self.client.post('/clients', payload, format='json')
        self.assertEqual(response.status_code, rest_framework.status.HTTP_201_CREATED)