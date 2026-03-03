from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecurityRegressionTests(StaticLiveServerTestCase):
    fixtures = ['testdb.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")

        cls.selenium = webdriver.Remote(
            command_executor="http://selenium-firefox:4444/wd/hub",
            options=opts
        )
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_role_restriction(self):
        """AUDITORIA: L'analista no ha d'entrar a /admin/"""
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.presence_of_element_located((By.ID, "id_username")))
        self.selenium.find_element(By.ID, "id_username").send_keys("analista1")
        self.selenium.find_element(By.ID, "id_password").send_keys("altoke21")
        self.selenium.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        wait.until(EC.url_changes('%s%s' % (self.live_server_url, '/accounts/login/')))
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.assertNotEqual(
            self.selenium.title,
            "Site administration | Django site admin"
        )
