/*
REPETIÇÃO DE DADOS
- Estrutura que permite a repetição
de determinas intruções (que fazem
parte do bloco)
*/

for(let i=0; i<10; i++){
    console.log('IFRN');
}

for(let i=1; i<=15; i++){
    console.log(i);
}

let lista = [1, 10.4, 'IFRN', true];

for(let i=0; i<lista.length; i++){
    console.log(lista[i]);
}

for(let valor of lista){
    console.log(valor);
}

let num = 1;

while(num<15){
    console.log(num);
    num++;
}