/*
LISTA DE DADOS
- Estrutura que agrupa vários valores
- Uma estrtura pode agrupar tipos de dados diferentes
- Utiliza [] para manipular listas e , para separar os elementos
- Os elementos são armazenados em posições que iniciam em 0
*/

let lista_1 = [5, 10, -2, 13];
let lista_2 = [10.5, 4.3, 2.2];
let lista_3 = ["Segunda", "Terça", "Quarta"];
let lista_4 = [true, false, false];
let lista_5 = [10, 8.5, false, "Dispositivos Móves"];
let lista_6 = [6, 3, 10.5, [5, 3, "Segunda"]];

/*
Para acessar ou alterar valor de uma lista,
utiliza [] também e a posição;
*/
console.log(lista_3[1]);
lista_3[1] = "Terça-feira";
console.log(lista_3[1]);

console.log(lista_6[3][1]);

// length é uma propiedade de lista
console.log(lista_4.length);

/*
FUNÇÕES
push() - Adiciona elemento ao fim da lista
unshift() - Adiciona elemento no início da lista
pop() - remove o último elemento
splice(posição, qtd) - remove uma qtd de elementos a
partir de uma posição
*/

lista_1.push(7);
console.log(lista_1);
lista_1.unshift(6);
console.log(lista_1);
lista_1.pop();
console.log(lista_1);

/*
indexOf - localiza um elemento dentro da lista
Se existir, retorna a posição dele
Se não existir, retorna -1
*/

console.log(lista_1.indexOf(10));
console.log(lista_1.indexOf(-10));

posicao = lista_1.indexOf(10)
lista_1.splice(posicao, 1);
console.log(lista_1);

/*
SITUAÇÃO
Vamos supor que eu quero atribuir cada
elemento de uma lista para variáveis diferentes...

Javascript tem a opção de desestruturar a lista
*/


let lista_7 = [5, 10, -3];
let num_1 = lista_7[0];
let num_2 = lista_7[1];
let num_3 = lista_7[2];

let [numero_1, numero_2, numero_3] = lista_7;
console.log(numero_1);

/*
Operador Spread
- Junte duas listas em 1
*/

// Situação

let lista_8 = [6, 4, 1];
let lista_9 = [3, 4, 1, ...lista_8];
console.log(lista_9);


/*
Função para ordenar lista:
sort()
*/

console.log(lista_9.sort());

/*
Função map()
- permite realizar uma determinada operação
com cada elemento da lista, e retorna uma
lista de mesmo tamanho com todos os valores
atualizados
*/

let lista_10 = [10, 2, 5, 12, -5];
let resultado = lista_10.map(function (num){
    return num+2;
});
console.log(resultado);

/*
Funçao filter()
Retorna uma nova lista somente com elementos
que satisfazem uma condição
*/

resultado = lista_10.filter(function (num){
    return num<0;
});
console.log(resultado);

/*
Função reduce()
- Reduzir a lista em apenas 1 valor, através
de uma operação desejada
*/

resultado = lista_10.reduce(function (num, acumulador){
    return acumulador+num;
}, 0);

console.log(resultado);





