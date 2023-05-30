
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "right=left+-left*rightsimetricoEM ESCREVE FAZER FIM FIMFUNC FIMPARA FUNC NUM PARA RANGE RETURN STRING VAR VARID init : block block : block instruction  block : instruction instruction : assign \n                        | declare_var\n                        | print\n                        | function\n                        | return\n                        | func_call print : ESCREVE E FIM\n                  | ESCREVE STRING FIM E : E '+' E  \n                | E '-' E \n                | E '*' E       E : '-' E   %prec simetrico  E : '(' E ')'  E :  NUM   E :  VARID   instruction : PARA VARID EM RANGE FAZER block FIMPARA FIM  declare_var : VAR VARID FIM assign : VAR VARID '=' E FIM return : RETURN E FIM function : FUNC VARID '(' params ')' block FIMFUNC params : params ','  VARID  params : VARID func_call : VARID '(' arguments ')' FIM  arguments : arguments ',' E   arguments : E"
    
_lr_action_items = {'PARA':([0,2,3,4,5,6,7,8,9,16,32,33,37,41,52,53,55,56,58,59,62,63,],[10,10,-3,-4,-5,-6,-7,-8,-9,-2,-20,-10,-11,-22,10,-26,-21,10,10,10,-23,-19,]),'VAR':([0,2,3,4,5,6,7,8,9,16,32,33,37,41,52,53,55,56,58,59,62,63,],[12,12,-3,-4,-5,-6,-7,-8,-9,-2,-20,-10,-11,-22,12,-26,-21,12,12,12,-23,-19,]),'ESCREVE':([0,2,3,4,5,6,7,8,9,16,32,33,37,41,52,53,55,56,58,59,62,63,],[13,13,-3,-4,-5,-6,-7,-8,-9,-2,-20,-10,-11,-22,13,-26,-21,13,13,13,-23,-19,]),'FUNC':([0,2,3,4,5,6,7,8,9,16,32,33,37,41,52,53,55,56,58,59,62,63,],[14,14,-3,-4,-5,-6,-7,-8,-9,-2,-20,-10,-11,-22,14,-26,-21,14,14,14,-23,-19,]),'RETURN':([0,2,3,4,5,6,7,8,9,16,32,33,37,41,52,53,55,56,58,59,62,63,],[15,15,-3,-4,-5,-6,-7,-8,-9,-2,-20,-10,-11,-22,15,-26,-21,15,15,15,-23,-19,]),'VARID':([0,2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,22,23,31,32,33,34,35,36,37,40,41,44,52,53,55,56,57,58,59,62,63,],[11,11,-3,-4,-5,-6,-7,-8,-9,17,19,25,26,25,-2,25,25,25,25,-20,-10,25,25,25,-11,50,-22,25,11,-26,-21,11,60,11,11,-23,-19,]),'$end':([1,2,3,4,5,6,7,8,9,16,32,33,37,41,53,55,62,63,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-2,-20,-10,-11,-22,-26,-21,-23,-19,]),'FIMPARA':([3,4,5,6,7,8,9,16,32,33,37,41,53,55,58,62,63,],[-3,-4,-5,-6,-7,-8,-9,-2,-20,-10,-11,-22,-26,-21,61,-23,-19,]),'FIMFUNC':([3,4,5,6,7,8,9,16,32,33,37,41,53,55,59,62,63,],[-3,-4,-5,-6,-7,-8,-9,-2,-20,-10,-11,-22,-26,-21,62,-23,-19,]),'(':([11,13,15,18,22,23,26,31,34,35,36,44,],[18,23,23,23,23,23,40,23,23,23,23,23,]),'STRING':([13,],[21,]),'-':([13,15,18,20,22,23,24,25,27,30,31,34,35,36,38,39,44,45,46,47,48,49,54,],[22,22,22,35,22,22,-17,-18,35,35,22,22,22,22,-15,35,22,35,-12,-13,-14,-16,35,]),'NUM':([13,15,18,22,23,31,34,35,36,44,],[24,24,24,24,24,24,24,24,24,24,]),'EM':([17,],[28,]),'=':([19,],[31,]),'FIM':([19,20,21,24,25,27,38,43,45,46,47,48,49,61,],[32,33,37,-17,-18,41,-15,53,55,-12,-13,-14,-16,63,]),'+':([20,24,25,27,30,38,39,45,46,47,48,49,54,],[34,-17,-18,34,34,-15,34,34,-12,-13,-14,-16,34,]),'*':([20,24,25,27,30,38,39,45,46,47,48,49,54,],[36,-17,-18,36,36,-15,36,36,36,36,-14,-16,36,]),')':([24,25,29,30,38,39,46,47,48,49,50,51,54,60,],[-17,-18,43,-28,-15,49,-12,-13,-14,-16,-25,56,-27,-24,]),',':([24,25,29,30,38,46,47,48,49,50,51,54,60,],[-17,-18,44,-28,-15,-12,-13,-14,-16,-25,57,-27,-24,]),'RANGE':([28,],[42,]),'FAZER':([42,],[52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'block':([0,52,56,],[2,58,59,]),'instruction':([0,2,52,56,58,59,],[3,16,3,3,16,16,]),'assign':([0,2,52,56,58,59,],[4,4,4,4,4,4,]),'declare_var':([0,2,52,56,58,59,],[5,5,5,5,5,5,]),'print':([0,2,52,56,58,59,],[6,6,6,6,6,6,]),'function':([0,2,52,56,58,59,],[7,7,7,7,7,7,]),'return':([0,2,52,56,58,59,],[8,8,8,8,8,8,]),'func_call':([0,2,52,56,58,59,],[9,9,9,9,9,9,]),'E':([13,15,18,22,23,31,34,35,36,44,],[20,27,30,38,39,45,46,47,48,54,]),'arguments':([18,],[29,]),'params':([40,],[51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> block','init',1,'p_init','EscreveGrammar.py',34),
  ('block -> block instruction','block',2,'p_block','EscreveGrammar.py',39),
  ('block -> instruction','block',1,'p_block_end','EscreveGrammar.py',45),
  ('instruction -> assign','instruction',1,'p_instruction','EscreveGrammar.py',49),
  ('instruction -> declare_var','instruction',1,'p_instruction','EscreveGrammar.py',50),
  ('instruction -> print','instruction',1,'p_instruction','EscreveGrammar.py',51),
  ('instruction -> function','instruction',1,'p_instruction','EscreveGrammar.py',52),
  ('instruction -> return','instruction',1,'p_instruction','EscreveGrammar.py',53),
  ('instruction -> func_call','instruction',1,'p_instruction','EscreveGrammar.py',54),
  ('print -> ESCREVE E FIM','print',3,'p_print','EscreveGrammar.py',58),
  ('print -> ESCREVE STRING FIM','print',3,'p_print','EscreveGrammar.py',59),
  ('E -> E + E','E',3,'p_expr_op','EscreveGrammar.py',63),
  ('E -> E - E','E',3,'p_expr_op','EscreveGrammar.py',64),
  ('E -> E * E','E',3,'p_expr_op','EscreveGrammar.py',65),
  ('E -> - E','E',2,'p_expr_sinalmenos','EscreveGrammar.py',69),
  ('E -> ( E )','E',3,'p_expr_pare','EscreveGrammar.py',73),
  ('E -> NUM','E',1,'p_expr_num','EscreveGrammar.py',77),
  ('E -> VARID','E',1,'p_expr_var','EscreveGrammar.py',81),
  ('instruction -> PARA VARID EM RANGE FAZER block FIMPARA FIM','instruction',8,'p_ciclos','EscreveGrammar.py',85),
  ('declare_var -> VAR VARID FIM','declare_var',3,'p_create_var','EscreveGrammar.py',89),
  ('assign -> VAR VARID = E FIM','assign',5,'p_assign_var','EscreveGrammar.py',93),
  ('return -> RETURN E FIM','return',3,'p_return','EscreveGrammar.py',98),
  ('function -> FUNC VARID ( params ) block FIMFUNC','function',7,'p_func','EscreveGrammar.py',102),
  ('params -> params , VARID','params',3,'p_params','EscreveGrammar.py',106),
  ('params -> VARID','params',1,'p_param_end','EscreveGrammar.py',112),
  ('func_call -> VARID ( arguments ) FIM','func_call',5,'p_func_call','EscreveGrammar.py',116),
  ('arguments -> arguments , E','arguments',3,'p_arguments','EscreveGrammar.py',120),
  ('arguments -> E','arguments',1,'p_arguments_end','EscreveGrammar.py',126),
]
