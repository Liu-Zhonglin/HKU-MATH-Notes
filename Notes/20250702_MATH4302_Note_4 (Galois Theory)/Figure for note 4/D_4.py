# D_4
from math import *
from manim import *
TESTING = False
class D_4(Scene):
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
            X_Label = MathTex(r"x", color = BLACK, font_size = 30).to_corner(RIGHT).shift([   0, -0.1, 0])
            Y_Label = MathTex(r"y", color = BLACK, font_size = 30).to_corner(   UP).shift([-0.1,    0, 0])
            self.add(X_Axis, Y_Axis, X_Label, Y_Label)
            for x in range(-7,8,1):
                if x != 0:
                    X_Isopleth = DashedLine([x, -config.frame_height/2, 0],
                                            [x,  config.frame_height/2, 0],
                                            stroke_width = 1.5,
                                            color = BLUE)
                    X_Intercept = Line([x, -0.1, 0], [x,  0.1, 0], stroke_width = 2, color = BLACK)
                    X_Intercept_Label = MathTex(str(x), color = BLACK, font_size = 30).move_to([x-0.1, -0.1, 0])
                    self.add(X_Isopleth, X_Intercept, X_Intercept_Label)
                else:
                    X_Intercept_Label = MathTex(  r"O", color = BLACK, font_size = 30).move_to([ -0.1, -0.1, 0])
                    self.add(X_Intercept_Label)
            for y in range(-4,5,1):
                if y != 0:
                    Y_Isopleth = DashedLine([-config.frame_width/2, y, 0],
                                            [ config.frame_width/2, y, 0],
                                            stroke_width = 1.5,
                                            color = BLUE)
                    Y_Intercept = Line([-0.1, y, 0], [ 0.1, y, 0], stroke_width = 2, color = BLACK)
                    Y_Intercept_Label = MathTex(str(y), color = BLACK, font_size = 30).move_to([ -0.1,y-0.1, 0])
                    self.add(Y_Isopleth, Y_Intercept, Y_Intercept_Label)
                else:
                    Y_Intercept_Label = MathTex(  r"O", color = BLACK, font_size = 30).move_to([ -0.1, -0.1, 0])
                    self.add(Y_Intercept_Label)
        Trivial_Group             = MathTex(r"\{e\}",
                                            font_size = 30, color = PURPLE).move_to([ 0.0, 3.0, 0])
        Cyclic_Group_02           = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_2)\rangle",
                                            font_size = 30, color = PURPLE).move_to([-4.0, 1.0, 0])
        Cyclic_Group_13           = MathTex(r"\langle(\bar{\ell}_1,\bar{\ell}_3)\rangle",
                                            font_size = 30, color = PURPLE).move_to([-2.0, 1.0, 0])
        Double_Cyclic_Group_02_13 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_2)(\bar{\ell}_1,\bar{\ell}_3)\rangle",
                                            font_size = 30, color = PURPLE).move_to([ 0.0, 1.0, 0])
        Double_Cyclic_Group_01_23 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1)(\bar{\ell}_2,\bar{\ell}_3)\rangle",
                                            font_size = 30, color = PURPLE).move_to([ 2.0, 1.0, 0])
        Double_Cyclic_Group_03_12 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_3)(\bar{\ell}_1,\bar{\ell}_2)\rangle",
                                            font_size = 30, color = PURPLE).move_to([ 4.0, 1.0, 0])
        Trivial_Group_In_Cyclic_Group_02           = Line([ 0.0, 3.0-0.2, 0], [-4.0, 1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_13           = Line([ 0.0, 3.0-0.2, 0], [-2.0, 1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Double_Cyclic_Group_02_13 = Line([ 0.0, 3.0-0.2, 0], [ 0.0, 1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Double_Cyclic_Group_01_23 = Line([ 0.0, 3.0-0.2, 0], [ 2.0, 1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Double_Cyclic_Group_03_12 = Line([ 0.0, 3.0-0.2, 0], [ 4.0, 1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)        
        Klein_4_Group_0   = MathTex(r"\begin{Bmatrix}"+
                                    r"    e,(\bar{\ell}_0,\bar{\ell}_2)(\bar{\ell}_1,\bar{\ell}_3)\\"+
                                    r"    (\bar{\ell}_0,\bar{\ell}_2),(\bar{\ell}_1,\bar{\ell}_3)\\"+
                                    r"\end{Bmatrix}",
                                    font_size = 30, color = PURPLE).move_to([-4.0, -1.0, 0])
        Cyclic_Group_0123 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_2,\bar{\ell}_3)\rangle",
                                    font_size = 30, color = PURPLE).move_to([ 0.0, -1.0, 0])
        Klein_4_Group_1   = MathTex(r"\begin{Bmatrix}"+
                                    r"    e,(\bar{\ell}_0,\bar{\ell}_2)(\bar{\ell}_1,\bar{\ell}_3)\\"+
                                    r"    (\bar{\ell}_0,\bar{\ell}_1)(\bar{\ell}_2,\bar{\ell}_3),(\bar{\ell}_0,\bar{\ell}_3)(\bar{\ell}_1,\bar{\ell}_2)\\"+
                                    r"\end{Bmatrix}",
                                    font_size = 30, color = PURPLE).move_to([ 4.0, -1.0, 0])
        Cyclic_Group_02_In_Klein_4_Group_0             = Line([-4.0, 1.0-0.2, 0], [-4.0, -1.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_13_In_Klein_4_Group_0             = Line([-2.0, 1.0-0.2, 0], [-4.0, -1.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_02_13_In_Klein_4_Group_0   = Line([ 0.0, 1.0-0.2, 0], [-4.0, -1.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_02_13_In_Cyclic_Group_0123 = Line([ 0.0, 1.0-0.2, 0], [ 0.0, -1.0+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_02_13_In_Klein_4_Group_1   = Line([ 0.0, 1.0-0.2, 0], [ 4.0, -1.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_01_23_In_Klein_4_Group_1   = Line([ 2.0, 1.0-0.2, 0], [ 4.0, -1.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_03_12_In_Klein_4_Group_1   = Line([ 4.0, 1.0-0.2, 0], [ 4.0, -1.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Dihedral_Group_0123 = MathTex(r"\mathbf{Dih}"+
                                      r"\begin{pmatrix}"+
                                      r"    \bar{\ell}_3 & \bar{\ell}_2\\"+
                                      r"    \bar{\ell}_0 & \bar{\ell}_1\\"+
                                      r"\end{pmatrix}",
                                      font_size = 30, color = PURPLE).move_to([ 0.0, -3.0, 0])
        Klein_4_Group_0_In_Dihedral_Group_0123   = Line([-4.0, -1.0-0.4, 0], [0.0, -3.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_0123_In_Dihedral_Group_0123 = Line([ 0.0, -1.0-0.2, 0], [0.0, -3.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_1_In_Dihedral_Group_0123   = Line([ 4.0, -1.0-0.4, 0], [0.0, -3.0+0.4, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        self.add(Trivial_Group,
                 Cyclic_Group_02,
                 Cyclic_Group_13,
                 Double_Cyclic_Group_02_13,
                 Double_Cyclic_Group_01_23,
                 Double_Cyclic_Group_03_12,
                 Klein_4_Group_0,
                 Cyclic_Group_0123,
                 Klein_4_Group_1,
                 Dihedral_Group_0123,
                 Trivial_Group_In_Cyclic_Group_02,
                 Trivial_Group_In_Cyclic_Group_13,
                 Trivial_Group_In_Double_Cyclic_Group_02_13,
                 Trivial_Group_In_Double_Cyclic_Group_01_23,
                 Trivial_Group_In_Double_Cyclic_Group_03_12,
                 Cyclic_Group_02_In_Klein_4_Group_0,
                 Cyclic_Group_13_In_Klein_4_Group_0,
                 Double_Cyclic_Group_02_13_In_Klein_4_Group_0,
                 Double_Cyclic_Group_02_13_In_Cyclic_Group_0123,
                 Double_Cyclic_Group_02_13_In_Klein_4_Group_1,
                 Double_Cyclic_Group_01_23_In_Klein_4_Group_1,
                 Double_Cyclic_Group_03_12_In_Klein_4_Group_1,
                 Klein_4_Group_0_In_Dihedral_Group_0123,
                 Cyclic_Group_0123_In_Dihedral_Group_0123,
                 Klein_4_Group_1_In_Dihedral_Group_0123)
