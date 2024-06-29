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
TKSub = 17
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
TKArray = 28

# Dicionário para mapear números de tokens para seus nomes correspondentes
token_names = {
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
    TKArray: "TKArray"
}


false = 0
true = 1

import string

pos = 0
tk = 0
lex = ""
arqin = None
c = ''  # último caractere lido do arquivo

class PalRes:
    def __init__(self, palavra, tk):
        self.palavra = palavra
        self.tk = tk

lista_pal = [
    ("void", TKVoid),
    ("int", TKInt),
    ("float", TKFloat),
    ("char", TKChar),
    ("double", TKDouble),
    ("else", TKElse),
    ("if", TKIf),
    ("long", TKLong),
    ("unsigned", TKUnsigned),
    ("fimtabela", TKId)
]

# def palavra_reservada(lex):
#     postab = 0
#     while lista_pal[postab].palavra != "fimtabela":
#         if lex == lista_pal[postab].palavra:
#             return lista_pal[postab].tk
#         postab += 1
#     return TKId

def palavra_reservada(lex):
    for palavra, token in lista_pal:
        if lex == palavra:
            return token
    return TKId

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
            elif c == '*':
                proxC()
                tk = TKProd
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
            elif c == '-':
                proxC()
                tk = TKSub
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                return
            elif c == '':
                tk = TKFimArquivo
                print(f"Token: {token_names.get(tk, 'Desconhecido')}, lex: {lex}")
                fim = True
                return
            elif c in r' \n\t\r':
                proxC()
                posl -= 1
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
                tk = palavra_reservada(lex)
                # if tk == TKId:
                #     lex = lex[:-1]
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
    if tk == TKInt or tk == TKFloat:
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
