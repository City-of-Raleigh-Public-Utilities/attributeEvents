#Author: Corey White
#Date: 5/13/15
#Company: City of Raleighs
#Description:

import arcpy

#set workspace
arcpy.env.workspace = "Database Connections\\RPUD.sde" # Need to change this to work where it runs

records = [
    {
        feature: 'RPUD.wHydrants',
        table: 'RPUD.hydrantEvents'
    }
]

def findNewEvents(inFeature, eventTables):
    #Get event table fields
    #For each record does
    #find last event if event exisits
    #If event
    #Check if record matches event
    #Add new event if record does not match event
