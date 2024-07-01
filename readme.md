# Analisador sintático de código C.

> Feito por: Gustavo Cauzzi e Thaís Linzemaier

Implementação simplificada da gramática ANSI C Yacc grammar
https://www.lysator.liu.se/c/ANSI-C-grammar-y.html#assignment-expression

Referências para o que foi utilizado da gramática original podem ser encontradas no [gramatica.txt](./gramatica.txt) ou na DocString das funções. Caso houver um símbolo de comentário "//" na gramática significa que aquele caminho foi ignorado pois saia do escopo do projeto.

---

> Nota: No código principal ainda seria possível simplificar as funções de gramática para não utilizar IF aninhados, mas certas partes do código foram deixadas assim para facilitar o processo de debug.
