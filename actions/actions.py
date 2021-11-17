# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import datetime

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
from rasa_sdk.forms import FormAction
import pandas as pd


class ActionRoomBookResults(Action):
    def name(self) -> Text:
        return "action_room_book_results"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        num_room = tracker.get_slot("number")
        type_room = tracker.get_slot("type_room")

        dispatcher.utter_message("You have chosen to book " + str(num_room) + " " + str(type_room) + " rooms. Will send a message to reception to book the rooms")
        return [Restarted()]


# class ActionCleanRoomResults(Action):
#     def name(self) -> Text:
#         return "action_clean_room_results"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         raw_clean_time = tracker.get_slot("time")
#         print(raw_clean_time)
#         # try:
#         # 	clean_time = dict(tracker.get_slot("time"))
#         # 	clean_time = clean_time['from']
#         # except:
#         # 	clean_time = tracker.get_slot("time")

#         # date = clean_time[0:10]
#         # time = clean_time[11:19]

#         # # ist = datetime.datetime.strptime(str(date) + ' ' + str(time), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=5, minutes=30)
#         # ist = datetime.datetime.strptime(str(date) + ' ' + str(time), '%Y-%m-%d %H:%M:%S')
#         # ist_now = datetime.datetime.now()

#         # difference = ist - ist_now
#         # print(raw_clean_time)
#         # print(ist)
#         # print(ist_now)
#         # print(difference.total_seconds())
#         # print(difference.days)
#         # print('===================')

#         # day_difference = (ist - ist_now.replace(hour=0, minute=0, second=0)).days

#         # if difference.total_seconds() <= 60:
#         #     dispatcher.utter_message("Sure, I will send someone to your room right away.")
#         #     return [Restarted()]

#         # if int(day_difference) == 0 :
#         # 	formatted_time = ist.strftime("%I:%M %p")
#         # 	dispatcher.utter_message("Sure, I have scheduled a cleaning for " + str(formatted_time) + " today.")
#         # 	return [Restarted()]
#         # elif int(day_difference) == 1:
#         # 	formatted_time = ist.strftime("%I:%M %p")
#         # 	dispatcher.utter_message("Sure, I have scheduled a cleaning for " + str(formatted_time) + " tomorrow.")
#         # 	return [Restarted()]
#         # else:
#         # 	formatted_time = ist.strftime("%I:%M %p on %d %b %Y.")
#         dispatcher.utter_message(f'Sure, I have scheduled a cleaning at {str(raw_clean_time)}')
#         return [Restarted()]

class action_search_restaurants(Action):
    def name(self) -> Text:
        return "action_search_restaurants"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        category = tracker.get_slot('food_type')
        # print(category)

        # df = pd.read_csv('/home/pravalli/hotel_room_bot/Simple-Hotel-Management-Chatbot/cuisine.csv')
        # print(df.head())
                
        # if category == 'italian':
        #     output = df[df['Cuisine'] == 'italian']
        #     print(output)
        # elif category == 'american':
        #     output = df[df['Cuisine'] == 'american']
        # elif category == 'mexican':
        #     output = df[df['Cuisine'] == 'mexican']
        if category == 'italian':
            output = 'You have chosen Italian cuisine.Nearby Italian restaurants are Pizza Antica, Paesano Ristorante Italiano, Mio Vicino'
        if category == 'american':
            output = 'You have chosen American cuisine.Nearby American restaurants are Yard House, The Grill on Alley, The Counter Santana Row'
        if category == 'mexican':
            output = 'You have chosen Mexican cuisine.Nearby Mexican restaurants are Casa Villa, Chavelas Restaurant, Tacos El Compa Taqueria'


        dispatcher.utter_message(text = output)

        return [Restarted()]

class action_search_activities(Action):
    def name(self) -> Text:
        return "action_search_activities"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        activity = tracker.get_slot('activity')
        cost = tracker.get_slot('cost')
        # print(category)

        # df = pd.read_csv('/home/pravalli/hotel_room_bot/Simple-Hotel-Management-Chatbot/cuisine.csv')
        # print(df.head())
                
        # if category == 'italian':
        #     output = df[df['Cuisine'] == 'italian']
        #     print(output)
        # elif category == 'american':
        #     output = df[df['Cuisine'] == 'american']
        # elif category == 'mexican':
        #     output = df[df['Cuisine'] == 'mexican']
        if (activity == 'outdoors') and (cost == 'pay'):
            output = 'Nearby places for outdoor activities.These places might have entry fee 1. Rose Garden - garden to play with kids 2. Hermon Adventures - Has zip line and hike trails 3. Vasona Park - Has train ride and hike trails'
        if activity == 'outdoors' and cost == 'free':
            output = 'Nearby places for outdoor activities without any entry fee 1. River Oaks Park'
        if activity == 'relax' and cost == 'pay':
            output = 'Nearby places to spend a relaxing day 1. Mimi Spa & Saloon 2. Paradise Spa'
        if activity == 'relax' and cost == 'free':
            output = 'Nearby places to spend a relaxing day. No entry fee required 1.Art of living center 2. Just Breathe Yoga'



        dispatcher.utter_message(text = output)

        return [Restarted()]


# class HotelBookForm(FormAction):

#     def name(self):
#         return "hotel_book_form"


#     @staticmethod
#     def required_slots(tracker):
#         return ["number", "type_room"]


#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:

#         dispatcher.utter_message("Thanks, great job!")
#         return []

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
