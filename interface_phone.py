#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:17:07 2021
@author: marinacastrillo
"""

from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


Builder.load_string('''
#:import random random.random
#:import Factory kivy.factory.Factory
<CreateAccountWindow>:
    name: "create"
    MDToolbar:
        title: 'Register'
        
        pos_hint: {'top': 1}
        
    MDTextField:
        hint_text: "Name"
        helper_text_mode: "on_focus"
        
        pos_hint:{'x': 0.1, 'y': 0.5}
        size_hint_x:None
        width:250
        
    MDTextField:
        hint_text: "Last name"
        helper_text_mode: "on_focus"
        
        pos_hint:{'x': 0.50, 'y': 0.5}
        size_hint_x:None
        width:250
        
    MDTextField:
        hint_text: "Birthday"
        helper_text_mode: "on_focus"
        
        pos_hint:{'x': 0.1, 'y': 0.4}
        size_hint_x:None
        width:250
         
    MDTextField:
        hint_text: "Sex"
        helper_text_mode: "on_focus"
        
        pos_hint:{'x': 0.50, 'y': 0.4}
        size_hint_x:None
        width:250
     
    MDTextField:
        hint_text: "Email"
        
        helper_text_mode: "on_focus"
        pos_hint:{'x': 0.1, 'y': 0.7}
        size_hint_x:None
        width:250
    MDTextField:
        hint_text: "Password"
        
        helper_text_mode: "on_focus"
       
        pos_hint:{'x': 0.1, 'y': 0.6}
        size_hint_x:None
        width:250
    MDTextField:
        hint_text: "Repeat password"
        
        helper_text_mode: "on_focus"
       
        pos_hint:{'x': 0.50, 'y': 0.6}
        size_hint_x:None
        width:250
    
    MDRoundFlatButton:
       
        pos_hint:{"center_x":0.5,"y":0.2}
        spacing: "56dp"
        adaptive_size: True
        font_size: "17sp"
        text: "Submit"
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = 'LoginWindow'
    MDRoundFlatButton:
        
        pos_hint:{"center_x":0.5,"y":0.1}
        size_hint: 0.2, 0.07
        text: "Log in"
        width:"250"
        spacing: "56dp"
        adaptive_size: True
        font_size: "17sp"
        on_release:
            
            root.manager.transition.direction = "left"
            root.manager.current = 'LoginWindow'
<LoginWindow>:
    MDCard:
        size_hint: 0.8,0.8
        height: 300
        width: 400
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
 
        MDLabel:
            id: welcome_label
            text: "Log in"
            font_size: "25sp"
            valign: 'top'
            halign: 'center'
 
        MDTextFieldRound:
            id: user
            hint_text: "username"
            icon_right: "account"
            width: 500
            font_size: "18sp"
            size_hint: None, None

            pos_hint: {"center_x": 0.5,"y": 0.8}
 
        MDTextFieldRound:
            id: password
            hint_text: "password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 500
            font_size: "18sp"
            pos_hint: {"center_x": 0.5,"y": 0.7}
            password: True

        Widget:
            size_hint_y: None
            height: 100
 
        MDRoundFlatButton:
            text: "LOG IN"
            font_size: "17sp"
            spacing: "56dp"
            adaptive_size: True
            pos_hint: {"center_x": 0.5,"y": 0.5}
            size_hint_x: None
            on_press: 
                root.manager.transition.direction = "left"
                root.manager.current = 'CustomScreen'
 
        MDRoundFlatButton:
            text: "REGISTER"
            font_size: "17sp"
            spacing: "56dp"
            adaptive_size: True
            pos_hint: {"center_x": 0.5,"y": 0.4} 
            size_hint_x: None
            on_press: 
                root.manager.transition.direction = "left"
                root.manager.current = 'CreateAccountWindow'
 
        Widget:
            size_hint_y: None
            height: 500
<CustomScreen>:
    name: 'CustomScreen'
    
    MDToolbar:
        title: 'Menu'
        
        pos_hint: {'top': 1}
    MDFloatingActionButton:
        icon: "bluetooth"
        md_bg_color: app.theme_cls.primary_light
        spacing: "56dp"
        adaptive_size: True
        user_font_size:"50sp"
        size: 600, 600
        size_hint: None, None
        pos_hint: {'center_x':0.5,'center_y':0.35}
        on_release:
            
            root.manager.transition.direction = 'left'
            root.manager.current = 'RVScreen'
            
    MDFloatingActionButton:
        icon: "database-export"
        md_bg_color: app.theme_cls.primary_light
        user_font_size:"50sp"
        size: 600, 600
        size_hint: None, None
        spacing: "56dp"
        adaptive_size: True
        pos_hint: {'center_x':0.5,'center_y':0.65}
        on_release: 
            root.manager.transition.direction = "left"
            root.manager.current = 'MeasuresScreen'
        
            
    MDBoxLayout:
        adaptive_size: True
        orientation: "vertical"
        MDIconButton:
            icon: 'arrow-collapse-left'
            size_hint: None, None
            size: 150, 50
            on_release: 
                root.manager.transition.direction = "left"
                root.manager.current = root.manager.previous()
            
        
<SelectableLabel>:
    
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (0.7529, 0.7529, 0.7529, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
<RVScreen>:
    name: 'RVScreen'
    MDToolbar:
        title: 'Select device'
        
        pos_hint: {'top': 1}
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: 'Select device'
            
            pos_hint: {'top': 1}
        
        RV:
                
                    
            
        MDIconButton:
            icon: 'arrow-collapse-left'
            size_hint: None, None
            size: 150, 50
            on_release: 
                root.manager.transition.direction = "left"
                root.manager.current = root.manager.previous()
            
<CustomDropdown@DropDown>:
    max_height: 300
    bar_width: 5
    bar_color: 0.502, 0.9412, 0.9922   
    bar_inactive_color: 10.051, 0.2157, 0.8824    
    effect_cls: 'ScrollEffect'
    scroll_type: ['bars', 'content']

<MeasuresScreen>:
    name:'MeasuresScreen'
    
    MDBoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        
        MDToolbar:
            title: 'Select a measurement'
            pos_hint: {'top': 1}
        
        Label:
        	id: click_label
        	font_size: 32

        Widget:
            size_hint_y: None
            height: 100

        FloatLayout:
            Spinner:
            	id: spinner_id
                size_hint: None, None
                size: 900, 200
                hling: 'center'
            	text:'Measurements'
                font_size: 50
            	values:['Heart rate','Respiratory rate','Blood pressure','Skin temperature','Weight','Sleep hours','Peripheral oxygen saturation','Activity']
                pos_hint:{'center_x':.5,'y':1.1}
                dropdown_cls: Factory.CustomDropdown

        Widget:
            size_hint_y: None
            height: 100

        FloatLayout:
            Spinner:
            	id: spinner_id
                size_hint: None, None
                size: 900, 200
            	text:'Frecuency'
                hling: 'center'
                font_size: 50
            	values:['Today','Last 7 days','Last Month']
                pos_hint:{'center_x':.5, 'y':1.5}
                dropdown_cls: Factory.CustomDropdown
        
        MDRoundFlatButton:
            text: "Submit"
            font_size: "17sp"
            spacing: "20dp"
            adaptive_size: True
            pos_hint: {"center_x": 0.5,"center_y": 0.5}
            size_hint_x: None
            
            
        Widget:
            size_hint_y: None
            height: 500
                
        MDIconButton:
            icon: 'arrow-collapse-left'
            size_hint: None, None
            size: 150, 50
            on_release: root.manager.current = root.manager.previous()
   
        
        
''')

class CreateAccountWindow(Screen):
    pass

class LoginWindow(Screen):
    pass

class CustomScreen(Screen):
    pass

class MeasuresScreen(Screen): 
	pass

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)
    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        self.dialog = None
        
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Connect to this device?",
                    buttons=[
                        MDFlatButton(
                            text="Yes",
                            theme_text_color="Custom",
                            
                            ),
                        MDFlatButton(
                            text="No",
                            theme_text_color="Custom",
                            
                            ),
                        ],
                    )
                
                self.dialog.open()
                
                
        #else:
            #print("selection removed for {0}".format(rv.data[index]))
        
    



class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(10)]
        
        
    


class RVScreen(Screen):
    pass


class ScreenManagerApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        root = ScreenManager()
        root.add_widget(LoginWindow(name='LoginWindow'))
        root.add_widget(CreateAccountWindow(name='CreateAccountWindow'))
        root.add_widget(CustomScreen(name='CustomScreen'))
        root.add_widget(RVScreen(name='RVScreen'))
        root.add_widget(MeasuresScreen(name='MeasuresScreen'))
        
        
        return root




if __name__ == '__main__':
   
    
    ScreenManagerApp().run()
