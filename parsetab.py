
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVnonassocUMINUSCOLON COMMA DIV DOUBLEQUOTE ELSE ELSE_IF EQ EQUAL FLOAT FOR GT ID IF INCREMENT INT LBRACE LBRACKET LPAREN LT MAIN MINUS NEQ NUMBER PERIOD PLUS POINTER PRINT QUOTE RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES VOIDexpr : ID EQUAL arith_exprexpr : bool_exprbool_expr : arith_exprbool_expr : bool_expr EQ arith_exprbool_expr : bool_expr NEQ arith_exprbool_expr : bool_expr GT arith_exprbool_expr : bool_expr LT arith_exprarith_expr : arith_expr PLUS arith_exprarith_expr : arith_expr MINUS arith_exprarith_expr : MINUS arith_expr %prec UMINUSarith_expr : arith_expr TIMES arith_expr\n            | arith_expr DIV arith_exprarith_expr : NUMBERarith_expr : LPAREN arith_expr RPAREN'
    
_lr_action_items = {'ID':([0,],[2,]),'MINUS':([0,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,],[5,10,5,-13,5,5,5,5,5,5,5,5,5,5,-10,10,10,-8,-9,-11,-12,10,10,10,10,-14,]),'NUMBER':([0,5,7,8,9,10,11,12,13,14,15,16,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'LPAREN':([0,5,7,8,9,10,11,12,13,14,15,16,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'$end':([1,3,4,6,17,19,20,21,22,23,24,25,26,27,28,],[0,-3,-2,-13,-10,-1,-8,-9,-11,-12,-4,-5,-6,-7,-14,]),'EQUAL':([2,],[8,]),'EQ':([3,4,6,17,20,21,22,23,24,25,26,27,28,],[-3,13,-13,-10,-8,-9,-11,-12,-4,-5,-6,-7,-14,]),'NEQ':([3,4,6,17,20,21,22,23,24,25,26,27,28,],[-3,14,-13,-10,-8,-9,-11,-12,-4,-5,-6,-7,-14,]),'GT':([3,4,6,17,20,21,22,23,24,25,26,27,28,],[-3,15,-13,-10,-8,-9,-11,-12,-4,-5,-6,-7,-14,]),'LT':([3,4,6,17,20,21,22,23,24,25,26,27,28,],[-3,16,-13,-10,-8,-9,-11,-12,-4,-5,-6,-7,-14,]),'PLUS':([3,6,17,18,19,20,21,22,23,24,25,26,27,28,],[9,-13,-10,9,9,-8,-9,-11,-12,9,9,9,9,-14,]),'TIMES':([3,6,17,18,19,20,21,22,23,24,25,26,27,28,],[11,-13,-10,11,11,11,11,-11,-12,11,11,11,11,-14,]),'DIV':([3,6,17,18,19,20,21,22,23,24,25,26,27,28,],[12,-13,-10,12,12,12,12,-11,-12,12,12,12,12,-14,]),'RPAREN':([6,17,18,20,21,22,23,28,],[-13,-10,28,-8,-9,-11,-12,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,],[1,]),'arith_expr':([0,5,7,8,9,10,11,12,13,14,15,16,],[3,17,18,19,20,21,22,23,24,25,26,27,]),'bool_expr':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> ID EQUAL arith_expr','expr',3,'p_expr_assign','pycparser.py',17),
  ('expr -> bool_expr','expr',1,'p_expr_bool','pycparser.py',21),
  ('bool_expr -> arith_expr','bool_expr',1,'p_compare_expr_arith','pycparser.py',25),
  ('bool_expr -> bool_expr EQ arith_expr','bool_expr',3,'p_compare_expr_eq','pycparser.py',29),
  ('bool_expr -> bool_expr NEQ arith_expr','bool_expr',3,'p_compare_expr_neq','pycparser.py',33),
  ('bool_expr -> bool_expr GT arith_expr','bool_expr',3,'p_compare_expr_gt','pycparser.py',37),
  ('bool_expr -> bool_expr LT arith_expr','bool_expr',3,'p_compare_expr_lt','pycparser.py',41),
  ('arith_expr -> arith_expr PLUS arith_expr','arith_expr',3,'p_add','pycparser.py',53),
  ('arith_expr -> arith_expr MINUS arith_expr','arith_expr',3,'p_sub','pycparser.py',61),
  ('arith_expr -> MINUS arith_expr','arith_expr',2,'p_expr2uminus','pycparser.py',69),
  ('arith_expr -> arith_expr TIMES arith_expr','arith_expr',3,'p_mult_div','pycparser.py',73),
  ('arith_expr -> arith_expr DIV arith_expr','arith_expr',3,'p_mult_div','pycparser.py',74),
  ('arith_expr -> NUMBER','arith_expr',1,'p_expr2NUM','pycparser.py',97),
  ('arith_expr -> LPAREN arith_expr RPAREN','arith_expr',3,'p_parens','pycparser.py',105),
]
