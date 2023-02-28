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

### Plain text files :  Comma-separated values files with header. You can select the folder contains the source data in the tool

Please don’t change the 'LOCAL_TEXT_FILES': 'LOCAL_TEXT_FILES' session
 

## Running the tools

### Start up the tools






