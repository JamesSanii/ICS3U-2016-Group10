# Created by: James
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from main_menu_scene import *
from pause_scene import *
import ui
import random
import time
import sound
import json
class GameScene(Scene):
	
	
		
    def setup(self):
        # this method is called, when user moves to this scene
        #function that assigns pictures to each gem button
        def assign_picture(gem_value):
            if gem_value == 1:
                gem_picture = './assets/sprites/gem1.PNG'
                return gem_picture
            elif gem_value == 2:
                gem_picture = './assets/sprites/gem2.PNG'
                return gem_picture
            elif gem_value == 3:
                gem_picture = './assets/sprites/gem3.PNG'
                return gem_picture
            elif gem_value == 4:
                gem_picture = './assets/sprites/gem4.PNG'
                return gem_picture
            elif gem_value == 5:
                gem_picture = './assets/sprites/gem5.PNG'
                return gem_picture
            elif gem_value == 6:
                gem_picture = './assets/sprites/gem6.PNG'
                return gem_picture
				
        # add white background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
        # variable that is used to see if another gem is selected to be swapped
        self.another_gem_pushed = False
        #gems that need to be randomized are put into this array
        self.to_be_removed = []
        #create position for main_menu_button
        self.main_menu_button_position = Vector2()
        self.main_menu_button_position.x = self.size.x/3
        self.main_menu_button_position.y = self.size.y/8
        #create position for menu button
        self.menu_button_position = Vector2()
        self.menu_button_position.x = self.size.x/2
        self.menu_button_position.y = self.size.y/2
        #create main menu button
        self.main_menu_button = SpriteNode('./assets/sprites/menu_button.png',
                                       parent = self,
                                       position = self.main_menu_button_position,
                                       scale = 0.5)
        #create pause button location
        self.pause_button_position = Vector2()
        self.pause_button_position.x = self.size.x/1.5
        self.pause_button_position.y = self.size.y/8
        #create menu button and pause button and sound button
        
        self.menu_button = SpriteNode('./assets/sprites/menu_button.png',
                                      parent = self,
                                      position = self.menu_button_position,
                                      alpha = -1)
        self.pause_button = SpriteNode('./assets/sprites/help.png',
                                       parent = self,
                                       position = self.pause_button_position,
                                       scale = 0.5)
        self.sound_button_position = Vector2()
        self.sound_button_position.x = self.size.x/10
        self.sound_button_position.y = self.size.y/8
        #create sound button
        self.sound_button = SpriteNode('./assets/sprites/sound_off.PNG',
                                      parent = self,
                                      position = self.sound_button_position,
                                      scale = 2)
        #number of tiles
        self.tile_number=100
        #array that holds all gem values
        self.chart = []
		#put numbers in array
        for number in range(0, self.tile_number):
            self.chart.append(random.randint(1, 6))
        
        #variables
        self.top_scores_file = open('./highscore.txt' , 'r+')
        self.the_highscore = json.load(self.top_scores_file)
        self.highscore = max(self.the_highscore)
        
        self.the_selected = 0
        self.play_sound = True
        self.score = 0
        self.count = 0
        self.number_count = 0
        self.game_over = False
        #the following are used for positioning in check function
        self.one_right = 1
        self.two_right = 2
        self.three_right = 3
        self.four_right = 4
        self.five_right = 5
        self.six_right = 6
        self.one_down = 7
        self.two_down = 14
        self.three_down = 21
        self.four_down = 28
        self.five_down = 35

        #gem positions and gem buttons
        self.gem_1_position = Vector2()
        self.gem_1_position.x = self.size.x/4.57
        self.gem_1_position.y = self.size.y/1.15
        self.gem_1_button = SpriteNode(assign_picture(self.chart[0]),
                                       parent = self,
                                       position = self.gem_1_position)
        self.gem_2_position = Vector2()
        self.gem_2_position.x = self.size.x/3.16
        self.gem_2_position.y = self.size.y/1.15
        self.gem_2_button = SpriteNode(assign_picture(self.chart[1]),
                                       parent = self,
                                       position = self.gem_2_position)
       
        self.gem_3_position = Vector2()
        self.gem_3_position.x = self.size.x/2.42
        self.gem_3_position.y = self.size.y/1.15
        self.gem_3_button = SpriteNode(assign_picture(self.chart[2]),
                                       parent = self,
                                       position = self.gem_3_position)
        self.gem_4_position = Vector2()
        self.gem_4_position.x = self.size.x/1.95
        self.gem_4_position.y = self.size.y/1.15
        self.gem_4_button = SpriteNode(assign_picture(self.chart[3]),
                                       parent = self,
                                       position = self.gem_4_position)
        self.gem_5_position = Vector2()
        self.gem_5_position.x = self.size.x/1.64
        self.gem_5_position.y = self.size.y/1.15
        self.gem_5_button = SpriteNode(assign_picture(self.chart[4]),
                                       parent = self,
                                       position = self.gem_5_position)
       
        self.gem_6_position = Vector2()
        self.gem_6_position.x = self.size.x/1.4
        self.gem_6_position.y = self.size.y/1.15
        self.gem_6_button = SpriteNode(assign_picture(self.chart[5]),
                                       parent = self,
                                       position = self.gem_6_position)
        self.gem_7_position = Vector2()
        self.gem_7_position.x = self.size.x/1.24
        self.gem_7_position.y = self.size.y/1.15
        self.gem_7_button = SpriteNode(assign_picture(self.chart[6]),
                                       parent = self,
                                       position = self.gem_7_position)
        self.gem_8_position = Vector2()
        self.gem_8_position.x = self.size.x/4.57
        self.gem_8_position.y = self.size.y/1.35
        self.gem_8_button = SpriteNode(assign_picture(self.chart[7]),
                                       parent = self,
                                       position = self.gem_8_position)
        self.gem_9_position = Vector2()
        self.gem_9_position.x = self.size.x/3.16
        self.gem_9_position.y = self.size.y/1.35
        self.gem_9_button = SpriteNode(assign_picture(self.chart[8]),
                                       parent = self,
                                       position = self.gem_9_position)
        self.gem_10_position = Vector2()
        self.gem_10_position.x = self.size.x/2.42
        self.gem_10_position.y = self.size.y/1.35
        self.gem_10_button = SpriteNode(assign_picture(self.chart[9]),
                                       parent = self,
                                       position = self.gem_10_position)
       
        self.gem_11_position = Vector2()
        self.gem_11_position.x = self.size.x/1.95
        self.gem_11_position.y = self.size.y/1.35
        self.gem_11_button = SpriteNode(assign_picture(self.chart[10]),
                                       parent = self,
                                       position = self.gem_11_position)
        self.gem_12_position = Vector2()
        self.gem_12_position.x = self.size.x/1.64
        self.gem_12_position.y = self.size.y/1.35
        self.gem_12_button = SpriteNode(assign_picture(self.chart[11]),
                                       parent = self,
                                       position = self.gem_12_position)
        self.gem_13_position = Vector2()
        self.gem_13_position.x = self.size.x/1.4
        self.gem_13_position.y = self.size.y/1.35
        self.gem_13_button = SpriteNode(assign_picture(self.chart[12]),
                                       parent = self,
                                       position = self.gem_13_position)
       
        self.gem_14_position = Vector2()
        self.gem_14_position.x = self.size.x/1.24
        self.gem_14_position.y = self.size.y/1.35
        self.gem_14_button = SpriteNode(assign_picture(self.chart[13]),
                                       parent = self,
                                       position = self.gem_14_position)
        self.gem_15_position = Vector2()
        self.gem_15_position.x = self.size.x/4.57
        self.gem_15_position.y = self.size.y/1.64
        self.gem_15_button = SpriteNode(assign_picture(self.chart[14]),
                                       parent = self,
                                       position = self.gem_15_position)
        self.gem_16_position = Vector2()
        self.gem_16_position.x = self.size.x/3.16
        self.gem_16_position.y = self.size.y/1.64
        self.gem_16_button = SpriteNode(assign_picture(self.chart[15]),
                                       parent = self,
                                       position = self.gem_16_position)
        self.gem_17_position = Vector2()
        self.gem_17_position.x = self.size.x/2.42
        self.gem_17_position.y = self.size.y/1.64
        self.gem_17_button = SpriteNode(assign_picture(self.chart[16]),
                                       parent = self,
                                       position = self.gem_17_position)
        self.gem_18_position = Vector2()
        self.gem_18_position.x = self.size.x/1.95
        self.gem_18_position.y = self.size.y/1.64
        self.gem_18_button = SpriteNode(assign_picture(self.chart[17]),
                                       parent = self,
                                       position = self.gem_18_position)
       
        self.gem_19_position = Vector2()
        self.gem_19_position.x = self.size.x/1.64
        self.gem_19_position.y = self.size.y/1.64
        self.gem_19_button = SpriteNode(assign_picture(self.chart[18]),
                                       parent = self,
                                       position = self.gem_19_position)
        self.gem_20_position = Vector2()
        self.gem_20_position.x = self.size.x/1.4
        self.gem_20_position.y = self.size.y/1.64
        self.gem_20_button = SpriteNode(assign_picture(self.chart[19]),
                                       parent = self,
                                       position = self.gem_20_position)
        self.gem_21_position = Vector2()
        self.gem_21_position.x = self.size.x/1.24
        self.gem_21_position.y = self.size.y/1.64
        self.gem_21_button = SpriteNode(assign_picture(self.chart[20]),
                                       parent = self,
                                       position = self.gem_21_position)
        self.gem_22_position = Vector2()
        self.gem_22_position.x = self.size.x/4.57
        self.gem_22_position.y = self.size.y/2.08
        self.gem_22_button = SpriteNode(assign_picture(self.chart[21]),
                                       parent = self,
                                       position = self.gem_22_position)
        self.gem_23_position = Vector2()
        self.gem_23_position.x = self.size.x/3.16
        self.gem_23_position.y = self.size.y/2.08
        self.gem_23_button = SpriteNode(assign_picture(self.chart[22]),
                                       parent = self,
                                       position = self.gem_23_position)
        self.gem_24_position = Vector2()
        self.gem_24_position.x = self.size.x/2.42
        self.gem_24_position.y = self.size.y/2.08
        self.gem_24_button = SpriteNode(assign_picture(self.chart[23]),
                                       parent = self,
                                       position = self.gem_24_position)
        self.gem_25_position = Vector2()
        self.gem_25_position.x = self.size.x/1.95
        self.gem_25_position.y = self.size.y/2.08
        self.gem_25_button = SpriteNode(assign_picture(self.chart[24]),
                                       parent = self,
                                       position = self.gem_25_position)
        self.gem_26_position = Vector2()
        self.gem_26_position.x = self.size.x/1.64
        self.gem_26_position.y = self.size.y/2.08
        self.gem_26_button = SpriteNode(assign_picture(self.chart[25]),
                                       parent = self,
                                       position = self.gem_26_position)
        self.gem_27_position = Vector2()
        self.gem_27_position.x = self.size.x/1.4
        self.gem_27_position.y = self.size.y/2.08
        self.gem_27_button = SpriteNode(assign_picture(self.chart[26]),
                                       parent = self,
                                       position = self.gem_27_position)
        self.gem_28_position = Vector2()
        self.gem_28_position.x = self.size.x/1.24
        self.gem_28_position.y = self.size.y/2.08
        self.gem_28_button = SpriteNode(assign_picture(self.chart[27]),
                                       parent = self,
                                       position = self.gem_28_position)
        self.gem_29_position = Vector2()
        self.gem_29_position.x = self.size.x/4.57
        self.gem_29_position.y = self.size.y/2.80
        self.gem_29_button = SpriteNode(assign_picture(self.chart[28]),
                                       parent = self,
                                       position = self.gem_29_position)
       
        self.gem_30_position = Vector2()
        self.gem_30_position.x = self.size.x/3.16
        self.gem_30_position.y = self.size.y/2.8
        self.gem_30_button = SpriteNode(assign_picture(self.chart[29]),
                                       parent = self,
                                       position = self.gem_30_position)
        self.gem_31_position = Vector2()
        self.gem_31_position.x = self.size.x/2.42
        self.gem_31_position.y = self.size.y/2.8
        self.gem_31_button = SpriteNode(assign_picture(self.chart[30]),
                                       parent = self,
                                       position = self.gem_31_position)
        self.gem_32_position = Vector2()
        self.gem_32_position.x = self.size.x/1.95
        self.gem_32_position.y = self.size.y/2.8
        self.gem_32_button = SpriteNode(assign_picture(self.chart[31]),
                                       parent = self,
                                       position = self.gem_32_position)
        self.gem_33_position = Vector2()
        self.gem_33_position.x = self.size.x/1.64
        self.gem_33_position.y = self.size.y/2.8
        self.gem_33_button = SpriteNode(assign_picture(self.chart[32]),
                                       parent = self,
                                       position = self.gem_33_position)
        self.gem_34_position = Vector2()
        self.gem_34_position.x = self.size.x/1.4
        self.gem_34_position.y = self.size.y/2.8
        self.gem_34_button = SpriteNode(assign_picture(self.chart[33]),
                                       parent = self,
                                       position = self.gem_34_position)
        self.gem_35_position = Vector2()
        self.gem_35_position.x = self.size.x/1.24
        self.gem_35_position.y = self.size.y/2.8
        self.gem_35_button = SpriteNode(assign_picture(self.chart[34]),
                                       parent = self,
                                       position = self.gem_35_position)
        self.gem_36_position = Vector2()
        self.gem_36_position.x = self.size.x/4.57
        self.gem_36_position.y = self.size.y/4
        self.gem_36_button = SpriteNode(assign_picture(self.chart[35]),
                                       parent = self,
                                       position = self.gem_36_position)
       
        self.gem_37_position = Vector2()
        self.gem_37_position.x = self.size.x/3.16
        self.gem_37_position.y = self.size.y/4
        self.gem_37_button = SpriteNode(assign_picture(self.chart[36]),
                                       parent = self,
                                       position = self.gem_37_position)
        self.gem_38_position = Vector2()
        self.gem_38_position.x = self.size.x/2.42
        self.gem_38_position.y = self.size.y/4
        self.gem_38_button = SpriteNode(assign_picture(self.chart[37]),
                                       parent = self,
                                       position = self.gem_38_position)
        self.gem_39_position = Vector2()
        self.gem_39_position.x = self.size.x/1.95
        self.gem_39_position.y = self.size.y/4
        self.gem_39_button = SpriteNode(assign_picture(self.chart[38]),
                                       parent = self,
                                       position = self.gem_39_position)
        self.gem_40_position = Vector2()
        self.gem_40_position.x = self.size.x/1.64
        self.gem_40_position.y = self.size.y/4
        self.gem_40_button = SpriteNode(assign_picture(self.chart[39]),
                                       parent = self,
                                       position = self.gem_40_position)
        self.gem_41_position = Vector2()
        self.gem_41_position.x = self.size.x/1.4
        self.gem_41_position.y = self.size.y/4
        self.gem_41_button = SpriteNode(assign_picture(self.chart[40]),
                                       parent = self,
                                       position = self.gem_41_position)
        self.gem_42_position = Vector2()
        self.gem_42_position.x = self.size.x/1.24
        self.gem_42_position.y = self.size.y/4
        self.gem_42_button = SpriteNode(assign_picture(self.chart[41]),
                                       parent = self,
                                       position = self.gem_42_position)
        #create moves initial value and moves label that displays the number of moves
        self.moves = 25
        self.moves_position = Vector2()
        self.moves_position.x = self.size.x / 10
        self.moves_position.y = self.size.y/1.5
        self.moves_label = LabelNode(text = 'moves: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     color = 'black',
                                     position = self.moves_position)
        #create score label and shows score to user
        self.score_position = Vector2()
        self.score_position.x = self.size.x / 10
        self.score_position.y = self.size.y/1.05
        self.score_label = LabelNode(text = 'score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     color = 'black',
                                     position = self.score_position)
        #highscore label and highscore label position
        self.highscore_position = Vector2()
        self.highscore_position.x = self.size.x / 2
        self.highscore_position.y = self.size.y/1.05
        self.highscore_label = LabelNode(text = 'Highscore: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     color = 'black',
                                     position = self.highscore_position)

    def update(self):
        # this method is called, hopefully, 60 times a second
        
        #assigns pictures depending on value
        def assign_picture(gem_value):
            if gem_value == 1:
                gem_picture = './assets/sprites/gem1.PNG'
                return gem_picture
            elif gem_value == 2:
                gem_picture = './assets/sprites/gem2.PNG'
                return gem_picture
            elif gem_value == 3:
                gem_picture = './assets/sprites/gem3.PNG'
                return gem_picture
            elif gem_value == 4:
                gem_picture = './assets/sprites/gem4.PNG'
                return gem_picture
            elif gem_value == 5:
                gem_picture = './assets/sprites/gem5.PNG'
                return gem_picture
            elif gem_value == 6:
                gem_picture = './assets/sprites/gem6.PNG'
                return gem_picture
        #assigns a picture to a gem button if they are selected
        def assign_selected_picture(gem_value):
            if gem_value == 1:
                gem_picture = './assets/sprites/gem_1_selected.JPG'
                return gem_picture
            elif gem_value == 2:
                gem_picture = './assets/sprites/gem_2_selected.JPG'
                return gem_picture
            elif gem_value == 3:
                gem_picture = './assets/sprites/gem_3_selected.JPG'
                return gem_picture
            elif gem_value == 4:
                gem_picture = './assets/sprites/gem_4_selected.JPG'
                return gem_picture
            elif gem_value == 5:
                gem_picture = './assets/sprites/gem_5_selected.JPG'
                return gem_picture
            elif gem_value == 6:
                gem_picture = './assets/sprites/gem_6_selected.JPG'
                return gem_picture
        #used to check for matches on the board horizontaly add points accordingly
        #items that need to be randomized are appended into to_be_removed for later randomized
        for gem in range(-1,41):
                if self.chart[gem]== self.chart[gem+self.one_right]==self.chart[gem+self.two_right] and (gem+self.two_right)%7!=0:
                    self.to_be_removed.append(gem)
                    self.to_be_removed.append(gem+self.one_right)
                    self.to_be_removed.append(gem+self.two_right)
                    if self.play_sound == True and self.moves != 25:
                        #if play_sound is true play sound effect
                        sound.play_effect('./assets/sounds/Explosion_3.caf')
                    self.score = self.score+3
                    if self.chart[gem+self.two_right] == self.chart[gem+self.three_right] and (gem+self.three_right)%7!=0:
                        self.to_be_removed.append(gem+self.three_right)
                        self.score=self.score+2
                        if self.chart[gem+self.three_right] == self.chart[gem+self.four_right] and (gem+self.four_right)%7!=0:
                            self.to_be_removed.append(gem+self.four_right)
                            self.score=self.score+2
                            if self.chart[gem+self.four_right] == self.chart[gem+self.five_right] and (gem+self.five_right)%7!=0:
                                self.to_be_removed.append(gem+self.five_right)
                                self.score=self.score+2
                                if self.chart[gem+self.five_right] == self.chart[gem+self.six_right] and (gem+self.six_right)%7!=0:
                                    self.to_be_removed.append(gem+self.six_right)
                                    self.score=self.score+2
        #used to check for matches vertically on the board add points accordingly
        #items that need to be randomized are appended into to_be_removed for later randomized
        for gem in range(-1,41):
                if self.chart[gem]== self.chart[gem+self.one_down]==self.chart[gem+self.two_down]:
                    self.to_be_removed.append(gem)
                    self.to_be_removed.append(gem+self.one_down)
                    self.to_be_removed.append(gem+self.two_down)
                    if self.play_sound == True and self.moves != 25:
                        sound.play_effect('./assets/sounds/Explosion_3.caf')
                    self.score = self.score+3
                    if self.chart[gem+self.two_down] == self.chart[gem+self.three_down]:
                        self.to_be_removed.append(gem+self.three_down)
                        self.score = self.score+3
                        if self.chart[gem+self.three_down] == self.chart[gem+self.four_down]:
                            self.to_be_removed.append(gem+self.four_down)
                            self.score = self.score+3
                            if self.chart[gem+self.four_down] == self.chart[gem+self.five_down]:
                                self.to_be_removed.append(gem+self.five_down)
                                self.score = self.score+3

        #randomizes the gems that have been matched
        for number in self.to_be_removed:
            self.chart[number]=random.randint(1,6)
            self.to_be_removed.remove(number)
            while number in self.to_be_removed:
                #since a number may be appended multiple times it needs to be removed multiple times
                self.to_be_removed.remove(number)
                #score is adjusted based off how many extra times it was added to the array
                self.score = self.score-1
        #assignes the score to zero until a move is made
        if self.moves == 25:
            self.score = 0

                
        #updates each picture depending on their new value
        self.gem_1_button.texture =Texture(assign_picture(self.chart[0]))
        self.gem_2_button.texture =Texture(assign_picture(self.chart[1]))
        self.gem_3_button.texture =Texture(assign_picture(self.chart[2]))
        self.gem_4_button.texture =Texture(assign_picture(self.chart[3]))
        self.gem_5_button.texture =Texture(assign_picture(self.chart[4]))
        self.gem_6_button.texture =Texture(assign_picture(self.chart[5]))
        self.gem_7_button.texture =Texture(assign_picture(self.chart[6]))
        self.gem_8_button.texture =Texture(assign_picture(self.chart[7]))
        self.gem_9_button.texture =Texture(assign_picture(self.chart[8]))
        self.gem_10_button.texture =Texture(assign_picture(self.chart[9]))
        self.gem_11_button.texture =Texture(assign_picture(self.chart[10]))
        self.gem_12_button.texture =Texture(assign_picture(self.chart[11]))
        self.gem_13_button.texture =Texture(assign_picture(self.chart[12]))
        self.gem_14_button.texture =Texture(assign_picture(self.chart[13]))
        self.gem_15_button.texture =Texture(assign_picture(self.chart[14]))
        self.gem_16_button.texture =Texture(assign_picture(self.chart[15]))
        self.gem_17_button.texture =Texture(assign_picture(self.chart[16]))
        self.gem_18_button.texture =Texture(assign_picture(self.chart[17]))
        self.gem_19_button.texture =Texture(assign_picture(self.chart[18]))
        self.gem_20_button.texture =Texture(assign_picture(self.chart[19]))
        self.gem_21_button.texture =Texture(assign_picture(self.chart[20]))
        self.gem_22_button.texture =Texture(assign_picture(self.chart[21]))
        self.gem_23_button.texture =Texture(assign_picture(self.chart[22]))
        self.gem_24_button.texture =Texture(assign_picture(self.chart[23]))
        self.gem_25_button.texture =Texture(assign_picture(self.chart[24]))
        self.gem_26_button.texture =Texture(assign_picture(self.chart[25]))
        self.gem_27_button.texture =Texture(assign_picture(self.chart[26]))
        self.gem_28_button.texture =Texture(assign_picture(self.chart[27]))
        self.gem_29_button.texture =Texture(assign_picture(self.chart[28]))
        self.gem_30_button.texture =Texture(assign_picture(self.chart[29]))
        self.gem_31_button.texture =Texture(assign_picture(self.chart[30]))
        self.gem_32_button.texture =Texture(assign_picture(self.chart[31]))
        self.gem_33_button.texture =Texture(assign_picture(self.chart[32]))
        self.gem_34_button.texture =Texture(assign_picture(self.chart[33]))
        self.gem_35_button.texture =Texture(assign_picture(self.chart[34]))
        self.gem_36_button.texture =Texture(assign_picture(self.chart[35]))
        self.gem_37_button.texture =Texture(assign_picture(self.chart[36]))
        self.gem_38_button.texture =Texture(assign_picture(self.chart[37]))
        self.gem_39_button.texture =Texture(assign_picture(self.chart[38]))
        self.gem_40_button.texture =Texture(assign_picture(self.chart[39]))
        self.gem_41_button.texture =Texture(assign_picture(self.chart[40]))
        self.gem_42_button.texture =Texture(assign_picture(self.chart[41]))
        # if play_sound is True, sound on button is shown
        if self.play_sound == True:
            self.sound_button.texture = Texture('./assets/sprites/sound_on.PNG')
        # if play_sound is False, sound off button is shown
        if self.play_sound == False:
            self.sound_button.texture = Texture('./assets/sprites/sound_off.PNG')
        #depending on what the_selected is equal to gives the selected gem a new picture
        if self.the_selected == 1:
            self.gem_1_button.texture =Texture(assign_selected_picture(self.chart[0]))
        if self.the_selected == 2:
            self.gem_2_button.texture =Texture(assign_selected_picture(self.chart[1]))
        if self.the_selected == 3:
            self.gem_3_button.texture =Texture(assign_selected_picture(self.chart[2]))
        if self.the_selected == 4:
            self.gem_4_button.texture =Texture(assign_selected_picture(self.chart[3]))
        if self.the_selected == 5:
            self.gem_5_button.texture =Texture(assign_selected_picture(self.chart[4]))
        if self.the_selected == 6:
            self.gem_6_button.texture =Texture(assign_selected_picture(self.chart[5]))
        if self.the_selected == 7:
            self.gem_7_button.texture =Texture(assign_selected_picture(self.chart[6]))
        if self.the_selected == 8:
            self.gem_8_button.texture =Texture(assign_selected_picture(self.chart[7]))
        if self.the_selected == 9:
            self.gem_9_button.texture =Texture(assign_selected_picture(self.chart[8]))
        if self.the_selected == 10:
            self.gem_10_button.texture =Texture(assign_selected_picture(self.chart[9]))
        if self.the_selected == 11:
            self.gem_11_button.texture =Texture(assign_selected_picture(self.chart[10]))
        if self.the_selected == 12:
            self.gem_12_button.texture =Texture(assign_selected_picture(self.chart[11]))
        if self.the_selected == 13:
            self.gem_13_button.texture =Texture(assign_selected_picture(self.chart[12]))
        if self.the_selected == 14:
            self.gem_14_button.texture =Texture(assign_selected_picture(self.chart[13]))
        if self.the_selected == 15:
            self.gem_15_button.texture =Texture(assign_selected_picture(self.chart[14]))
        if self.the_selected == 16:
            self.gem_16_button.texture =Texture(assign_selected_picture(self.chart[15]))
        if self.the_selected == 17:
            self.gem_17_button.texture =Texture(assign_selected_picture(self.chart[16]))
        if self.the_selected == 18:
            self.gem_18_button.texture =Texture(assign_selected_picture(self.chart[17]))
        if self.the_selected == 19:
            self.gem_19_button.texture =Texture(assign_selected_picture(self.chart[18]))
        if self.the_selected == 20:
            self.gem_20_button.texture =Texture(assign_selected_picture(self.chart[19]))
        if self.the_selected == 21:
            self.gem_21_button.texture =Texture(assign_selected_picture(self.chart[20]))
        if self.the_selected == 22:
            self.gem_22_button.texture =Texture(assign_selected_picture(self.chart[21]))
        if self.the_selected == 23:
            self.gem_23_button.texture =Texture(assign_selected_picture(self.chart[22]))
        if self.the_selected == 24:
            self.gem_24_button.texture =Texture(assign_selected_picture(self.chart[23]))
        if self.the_selected == 25:
            self.gem_25_button.texture =Texture(assign_selected_picture(self.chart[24]))
        if self.the_selected == 26:
            self.gem_26_button.texture =Texture(assign_selected_picture(self.chart[25]))
        if self.the_selected == 27:
            self.gem_27_button.texture =Texture(assign_selected_picture(self.chart[26]))
        if self.the_selected == 28:
            self.gem_28_button.texture =Texture(assign_selected_picture(self.chart[27]))
        if self.the_selected == 29:
            self.gem_29_button.texture =Texture(assign_selected_picture(self.chart[28]))
        if self.the_selected == 30:
            self.gem_30_button.texture =Texture(assign_selected_picture(self.chart[29]))
        if self.the_selected == 31:
            self.gem_31_button.texture =Texture(assign_selected_picture(self.chart[30]))
        if self.the_selected == 32:
            self.gem_32_button.texture =Texture(assign_selected_picture(self.chart[31]))
        if self.the_selected == 33:
            self.gem_33_button.texture =Texture(assign_selected_picture(self.chart[32]))
        if self.the_selected == 34:
            self.gem_34_button.texture =Texture(assign_selected_picture(self.chart[33]))
        if self.the_selected == 35:
            self.gem_35_button.texture =Texture(assign_selected_picture(self.chart[34]))
        if self.the_selected == 36:
            self.gem_36_button.texture =Texture(assign_selected_picture(self.chart[35]))
        if self.the_selected == 37:
            self.gem_37_button.texture =Texture(assign_selected_picture(self.chart[36]))
        if self.the_selected == 38:
            self.gem_38_button.texture =Texture(assign_selected_picture(self.chart[37]))
        if self.the_selected == 39:
            self.gem_39_button.texture =Texture(assign_selected_picture(self.chart[38]))
        if self.the_selected == 40:
            self.gem_40_button.texture =Texture(assign_selected_picture(self.chart[39]))
        if self.the_selected == 41:
            self.gem_41_button.texture =Texture(assign_selected_picture(self.chart[40]))
        if self.the_selected == 42:
            self.gem_42_button.texture =Texture(assign_selected_picture(self.chart[41]))
        #update moves and score label values
        self.moves_label.text = 'Moves: ' + str(self.moves)
        self.score_label.text = 'Score: ' + str(self.score)
        if self.score >= self.highscore:
            self.highscore_label.text = 'Highscore: ' + str(self.score)
        else:
            self.highscore_label.text = 'Highscore: ' + str(self.highscore)
        #if moves is zero, gameover happens and the main menu button appears
        if self.moves == 0:
            self.game_over = True
            self.the_highscore.append(self.score)
            self.highscore = max(self.the_highscore)
            self.top_scores_file.seek(0)
            json.dump(self.the_highscore, self.top_scores_file)
            self.top_scores_file.close()
            print(self.highscore)
            self.menu_button = SpriteNode('./assets/sprites/menu_button.png',
                                      parent = self,
                                      position = self.menu_button_position,
                                      alpha = 1.0)
        
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #if pause button is pushed go to pause menu
        if self.pause_button.frame.contains_point(touch.location):
            self.present_modal_scene(PauseScene())
        #if main menu button is pushed go to main menu
        if self.main_menu_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        #changes the sound value to the opposite one when pressed
        if self.sound_button.frame.contains_point(touch.location):
            if self.play_sound == True:
                self.play_sound = False
            elif self.play_sound == False:
                self.play_sound = True

        #all of the following applies to all gem buttons
        #if the gem is pushed 
        if self.gem_1_button.frame.contains_point(touch.location) and self.game_over == False:
            #if another gem was already pushed
            if self.another_gem_pushed == True:
                #swaps the two selected tiles values
                self.chart[self.selected]=self.chart[0]
                self.chart[0] = self.placeholder
                #another gem pushed is now false
                self.another_gem_pushed = False
                #reduced number of moves by 1
                if self.the_selected != 1:
                    self.moves= self.moves-1
                #the_selected is now zero making all backgrounds white
                self.the_selected = 0
                
                
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[0]
                self.selected = 0
                self.the_selected = 1
                
        if self.gem_2_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[1]
                self.chart[1] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 2:
                    self.moves= self.moves-1
                self.the_selected = 0
                
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[1]
                self.selected = 1
                self.the_selected = 2
        if self.gem_3_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[2]
                self.chart[2] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 3:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[2]
                self.selected = 2
                self.the_selected = 3
        if self.gem_4_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[3]
                self.chart[3] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 4:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[3]
                self.selected = 3
                self.the_selected = 4
        if self.gem_5_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.another_gem_pushed = False
                self.chart[self.selected]=self.chart[4]
                self.chart[4] = self.placeholder
                if self.the_selected != 5:
                    self.moves= self.moves-1
                self.the_selected = 0
                
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[4]
                self.selected = 4
                self.the_selected = 5
        if self.gem_6_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[5]
                self.chart[5] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 6:
                    self.moves= self.moves-1
                self.the_selected = 0
                
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[5]
                self.selected = 5
                self.the_selected = 6
        if self.gem_7_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[6]
                self.chart[6] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 7:
                    self.moves= self.moves-1
                self.the_selected = 0
                
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[6]
                self.selected = 6
                self.the_selected = 7
                
        if self.gem_8_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[7]
                self.chart[7] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 8:
                    self.moves= self.moves-1
                self.the_selected = 0
                
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[7]
                self.selected = 7
                self.the_selected = 8
        if self.gem_9_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[8]
                self.chart[8] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 9:
                    self.moves= self.moves-1
                self.the_selected = 0
                
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[8]
                self.selected = 8
                self.the_selected = 9
        if self.gem_10_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[9]
                self.chart[9] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 10:
                    self.moves= self.moves-1
                self.the_selected = 0
                
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[9]
                self.selected = 9
                self.the_selected = 10
        if self.gem_11_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[10]
                self.chart[10] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 11:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[10]
                self.selected = 10
                self.the_selected = 11
                
        if self.gem_12_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[11]
                self.chart[11] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 12:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[11]
                self.selected = 11
                self.the_selected = 12
        if self.gem_13_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[12]
                self.chart[12] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 13:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[12]
                self.selected = 12
                self.the_selected = 13
        if self.gem_14_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[13]
                self.chart[13] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 14:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[13]
                self.selected = 13
                self.the_selected = 14
        if self.gem_15_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[14]
                self.chart[14] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 15:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[14]
                self.selected = 14
                self.the_selected = 15
        if self.gem_16_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[15]
                self.chart[15] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 16:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[15]
                self.selected = 15
                self.the_selected = 16
        if self.gem_17_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[16]
                self.chart[16] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 17:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[16]
                self.selected = 16
                self.the_selected = 17
        if self.gem_18_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[17]
                self.chart[17] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 18:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[17]
                self.selected = 17
                self.the_selected = 18
        if self.gem_19_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[18]
                self.chart[18] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 19:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[18]
                self.selected = 18
                self.the_selected = 19
        if self.gem_20_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[19]
                self.chart[19] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 20:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[19]
                self.selected = 19
                self.the_selected = 20
        if self.gem_21_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[20]
                self.chart[20] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 21:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[20]
                self.selected = 20
                self.the_selected = 21
        if self.gem_22_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[21]
                self.chart[21] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 22:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[21]
                self.selected = 21
                self.the_selected = 22
        if self.gem_23_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[22]
                self.chart[22] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 23:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[22]
                self.selected = 22
                self.the_selected = 23
        if self.gem_24_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[23]
                self.chart[23] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 24:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[23]
                self.selected = 23
                self.the_selected = 24
        if self.gem_25_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[24]
                self.chart[24] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 25:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[24]
                self.selected = 24
                self.the_selected = 25
        if self.gem_26_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[25]
                self.chart[25] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 26:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[25]
                self.selected = 25
                self.the_selected = 26
        if self.gem_27_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[26]
                self.chart[26] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 27:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[26]
                self.selected = 26
                self.the_selected = 27
        if self.gem_28_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[27]
                self.chart[27] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 28:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[27]
                self.selected = 27
                self.the_selected = 28
        if self.gem_29_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[28]
                self.chart[28] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 29:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[28]
                self.selected = 28
                self.the_selected = 29
                
        if self.gem_30_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[29]
                self.chart[29] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 30:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[29]
                self.selected = 29
                self.the_selected = 30
        if self.gem_31_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[30]
                self.chart[30] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 30:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[30]
                self.selected = 30
                self.the_selected = 31
        if self.gem_32_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[31]
                self.chart[31] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 32:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[31]
                self.selected = 31
                self.the_selected = 32
        if self.gem_33_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[32]
                self.chart[32] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 33:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[32]
                self.selected = 32
                self.the_selected = 33
        if self.gem_34_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[33]
                self.chart[33] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 34:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[33]
                self.selected = 33
                self.the_selected = 34
        if self.gem_35_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[34]
                self.chart[34] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 35:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[34]
                self.selected = 34
                self.the_selected = 35
        if self.gem_36_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[35]
                self.chart[35] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 36:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[35]
                self.selected = 35
                self.the_selected = 36
        if self.gem_37_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[36]
                self.chart[36] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 37:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[36]
                self.selected = 36
                self.the_selected = 37
        if self.gem_38_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[37]
                self.chart[37] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 38:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[37]
                self.selected = 37
                self.the_selected = 38
        if self.gem_39_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[38]
                self.chart[38] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 39:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[38]
                self.selected = 38
                self.the_selected = 39
        if self.gem_40_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[39]
                self.chart[39] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 40:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[39]
                self.selected = 39
                self.the_selected = 40
        if self.gem_41_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[40]
                self.chart[40] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 41:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[40]
                self.selected = 40
                self.the_selected = 41
        if self.gem_42_button.frame.contains_point(touch.location) and self.game_over == False:
            if self.another_gem_pushed == True:
                self.chart[self.selected]=self.chart[42]
                self.chart[41] = self.placeholder
                self.another_gem_pushed = False
                if self.the_selected != 42:
                    self.moves= self.moves-1
                self.the_selected = 0
            else:
                self.another_gem_pushed = True
                self.placeholder = self.chart[41]
                self.selected = 41
                self.the_selected = 42

        
            
        # if menu button is pressed, go to menu scene
        if self.game_over == True:
            if self.menu_button.frame.contains_point(touch.location):
                self.dismiss_modal_scene()
        pass
        
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
