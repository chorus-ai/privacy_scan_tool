# setup coonfiguration data here
import os

available_dbs = {'PSQL_MIMIC': ["postgresql://gpadmin:dataroad@129.106.31.45:15432/mimic","mimiciii"],
                'IQVIA_ONGOLOGY': ["postgresql://gpadmin:dataroad@129.106.31.45:15432/iqvia","oncology"],
                'LOCAL_TEXT_FILES': 'LOCAL_TEXT_FILES'
        }


target_models = {'CDMV5.4': './dataModel/CDMV5.4.json',
                'FHIR': './dataModel/FHIR.json'
        }


dest_db =  "postgresql://gpadmin:dataroad@129.106.31.45:15432/omop_5_4"
 
target_dbs = {'OMOP_5.4_staging': ["postgresql://gpadmin:dataroad@129.106.31.45:15432/omop_5_4","staging"],
              'OMOP_5.4_final': ["postgresql://gpadmin:dataroad@129.106.31.45:15432/omop_5_4","final"]
        }

data_profile_sample_size = 500  

PHI_SCAN_MODEL = './phi_scan/XGBClassifier(V220230227).json'