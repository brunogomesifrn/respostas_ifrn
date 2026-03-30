/*
O ; ao final das instruções é opcional;

*/

console.log("Primeira Impressão");
console.log("Segunda IMpressão")

/*
TIPOS DE DADOS
numérico - inteiro, real..
strings - texto (cadeia de caracteres)
Lógico - true ou false
Null - Objeto sem valor
Undefined - variável que não foi inicializada

DECLARAÇÃO DE VARIÁVEIS EM JS
var - mais antigo; possui apenas 
escopo de função; pode ser redeclarada;

let - possui escopo de bloco {}, não pode 
ser redeclarada;

const - escopo de bloco também; não pode ser
modificada.

Obs.: JS é fracamente tipada;

*/

let idade = 30;
let nome = "Bruno Gomes";
let nota = 8.5;
let valor = true;
let objeto = null;
let valor_2 = undefined;

console.log(nome);

console.log("Nome: " + nome + ". Idade: "+ idade);

// Template Strings
console.log(`Nome: ${nome}. Idade: ${idade}`);


/*
OPERADORES ARITMÉTICOS
Obs.: Sempre retornam um valor numérico
+ soma
- subtração
/ divisão
* multiplicação
% resto da divisão
*/

console.log(5+3);

let resultado = 4-3;
console.log(resultado);

let num1 = 10;
resultado = num1 * 10;
console.log(resultado);

/*
OPERADORES ARIMÉTICOS
++ incrementa em 1
-- decrementa em 1

Pode ser usado antes ou depois da
variável (funciona diferente)
*/

let num_2 = 10;
console.log(++num_2);
console.log(num_2);

let num_3 = 10;
console.log(num_3++);
console.log(num_3);

let num_4 = 15;
resultado = num_4++ + 10;
console.log(resultado);

/*
OPERADORES DE COMPARAÇÃO
Obs.: sempre retornam valor LÓGICO
== verifica se os valores são iguais
=== verifica se valor e tipo são iguais
!= verifica se os valores são diferentes
!=== verifica se valor e tipo são diferentes
< verifica se um valor é menor que outro
> verifica se um valor é maior que outro
<= verifica se um valor é menor ou igual a outro
>= verifica se um valor é maior ou igual a outro
*/

console.log(5==3);
console.log(5==5);
console.log(5==5.0);
console.log(5===5.0);
console.log(3!="3");
console.log(3!=="3");
console.log(15>4);
console.log(15>15);
console.log(15>=15);

/*
OPERADORES LÓGICOS
Obs.: sempre retornam valor LÓGICO
&&   E lógico
||   OU lógico
!    negação
*/

console.log(5>3 && 4==3);
console.log(5>3 || 4==3);
console.log(!(5!=5));
