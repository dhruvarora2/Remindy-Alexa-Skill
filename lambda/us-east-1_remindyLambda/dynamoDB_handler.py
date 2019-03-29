import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def insert_into_table(table_name, user_id , details):
    table = dynamodb.Table(table_name)
    thing_var = details['thing']
    where_loc = details['location']
    preposition = details['preposition']


    response = table.put_item(
        Item={
            'uid': user_id,
            'thing': [
                {
                    'what': thing_var,
                    'loc': where_loc,
                    'prep': preposition
                }

            ]
        }
    )

    logger.info("Response from save DB: "+str(response))
    return True
    
def insert_into_table2(table_name, user_id , details):
    table = dynamodb.Table(table_name)
    # thing_var = details['thing']
    # where_loc = details['location']
    # preposition = details['preposition']


    response = table.put_item(
        Item={
            'uid': user_id,
            'thing': details
        }
    )

    logger.info("Response from save DB: "+str(response))
    return True

def update_item2(table_name, user_id, details):
    table = dynamodb.Table(table_name)
    # thing_var = details['thing']
    # where_loc = details['location']
    # preposition = details['preposition']
    response = table.update_item(
        Key={
            'uid': user_id
            },
        UpdateExpression= 'SET thing = list_append(if_not_exists(#thing, :empty_list), :details)',
        ExpressionAttributeNames= {
          '#thing': 'thing'
        },
        ExpressionAttributeValues= {
          ':details': [details],
          ':empty_list': []
        }
    )

    logger.info("Response from save DB: "+str(response))
    return True
    

def search_item(table_name, user_id, thing):
    table = dynamodb.Table(table_name)

    response = table.get_item(
        Key={
            'uid': user_id
        }
    )

    print("The resp json "+str(response))
    if 'Item' not in response:
        logger.info("There is no item")
        return [False, "Can't Find, Are you sure you asked me to save it?"]
    thing_json = response['Item']['thing']
    for ele in thing_json:
        print("ele "+str(ele))
        if ele['what'] == thing:
            logger.info("Found the thing ")
            resp = [ele['loc'], ele['prep'], thing_json]
            return [True, resp]

    return [False, "Can't Find, Are you sure you asked me to save it?"]
    
    
def update_item2_new(table_name, user_id, details):
    table = dynamodb.Table(table_name)
    thing = details['what']

    search_resp = search_item(table_name, user_id, thing)
    print("Search resp "+str(search_resp))
    if search_resp[0] == False:
        search_resp_val = search_resp[1]
    else:
        location = search_resp[1][0]
        preposition = search_resp[1][1]
        json_body = search_resp[1][2]
        
        count=0
        for element in json_body:
            print("count is "+str(count))
            print("element is "+str(element))
        
            if element['what'] == thing:
                # means we need replace it.
                print("The details are "+str(details))
                element['prep'] = details['prep']
                element['loc'] = details['loc']
                print("the element becomes "+str(element))
                # print("checking "+str(json_body['Item']['thing'][element]))
                # json_body['Item']['thing'][element]['prep'] = 'on'
                # json_body['Item']['thing'][element]['prep'] = 'laptop'
                logger.info("The new json_body is"+str(json_body))
                insert_into_table2(table_name, user_id, json_body)
                logger.info("New details added!: +"+str(json_body))
                return "Done"
            count = count + 1
        
        
    
    # thing_var = details['thing']
    # where_loc = details['location']
    # preposition = details['preposition']
    response = table.update_item(
        Key={
            'uid': user_id
            },
        UpdateExpression= 'SET thing = list_append(if_not_exists(#thing, :empty_list), :details)',
        ExpressionAttributeNames= {
          '#thing': 'thing'
        },
        ExpressionAttributeValues= {
          ':details': [details],
          ':empty_list': []
        }
    )

    logger.info("Response from save DB: "+str(response))
    return True
    