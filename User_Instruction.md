# ChoRUS Privacy Scan Tool User Guide V0.1

## Configuring Source Data

Modify the source data by editing the config.py file.

The tool supports two types of source data:

### Postgresql Database:
~~~
available_dbs = {'PSQL_MIMIC': ["postgresql://userid:password@192.168.0.199:5432/mimic","mimiciii"],
                'LOCAL_TEXT_FILES': 'LOCAL_TEXT_FILES'
        }
~~~

Here, "mimic" is the database name and "mimiciii" is the data schema name.

### Plain Text Files:

Comma-separated values (CSV) files with a header. Select the folder containing the source data in the tool.

Do not change the 'LOCAL_TEXT_FILES': 'LOCAL_TEXT_FILES' line.
 

## Step 1. Running the Tool on Mac OS:

### 1. Open a terminal and navigate to the selected folder
~~~
cd ~/my_folder
$
~~~

### 2. Activate the virtual environment
~~~
source ChoRUS_env/bin/activate
(ChoRUS_env) $
~~~
 
### 3. Enter the folder containing the source code
~~~
cd ChoRUS_Privacy_Scan
~~~

### 4. Run the Python Privacy Scan Tool
~~~
python main.py
~~~
 

## Running the Tool on Windows:

### 1. Open a command prompt and navigate to the selected folder
~~~
cd c:\my_folder
c:\my_folder>
$
~~~

### 2. Activate the virtual environment
~~~
ChoRUS_env\Scripts\activate.bat
(ChoRUS_env) c:\my_folder>
~~~

### 3. Enter the folder containing the source code
~~~
cd ChoRUS_Privacy_Scan
~~~

### 4. Run the Python Privacy Scan Tool
~~~
python main.py
~~~

The main screen will appear as shown below.

![main](screen_capture/main.JPG?raw=true)
 
## Step 2: Choose the Source Data Type
Select the source data type from the dropdown list. To add a new data source, refer to the "Configuring Source Data" section of this document.

![select_source_db](screen_capture/select_source_db.JPG?raw=true)

For local CSV files, choose the "LOCAL_TEXT_FILE" option. When selected, users can pick the folder containing the CSV files.

![Model](screen_capture/csv_files.JPG?raw=true)

## Step 3: Select the Source Tables to Scan
Select the tables (CSV files) from the source database.

![select_table](screen_capture/select_table.JPG?raw=true")

The chosen tables will appear in the "Selected Source Tables" form.

![selected_tables](screen_capture/selected_tables.JPG?raw=true)

## Step 4: Perform Data Profiling
Click "Generate DB profile" to run the data profiling tool in the background and generate table statistics.

![Profiling](screen_capture/Profiling.JPG?raw=true)

Users can view the profiling results in the following screen.

![Profiling_result](screen_capture/Profiling_result.JPG?raw=true)

## Step 5: Execute PHI Data Scan
Perform PHI scanning after data profiling. The scan runs in the background, and the status is displayed in the message window.

![Scanning](screen_capture/Scanning.JPG?raw=true)

## Step 6: View the PHI Data Scan Results
Click "View Result" to display the scan results. Columns with a high likelihood of containing PHI data will be highlighted.

![Scan_result](screen_capture/Scan_result.JPG?raw=true)

The results can also be exported to an Excel file.

![Scan_result_export](screen_capture/Scan_result_export.JPG?raw=true)

## Step 7: Save and Load the Project

You can save and load the progress of data profiling and PHI scanning using the menu. The progress is stored in a JSON file, enabling you to resume your work or review the results at a later time.

![save_project](screen_capture/save_project.JPG?raw=true)


