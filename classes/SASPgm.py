import uuid

class SASPgm:

    def __init__(self, priority_counter, swimlane_counter, swimlane_pgm_counter, code):
        self._priority_counter = priority_counter
        self._sasswimlane_counter = swimlane_counter
        self._sasswimlane_pgm_counter = swimlane_pgm_counter
        self._saspgm_id = 'id-pgm-' + str(self._priority_counter)
        self._saspgm_code = code
        self._saspgm_json = \
        {
            "id": {
                "nodeType": "step",
                "version": 1,
                "id": "", 
                "name": "", 
                "note": { 
                    "version": 1, 
                    "id": "",  
                    "properties": { 
                        "UI_NOTE_PROP_HEIGHT": "0", 
                        "UI_NOTE_PROP_IS_EXPANDED": "false", 
                        "UI_NOTE_PROP_IS_STICKYNOTE": "false", 
                        "UI_NOTE_PROP_WIDTH": "0" 
                    } 
                }, 
                "priority": 1, 
                "properties": { 
                    "UI_PROP_COLORGRP": "1", 
                    "UI_PROP_INPUT_PORT|inTables|0": "", 
                    "UI_PROP_IS_INPUT_EXPANDED": "false", 
                    "UI_PROP_IS_OUTPUT_EXPANDED": "false", 
                    "UI_PROP_NODE_DATA_ID": "a7190700-f59c-4a94-afe2-214ce639fcde", 
                    "UI_PROP_NODE_DATA_MODIFIED_DATE": "1664303562062", 
                    "UI_PROP_PORT_DESCRIPTION|outTables|0": "Output tables", 
                    "UI_PROP_PORT_ID|outTables|0": "", 
                    "UI_PROP_PORT_LABEL|outTables|0": "Output tables 1", 
                    "UI_PROP_XPOS": "30", 
                    "UI_PROP_YPOS": "10" 
                }, 
                "portMappings": [ 
                    { 
                        "mappingType": "tableStructure", 
                        "portName": "outTables", 
                        "portIndex": 0, 
                        "tableStructure": { 
                        } 
                    } 
                ], 
                "stepUri": "/dataFlows/steps/a7190700-f59c-4a94-afe2-214ce639fcde", 
                "arguments": { 
                    "codeOptions": { 
                        "code": "", 
                        "contentType": "embedded", 
                        "logHTML": "", 
                        "resultsHTML": "", 
                        "variables": [ 
                            { 
                                "name": "_input1", 
                                "value": { 
                                    "portIndex": 0, 
                                    "portName": "inTables", 
                                    "referenceType": "inputPort" 
                                } 
                            }, 
                            { 
                                "name": "_output1", 
                                "value": { 
                                    "portIndex": 0, 
                                    "portName": "outTables", 
                                    "referenceType": "outputPort" 
                                } 
                            } 
                        ] 
                    } 
                } 
            }
        }

    def setPgmValues(self):
        self._saspgm_json['id']['properties']['UI_PROP_INPUT_PORT|inTables|0'] = str(uuid.uuid4()) + '|Input tables 1|Input tables'
        self._saspgm_json['id']['properties']['UI_PROP_PORT_ID|outTables|0'] = str(uuid.uuid4())
        self._saspgm_json['id']['properties']['UI_PROP_XPOS'] = str(self._sasswimlane_pgm_counter * 120 + 10)
        self._saspgm_json['id']['properties']['UI_PROP_YPOS'] = str(self._sasswimlane_counter * 50 + 10)
        self._saspgm_json['id']['arguments']['codeOptions']['code'] = self._saspgm_code
        self._saspgm_json['id']['priority'] = self._priority_counter
        self._saspgm_json['id']['note']['id'] = self._saspgm_id + '-note'
        self._saspgm_json['id']['name'] = "SAS Program " + str(self._priority_counter)
        self._saspgm_json['id']['id'] = self._saspgm_id
        self._saspgm_json[self._saspgm_id] = self._saspgm_json.pop('id')

    def getPgm(self):
        return(self._saspgm_json)

    def getPgmID(self):
        return(self._saspgm_id)