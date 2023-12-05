# ChoRUS Privacy Scan Tool

## Introduction

This tool helps you identify privacy concerns before sharing your data with others. It is a part of the RASx-rad and ChoRUS project for NIH.

The project introduction presentation can be found [here](https://github.com/chorus-ai/ChoRUS_Privacy_Scan/blob/main/De%E2%80%91identifcation%20of%20Structured%20EHR%20Using%20Machine%20Learning.pptx).

**Notes**:

PHI data predictions are based on statistical results. We recommend having a minimum of 1,000 records for each table to ensure accuracy.

## Prerequisites:
Windows 10 or Mac with Python 3.8 or 3.9 (with Git tools)

## Mac OS Installation:

### 1. Create or choose a folder on your workstation

### 2. Open a terminal window and navigate to the selected folder
~~~
cd ~/my_folder
$
~~~

### 3. Create a Python virtual environment
~~~
python3.8 -m venv ChoRUS_env
~~~

### 4. Activate the virtual environment
~~~
source ChoRUS_env/bin/activate
(ChoRUS_env) $
~~~

### 5. Clone the package from Github
~~~
git clone https://github.com/chorus-ai/ChoRUS_Privacy_Scan.git
cd ChoRUS_Privacy_Scan
~~~

### 6. Install the required Python packages
~~~
python -m pip install -r requirements.txt
~~~

### 7. Run the Privacy Scan Tool
~~~
python main.py
~~~

## Windows Installation:

### 1. Create or choose a folder on your workstation

### 2. Open a command prompt and navigate to the selected folder
~~~
cd c:\my_folder
c:\my_folder
~~~

### 3. Create a Python virtual environment
~~~
python3.8 -m venv ChoRUS_env
~~~

### 4. Activate the virtual environment
~~~
ChoRUS_env\Scripts\activate.bat
(ChoRUS_env) c:\my_folder>
~~~

### 5. Clone the package from Github
~~~
git clone https://github.com/chorus-ai/ChoRUS_Privacy_Scan.git
cd ChoRUS_Privacy_Scan
~~~

### 6. Install the required Python packages
~~~
python -m pip install -r requirements.txt
~~~

### 7. Run the Privacy Scan Tool
~~~
python main.py
~~~

## The user instructions can be found [here](https://github.com/chorus-ai/ChoRUS_Privacy_Scan/blob/main/User_Instruction.md).


## Version Log:

V_2.28.2023  Initial version for RADx-rad and ChoRUS project

V_3.6.2023  Updated models

## Acknowledgemant

This project is supported by RADx-rad DCC (1U24LM013755) and ChoRUS (OT2OD032701)
