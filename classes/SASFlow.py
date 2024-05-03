import uuid
import datetime

class SASFlow:

    def __init__(self, flow_name):
        self._sasflow_name = flow_name + '.flw'
        self._sasflow_dt = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        self._sasflow_json = \
        {
            "creationTimeStamp": "",
            "modifiedTimeStamp": "",
            "createdBy": "sasdemo",
            "modifiedBy": "sasdemo",
            "version": 2,
            "name": "",
            "properties": {
                "UI_PROP_DF_OPTIMIZE": "false",
                "UI_PROP_DF_ID": "7ec643e8-4f23-48d6-8e37-04025b4906ed",
                "UI_PROP_DF_EXECUTION_ORDERED": "true"
            },
            # TODO: what to do with these links???? Seems like they are auto-corrected when I open the flow in SAS Studio 
            #       and I am prompted to associate the flow with SAS Studio
            "links": [
                {
                    "method": "GET",
                    "rel": "self",
                    "href": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "uri": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "type": "application/vnd.sas.data.flow"
                },
                {
                    "method": "GET",
                    "rel": "alternate",
                    "href": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "uri": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "type": "application/vnd.sas.data.flow.summary"
                },
                {
                    "method": "GET",
                    "rel": "up",
                    "href": "/dataFlows/dataFlows",
                    "uri": "/dataFlows/dataFlows",
                    "type": "application/vnd.sas.collection",
                    "itemType": "application/vnd.sas.data.flow.summary"
                },
                {
                    "method": "PUT",
                    "rel": "update",
                    "href": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "uri": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "type": "application/vnd.sas.data.flow",
                    "responseType": "application/vnd.sas.data.flow"
                },
                {
                    "method": "DELETE",
                    "rel": "delete",
                    "href": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "uri": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631"
                },
                {
                    "method": "GET",
                    "rel": "transferExport",
                    "href": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "uri": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "responseType": "application/vnd.sas.transfer.object"
                },
                {
                    "method": "PUT",
                    "rel": "transferImportUpdate",
                    "href": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "uri": "/dataFlows/dataFlows/cc326275-a9c4-41db-9c2c-5a4f0ee20631",
                    "type": "application/vnd.sas.transfer.object",
                    "responseType": "application/vnd.sas.summary"
                }
            ],
            # nodes will be populated in the code
            "nodes": dict(),
            "parameters": {},
            "connections": [],
            "extendedProperties": {},
            "stickyNotes": []
        }


    def setFlowValues(self):
        self._sasflow_json['name'] = self._sasflow_name
        self._sasflow_json['creationTimeStamp'] = self._sasflow_dt
        self._sasflow_json['modifiedTimeStamp'] = self._sasflow_dt

    def getFlow(self):
        return(self._sasflow_json)

    def addSwimLane(self, swimlane_json):
        self._sasflow_json['nodes'].update(swimlane_json)
