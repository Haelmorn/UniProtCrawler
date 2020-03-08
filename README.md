# UniProtCrawler

A simple web scraper designed to gather information about proteins.

## Getting Started

To run this scraper, you will need a python3 environment on your machine.

### Prerequisites

The only library required for the scripts to work is scrapy. You can install it with:

```
$ pip install scrapy
```

## Running

### Picking sequences/proteins to scrape

In order to set a protein or nucleotide sequence you want to obtain, please edit either: 

`embl_list` variable found in `./spiders/EMBLspider.py`

or

`upfastalist` variable found in `./spiders/upfasta.py`

Scrapy operates as a CLI program. To run any of the crawlers, navigate to the project main directory and run:

```bash
scrapy crawl upspider
```

or

```bash
scrapy crawl emblspider
```

depending on which spider you want to run (Use upspider to get general data, use emblspider to get nucleotide sequences only). Note that you can store crawling results in a .json file using:

```bash
scrapy crawl <spider_name> -o <filename>.json
```

For any further information on how this project works, please refer to the official scrapy documentation (http://doc.scrapy.org/en/latest/index.html)

## TODO's

This project is a work-in-progress.

The next big thing on the list is turning the entire application into a pipeline, which would allow the user to obtain any desired information by entering gene name *only*.

## Authors

* **Karol Ciuchcinski** - *Initial work* - [Haelmorn](https://github.com/Haelmorn)
