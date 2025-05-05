// Função tradicional/nativa

function sigla(){
    return "IFRN";
}

console.log(sigla());

// Função anônima

let instituto = function (){
    return "IFRN";
}

console.log(instituto());

// Executando função anônima

(function (){
    console.log("IFRN");
})();

// Arrow Function

let nome = () => console.log("IFRN");
nome();

let inst = () => {
    return "IFRN";
};
console.log(inst());

let soma = (num1, num2) => {
    return num1+num2;
};
console.log(soma(10, 6));
