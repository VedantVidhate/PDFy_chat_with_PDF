# <div align="center">PDFy: chat with your PDF</div>


## Table of content
--------------

1. [Introduction](#introduction)
2. [Steps](#steps)
3. [Use_the_project](use-the-project)


## Introduction
--------------
Information is more available and abundant than ever in this digital age, and it has an important effect on how economies, civilizations, and individual lives are shaped. The ability of knowledge to connect, educate, and empower people globally is what makes it so important. **PDF (Portable Document Format)** is essential for the dissemination of knowledge due to it’s accessibility and versatility. PDFs maintain a document's formatting and layout, guaranteeing that the content will appear the same on various platforms and device. Numerous activities, such as **text production**, **language translation**, and **natural language understanding**, can be accomplished by large language models such as **ChatGPT**, **Google LaMDA**, **PaLM2**, **Meta’s Llama2** and others. They can help with writing, providing answers to queries, summarizing literature, and even coming up with original works of art like poetry or stories. We can utilize these language models for extracting information from documents on any topic and present it in a form that is both appealing as well as useful thereby saving a lot of time and effort in going through the whole corpus of text. ChatPDF is a tool which helps users interact with their  answers to users questions. **Retrieval Augmented Generation** is a technique by which appropriate information is gathered from various knowledge bases thereby keeping the language model up to date. The main purpose of this project is to present an alternative solution to this problem using LangChain and a large language model to provide an interactive environment to users where they can ask questions and get accurate answers based on the document corpus as well as recent information and developments.


## Steps
--------------
1. Created, virtual environment using conda with **python version 3.11**.
2. Created, **README.md** file to maintain all the recrds and steps used in project.
3. created, **requirements.txt** file so that all the requirements can be noted with specific version.
4. Created, **.gitignore** so that the files that we don't want to share on github can be avoided.
5. Created, **.env** where all credentials and configurations will be stored and this file will be ignored by git through **.gitignore**.
6. Created, **.python-version** where i have stored my python version.
7. Created, **setup.py** file. 
   - this script is a standard way to define metadata and dependencies for a Python package.
   - The script is designed to be executed to create a distributable package for this project.
   - To run this file >> **python setup.py install**.
8. Installed some importan libraries.
   - streamlit: To create GUI
   - pypdf2: To read the pdf using python
   - langchain: An open-source framework that helps developers to work with LLM's 
   - python-dotenv: To work with .env file.
   - faiss-cpu: Facebook AI similarity Search, FAISS CPU is a library for efficient similarity search and clustering of dense vectors. It is written in C++ and provides a       Python interface.
   - openai
   - huggingface-hub
9. Created a basic GUI using streamlit
10. Obtain API keys from **OPENAI** and **HUGGINGFACEHUB** and save them in .env .
11. Proceeded according to **PDFy_Architecture**.
   - At **embedding** stage we had two ways to convert the text_chunks to vector:
        -- Using OPENAI which is paid
        -- Using Instructor platform which is free but uses lot of hardware resources so very large file will take time.
              --- To use ***Instructor** we need no isntall some other libraries:
                  - InstructorEmbedding
                  - sentence-transformers
12. We have used **FAISS** for storing vectors of our text_chunks which uses our local system to store its like a local database.


## Use_the_project
--------------

1. Git clone this repository
2. pip isntall requirements.txt
3. create .env file and enter your "OpenAI" and "HuggingFaceHub" API keys there
   - OPENAI_API_KEY = 
   - HUGGINGFACEHUB_API_TOKEN =
4. streamlit run application.py
5. Upload your pdfs and ask questions