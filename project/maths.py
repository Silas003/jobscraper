from .Internship import jobs
from celery import shared_task
import requests
import csv
import os

@shared_task
def add():
    for i in range(10):
        print(i)
    return 'Done'

@shared_task()
def search_job(query='backend'):

    url = "https://jsearch.p.rapidapi.com/search"


    #query=['backend developer,mobile developer']

    querystring = {"query":query,"page":"1","num_pages":"5"}

    headers = {
        "X-RapidAPI-Key": "73bdff1dbcmsh0f0a1522e024a65p11bfd9jsnd5e2cacd763d",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)

    except  ConnectionAbortedError as E:
        print(E)

    i = 0
    while os.path.exists(f'internship{i}.csv'):
        i += 1

    file=f"internship{i}.csv"
    csv_file=open(file,'w',encoding='utf-8')

    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['employer name',
                        'job title',
                        'job link',
                        'job_description',
                        'employment type',
                        'job_location',
                        'is_job_remote',
                        'required skills',
                        'experience'
                        'education',
                        'min_salary',
                        'max_salary',
                        'responsiblities'])

    data1=response.json()
    data2=data1['data']
    for info in data2:
        employername=info['employer_name'] 
        jobtitle=info['job_title']
        joblink=info['job_apply_link']
        jobdesc=info['job_description']
        jobtype=info['job_employment_type']
        jobcountry=info['job_country']
        jobloc=info['job_is_remote']
        jobskills=info['job_required_skills']
        experience=info['job_required_experience']['experience_preferred']
        jobeducation=info['job_required_education']['degree_mentioned']
        min_salary=f"{info['job_salary_currency']}  {info['job_min_salary']} "
        max_salary=f"{info['job_salary_currency']} {info['job_max_salary']}"
        responsibilties=info['job_highlights']
        csv_writer.writerow([employername,
                            jobtitle,
                            joblink,
                            jobdesc,
                            jobtype,
                            jobcountry,
                            jobloc,
                            jobskills,
                            experience,
                            jobeducation,
                            min_salary,
                            max_salary,
                            responsibilties])

    csv_file.close()

    return 'Done'