
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "right=left+-left*rightsimetricoEM ESCREVE FAZER FIM INSTRUCAO NUM PARA PARAFIM SEPARADOR STRING VAR VARID initial : comando\n                    | assign\n                    | declare_var comando : ESCREVE lista_strings FIMlista_strings : lista_strings SEPARADOR E\n                         | lista_strings SEPARADOR NUM\n                         | lista_strings SEPARADOR STRING E : E '+' E  \n                | E '-' E \n                | E '*' E      lista_strings : STRING\n                         | NUM\n                         | E E : '-' E   %prec simetrico  E : '(' E ')'  E :  NUM   E :  VARID   declare_var : VAR VARID FIM assign : VAR VARID '=' E FIM"
    
_lr_action_items = {'ESCREVE':([0,],[5,]),'VAR':([0,],[6,]),'$end':([1,2,3,4,15,24,33,],[0,-1,-2,-3,-4,-18,-19,]),'STRING':([5,16,],[10,27,]),'NUM':([5,11,12,16,17,18,19,23,],[9,21,21,26,21,21,21,21,]),'-':([5,8,9,11,12,13,16,17,18,19,20,21,22,23,25,26,28,29,30,31,32,],[11,18,-16,11,11,-17,11,11,11,11,-14,-16,18,11,18,-16,-8,-9,-10,-15,18,]),'(':([5,11,12,16,17,18,19,23,],[12,12,12,12,12,12,12,12,]),'VARID':([5,6,11,12,16,17,18,19,23,],[13,14,13,13,13,13,13,13,13,]),'FIM':([7,8,9,10,13,14,20,21,25,26,27,28,29,30,31,32,],[15,-13,-12,-11,-17,24,-14,-16,-5,-6,-7,-8,-9,-10,-15,33,]),'SEPARADOR':([7,8,9,10,13,20,21,25,26,27,28,29,30,31,],[16,-13,-12,-11,-17,-14,-16,-5,-6,-7,-8,-9,-10,-15,]),'+':([8,9,13,20,21,22,25,26,28,29,30,31,32,],[17,-16,-17,-14,-16,17,17,-16,-8,-9,-10,-15,17,]),'*':([8,9,13,20,21,22,25,26,28,29,30,31,32,],[19,-16,-17,-14,-16,19,19,-16,19,19,-10,-15,19,]),')':([13,20,21,22,28,29,30,31,],[-17,-14,-16,31,-8,-9,-10,-15,]),'=':([14,],[23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'initial':([0,],[1,]),'comando':([0,],[2,]),'assign':([0,],[3,]),'declare_var':([0,],[4,]),'lista_strings':([5,],[7,]),'E':([5,11,12,16,17,18,19,23,],[8,20,22,25,28,29,30,32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> initial","S'",1,None,None,None),
  ('initial -> comando','initial',1,'p_initial','EscreveGrammar.py',31),
  ('initial -> assign','initial',1,'p_initial','EscreveGrammar.py',32),
  ('initial -> declare_var','initial',1,'p_initial','EscreveGrammar.py',33),
  ('comando -> ESCREVE lista_strings FIM','comando',3,'p_comando_escreve','EscreveGrammar.py',56),
  ('lista_strings -> lista_strings SEPARADOR E','lista_strings',3,'p_lista_strings_multiple','EscreveGrammar.py',63),
  ('lista_strings -> lista_strings SEPARADOR NUM','lista_strings',3,'p_lista_strings_multiple','EscreveGrammar.py',64),
  ('lista_strings -> lista_strings SEPARADOR STRING','lista_strings',3,'p_lista_strings_multiple','EscreveGrammar.py',65),
  ('E -> E + E','E',3,'p_expr_op','EscreveGrammar.py',70),
  ('E -> E - E','E',3,'p_expr_op','EscreveGrammar.py',71),
  ('E -> E * E','E',3,'p_expr_op','EscreveGrammar.py',72),
  ('lista_strings -> STRING','lista_strings',1,'p_lista_strings_single','EscreveGrammar.py',84),
  ('lista_strings -> NUM','lista_strings',1,'p_lista_strings_single','EscreveGrammar.py',85),
  ('lista_strings -> E','lista_strings',1,'p_lista_strings_single','EscreveGrammar.py',86),
  ('E -> - E','E',2,'p_expr_sinalmenos','EscreveGrammar.py',90),
  ('E -> ( E )','E',3,'p_expr_pare','EscreveGrammar.py',94),
  ('E -> NUM','E',1,'p_expr_num','EscreveGrammar.py',100),
  ('E -> VARID','E',1,'p_expr_var','EscreveGrammar.py',104),
  ('declare_var -> VAR VARID FIM','declare_var',3,'p_create_var','EscreveGrammar.py',114),
  ('assign -> VAR VARID = E FIM','assign',5,'p_assign_var','EscreveGrammar.py',119),
]
