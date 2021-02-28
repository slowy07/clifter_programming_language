# clifter programming language

[![license](https://img.shields.io/github/license/slowy07/slowy_programming_language?style=for-the-badge)](LICENSE)
![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![progress](https://progress-bar.dev/80/)

my programming language written with python
reference
- [introduction to computers and programming](https://www.pearsonhighered.com/assets/samplechapter/0/3/2/1/0321537114.pdf)
- [introduction to python](http://tdc-www.harvard.edu/Python.pdf)
- [advanced programming language design](https://www.researchgate.net/publication/220692467_Advanced_programming_language_design)


## information variables
```python
TT_INT			= 'INT'             #int
TT_FLOAT    	= 'FLOAT'           #float
TT_IDENTIFIER	= 'IDENTIFIER'      #identifier variable
TT_STRING       = 'STRING'          #string
TT_KEYWORD		= 'KEYWORD'         #keyword 'and' 'or' 'not' 'var'
TT_PLUS     	= 'PLUS'            #plus operator
TT_MINUS    	= 'MINUS'           #minus operator
TT_MUL      	= 'MUL'             #multiple
TT_DIV      	= 'DIV'             #divide
TT_POW			= 'POW'             #power number
TT_EQ			= 'EQ'              #equal 
TT_LPAREN   	= 'LPAREN'          # (
TT_RPAREN   	= 'RPAREN'          # )
TT_EE			= 'EE'              # equal
TT_NE			= 'NE'              # not equal
TT_LT			= 'LT'              # less than
TT_GT			= 'GT'              # greater than
TT_LTE			= 'LTE'             # less than equal
TT_GTE			= 'GTE'             # greater than equal
```

## basic terminal
**variable**
```
>> var number = 2
>>2
>>number + 2
>>4
```
**logical operation**
```
>>var mynum = 1
>>for i = 1 to 6 then var result = result * i
>>result
>>120
>>if mynum == 1 then mynum + 123
>>124
```
**function**
```
>>fun multiple(a, b) -> a * b
<function multiple>
>>multiple(5, 5)
25
```
**string**
```
>>"hello world"
"hello world"
>>fun greetings(name) -> "hello " + name
>>greetings("jole")
"hello jole"
>>var name = "arfy"
>>var name2 = "slowy"
>>"hello " + name + " "+name2
"hello arfy slowy"
```
**list**
```
>> var list1 = [1,2,3,4]
>> list1
[1,2,3,4]
>> list1 + 5
[1,2,3,4,5]
>>list1 * [6,7,8]
[1,2,3,4,5,6,7,8]
>>list1/2
3
>>list1/0
1
>>for i = 1 to 5 then 5 ^ i
[5,25,125,625]
```
**multi line statement**
```
clifter 1.0.0[February - 28 - 2021] 
on ----- [Python ------]
[]>1+2;3+4;5+6;
[3, 7, 11]
[]>var multi = if 5 == 5 then "yuhuuuuu" else "nooooo"
"yuhuuuuu"
[]>multi
"yuhuuuuu"
[]>
```