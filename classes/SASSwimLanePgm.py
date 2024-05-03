import uuid

class SASSwimLanePgm:

    def __init__(self, swimlane_counter):
        self._sasswimlane_counter = swimlane_counter
        self._sasswimlane_id = 'id-swimlane-' + str(self._sasswimlane_counter)
        self._sasswimlane_json = \
        {    
            "id": {
                "nodeType": "dataFlow",
                "version": 1,
                "id": "",
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
                        # nodes will be populated in the code
                        "nodes": dict(),
                        "parameters": {},
                        # connections will be populated in the code 
                        "connections": list(),
                        "extendedProperties": {},
                        "stickyNotes": []
                    },
                    "executionBindings": {
                        # do we need sessionid?
                        "sessionId": "a9b8c5e6-6187-4fb2-8c29-0f564a8f0f2c-ses0000",
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
        self._sasswimlane_json['id']['name'] = 'Swimlane ' + str(self._sasswimlane_counter)
        self._sasswimlane_json['id']['priority'] = self._sasswimlane_counter
        self._sasswimlane_json['id']['id'] = self._sasswimlane_id
        self._sasswimlane_json[self._sasswimlane_id] = self._sasswimlane_json.pop('id')

    def addPgm(self, pgm_json):
        self._sasswimlane_json[self._sasswimlane_id]['dataFlowAndBindings']['dataFlow']['nodes'].update(pgm_json)

    def addConnection(self, priority_counter):
        self._sasswimlane_connection = \
        {
            "sourcePort": {
                "node": "id-pgm-" + str(priority_counter-1),
                "portName": "outTables",
                "index": 0
            },
            "targetPort": {
                "node": "id-pgm-" + str(priority_counter),
                "portName": "inTables",
                "index": 0
            }
        }
        self._sasswimlane_json[self._sasswimlane_id]['dataFlowAndBindings']['dataFlow']['connections'].append(self._sasswimlane_connection)


    def getSwimLane(self):
        return(self._sasswimlane_json)

    def getSwimLaneID(self):
        return(self._sasswimlane_id )
