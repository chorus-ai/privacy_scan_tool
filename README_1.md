# ChoRUS Privacy Scan Tool

## Introduction

This is a tool that allows you to check for privacy issues before sharing your data with others. It is part of the ChoRUS project for NIH. The presentation for the project introduction can be found [here](https://github.com/chorus-project/intro-presentation). The prediction of PHI data is based on statistics results. We need to check the distribution of data and make sure that the data is not biased. 1. Recommend having at least 1,000 records for each table to ensure accuracy.

## Prerequisite: Windows 10 or Mac with python3.8 or python3.9 (with Git tools)

## Installation for Mac OS:

### 1. 1. Create or select a folder on your workstation.
2. Open a terminal window and go to the selected folder:

~~~

cd ~/my_folder

$ ~~~

3. Create a Python virtual environment:

~~~

python3.8 -m venv ChoRUS_env 

### 4. Active the virtual environment 

source ChoRUS_env/bin/activate 

(ChoRUS_env) $ 

### 5. Clone the package from Github.com 

git clone https://github.com/chorus- # Clone the ChoRUS_Privacy_Scan repository
git clone https://github.com/ai/ChoRUS_Privacy_Scan.git

# Change directory into the ChoRUS_Privacy_Scan folder
cd ChoRUS_Privacy_Scan

# Install the required python package
python -m pip install -r requirement.txt

# Run the python Privacy Scan Tool
python main.py

## installation for Windows:

### 1. create or select a folder on your workstation

### 2. Open a command prompt and go to the selected folder

cd c:\my_folder

c:\my_folder ### 3. Create a Python Virtual Environment

~~~

python3.8 -m venv ChoRUS_env

~~~

### 4. Activate the Virtual Environment

~~~

ChoRUS_env\Scripts\activate.bat

(ChoRUS_env) c:\my_folder>

~~~

### 5. Clone ##### the package from Github.com
```
git clone https://github.com/chorus-ai/ChoRUS_Privacy_Scan.git
cd ChoRUS_Privacy_Scan
```

##### 6. Install the required python package
```
python -m pip install -r
``` requirement.txt 

### 7. run the python Privacy Scan Tool 

~~~ python main.py ~~~  

The user instruciton can be found at [Here ](https://github.com/chorus- ## Version Log

- V_2.28.2023: Inital version for ChoRUS project
- V_3.6.2023: update models
