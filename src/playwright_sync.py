from playwright.sync_api import sync_playwright
from credentials import USERNAME, PASSWORD

CSS_SELECTORS = {
    "username": "input#login_form__username",  # input username selector from the page:
    "password": "input#login_form__password",
    "submit": "button[type=submit]",
    "jobs_container": "#app-main-content",
    "job_card": ""
}


class PlaywrightSync:
    playwright = None
    browser = None
    headless: bool = True
    slow_mo: int = None

    def __init__(self, *args, **kwargs):
        self.playwright = sync_playwright().start()
        self.browser = self._get_browser()

    def _get_browser(self):
        return self.playwright.chromium.launch(
            headless=self.headless,
            slow_mo=self.slow_mo
        )

    def get_page(self):
        return self.browser.new_page()

    @staticmethod
    def get_by_selector(page, css_selector=CSS_SELECTORS["jobs_container"]):
        page.is_visible(css_selector)
        return page.inner_html(css_selector)

    @staticmethod
    def login(page, url, username=USERNAME, password=PASSWORD):
        page.goto(url)
        page.fill(CSS_SELECTORS["username"], username)
        page.fill(CSS_SELECTORS["password"], password)
        page.click(CSS_SELECTORS["submit"])



