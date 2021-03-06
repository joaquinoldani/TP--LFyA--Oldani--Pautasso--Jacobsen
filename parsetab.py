
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS ASC BY COMMA CONTIDION COUNT DESC DISTINCT DOT EQUAL FROM FULL GREATER_THAN GREATER_THAN_OR_EQUALS GROUP HAVING IN INNER JOIN LEFT LEFT_BRACKET LEFT_PARENTHESIS LESS_THAN LESS_THAN_OR_EQUALS MAX MIN NOT_EQUAL NULL NUMBER ON OR ORDER OUTER QUOTE RIGHT RIGHT_BRACKET RIGHT_PARENTHESIS SELECT STRING WHEREQUERY : SELECT_NT FROM_NT JOIN_NT WHERE_NT GROUP_BY_NT ORDER_BY_NTSELECT_NT : SELECT DISTINCT COLUMNS\n                 | SELECT COLUMNSCOLUMNS : COLUMN COMMA COLUMNS\n               | DISTINCT COLUMN COMMA COLUMNS\n               | COLUMNALIAS : AS QUOTE STRING QUOTE\n             | AS QUOTE STRING STRINGS QUOTE\n             |\xa0AS STRINGSTRINGS : STRING STRINGS\n               | STRINGCOLUMN : COLUMN_WIHTOUT_ALIAS\n              | STRING DOT STRING ALIAS\n              | FUNCTION ALIAS\n              |\xa0FUNCTIONCOLUMN_WIHTOUT_ALIAS : STRING DOT STRINGFUNCTION : VALID_FUNCTIONS LEFT_PARENTHESIS COLUMN_WIHTOUT_ALIAS RIGHT_PARENTHESISVALID_FUNCTIONS : COUNT\n                       | MAX\n                       |\xa0MINFROM_NT : FROM TABLESTABLES : TABLE\n              | TABLE COMMA TABLESTABLE : STRING STRING\n             |\xa0STRING AS STRING\n             | STRINGJOIN_NT : VALID_JOINS\n                |\xa0VALID_JOINS : VALID_JOIN\n                   |\xa0VALID_JOIN VALID_JOINSVALID_JOIN : INNER JOIN TABLE ON CONDITION\n                   | LEFT JOIN TABLE ON CONDITION\n                   |\xa0RIGHT JOIN TABLE ON CONDITION\n                   |\xa0FULL OUTER JOIN TABLE ON CONDITIONCONDITIONS : CONDITION\n                  | CONTIDION CONDITIONSCONDITION : COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR COLUMN_WIHTOUT_ALIAS\n                 | COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR FUNCTION\n                 |\xa0COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR QUOTE STRING QUOTE\n                 |\xa0COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR NUMBERCOMPARATION_OPERATOR : EQUAL\n                            |\xa0NOT_EQUAL\n                            |\xa0GREATER_THAN\n                            |\xa0GREATER_THAN_OR_EQUALS\n                            |\xa0LESS_THAN\n                            |\xa0LESS_THAN_OR_EQUALSWHERE_NT : WHERE COMPARATIONS\n                | WHERE COLUMN IN LEFT_PARENTHESIS QUERY RIGHT_PARENTHESIS\n                |\xa0COMPARATIONS : CONDITION\n                    |\xa0CONDITION AND COMPARATIONSGROUP_BY_NT : GROUP BY_NT\n                    | BY_NT : BY COLUMNS\n          | BY COLUMNS HAVING FUNCTION COMPARATION_OPERATOR STRING\n          | BY COLUMNS HAVING FUNCTION COMPARATION_OPERATOR NUMBERORDER_BY_NT : ORDER BY_NT_WITHOUT_HAVING\n                    |\xa0BY_NT_WITHOUT_HAVING : BY COLUMNS DESC\n                            | BY COLUMNS ASC\n                            |\xa0BY COLUMNS'
    
_lr_action_items = {'SELECT':([0,95,],[3,3,]),'$end':([1,4,8,9,11,16,17,18,23,24,25,31,34,36,42,46,47,49,52,54,56,62,63,66,68,70,72,87,88,91,92,94,96,98,99,101,102,103,104,107,108,112,113,114,116,117,119,120,],[0,-28,-6,-12,-15,-49,-27,-29,-21,-22,-26,-14,-53,-30,-24,-4,-16,-9,-58,-47,-50,-23,-25,-13,-17,-1,-52,-5,-7,-16,-57,-54,-51,-37,-38,-40,-31,-32,-33,-8,-61,-34,-59,-60,-48,-39,-55,-56,]),'FROM':([2,7,8,9,11,27,28,31,46,47,49,65,66,68,87,88,107,],[5,-3,-6,-12,-15,-2,-6,-14,-4,-16,-9,-4,-13,-17,-5,-7,-8,]),'DISTINCT':([3,6,29,45,64,73,93,],[6,26,26,26,26,26,26,]),'STRING':([3,5,6,25,26,29,30,32,33,35,37,38,39,41,43,45,48,61,64,67,69,73,75,76,77,78,79,80,81,82,83,84,85,89,93,100,105,118,],[10,25,10,42,10,10,47,49,51,10,25,25,25,25,63,10,67,25,10,89,91,10,51,51,-41,-42,-43,-44,-45,-46,51,51,51,89,10,111,51,119,]),'COUNT':([3,6,26,29,35,45,64,73,76,77,78,79,80,81,82,93,109,],[13,13,13,13,13,13,13,13,13,-41,-42,-43,-44,-45,-46,13,13,]),'MAX':([3,6,26,29,35,45,64,73,76,77,78,79,80,81,82,93,109,],[14,14,14,14,14,14,14,14,14,-41,-42,-43,-44,-45,-46,14,14,]),'MIN':([3,6,26,29,35,45,64,73,76,77,78,79,80,81,82,93,109,],[15,15,15,15,15,15,15,15,15,-41,-42,-43,-44,-45,-46,15,15,]),'WHERE':([4,16,17,18,23,24,25,36,42,62,63,68,91,98,99,101,102,103,104,112,117,],[-28,35,-27,-29,-21,-22,-26,-30,-24,-23,-25,-17,-16,-37,-38,-40,-31,-32,-33,-34,-39,]),'GROUP':([4,16,17,18,23,24,25,34,36,42,54,56,62,63,68,91,96,98,99,101,102,103,104,112,116,117,],[-28,-49,-27,-29,-21,-22,-26,53,-30,-24,-47,-50,-23,-25,-17,-16,-51,-37,-38,-40,-31,-32,-33,-34,-48,-39,]),'ORDER':([4,8,9,11,16,17,18,23,24,25,31,34,36,42,46,47,49,52,54,56,62,63,66,68,72,87,88,91,94,96,98,99,101,102,103,104,107,112,116,117,119,120,],[-28,-6,-12,-15,-49,-27,-29,-21,-22,-26,-14,-53,-30,-24,-4,-16,-9,71,-47,-50,-23,-25,-13,-17,-52,-5,-7,-16,-54,-51,-37,-38,-40,-31,-32,-33,-8,-34,-48,-39,-55,-56,]),'RIGHT_PARENTHESIS':([4,8,9,11,16,17,18,23,24,25,31,34,36,42,46,47,49,50,52,54,56,62,63,66,68,70,72,87,88,91,92,94,96,98,99,101,102,103,104,107,108,110,112,113,114,116,117,119,120,],[-28,-6,-12,-15,-49,-27,-29,-21,-22,-26,-14,-53,-30,-24,-4,-16,-9,68,-58,-47,-50,-23,-25,-13,-17,-1,-52,-5,-7,-16,-57,-54,-51,-37,-38,-40,-31,-32,-33,-8,-61,116,-34,-59,-60,-48,-39,-55,-56,]),'INNER':([4,18,23,24,25,42,62,63,68,91,98,99,101,102,103,104,112,117,],[19,19,-21,-22,-26,-24,-23,-25,-17,-16,-37,-38,-40,-31,-32,-33,-34,-39,]),'LEFT':([4,18,23,24,25,42,62,63,68,91,98,99,101,102,103,104,112,117,],[20,20,-21,-22,-26,-24,-23,-25,-17,-16,-37,-38,-40,-31,-32,-33,-34,-39,]),'RIGHT':([4,18,23,24,25,42,62,63,68,91,98,99,101,102,103,104,112,117,],[21,21,-21,-22,-26,-24,-23,-25,-17,-16,-37,-38,-40,-31,-32,-33,-34,-39,]),'FULL':([4,18,23,24,25,42,62,63,68,91,98,99,101,102,103,104,112,117,],[22,22,-21,-22,-26,-24,-23,-25,-17,-16,-37,-38,-40,-31,-32,-33,-34,-39,]),'COMMA':([8,9,11,24,25,28,31,42,44,47,49,63,66,68,88,107,],[29,-12,-15,41,-26,45,-14,-24,64,-16,-9,-25,-13,-17,-7,-8,]),'HAVING':([8,9,11,31,46,47,49,66,68,87,88,94,107,],[-6,-12,-15,-14,-4,-16,-9,-13,-17,-5,-7,109,-8,]),'DESC':([8,9,11,31,46,47,49,66,68,87,88,107,108,],[-6,-12,-15,-14,-4,-16,-9,-13,-17,-5,-7,-8,113,]),'ASC':([8,9,11,31,46,47,49,66,68,87,88,107,108,],[-6,-12,-15,-14,-4,-16,-9,-13,-17,-5,-7,-8,114,]),'DOT':([10,51,],[30,69,]),'IN':([11,31,47,49,55,57,66,68,88,107,],[-15,-14,-16,-9,74,-12,-13,-17,-7,-8,]),'AS':([11,25,47,68,],[32,43,32,-17,]),'LEFT_PARENTHESIS':([12,13,14,15,74,],[33,-18,-19,-20,95,]),'JOIN':([19,20,21,40,],[37,38,39,61,]),'OUTER':([22,],[40,]),'ON':([25,42,58,59,60,63,86,],[-26,-24,83,84,85,-25,105,]),'QUOTE':([32,67,76,77,78,79,80,81,82,89,90,106,111,],[48,88,100,-41,-42,-43,-44,-45,-46,-11,107,-10,117,]),'EQUAL':([47,57,68,91,97,115,],[-16,77,-17,-16,77,77,]),'NOT_EQUAL':([47,57,68,91,97,115,],[-16,78,-17,-16,78,78,]),'GREATER_THAN':([47,57,68,91,97,115,],[-16,79,-17,-16,79,79,]),'GREATER_THAN_OR_EQUALS':([47,57,68,91,97,115,],[-16,80,-17,-16,80,80,]),'LESS_THAN':([47,57,68,91,97,115,],[-16,81,-17,-16,81,81,]),'LESS_THAN_OR_EQUALS':([47,57,68,91,97,115,],[-16,82,-17,-16,82,82,]),'BY':([53,71,],[73,93,]),'AND':([56,68,91,98,99,101,117,],[75,-17,-16,-37,-38,-40,-39,]),'NUMBER':([76,77,78,79,80,81,82,118,],[101,-41,-42,-43,-44,-45,-46,120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'QUERY':([0,95,],[1,110,]),'SELECT_NT':([0,95,],[2,2,]),'FROM_NT':([2,],[4,]),'COLUMNS':([3,6,29,45,64,73,93,],[7,27,46,65,87,94,108,]),'COLUMN':([3,6,26,29,35,45,64,73,93,],[8,28,44,8,55,8,8,8,8,]),'COLUMN_WIHTOUT_ALIAS':([3,6,26,29,33,35,45,64,73,75,76,83,84,85,93,105,],[9,9,9,9,50,57,9,9,9,97,98,97,97,97,9,97,]),'FUNCTION':([3,6,26,29,35,45,64,73,76,93,109,],[11,11,11,11,11,11,11,11,99,11,115,]),'VALID_FUNCTIONS':([3,6,26,29,35,45,64,73,76,93,109,],[12,12,12,12,12,12,12,12,12,12,12,]),'JOIN_NT':([4,],[16,]),'VALID_JOINS':([4,18,],[17,36,]),'VALID_JOIN':([4,18,],[18,18,]),'TABLES':([5,41,],[23,62,]),'TABLE':([5,37,38,39,41,61,],[24,58,59,60,24,86,]),'ALIAS':([11,47,],[31,66,]),'WHERE_NT':([16,],[34,]),'GROUP_BY_NT':([34,],[52,]),'COMPARATIONS':([35,75,],[54,96,]),'CONDITION':([35,75,83,84,85,105,],[56,56,102,103,104,112,]),'ORDER_BY_NT':([52,],[70,]),'BY_NT':([53,],[72,]),'COMPARATION_OPERATOR':([57,97,115,],[76,76,118,]),'STRINGS':([67,89,],[90,106,]),'BY_NT_WITHOUT_HAVING':([71,],[92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> QUERY","S'",1,None,None,None),
  ('QUERY -> SELECT_NT FROM_NT JOIN_NT WHERE_NT GROUP_BY_NT ORDER_BY_NT','QUERY',6,'p_QUERY_AXIOM','grupo04.py',102),
  ('SELECT_NT -> SELECT DISTINCT COLUMNS','SELECT_NT',3,'p_SELECT','grupo04.py',105),
  ('SELECT_NT -> SELECT COLUMNS','SELECT_NT',2,'p_SELECT','grupo04.py',106),
  ('COLUMNS -> COLUMN COMMA COLUMNS','COLUMNS',3,'p_COLUMNS','grupo04.py',109),
  ('COLUMNS -> DISTINCT COLUMN COMMA COLUMNS','COLUMNS',4,'p_COLUMNS','grupo04.py',110),
  ('COLUMNS -> COLUMN','COLUMNS',1,'p_COLUMNS','grupo04.py',111),
  ('ALIAS -> AS QUOTE STRING QUOTE','ALIAS',4,'p_ALIAS','grupo04.py',114),
  ('ALIAS -> AS QUOTE STRING STRINGS QUOTE','ALIAS',5,'p_ALIAS','grupo04.py',115),
  ('ALIAS -> AS STRING','ALIAS',2,'p_ALIAS','grupo04.py',116),
  ('STRINGS -> STRING STRINGS','STRINGS',2,'p_STRINGS','grupo04.py',119),
  ('STRINGS -> STRING','STRINGS',1,'p_STRINGS','grupo04.py',120),
  ('COLUMN -> COLUMN_WIHTOUT_ALIAS','COLUMN',1,'p_COLUMN','grupo04.py',123),
  ('COLUMN -> STRING DOT STRING ALIAS','COLUMN',4,'p_COLUMN','grupo04.py',124),
  ('COLUMN -> FUNCTION ALIAS','COLUMN',2,'p_COLUMN','grupo04.py',125),
  ('COLUMN -> FUNCTION','COLUMN',1,'p_COLUMN','grupo04.py',126),
  ('COLUMN_WIHTOUT_ALIAS -> STRING DOT STRING','COLUMN_WIHTOUT_ALIAS',3,'p_COLUMN_WIHTOUT_ALIAS','grupo04.py',133),
  ('FUNCTION -> VALID_FUNCTIONS LEFT_PARENTHESIS COLUMN_WIHTOUT_ALIAS RIGHT_PARENTHESIS','FUNCTION',4,'p_FUNCTION','grupo04.py',140),
  ('VALID_FUNCTIONS -> COUNT','VALID_FUNCTIONS',1,'p_VALID_FUNCTIONS','grupo04.py',143),
  ('VALID_FUNCTIONS -> MAX','VALID_FUNCTIONS',1,'p_VALID_FUNCTIONS','grupo04.py',144),
  ('VALID_FUNCTIONS -> MIN','VALID_FUNCTIONS',1,'p_VALID_FUNCTIONS','grupo04.py',145),
  ('FROM_NT -> FROM TABLES','FROM_NT',2,'p_FROM','grupo04.py',148),
  ('TABLES -> TABLE','TABLES',1,'p_TABLES','grupo04.py',151),
  ('TABLES -> TABLE COMMA TABLES','TABLES',3,'p_TABLES','grupo04.py',152),
  ('TABLE -> STRING STRING','TABLE',2,'p_TABLE','grupo04.py',155),
  ('TABLE -> STRING AS STRING','TABLE',3,'p_TABLE','grupo04.py',156),
  ('TABLE -> STRING','TABLE',1,'p_TABLE','grupo04.py',157),
  ('JOIN_NT -> VALID_JOINS','JOIN_NT',1,'p_JOIN_NT','grupo04.py',169),
  ('JOIN_NT -> <empty>','JOIN_NT',0,'p_JOIN_NT','grupo04.py',170),
  ('VALID_JOINS -> VALID_JOIN','VALID_JOINS',1,'p_VALID_JOINS','grupo04.py',173),
  ('VALID_JOINS -> VALID_JOIN VALID_JOINS','VALID_JOINS',2,'p_VALID_JOINS','grupo04.py',174),
  ('VALID_JOIN -> INNER JOIN TABLE ON CONDITION','VALID_JOIN',5,'p_VALID_JOIN','grupo04.py',177),
  ('VALID_JOIN -> LEFT JOIN TABLE ON CONDITION','VALID_JOIN',5,'p_VALID_JOIN','grupo04.py',178),
  ('VALID_JOIN -> RIGHT JOIN TABLE ON CONDITION','VALID_JOIN',5,'p_VALID_JOIN','grupo04.py',179),
  ('VALID_JOIN -> FULL OUTER JOIN TABLE ON CONDITION','VALID_JOIN',6,'p_VALID_JOIN','grupo04.py',180),
  ('CONDITIONS -> CONDITION','CONDITIONS',1,'p_CONDITIONS','grupo04.py',183),
  ('CONDITIONS -> CONTIDION CONDITIONS','CONDITIONS',2,'p_CONDITIONS','grupo04.py',184),
  ('CONDITION -> COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR COLUMN_WIHTOUT_ALIAS','CONDITION',3,'p_CONDITION','grupo04.py',187),
  ('CONDITION -> COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR FUNCTION','CONDITION',3,'p_CONDITION','grupo04.py',188),
  ('CONDITION -> COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR QUOTE STRING QUOTE','CONDITION',5,'p_CONDITION','grupo04.py',189),
  ('CONDITION -> COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR NUMBER','CONDITION',3,'p_CONDITION','grupo04.py',190),
  ('COMPARATION_OPERATOR -> EQUAL','COMPARATION_OPERATOR',1,'p_COMPARATION_OPERATOR','grupo04.py',193),
  ('COMPARATION_OPERATOR -> NOT_EQUAL','COMPARATION_OPERATOR',1,'p_COMPARATION_OPERATOR','grupo04.py',194),
  ('COMPARATION_OPERATOR -> GREATER_THAN','COMPARATION_OPERATOR',1,'p_COMPARATION_OPERATOR','grupo04.py',195),
  ('COMPARATION_OPERATOR -> GREATER_THAN_OR_EQUALS','COMPARATION_OPERATOR',1,'p_COMPARATION_OPERATOR','grupo04.py',196),
  ('COMPARATION_OPERATOR -> LESS_THAN','COMPARATION_OPERATOR',1,'p_COMPARATION_OPERATOR','grupo04.py',197),
  ('COMPARATION_OPERATOR -> LESS_THAN_OR_EQUALS','COMPARATION_OPERATOR',1,'p_COMPARATION_OPERATOR','grupo04.py',198),
  ('WHERE_NT -> WHERE COMPARATIONS','WHERE_NT',2,'p_WHERE_NT','grupo04.py',201),
  ('WHERE_NT -> WHERE COLUMN IN LEFT_PARENTHESIS QUERY RIGHT_PARENTHESIS','WHERE_NT',6,'p_WHERE_NT','grupo04.py',202),
  ('WHERE_NT -> <empty>','WHERE_NT',0,'p_WHERE_NT','grupo04.py',203),
  ('COMPARATIONS -> CONDITION','COMPARATIONS',1,'p_COMPARATIONS','grupo04.py',206),
  ('COMPARATIONS -> CONDITION AND COMPARATIONS','COMPARATIONS',3,'p_COMPARATIONS','grupo04.py',207),
  ('GROUP_BY_NT -> GROUP BY_NT','GROUP_BY_NT',2,'p_GROUP_BY_NT','grupo04.py',210),
  ('GROUP_BY_NT -> <empty>','GROUP_BY_NT',0,'p_GROUP_BY_NT','grupo04.py',211),
  ('BY_NT -> BY COLUMNS','BY_NT',2,'p_BY_NT','grupo04.py',214),
  ('BY_NT -> BY COLUMNS HAVING FUNCTION COMPARATION_OPERATOR STRING','BY_NT',6,'p_BY_NT','grupo04.py',215),
  ('BY_NT -> BY COLUMNS HAVING FUNCTION COMPARATION_OPERATOR NUMBER','BY_NT',6,'p_BY_NT','grupo04.py',216),
  ('ORDER_BY_NT -> ORDER BY_NT_WITHOUT_HAVING','ORDER_BY_NT',2,'p_ORDER_BY_NT','grupo04.py',219),
  ('ORDER_BY_NT -> <empty>','ORDER_BY_NT',0,'p_ORDER_BY_NT','grupo04.py',220),
  ('BY_NT_WITHOUT_HAVING -> BY COLUMNS DESC','BY_NT_WITHOUT_HAVING',3,'p_BY_NT_WITHOUT_HAVING','grupo04.py',223),
  ('BY_NT_WITHOUT_HAVING -> BY COLUMNS ASC','BY_NT_WITHOUT_HAVING',3,'p_BY_NT_WITHOUT_HAVING','grupo04.py',224),
  ('BY_NT_WITHOUT_HAVING -> BY COLUMNS','BY_NT_WITHOUT_HAVING',2,'p_BY_NT_WITHOUT_HAVING','grupo04.py',225),
]
