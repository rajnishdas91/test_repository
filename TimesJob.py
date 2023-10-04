from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml') #parse method.
# Data parsing is converting data from one format to another.
# Widely used for data structuring, it is generally done to make the
# existing, often unstructured, unreadable data more comprehensible.
jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    posted = job.find('span', class_='sim-posted').text
    if 'few' in posted:
        company_name = job.find('h3', class_='joblist-comp-name').text#.replace(' ','')

        skill = job.find('span', class_='srp-skills').text.replace(' ','')

        #job_info = job.header.h2.a['href']
        job_info = job.a['href']


        print(f'Company Name: {company_name.strip()}')
        print('Required Skill:', skill.strip())
        print(f'Published on: {posted.strip()}')
        print(f'Job Description: {job_info}')
        print(' ')

        #print(f'''
        #Company Name: {company_name}
        #Required Skill: {skill}
        #Published on: {posted}
        #''')
