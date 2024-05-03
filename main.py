import json
import os
from pathlib import Path
#from getpass import getpass


# sasctl - SAS Viya 
from sasctl import Session
from sasctl.services import files,folders

# internal classes
from classes.SASFlow import SASFlow
from classes.SASSwimLanePgm import SASSwimLanePgm
from classes.SASSwimLaneSubFlow import SASSwimLaneSubFlow
from classes.SASPgm import SASPgm

#
# GLOBAL VALUES - modify as needed
# g_flow_viya_path top-level folder needs to be created by a SAS admin
#
g_flow_disk_path = '/tmp/project/Flows/Converted'
g_flow_viya_path = '/project/Flows/Converted'
g_viya_server = 'server.demo.sas.com'
g_viya_user = 'sasdemo'
g_viya_password = 'Orion123'
#g_viya_password = getpass()


#
# Authenticate to the SAS Viya environment
#
Session(g_viya_server, g_viya_user, g_viya_password, verify_ssl=False)

#
# Create Viya folder tree
# assuming top level folder exists (i.e. /Public) so no need to create it
#
for idx, viya_folder in enumerate(g_flow_viya_path.split('/')[1:]):
    parent_viya_folder = folders.get_folder(viya_folder) if idx == 0 else folders.create_folder(viya_folder, parent=parent_viya_folder)

#
# Create disk folder tree
#
Path(g_flow_disk_path).mkdir(parents=True, exist_ok=True)

#
# READ INPUT JSON
#
with open('input.json', 'r') as f:
    input_json = json.load(f) 

#
# SETUP FLOW
#
for flow in input_json:

    current_master_flow_name = flow['flow_name']
    current_master_subflow_viya_path = g_flow_viya_path + '/' + current_master_flow_name + '/'
    current_master_subflow_disk_path = g_flow_disk_path + '/' + current_master_flow_name + '/'

    # create a folder in SAS Viya for each flows
    current_master_flow_viya_folder = folders.create_folder(current_master_flow_name, parent=parent_viya_folder)        

    #
    # SETUP SUBFLOWS with FLOW
    #
    for subflow in flow['subflows']:

        current_master_subflow_name = subflow['subflow_name']

        # create flow object
        flow_obj = SASFlow(current_master_flow_name)
        flow_obj.setFlowValues()

        # setup counters. priority seems to be zero-indexed so therefore initialized with -1
        priority_counter = -1
        swimlane_counter = 0
        
        #
        # SETUP SWIMLANES
        #
        swimlanes = subflow['swimlanes']
        for swimlane in swimlanes:

            current_swimlane_type = swimlane['swimlane_type']

            # swimlane counter (priority)
            swimlane_counter += 1

            # check swimlane type - in this case handle "pgm" type swimlanes
            # pgm type subflows can contain 1 or more code steps
            if current_swimlane_type == "pgms":

                # create swimlane object
                swimlane_obj = SASSwimLanePgm(swimlane_counter)
                swimlane_obj.setSwimLaneValues()
                swimlane_json = swimlane_obj.getSwimLane()
                swimlane_id = swimlane_obj.getSwimLaneID()

                # 
                # SETUP STEPS/PGMS
                #
                # swimlane_step_counter counts the number of steps/pgms within current swimlane
                #
                pgms = swimlane['swimlane_pgms']
                swimlane_pgm_counter = 0
                for current_pgm in pgms:

                    # advance counters
                    priority_counter += 1
                    swimlane_pgm_counter += 1

                    # set dynamic values
                    pgm_obj = SASPgm(priority_counter, swimlane_counter, swimlane_pgm_counter, current_pgm)
                    pgm_obj.setPgmValues()

                    # add pgm to swimlane
                    pgm_json = pgm_obj.getPgm()
                    swimlane_obj.addPgm(pgm_json)

                    # add connections if more than 1 pgm in the current swimlane
                    if swimlane_pgm_counter > 1:
                            swimlane_obj.addConnection(priority_counter)

            # check swimlane type - in this case handle "subflow" type swimlanes
            # "subflow" type subflows can contain just 1 subflow
            elif current_swimlane_type == "subflow":
                current_reference_subflow_name = swimlane['swimlane_subflow_name']

                # advance counters
                priority_counter += 1

                # SETUP SUFLOW REFERENCE
                swimlane_obj = SASSwimLaneSubFlow(swimlane_counter, priority_counter, current_master_subflow_viya_path, current_reference_subflow_name)
                swimlane_obj.setSwimLaneValues()
                swimlane_json = swimlane_obj.getSwimLane()
                
            else:
                raise Exception('ERROR: undefined subflow type!')
                    
            # add swimlane to flow
            flow_obj.addSwimLane(swimlane_json)
        
        # dump flow complete dictionary to JSON format
        flow_json = json.dumps(flow_obj.getFlow(), indent=4) 
        
        # create dictory and save .flw file to it
        filename = current_master_subflow_name + '.flw'
        filename_disk_path = current_master_subflow_disk_path + filename
        Path(current_master_subflow_disk_path).mkdir(parents=True, exist_ok=True)
        with open(filename_disk_path, 'w') as f:
            f.write(flow_json)
        
        # upload flow file (.flw file) to SAS Viya folder
        # TODO: when opening the "flw" file in SAS Studio I am prompted if to associate the flow to SAS Studio - how to avoid it?
        files.create_file(filename_disk_path, folder=current_master_flow_viya_folder, filename=filename)