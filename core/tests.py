from django.test import TestCase
from django.contrib.auth.models import User

class PrivilegeEscalationTest(TestCase):

    def setUp(self):
        # Crear usuari normal
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def test_sql_injection_privilege_escalation(self):
        # Login amb l'usuari normal
        self.client.login(username="testuser", password="testpass123")

        # Payload maliciós
        malicious_payload = {
            "email": "test@test.com', is_superuser = true --"
        }

        # Simular POST vulnerable
        self.client.post("/update-email/", malicious_payload)

        # Refrescar usuari des de BD
        self.user.refresh_from_db()

        # Assert que NO hauria de ser superusuari
        self.assertFalse(self.user.is_superuser)
