/*
FUNÇÕES ANÔNIMAS
- São funções que não possuem nome;
- Como não possui nome, só está acessível
durante a sua criação;
- Deve ser executada no momento da sua 
declaração ou atribuída a uma variável.

Sintaxe:
function () {

}
*/

let instituicao = function () {
    console.log("IFRN");
}

/*
Para executar a função, utiliza a
variável com os parênteses;
*/

instituicao();

// Executar no momento da declaração
/*
let variavel = function () {
    console.log("Institudo Federal");
}
variavel();
*/

(function () {
    console.log("Institudo Federal");
})();

// Passagem de função entre variáveis

let nome = function () {
    console.log("Canguaretama");
}

let nome_instituicao = nome;
nome_instituicao();

/* É possível nomear uma função e 
atribuí-la a uma variável;
*/

let estado = function sigla(){
    console.log("RN");
}

estado();

// Passagem de parâmetros em funções anônimas

let soma = function (num1, num2){
    console.log(num1+num2);
}

soma(5,3);

/*
    ARROW FUNCTIONS
    - Abreviação da função anônima
*/

/*
let campus = function () {
    console.log("CANG");
}
*/

let campus = () => console.log("CANG");
campus();


let multiplicacao = function (num1, num2){
    return (num1*num2);
}

console.log(multiplicacao(2,10));

let multi = (num1, num2) => num1*num2;

console.log(multi(2,10));