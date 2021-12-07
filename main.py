from src.best_jobs_spider import BestJobsSpider

if __name__ == '__main__':
    login_url = "https://www.bestjobs.eu/en/login"

    spider = BestJobsSpider()
    page = spider.get_page()
    spider.login(page, login_url)
    first_page_text = spider.get_by_selector(page)
    first_page_selector = spider.get_selector_from_text(first_page_text)
    job_cards = spider.get_from_selector(first_page_selector)

    job_items = []
    for job_dict in spider.generate_job_dicts(job_cards):
        job_items.append(job_dict)

    # pw = PlaywrightSync()
    # page = pw.get_page()
    # pw.login(page, login_url)

    print(1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
