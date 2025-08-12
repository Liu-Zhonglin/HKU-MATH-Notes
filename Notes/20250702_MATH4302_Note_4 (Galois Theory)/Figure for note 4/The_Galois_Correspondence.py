# The_Galois_Correspondence
from math import *
from manim import *
TESTING = False
class The_Galois_Correspondence(Scene):
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
        K                  = MathTex(r"K",
                                     font_size = 30, color = PURPLE).move_to([-3.0, -3.0, 0])
        G                  = MathTex(r"G",
                                     font_size = 30, color = PURPLE).move_to([ 3.0, -3.0, 0])
        L                  = MathTex(r"L",
                                     font_size = 30, color = PURPLE).move_to([-3.0,  0.0, 0])
        K_in_L             = Line([-3.0, -3.0+0.2, 0], [-3.0,  0.0-0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)  
        H                  = MathTex(r"H",
                                     font_size = 30, color = PURPLE).move_to([ 3.0,  0.0, 0])
        H_in_G             = Line([ 3.0,  0.0-0.2, 0], [ 3.0, -3.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        L_to_H             = Arrow([-3.0+0.2,  0.0+0.1, 0], [ 3.0-0.2,  0.0+0.1, 0], color = ORANGE, stroke_width =1.5, buff = 0.0, tip_length = 0.2)
        L_to_H_Label       = MathTex(r"H=\mathbf{Aut}(M/L)",
                                     font_size = 30, color = PURPLE).move_to([ 0.0,  0.5, 0])
        H_to_L             = Arrow([ 3.0-0.2,  0.0-0.1, 0], [-3.0+0.2,  0.0-0.1, 0], color = ORANGE, stroke_width =1.5, buff = 0.0, tip_length = 0.2)
        H_to_L_Label       = MathTex(r"L=M^H",
                                     font_size = 30, color = PURPLE).move_to([ 0.0, -0.5, 0])
        M                  = MathTex(r"M",
                                     font_size = 30, color = PURPLE).move_to([-3.0,  3.0, 0])
        L_in_M             = Line([-3.0,  0.0+0.2, 0], [-3.0,  3.0-0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group      = MathTex(r"\{e\}",
                                     font_size = 30, color = PURPLE).move_to([ 3.0,  3.0, 0])
        Trivial_Group_in_H = Line([ 3.0,  3.0-0.2, 0], [ 3.0,  0.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        self.add(K,
                 G,
                 L,
                 K_in_L,
                 H,
                 H_in_G,
                 L_to_H,
                 L_to_H_Label,
                 H_to_L,
                 H_to_L_Label,
                 M,
                 L_in_M,
                 Trivial_Group,
                 Trivial_Group_in_H)
