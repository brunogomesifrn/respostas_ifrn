console.log("Lista de Dados em JS");

/*
LISTA DE DADOS
- Local que permite o armazenamento
temporário de vários valores ao
mesmo tempo.
- Utiliza [] para se criar uma lista
*/

let lista_numero = [6, 4, 1, 15];
let lista_reais = [1.5, 6.3, 9.3, 10.2];
let lista_texto = ["IFRN", "Campus", "Canguaretama"];
let lista_booleano = [true, false, false, false];

let lista_misturado = [6, 10.5, "IFRN", false];

// ACESSANDO UM VALOR DA LISTA
let nome = lista_texto[2];
console.log(nome);

console.log(lista_texto[0]);

// ALTERANDO UM VALOR DA LISTA
lista_texto[2] = "CANG";
console.log("Lista com elemento altedado: ",lista_texto);

// PROPRIEDADE length - retorna o tamanho da lista
console.log("Tamanho: "+lista_texto.length);

// FUNÇÃO pop() - Remove o último elemento
console.log("Lista antes da remoção:",lista_numero);
let numero_removido = lista_numero.pop();
console.log("Elemento removido: ",numero_removido);
console.log("Lista sem o último elemento: ",lista_numero);

// FUNÇÃO shift() - Remove o primeiro elemento
lista_numero.shift();
console.log(lista_numero);

// FUNÇÃO push() - insere ao final da lista
lista_numero.push(9);
console.log("Lista com novo número: ",lista_numero);

lista_numero.push(15, 2, -3);
console.log(lista_numero);

// FUNÇÃO unshift() - insere no início da lista
lista_numero.unshift(150, 2);
console.log(lista_numero);

// FUNÇÃO indexOf() - retorna a posição de um elemento
let posicao = lista_texto.indexOf("CANG");
console.log("O indice de CANG é: ", posicao);

// FUNÇÃO sort() - ordena a lista
console.log(lista_numero.sort());

// FUNÇÃO splice - remove de acordo com posição inicial e qtd de elementos para frente
lista_numero.splice(2,5);
console.log(lista_numero);



