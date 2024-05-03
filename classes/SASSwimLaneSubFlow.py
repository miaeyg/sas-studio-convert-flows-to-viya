import uuid

class SASSwimLaneSubFlow:

    def __init__(self, swimlane_counter, priority_counter, subflow_path, subflow_name):
        self._sasswimlane_counter = swimlane_counter
        self._priority_counter = priority_counter
        self._sassubflow_name = subflow_name
        self._sassubflow_path = subflow_path
        self._sasswimlane_id = 'id-swimlane-' + str(self._sasswimlane_counter)
        self._sassubflow_id = 'id-subflow-' + str(self._priority_counter)
        self._sasswimlane_json = \
        {
            "id": {
                "nodeType": "dataFlow",
                "version": 1,
                "id": "id",
                "name": "",
                "priority": 1,
                "properties": {
                    "UI_PROP_IS_EXPANDED": "true",
                    "UI_PROP_IS_SWIMLANE": "true"
                },
                "portMappings": [],
                "dataFlowAndBindings": {
                    "dataFlow": {
                        "creationTimeStamp": "0001-01-01T00:00:00.000Z",
                        "modifiedTimeStamp": "0001-01-01T00:00:00.000Z",
                        "version": 2,
                        "properties": {},
                        "links": [],
                        "nodes": {
                            "id-subflow-1": {
                                "nodeType": "dataFlow",
                                "version": 1,
                                "id": "id-subflow-1",
                                "name": "Subflow",
                                "note": {
                                    "version": 1,
                                    "id": "id-1672741649102-1555",
                                    "properties": {
                                        "UI_NOTE_PROP_HEIGHT": "0",
                                        "UI_NOTE_PROP_IS_EXPANDED": "false",
                                        "UI_NOTE_PROP_IS_STICKYNOTE": "false",
                                        "UI_NOTE_PROP_WIDTH": "0"
                                    }
                                },
                                "priority": 1,
                                "properties": {
                                    "UI_PROP_COLORGRP": "0",
                                    "UI_PROP_IS_INPUT_EXPANDED": "false",
                                    "UI_PROP_IS_OUTPUT_EXPANDED": "false",
                                    "UI_PROP_NODE_DATA_ID": "REFERENCED_FLOW_STEP",
                                    "UI_PROP_XPOS": "142",
                                    "UI_PROP_YPOS": "306"
                                },
                                "portMappings": [],
                                "dataFlowAndBindings": {
                                    "executionBindings": {
                                        "sessionId": "95eff37e-51e4-4d6b-8229-2e20b7820a79-ses0000",
                                        "contextId": "7fccb933-a87d-4322-90e6-93097092a0f3",
                                        "environmentId": "Compute",
                                        "arguments": {
                                            "__NO_OPTIMIZE": {
                                                "argumentType": "string",
                                                "version": 1,
                                                "value": "true"
                                            }
                                        }
                                    },
                                    "dataFlowReference": {
                                        "type": "content",
                                        "path": ""
                                    }
                                }
                            }
                        },
                        "parameters": {},
                        "connections": [],
                        "extendedProperties": {},
                        "stickyNotes": []
                    },
                    "executionBindings": {
                        # do we need sessionid?
                        "sessionId": "95eff37e-51e4-4d6b-8229-2e20b7820a79-ses0000",
                        # do we need contextid?
                        "contextId": "7fccb933-a87d-4322-90e6-93097092a0f3",
                        "environmentId": "Compute",
                        "arguments": {
                            "__NO_OPTIMIZE": {
                                "argumentType": "string",
                                "version": 1,
                                "value": "true"
                            }
                        }
                    }
                }
            }
        }

    def setSwimLaneValues(self):
        self._sasswimlane_json['id']['dataFlowAndBindings']['dataFlow']['nodes']['id-subflow-1']['dataFlowAndBindings']['dataFlowReference']['path'] = self._sassubflow_path + self._sassubflow_name + '.flw'
        self._sasswimlane_json['id']['name'] = 'Swimlane ' + str(self._sasswimlane_counter)
        self._sasswimlane_json['id']['priority'] = self._sasswimlane_counter
        self._sasswimlane_json['id']['dataFlowAndBindings']['dataFlow']['nodes']['id-subflow-1']['priority'] = self._priority_counter 
        self._sasswimlane_json['id']['id'] = self._sasswimlane_id
        self._sasswimlane_json['id']['dataFlowAndBindings']['dataFlow']['nodes']['id-subflow-1']['id'] =self._sassubflow_id
        self._sasswimlane_json['id']['dataFlowAndBindings']['dataFlow']['nodes'][self._sassubflow_id] = self._sasswimlane_json['id']['dataFlowAndBindings']['dataFlow']['nodes'].pop('id-subflow-1')
        self._sasswimlane_json[self._sasswimlane_id] = self._sasswimlane_json.pop('id')

    def getSwimLane(self):
        return(self._sasswimlane_json)

    def getSwimLaneID(self):
        return(self._sasswimlane_id )
