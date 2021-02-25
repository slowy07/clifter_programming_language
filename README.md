# my programming language
[![license](https://img.shields.io/github/license/slowy07/slowy_programming_language?style=for-the-badge)](LICENSE)
![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

my own programming language written with python



## grammar

```
expr = term((PLUS|MINUS) term)*
term = factor((MUL|DIV) factor)*
factor = int | float
power = atom(POW factor)*
atom = INT | FLOAT | IDENTIFIER


```