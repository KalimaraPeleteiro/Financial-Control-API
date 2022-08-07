from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Receitas-list')
        self.user = User.objects.create_user(username = 'example', password = '123')

    def test_verifica_autenticacao_com_credenciais_corretas(self):
        """Teste que verifica se um usuário com as credenciais corretas é capaz de se autenticar"""
        user = authenticate(username = 'example', password = '123')
        self.assertTrue((user is not None) and user.is_authenticated)
    
    def test_bloqueia_requisicao_nao_autorizada(self):
        """Teste que verifica se requisições GET não autorizadas são bloqueadas"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permite_requisicao_autorizada(self):
        """Teste que verifica se requisições GET autorizadas são permitidas"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
