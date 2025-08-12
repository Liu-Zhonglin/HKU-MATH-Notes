# A_4_Extension
from math import *
from manim import *
TESTING = False
class A_4_Extension(Scene):
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
        Trivial_Group             = MathTex(r"\mathbb{Q}[\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_2,\bar{\ell}_3]",
                                            font_size = 30, color = PURPLE).move_to([ 0.0, 3.0, 0])
        Double_Cyclic_Group_01_23 = MathTex(r"\mathbb{Q}[\bar{\kappa}_2]",
                                            font_size = 30, color = PURPLE).move_to([-6.0, 1.0, 0])
        Double_Cyclic_Group_02_13 = MathTex(r"\mathbb{Q}[\bar{\kappa}_1]",
                                            font_size = 30, color = PURPLE).move_to([-4.0, 1.0, 0])
        Double_Cyclic_Group_03_12 = MathTex(r"\mathbb{Q}[\bar{\kappa}_0]",
                                            font_size = 30, color = PURPLE).move_to([-2.0, 1.0, 0])
        Cyclic_Group_012          = MathTex(r"\mathbb{Q}[\bar{\ell}_3]",
                                            font_size = 30, color = PURPLE).move_to([ 0.0, 0.0, 0])
        Cyclic_Group_013          = MathTex(r"\mathbb{Q}[\bar{\ell}_2]",
                                            font_size = 30, color = PURPLE).move_to([ 2.0, 0.0, 0])
        Cyclic_Group_023          = MathTex(r"\mathbb{Q}[\bar{\ell}_1]",
                                            font_size = 30, color = PURPLE).move_to([ 4.0, 0.0, 0])
        Cyclic_Group_123          = MathTex(r"\mathbb{Q}[\bar{\ell}_0]",
                                            font_size = 30, color = PURPLE).move_to([ 6.0, 0.0, 0])
        Trivial_Group_In_Double_Cyclic_Group_01_23 = Line([ 0.0, 3.0-0.2, 0], [-6.0, 1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Double_Cyclic_Group_02_13 = Line([ 0.0, 3.0-0.2, 0], [-4.0, 1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Double_Cyclic_Group_03_12 = Line([ 0.0, 3.0-0.2, 0], [-2.0, 1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_012          = Line([ 0.0, 3.0-0.2, 0], [ 0.0, 0.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_013          = Line([ 0.0, 3.0-0.2, 0], [ 2.0, 0.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_023          = Line([ 0.0, 3.0-0.2, 0], [ 4.0, 0.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_123          = Line([ 0.0, 3.0-0.2, 0], [ 6.0, 0.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_3 = MathTex(r"\mathbb{Q}[\bar{\ell}_0^2]",
                                  font_size = 30, color = PURPLE).move_to([-4.0, -1.0, 0])
        Double_Cyclic_Group_01_23_In_Klein_4_Group_3 = Line([-6.0, 1.0-0.2, 0], [-4.0, -1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_02_13_In_Klein_4_Group_3 = Line([-4.0, 1.0-0.2, 0], [-4.0, -1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_03_12_In_Klein_4_Group_3 = Line([-2.0, 1.0-0.2, 0], [-4.0, -1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Alt_0123 = MathTex(r"\mathbb{Q}",
                           font_size = 30, color = PURPLE).move_to([ 0.0, -3.0, 0])
        Cyclic_Group_012_In_Alt_0123 = Line([ 0.0,  0.0-0.2, 0], [ 0.0, -3.0+0.2, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_013_In_Alt_0123 = Line([ 2.0,  0.0-0.2, 0], [ 0.0, -3.0+0.2, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_023_In_Alt_0123 = Line([ 4.0,  0.0-0.2, 0], [ 0.0, -3.0+0.2, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_123_In_Alt_0123 = Line([ 6.0,  0.0-0.2, 0], [ 0.0, -3.0+0.2, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_3_In_Alt_0123  = Line([-4.0, -1.0-0.2, 0], [ 0.0, -3.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        self.add(Trivial_Group,
                 Double_Cyclic_Group_01_23,
                 Double_Cyclic_Group_02_13,
                 Double_Cyclic_Group_03_12,
                 Cyclic_Group_012,
                 Cyclic_Group_013,
                 Cyclic_Group_023,
                 Cyclic_Group_123,
                 Trivial_Group_In_Double_Cyclic_Group_01_23,
                 Trivial_Group_In_Double_Cyclic_Group_02_13,
                 Trivial_Group_In_Double_Cyclic_Group_03_12,
                 Trivial_Group_In_Cyclic_Group_012,
                 Trivial_Group_In_Cyclic_Group_013,
                 Trivial_Group_In_Cyclic_Group_023,
                 Trivial_Group_In_Cyclic_Group_123,
                 Klein_4_Group_3,
                 Double_Cyclic_Group_01_23_In_Klein_4_Group_3,
                 Double_Cyclic_Group_02_13_In_Klein_4_Group_3,
                 Double_Cyclic_Group_03_12_In_Klein_4_Group_3,
                 Alt_0123,
                 Cyclic_Group_012_In_Alt_0123,
                 Cyclic_Group_013_In_Alt_0123,
                 Cyclic_Group_023_In_Alt_0123,
                 Cyclic_Group_123_In_Alt_0123,
                 Klein_4_Group_3_In_Alt_0123)
