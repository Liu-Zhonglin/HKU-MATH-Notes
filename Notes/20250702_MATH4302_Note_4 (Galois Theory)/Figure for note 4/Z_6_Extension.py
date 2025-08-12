# Z_6_Extension
from math import *
from manim import *
TESTING = False
class Z_6_Extension(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        if TESTING == True: # Global Coordinate System
            X_Axis = Arrow([-config.frame_width/2, 0, 0],
                           [ config.frame_width/2, 0, 0],
                           stroke_width = 3,
                           color = BLACK,
                           buff = 0,
                           tip_length=0.2)
            Y_Axis = Arrow([0, -config.frame_height/2, 0],
                           [0,  config.frame_height/2, 0],
                           stroke_width = 3,
                           color = BLACK,
                           buff = 0,
                           tip_length=0.2)
            X_Label = MathTex(r"x", color = BLACK, font_size = 20).to_corner(RIGHT).shift([   0, -0.1, 0])
            Y_Label = MathTex(r"y", color = BLACK, font_size = 20).to_corner(   UP).shift([-0.1,    0, 0])
            self.add(X_Axis, Y_Axis, X_Label, Y_Label)
            for x in range(-7,8,1):
                if x != 0:
                    X_Isopleth = DashedLine([x, -config.frame_height/2, 0],
                                            [x,  config.frame_height/2, 0],
                                            stroke_width = 1.5,
                                            color = BLUE)
                    X_Intercept = Line([x, -0.1, 0], [x,  0.1, 0], stroke_width = 2, color = BLACK)
                    X_Intercept_Label = MathTex(str(x), color = BLACK, font_size = 20).move_to([x-0.1, -0.1, 0])
                    self.add(X_Isopleth, X_Intercept, X_Intercept_Label)
                else:
                    X_Intercept_Label = MathTex(  r"O", color = BLACK, font_size = 20).move_to([ -0.1, -0.1, 0])
                    self.add(X_Intercept_Label)
            for y in range(-4,5,1):
                if y != 0:
                    Y_Isopleth = DashedLine([-config.frame_width/2, y, 0],
                                            [ config.frame_width/2, y, 0],
                                            stroke_width = 1.5,
                                            color = BLUE)
                    Y_Intercept = Line([-0.1, y, 0], [ 0.1, y, 0], stroke_width = 2, color = BLACK)
                    Y_Intercept_Label = MathTex(str(y), color = BLACK, font_size = 20).move_to([ -0.1,y-0.1, 0])
                    self.add(Y_Isopleth, Y_Intercept, Y_Intercept_Label)
                else:
                    Y_Intercept_Label = MathTex(  r"O", color = BLACK, font_size = 20).move_to([ -0.1, -0.1, 0])
                    self.add(Y_Intercept_Label)
        Trivial_Group                = MathTex(r"\mathbb{Q}[\bar{\kappa}_0]",
                                               font_size = 30, color = PURPLE).move_to([ 0.0, 3.0, 0])
        Double_Cyclic_Group_024_135  = MathTex(r"\mathbb{Q}[\bar{\kappa}_0+\bar{\kappa}_2+\bar{\kappa}_4]",
                                               font_size = 30, color = PURPLE).move_to([-3.0, 0.0, 0])
        Triple_Cyclic_Group_03_14_25 = MathTex(r"\mathbb{Q}[\bar{\kappa}_0+\bar{\kappa}_3]",
                                               font_size = 30, color = PURPLE).move_to([ 3.0, 0.0, 0])
        Trivial_Group_In_Double_Cyclic_Group_024_135  = Line([ 0.0, 3.0-0.2, 0], [-3.0, 0.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Triple_Cyclic_Group_03_14_25 = Line([ 0.0, 3.0-0.2, 0], [ 3.0, 0.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_012345 = MathTex(r"\mathbb{Q}",
                                      font_size = 30, color = PURPLE).move_to([0.0, -3.0, 0])
        Double_Cyclic_Group_024_135_In_Cyclic_Group_012345  = Line([-3.0, 0.0-0.2, 0], [0.0, -3.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Triple_Cyclic_Group_03_14_25_In_Cyclic_Group_012345 = Line([ 3.0, 0.0-0.2, 0], [0.0, -3.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        self.add(Trivial_Group,
                 Double_Cyclic_Group_024_135,
                 Triple_Cyclic_Group_03_14_25,
                 Trivial_Group_In_Double_Cyclic_Group_024_135,
                 Trivial_Group_In_Triple_Cyclic_Group_03_14_25,
                 Cyclic_Group_012345,
                 Double_Cyclic_Group_024_135_In_Cyclic_Group_012345,
                 Triple_Cyclic_Group_03_14_25_In_Cyclic_Group_012345)
