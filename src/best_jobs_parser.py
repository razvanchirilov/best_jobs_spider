from parsel import Selector

CSS_SELECTORS = {
    "username": "input#login_form__username",  # input username selector from the page:
    "password": "input#login_form__password",  # input password selector from the page
    "submit": "button[type=submit]",
    "jobs_container": "#app-main-content",
    "job_employer": "::attr(data-employer-name)",
    "job_name": "::attr(data-title)"
}

XPATH_SELECTOR = {
    "job_cards": "//div[contains(@class,'job-card')]",
    "job_location": ".//span[@class='stretched-link-exception']//a/text()",
    "job_salary": "normalize-space(.//div[@class='text-right']//div[@class='text-nowrap']/text())"

}


class BestJobsParser:

    @staticmethod
    def get_selector_from_text(text: str) -> Selector:
        return Selector(text=text)

    @staticmethod
    def get_from_selector(selector: Selector, xpath_selector=XPATH_SELECTOR["job_cards"]) -> list:
        return selector.xpath(xpath_selector)

    @staticmethod
    def generate_job_dicts(job_cards: list):
        for job_card in job_cards:
            job_dict = dict(
                job_employer=job_card.css(CSS_SELECTORS["job_employer"]).get(),
                job_name=job_card.css(CSS_SELECTORS["job_name"]).get(),
                job_location=job_card.xpath(XPATH_SELECTOR["job_location"]).get(),
                job_salary=job_card.xpath(XPATH_SELECTOR["job_salary"]).get(),
            )
            yield job_dict


