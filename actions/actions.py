from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["division"]["opslots"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def doctors(self, tracker):
        def convertTuple(tup):
                # initialize an empty string
            str = '\n \n'
            for item in tup:
                str = str +'- '+ item + ' \n \n '
            return str
        if("cardiac"==tracker.get_slot("division")):
            f = open('../data.json',)
            data = json.load(f)
            for i in data["cardiac"]:
                a = data["cardiac"].keys()
            f.close() 
            return a      
        if("general"==tracker.get_slot("division")):
            f = open('../data.json',)
            data = json.load(f)
            for i in data["general"]:
                a = data["general"].keys()
            f.close() 
            return a 
        if("ortho"==tracker.get_slot("division")):
            f = open('../data.json',)
            data = json.load(f)
            for i in data["ortho"]:
                a = list(data["general"].keys())
            b = convertTuple(a)
            f.close() 
            return b
        return "None"

    def slots(self, tracker):
        def convertTuple(tup):
            str = ''
            for item in tup:
                str = str + item
            return str
        if("cardiac"==tracker.get_slot("division")):
            f = open('../data.json',)
            data = json.load(f)
            for i in data["cardiac"]:
                b = data["cardiac"]
            f.close() 
            return b    
        if("general"==tracker.get_slot("division")):
            f = open('../data.json',)
            data = json.load(f)
            for i in data["general"]:
                b = data["general"]
            f.close() 
            return b 
        if("ortho"==tracker.get_slot("division")):
            f = open('../data.json',)
            data = json.load(f)
            for i in data["ortho"]:
                b = data["ortho"]
            f.close() 
            ans = ""
            for x in b:
                ans+= '\n\n'+'- '+'Doctor: '+(x)
                for y in b[x]:
                    c = (y,':',b[x][y])
                    str = convertTuple(c)
                    ans+= ' \n \n '+str
            return ans
        return "None"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        if("no"==tracker.get_slot("opslots")):
            a = self.doctors(tracker)
            dispatcher.utter_message(template="utter_doctors",
                                    Names = a,
                                    division = tracker.get_slot("division"))
        else:
            b = self.slots(tracker)
            dispatcher.utter_message(template="utter_details",
                                    slots = b,
                                    division = tracker.get_slot("division"))
