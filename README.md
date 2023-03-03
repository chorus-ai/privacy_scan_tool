# ChoRUS Privacy Scan Tool

## Introduciton :

This is a tools to allow you to check the priovacy issue before share your data with others. 

It is the part of ChoRUS project for NIH

**Notes**:

The prediction of PHI data is based on statistics results. We recommend to have at least 1,000 records for each table to ensure accuracy. 


## Prerequisite:
Windows 10  or Mac with python3.8 or python3.9 ( with Git tools )

## Installation for Mac OS :

### 1. create or select a folder on your workstation 

### 2. Open a terminal window and go to the selected folder
~~~
cd ~/my_folder
$
~~~

### 3. create a python virtual environment
~~~
python3.8 -m venv ChoRUS_env
~~~
### 4. Active the virtual environment
~~~
source ChoRUS_env/bin/activate
(ChoRUS_env) $
~~~

### 5. Clone the package from Github.com 
~~~
git clone https://github.com/Luyaochen1/ChoRUS_Privacy_Scan.git
cd ChoRUS_Privacy_Scan
~~~

### 6. Install the required python package
~~~
python -m pip install -r requirement.txt
~~~

### 7. run the python Privacy Scan Tool
~~~
python main.py
~~~
 

## installation for Windows :

### 1. create or select a folder on your workstation 

### 2. Open a command prompt and go to the selected folder
~~~
cd c:\my_folder
c:\my_folder
~~~

### 3. create a python virtual environment
~~~
python3.8 -m venv ChoRUS_env
~~~
### 4. Active the virtual environment
~~~
ChoRUS_env\Scripts\activate.bat
(ChoRUS_env) c:\my_folder>
~~~

### 5. Clone the package from Github.com 
~~~
git clone https://github.com/Luyaochen1/ChoRUS_Privacy_Scan.git
cd ChoRUS_Privacy_Scan
~~~

### 6. Install the required python package
~~~
python -m pip install -r requirement.txt
~~~

### 7. run the python Privacy Scan Tool
~~~
python main.py
~~~
 
The user instruciton can be found at [Here ](https://github.com/Luyaochen1/ChoRUS_Privacy_Scan/blob/main/User_Instruction.md) 
 

## Version Log :

V_2.28.2023  Inital version for ChoRUS project

