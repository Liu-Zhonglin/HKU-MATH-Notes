# S_4
from math import *
from manim import *
TESTING = False
class S_4(Scene):
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
            X_Label = MathTex(r"x", color = BLACK, font_size = 15).to_corner(RIGHT).shift([   0, -0.1, 0])
            Y_Label = MathTex(r"y", color = BLACK, font_size = 15).to_corner(   UP).shift([-0.1,    0, 0])
            self.add(X_Axis, Y_Axis, X_Label, Y_Label)
            for x in range(-7,8,1):
                if x != 0:
                    X_Isopleth = DashedLine([x, -config.frame_height/2, 0],
                                            [x,  config.frame_height/2, 0],
                                            stroke_width = 1.5,
                                            color = BLUE)
                    X_Intercept = Line([x, -0.1, 0], [x,  0.1, 0], stroke_width = 2, color = BLACK)
                    X_Intercept_Label = MathTex(str(x), color = BLACK, font_size = 15).move_to([x-0.1, -0.1, 0])
                    self.add(X_Isopleth, X_Intercept, X_Intercept_Label)
                else:
                    X_Intercept_Label = MathTex(  r"O", color = BLACK, font_size = 15).move_to([ -0.1, -0.1, 0])
                    self.add(X_Intercept_Label)
            for y in range(-4,5,1):
                if y != 0:
                    Y_Isopleth = DashedLine([-config.frame_width/2, y, 0],
                                            [ config.frame_width/2, y, 0],
                                            stroke_width = 1.5,
                                            color = BLUE)
                    Y_Intercept = Line([-0.1, y, 0], [ 0.1, y, 0], stroke_width = 2, color = BLACK)
                    Y_Intercept_Label = MathTex(str(y), color = BLACK, font_size = 15).move_to([ -0.1,y-0.1, 0])
                    self.add(Y_Isopleth, Y_Intercept, Y_Intercept_Label)
                else:
                    Y_Intercept_Label = MathTex(  r"O", color = BLACK, font_size = 15).move_to([ -0.1, -0.1, 0])
                    self.add(Y_Intercept_Label)
        Trivial_Group             = MathTex(r"\{e\}",
                                            font_size = 15, color = PURPLE).move_to([ 0.00, 3.5, 0])
        Double_Cyclic_Group_01_23 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1)(\bar{\ell}_2,\bar{\ell}_3)\rangle",
                                            font_size = 15, color = PURPLE).move_to([-6.50, 2.5, 0])
        Double_Cyclic_Group_02_13 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_2)(\bar{\ell}_1,\bar{\ell}_3)\rangle",
                                            font_size = 15, color = PURPLE).move_to([-5.25, 2.5, 0])
        Double_Cyclic_Group_03_12 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_3)(\bar{\ell}_1,\bar{\ell}_2)\rangle",
                                            font_size = 15, color = PURPLE).move_to([-4.00, 2.5, 0])
        Cyclic_Group_01           = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1)\rangle",
                                            font_size = 15, color = PURPLE).move_to([-2.75, 2.5, 0])
        Cyclic_Group_02           = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_2)\rangle",
                                            font_size = 15, color = PURPLE).move_to([-2.00, 2.5, 0])
        Cyclic_Group_03           = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_3)\rangle",
                                            font_size = 15, color = PURPLE).move_to([-1.25, 2.5, 0])
        Cyclic_Group_12           = MathTex(r"\langle(\bar{\ell}_1,\bar{\ell}_2)\rangle",
                                            font_size = 15, color = PURPLE).move_to([-0.50, 2.5, 0])
        Cyclic_Group_13           = MathTex(r"\langle(\bar{\ell}_1,\bar{\ell}_3)\rangle",
                                            font_size = 15, color = PURPLE).move_to([ 0.25, 2.5, 0])
        Cyclic_Group_23           = MathTex(r"\langle(\bar{\ell}_2,\bar{\ell}_3)\rangle",
                                            font_size = 15, color = PURPLE).move_to([ 1.00, 2.5, 0])
        Cyclic_Group_012          = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_2)\rangle",
                                            font_size = 15, color = PURPLE).move_to([ 2.75, 1.5, 0])
        Cyclic_Group_013          = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_3)\rangle",
                                            font_size = 15, color = PURPLE).move_to([ 4.00, 1.5, 0])
        Cyclic_Group_023          = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_2,\bar{\ell}_3)\rangle",
                                            font_size = 15, color = PURPLE).move_to([ 5.25, 1.5, 0])
        Cyclic_Group_123          = MathTex(r"\langle(\bar{\ell}_1,\bar{\ell}_2,\bar{\ell}_3)\rangle",
                                            font_size = 15, color = PURPLE).move_to([ 6.50, 1.5, 0])
        Trivial_Group_In_Double_Cyclic_Group_01_23 = Line([0.00, 3.5-0.1, 0], [-6.50, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Double_Cyclic_Group_02_13 = Line([0.00, 3.5-0.1, 0], [-5.25, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Double_Cyclic_Group_03_12 = Line([0.00, 3.5-0.1, 0], [-4.00, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_01           = Line([0.00, 3.5-0.1, 0], [-2.75, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_02           = Line([0.00, 3.5-0.1, 0], [-2.00, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_03           = Line([0.00, 3.5-0.1, 0], [-1.25, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_12           = Line([0.00, 3.5-0.1, 0], [-0.50, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_13           = Line([0.00, 3.5-0.1, 0], [ 0.25, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_23           = Line([0.00, 3.5-0.1, 0], [ 1.00, 2.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_012          = Line([0.00, 3.5-0.1, 0], [ 2.75, 1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_013          = Line([0.00, 3.5-0.1, 0], [ 4.00, 1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_023          = Line([0.00, 3.5-0.1, 0], [ 5.25, 1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Trivial_Group_In_Cyclic_Group_123          = Line([0.00, 3.5-0.1, 0], [ 6.50, 1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_0 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1),(\bar{\ell}_2,\bar{\ell}_3)\rangle",
                                  font_size = 15, color = PURPLE).move_to([-6.50, 0.5, 0])
        Klein_4_Group_1 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_2),(\bar{\ell}_1,\bar{\ell}_3)\rangle",
                                  font_size = 15, color = PURPLE).move_to([-5.25, 0.5, 0])
        Klein_4_Group_2 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_3),(\bar{\ell}_1,\bar{\ell}_2)\rangle",
                                  font_size = 15, color = PURPLE).move_to([-4.00, 0.5, 0])
        Klein_4_Group_3 = MathTex(r"\begin{Bmatrix}"+
                                  r"    e,(\bar{\ell}_0,\bar{\ell}_1)(\bar{\ell}_2,\bar{\ell}_3)\\"+
                                  r"    (\bar{\ell}_0,\bar{\ell}_2)(\bar{\ell}_1,\bar{\ell}_3),(\bar{\ell}_0,\bar{\ell}_3)(\bar{\ell}_1,\bar{\ell}_2)\\"+
                                  r"\end{Bmatrix}",
                                  font_size = 15, color = PURPLE).move_to([ 0.00, 0.5, 0])
        Double_Cyclic_Group_01_23_In_Klein_4_Group_0 = Line([-6.50, 2.5-0.1, 0], [-6.50, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_01_23_In_Klein_4_Group_3 = Line([-6.50, 2.5-0.1, 0], [ 0.00, 0.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_02_13_In_Klein_4_Group_1 = Line([-5.25, 2.5-0.1, 0], [-5.25, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_02_13_In_Klein_4_Group_3 = Line([-5.25, 2.5-0.1, 0], [ 0.00, 0.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_03_12_In_Klein_4_Group_2 = Line([-4.00, 2.5-0.1, 0], [-4.00, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_03_12_In_Klein_4_Group_3 = Line([-4.00, 2.5-0.1, 0], [ 0.00, 0.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_01_In_Klein_4_Group_0           = Line([-2.75, 2.5-0.1, 0], [-6.50, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_02_In_Klein_4_Group_1           = Line([-2.00, 2.5-0.1, 0], [-5.25, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_03_In_Klein_4_Group_2           = Line([-1.25, 2.5-0.1, 0], [-4.00, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_12_In_Klein_4_Group_2           = Line([-0.50, 2.5-0.1, 0], [-4.00, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_13_In_Klein_4_Group_1           = Line([ 0.25, 2.5-0.1, 0], [-5.25, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_23_In_Klein_4_Group_0           = Line([ 1.00, 2.5-0.1, 0], [-6.50, 0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Sym_012 = MathTex(r"\mathbf{Sym}(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_2)",
                          font_size = 15, color = PURPLE).move_to([2.75, -1.5, 0])
        Sym_013 = MathTex(r"\mathbf{Sym}(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_3)",
                          font_size = 15, color = PURPLE).move_to([4.00, -1.5, 0])
        Sym_023 = MathTex(r"\mathbf{Sym}(\bar{\ell}_0,\bar{\ell}_2,\bar{\ell}_3)",
                          font_size = 15, color = PURPLE).move_to([5.25, -1.5, 0])
        Sym_123 = MathTex(r"\mathbf{Sym}(\bar{\ell}_1,\bar{\ell}_2,\bar{\ell}_3)",
                          font_size = 15, color = PURPLE).move_to([6.50, -1.5, 0])
        Cyclic_Group_01_In_Sym_012  = Line([-2.75, 2.5-0.1, 0], [2.75, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_01_In_Sym_013  = Line([-2.75, 2.5-0.1, 0], [4.00, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_02_In_Sym_012  = Line([-2.00, 2.5-0.1, 0], [2.75, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_02_In_Sym_023  = Line([-2.00, 2.5-0.1, 0], [5.25, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_03_In_Sym_013  = Line([-1.25, 2.5-0.1, 0], [4.00, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_03_In_Sym_023  = Line([-1.25, 2.5-0.1, 0], [5.25, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_12_In_Sym_012  = Line([-0.50, 2.5-0.1, 0], [2.75, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_12_In_Sym_123  = Line([-0.50, 2.5-0.1, 0], [6.50, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_13_In_Sym_013  = Line([ 0.25, 2.5-0.1, 0], [4.00, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_13_In_Sym_123  = Line([ 0.25, 2.5-0.1, 0], [6.50, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_23_In_Sym_023  = Line([ 1.00, 2.5-0.1, 0], [5.25, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_23_In_Sym_123  = Line([ 1.00, 2.5-0.1, 0], [6.50, -1.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_012_In_Sym_012 = Line([ 2.75, 1.5-0.1, 0], [2.75, -1.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_013_In_Sym_013 = Line([ 4.00, 1.5-0.1, 0], [4.00, -1.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_023_In_Sym_023 = Line([ 5.25, 1.5-0.1, 0], [5.25, -1.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_123_In_Sym_123 = Line([ 6.50, 1.5-0.1, 0], [6.50, -1.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_0213 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_2,\bar{\ell}_1,\bar{\ell}_3)\rangle",
                                    font_size = 15, color = PURPLE).move_to([-5.875, -0.5, 0])
        Cyclic_Group_0123 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_2,\bar{\ell}_3)\rangle",
                                    font_size = 15, color = PURPLE).move_to([-4.625, -0.5, 0])
        Cyclic_Group_0132 = MathTex(r"\langle(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_3,\bar{\ell}_2)\rangle",
                                    font_size = 15, color = PURPLE).move_to([-3.375, -0.5, 0])
        Double_Cyclic_Group_01_23_In_Cyclic_Group_0213 = Line([-6.50, 2.5-0.1, 0], [-5.875, -0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_02_13_In_Cyclic_Group_0123 = Line([-5.25, 2.5-0.1, 0], [-4.625, -0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Double_Cyclic_Group_03_12_In_Cyclic_Group_0132 = Line([-4.00, 2.5-0.1, 0], [-3.375, -0.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Dihedral_Group_0213 = MathTex(r"\mathbf{Dih}"+
                                      r"\begin{pmatrix}"+
                                      r"    \bar{\ell}_3 & \bar{\ell}_1\\"+
                                      r"    \bar{\ell}_0 & \bar{\ell}_2\\"+
                                      r"\end{pmatrix}",
                                      font_size = 15, color = PURPLE).move_to([-5.875, -2.5, 0])
        Dihedral_Group_0123 = MathTex(r"\mathbf{Dih}"+
                                      r"\begin{pmatrix}"+
                                      r"    \bar{\ell}_3 & \bar{\ell}_2\\"+
                                      r"    \bar{\ell}_0 & \bar{\ell}_1\\"+
                                      r"\end{pmatrix}",
                                      font_size = 15, color = PURPLE).move_to([-4.625, -2.5, 0])
        Dihedral_Group_0132 = MathTex(r"\mathbf{Dih}"+
                                      r"\begin{pmatrix}"+
                                      r"    \bar{\ell}_2 & \bar{\ell}_3\\"+
                                      r"    \bar{\ell}_0 & \bar{\ell}_1\\"+
                                      r"\end{pmatrix}",
                                      font_size = 15, color = PURPLE).move_to([-3.375, -2.5, 0])
        Alt_0123            = MathTex(r"\mathbf{Alt}(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_2,\bar{\ell}_3)",
                                      font_size = 15, color = PURPLE).move_to([ 0.000, -2.5, 0])
        Cyclic_Group_012_In_Alt_0123             = Line([ 2.75,  1.5-0.1, 0], [ 0.0, -2.5+0.1, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_013_In_Alt_0123             = Line([ 4.00,  1.5-0.1, 0], [ 0.0, -2.5+0.1, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_023_In_Alt_0123             = Line([ 5.25,  1.5-0.1, 0], [ 0.0, -2.5+0.1, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_123_In_Alt_0123             = Line([ 6.50,  1.5-0.1, 0], [ 0.0, -2.5+0.1, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_0213_In_Dihedral_Group_0213 = Line([-5.875, -0.5-0.1, 0], [-5.875, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_0123_In_Dihedral_Group_0123 = Line([-4.625, -0.5-0.1, 0], [-4.625, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Cyclic_Group_0132_In_Dihedral_Group_0132 = Line([-3.375, -0.5-0.1, 0], [-3.375, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_0_In_Dihedral_Group_0213   = Line([-6.50,  0.5-0.1, 0], [-5.875, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_1_In_Dihedral_Group_0123   = Line([-5.25,  0.5-0.1, 0], [-4.625, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_2_In_Dihedral_Group_0132   = Line([-4.00,  0.5-0.1, 0], [-3.375, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_3_In_Dihedral_Group_0213   = Line([ 0.00,  0.5-0.2, 0], [-5.875, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_3_In_Dihedral_Group_0123   = Line([ 0.00,  0.5-0.2, 0], [-4.625, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_3_In_Dihedral_Group_0132   = Line([ 0.00,  0.5-0.2, 0], [-3.375, -2.5+0.2, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Klein_4_Group_3_In_Alt_0123              = Line([ 0.00,  0.5-0.2, 0], [ 0.000, -2.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Sym_0123 = MathTex(r"\mathbf{Sym}(\bar{\ell}_0,\bar{\ell}_1,\bar{\ell}_2,\bar{\ell}_3)", font_size = 15, color = PURPLE).move_to([0.0, -3.5, 0.0])
        Dihedral_Group_0213_In_Sym_0123          = Line([-5.875, -2.5-0.2, 0], [ 0.0, -3.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Dihedral_Group_0123_In_Sym_0123          = Line([-4.625, -2.5-0.2, 0], [ 0.0, -3.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Dihedral_Group_0132_In_Sym_0123          = Line([-3.375, -2.5-0.2, 0], [ 0.0, -3.5+0.1, 0], color =   RED, stroke_width = 1.5, buff = 0.0)
        Alt_0123_In_Sym_0123                     = Line([ 0.000, -2.5-0.1, 0], [ 0.0, -3.5+0.1, 0], color = BLACK, stroke_width = 1.5, buff = 0.0)
        Sym_012_In_Sym_0123                      = Line([ 2.75,  -1.5-0.1, 0], [ 0.0, -3.5+0.1, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Sym_013_In_Sym_0123                      = Line([ 4.00,  -1.5-0.1, 0], [ 0.0, -3.5+0.1, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Sym_023_In_Sym_0123                      = Line([ 5.25,  -1.5-0.1, 0], [ 0.0, -3.5+0.1, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        Sym_123_In_Sym_0123                      = Line([ 6.50,  -1.5-0.1, 0], [ 0.0, -3.5+0.1, 0], color =  BLUE, stroke_width = 1.5, buff = 0.0)
        self.add(Trivial_Group,
                 Double_Cyclic_Group_01_23,
                 Double_Cyclic_Group_02_13,
                 Double_Cyclic_Group_03_12,
                 Cyclic_Group_01,
                 Cyclic_Group_02,
                 Cyclic_Group_03,
                 Cyclic_Group_12,
                 Cyclic_Group_13,
                 Cyclic_Group_23,
                 Cyclic_Group_012,
                 Cyclic_Group_013,
                 Cyclic_Group_023,
                 Cyclic_Group_123,
                 Trivial_Group_In_Double_Cyclic_Group_01_23,
                 Trivial_Group_In_Double_Cyclic_Group_02_13,
                 Trivial_Group_In_Double_Cyclic_Group_03_12,
                 Trivial_Group_In_Cyclic_Group_01,
                 Trivial_Group_In_Cyclic_Group_02,
                 Trivial_Group_In_Cyclic_Group_03,
                 Trivial_Group_In_Cyclic_Group_12,
                 Trivial_Group_In_Cyclic_Group_13,
                 Trivial_Group_In_Cyclic_Group_23,
                 Trivial_Group_In_Cyclic_Group_012,
                 Trivial_Group_In_Cyclic_Group_013,
                 Trivial_Group_In_Cyclic_Group_023,
                 Trivial_Group_In_Cyclic_Group_123,
                 Klein_4_Group_0,
                 Klein_4_Group_1,
                 Klein_4_Group_2,
                 Klein_4_Group_3,
                 Double_Cyclic_Group_01_23_In_Klein_4_Group_0,
                 Double_Cyclic_Group_01_23_In_Klein_4_Group_3,
                 Double_Cyclic_Group_02_13_In_Klein_4_Group_1,
                 Double_Cyclic_Group_02_13_In_Klein_4_Group_3,
                 Double_Cyclic_Group_03_12_In_Klein_4_Group_2,
                 Double_Cyclic_Group_03_12_In_Klein_4_Group_3,
                 Cyclic_Group_01_In_Klein_4_Group_0,
                 Cyclic_Group_02_In_Klein_4_Group_1,
                 Cyclic_Group_03_In_Klein_4_Group_2,
                 Cyclic_Group_12_In_Klein_4_Group_2,
                 Cyclic_Group_13_In_Klein_4_Group_1,
                 Cyclic_Group_23_In_Klein_4_Group_0,
                 Sym_012,
                 Sym_013,
                 Sym_023,
                 Sym_123,
                 Cyclic_Group_01_In_Sym_012,
                 Cyclic_Group_01_In_Sym_013,
                 Cyclic_Group_02_In_Sym_012,
                 Cyclic_Group_02_In_Sym_023,
                 Cyclic_Group_03_In_Sym_013,
                 Cyclic_Group_03_In_Sym_023,
                 Cyclic_Group_12_In_Sym_012,
                 Cyclic_Group_12_In_Sym_123,
                 Cyclic_Group_13_In_Sym_013,
                 Cyclic_Group_13_In_Sym_123,
                 Cyclic_Group_23_In_Sym_023,
                 Cyclic_Group_23_In_Sym_123,
                 Cyclic_Group_012_In_Sym_012,
                 Cyclic_Group_013_In_Sym_013,
                 Cyclic_Group_023_In_Sym_023,
                 Cyclic_Group_123_In_Sym_123,
                 Cyclic_Group_0123,
                 Cyclic_Group_0132,
                 Cyclic_Group_0213,
                 Double_Cyclic_Group_01_23_In_Cyclic_Group_0213,
                 Double_Cyclic_Group_02_13_In_Cyclic_Group_0123,
                 Double_Cyclic_Group_03_12_In_Cyclic_Group_0132,
                 Dihedral_Group_0123,
                 Dihedral_Group_0132,
                 Dihedral_Group_0213,
                 Alt_0123,
                 Cyclic_Group_012_In_Alt_0123,
                 Cyclic_Group_013_In_Alt_0123,
                 Cyclic_Group_023_In_Alt_0123,
                 Cyclic_Group_123_In_Alt_0123,
                 Cyclic_Group_0123_In_Dihedral_Group_0123,
                 Cyclic_Group_0132_In_Dihedral_Group_0132,
                 Cyclic_Group_0213_In_Dihedral_Group_0213,
                 Klein_4_Group_0_In_Dihedral_Group_0213,
                 Klein_4_Group_1_In_Dihedral_Group_0123,
                 Klein_4_Group_2_In_Dihedral_Group_0132,
                 Klein_4_Group_3_In_Dihedral_Group_0123,
                 Klein_4_Group_3_In_Dihedral_Group_0132,
                 Klein_4_Group_3_In_Dihedral_Group_0213,
                 Klein_4_Group_3_In_Alt_0123,
                 Sym_0123,
                 Dihedral_Group_0123_In_Sym_0123,
                 Dihedral_Group_0132_In_Sym_0123,
                 Dihedral_Group_0213_In_Sym_0123,
                 Alt_0123_In_Sym_0123,
                 Sym_012_In_Sym_0123,
                 Sym_013_In_Sym_0123,
                 Sym_023_In_Sym_0123,
                 Sym_123_In_Sym_0123)
