# Web_Scraping_Example

## Install dependencies

- Install Python 3.10.11

- Install libraries by typing:
```
$ pip3 install -r requirements.txt
```

## Project Explanation

This is a practicing example of web scraping. In project the steps follows like:

1. With **download_links.py** code we get the new pages links from https://mfa.gov.lk/category/news/media-releases/ and save them into `\data\link_list.txt`. There are almost 2000 subpages and the code saves their links for next step.

2. **save_html_pages.py** code reads the links from txt and downloads the pages to `\data\raw_html` folder. The process was taking long and I write an alternative which uses threads for paralel downloading. **save_html_pages_paralel.py** code does the process in very shorter time.

3. **parse_html.py** extracts 'date', 'title' and 'content' data from everty page and saves it to `\data\parsed_data.jsons`

4. Finally **DataAnalysis.ipynb** makes analyzes data and visualize as graphics, then saves to `\figures` folder as `content_line_count.png`, `html_file_size.png`, `html_line_count.png`.