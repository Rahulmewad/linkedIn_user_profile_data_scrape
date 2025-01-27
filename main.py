"""
Linkedin User profile Data fetch APPs
Author : Rahul Mewada
Developer : Rahul Mewada
Create Date : 24-01-2025

Dependency library installation :- 
    pip install fastapi uvicorn

Run terminal command :- 
    python -m uvicorn main:app --reload

Uvicorn running on browser :- 
     http://128.0.0.2:8000/docs

Quit terminal :
    (Press CTRL+C to quit)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import requests
from lxml import html
import sys
import linkedin_constants as constants
import json

def get_title_path(tree):
    title = "-"
    try:
        title = tree.xpath(constants.TITEL_XPATH)[0].strip()
    except Exception as e:
        line_no = sys.exc_info()[-1].tb_lineno
        error_desc = f"Exception occured in get_title_path : {line_no} -- {e}"
        print(error_desc)
    return title

def get_heading_path(tree):
    heading = ''
    try:
        heading = tree.xpath(constants.HEADING_XPATH)[0].strip().replace('\n',' ')
    except Exception as e:
        line_no = sys.exc_info()[-1].tb_lineno
        error_desc = f"Exception occured in get_heading_path : {line_no} -- {e}"
        print(error_desc)
    return heading

def get_address_path(tree):
    address = ''
    try:
        address = tree.xpath(constants.ADDRESS_XPATH)[0]
    except Exception as e:
        line_no = sys.exc_info()[-1].tb_lineno
        error_desc = f"Exception occured in get_address_path : {line_no} -- {e}"
        print(error_desc)
    return address

def get_about_path(tree):
    about = ''
    try:
        about = ', '.join([abu.replace('\n','').replace('\t','').replace('\uf076','').strip() for abu in tree.xpath(constants.ABOUT_XPATH) if abu.strip().replace("\n",'') !='']).replace('About, ','About: ')
    except Exception as e:
        line_no = sys.exc_info()[-1].tb_lineno
        error_desc = f"Exception occured in get_about_path : {line_no} -- {e}"
        print(error_desc)
    return about

def get_company_name_path(tree):
    company_name = ''
    try:
        company_name = tree.xpath(constants.COMPANY_NAME_XPATH)[0].strip()
    except Exception as e:
        line_no = sys.exc_info()[-1].tb_lineno
        error_desc = f"Exception occured in get_company_name_path : {line_no} -- {e}"
        print(error_desc)
    return company_name


def get_education_path(tree):
    education = ''
    try:
        education = tree.xpath(constants.EDUCATION_XPATH)[0].strip()
    except Exception as e:
        line_no = sys.exc_info()[-1].tb_lineno
        error_desc = f"Exception occured in get_education_path : {line_no} -- {e}"
        print(error_desc)
    return education

def get_experience_path(tree):
    experience = '-'
    try:
        experience_xpath = tree.xpath(constants.EXPERIENCE_XPATH)
        experience_data = {}
        count = 0
        for exp in experience_xpath:
            count +=1
            expr = exp.xpath(".//text()")
            expr2 = [expr_cln.replace('\n','').replace('\t','').replace('\uf0fc','').strip()for expr_cln in expr if expr_cln.strip().replace("\n",'') !='']
            expr3 = ', '.join(expr2)  
            experience_data[f"experience_{count}"] = expr3
        experience = json.dumps(experience_data)   
    except Exception as e:
        line_no = sys.exc_info()[-1].tb_lineno
        error_desc = f"Exception occured in get_experience_path : {line_no} -- {e}"
        print(error_desc)
    return experience


app = FastAPI()

# Define the input and output models
class LinkedInRequest(BaseModel):
    linkedin_url: HttpUrl

class PersonDetails(BaseModel):
    title: str
    heading: str
    address: str
    about: str
    company_name: str
    education: str
    experience: str


# Function to scrape LinkedIn details
def scrape_linkedin_details(linkedin_url: str):
    try:
        response = requests.get(linkedin_url, headers=constants.HEADERS, cookies=constants.COOKIES)
        if response.status_code != 200:
            raise ValueError(f"Failed to fetch the LinkedIn page: {response.status_code}")

        tree = html.fromstring(response.content)  
        dict_data = {}    

        dict_data["title"] = get_title_path(tree)
        dict_data["heading"] = get_heading_path(tree)
        dict_data["address"] = get_address_path(tree)
        dict_data["about"] = get_about_path(tree)
        dict_data["company_name"] = get_company_name_path(tree)
        dict_data["education"] = get_education_path(tree)
        dict_data["experience"] = get_experience_path(tree)
    
        return dict_data

    except Exception as e:
        raise ValueError(f"Error occurred while scraping LinkedIn: {e}")

# Endpoint to fetch LinkedIn details
@app.post("/fetch_linkedin_details", response_model=PersonDetails)
async def fetch_linkedin_details(request: LinkedInRequest):
    try:
        # Fetch details using the scrape function
        dict_data = scrape_linkedin_details(request.linkedin_url)
        return dict_data
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching details")
