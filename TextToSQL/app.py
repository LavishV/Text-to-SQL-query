# create a streamlit app and entire LLM aplication willl be created in this file


from dotenv import load_dotenv
load_dotenv() ##load all the environment variables from .env file

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Function to load Google gemini model and provide query and response

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-3.6-flash")
    response = model.generate_content([prompt, question])
    return response.text

#Function to retrieve query from the sql database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows    

### Define your Prompt:

prompt = """
    You are an exper in converting English questions to SQL query
    The SQL database has the name STUDENT and has the following columns: NAME, CLASS, SECTION, MARKS
    \n\n For example, \n example 1 - how many entries of records are present ?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT; \n example 2 - what is the average marks of students in class 10th ?, the SQL command will be something like this SELECT AVG(MARKS) FROM STUDENT WHERE CLASS='10th'; \n example 3 - what is the name of student who has scored highest marks ?, the SQL command will be something like this SELECT NAME FROM STUDENT ORDER BY MARKS DESC LIMIT 1; \n\n Now, based on the above examples, please convert the following question into SQL query: 
    also the sql code should not have ''' in beginning and end of the code, it should be a single line code without any new line characters.
"""

st.set_page_config(page_title="I can retrieve any SQL Query")
st.header("Gemini App to retreive SQL data")

question=st.text_input("Input: ", key= "input")

submit=st.button("Ask the question")

#if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data=read_sql_query(response, "student.db")
    st.subheader("The response is : " )

    for row in data:
        print(row)
        st.header(row)
