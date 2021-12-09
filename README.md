# best_jobs_crawler

|This Spider crawl the www.bestjobs.ro website do the following:
    - Start a new chromium browser and a new page;
    - Login into Bestjobs website with credentials.py from credentials.py file (secured with keyring library -> api token);
    - Scrape jobs information from the first jobs page after the following criterias:
      1. job_employer
      2. job_name
      3. job_location
      4. job_salary
    - Arrange and write the information in a .json jobs dictionary.
