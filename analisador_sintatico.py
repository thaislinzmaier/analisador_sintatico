DEBUG = {'lexico': False, 'pilha': False, 'token': True}

# Definindo os tokens
TKId = 1
TKVoid = 2
TKInt = 3
TKFloat = 4
TKVirgula = 5
TKDoisPontos = 6
TKAbrePar = 7
TKFechaPar = 8
TKAtrib = 9
TKPontoEVirgula = 10
TKAbreChaves = 11
TKFechaChaves = 12
TKMais = 13
TKDuploMais = 14
TKProd = 15
TKChar = 16
TKMenos = 17
TKAbreColchete = 18
TKFechaColchete = 19
TKAtribMais = 20
TKDouble = 21
TKCteInt = 22
TKElse = 23
TKIf = 23
TKFimArquivo = 24
TKLong = 25
TKUnsigned = 26
TKPointer = 27
TKArray = 28  # ERRO
TKFor = 28
TKDiv = 29
TKPerc = 30
TKMaior = 31
TKMenor = 32
TKIgual = 33
TKDiferente = 34
TKMenorIgual = 35
TKMaiorIgual = 36
TKAnd = 37
TKPipe = 38
TKCirc = 39
TKShiftRight = 40
TKShiftLeft = 41
TKTil = 42
TKAndAnd = 43
TKPipePipe = 44
TKExc = 45
TKMenosIgual = 46
TKAstIgual = 47
TKDivIgual = 48
TKPercIgual = 49
TKShiftRightIgual = 50
TKShiftLeftIgual = 51
TKWhile = 52
TKDo = 53
TKDuploMenos = 54


# Dicionário para mapear números de tokens para seus nomes correspondentes
token_names = {  # TODO: Transformar isso em um enum
    TKId: "TKId",
    TKVoid: "TKVoid",
    TKInt: "TKInt",
    TKFloat: "TKFloat",
    TKChar: "TKChar",
    TKDouble: "TKDouble",
    TKElse: "TKElse",
    TKIf: "TKIf",
    TKLong: "TKLong",
    TKUnsigned: "TKUnsigned",
    TKFimArquivo: "TKFimArquivo",
    TKCteInt: "TKCteInt",
    TKAtrib: "TKAtrib",
    TKMais: "TKMais",
    TKDuploMais: "TKDuploMais",
    TKAtribMais: "TKAtribMais",
    TKProd: "TKProd",
    TKAbreColchete: "TKAbreColchete",
    TKFechaColchete: "TKFechaColchete",
    TKAbrePar: "TKAbrePar",
    TKFechaPar: "TKFechaPar",
    TKAbreChaves: "TKAbreChaves",
    TKFechaChaves: "TKFechaChaves",
    TKVirgula: "TKVirgula",
    TKPontoEVirgula: "TKPontoEVirgula",
    TKDoisPontos: "TKDoisPontos",
    TKMenos: "TKDuploMais",
    TKPointer: "TKPointer",
    TKArray: "TKArray",
    TKFor: "TKFor",
    TKDiv: "TKDiv",
    TKPerc: "TKPerc",
    TKMaior: "TKMaior",
    TKMenor: "TKMenor",
    TKIgual: "TKIgual",
    TKDiferente: "TKDiferente",
    TKMenorIgual: "TKMenorIgual",
    TKMaiorIgual: "TKMaiorIgual",
    TKAnd: "TKAnd",
    TKPipe: "TKPipe",
    TKCirc: "TKCirc",
    TKShiftRight: "TKShiftRight",
    TKShiftLeft: "TKShiftLeft",
    TKTil: "TKTil",
    TKAndAnd: "TKAndAnd",
    TKPipePipe: "TkPipePipe",
    TKExc: "TKExc",
    TKMenosIgual: "TKMenosIgual",
    TKAstIgual: "TKAstIgual",
    TKDivIgual: "TKDivIgual",
    TKPercIgual: "TKPercIgual",
    TKShiftRightIgual: "TKShiftRightIgual",
    TKShiftLeftIgual: "TKShiftLeftIgual",
    TKWhile: "TKWhile",
    TKDo: "TKDo",
    TKDuploMenos: "TKDuploMenos",
}


curr_position = 0
token = 0
lexico = ""
arquivo_entrada = None
current_char = ''  # último caractere lido do arquivo


lista_palavras_reservadas = {
    "void": TKVoid,
    "int": TKInt,
    "float": TKFloat,
    "char": TKChar,
    "double": TKDouble,
    "else": TKElse,
    "while": TKWhile,
    "do": TKDo,
    "for": TKFor,
    "if": TKIf,
    "long": TKLong,
    "unsigned": TKUnsigned,
    "fimtabela": TKId,
}


def palavra_reservada(lex):
    return lista_palavras_reservadas.get(lex, TKId)


def get_nome_token(tk):
    return token_names.get(tk, 'Desconhecido')


def print_token_after(func):
    def wrapper():
        func()
        if DEBUG['token']:
            print(f"Token: {get_nome_token(token)}, lex: {lexico}")

    return wrapper


@print_token_after
def get_next_token():
    global token, current_char, lexico, curr_position
    estado = 0
    fim = False
    lexico = ''
    while not fim:
        lexico += current_char

        if DEBUG['lexico']:
            print(f'lexico: {lexico}')

        if estado == 0:
            if current_char.isalpha() or current_char == '_':
                proxC()
                estado = 1
            elif current_char.isdigit():
                while current_char.isdigit():
                    proxC()
                token = TKCteInt
                return
            elif current_char == '=':
                proxC()
                if current_char == '=':
                    lexico += current_char
                    proxC()
                    token = TKIgual
                    return
                token = TKAtrib
                return
            elif current_char == '+':
                proxC()
                if current_char == '+':
                    lexico += current_char
                    proxC()
                    token = TKDuploMais
                    return
                elif current_char == '=':
                    lexico += current_char
                    proxC()
                    token = TKAtribMais
                    return
                else:
                    token = TKMais
                    return
            elif current_char == '-':
                proxC()
                if current_char == '-':
                    lexico += current_char
                    proxC()
                    token = TKDuploMenos
                    return
                elif current_char == '=':
                    lexico += current_char
                    proxC()
                    token = TKMenosIgual
                    return
                else:
                    token = TKMenos
                    return
            elif current_char == '*':
                proxC()
                if current_char.isalpha():
                    token = TKPointer
                elif current_char == '=':
                    token = TKAstIgual
                else:
                    token = TKProd
                proxC()
                return
            elif current_char == '/':
                proxC()
                if current_char == '=':
                    lexico += current_char
                    proxC()
                    token = TKDivIgual
                    return
                else:
                    token = TKDiv
                    return
            elif current_char == '%':
                proxC()
                if current_char == '=':
                    lexico += current_char
                    proxC()
                    token = TKPercIgual
                    return
                else:
                    token = TKPerc
                    return
            elif current_char == '!':
                proxC()
                if current_char == '=':
                    lexico += current_char
                    proxC()
                    token = TKDiferente
                    return
                else:
                    token = TKExc
                    return
            elif current_char == '&':
                proxC()
                if current_char == '&':
                    lexico += current_char
                    proxC()
                    token = TKAndAnd
                    return
                else:
                    token = TKAnd
                    return
            elif current_char == '|':
                proxC()
                if current_char == '|':
                    lexico += current_char
                    proxC()
                    token = TKPipePipe
                    return
                else:
                    token = TKPipe
                    return
            elif current_char == '>':
                proxC()
                if current_char == '=':
                    lexico += current_char
                    proxC()
                    token = TKMaiorIgual
                    return
                if current_char == '>':
                    proxC()
                    if current_char == '=':
                        lexico += current_char
                        proxC()
                        token = TKShiftRightIgual
                        return
                    else:
                        token = TKShiftRight
                        return
                else:
                    token = TKMaior
                    return
            elif current_char == '<':
                proxC()
                if current_char == '=':
                    lexico += current_char
                    proxC()
                    token = TKMenorIgual
                    return
                if current_char == '<':
                    proxC()
                    if current_char == '=':
                        lexico += current_char
                        proxC()
                        token = TKShiftLeftIgual
                        return
                    else:
                        token = TKShiftLeft
                        return
                else:
                    token = TKMenor
                    return
            elif current_char == '[':
                proxC()
                token = TKAbreColchete
                return
            elif current_char == ']':
                proxC()
                token = TKFechaColchete
                return
            elif current_char == '(':
                proxC()
                token = TKAbrePar
                return
            elif current_char == ')':
                proxC()
                token = TKFechaPar
                return
            elif current_char == '{':
                proxC()
                token = TKAbreChaves
                return
            elif current_char == '}':
                proxC()
                token = TKFechaChaves
                return
            elif current_char == ',':
                proxC()
                token = TKVirgula
                return
            elif current_char == '^':
                proxC()
                token = TKCirc
                return
            elif current_char == '~':
                proxC()
                token = TKTil
                return
            elif current_char == ';':
                proxC()
                token = TKPontoEVirgula
                return
            elif current_char == ':':
                proxC()
                token = TKDoisPontos
                return
            elif current_char == '':
                token = TKFimArquivo
                fim = True
                return
            elif current_char in ' \n\t\r':
                lexico = lexico[:-1]
                proxC()
            else:
                print(
                    f"Erro léxico: encontrou o caractere {current_char} ({ord(current_char)})"
                )
                while current_char != '\n':
                    proxC()
        elif estado == 1:
            if current_char.isalnum() or current_char == '_':
                proxC()
            else:
                lexico = lexico[:-1]
                token = palavra_reservada(lexico)
                return


pilha = []


def empilha():
    global current_char, pilha, token
    config = {'arqin_pos': arquivo_entrada.tell(), 'c': current_char, 'tk': token}
    pilha.append(config)
    if DEBUG['pilha']:
        print(f'/\ Empilhando {config}')


def desempilha_sem_restaurar():
    return pilha.pop()


def desempilha():
    global current_char, token
    config = desempilha_sem_restaurar()
    if DEBUG['pilha']:
        print(f'\/ Restaurando {config}')
    arquivo_entrada.seek(config['arqin_pos'])
    current_char = config['c']
    token = config['tk']


def volta_estado_se_der_errado(callable_bool):
    empilha()
    resultado = callable_bool()
    if resultado:
        desempilha_sem_restaurar()
    else:
        desempilha()
    return resultado


def se_eh(*tokens):
    '''
    Testa se eh o token e já consome
    '''
    if era_algum := token in tokens:
        get_next_token()
    return era_algum


def possivelmente_vazio(func):
    def wrapper_func():
        volta_estado_se_der_errado(func)
        return True

    return wrapper_func


def proxC():
    global current_char
    current_char = arquivo_entrada.read(1)
    if not current_char:
        current_char = ''
    # print(f"Caractere lido: '{c}'")


def compound_statement():  # Medo
    '''
    compound_statement
        : '{' '}'
        | '{' declaration_list '}'
        | '{' declaration_list statement_list '}'
        | '{' statement_list '}'
        ;
    '''
    if se_eh(TKAbreChaves):
        if se_eh(TKFechaChaves):
            return True
        elif volta_estado_se_der_errado(lambda: declaration_list()):
            if se_eh(TKFechaChaves):
                return True
            if statement_list():
                if se_eh(TKFechaChaves):
                    return True
        elif statement_list() and se_eh(TKFechaChaves):
            return True


def declaration_list():
    '''
    declaration_list
        : declaration declaration_list_aux
        ;
    '''
    if declaration():
        if declaration_list_aux():
            return True


def declaration_list_aux():
    '''
    declaration_list_aux
        | declaration declaration_list_aux
        | vazio
        ;
    '''
    if volta_estado_se_der_errado(lambda: declaration()):
        if declaration_list_aux():
            return True
    return True  # vazio


def declaration():
    '''
    declaration
        : declaration_specifiers ';'
        | declaration_specifiers init_declarator_list ';'
        ;
    '''
    if declaration_specifiers():
        if se_eh(TKPontoEVirgula):
            return True
        elif init_declarator_list() and se_eh(TKPontoEVirgula):
            return True


def init_declarator_list():
    '''
    init_declarator
        : declarator
        | declarator '=' initializer
        ;
    '''
    if declarator():
        if se_eh(TKAtrib):
            if initializer():
                return True
        else:
            return True


def initializer():
    '''
    initializer
        : assignment_expression
        // | '{' initializer_list '}'
        // | '{' initializer_list ',' '}'
        ;
    '''
    return assignment_expression()


def assignment_operator():
    '''
    assignment_operator
        : '='
        | MUL_ASSIGN
        | DIV_ASSIGN
        | MOD_ASSIGN
        | ADD_ASSIGN
        | SUB_ASSIGN
        | LEFT_ASSIGN
        | RIGHT_ASSIGN
        // | AND_ASSIGN
        // | XOR_ASSIGN
        // | OR_ASSIGN
        ;
    '''
    return se_eh(
        TKAtrib,
        TKAstIgual,
        TKDivIgual,
        TKPercIgual,
        TKAtribMais,
        TKMenosIgual,
        TKShiftLeftIgual,
        TKShiftRightIgual,
    )


# ---------- Expressions rabbit hole
def assignment_expression():
    '''
    assignment_expression
        : conditional_expression
        | unary_expression assignment_operator assignment_expression
        ;
    '''

    def procura_atrib():
        if unary_expression():
            if assignment_operator():
                if assignment_expression():
                    return True

    if volta_estado_se_der_errado(procura_atrib):
        return True
    elif conditional_expression():
        return True


def conditional_expression():
    '''
    conditional_expression
        : logical_or_expression
        |// logical_or_expression '?' expression ':' conditional_expression
        ;
    '''
    if logical_or_expression():
        return True


def logical_or_expression():
    '''
    logical_or_expression
        : logical_and_expression logical_or_expression_aux
        ;
    '''
    if logical_and_expression():
        if logical_or_expression_aux():
            return True


@possivelmente_vazio
def logical_or_expression_aux():
    '''
    logical_or_expression_aux
        | OR_OP logical_and_expression logical_or_expression_aux
        | vazio
        ;
    '''
    if se_eh(TKPipePipe):
        if logical_and_expression():
            if logical_or_expression_aux():
                return True


def logical_and_expression():
    '''
    logical_and_expression
        : inclusive_or_expression logical_and_expression_aux
        ;
    '''
    if inclusive_or_expression():
        if logical_and_expression_aux():
            return True


@possivelmente_vazio
def logical_and_expression_aux():
    '''
    logical_or_expression_aux
        | OR_OP logical_and_expression logical_or_expression_aux
        | vazio
        ;
    '''
    if se_eh(TKAndAnd):
        if inclusive_or_expression():
            if logical_and_expression_aux():
                return True


def inclusive_or_expression():
    '''
    inclusive_or_expression
        : exclusive_or_expression inclusive_or_expression_aux
        ;
    '''
    if exclusive_or_expression():
        if inclusive_or_expression_aux():
            return True


@possivelmente_vazio
def inclusive_or_expression_aux():
    '''
    inclusive_or_expression_aux
        | '|' exclusive_or_expression inclusive_or_expression_aux
        | vazio
        ;
    '''
    if se_eh(TKPipe):
        if exclusive_or_expression():
            if inclusive_or_expression_aux():
                return True


def exclusive_or_expression():
    '''
    exclusive_or_expression
        : and_expression exclusive_or_expression_aux
        ;
    '''
    if and_expression():
        if exclusive_or_expression_aux():
            return True


@possivelmente_vazio
def exclusive_or_expression_aux():
    '''
    exclusive_or_expression_aux
        : '^' and_expression exclusive_or_expression_aux
        | vazio
        ;
    '''
    if se_eh(TKCirc):
        if and_expression():
            if exclusive_or_expression_aux():
                return True


def and_expression():
    '''
    and_expression
        : equality_expression and_expression_aux
        ;
    '''
    if equality_expression():
        if and_expression_aux():
            return True


@possivelmente_vazio
def and_expression_aux():
    '''
    and_expression_aux
        | '&' equality_expression and_expression_aux
        | vazio
        ;
    '''
    if se_eh(TKAnd):
        if equality_expression():
            if and_expression_aux():
                return True


def equality_expression():
    '''
    equality_expression
        : relational_expression equality_expression_aux
        ;
    '''
    if relational_expression():
        if equality_expression_aux():
            return True


@possivelmente_vazio
def equality_expression_aux():
    '''
    equality_expression_aux
        | EQ_OP relational_expression equality_expression_aux
        | NE_OP relational_expression equality_expression_aux
        | vazio
        ;
    '''
    if se_eh(TKIgual, TKDiferente):
        if relational_expression():
            if equality_expression_aux():
                return True


def relational_expression():
    '''
    relational_expression
        : shift_expression relational_expression_aux
        ;
    '''
    if shift_expression():
        if relational_expression_aux():
            return True


@possivelmente_vazio
def relational_expression_aux():
    '''
    relational_expression_aux
        | '<' shift_expression relational_expression_aux
        | '>' shift_expression relational_expression_aux
        | LE_OP shift_expression relational_expression_aux
        | GE_OP shift_expression relational_expression_aux
        | vazio
        ;
    '''
    if (
        token == TKMenor
        or token == TKMaior
        or token == TKMenorIgual
        or token == TKMaiorIgual
    ):
        get_next_token()
        if shift_expression():
            if relational_expression_aux():
                return True


def shift_expression():
    '''
    shift_expression
        : additive_expression shift_expression_aux
        ;
    '''
    if additive_expression():
        if shift_expression_aux():
            return True


@possivelmente_vazio
def shift_expression_aux():
    '''
    shift_expression_aux
        | LEFT_OP additive_expression shift_expression_aux
        | RIGHT_OP additive_expression shift_expression_aux
        | vazio
        ;
    '''
    if token == TKShiftLeft or token == TKShiftRight:
        get_next_token()
        if additive_expression():
            if shift_expression_aux():
                return True


def additive_expression():
    '''
    additive_expression
        : multiplicative_expression additive_expression_aux
        ;
    '''
    if multiplicative_expression():
        if additive_expression_aux():
            return True


@possivelmente_vazio
def additive_expression_aux():
    '''
    additive_expression_aux
        | '+' multiplicative_expression additive_expression_aux
        | '-' multiplicative_expression additive_expression_aux
        | vazio
        ;
    '''
    if token == TKMais or token == TKMenos:
        get_next_token()
        if multiplicative_expression():
            if additive_expression_aux():
                return True


def multiplicative_expression():
    '''
    multiplicative_expression
        : cast_expression multiplicative_expression_aux
        ;
    '''
    if cast_expression():
        if multiplicative_expression_aux():
            return True


@possivelmente_vazio
def multiplicative_expression_aux():
    '''
    multiplicative_expression_aux
        | '*' cast_expression multiplicative_expression_aux
        | '/' cast_expression multiplicative_expression_aux
        | '%' cast_expression multiplicative_expression_aux
        | vazio
        ;
    '''
    if token == TKProd or token == TKDiv or token == TKPerc:
        get_next_token()
        if cast_expression():
            if multiplicative_expression_aux():
                return True


def cast_expression():
    '''
    cast_expression // Simplificado pois não há a necessidade de casting
        : unary_expression
        | '(' type_name ')' cast_expression
        ;
    '''
    return unary_expression()


def unary_expression():
    '''
    unary_expression
            : postfix_expression
        | INC_OP unary_expression
        | DEC_OP unary_expression
        | unary_operator cast_expression
        //| SIZEOF unary_expression
        //| SIZEOF '(' type_name ')'
        ;
    '''
    if se_eh(TKDuploMais, TKDuploMenos):
        if unary_expression():
            return True
    elif volta_estado_se_der_errado(lambda: unary_operator()):  # Precisa?
        if cast_expression():
            return True
    elif postfix_expression():
        return True


def unary_operator():
    '''
    unary_operator
        : '&'
        | '*'
        | '+'
        | '-'
        | '~'
        | '!'
        ;
    '''
    return se_eh(
        TKAnd,
        TKProd,
        TKMais,
        TKMenos,
        TKTil,
        TKExc,
    )


def postfix_expression():
    '''
    postfix_expression
        : primary_expression postfix_expression_aux
        ;
    '''
    if primary_expression():
        if postfix_expression_aux():
            return True


@possivelmente_vazio
def postfix_expression_aux():
    '''
    postfix_expression_aux
        | '[' expression ']'  postfix_expression_aux
        | '(' ')' postfix_expression_aux
        | '(' argument_expression_list ')' postfix_expression_aux
        // | '.' IDENTIFIER postfix_expression_aux
        // | PTR_OP IDENTIFIER postfix_expression_aux
        | INC_OP postfix_expression_aux
        | DEC_OP postfix_expression_aux
        ;
    '''
    if se_eh(TKAbreColchete):
        if expression():
            if se_eh(TKFechaColchete):
                if postfix_expression_aux():
                    return True
    if se_eh(TKDuploMais, TKDuploMenos):
        if postfix_expression_aux():
            return True
    if se_eh(TKAbreChaves):
        if se_eh(TKAbreChaves):
            if postfix_expression_aux():
                return True
        elif argument_expression_list():
            if se_eh(TKAbreChaves):
                if postfix_expression_aux():
                    return True


def argument_expression_list():
    '''
    argument_expression_list
        : assignment_expression argument_expression_list_aux
        ;
    '''
    if assignment_expression():
        if argument_expression_list_aux():
            return True


@possivelmente_vazio
def argument_expression_list_aux():
    '''
    argument_expression_list_aux
        | ',' assignment_expression argument_expression_list_aux
        | vazio
        ;
    '''
    if se_eh(TKVirgula):
        if assignment_expression():
            if argument_expression_list_aux():
                return


def primary_expression():
    '''
    primary_expression
        : IDENTIFIER
        | CONSTANT
        //| STRING_LITERAL
        | '(' expression ')'
        ;
    '''
    if se_eh(TKAbrePar):
        if expression():
            if se_eh(TKFechaPar):
                return True
    elif se_eh(TKCteInt) or se_eh(TKId):
        return True


# ----------


def statement_list():
    '''
    statement_list
        : statement statement_list_aux
        ;
    '''
    return statement() and statement_list_aux()


def statement_list_aux():
    '''
    statement_list_aux
        : statement statement_list_aux
        | vazio
        ;
    '''
    # TODO usar volta_estado_se_der_errado
    empilha()
    if statement() and statement_list_aux():
        desempilha_sem_restaurar()
        return True
    else:
        desempilha()
    return True


def statement():
    '''
    statement
        : // labeled_statement
        | iteration_statement
        | selection_statement
        | expression_statement
        | compound_statement
        | // jump_statement
        ;
    '''
    # if volta_estado_se_der_errado(lambda: iteration_statement()):
    #     return True
    # elif volta_estado_se_der_errado(lambda: selection_statement()):
    #     return True
    # elif volta_estado_se_der_errado(lambda: expression_statement()):
    #     return True
    # elif volta_estado_se_der_errado(lambda: compound_statement()):
    #     return True
    if (
        iteration_statement()
        or selection_statement()
        or expression_statement()
        or compound_statement()
    ):
        return True


def expression_statement():
    '''
    expression_statement
        : ';'
        | expression ';'
        ;
    '''
    if se_eh(TKPontoEVirgula):
        return True
    if expression() and se_eh(TKPontoEVirgula):
        return True


def expression():
    '''
    expression
        : assignment_expression expression_aux
        ;
    '''
    if assignment_expression():
        if expression_aux():
            return True


@possivelmente_vazio
def expression_aux():
    '''
    expression_aux
        : ',' assignment_expression expression_aux
        | vazio
        ;
    '''
    if se_eh(TKVirgula):
        if assignment_expression():
            if expression_aux():
                return True


def selection_statement():
    '''
    selection_statement
        : IF '(' expression ')' statement
        | IF '(' expression ')' statement ELSE statement
        ;
    '''
    if (
        se_eh(TKIf)
        and se_eh(TKAbrePar)
        and expression()
        and se_eh(TKFechaPar)
        and statement()
    ):
        if se_eh(TKElse) and statement():
            return True
        return True


def iteration_statement():
    '''
    iteration_statement
        : WHILE '(' expression ')' statement
        | DO statement WHILE '(' expression ')' ';'
        | FOR '(' expression_statement expression_statement ')' statement
        | FOR '(' expression_statement expression_statement expression ')' statement
        ;
    '''
    if (
        se_eh(TKWhile)
        and se_eh(TKAbrePar)
        and expression()
        and se_eh(TKFechaPar)
        and statement()
    ):
        return True
    if se_eh(TKDo):
        if statement() and se_eh(TKWhile):
            if se_eh(TKAbrePar):
                if expression() and se_eh(TKFechaPar):
                    if se_eh(TKPontoEVirgula):
                        return True
    if (
        se_eh(TKFor)
        and se_eh(TKAbrePar)
        and expression_statement()
        and expression_statement()
    ):
        if volta_estado_se_der_errado(
            lambda: se_eh(TKFechaPar) and statement()
        ):  # Certamente tem um jeito menos preguiçoso de fazer essa parte
            return True
        elif expression() and se_eh(TKFechaPar) and statement():
            return True


def function_definition():
    '''
    function_definition
        //: declaration_specifiers declarator declaration_list compound_statement
        | declaration_specifiers declarator compound_statement
        //| declarator declaration_list compound_statement
        //| declarator compound_statement
        ;
    '''
    if declaration_specifiers() and declarator() and compound_statement():
        return True


# --------- Tipos
def declaration_specifiers():
    '''
    declaration_specifiers
        | type_specifier
        | type_specifier declaration_specifiers
        ;
    '''
    if type_specifier():
        empilha()
        if declaration_specifiers():
            desempilha_sem_restaurar()
        else:
            desempilha()
        return True


# def abstract_declarator():
#     if tk == TKPointer:
#         return True
#     | direct_abstract_declarator
#     | pointer direct_abstract_declarator
#     ;


def type_specifier():
    '''
    type_specifier
        : VOID
        | CHAR
        | INT
        | LONG
        | FLOAT
        | DOUBLE
        | UNSIGNED
    '''
    return se_eh(
        TKVoid,
        TKChar,
        TKInt,
        TKLong,
        TKFloat,
        TKDouble,
        TKUnsigned,
    )


def specifier_qualifier_list():
    '''
    specifier_qualifier_list
        : type_specifier specifier_qualifier_list
        | type_specifier
    '''
    global token
    print('TODOTODOTODOTODOTODO', token)


# -------------- Declarators
def direct_declarator():
    '''
    direct_declarator
        : IDENTIFIER direct_declarator_aux
        | '(' declarator ')' direct_declarator_aux
    '''
    if se_eh(TKId):
        if direct_declarator_aux():
            return True
    elif (
        se_eh(TKAbrePar)
        and declarator()
        and se_eh(TKFechaPar)
        and direct_declarator_aux()
    ):
        return True


@possivelmente_vazio
def direct_declarator_aux():
    '''
    direct_declarator_aux
        | '[' constant_expression ']' direct_declarator_aux
        | '[' ']' direct_declarator_aux
        | '(' parameter_type_list ')' direct_declarator_aux
        | '(' identifier_list ')' direct_declarator_aux
        | '(' ')' direct_declarator_aux
        | vazio
    '''
    if se_eh(TKAbreColchete):
        if se_eh(TKCteInt):
            pass
        if se_eh(TKFechaColchete):
            if direct_declarator_aux():
                return True
    if se_eh(TKAbrePar):
        # TODO usar volta_estado_se_der_errado
        empilha()
        if parameter_type_list():
            desempilha_sem_restaurar()
        else:
            desempilha()
            empilha()
            if identifier_list():
                desempilha_sem_restaurar()
            else:
                desempilha()
        if se_eh(TKFechaPar):
            if direct_declarator_aux():
                return True


def identifier_list():
    '''
    identifier_list
        : IDENTIFIER identifier_list_aux
        ;
    '''
    if se_eh(TKId):
        if identifier_list_aux():
            return True


@possivelmente_vazio
def identifier_list_aux():
    '''
    identifier_list_aux
        | ',' IDENTIFIER identifier_list_aux
        | vazio
        ;
    '''
    if se_eh(TKVirgula) and se_eh(TKId) and identifier_list_aux():
        return True


def parameter_type_list():
    '''
    Teria mais coisas aqui se fosse uma gramatica real
    parameter_type_list
        : parameter_list
        ;
    '''
    return parameter_list()


def parameter_list():
    '''
    parameter_list
        : parameter_declaration parameter_list_aux
        ;
    '''
    return parameter_declaration() and parameter_list_aux()


@possivelmente_vazio
def parameter_list_aux():
    '''
    parameter_list_aux
        : ',' parameter_declaration parameter_list_aux
        | vazio
    ;
    '''
    return se_eh(TKVirgula) and parameter_declaration() and parameter_list_aux()


def parameter_declaration():
    '''
    parameter_declaration
        // : declaration_specifiers declarator
        // | declaration_specifiers abstract_declarator
        | declaration_specifiers
        ;
    '''
    return declaration_specifiers()


def pointer():
    return se_eh(TKPointer)


def declarator():
    '''
    declarator
        : pointer direct_declarator
        | direct_declarator
        ;
    '''
    if volta_estado_se_der_errado(lambda: pointer()):
        pass
    return direct_declarator()


def main():
    global arquivo_entrada
    arquivo_entrada = open("arquivo.txt", "r")
    if not arquivo_entrada:
        print("Erro na abertura do fonte.")
        return

    proxC()  # lê primeiro caractere do arquivo
    get_next_token()  # lê primeiro token
    if function_definition():
        print("Reconheceu OK")
    else:
        print(current_char)
        print("Erro sintático")
    arquivo_entrada.close()


if __name__ == "__main__":
    main()
