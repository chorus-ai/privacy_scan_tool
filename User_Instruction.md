# ChoRUS Privacy Scan Tool User Guide V0.1
 
## Source data and configuration

The configuration is done via the config.py. We can modify the source data by changing the configuration file.

The tool currently supports the access to two types of source data:

### Postgresql database:  

~~~
available_dbs = {'PSQL_MIMIC': ["postgresql://userid:password@192.168.0.199:5432/mimic","mimiciii"],
                'LOCAL_TEXT_FILES': 'LOCAL_TEXT_FILES'
        }
~~~        

Where mimic is the database name and mimiciii is the data schema name

### Plain text files :  

Comma-separated values files with a header. You can select the folder that contains the source data in the tool.

Please don’t change the 'LOCAL_TEXT_FILES': 'LOCAL_TEXT_FILES' session
 

## Running the tool from Mac OS :

### 1. Open a terminal and go to the selected folder
~~~
cd ~/my_folder
$
~~~

### 2. Active the virtual environment
~~~
source ChoRUS_env/bin/activate
(ChoRUS_env) $
 
~~~

### 3. enter the folder where the source code located 
~~~
cd ChoRUS_Privacy_Scan
~~~

### 4. run the python privacy Scan Tool
~~~
python main.py
~~~
 

## Running the tool from Windows :

### 1. Open a command prompt and go to the selected folder
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

### 3. enter the folder where the source code located 
~~~
cd ChoRUS_Privacy_Scan
~~~

### 4. run the python privacy Scan Tool
~~~
python main.py
~~~
The main screen is like this.

![main](screen_capture/main.JPG?raw=true)
 
## Step 1. Decide the source data type 
Users can select the source data type from the dropdown list. To add a new data source, please refer to the "Source data and configuration" session of this document.

![select_source_db](screen_capture/select_source_db.JPG?raw=true)

For local CSV files, please select the "LOCAL_TEXT_FILE" option. If it is selected, the user can choose the folder where the CSV files are located.

![Model](screen_capture/csv_files.JPG?raw=true)

## Step 2. Select the source tables to scan 

The next step is to select the tables(CSV files) from the source database.

![select_table](screen_capture/select_table.JPG?raw=true")

The selected tables will be displayed in the "Selected Source Tables" form.

![selected_tables](screen_capture/selected_tables.JPG?raw=true)

## Step 3. Run data profiling 
By clicking the "Generate DB profile", the data profiling tool will run at the backend to generate the statistics of the tables.

![Profiling](screen_capture/Profiling.JPG?raw=true)

The user can view the profiling result in the below screen.

![Profiling_result](screen_capture/Profiling_result.JPG?raw=true)

## Step 4. Run PHI data scan

PHI scanning must be done after the profiling. It is running at the backend and the message window will show the status.

![Scanning](screen_capture/Scanning.JPG?raw=true)

## Step 5. View the PHI data scan

The scan result can be viewed by clicking "View Result".  The columns with a high chance to contain PHI data will be highlighted. 

![Scan_result](screen_capture/Scan_result.JPG?raw=true)

It also can be exported to an Excel file.  

![Scan_result_export](screen_capture/Scan_result_export.JPG?raw=true)

## Step 6. Save/load the project

The progress of the data profiling and PHI scanning can be saved and loaded via the menu. The progress is saved in a JSON file and can be loaded back to continue the work or review the results. 


![save_project](screen_capture/save_project.JPG?raw=true)



 
 
 





