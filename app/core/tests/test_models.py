from django.test import TestCase
from core.models import Writer,Book
from core.serilazers import WriterSerializer,BookSerializer

Writer_URL=reverse('recipe:recipe-list')

def create_autor(self):
    name='test'
    last_name="last_test"
    return Writer.objects.create(name=name,last_name=last_name)

class ModelTest(TestCase):
    def test_create_writer(self):
        create_autor()
        create_autor()
        res = self.client.get(Writer_URL)
        data=Writer.objects.all()
        serializer=WriterSerializer(data=data,many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)