# Created by: James Sanii
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui

from main_menu_scene import *


class CreditsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'blue', 
                                     parent = self, 
                                     size = self.size)
        #created by james label
        self.text = LabelNode(text = 'Created by James',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.size / 2)
        #gem art position
        self.art_credit_position = Vector2()
        self.art_credit_position.x = self.size.x / 2
        self.art_credit_position.y = self.size.y / 3
        #gem art label
        self.art_credit = LabelNode(text = 'Gem artwork by: Ville Seppanen',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.art_credit_position)
        #sound icon credit location
        self.sound_icon_credit_position = Vector2()
        self.sound_icon_credit_position.x = self.size.x / 2
        self.sound_icon_credit_position.y = self.size.y / 4
        #sound icon credit labelnode
        self.sound_icon_credit = LabelNode(text = 'Sound button artwork by: SCX',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.sound_icon_credit_position)
        #Mr.Coxall credit location
        self.Mr_Coxall_credit_position = Vector2()
        self.Mr_Coxall_credit_position.x = self.size.x / 2
        self.Mr_Coxall_credit_position.y = self.size.y / 2.5
        #Mr.Coxall credit label
        self.Mr_Coxall_credit = LabelNode(text = 'Start, Help, Menu, Backbutton and School Crest by: Mr.Coxall',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.Mr_Coxall_credit_position)
        #create back button position
        back_button_position = self.size
        back_button_position.x = self.size.x /10
        back_button_position.y = self.size.y / 1.2
        #create back button spritenode
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if back button is pressed, go to main menu scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
