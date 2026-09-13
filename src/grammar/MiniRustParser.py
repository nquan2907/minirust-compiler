# Generated from E:/PPL BTL/minirust-assignment-2453063/src/grammar/MiniRust.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,60,507,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,5,0,92,8,0,
        10,0,12,0,95,9,0,1,0,5,0,98,8,0,10,0,12,0,101,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,112,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,120,
        8,2,1,3,1,3,1,3,1,3,1,3,3,3,127,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,142,8,5,1,5,1,5,1,6,1,6,3,6,148,8,6,
        1,7,1,7,1,7,1,7,1,7,3,7,155,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,3,10,169,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,186,8,11,1,12,
        1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,212,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,5,15,220,8,15,10,15,12,15,223,9,15,
        1,16,1,16,1,16,1,16,1,16,1,16,5,16,231,8,16,10,16,12,16,234,9,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,245,8,17,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,3,18,264,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,5,19,275,8,19,10,19,12,19,278,9,19,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,292,8,20,10,20,12,20,
        295,9,20,1,21,1,21,1,21,1,21,1,21,3,21,302,8,21,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,3,22,322,8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,5,
        22,332,8,22,10,22,12,22,335,9,22,1,23,1,23,3,23,339,8,23,1,24,1,
        24,1,24,1,24,1,24,3,24,346,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,
        26,1,26,1,26,1,26,1,26,3,26,359,8,26,1,27,1,27,1,27,1,27,1,28,1,
        28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,3,29,375,8,29,1,30,1,
        30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,3,31,418,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,
        32,429,8,32,1,33,1,33,1,33,1,33,3,33,435,8,33,1,34,1,34,1,34,1,34,
        1,34,1,34,1,35,1,35,4,35,445,8,35,11,35,12,35,446,1,35,4,35,450,
        8,35,11,35,12,35,451,1,35,1,35,5,35,456,8,35,10,35,12,35,459,9,35,
        1,35,4,35,462,8,35,11,35,12,35,463,3,35,466,8,35,1,36,1,36,1,37,
        1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,39,1,39,1,40,1,40,1,40,
        1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,43,
        1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,3,44,505,8,44,1,44,0,5,30,
        32,38,40,44,45,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,0,1,3,0,21,22,50,51,59,59,531,0,93,1,0,0,0,2,111,
        1,0,0,0,4,119,1,0,0,0,6,126,1,0,0,0,8,128,1,0,0,0,10,134,1,0,0,0,
        12,147,1,0,0,0,14,154,1,0,0,0,16,156,1,0,0,0,18,160,1,0,0,0,20,168,
        1,0,0,0,22,185,1,0,0,0,24,187,1,0,0,0,26,192,1,0,0,0,28,211,1,0,
        0,0,30,213,1,0,0,0,32,224,1,0,0,0,34,244,1,0,0,0,36,263,1,0,0,0,
        38,265,1,0,0,0,40,279,1,0,0,0,42,301,1,0,0,0,44,321,1,0,0,0,46,338,
        1,0,0,0,48,345,1,0,0,0,50,347,1,0,0,0,52,358,1,0,0,0,54,360,1,0,
        0,0,56,364,1,0,0,0,58,374,1,0,0,0,60,376,1,0,0,0,62,417,1,0,0,0,
        64,428,1,0,0,0,66,434,1,0,0,0,68,436,1,0,0,0,70,465,1,0,0,0,72,467,
        1,0,0,0,74,469,1,0,0,0,76,474,1,0,0,0,78,478,1,0,0,0,80,480,1,0,
        0,0,82,484,1,0,0,0,84,492,1,0,0,0,86,495,1,0,0,0,88,504,1,0,0,0,
        90,92,3,50,25,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,
        1,0,0,0,94,99,1,0,0,0,95,93,1,0,0,0,96,98,3,10,5,0,97,96,1,0,0,0,
        98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,
        99,1,0,0,0,102,103,5,0,0,1,103,1,1,0,0,0,104,112,5,16,0,0,105,112,
        5,17,0,0,106,112,5,18,0,0,107,112,5,20,0,0,108,112,5,19,0,0,109,
        112,5,52,0,0,110,112,3,8,4,0,111,104,1,0,0,0,111,105,1,0,0,0,111,
        106,1,0,0,0,111,107,1,0,0,0,111,108,1,0,0,0,111,109,1,0,0,0,111,
        110,1,0,0,0,112,3,1,0,0,0,113,114,5,27,0,0,114,120,5,28,0,0,115,
        116,5,27,0,0,116,117,3,6,3,0,117,118,5,28,0,0,118,120,1,0,0,0,119,
        113,1,0,0,0,119,115,1,0,0,0,120,5,1,0,0,0,121,122,3,26,13,0,122,
        123,5,30,0,0,123,124,3,6,3,0,124,127,1,0,0,0,125,127,3,26,13,0,126,
        121,1,0,0,0,126,125,1,0,0,0,127,7,1,0,0,0,128,129,5,27,0,0,129,130,
        3,2,1,0,130,131,5,29,0,0,131,132,5,51,0,0,132,133,5,28,0,0,133,9,
        1,0,0,0,134,135,5,1,0,0,135,136,5,52,0,0,136,137,5,23,0,0,137,138,
        3,12,6,0,138,141,5,24,0,0,139,140,5,35,0,0,140,142,3,2,1,0,141,139,
        1,0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,144,3,18,9,0,144,11,
        1,0,0,0,145,148,3,14,7,0,146,148,1,0,0,0,147,145,1,0,0,0,147,146,
        1,0,0,0,148,13,1,0,0,0,149,150,3,16,8,0,150,151,5,30,0,0,151,152,
        3,14,7,0,152,155,1,0,0,0,153,155,3,16,8,0,154,149,1,0,0,0,154,153,
        1,0,0,0,155,15,1,0,0,0,156,157,5,52,0,0,157,158,5,31,0,0,158,159,
        3,2,1,0,159,17,1,0,0,0,160,161,5,25,0,0,161,162,3,20,10,0,162,163,
        5,26,0,0,163,19,1,0,0,0,164,165,3,22,11,0,165,166,3,20,10,0,166,
        169,1,0,0,0,167,169,1,0,0,0,168,164,1,0,0,0,168,167,1,0,0,0,169,
        21,1,0,0,0,170,171,3,24,12,0,171,172,5,29,0,0,172,186,1,0,0,0,173,
        174,3,26,13,0,174,175,5,29,0,0,175,186,1,0,0,0,176,186,3,62,31,0,
        177,186,3,64,32,0,178,186,3,68,34,0,179,186,3,80,40,0,180,186,3,
        82,41,0,181,186,3,84,42,0,182,186,3,86,43,0,183,186,3,88,44,0,184,
        186,3,18,9,0,185,170,1,0,0,0,185,173,1,0,0,0,185,176,1,0,0,0,185,
        177,1,0,0,0,185,178,1,0,0,0,185,179,1,0,0,0,185,180,1,0,0,0,185,
        181,1,0,0,0,185,182,1,0,0,0,185,183,1,0,0,0,185,184,1,0,0,0,186,
        23,1,0,0,0,187,188,5,52,0,0,188,189,5,23,0,0,189,190,3,46,23,0,190,
        191,5,24,0,0,191,25,1,0,0,0,192,193,3,28,14,0,193,27,1,0,0,0,194,
        195,5,52,0,0,195,196,5,49,0,0,196,212,3,28,14,0,197,198,3,30,15,
        0,198,199,5,33,0,0,199,200,5,52,0,0,200,201,5,49,0,0,201,202,3,28,
        14,0,202,212,1,0,0,0,203,204,3,30,15,0,204,205,5,27,0,0,205,206,
        3,26,13,0,206,207,5,28,0,0,207,208,5,49,0,0,208,209,3,28,14,0,209,
        212,1,0,0,0,210,212,3,30,15,0,211,194,1,0,0,0,211,197,1,0,0,0,211,
        203,1,0,0,0,211,210,1,0,0,0,212,29,1,0,0,0,213,214,6,15,-1,0,214,
        215,3,32,16,0,215,221,1,0,0,0,216,217,10,2,0,0,217,218,5,47,0,0,
        218,220,3,32,16,0,219,216,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,
        0,221,222,1,0,0,0,222,31,1,0,0,0,223,221,1,0,0,0,224,225,6,16,-1,
        0,225,226,3,34,17,0,226,232,1,0,0,0,227,228,10,2,0,0,228,229,5,46,
        0,0,229,231,3,34,17,0,230,227,1,0,0,0,231,234,1,0,0,0,232,230,1,
        0,0,0,232,233,1,0,0,0,233,33,1,0,0,0,234,232,1,0,0,0,235,245,3,36,
        18,0,236,237,3,36,18,0,237,238,5,40,0,0,238,239,3,36,18,0,239,245,
        1,0,0,0,240,241,3,36,18,0,241,242,5,41,0,0,242,243,3,36,18,0,243,
        245,1,0,0,0,244,235,1,0,0,0,244,236,1,0,0,0,244,240,1,0,0,0,245,
        35,1,0,0,0,246,264,3,38,19,0,247,248,3,38,19,0,248,249,5,42,0,0,
        249,250,3,38,19,0,250,264,1,0,0,0,251,252,3,38,19,0,252,253,5,43,
        0,0,253,254,3,38,19,0,254,264,1,0,0,0,255,256,3,38,19,0,256,257,
        5,45,0,0,257,258,3,38,19,0,258,264,1,0,0,0,259,260,3,38,19,0,260,
        261,5,44,0,0,261,262,3,38,19,0,262,264,1,0,0,0,263,246,1,0,0,0,263,
        247,1,0,0,0,263,251,1,0,0,0,263,255,1,0,0,0,263,259,1,0,0,0,264,
        37,1,0,0,0,265,266,6,19,-1,0,266,267,3,40,20,0,267,276,1,0,0,0,268,
        269,10,3,0,0,269,270,5,36,0,0,270,275,3,40,20,0,271,272,10,2,0,0,
        272,273,5,37,0,0,273,275,3,40,20,0,274,268,1,0,0,0,274,271,1,0,0,
        0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,39,1,0,0,0,
        278,276,1,0,0,0,279,280,6,20,-1,0,280,281,3,42,21,0,281,293,1,0,
        0,0,282,283,10,4,0,0,283,284,5,38,0,0,284,292,3,42,21,0,285,286,
        10,3,0,0,286,287,5,39,0,0,287,292,3,42,21,0,288,289,10,2,0,0,289,
        290,5,34,0,0,290,292,3,42,21,0,291,282,1,0,0,0,291,285,1,0,0,0,291,
        288,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,
        41,1,0,0,0,295,293,1,0,0,0,296,297,5,37,0,0,297,302,3,42,21,0,298,
        299,5,48,0,0,299,302,3,42,21,0,300,302,3,44,22,0,301,296,1,0,0,0,
        301,298,1,0,0,0,301,300,1,0,0,0,302,43,1,0,0,0,303,304,6,22,-1,0,
        304,305,5,52,0,0,305,306,5,23,0,0,306,307,3,46,23,0,307,308,5,24,
        0,0,308,322,1,0,0,0,309,310,5,23,0,0,310,311,3,26,13,0,311,312,5,
        24,0,0,312,322,1,0,0,0,313,322,5,51,0,0,314,322,5,50,0,0,315,322,
        5,59,0,0,316,322,5,21,0,0,317,322,5,22,0,0,318,322,5,52,0,0,319,
        322,3,4,2,0,320,322,3,56,28,0,321,303,1,0,0,0,321,309,1,0,0,0,321,
        313,1,0,0,0,321,314,1,0,0,0,321,315,1,0,0,0,321,316,1,0,0,0,321,
        317,1,0,0,0,321,318,1,0,0,0,321,319,1,0,0,0,321,320,1,0,0,0,322,
        333,1,0,0,0,323,324,10,12,0,0,324,325,5,27,0,0,325,326,3,26,13,0,
        326,327,5,28,0,0,327,332,1,0,0,0,328,329,10,11,0,0,329,330,5,33,
        0,0,330,332,5,52,0,0,331,323,1,0,0,0,331,328,1,0,0,0,332,335,1,0,
        0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,45,1,0,0,0,335,333,1,0,0,
        0,336,339,3,48,24,0,337,339,1,0,0,0,338,336,1,0,0,0,338,337,1,0,
        0,0,339,47,1,0,0,0,340,341,3,26,13,0,341,342,5,30,0,0,342,343,3,
        48,24,0,343,346,1,0,0,0,344,346,3,26,13,0,345,340,1,0,0,0,345,344,
        1,0,0,0,346,49,1,0,0,0,347,348,5,4,0,0,348,349,5,52,0,0,349,350,
        5,25,0,0,350,351,3,52,26,0,351,352,5,26,0,0,352,51,1,0,0,0,353,354,
        3,54,27,0,354,355,5,30,0,0,355,356,3,52,26,0,356,359,1,0,0,0,357,
        359,3,54,27,0,358,353,1,0,0,0,358,357,1,0,0,0,359,53,1,0,0,0,360,
        361,5,52,0,0,361,362,5,31,0,0,362,363,3,2,1,0,363,55,1,0,0,0,364,
        365,5,52,0,0,365,366,5,25,0,0,366,367,3,58,29,0,367,368,5,26,0,0,
        368,57,1,0,0,0,369,370,3,60,30,0,370,371,5,30,0,0,371,372,3,58,29,
        0,372,375,1,0,0,0,373,375,3,60,30,0,374,369,1,0,0,0,374,373,1,0,
        0,0,375,59,1,0,0,0,376,377,5,52,0,0,377,378,5,31,0,0,378,379,3,26,
        13,0,379,61,1,0,0,0,380,381,5,2,0,0,381,382,5,52,0,0,382,383,5,31,
        0,0,383,384,3,2,1,0,384,385,5,49,0,0,385,386,3,26,13,0,386,387,5,
        29,0,0,387,418,1,0,0,0,388,389,5,2,0,0,389,390,5,3,0,0,390,391,5,
        52,0,0,391,392,5,31,0,0,392,393,3,2,1,0,393,394,5,49,0,0,394,395,
        3,26,13,0,395,396,5,29,0,0,396,418,1,0,0,0,397,398,5,2,0,0,398,399,
        5,3,0,0,399,400,5,52,0,0,400,401,5,49,0,0,401,402,3,26,13,0,402,
        403,5,29,0,0,403,418,1,0,0,0,404,405,5,2,0,0,405,406,5,3,0,0,406,
        407,5,52,0,0,407,408,5,31,0,0,408,409,3,2,1,0,409,410,5,29,0,0,410,
        418,1,0,0,0,411,412,5,2,0,0,412,413,5,52,0,0,413,414,5,49,0,0,414,
        415,3,26,13,0,415,416,5,29,0,0,416,418,1,0,0,0,417,380,1,0,0,0,417,
        388,1,0,0,0,417,397,1,0,0,0,417,404,1,0,0,0,417,411,1,0,0,0,418,
        63,1,0,0,0,419,420,5,5,0,0,420,421,3,26,13,0,421,422,3,18,9,0,422,
        423,3,66,33,0,423,429,1,0,0,0,424,425,5,5,0,0,425,426,3,26,13,0,
        426,427,3,18,9,0,427,429,1,0,0,0,428,419,1,0,0,0,428,424,1,0,0,0,
        429,65,1,0,0,0,430,431,5,6,0,0,431,435,3,18,9,0,432,433,5,6,0,0,
        433,435,3,64,32,0,434,430,1,0,0,0,434,432,1,0,0,0,435,67,1,0,0,0,
        436,437,5,12,0,0,437,438,3,26,13,0,438,439,5,25,0,0,439,440,3,70,
        35,0,440,441,5,26,0,0,441,69,1,0,0,0,442,444,3,76,38,0,443,445,3,
        74,37,0,444,443,1,0,0,0,445,446,1,0,0,0,446,444,1,0,0,0,446,447,
        1,0,0,0,447,466,1,0,0,0,448,450,3,74,37,0,449,448,1,0,0,0,450,451,
        1,0,0,0,451,449,1,0,0,0,451,452,1,0,0,0,452,453,1,0,0,0,453,457,
        3,76,38,0,454,456,3,74,37,0,455,454,1,0,0,0,456,459,1,0,0,0,457,
        455,1,0,0,0,457,458,1,0,0,0,458,466,1,0,0,0,459,457,1,0,0,0,460,
        462,3,74,37,0,461,460,1,0,0,0,462,463,1,0,0,0,463,461,1,0,0,0,463,
        464,1,0,0,0,464,466,1,0,0,0,465,442,1,0,0,0,465,449,1,0,0,0,465,
        461,1,0,0,0,466,71,1,0,0,0,467,468,3,74,37,0,468,73,1,0,0,0,469,
        470,5,13,0,0,470,471,3,78,39,0,471,472,5,31,0,0,472,473,3,20,10,
        0,473,75,1,0,0,0,474,475,5,14,0,0,475,476,5,31,0,0,476,477,3,20,
        10,0,477,77,1,0,0,0,478,479,7,0,0,0,479,79,1,0,0,0,480,481,5,7,0,
        0,481,482,3,26,13,0,482,483,3,18,9,0,483,81,1,0,0,0,484,485,5,8,
        0,0,485,486,5,52,0,0,486,487,5,9,0,0,487,488,3,26,13,0,488,489,5,
        32,0,0,489,490,3,26,13,0,490,491,3,18,9,0,491,83,1,0,0,0,492,493,
        5,10,0,0,493,494,5,29,0,0,494,85,1,0,0,0,495,496,5,11,0,0,496,497,
        5,29,0,0,497,87,1,0,0,0,498,499,5,15,0,0,499,505,5,29,0,0,500,501,
        5,15,0,0,501,502,3,26,13,0,502,503,5,29,0,0,503,505,1,0,0,0,504,
        498,1,0,0,0,504,500,1,0,0,0,505,89,1,0,0,0,36,93,99,111,119,126,
        141,147,154,168,185,211,221,232,244,263,274,276,291,293,301,321,
        331,333,338,345,358,374,417,428,434,446,451,457,463,465,504
    ]

class MiniRustParser ( Parser ):

    grammarFileName = "MiniRust.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'fn'", "'let'", "'mut'", "'struct'", 
                     "'if'", "'else'", "'while'", "'for'", "'in'", "'break'", 
                     "'continue'", "'switch'", "'case'", "'default'", "'return'", 
                     "'i32'", "'f32'", "'bool'", "'void'", "'string'", "'true'", 
                     "'false'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "':'", "'..'", "'.'", "'%'", "'->'", 
                     "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'<='", 
                     "'>='", "'<'", "'>'", "'&&'", "'||'", "'!'", "'='" ]

    symbolicNames = [ "<INVALID>", "FN", "LET", "MUT", "STRUCT", "IF", "ELSE", 
                      "WHILE", "FOR", "IN", "BREAK", "CONTINUE", "SWITCH", 
                      "CASE", "DEFAULT", "RETURN", "I32", "F32", "BOOL", 
                      "VOID", "STRING", "TRUE", "FALSE", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", 
                      "COLON", "DOTDOT", "DOT", "MOD", "ARROW", "ADD", "SUB", 
                      "MUL", "DIV", "EQ", "NEQ", "LTE", "GTE", "LT", "GT", 
                      "AND", "OR", "NOT", "ASSIGN", "FLOAT_LIT", "INT_LIT", 
                      "ID", "WS", "COMMENT", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRING_LITERAL", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_typeExpr = 1
    RULE_arrayLiteral = 2
    RULE_array_list = 3
    RULE_arrayType = 4
    RULE_funcDecl = 5
    RULE_paramList = 6
    RULE_paramListPrime = 7
    RULE_param = 8
    RULE_block = 9
    RULE_statementList = 10
    RULE_statement = 11
    RULE_callExpr = 12
    RULE_expr = 13
    RULE_assign_expr = 14
    RULE_or_expr = 15
    RULE_and_expr = 16
    RULE_eq_expr = 17
    RULE_rel_expr = 18
    RULE_add_expr = 19
    RULE_mul_expr = 20
    RULE_una_expr = 21
    RULE_primary_expr = 22
    RULE_argList = 23
    RULE_argListprime = 24
    RULE_struct_expr = 25
    RULE_fieldDeclList = 26
    RULE_fieldDec = 27
    RULE_structLiteral = 28
    RULE_initializerList = 29
    RULE_initializerDec = 30
    RULE_vardecl = 31
    RULE_ifStmt = 32
    RULE_elsePart = 33
    RULE_switchStmt = 34
    RULE_switchBody = 35
    RULE_switchClause = 36
    RULE_caseClause = 37
    RULE_defaultClause = 38
    RULE_literal = 39
    RULE_whileStmt = 40
    RULE_forStmt = 41
    RULE_breakStmt = 42
    RULE_continueStmt = 43
    RULE_returnStmt = 44

    ruleNames =  [ "program", "typeExpr", "arrayLiteral", "array_list", 
                   "arrayType", "funcDecl", "paramList", "paramListPrime", 
                   "param", "block", "statementList", "statement", "callExpr", 
                   "expr", "assign_expr", "or_expr", "and_expr", "eq_expr", 
                   "rel_expr", "add_expr", "mul_expr", "una_expr", "primary_expr", 
                   "argList", "argListprime", "struct_expr", "fieldDeclList", 
                   "fieldDec", "structLiteral", "initializerList", "initializerDec", 
                   "vardecl", "ifStmt", "elsePart", "switchStmt", "switchBody", 
                   "switchClause", "caseClause", "defaultClause", "literal", 
                   "whileStmt", "forStmt", "breakStmt", "continueStmt", 
                   "returnStmt" ]

    EOF = Token.EOF
    FN=1
    LET=2
    MUT=3
    STRUCT=4
    IF=5
    ELSE=6
    WHILE=7
    FOR=8
    IN=9
    BREAK=10
    CONTINUE=11
    SWITCH=12
    CASE=13
    DEFAULT=14
    RETURN=15
    I32=16
    F32=17
    BOOL=18
    VOID=19
    STRING=20
    TRUE=21
    FALSE=22
    LPAREN=23
    RPAREN=24
    LBRACE=25
    RBRACE=26
    LBRACK=27
    RBRACK=28
    SEMI=29
    COMMA=30
    COLON=31
    DOTDOT=32
    DOT=33
    MOD=34
    ARROW=35
    ADD=36
    SUB=37
    MUL=38
    DIV=39
    EQ=40
    NEQ=41
    LTE=42
    GTE=43
    LT=44
    GT=45
    AND=46
    OR=47
    NOT=48
    ASSIGN=49
    FLOAT_LIT=50
    INT_LIT=51
    ID=52
    WS=53
    COMMENT=54
    LINE_COMMENT=55
    BLOCK_COMMENT=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58
    STRING_LITERAL=59
    ERROR_TOKEN=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniRustParser.EOF, 0)

        def struct_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRustParser.Struct_exprContext)
            else:
                return self.getTypedRuleContext(MiniRustParser.Struct_exprContext,i)


        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRustParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(MiniRustParser.FuncDeclContext,i)


        def getRuleIndex(self):
            return MiniRustParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniRustParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 90
                self.struct_expr()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 96
                self.funcDecl()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(MiniRustParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def I32(self):
            return self.getToken(MiniRustParser.I32, 0)

        def F32(self):
            return self.getToken(MiniRustParser.F32, 0)

        def BOOL(self):
            return self.getToken(MiniRustParser.BOOL, 0)

        def STRING(self):
            return self.getToken(MiniRustParser.STRING, 0)

        def VOID(self):
            return self.getToken(MiniRustParser.VOID, 0)

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniRustParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_typeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExpr" ):
                listener.enterTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExpr" ):
                listener.exitTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeExpr" ):
                return visitor.visitTypeExpr(self)
            else:
                return visitor.visitChildren(self)




    def typeExpr(self):

        localctx = MiniRustParser.TypeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typeExpr)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(MiniRustParser.I32)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(MiniRustParser.F32)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.match(MiniRustParser.BOOL)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(MiniRustParser.STRING)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                self.match(MiniRustParser.VOID)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 6)
                self.state = 109
                self.match(MiniRustParser.ID)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 7)
                self.state = 110
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniRustParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniRustParser.RBRACK, 0)

        def array_list(self):
            return self.getTypedRuleContext(MiniRustParser.Array_listContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = MiniRustParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arrayLiteral)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(MiniRustParser.LBRACK)
                self.state = 114
                self.match(MiniRustParser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(MiniRustParser.LBRACK)
                self.state = 116
                self.array_list()
                self.state = 117
                self.match(MiniRustParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniRustParser.COMMA, 0)

        def array_list(self):
            return self.getTypedRuleContext(MiniRustParser.Array_listContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_array_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_list" ):
                listener.enterArray_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_list" ):
                listener.exitArray_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = MiniRustParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_list)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.expr()
                self.state = 122
                self.match(MiniRustParser.COMMA)
                self.state = 123
                self.array_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniRustParser.LBRACK, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(MiniRustParser.TypeExprContext,0)


        def SEMI(self):
            return self.getToken(MiniRustParser.SEMI, 0)

        def INT_LIT(self):
            return self.getToken(MiniRustParser.INT_LIT, 0)

        def RBRACK(self):
            return self.getToken(MiniRustParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniRustParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(MiniRustParser.LBRACK)
            self.state = 129
            self.typeExpr()
            self.state = 130
            self.match(MiniRustParser.SEMI)
            self.state = 131
            self.match(MiniRustParser.INT_LIT)
            self.state = 132
            self.match(MiniRustParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FN(self):
            return self.getToken(MiniRustParser.FN, 0)

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniRustParser.LPAREN, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniRustParser.ParamListContext,0)


        def RPAREN(self):
            return self.getToken(MiniRustParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniRustParser.BlockContext,0)


        def ARROW(self):
            return self.getToken(MiniRustParser.ARROW, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(MiniRustParser.TypeExprContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniRustParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(MiniRustParser.FN)
            self.state = 135
            self.match(MiniRustParser.ID)
            self.state = 136
            self.match(MiniRustParser.LPAREN)
            self.state = 137
            self.paramList()
            self.state = 138
            self.match(MiniRustParser.RPAREN)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 139
                self.match(MiniRustParser.ARROW)
                self.state = 140
                self.typeExpr()


            self.state = 143
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramListPrime(self):
            return self.getTypedRuleContext(MiniRustParser.ParamListPrimeContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MiniRustParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramList)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.paramListPrime()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniRustParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniRustParser.COMMA, 0)

        def paramListPrime(self):
            return self.getTypedRuleContext(MiniRustParser.ParamListPrimeContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_paramListPrime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamListPrime" ):
                listener.enterParamListPrime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamListPrime" ):
                listener.exitParamListPrime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamListPrime" ):
                return visitor.visitParamListPrime(self)
            else:
                return visitor.visitChildren(self)




    def paramListPrime(self):

        localctx = MiniRustParser.ParamListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramListPrime)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.param()
                self.state = 150
                self.match(MiniRustParser.COMMA)
                self.state = 151
                self.paramListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniRustParser.COLON, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(MiniRustParser.TypeExprContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniRustParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MiniRustParser.ID)
            self.state = 157
            self.match(MiniRustParser.COLON)
            self.state = 158
            self.typeExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniRustParser.LBRACE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniRustParser.StatementListContext,0)


        def RBRACE(self):
            return self.getToken(MiniRustParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniRustParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MiniRustParser.LBRACE)
            self.state = 161
            self.statementList()
            self.state = 162
            self.match(MiniRustParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniRustParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(MiniRustParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MiniRustParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statementList)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 5, 7, 8, 10, 11, 12, 15, 21, 22, 23, 25, 27, 37, 48, 50, 51, 52, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.statement()
                self.state = 165
                self.statementList()
                pass
            elif token in [-1, 13, 14, 26]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callExpr(self):
            return self.getTypedRuleContext(MiniRustParser.CallExprContext,0)


        def SEMI(self):
            return self.getToken(MiniRustParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniRustParser.VardeclContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniRustParser.IfStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(MiniRustParser.SwitchStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MiniRustParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiniRustParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(MiniRustParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(MiniRustParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MiniRustParser.ReturnStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniRustParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniRustParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.callExpr()
                self.state = 171
                self.match(MiniRustParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.expr()
                self.state = 174
                self.match(MiniRustParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.vardecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.switchStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.whileStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.forStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 181
                self.breakStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 182
                self.continueStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 183
                self.returnStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 184
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniRustParser.LPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(MiniRustParser.ArgListContext,0)


        def RPAREN(self):
            return self.getToken(MiniRustParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_callExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpr" ):
                listener.enterCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpr" ):
                listener.exitCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)




    def callExpr(self):

        localctx = MiniRustParser.CallExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_callExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MiniRustParser.ID)
            self.state = 188
            self.match(MiniRustParser.LPAREN)
            self.state = 189
            self.argList()
            self.state = 190
            self.match(MiniRustParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniRustParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.assign_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniRustParser.ASSIGN, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Assign_exprContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Or_exprContext,0)


        def DOT(self):
            return self.getToken(MiniRustParser.DOT, 0)

        def LBRACK(self):
            return self.getToken(MiniRustParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniRustParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_assign_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_expr" ):
                listener.enterAssign_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_expr" ):
                listener.exitAssign_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_expr" ):
                return visitor.visitAssign_expr(self)
            else:
                return visitor.visitChildren(self)




    def assign_expr(self):

        localctx = MiniRustParser.Assign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_expr)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(MiniRustParser.ID)
                self.state = 195
                self.match(MiniRustParser.ASSIGN)
                self.state = 196
                self.assign_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.or_expr(0)
                self.state = 198
                self.match(MiniRustParser.DOT)
                self.state = 199
                self.match(MiniRustParser.ID)
                self.state = 200
                self.match(MiniRustParser.ASSIGN)
                self.state = 201
                self.assign_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.or_expr(0)
                self.state = 204
                self.match(MiniRustParser.LBRACK)
                self.state = 205
                self.expr()
                self.state = 206
                self.match(MiniRustParser.RBRACK)
                self.state = 207
                self.match(MiniRustParser.ASSIGN)
                self.state = 208
                self.assign_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.or_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self):
            return self.getTypedRuleContext(MiniRustParser.And_exprContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Or_exprContext,0)


        def OR(self):
            return self.getToken(MiniRustParser.OR, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_or_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_expr" ):
                listener.enterOr_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_expr" ):
                listener.exitOr_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_expr" ):
                return visitor.visitOr_expr(self)
            else:
                return visitor.visitChildren(self)



    def or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniRustParser.Or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniRustParser.Or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    self.match(MiniRustParser.OR)
                    self.state = 218
                    self.and_expr(0) 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eq_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Eq_exprContext,0)


        def and_expr(self):
            return self.getTypedRuleContext(MiniRustParser.And_exprContext,0)


        def AND(self):
            return self.getToken(MiniRustParser.AND, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_and_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expr" ):
                listener.enterAnd_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expr" ):
                listener.exitAnd_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expr" ):
                return visitor.visitAnd_expr(self)
            else:
                return visitor.visitChildren(self)



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniRustParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.eq_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniRustParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 227
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 228
                    self.match(MiniRustParser.AND)
                    self.state = 229
                    self.eq_expr() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Eq_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRustParser.Rel_exprContext)
            else:
                return self.getTypedRuleContext(MiniRustParser.Rel_exprContext,i)


        def EQ(self):
            return self.getToken(MiniRustParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniRustParser.NEQ, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_eq_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq_expr" ):
                listener.enterEq_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq_expr" ):
                listener.exitEq_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq_expr" ):
                return visitor.visitEq_expr(self)
            else:
                return visitor.visitChildren(self)




    def eq_expr(self):

        localctx = MiniRustParser.Eq_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_eq_expr)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.rel_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.rel_expr()
                self.state = 237
                self.match(MiniRustParser.EQ)
                self.state = 238
                self.rel_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.rel_expr()
                self.state = 241
                self.match(MiniRustParser.NEQ)
                self.state = 242
                self.rel_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRustParser.Add_exprContext)
            else:
                return self.getTypedRuleContext(MiniRustParser.Add_exprContext,i)


        def LTE(self):
            return self.getToken(MiniRustParser.LTE, 0)

        def GTE(self):
            return self.getToken(MiniRustParser.GTE, 0)

        def GT(self):
            return self.getToken(MiniRustParser.GT, 0)

        def LT(self):
            return self.getToken(MiniRustParser.LT, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_rel_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_expr" ):
                listener.enterRel_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_expr" ):
                listener.exitRel_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_expr" ):
                return visitor.visitRel_expr(self)
            else:
                return visitor.visitChildren(self)




    def rel_expr(self):

        localctx = MiniRustParser.Rel_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_rel_expr)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.add_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.add_expr(0)
                self.state = 248
                self.match(MiniRustParser.LTE)
                self.state = 249
                self.add_expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.add_expr(0)
                self.state = 252
                self.match(MiniRustParser.GTE)
                self.state = 253
                self.add_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 255
                self.add_expr(0)
                self.state = 256
                self.match(MiniRustParser.GT)
                self.state = 257
                self.add_expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 259
                self.add_expr(0)
                self.state = 260
                self.match(MiniRustParser.LT)
                self.state = 261
                self.add_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Mul_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Add_exprContext,0)


        def ADD(self):
            return self.getToken(MiniRustParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniRustParser.SUB, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_add_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_expr" ):
                listener.enterAdd_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_expr" ):
                listener.exitAdd_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniRustParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_add_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 274
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MiniRustParser.Add_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                        self.state = 268
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 269
                        self.match(MiniRustParser.ADD)
                        self.state = 270
                        self.mul_expr(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniRustParser.Add_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                        self.state = 271
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 272
                        self.match(MiniRustParser.SUB)
                        self.state = 273
                        self.mul_expr(0)
                        pass

             
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def una_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Una_exprContext,0)


        def mul_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Mul_exprContext,0)


        def MUL(self):
            return self.getToken(MiniRustParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniRustParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniRustParser.MOD, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_mul_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_expr" ):
                listener.enterMul_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_expr" ):
                listener.exitMul_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)



    def mul_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniRustParser.Mul_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_mul_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.una_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 291
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniRustParser.Mul_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                        self.state = 282
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 283
                        self.match(MiniRustParser.MUL)
                        self.state = 284
                        self.una_expr()
                        pass

                    elif la_ == 2:
                        localctx = MiniRustParser.Mul_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                        self.state = 285
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 286
                        self.match(MiniRustParser.DIV)
                        self.state = 287
                        self.una_expr()
                        pass

                    elif la_ == 3:
                        localctx = MiniRustParser.Mul_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                        self.state = 288
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 289
                        self.match(MiniRustParser.MOD)
                        self.state = 290
                        self.una_expr()
                        pass

             
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Una_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MiniRustParser.SUB, 0)

        def una_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Una_exprContext,0)


        def NOT(self):
            return self.getToken(MiniRustParser.NOT, 0)

        def primary_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Primary_exprContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_una_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUna_expr" ):
                listener.enterUna_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUna_expr" ):
                listener.exitUna_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUna_expr" ):
                return visitor.visitUna_expr(self)
            else:
                return visitor.visitChildren(self)




    def una_expr(self):

        localctx = MiniRustParser.Una_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_una_expr)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(MiniRustParser.SUB)
                self.state = 297
                self.una_expr()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(MiniRustParser.NOT)
                self.state = 299
                self.una_expr()
                pass
            elif token in [21, 22, 23, 27, 50, 51, 52, 59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 300
                self.primary_expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniRustParser.LPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(MiniRustParser.ArgListContext,0)


        def RPAREN(self):
            return self.getToken(MiniRustParser.RPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def INT_LIT(self):
            return self.getToken(MiniRustParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniRustParser.FLOAT_LIT, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniRustParser.STRING_LITERAL, 0)

        def TRUE(self):
            return self.getToken(MiniRustParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniRustParser.FALSE, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(MiniRustParser.ArrayLiteralContext,0)


        def structLiteral(self):
            return self.getTypedRuleContext(MiniRustParser.StructLiteralContext,0)


        def primary_expr(self):
            return self.getTypedRuleContext(MiniRustParser.Primary_exprContext,0)


        def LBRACK(self):
            return self.getToken(MiniRustParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniRustParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniRustParser.DOT, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_primary_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expr" ):
                listener.enterPrimary_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expr" ):
                listener.exitPrimary_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)



    def primary_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniRustParser.Primary_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_primary_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 304
                self.match(MiniRustParser.ID)
                self.state = 305
                self.match(MiniRustParser.LPAREN)
                self.state = 306
                self.argList()
                self.state = 307
                self.match(MiniRustParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 309
                self.match(MiniRustParser.LPAREN)
                self.state = 310
                self.expr()
                self.state = 311
                self.match(MiniRustParser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 313
                self.match(MiniRustParser.INT_LIT)
                pass

            elif la_ == 4:
                self.state = 314
                self.match(MiniRustParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.state = 315
                self.match(MiniRustParser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.state = 316
                self.match(MiniRustParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 317
                self.match(MiniRustParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 318
                self.match(MiniRustParser.ID)
                pass

            elif la_ == 9:
                self.state = 319
                self.arrayLiteral()
                pass

            elif la_ == 10:
                self.state = 320
                self.structLiteral()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 331
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MiniRustParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 323
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 324
                        self.match(MiniRustParser.LBRACK)
                        self.state = 325
                        self.expr()
                        self.state = 326
                        self.match(MiniRustParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniRustParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 328
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 329
                        self.match(MiniRustParser.DOT)
                        self.state = 330
                        self.match(MiniRustParser.ID)
                        pass

             
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argListprime(self):
            return self.getTypedRuleContext(MiniRustParser.ArgListprimeContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = MiniRustParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_argList)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23, 27, 37, 48, 50, 51, 52, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.argListprime()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniRustParser.COMMA, 0)

        def argListprime(self):
            return self.getTypedRuleContext(MiniRustParser.ArgListprimeContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_argListprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgListprime" ):
                listener.enterArgListprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgListprime" ):
                listener.exitArgListprime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgListprime" ):
                return visitor.visitArgListprime(self)
            else:
                return visitor.visitChildren(self)




    def argListprime(self):

        localctx = MiniRustParser.ArgListprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_argListprime)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.expr()
                self.state = 341
                self.match(MiniRustParser.COMMA)
                self.state = 342
                self.argListprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniRustParser.STRUCT, 0)

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniRustParser.LBRACE, 0)

        def fieldDeclList(self):
            return self.getTypedRuleContext(MiniRustParser.FieldDeclListContext,0)


        def RBRACE(self):
            return self.getToken(MiniRustParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_struct_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_expr" ):
                listener.enterStruct_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_expr" ):
                listener.exitStruct_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_expr" ):
                return visitor.visitStruct_expr(self)
            else:
                return visitor.visitChildren(self)




    def struct_expr(self):

        localctx = MiniRustParser.Struct_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_struct_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(MiniRustParser.STRUCT)
            self.state = 348
            self.match(MiniRustParser.ID)
            self.state = 349
            self.match(MiniRustParser.LBRACE)
            self.state = 350
            self.fieldDeclList()
            self.state = 351
            self.match(MiniRustParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDec(self):
            return self.getTypedRuleContext(MiniRustParser.FieldDecContext,0)


        def COMMA(self):
            return self.getToken(MiniRustParser.COMMA, 0)

        def fieldDeclList(self):
            return self.getTypedRuleContext(MiniRustParser.FieldDeclListContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_fieldDeclList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDeclList" ):
                listener.enterFieldDeclList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDeclList" ):
                listener.exitFieldDeclList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclList" ):
                return visitor.visitFieldDeclList(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclList(self):

        localctx = MiniRustParser.FieldDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_fieldDeclList)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.fieldDec()
                self.state = 354
                self.match(MiniRustParser.COMMA)
                self.state = 355
                self.fieldDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.fieldDec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniRustParser.COLON, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(MiniRustParser.TypeExprContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_fieldDec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDec" ):
                listener.enterFieldDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDec" ):
                listener.exitFieldDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDec" ):
                return visitor.visitFieldDec(self)
            else:
                return visitor.visitChildren(self)




    def fieldDec(self):

        localctx = MiniRustParser.FieldDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_fieldDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniRustParser.ID)
            self.state = 361
            self.match(MiniRustParser.COLON)
            self.state = 362
            self.typeExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniRustParser.LBRACE, 0)

        def initializerList(self):
            return self.getTypedRuleContext(MiniRustParser.InitializerListContext,0)


        def RBRACE(self):
            return self.getToken(MiniRustParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_structLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructLiteral" ):
                listener.enterStructLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructLiteral" ):
                listener.exitStructLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLiteral" ):
                return visitor.visitStructLiteral(self)
            else:
                return visitor.visitChildren(self)




    def structLiteral(self):

        localctx = MiniRustParser.StructLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_structLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MiniRustParser.ID)
            self.state = 365
            self.match(MiniRustParser.LBRACE)
            self.state = 366
            self.initializerList()
            self.state = 367
            self.match(MiniRustParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializerDec(self):
            return self.getTypedRuleContext(MiniRustParser.InitializerDecContext,0)


        def COMMA(self):
            return self.getToken(MiniRustParser.COMMA, 0)

        def initializerList(self):
            return self.getTypedRuleContext(MiniRustParser.InitializerListContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_initializerList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializerList" ):
                listener.enterInitializerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializerList" ):
                listener.exitInitializerList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializerList" ):
                return visitor.visitInitializerList(self)
            else:
                return visitor.visitChildren(self)




    def initializerList(self):

        localctx = MiniRustParser.InitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_initializerList)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.initializerDec()
                self.state = 370
                self.match(MiniRustParser.COMMA)
                self.state = 371
                self.initializerList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.initializerDec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializerDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniRustParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_initializerDec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializerDec" ):
                listener.enterInitializerDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializerDec" ):
                listener.exitInitializerDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializerDec" ):
                return visitor.visitInitializerDec(self)
            else:
                return visitor.visitChildren(self)




    def initializerDec(self):

        localctx = MiniRustParser.InitializerDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_initializerDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(MiniRustParser.ID)
            self.state = 377
            self.match(MiniRustParser.COLON)
            self.state = 378
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(MiniRustParser.LET, 0)

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniRustParser.COLON, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(MiniRustParser.TypeExprContext,0)


        def ASSIGN(self):
            return self.getToken(MiniRustParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniRustParser.SEMI, 0)

        def MUT(self):
            return self.getToken(MiniRustParser.MUT, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_vardecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl" ):
                listener.enterVardecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl" ):
                listener.exitVardecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniRustParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_vardecl)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(MiniRustParser.LET)
                self.state = 381
                self.match(MiniRustParser.ID)
                self.state = 382
                self.match(MiniRustParser.COLON)
                self.state = 383
                self.typeExpr()
                self.state = 384
                self.match(MiniRustParser.ASSIGN)
                self.state = 385
                self.expr()
                self.state = 386
                self.match(MiniRustParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(MiniRustParser.LET)
                self.state = 389
                self.match(MiniRustParser.MUT)
                self.state = 390
                self.match(MiniRustParser.ID)
                self.state = 391
                self.match(MiniRustParser.COLON)
                self.state = 392
                self.typeExpr()
                self.state = 393
                self.match(MiniRustParser.ASSIGN)
                self.state = 394
                self.expr()
                self.state = 395
                self.match(MiniRustParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 397
                self.match(MiniRustParser.LET)
                self.state = 398
                self.match(MiniRustParser.MUT)
                self.state = 399
                self.match(MiniRustParser.ID)
                self.state = 400
                self.match(MiniRustParser.ASSIGN)
                self.state = 401
                self.expr()
                self.state = 402
                self.match(MiniRustParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 404
                self.match(MiniRustParser.LET)
                self.state = 405
                self.match(MiniRustParser.MUT)
                self.state = 406
                self.match(MiniRustParser.ID)
                self.state = 407
                self.match(MiniRustParser.COLON)
                self.state = 408
                self.typeExpr()
                self.state = 409
                self.match(MiniRustParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 411
                self.match(MiniRustParser.LET)
                self.state = 412
                self.match(MiniRustParser.ID)
                self.state = 413
                self.match(MiniRustParser.ASSIGN)
                self.state = 414
                self.expr()
                self.state = 415
                self.match(MiniRustParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniRustParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniRustParser.BlockContext,0)


        def elsePart(self):
            return self.getTypedRuleContext(MiniRustParser.ElsePartContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MiniRustParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifStmt)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.match(MiniRustParser.IF)
                self.state = 420
                self.expr()
                self.state = 421
                self.block()
                self.state = 422
                self.elsePart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(MiniRustParser.IF)
                self.state = 425
                self.expr()
                self.state = 426
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsePartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniRustParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniRustParser.BlockContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniRustParser.IfStmtContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_elsePart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsePart" ):
                listener.enterElsePart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsePart" ):
                listener.exitElsePart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsePart" ):
                return visitor.visitElsePart(self)
            else:
                return visitor.visitChildren(self)




    def elsePart(self):

        localctx = MiniRustParser.ElsePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elsePart)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(MiniRustParser.ELSE)
                self.state = 431
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(MiniRustParser.ELSE)
                self.state = 433
                self.ifStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(MiniRustParser.SWITCH, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(MiniRustParser.LBRACE, 0)

        def switchBody(self):
            return self.getTypedRuleContext(MiniRustParser.SwitchBodyContext,0)


        def RBRACE(self):
            return self.getToken(MiniRustParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStmt" ):
                return visitor.visitSwitchStmt(self)
            else:
                return visitor.visitChildren(self)




    def switchStmt(self):

        localctx = MiniRustParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_switchStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(MiniRustParser.SWITCH)
            self.state = 437
            self.expr()
            self.state = 438
            self.match(MiniRustParser.LBRACE)
            self.state = 439
            self.switchBody()
            self.state = 440
            self.match(MiniRustParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defaultClause(self):
            return self.getTypedRuleContext(MiniRustParser.DefaultClauseContext,0)


        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRustParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(MiniRustParser.CaseClauseContext,i)


        def getRuleIndex(self):
            return MiniRustParser.RULE_switchBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBody" ):
                listener.enterSwitchBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBody" ):
                listener.exitSwitchBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchBody" ):
                return visitor.visitSwitchBody(self)
            else:
                return visitor.visitChildren(self)




    def switchBody(self):

        localctx = MiniRustParser.SwitchBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_switchBody)
        self._la = 0 # Token type
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.defaultClause()
                self.state = 444 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 443
                    self.caseClause()
                    self.state = 446 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==13):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 448
                    self.caseClause()
                    self.state = 451 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==13):
                        break

                self.state = 453
                self.defaultClause()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 454
                    self.caseClause()
                    self.state = 459
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 461 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 460
                    self.caseClause()
                    self.state = 463 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==13):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseClause(self):
            return self.getTypedRuleContext(MiniRustParser.CaseClauseContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_switchClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchClause" ):
                listener.enterSwitchClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchClause" ):
                listener.exitSwitchClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchClause" ):
                return visitor.visitSwitchClause(self)
            else:
                return visitor.visitChildren(self)




    def switchClause(self):

        localctx = MiniRustParser.SwitchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_switchClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.caseClause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(MiniRustParser.CASE, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniRustParser.LiteralContext,0)


        def COLON(self):
            return self.getToken(MiniRustParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniRustParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_caseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseClause" ):
                listener.enterCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseClause" ):
                listener.exitCaseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseClause" ):
                return visitor.visitCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def caseClause(self):

        localctx = MiniRustParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_caseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(MiniRustParser.CASE)
            self.state = 470
            self.literal()
            self.state = 471
            self.match(MiniRustParser.COLON)
            self.state = 472
            self.statementList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(MiniRustParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(MiniRustParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniRustParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_defaultClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultClause" ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultClause" ):
                listener.exitDefaultClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultClause" ):
                return visitor.visitDefaultClause(self)
            else:
                return visitor.visitChildren(self)




    def defaultClause(self):

        localctx = MiniRustParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_defaultClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniRustParser.DEFAULT)
            self.state = 475
            self.match(MiniRustParser.COLON)
            self.state = 476
            self.statementList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniRustParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniRustParser.FLOAT_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniRustParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniRustParser.FALSE, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniRustParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniRustParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 579838452030242816) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniRustParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniRustParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MiniRustParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(MiniRustParser.WHILE)
            self.state = 481
            self.expr()
            self.state = 482
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniRustParser.FOR, 0)

        def ID(self):
            return self.getToken(MiniRustParser.ID, 0)

        def IN(self):
            return self.getToken(MiniRustParser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRustParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniRustParser.ExprContext,i)


        def DOTDOT(self):
            return self.getToken(MiniRustParser.DOTDOT, 0)

        def block(self):
            return self.getTypedRuleContext(MiniRustParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MiniRustParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(MiniRustParser.FOR)
            self.state = 485
            self.match(MiniRustParser.ID)
            self.state = 486
            self.match(MiniRustParser.IN)
            self.state = 487
            self.expr()
            self.state = 488
            self.match(MiniRustParser.DOTDOT)
            self.state = 489
            self.expr()
            self.state = 490
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniRustParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MiniRustParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = MiniRustParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(MiniRustParser.BREAK)
            self.state = 493
            self.match(MiniRustParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniRustParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniRustParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniRustParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = MiniRustParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(MiniRustParser.CONTINUE)
            self.state = 496
            self.match(MiniRustParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniRustParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MiniRustParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRustParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniRustParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MiniRustParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_returnStmt)
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(MiniRustParser.RETURN)
                self.state = 499
                self.match(MiniRustParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(MiniRustParser.RETURN)
                self.state = 501
                self.expr()
                self.state = 502
                self.match(MiniRustParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.or_expr_sempred
        self._predicates[16] = self.and_expr_sempred
        self._predicates[19] = self.add_expr_sempred
        self._predicates[20] = self.mul_expr_sempred
        self._predicates[22] = self.primary_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def or_expr_sempred(self, localctx:Or_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def and_expr_sempred(self, localctx:And_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def mul_expr_sempred(self, localctx:Mul_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def primary_expr_sempred(self, localctx:Primary_exprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 11)
         




