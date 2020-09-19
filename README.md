# Web Scraping
Web scraping refers to the extraction of data from a website. This information is collected and then exported into a format that is more useful for the user. Although web scraping can be done manually, in most cases, automated tools are preferred when scraping web data as they can be less costly and work at a faster rate.

But in most cases, web scraping is not a simple task. Websites come in many shapes and forms, as a result, web scrapers vary in functionality and features.

In this repo, I scraped a Wikipedia page and recorded which passages need citations. Also, generated a report that contains all the paragraphs which needs citation.

## Implementation Notes
For implementation, I used two functions:
- Count function, get_citations_needed_count, takes in a url and returns an integer represinting how many citations are needed.

- Report function, get_citations_needed_report, takes in a url and returns a string, the string is formatted with each citation needed on own line, in order found. The report will be stored in a txt file.
