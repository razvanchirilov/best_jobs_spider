from src.best_jobs_parser import BestJobsParser
from src.playwright_sync import PlaywrightSync
from src.best_jobs_parser import BestJobsParser


class BestJobsSpider(PlaywrightSync, BestJobsParser):

    def __init__(self, *args, **kwargs):
        super().__init__(PlaywrightSync, *args, **kwargs)

    """
    Spider will do the following:
    - Start a new chromium browser and a new page;
    - Login into Bestjobs website with credentials.py from credentials.py.py file;
    - Scrape jobs information from the jobs page in a Jobs dict.
    """