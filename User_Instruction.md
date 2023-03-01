# ChoRUS Privacy Scan Tool User Guide V0.1
 
## Source data and configuration

The configuration is done via the config.py. We can modify the source data by changing configuration file.

The tool currently supports access two types of source data:

### Postgresql database:  

~~~
available_dbs = {'PSQL_MIMIC': ["postgresql://userid:password@192.168.0.199:5432/mimic","mimiciii"],
                'LOCAL_TEXT_FILES': 'LOCAL_TEXT_FILES'
        }
~~~        

Where mimic is the database name and mimiciii is the data schema name

### Plain text files :  

Comma-separated values files with header. You can select the folder contains the source data in the tool.

Please don’t change the 'LOCAL_TEXT_FILES': 'LOCAL_TEXT_FILES' session
 

## Running the tool from Mac OS :

### 1. go to the selected folder
~~~
cd ~/my_folder
$
~~~

### 2. Active the virtual environment
~~~
source ChoRUS_env/bin/activate
(ChoRUS_env) $
 
~~~

### 3. enter folder of the package cloned from Github.com 
~~~
cd ChoRUS_Privacy_Scan
~~~

### 4. run the python privacy Scan Tool
~~~
python main.py
~~~
 

## Running the tool from Windows :

### 1. go to the selected folder
~~~
cd c:\my_folder
c:\my_folder>
$
~~~

### 2. Active the virtual environment
~~~
ChoRUS_env\Scripts\activate.bat
(ChoRUS_env) c:\my_folder>
~~~

### 3. enter folder of the package cloned from Github.com 
~~~
cd ChoRUS_Privacy_Scan
~~~

### 4. run the python privacy Scan Tool
~~~
python main.py
~~~
 
## Step 1 decide the source data type 
User can select the source data type from the dropdown list. To add a new data source, please refer to the "Source data and configuration" session of this document.

![select_source_db](screen_capture/select_source_db.JPG?raw=true)

For local csv files, please select the "LOCAL_TEXT_FILE" option . If it is selected, user can  choose the folder where the csv files located.

![Model](screen_capture/csv_files.JPG?raw=true)

## Step 2 select the source tables to scan 

The next step is to select the tables(csv files) from the soruce data base to scan.

![select_table](screen_capture/select_table.JPG?raw=true")

The selected tables will be displayed in the "Selected Source Tables" form.

![selected_tables](screen_capture/selected_tables.JPG?raw=true)

## Step 3 run data profiling 
By clicking the "Genereate DB profile", the data profiling tool will run at the backend to genereate the statistics of the tables.

![Profiling](screen_capture/Profiling.JPG?raw=true)

The user can view the the profiling result as the below screen.

![Profiling_result](screen_capture/Profiling_result.JPG?raw=true)

## Step 4 run PHI data scan

PHI scanning must be done after the profiling. It is runnning at the backend and the message window will show the status.

![Scanning](screen_capture/Scanning.JPG?raw=true)

## Step 5 view the PHI data scan

The scan result can be viewed by clicking "View Result".  The columns with the high chance conain PHI data will be hightlighed. 

![Scan_result](screen_capture/Scan_result.JPG?raw=true)

It also can be exported to an Excel file.  

![Scan_result_export](screen_capture/Scan_result_export.JPG?raw=true)

## Step 6 save/load the project

The progress of the data profoiling and PHI scanning can be saved and loaded via the menu. The progress is saved in a json file  can be loaded back to continue the work or review the reuslts. 





 
 
 





