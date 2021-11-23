from parsel import Selector


class BestJobsParser:

    @staticmethod
    def get_selector_from_text(text: str) -> Selector:
        return Selector(text=text)

    @staticmethod
    def get_from_selector(selector: Selector, xpath_selector="//div[contains(@class, 'job-card')]") -> list:
        return selector.xpath(xpath_selector)

    @staticmethod
    def generate_job_dicts(job_cards: list):
        for job_card in job_cards:
            job_dict = dict(
                job_employer=job_card.css("::attr(data-employer-name)").get(),
                # TODO
                job_name="",
                job_location="",
                job_salary=""
            )
            yield job_dict


