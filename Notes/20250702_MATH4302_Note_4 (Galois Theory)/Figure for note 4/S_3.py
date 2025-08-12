# S_3
from math import *
from manim import *
TESTING = False
class S_3(Scene):
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
        Trivial_Group    = MathTex(r"\{e\}",
                                   font_size = 30, color = PURPLE).move_to([ 0.0, 3.0, 0])
        Cyclic_Group_01  = MathTex(r"\langle(\bar{\kappa}_0,\bar{\kappa}_1)\rangle",
                                   font_size = 30, color = PURPLE).move_to([-3.0, 0.0, 0])
        Cyclic_Group_02  = MathTex(r"\langle(\bar{\kappa}_0,\bar{\kappa}_2)\rangle",
                                   font_size = 30, color = PURPLE).move_to([-1.0, 0.0, 0])
        Cyclic_Group_12  = MathTex(r"\langle(\bar{\kappa}_1,\bar{\kappa}_2)\rangle",
                                   font_size = 30, color = PURPLE).move_to([ 1.0, 0.0, 0])
        Cyclic_Group_012 = MathTex(r"\langle(\bar{\kappa}_0,\bar{\kappa}_1,\bar{\kappa}_2)\rangle",
                                   font_size = 30, color = PURPLE).move_to([ 3.0, 0.0, 0])
        Trivial_Group_In_Cyclic_Group_01  = Line([ 0.0, 3.0-0.2, 0], [-3.0, 0.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_02  = Line([ 0.0, 3.0-0.2, 0], [-1.0, 0.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_12  = Line([ 0.0, 3.0-0.2, 0], [ 1.0, 0.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_012 = Line([ 0.0, 3.0-0.2, 0], [ 3.0, 0.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Sym_012 = MathTex(r"\mathbf{Sym}(\bar{\kappa}_0,\bar{\kappa}_1,\bar{\kappa}_2)",
                          font_size = 30, color = PURPLE).move_to([0.0, -3.0, 0])
        Cyclic_Group_01_In_Sym_012  = Line([-3.0, 0.0-0.2, 0], [0.0, -3.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_02_In_Sym_012  = Line([-1.0, 0.0-0.2, 0], [0.0, -3.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_12_In_Sym_012  = Line([ 1.0, 0.0-0.2, 0], [0.0, -3.0+0.2, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_012_In_Sym_012 = Line([ 3.0, 0.0-0.2, 0], [0.0, -3.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        self.add(Trivial_Group,
                 Cyclic_Group_01,
                 Cyclic_Group_02,
                 Cyclic_Group_12,
                 Cyclic_Group_012,
                 Trivial_Group_In_Cyclic_Group_01,
                 Trivial_Group_In_Cyclic_Group_02,
                 Trivial_Group_In_Cyclic_Group_12,
                 Trivial_Group_In_Cyclic_Group_012,
                 Sym_012,
                 Cyclic_Group_01_In_Sym_012,
                 Cyclic_Group_02_In_Sym_012,
                 Cyclic_Group_12_In_Sym_012,
                 Cyclic_Group_012_In_Sym_012)
