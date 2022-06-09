from urllib.request import urlopen
import json

from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, TwoLineListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons

url = "http://127.0.0.1:1722/data"
response = urlopen(url)
jsonObject = json.loads(response.read())

flags = jsonObject['Flags']
pips = jsonObject['Pips']
firegroup = jsonObject['FireGroup']
gui_focus = jsonObject['GuiFocus']
fuel_main = jsonObject['Fuel']["FuelMain"]
fuel_reservoir = jsonObject['Fuel']['FuelReservoir']

flags_bin = list('{0:#034b}'.format(flags))
flags_bin = flags_bin[2:34:1]

flags_desc = [
"srvHighBeam",
"fsdJump",
"Altitude from Average radius",
"Night Vision",
"Hud in Analysis mode",
"In SRV",
"In Fighter",
"In MainShip",
"Being Interdicted",
"IsInDanger",
"Has Lat Long",
"Over Heating ( > % )",
"Low Fuel ( < % )",
"Fsd Cooldown",
"Fsd Charging",
"Fsd MassLocked",
"Srv DriveAssist",
"Srv Turret retracted (close to ship)",
"Srv using Turret view",
"Srv Handbrake",
"Scooping Fuel",
"Silent Running",
"Cargo Scoop Deployed",
"LightsOn",
"In Wing",
"Hardpoints Deployed",
"FlightAssist Off",
"Supercruise",
"Shields Up",
"Landing Gear Down",
"Landed (on planet surface)",
"Docked (on a landing pad)"
]



KV = '''
<ListItemWithCheckbox>:

    IconLeftWidget:
        icon: root.icon

    RightCheckbox:


MDBoxLayout:

    ScrollView:

        MDList:
            id: scroll
'''


class ListItemWithCheckbox(TwoLineListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons = list(md_icons.keys())
        for i in range(32):
            self.root.ids.scroll.add_widget(
               TwoLineListItem(text=flags_desc[i], secondary_text=flags_bin[i])
            )


MainApp().run()