from builtins import dict, len, print, range, str, zip
import random
from selenium import webdriver
import pandas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")
import faker
import numpy as np
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

f = faker.Faker()
first_names = ['Aarav', 'Aditya', 'Akshay', 'Aman', 'Amit', 'Anjali', 'Ankit', 'Anuja', 'Anupam', 'Arun','Aryan', 'Ayush', 'Bhavya', 'Chirag', 'Deepak', 'Devendra', 'Divya', 'Gaurav', 'Hari', 'Harsh','Isha', 'Jatin', 'Kajal', 'Kanika', 'Karthik', 'Kiran', 'Krishna', 'Kunal', 'Manisha', 'Manoj','Mayank', 'Meena', 'Mohit', 'Mukesh', 'Naveen', 'Neelam', 'Neha', 'Nikita', 'Nitin', 'Pooja','Pradeep', 'Prakash', 'Pranav', 'Prashant', 'Preeti', 'Raj', 'Rajat', 'Rajesh', 'Rakesh', 'Rashi','Ravi', 'Riya', 'Rohit', 'Sakshi', 'Sandeep', 'Sanjay', 'Sarika', 'Satish', 'Shikha', 'Shilpa','Shreya', 'Shubham', 'Siddharth', 'Simran', 'Sneha', 'Sonam', 'Sourabh', 'Subhash', 'Sudhir','Suman', 'Suresh', 'Sushma', 'Swati', 'Tanvi', 'Tanya', 'Tushar', 'Uday', 'Ujjwal', 'Vaishali','Varun', 'Vikas', 'Vikram', 'Vinay', 'Vineet', 'Vivek', 'Yogesh']
# colors = ["Blue","Pink","Black","White","Green"]
last_names = ['Ahuja', 'Bansal', 'Bhatia', 'Chauhan', 'Choudhary', 'Dutta', 'Garg', 'Ghosh', 'Goyal', 'Gupta','Jain', 'Jha', 'Joshi', 'Kumar', 'Mahajan', 'Mehra', 'Mishra', 'Mittal', 'Nair', 'Patel', 'Paul',               'Rajput', 'Rana', 'Rao', 'Reddy', 'Saha', 'Saxena', 'Sharma', 'Singh', 'Sinha', 'Soni', 'Srivastava','Thakur', 'Trivedi', 'Varma', 'Yadav']
Designations = ["Micro Enterprenuer"]
Email_addresses = [
    'freeuse14@gmail.com',
'freeforyou14@gmail.com',	
'takaagmail@gmail.com',
'gmailfor25@gmail.com',
'wantagmail12@gmail.com',
'gmailolla14@gmail.com',
'gmaill236@gmail.com',
'gmail985@gmail.com',
'gmailpopi36@gmail.com',
'gmailgenerator85@gmail.com'

] 
Mobile_numbers = []
for i in range(100):
    mobile_number = "9"
    for j in range(9):
        mobile_number += str(random.randint(0, 9))
    Mobile_numbers.append(mobile_number)
# print(len(Mobile_numbers))
# print(Mobile_numbers)

youtube_channels = []

for i in range(10):
    channel_id = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for j in range(24))
    youtube_channels.append(f'https://www.youtube.com/channel/{channel_id}')

# print(youtube_channels)

first_name = [random.choice(first_names) for n in range(10)]
last_name = [random.choice(last_names) for n in range(10)]
designation = [random.choice(Designations) for n in range(10)]
email = [Email_addresses[n] for n in range(10)]
Organisation_Name = ['self-employed' for i in range(10)]
Organisation_City=['VIZIANAGARAM' for i in range(10)]
Organisation_State = ['Andhra Pradesh' for i in range(10)]
mobile_number = [Mobile_numbers[n] for n in range(10)]
# Subscription = ['I have subscribed to SKOCH TV YouTube channel' for i in range(10)]
# confirmation = [('Please confirm that you have subscribed to the YouTube channel',"Please confirm that you have pressed the 'Bell Icon.'") for i in range(10)]
# next_step_youtube = [ youtube_channels[n] for n in range(10)]
# num_of_ads = ['1' for i in range(10)]
# i_confirm = ['I confirm' for i in range(10)]
List_of_Projects = ['Skill Development Training Program and Japan India Institute for Manufacturing program for ITI candidates of rural and interior villages of Telangana State - Andhra Pradesh Productivity Council' for i in range(10)]
terms_conditions = ['I accept the terms & conditions' for i in range(10)]


database = pd.DataFrame(dict(first_name=first_name,last_name=last_name,designation = designation,email = email,Organisation_Name =Organisation_Name, Organisation_City = Organisation_City,Organisation_State = Organisation_State,mobile_number = mobile_number,List_of_Projects = List_of_Projects,terms_conditions = terms_conditions))
database.to_csv("submission_form_database.csv", index=False)
database.head()

text_question_element_class = "zHQkBf"
# text_question_element_class2 = "zHQkBf"


# textarea_question_element_class = "KHxj8b tL9Q4c"
# # text_question_element_class2 = "whsOnd zHQkBf"
checkbox_question_element_class = "Id5V1"


submit_element_class = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div[1]/div[1]/div/span/span' 

url = "https://docs.google.com/forms/d/e/1FAIpQLSfpKuoweWNbeWBOFQGR9FhjWazx9FRDV2i4vBJS4119ViMi0w/formResponse?embedded=true"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

def answerNamefeedback(driver, df, element_class, user_id):
    first_name = df["first_name"][user_id]
    last_name = df["last_name"][user_id]
    designation = df["designation"][user_id]
    email = df["email"][user_id]
    Organisation_Name = df["Organisation_Name"][user_id]
    Organisation_City = df["Organisation_City"][user_id]
    # Organisation_State = df["Organisation_State"][user_id]
    mobile_number = df["mobile_number"][user_id]
    # Subscription = df["Subscription"][user_id]
    # confirmation = df["confirmation"][user_id]
    # next_step_youtube = df["next_step_youtube"][user_id]
    # num_of_ads = df["num_of_ads"][user_id]
    # i_confirm = df["i_confirm"][user_id]
    # List_of_Projects = df["List_of_Projects"][user_id]
    # terms_conditions = df["terms_conditions"][user_id]
    
    
    # feedback = df["feedback"][user_id]
    text_answers = [first_name, last_name,designation,email,Organisation_Name,Organisation_City,mobile_number] # following the ord
    text_questions = driver.find_elements(by=By.CLASS_NAME, value=element_class)
    # text_questions = driver.find_elements_by_class_name(element_class)
    for a,q in zip(text_answers,text_questions):
        q.send_keys(str(a))
    return driver

state_index_dict = {"Andhra Pradesh": 1}
# subs_index_dict = {"I have subscribed to SKOCH TV YouTube channel": 0}
# please_iconfirm_index_dict = {"Please confirm that you have subscribed to the YouTube channel" : 0 }
# please_iconfirm_index_dict2 = {"Please confirm that you have pressed the 'Bell Icon." : 1 }
# iconfirm_index_dict = {"I confirm",0}
List_of_Projects_index_dict = {"Skill Development Training Program and Japan India Institute for Manufacturing program for ITI candidates of rural and interior villages of Telangana State - Andhra Pradesh Productivity Council",6}
terms_conditions_index_dict = {"I accept the terms & conditions",0}

def Organisation(driver, df, element_class, user_id):
    # state_index=  2
    # driver.find_elements(by=By.CLASS_NAME ,value= element_class)[state_index].click()
    
    # driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span").click()
    
    # driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span").click()
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span").click()
    
    return driver

def subs(driver, df, element_class, user_id):
    
    # subs_index= 0 
    # driver.find_elements_by_class_name(element_class)[subs_index].click()
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div[2]/div[10]/div/div/div[2]/div/div/span/div/div/label/div/div[2]/div/span").click()
    
    return driver

def please_iconfirm(driver, df, element_class, user_id):
    # please_iconfirm_index= 0
    # please_iconfirm2_index= 1 
    # driver.find_elements_by_class_name(element_class)[please_iconfirm_index].click()
    # driver.find_elements_by_class_name(element_class)[please_iconfirm2_index].click()
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div[2]/div[11]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span").click()
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div[2]/div[11]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span").click()
    
    return driver

def i_confirm_(driver, df, element_class, user_id):
    # iconfirm_index= 0  
    # driver.find_elements_by_class_name(element_class)[iconfirm_index].click()
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div[2]/div[14]/div/div/div[2]/div/div/span/div/div/label/div/div[2]/div/span").click()
    
    return driver

def list_of(driver, df, element_class, user_id):
    # list_of_proj_index = 6 
    # driver.find_elements_by_class_name(element_class)[list_of_proj_index].click()
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span").click()
    
    return driver

def Terms(driver, df, element_class, user_id):
    terms_index= 0
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div[2]/div[12]/div/div/div[2]/div/div/span/div/div/label/div/div[2]/div/span").click()
    
    return driver

def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver


df = pd.read_csv("./submission_form_database.csv")
text_question_element_class = "zHQkBf"
# textarea_question_element_class = "KHxj8b tL9Q4c"

url = "https://docs.google.com/forms/d/e/1FAIpQLSfpKuoweWNbeWBOFQGR9FhjWazx9FRDV2i4vBJS4119ViMi0w/formResponse?embedded=true"

driver = webdriver.Chrome(ChromeDriverManager().install())
for user_id in range(len(df)):
    driver.get(url)
    driver.maximize_window()
    driver = answerNamefeedback(driver, df, text_question_element_class, user_id)
    driver = Organisation(driver, df, checkbox_question_element_class, user_id)
    # driver = subs(driver, df, checkbox_question_element_class, user_id)
    # driver = please_iconfirm(driver, df, checkbox_question_element_class, user_id)
    # driver = i_confirm_(driver, df, checkbox_question_element_class, user_id)
    driver = list_of(driver, df, checkbox_question_element_class, user_id)
    driver = Terms(driver, df, checkbox_question_element_class, user_id)
    # driver = answerCheckBox(driver, df, checkbox_question_element_class, user_id)
    driver = submit(driver, submit_element_class)
    
