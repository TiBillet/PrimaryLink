from django.test import TestCase
from primary_server_core.models import PrimaryLink

'''
'''
# Creating the PrimaryLink test clasx
class PrimaryLinkCase(TestCase):
    # creating a primary_link object
    def setUp(self):
        PrimaryLink.objects.create(pin_code="789112", server_url="https://tibillet.org/")

    # Testing primarylink
    def test_primary_link(self):
        pin1 = PrimaryLink.objects.get(pin_code='789112')
        # Testing when the code and the server url is right
        self.assertEqual(pin1.pin_code, '789112')
        self.assertEqual(pin1.server_url, 'https://tibillet.org/')
        # testing when the pin code and the server_url is wrong
        self.assertNotEquals(pin1.pin_code, '123456')
        self.assertNotEquals(pin1.server_url, 'https://yahoo.com/')


    # Testing the return of status.HTTP_404 or 200
    def test_post_status(self):
        # Testing retour from POST
        response1 = self.client.post('http://127.0.0.1:8000/pin_code/',{"pinCode":'789112'})
        response2 = self.client.post('http://127.0.0.1:8000/pin_code/',{"pinCode":'111111'})

        # checking the return status with the right code posted
        self.assertEqual(response1.status_code, 200)
        self.assertNotEquals(response1.status_code, 404)

        # checking the return status with the right code posted
        self.assertEqual(response2.status_code, 404)
        self.assertNotEquals(response2.status_code, 200)


    # Testing the error message or the server_link
    def test_return_message_or_server_link(self):
        smallen_pin = self.client.post('http://127.0.0.1:8000/pin_code/',{"pinCode":'78911'})
        biger_pin = self.client.post('http://127.0.0.1:8000/pin_code/',{"pinCode":'123456789'})
        respons = self.client.post('http://127.0.0.1:8000/pin_code/',{"pinCode":'789112'})

        self.assertEqual(respons.status_code,200)
