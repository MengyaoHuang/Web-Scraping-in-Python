# Web-Scraping-in-Python
## Introduction
This project is designed for film directors' works analysis. What we want to explore is the relationship between films' performance and film directors' background.

## Steps to follow
- Directors dataset: [Extract directors' birthplace/birthday/bio/trivia/race/gender information](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/web%20scrapping.ipynb)
  - A short VBA code to automatically download images from url address and insert in Excel:
  - [Fill in Excel cells by automatically downloading images from url address](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/VB%20fill%20in%20images%20through%20downloads.txt)

- Scores dataset: [Extract Users' ratings and Critic scores/comments for Top films](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/score_scraping.ipynb)
  - Users ratings distribution for TOP200 films each year starting from 2004:
  ![](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/Users.PNG)
  
  - Critic/Metascore ratings distribution for TOP200 films each year starting from 2004:
  ![](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/Critics.PNG)
  
 - Nature Language Processing Analysis - Topic modeling and text analysis for comments
    - LIWC: [LIWC transparent text analysis](https://www.cs.cmu.edu/~ylataus/files/TausczikPennebaker2010.pdf)
      - By using LIWC Topic model analysis, we calculate the word frequency of critic rating comments related to specific ten topics. The LIWC Extractor code in notebook can be found [here](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/LIWC%20implementation.ipynb)
    - LSA/LDA decomposition: [A simplified notebook to implement basic LDA/LSA analysis for sample text](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/Topic%20model%20analysis.ipynb)
- Word Topic frequency statistical analysis given race and gender info
  - We have fixed around 10 topics that we may interest from LIWC. What we did here was to extract word-text related to these topics, gave statistical info and compared how their frequencies may vary among people with different race and gender. [Notebook details can be found here](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/Word%20Topic%20frequency%20analysis.ipynb)

- Login Web scraping
  - [Task1](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/Log%20in%20Task/Data_scraping_log_in_related_task_Section1_.ipynb): (Login not needed) Use "bomlink" and "imdblink" of each film to scrape information including 'releasedate' and 'closedate' and 'number of critics'. 
  - [Task2](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/Log%20in%20Task/star_power_actor.ipynb): Here we want to scrap StarPower values for the Top5 casts for each film measured 10 weeks prior to the release date (scraped from Task1). To be more specific, we would use [Selenium](https://www.seleniumhq.org/) to set up a driver and log in our account first. And by visiting Pro-IMDb profile of casts, we would tell certain period rankings through graph Data automatically.
  - [Task3](https://github.com/MengyaoHuang/Web-Scraping-in-Python/blob/master/Log%20in%20Task/seasonality_score_scraping_boxOffice.ipynb): Find out each film's release date and match the date to week's gross and total number of movies info identified by boxofficemojo.com
    - " Season captures whether a distributor released a film during a high-demand period. Though most peak seasons revolve around holidays, we developed a continuous measure of seasonality by creating a moving average of total box office receipts across all films for a three-week window centered around the film’s release date during the previous three years" (Sorenson and Waguespack, 2006: p. 572)
