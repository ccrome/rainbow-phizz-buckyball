from math import sqrt
from numpy  import *
import subprocess
import functools

torus_5_10 = {
    "points" :
        [
        [6.309064, 0.000000, 0.000000],
        [6.205568, 1.138073, 0.000000],
        [5.898476, 2.238808, 0.000000],
        [5.397864, 3.266091, 0.000000],
        [4.720155, 4.186218, 0.000000],
        [3.887585, 4.969001, 0.000000],
        [2.927469, 5.588758, 0.000000],
        [1.871306, 6.025155, 0.000000],
        [0.753749, 6.263876, 0.000000],
        [-0.388538, 6.297088, 0.000000],
        [-1.518078, 6.123702, 0.000000],
        [-2.597811, 5.749405, 0.000000],
        [-3.592314, 5.186479, 0.000000],
        [-4.468958, 4.453392, 0.000000],
        [-5.198982, 3.574195, 0.000000],
        [-5.758435, 2.577733, 0.000000],
        [-6.128962, 1.496700, 0.000000],
        [-6.298406, 0.366563, 0.000000],
        [-6.261208, -0.775601, 0.000000],
        [-6.018589, -1.892319, 0.000000],
        [-5.578509, -2.946952, 0.000000],
        [-4.955405, -3.904900, 0.000000],
        [-4.169722, -4.734734, 0.000000],
        [-3.247236, -5.409228, 0.000000],
        [-2.218213, -5.906252, 0.000000],
        [-1.116413, -6.209501, 0.000000],
        [0.022015, -6.309025, 0.000000],
        [1.159720, -6.201559, 0.000000],
        [2.259376, -5.890628, 0.000000],
        [3.284906, -5.386435, 0.000000],
        [4.202662, -4.705519, 0.000000],
        [4.982535, -3.870223, 0.000000],
        [5.598939, -2.907950, 0.000000],
        [6.031648, -1.850271, 0.000000],
        [6.266468, -0.731887, 0.000000],
        [5.759197, 0.000000, 0.756827],
        [5.664721, 1.038884, 0.756827],
        [5.384394, 2.043685, 0.756827],
        [4.927413, 2.981434, 0.756827],
        [4.308770, 3.821368, 0.756827],
        [3.548762, 4.535927, 0.756827],
        [2.672325, 5.101669, 0.756827],
        [1.708212, 5.500033, 0.756827],
        [0.688056, 5.717948, 0.756827],
        [-0.354675, 5.748265, 0.756827],
        [-1.385769, 5.589990, 0.756827],
        [-2.371399, 5.248316, 0.756827],
        [-3.279226, 4.734451, 0.756827],
        [-4.079466, 4.065256, 0.756827],
        [-4.745865, 3.262686, 0.756827],
        [-5.256558, 2.353071, 0.756827],
        [-5.594792, 1.366255, 0.756827],
        [-5.749468, 0.334615, 0.756827],
        [-5.715512, -0.708004, 0.756827],
        [-5.494039, -1.727394, 0.756827],
        [-5.092313, -2.690110, 0.756827],
        [-4.523516, -3.564568, 0.756827],
        [-3.806309, -4.322078, 0.756827],
        [-2.964223, -4.937786, 0.756827],
        [-2.024884, -5.391493, 0.756827],
        [-1.019112, -5.668312, 0.756827],
        [0.020096, -5.759162, 0.756827],
        [1.058644, -5.661062, 0.756827],
        [2.062460, -5.377230, 0.756827],
        [2.998610, -4.916980, 0.756827],
        [3.836379, -4.295410, 0.756827],
        [4.548282, -3.532913, 0.756827],
        [5.110963, -2.654507, 0.756827],
        [5.505960, -1.689010, 0.756827],
        [5.720314, -0.668100, 0.756827],
        [4.869494, 0.000000, 0.467745],
        [4.789613, 0.878394, 0.467745],
        [4.552592, 1.727968, 0.467745],
        [4.166207, 2.520851, 0.467745],
        [3.643134, 3.231028, 0.467745],
        [3.000536, 3.835199, 0.467745],
        [2.259494, 4.313543, 0.467745],
        [1.444321, 4.650366, 0.467745],
        [0.581762, 4.834617, 0.467745],
        [-0.299883, 4.860251, 0.467745],
        [-1.171690, 4.726427, 0.467745],
        [-2.005056, 4.437535, 0.467745],
        [-2.772638, 4.003055, 0.467745],
        [-3.449254, 3.437239, 0.467745],
        [-4.012705, 2.758653, 0.467745],
        [-4.444505, 1.989559, 0.467745],
        [-4.730486, 1.155191, 0.467745],
        [-4.861268, 0.282922, 0.467745],
        [-4.832558, -0.598628, 0.467745],
        [-4.645298, -1.460539, 0.467745],
        [-4.305633, -2.274532, 0.467745],
        [-3.824706, -3.013900, 0.467745],
        [-3.218296, -3.654386, 0.467745],
        [-2.506298, -4.174978, 0.467745],
        [-1.712072, -4.558594, 0.467745],
        [-0.861676, -4.792649, 0.467745],
        [0.016991, -4.869464, 0.467745],
        [0.895101, -4.786519, 0.467745],
        [1.743843, -4.546535, 0.467745],
        [2.535373, -4.157385, 0.467745],
        [3.243720, -3.631838, 0.467745],
        [3.845646, -2.987135, 0.467745],
        [4.321401, -2.244429, 0.467745],
        [4.655378, -1.428086, 0.467745],
        [4.836618, -0.564889, 0.467745],
        [4.869494, 0.000000, -0.467745],
        [4.789613, 0.878394, -0.467745],
        [4.552592, 1.727968, -0.467745],
        [4.166207, 2.520851, -0.467745],
        [3.643134, 3.231028, -0.467745],
        [3.000536, 3.835199, -0.467745],
        [2.259494, 4.313543, -0.467745],
        [1.444321, 4.650366, -0.467745],
        [0.581762, 4.834617, -0.467745],
        [-0.299883, 4.860251, -0.467745],
        [-1.171690, 4.726427, -0.467745],
        [-2.005056, 4.437535, -0.467745],
        [-2.772638, 4.003055, -0.467745],
        [-3.449254, 3.437239, -0.467745],
        [-4.012705, 2.758653, -0.467745],
        [-4.444505, 1.989559, -0.467745],
        [-4.730486, 1.155191, -0.467745],
        [-4.861268, 0.282922, -0.467745],
        [-4.832558, -0.598628, -0.467745],
        [-4.645298, -1.460539, -0.467745],
        [-4.305633, -2.274532, -0.467745],
        [-3.824706, -3.013900, -0.467745],
        [-3.218296, -3.654386, -0.467745],
        [-2.506298, -4.174978, -0.467745],
        [-1.712072, -4.558594, -0.467745],
        [-0.861676, -4.792649, -0.467745],
        [0.016991, -4.869464, -0.467745],
        [0.895101, -4.786519, -0.467745],
        [1.743843, -4.546535, -0.467745],
        [2.535373, -4.157385, -0.467745],
        [3.243720, -3.631838, -0.467745],
        [3.845646, -2.987135, -0.467745],
        [4.321401, -2.244429, -0.467745],
        [4.655378, -1.428086, -0.467745],
        [4.836618, -0.564889, -0.467745],
        [5.759197, 0.000000, -0.756827],
        [5.664721, 1.038884, -0.756827],
        [5.384394, 2.043685, -0.756827],
        [4.927413, 2.981434, -0.756827],
        [4.308770, 3.821368, -0.756827],
        [3.548762, 4.535927, -0.756827],
        [2.672325, 5.101669, -0.756827],
        [1.708212, 5.500033, -0.756827],
        [0.688056, 5.717948, -0.756827],
        [-0.354675, 5.748265, -0.756827],
        [-1.385769, 5.589990, -0.756827],
        [-2.371399, 5.248316, -0.756827],
        [-3.279226, 4.734451, -0.756827],
        [-4.079466, 4.065256, -0.756827],
        [-4.745865, 3.262686, -0.756827],
        [-5.256558, 2.353071, -0.756827],
        [-5.594792, 1.366255, -0.756827],
        [-5.749468, 0.334615, -0.756827],
        [-5.715512, -0.708004, -0.756827],
        [-5.494039, -1.727394, -0.756827],
        [-5.092313, -2.690110, -0.756827],
        [-4.523516, -3.564568, -0.756827],
        [-3.806309, -4.322078, -0.756827],
        [-2.964223, -4.937786, -0.756827],
        [-2.024884, -5.391493, -0.756827],
        [-1.019112, -5.668312, -0.756827],
        [0.020096, -5.759162, -0.756827],
        [1.058644, -5.661062, -0.756827],
        [2.062460, -5.377230, -0.756827],
        [2.998610, -4.916980, -0.756827],
        [3.836379, -4.295410, -0.756827],
        [4.548282, -3.532913, -0.756827],
        [5.110963, -2.654507, -0.756827],
        [5.505960, -1.689010, -0.756827],
        [5.720314, -0.668100, -0.756827],
        ]
    }

icosohedron = {
    "points" :
        [
         [0.0       ,  0.0     ,   2.0],
         [1.788854  ,  0.000000,   0.894427],
         [0.552786  ,  1.701302,   0.894427],
         [-1.447214 ,  1.051462,   0.894427],
         [-1.447214 , -1.051462,   0.894427],
         [0.552786  , -1.701302,   0.894427],
         [1.447214  ,  1.051462,  -0.894427],
         [-0.552786 ,  1.701302,  -0.894427],
         [-1.788854 ,  0.000000,  -0.894427],
         [-0.552786 , -1.701302,  -0.894427],
         [1.447214  , -1.051462,  -0.894427],
         [0.0       ,  0.0     ,  -2.0],
         ],
    }

dodecahedron = {
    "points" :
        [
        [ 0.469,     0.469,     0.469],
        [ 0.290,     0.000,     0.759],
        [-0.759,    -0.290,     0.000],
        [ 0.759,     0.290,     0.000],
        [-0.469,     0.469,    -0.469],
        [ 0.000,    -0.759,    -0.290],
        [-0.759,     0.290,     0.000],
        [ 0.469,    -0.469,     0.469],
        [-0.469,     0.469,     0.469],
        [-0.469,    -0.469,     0.469],
        [ 0.469,    -0.469,    -0.469],
        [ 0.290,     0.000,    -0.759],
        [-0.469,    -0.469,    -0.469],
        [ 0.000,    -0.759,     0.290],
        [ 0.000,     0.759,    -0.290],
        [-0.290,     0.000,     0.759],
        [ 0.759,    -0.290,     0.000],
        [-0.290,     0.000,    -0.759],
        [ 0.469,     0.469,    -0.469],
        [ 0.000,     0.759,     0.290],
        ],
    }

buckeyball =  {
    "points" : 
    [
      [-0.0655604, -0.854729,  0.514918],
      [-0.0655604,  0.854729,  0.514918],
      [-0.106079,  -0.326477, -0.939234],
      [-0.106079,  -0.979432, -0.171639],
      [-0.106079,   0.326477, -0.939234],
      [-0.106079,   0.979432, -0.171639],
      [-0.212158,  -0.652955, -0.727076],
      [-0.212158,   0.652955, -0.727076],
      [-0.277718,  -0.201774,  0.939234],
      [-0.277718,   0.201774,  0.939234],
      [-0.343279,   0.000000, -0.939234],
      [-0.449358,  -0.730026,  0.514918],
      [-0.449358,   0.730026,  0.514918],
      [-0.489876,  -0.854729, -0.171639],
      [-0.489876,   0.854729, -0.171639],
      [-0.555436,  -0.403548,  0.727076],
      [-0.555436,  -0.652955, -0.514918],
      [-0.555436,   0.403548,  0.727076],
      [-0.555436,   0.652955, -0.514918],
      [-0.661515,  -0.730026,  0.171639],
      [-0.661515,   0.730026,  0.171639],
      [-0.686557,   0.000000, -0.727076],
      [-0.792636,  -0.326477, -0.514918],
      [-0.792636,   0.326477, -0.514918],
      [-0.833155,  -0.201774,  0.514918],
      [-0.833155,   0.201774,  0.514918],
      [-0.898715,  -0.403548,  0.171639],
      [-0.898715,   0.403548,  0.171639],
      [-0.964275,  -0.201774, -0.171639],
      [-0.964275,   0.201774, -0.171639],
      [0.0655604,  -0.854729, -0.514918],
      [0.0655604,   0.854729, -0.514918],
      [0.106079,   -0.326477,  0.939234],
      [0.106079,   -0.979432,  0.171639],
      [0.106079,    0.326477,  0.939234],
      [0.106079,    0.979432,  0.171639],
      [0.212158,   -0.652955,  0.727076],
      [0.212158,    0.652955,  0.727076],
      [0.277718,   -0.201774, -0.939234],
      [0.277718,    0.201774, -0.939234],
      [0.343279,    0,         0.939234],
      [0.449358,   -0.730026, -0.514918],
      [0.449358,    0.730026, -0.514918],
      [0.489876,   -0.854729,  0.171639],
      [0.489876,    0.854729,  0.171639],
      [0.555436,   -0.403548, -0.727076],
      [0.555436,   -0.652955,  0.514918],
      [0.555436,    0.403548, -0.727076],
      [0.555436,    0.652955,  0.514918],
      [0.661515,   -0.730026, -0.171639],
      [0.661515,    0.730026, -0.171639],
      [0.686557,    0,         0.727076],
      [0.792636,   -0.326477,  0.514918],
      [0.792636,    0.326477,  0.514918],
      [0.833155,   -0.201774, -0.514918],
      [0.833155,    0.201774, -0.514918],
      [0.898715,   -0.403548, -0.171639],
      [0.898715,    0.403548, -0.171639],
      [0.964275,   -0.201774,  0.171639],
      [0.964275,    0.201774,  0.171639],
      ],
    }

bucky_240_points = {
    "points" :
     [
      [-0.0216227, -0.630351, -0.776009],
      [-0.0216227, 0.630351, -0.776009],
      [0.0216227, -0.630351, 0.776009],
      [0.0216227, 0.630351, 0.776009],
      [-0.0349863, -0.456127, 0.889227],
      [-0.0349863, 0.456127, 0.889227],
      [0.0349863, -0.456127, -0.889227],
      [0.0349863, 0.456127, -0.889227],
      [-0.0500698, -0.154099, -0.986786],
      [-0.0500698, 0.154099, -0.986786],
      [0.0500698, -0.154099, 0.986786],
      [0.0500698, 0.154099, 0.986786],
      [-0.0655604, -0.854729, 0.514918],
      [-0.0655604, 0.854729, 0.514918],
      [0.0655604, -0.854729, -0.514918],
      [0.0655604, 0.854729, -0.514918],
      [-0.0915954, -0.978801, 0.183191],
      [-0.0915954, 0.978801, 0.183191],
      [0.0915954, -0.978801, -0.183191],
      [0.0915954, 0.978801, -0.183191],
      [-0.106079, -0.326477, -0.939234],
      [-0.106079, 0.326477, -0.939234],
      [0.106079, -0.326477, 0.939234],
      [0.106079, 0.326477, 0.939234],
      [-0.106079, -0.979432, -0.171639],
      [-0.106079, 0.979432, -0.171639],
      [0.106079, -0.979432, 0.171639],
      [0.106079, 0.979432, 0.171639],
      [-0.119265, -0.865734, -0.486088],
      [-0.119265, 0.865734, -0.486088],
      [0.119265, -0.865734, 0.486088],
      [0.119265, 0.865734, 0.486088],
      [-0.126582, -0.738028, 0.662791],
      [-0.126582, 0.738028, 0.662791],
      [0.126582, -0.738028, -0.662791],
      [0.126582, 0.738028, -0.662791],
      [-0.131084, -0.0952384, 0.986786],
      [-0.131084, 0.0952384, 0.986786],
      [0.131084, -0.0952384, -0.986786],
      [0.131084, 0.0952384, -0.986786],
      [-0.162029, 0, -0.986786],
      [0.162029, 0, 0.986786],
      [-0.183191, -0.912253, 0.366382],
      [-0.183191, 0.912253, 0.366382],
      [0.183191, -0.912253, -0.366382],
      [0.183191, 0.912253, -0.366382],
      [-0.200279, -0.924594, -0.324059],
      [-0.200279, 0.924594, -0.324059],
      [0.200279, -0.924594, 0.324059],
      [0.200279, 0.924594, 0.324059],
      [-0.204814, -0.978801, 0],
      [-0.204814, 0.978801, 0],
      [0.204814, -0.978801, 0],
      [0.204814, 0.978801, 0],
      [-0.212158, -0.652955, -0.727076],
      [-0.212158, 0.652955, -0.727076],
      [0.212158, -0.652955, 0.727076],
      [0.212158, 0.652955, 0.727076],
      [-0.2398, -0.389579, 0.889227],
      [-0.2398, 0.389579, 0.889227],
      [0.2398, -0.389579, -0.889227],
      [0.2398, 0.389579, -0.889227],
      [-0.250349, -0.770495, -0.586227],
      [-0.250349, 0.770495, -0.586227],
      [0.250349, -0.770495, 0.586227],
      [0.250349, 0.770495, 0.586227],
      [-0.277718, -0.201774, 0.939234],
      [-0.277718, 0.201774, 0.939234],
      [0.277718, -0.201774, -0.939234],
      [0.277718, 0.201774, -0.939234],
      [-0.296409, -0.34845, -0.889227],
      [-0.296409, 0.34845, -0.889227],
      [0.296409, -0.34845, 0.889227],
      [0.296409, 0.34845, 0.889227],
      [-0.331395, -0.67148, 0.662791],
      [-0.331395, 0.67148, 0.662791],
      [0.331395, -0.67148, -0.662791],
      [0.331395, 0.67148, -0.662791],
      [-0.343279, 0, -0.939234],
      [0.343279, 0, 0.939234],
      [-0.353018, -0.522674, -0.776009],
      [-0.353018, 0.522674, -0.776009],
      [0.353018, -0.522674, 0.776009],
      [0.353018, 0.522674, 0.776009],
      [-0.381433, -0.865734, -0.324059],
      [-0.381433, 0.865734, -0.324059],
      [0.381433, -0.865734, 0.324059],
      [0.381433, 0.865734, 0.324059],
      [-0.388004, -0.497255, 0.776009],
      [-0.388004, 0.497255, 0.776009],
      [0.388004, -0.497255, -0.776009],
      [0.388004, 0.497255, -0.776009],
      [-0.388004, -0.845705, 0.366382],
      [-0.388004, 0.845705, 0.366382],
      [0.388004, -0.845705, -0.366382],
      [0.388004, 0.845705, -0.366382],
      [-0.409627, -0.912253, 0],
      [-0.409627, 0.912253, 0],
      [0.409627, -0.912253, 0],
      [0.409627, 0.912253, 0],
      [-0.412378, -0.770495, -0.486088],
      [-0.412378, 0.770495, -0.486088],
      [0.412378, -0.770495, 0.486088],
      [0.412378, 0.770495, 0.486088],
      [-0.422991, -0.174225, -0.889227],
      [-0.422991, 0.174225, -0.889227],
      [0.422991, -0.174225, 0.889227],
      [0.422991, 0.174225, 0.889227],
      [-0.444613, -0.107677, 0.889227],
      [-0.444613, 0.107677, 0.889227],
      [0.444613, -0.107677, -0.889227],
      [0.444613, 0.107677, -0.889227],
      [-0.449358, -0.730026, 0.514918],
      [-0.449358, 0.730026, 0.514918],
      [0.449358, -0.730026, -0.514918],
      [0.449358, 0.730026, -0.514918],
      [-0.489876, -0.854729, -0.171639],
      [-0.489876, 0.854729, -0.171639],
      [0.489876, -0.854729, 0.171639],
      [0.489876, 0.854729, 0.171639],
      [-0.501223, -0.845705, 0.183191],
      [-0.501223, 0.845705, 0.183191],
      [0.501223, -0.845705, -0.183191],
      [0.501223, 0.845705, -0.183191],
      [-0.536209, -0.522674, -0.662791],
      [-0.536209, 0.522674, -0.662791],
      [0.536209, -0.522674, 0.662791],
      [0.536209, 0.522674, 0.662791],
      [-0.555436, -0.403548, 0.727076],
      [-0.555436, 0.403548, 0.727076],
      [0.555436, -0.403548, -0.727076],
      [0.555436, 0.403548, -0.727076],
      [-0.555436, -0.652955, -0.514918],
      [-0.555436, 0.652955, -0.514918],
      [0.555436, -0.652955, 0.514918],
      [0.555436, 0.652955, 0.514918],
      [-0.592818, -0.215354, 0.776009],
      [-0.592818, 0.215354, 0.776009],
      [0.592818, -0.215354, -0.776009],
      [0.592818, 0.215354, -0.776009],
      [-0.605352, -0.630291, 0.486088],
      [-0.605352, 0.630291, 0.486088],
      [0.605352, -0.630291, -0.486088],
      [0.605352, 0.630291, -0.486088],
      [-0.606182, -0.174225, -0.776009],
      [-0.606182, 0.174225, -0.776009],
      [0.606182, -0.174225, 0.776009],
      [0.606182, 0.174225, 0.776009],
      [-0.649427, -0.738028, -0.183191],
      [-0.649427, 0.738028, -0.183191],
      [0.649427, -0.738028, 0.183191],
      [0.649427, 0.738028, 0.183191],
      [-0.655422, -0.476192, 0.586227],
      [-0.655422, 0.476192, 0.586227],
      [0.655422, -0.476192, -0.586227],
      [0.655422, 0.476192, -0.586227],
      [-0.661515, -0.730026, 0.171639],
      [-0.661515, 0.730026, 0.171639],
      [0.661515, -0.730026, -0.171639],
      [0.661515, 0.730026, -0.171639],
      [-0.662791, -0.34845, -0.662791],
      [-0.662791, 0.34845, -0.662791],
      [0.662791, -0.34845, 0.662791],
      [0.662791, 0.34845, 0.662791],
      [-0.684413, -0.630351, -0.366382],
      [-0.684413, 0.630351, -0.366382],
      [0.684413, -0.630351, 0.366382],
      [0.684413, 0.630351, 0.366382],
      [-0.686557, 0, -0.727076],
      [0.686557, 0, 0.727076],
      [-0.705492, -0.630291, 0.324059],
      [-0.705492, 0.630291, 0.324059],
      [0.705492, -0.630291, -0.324059],
      [0.705492, 0.630291, -0.324059],
      [-0.741022, -0.107677, 0.662791],
      [-0.741022, 0.107677, 0.662791],
      [0.741022, -0.107677, -0.662791],
      [0.741022, 0.107677, -0.662791],
      [-0.741022, -0.67148, 0],
      [-0.741022, 0.67148, 0],
      [0.741022, -0.67148, 0],
      [0.741022, 0.67148, 0],
      [-0.786507, -0.380954, 0.486088],
      [-0.786507, 0.380954, 0.486088],
      [0.786507, -0.380954, -0.486088],
      [0.786507, 0.380954, -0.486088],
      [-0.792636, -0.326477, -0.514918],
      [-0.792636, 0.326477, -0.514918],
      [0.792636, -0.326477, 0.514918],
      [0.792636, 0.326477, 0.514918],
      [-0.810146, 0, -0.586227],
      [0.810146, 0, 0.586227],
      [-0.810995, -0.456127, -0.366382],
      [-0.810995, 0.456127, -0.366382],
      [0.810995, -0.456127, 0.366382],
      [0.810995, 0.456127, 0.366382],
      [-0.817452, -0.476192, 0.324059],
      [-0.817452, 0.476192, 0.324059],
      [0.817452, -0.476192, -0.324059],
      [0.817452, 0.476192, -0.324059],
      [-0.833155, -0.201774, 0.514918],
      [-0.833155, 0.201774, 0.514918],
      [0.833155, -0.201774, -0.514918],
      [0.833155, 0.201774, -0.514918],
      [-0.860216, -0.154099, -0.486088],
      [-0.860216, 0.154099, -0.486088],
      [0.860216, -0.154099, 0.486088],
      [0.860216, 0.154099, 0.486088],
      [-0.867604, -0.497255, 0],
      [-0.867604, 0.497255, 0],
      [0.867604, -0.497255, 0],
      [0.867604, 0.497255, 0],
      [-0.898715, -0.403548, 0.171639],
      [-0.898715, 0.403548, 0.171639],
      [0.898715, -0.403548, -0.171639],
      [0.898715, 0.403548, -0.171639],
      [-0.902591, -0.389579, -0.183191],
      [-0.902591, 0.389579, -0.183191],
      [0.902591, -0.389579, 0.183191],
      [0.902591, 0.389579, 0.183191],
      [-0.924213, -0.107677, 0.366382],
      [-0.924213, 0.107677, 0.366382],
      [0.924213, -0.107677, -0.366382],
      [0.924213, 0.107677, -0.366382],
      [-0.941231, -0.0952384, -0.324059],
      [-0.941231, 0.0952384, -0.324059],
      [0.941231, -0.0952384, 0.324059],
      [0.941231, 0.0952384, 0.324059],
      [-0.9592, -0.215354, 0.183191],
      [-0.9592, 0.215354, 0.183191],
      [0.9592, -0.215354, -0.183191],
      [0.9592, 0.215354, -0.183191],
      [-0.964275, -0.201774, -0.171639],
      [-0.964275, 0.201774, -0.171639],
      [0.964275, -0.201774, 0.171639],
      [0.964275, 0.201774, 0.171639],
      [-0.994186, -0.107677, 0],
      [-0.994186, 0.107677, 0],
      [0.994186, -0.107677, 0],
      [0.994186, 0.107677, 0],
      ],
    }

polygons = {
    "icosohedron"   : icosohedron,
    "dodecahedron"  : dodecahedron,
    "buckyball"     : buckeyball,
    "buckyball_240" : bucky_240_points,
    "torus_5_10"    : torus_5_10,
    }


def get_polygons():
    return list(polygons.keys())

def contains(str_arr, string):
    for s in str_arr:
        if (s == string):
            return True
    return False
def get_edges(polygon_name):
    polygon = polygons[polygon_name]
    points, adjacency = polygon['points'], polygon['adjacency']
    edges_complete = {}
    edges = []
    npoints = len(points)
    for point in range(npoints):
        color = correct(points[point])
        # go through each point adjacent to this one, and print it's number&color
        for other_point in adjacency[point]:
            if (point < other_point):
                p, op = point, other_point
            else:
                op, p = point, other_point
            name = "%d,%d" % (p, op)
            try:
                x = edges_complete[name]
            except KeyError:
                # We have not done this edge.
                other_color = correct(points[op])
                edges.append(["%d" % p, color, "%d" % op, other_color])
                edges_complete[name] = 1
    return edges;

def color_string(color):
    r, g, b = color[0], color[1], color[2]
    c = ((r << 16) + (g << 8) + b)
    color = "%06X" % c
    return color

def print_edges(edges):
    for edge in edges:
        print((" ".join(edge)))

def correct(p):
    result = []
    for x in p:
        result.append(int(x * 255))
    return result;

def find_adjacency_matrix(points):
    #print points
    npoints = len(points)
    distance_matrix = zeros((npoints, npoints))
    minimum_distance = -1
    for x in range(npoints):
        for y in range(npoints):
            if (x != y):
                dist = distance(points[x], points[y])
                if (minimum_distance < 0):
                    minimum_distance = dist;
                else:
                    if (dist < minimum_distance and dist != 0):
                        minimum_distance = dist
                distance_matrix[x][y] = dist;
    maximum_distance = minimum_distance * 1.2
    result = []
    for x in range(npoints):
        adjacent_points = []
        for y in range(npoints):
            if (x != y):
                if (distance_matrix[x][y] >= minimum_distance and
                    distance_matrix[x][y] <= maximum_distance):
                    adjacent_points.append(y)
        result.append(adjacent_points)
    return result;

def distance(point1, point2):
    x1, y1, z1 = point1[0], point1[1], point1[2]
    x2, y2, z2 = point2[0], point2[1], point2[2]
    distance = sqrt(
        (x1-x2)*(x1-x2) +
        (y1-y2)*(y1-y2) +
        (z1-z2)*(z1-z2));
    return distance;


def scale_and_translate(points):
    maxx, maxy, maxz = -1000000,-1000000,-1000000
    minx, miny, minz =  1000000, 1000000, 1000000
    npoints = len(points)
    for point in range(npoints):
        x, y, z = points[point][0], points[point][1], points[point][2]
        if (x > maxx):
            maxx = x 
        if (y > maxy):
            maxy = y 
        if (z > maxz):
            maxz = z
        if (x < minx):
            minx = x
        if (y < miny):
            miny = y
        if (z < minz):
            minz = z
    deltax     =  -minx
    deltay     =  -miny
    deltaz     =  -minz
    extentx    = (maxx - minx)
    extenty    = (maxy - miny)
    extentz    = (maxz - minz)
    maxextent  = extentx
    if (extenty > maxextent):
        maxextent  = extenty
    if (extentz > maxextent):
        maxextent = extentz
    
    scale = 1.0 / maxextent;

    result = []
    for point in range(npoints):
        x, y, z = points[point][0], points[point][1], points[point][2]
        x = x + deltax
        y = y + deltay
        z = z + deltaz
        x = x * scale
        y = y * scale
        z = z * scale
        newpoint = [x, y, z]
        result.append(newpoint)
    return result

# put the polygon in the + + + octant
# and size it so the minimum coordinate is zero
# and the maximum coordinate is 1.
def normalize(polygons):
    for polygon in polygons:
        polygons[polygon]['adjacency'] = find_adjacency_matrix(polygons[polygon]['points'])
        polygons[polygon]['points']    = scale_and_translate  (polygons[polygon]['points'])


def numeric(a, b):
    A = a.split(" ")
    B = b.split(" ")
    if (int(A[0]) < int(B[0])):
        return -1
    elif (int(A[0]) > int(B[0])):
        return 1
    else:
        if (int(A[1]) < int(B[1])):
            return -1
        elif (int(A[1]) > int(B[1])):
            return 1
        else:
            return 0


# Writes the adjacency matrix of polygon to filename.
# Returns undef on success, or an error message on failure.
def write_adjacency_matrix(polygon_name, file_name):
    matrix = polygons[polygon_name]['adjacency']
    points = polygons[polygon_name]['points']
    fh = open(file_name, "w")
    result = None
    if fh:
        fh.write("# Adjacency matrix for the %s polytype.\n" % polygon_name);
        if (len(matrix) > 0):
            count = 0
            for line in matrix:
                fh.write("%d: %s\n"  % (count, line))
                count = count + 1
        else:
            result = "Error in ColorIt::write_adjacency_matrix.  Couldn't get the matrix for some reason.";
            print((fh, result))
        fh.close()
    else:
        result = "Couldn't open %s for writing." % file_name;
        return
    fn_neato1 = "%s_1.neato" % file_name
    fn_neato2 = "%s_2.neato" % file_name
    fh_neato1 = open(fn_neato1, "w")
    fh_neato2 = open(fn_neato2, "w")
    if (fh_neato1 and fh_neato2):
        neato = {}
        tracker = {}
        for i in range(len(matrix)):
            friends = matrix[i]
            for j in range(len(friends)):
                n1 = i
                n2 = friends[j]
                if (n1 > n2):
                    t = n1
                    n1 = n2
                    n2 = t
                tracker["%d %d" % (n1, n2)] = [n1, n2, "%d -- %d;\n" % (n1, n2)]
        l = list(tracker.keys())
        
        fh_neato1.write("graph G1 {\n")
        tracker2 = {}
        for x in sorted(list(tracker.keys()), key=functools.cmp_to_key(numeric)):
            n1, n2, s = tracker[x]
            tracker2[n1] = 1
            tracker2[n2] = 1
            if (points[n1][0] <= 0.5):
                fh_neato1.write(s)
        for x in tracker2:
            if (points[x][0] <= 0.5):
                r, g, b = correct(points[x])
                if (sqrt((r*r+g*g+b*b)/3) < 128):
                    textcolor = '"white"'
                else:
                    textcolor = '"black"'
                fh_neato1.write("%d [style=filled, fontcolor=%s, fillcolor=\"#%02x%02x%02x\"];\n" % (x, textcolor, r, g, b))
        fh_neato1.write("}\n")
        fh_neato1.close()
 
        fh_neato2.write("graph G1 {\n")
        tracker2 = {}
        for x in sorted(list(tracker.keys()), key=functools.cmp_to_key(numeric)):
            n1, n2, s = tracker[x]
            tracker2[n1] = 1
            tracker2[n2] = 1
            if (points[n1][0] > 0.5):
                fh_neato2.write(s)
        for x in tracker2:
            if (points[x][0] > 0.5):
                r, g, b = correct(points[x])
                if (sqrt((r*r+g*g+b*b)/3) < 128):
                    textcolor = '"white"'
                else:
                    textcolor = '"black"'
                fh_neato2.write("%d [style=filled, fontcolor=%s, fillcolor=\"#%02x%02x%02x\"];\n" % (x, textcolor, r, g, b))
        fh_neato2.write("}\n")
        fh_neato2.close()
        for fn in [fn_neato1, fn_neato2]:
            cmd = ['neato', 
                   '-Tpng',
                   '-o', "%s.png" % fn,
                   fn]
            try:
                subprocess.call(cmd)
            except Exception:
                print ("ERROR:  you probably don't have neato installed.  'sudo apt-get install graphviz' to fix this error.")
                exit(-1)

        
normalize(polygons)
