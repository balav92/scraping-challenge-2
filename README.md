# scraping-challenge-2
**Overview:**

Referral Links: 
https://splash.readthedocs.io/en/stable/

https://www.zyte.com/blog/handling-javascript-in-scrapy-with-splash/

https://github.com/scrapy-plugins/scrapy-splash

https://docs.scrapy.org/en/latest/intro/tutorial.html


We are going to obtain the following data from the site http://quotes.toscrape.com/js/ using Splash and Scrapy:

Quote, Author Name and Tags.

**Step 1:** First, we should set up Splash by Docker using the following command. 

```
docker run –p 8050:8050 scrapinghub/splash
```

To test that if the docker has been successfully created, you can try accessing the URL http://localhost:8050.

**Step 2:** Navigate to the project folder and run the below commands to install the pre-requisites to run the spider.

```
pip install scrapy

pip install scrapy_splash
```

**Step3:** To test out the "scraping-challenge-2"  project, please execute the below commands. 

```
git clone https://github.com/balav92/scraping-challenge-2.git

cd scraping-challenge-2

scrapy crawl quotes
```

Note: To identify the name of the spider use the below command under the project folder

```
scrapy list
```

**Step 4:** In order to export the data into a CSV or JSON format, please execute the below command

```
scrapy crawl quotes -o output.csv 
or 
scrapy crawl quotes -o output.json
```

Note: You can specify your desired filename for the .csv or json file in the above command ( Ex: result.csv, Finaloutput.csv).
Now the following fields are displayed in the CSV output file :

```
Quote
Author
Tags
```

Thats all folks!
