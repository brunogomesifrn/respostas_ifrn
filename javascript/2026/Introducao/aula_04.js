/*
FUNÇÃO
- Agrupa um conjunto de instruções com
o objetivo de reutilização de código, ou
mesmo evitar a repetição de código.
- Utiliza a palavra-reservada "function" e ().
*/

// FUNÇÃO SEM RETORNO E SEM PARÂMETROS

function sigla(){
    console.log("IFRN");
}

sigla();

// FUNÇÃO COM RETORNO E SEM PARÂMETROS

function instituicao(){
    return "Instituto Federal";
}

let nome = instituicao();
console.log(nome);

//ou

console.log(instituicao());

// FUNÇÃO SEM RETORNO E COM PARÂMETROS

function soma(num_1, num_2){
    console.log(num_1+num_2);
}

soma(10, 5);

// FUNÇÃO COM RETORNO E PARÂMETROS

function subtracao(num_1, num_2){
    return num_1-num_2;
}

console.log(subtracao(500, 210));


/*
FUNÇÕES COM PARÂMETROS OPCIONAIS
*/

function cadastro(usuario, senha){
    console.log(` ${usuario} - ${senha} `);
}

cadastro("BG", "123");

function cadastro_opcional(usuario, senha="12345"){
    console.log(` ${usuario} - ${senha} `);
}

cadastro_opcional("BG", "321");
cadastro_opcional("BGA");

/* 
FUNÇÃO ANÔNIMA
- Função sem nome;
- Função para ser executada naquele instante e que 
pode ser atribuída;
*/

let instituto = function (){
    console.log("IFRN");
}

instituto();

// Executar uma função anônima

(function (){
    console.log("Canguaretama");
})();

// ARROW FUNCTION

let curso = ()=>{
    console.log("TSI");
}

curso();

let periodo = () => console.log("5");

let periodo_atual = () => "5";

let periodo_atual_curso = () => "5";