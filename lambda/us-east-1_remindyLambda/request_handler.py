import json
import dynamoDB_handler
import response_handler
import logging
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)

    
    
def request_handler(event, context):
    table_name = 'remindy'
    thing ='';preposition='';location=''
    logger.info("Request is "+str(event))
    print(str(event['request']['type']))
    if event['request']['type'] == 'LaunchRequest':
        return response_handler.createWelcomeResponse()
    if event['request']['type'] == 'SessionEndedRequest':
        return None
    if event['request']['intent']['name'] == 'SaveIntent':
        slots = event['request']['intent']['slots']
        # if 'value' in slots['item']:
        #     logger.info("Got the thing value")
        #     thing = slots['item']['value']
        # if 'value' in slots['preposition']:
        #     logger.info("Got the preposition slot")
        #     preposition = slots['preposition']['value']
        # if 'value' in slots['location']:
        #     logger.info("Got the location slot")
        #     location = slots['location']['value']
        if 'value' in slots['itemPhrase']:
            logger.info("Got the itemPhrase slot")
            itemPhrase = slots['itemPhrase']['value']
            thing, preposition, location = extractSlots(itemPhrase)
            print("thing"+str(thing))
        if " is" in thing:
            thing = thing.rstrip(" is")
            print("Removed is new thing is "+thing)
        if " " in thing:
            thing = thing.rstrip()
            print("Removed a black space - new thing is "+thing)
        user_id = event['session']['user']['userId']
        details = {
            'what': thing,
            'prep': preposition,
            'loc': location
        }
        dialogState = event['request']['dialogState']
        if dialogState == 'STARTED' or dialogState == 'IN_PROGRESS':
            logger.info("Dialog State is In Progress")
            return response_handler.createInProgressResponse()
        elif event['request']['dialogState'] == 'COMPLETED':
            logger.info("In the complete stage")
            if event['request']['intent']['confirmationStatus'] == 'DENIED':
                logger.error("The status is denied")
                return response_handler.createWelcomeResponse()
            logger.info("Dialog State is Completed")
            dynamoDB_handler.update_item2_new(table_name, user_id, details)
            return response_handler.createSaveResponse()
        #return response_handler.createInProgressResponse
    elif event['request']['intent']['name'] == 'QueryIntent':
        user_id = event['session']['user']['userId']
        thing = event['request']['intent']['slots']['itemPhrase']['value']
        search_resp = dynamoDB_handler.search_item(table_name, user_id, thing)
        if search_resp[0] == False:
            return response_handler.createItemNotFoundResponse()
        else:
            location = search_resp[1][0]
            # if "my " in location:
            #     location.replace(" my "," your ")
            #     print("new ",location)
            preposition = search_resp[1][1]
            json_body = search_resp[1][2]
            return response_handler.createQueryResponse(thing, preposition, location)
    elif event['request']['intent']['name'] == 'ThankYouIntent':
        return response_handler.createThankyouResponse()
    elif event['request']['intent']['name'] == "AMAZON.HelpIntent":
        return response_handler.createHelpResponse()
        
def extractSlots(item):
    return tuple(re.split('\\s(at|in|on|at|under|over|after|before|beside)\\s', item))
    
def removeIs(item):
    return item.replace(" is ", " ")