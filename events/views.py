from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
import slack

def cards_actions(json_dict):
    user = json_dict['sender']['username']
    card_num = json_dict['card']['permanent_id']
    card_link = 'https://app.gitkraken.com/glo/view/card/{}'.format(card_num)
    column_id = json_dict['card']['column_id']
    card_name = json_dict['card']['name']

    if json_dict['action'] == 'added':
        response_text = "Hello, :wave: *<@{}>* added a new card, {}! Check it out <{}|Here>".format(
            user, card_name, card_link)
        send_msg(response_text) 

    if json_dict['action'] == 'moved_column':
        response_text = "Hello, :wave: *<@{}>* moved the {} card! Check it out <{}|Here>".format(user, card_name,card_link)
        print('sending msg')
        send_msg(response_text)

    # use this to narrow down card added actions to format
    # message to slack, then call in send_msg and pass
    # response_msg
    # card 'permanent_id' is the end of the link. i.e. 
    # you can send a link with below with the numbers
    # at the end added
    # https: // app.gitkraken.com/glo/view/card/bc993b56db3b49cd9c82d253a374dcd8

def card_assignee(json_dict):
    name_data = json_dict['assignees']['added'][0]
    assigned_to = name_data['username']
    card_num = json_dict['card']['id']
    card_name = json_dict['card']['name']
    card_link = 'https://app.gitkraken.com/glo/view/card/{}'.format(card_num)
    response_text = "Hello, :wave: *<@{}>* has been assigned to <{}|{}>".format(
        assigned_to, card_link, card_name)

    send_msg(response_text)


    

def send_msg(response_msg):
    #call this from within specific functs (added_card)
    # after the creation of response_msg dict (see line 41)
    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    client.chat_postMessage(
        channel='sandbox',
        blocks=[
                {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "{}".format(response_msg)
                }
            },
            {
             "type": 'divider'
            }
        ]
    )

@csrf_exempt
def event_hook(request):
    '''
    Creates a simple reply when a user writes a dm to
    the bot.
    '''
    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    json_dict = json.loads(request.body.decode('utf-8'))    
    if json_dict['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in json_dict:
        if json_dict['type'] == 'url_verification':
            response_dict = {"challenge": json_dict['challenge']}
            return JsonResponse(response_dict, safe=False)   
    if 'event' in json_dict:
        event_msg = json_dict['event']
        # if message if from the bot... ignore
        if 'bot_id' in event_msg:
            print('bot message, ignoring')
            return HttpResponse(status=200)
        # if message is from real user, reply
        if event_msg['type'] == 'message':
            user = event_msg['user']
            channel = event_msg['channel']
            response_msg = ":wave:, Hello <@{}>".format(user)
            client.chat_postMessage(channel=channel, text=response_msg)
    return HttpResponse(status=200)        

@require_POST
@csrf_exempt
def incoming_web_hook(request):
    json_head = request.headers
    json_dict = json.loads(request.body.decode('utf-8'))
    if json_head['x-gk-event'] == 'cards':
        if (json_dict['action'] == 'added') or (json_dict['action'] == 'moved_column'):
            cards_actions(json_dict)
        if json_dict['action'] == 'assignees_updated':
            card_assignee(json_dict)
        # Other actions for cards type event
    # other events in json head as needed
        # actions for each of the events
    
    return HttpResponse('Hey, You hit the API')
