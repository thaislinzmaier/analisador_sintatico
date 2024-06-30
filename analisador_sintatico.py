import string

# Definindo os tokens
TKId = 1 #ok
TKVoid = 2 #ok
TKInt = 3 #ok
TKFloat = 4 #ok
TKVirgula = 5 #ok
TKDoisPontos = 6 #ok
TKAbrePar = 7 #ok
TKFechaPar = 8 #ok
TKAtrib = 9 #ok
TKPontoEVirgula = 10 #ok
TKAbreChaves = 11 #ok
TKFechaChaves = 12 #ok
TKMais = 13 #ok
TKDuploMais = 14 #ok
TKProd = 15 #ok
TKChar = 16 #ok
TKSub = 17 #ok
TKAbreColchete = 18 #ok
TKFechaColchete = 19 #ok
TKAtribMais = 20 #ok
TKDouble = 21 #ok
TKCteInt = 22 #ok
TKElse = 23 #ok
TKIf = 23 #ok
TKFimArquivo = 24 #ok
TKLong = 25 #ok
TKUnsigned = 26 #ok
TKPointer = 27 #ok
TKArray = 28 #ERRO
TKFor = 28 #ok
TKDiv = 29 #ok
TKPerc = 30 #ok
TKMaior = 31 #ok
TKMenor = 32 #ok
TKIgual = 33 #ok
TKDiferente = 34 #ok
TKMenorIgual = 35 #ok
TKMaiorIgual = 36 #ok
TKAnd = 37 #ok
TKPipe = 38 #ok
TKCirc = 39 #ok
TKShiftRight = 40 #ok
TKShiftLeft = 41 #ok
TKTil = 42 #ok
TKAndAnd = 43 #ok
TKPipePipe = 44 #ok
TKExc = 45 #ok
TKMenosIgual = 46 #ok
TKAstIgual = 47 #ok
TKDivIgual = 48 #ok
TKPercIgual = 49 #ok
TKShiftRightIgual = 50 #ok
TKShiftLeftIgual = 51 #ok



# Dicionário para mapear números de tokens para seus nomes correspondentes
token_names = {  # Meter um enum pra tirar essas constantezada malucas talvez?
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
    TKSub: "TKSub",
    TKPointer: "TKPointer",
    TKArray: "TKArray",
    TKFor: "TKFor",
    TKDiv : "TKDiv",
    TKPerc : "TKPerc",
    TKMaior : "TKMaior",
    TKMenor : "TKMenor",
    TKIgual : "TKIgual",
    TKDiferente : "TKDiferente",
    TKMenorIgual : "TKMenorIgual",
    TKMaiorIgual : "TKMaiorIgual",
    TKAnd : "TKAnd",
    TKPipe : "TKPipe",
    TKCirc : "TKCirc",
    TKShiftRight : "TKShiftRight",
    TKShiftLeft : "TKShiftLeft",
    TKTil : "TKTil",
    TKAndAnd : "TKAndAnd",
    TKPipePipe : "TkPipePipe",
    TKExc : "TKExc",
    TKMenosIgual : "TKMenosIgual",
    TKAstIgual : "TKAstIgual",
    TKDivIgual : "TKDivIgual",
    TKPercIgual : "TKPercIgual",
    TKShiftRightIgual : "TKShiftRightIgual",
    TKShiftLeftIgual : "TKShiftLeftIgual"
}


pos = 0
tk = 0
lex = ""
arqin = None
c = ''  # último caractere lido do arquivo


lista_palavras_reservadas = {
    "void": TKVoid,
    "int": TKInt,
    "float": TKFloat,
    "char": TKChar,
    "double": TKDouble,
    "else": TKElse,
    "for": TKFor,
    "if": TKIf,
    "long": TKLong,
    "unsigned": TKUnsigned,
    "fimtabela": TKId,
}

def palavra_reservada(lex):
    return lista_palavras_reservadas.get(lex, TKId)


def getToken():
    global tk, c, lex, pos
    estado = 0
    fim = False
    posl = 0
    lex = ''
    while not fim:
        print(c)
        lex += c
        print(lex)
        if estado == 0:
            if c.isalpha() or c == '_':
                proxC()
                estado = 1
            elif c.isdigit():
                while c.isdigit():
                    proxC()
                tk = TKCteInt
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '=':
                proxC()
                if c == '=':
                    lex += c
                    proxC()
                    tk = TKIgual
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                tk = TKAtrib
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '+':
                proxC()
                if c == '+':
                    lex += c
                    proxC()
                    tk = TKDuploMais
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                elif c == '=':
                    lex += c
                    proxC()
                    tk = TKAtribMais
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                else:
                    tk = TKMais
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '-':
                proxC()
                if c == '=':
                    lex += c
                    proxC()
                    tk = TKMenosIgual
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                else:
                    tk = TKSub
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '*':
                proxC()
                if c.isalpha():
                    tk = TKPointer
                elif c == '=':
                    tk = TKAstIgual
                else:
                    tk = TKProd
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '/':
                proxC()
                if c == '=':
                    lex += c
                    proxC()
                    tk = TKDivIgual
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                else:
                    tk = TKDiv
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '%':
                proxC()
                if c == '=':
                    lex += c
                    proxC()
                    tk = TKPercIgual
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                else:
                    tk = TKPerc
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '!':
                proxC()
                if c == '=':
                    lex += c
                    proxC()
                    tk = TKDiferente
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                else:
                    tk = TKExc
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '&':
                proxC()
                if c == '&':
                    lex += c
                    proxC()
                    tk = TKAndAnd
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                else:
                    tk = TKAnd
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '|':
                proxC()
                if c == '|':
                    lex += c
                    proxC()
                    tk = TKPipePipe
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                else:
                    tk = TKPipe
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '>':
                proxC()
                if c == '=':
                    lex += c
                    proxC()
                    tk = TKMaiorIgual
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                if c == '>':
                    proxC()
                    if c == '=':
                        lex += c
                        proxC()
                        tk = TKShiftRightIgual
                        print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                        return
                    else:
                        tk = TKShiftRight
                        print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                        return
                else:
                    tk = TKMaior
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '<':
                proxC()
                if c == '=':
                    lex += c
                    proxC()
                    tk = TKMenorIgual
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
                if c == '<':
                    proxC()
                    if c == '=':
                        lex += c
                        proxC()
                        tk = TKShiftLeftIgual
                        print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                        return
                    else:
                        tk = TKShiftLeft
                        print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                        return
                else:
                    tk = TKMenor
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    return
            elif c == '[':
                proxC()
                tk = TKAbreColchete
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == ']':
                proxC()
                tk = TKFechaColchete
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '(':
                proxC()
                tk = TKAbrePar
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == ')':
                proxC()
                tk = TKFechaPar
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '{':
                proxC()
                tk = TKAbreChaves
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '}':
                proxC()
                tk = TKFechaChaves
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == ',':
                proxC()
                tk = TKVirgula
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '^':
                proxC()
                tk = TKCirc
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '~':
                proxC()
                tk = TKTil
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == ';':
                proxC()
                tk = TKPontoEVirgula
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == ':':
                proxC()
                tk = TKDoisPontos
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '':
                tk = TKFimArquivo
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                fim = True
                return
            elif c in ' \n\t\r':
                lex = lex[:-1]
                proxC()
            else:
                print(f"Erro léxico: encontrou o caractere {c} ({ord(c)})")
                while c != '\n':
                    proxC()
        elif estado == 1:
            if c.isalnum() or c == '_':
                proxC()
            # else:
            #     print(lex)
            #     lex = lex[:-1]
            #     print(lex)
            #     tk = palavra_reservada(lex)
            #     return
            else:
                if c.isspace():
                    lex = lex[:-1]
                    tk = palavra_reservada(lex)
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                    lex = ""
                else:
                    lex += c
                
                print('LEX PROBLEMATICO', lex)
                print('C DEPOIS DO LEX PROBLEMATICO', c)
                
                proxC()

                if lex:
                    tk = palavra_reservada(lex)
                    print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return


def proxC():
    global c
    c = arqin.read(1)
    if not c:
        c = ''
    print(f"Caractere lido: '{c}'")


def E():
    if F():
        if E2():
            return True
    return False


def E2():
    global tk
    if tk == TKMais:
        getToken()
        if F():
            if E2():
                return True
        return False
    return True


def F():
    global tk
    if tk == TKId or tk == TKCteInt:
        getToken()
        return True
    else:
        print(f"Esperava um identificador ou constante. Encontrou {lex}")
        return False


def DecFunc():
    if Tipo():
        if tk == TKId:
            getToken()
            if tk == TKAbrePar:
                getToken()
                if tk == TKFechaPar:
                    getToken()
                    if ComComp():
                        return True
                    return False
                else:
                    print(f"Esperava ')'. Encontrou {lex}")
                    return False
            return False
        return False
    return False


def Tipo():
    global tk
    print('TK', tk)
    if tk == TKInt or tk == TKFloat or tk == TKVoid:
        getToken()
        return True
    return False


def ComComp():
    global tk
    print("Entrei no Comando Composto")
    if tk == TKAbreChaves:
        getToken()
        print("Abrechaves")
        if Lista():
            if tk == TKFechaChaves:
                getToken()
                return True
            return False
        return False
    return False


def Lista():
    global tk
    print(f"Entrei na lista. token={tk}")
    if tk == TKFechaChaves:
        return True
    if ComExp():
        print("Reconheci comando expressão")
        if Lista():
            return True
        return False
    if DecVar():
        if Lista():
            return True
        return False
    return True


def ComExp():
    print("Entrei no ComExp")
    if E():
        if tk == TKPontoEVirgula:
            getToken()
            return True
        return False
    return False


def DecVar():
    if Tipo():
        if tk == TKId:
            getToken()
            if tk == TKPontoEVirgula:
                getToken()
                return True
            return False
        return False
    return False


def main():
    global arqin
    arqin = open("arquivo.txt", "r")
    if not arqin:
        print("Erro na abertura do fonte.")
        return

    proxC()  # lê primeiro caractere do arquivo
    getToken()  # lê primeiro token
    if DecFunc():
        print("Reconheceu OK")
    else:
        print(c)
        print("Erro sintático")
    arqin.close()


if __name__ == "__main__":
    main()
