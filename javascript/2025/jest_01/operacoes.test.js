let operacoes = require("./operacoes");

describe("Testes na operação de soma", ()=>{
    test("Soma entre positivos", ()=>{
        expect(operacoes.soma(5,3)).toBe(8);
    });
    
    test("Soma entre Positivo e Negativo", ()=>{
        expect(operacoes.soma(5,-2)).toBe(3);
    });
});

describe("Testes na subtração", ()=>{
    test("Subtracao entre positivos", ()=>{
        expect(operacoes.subtracao(10,4)).toBe(6);
    });

    test("Subtracao entre + e -", ()=>{
        expect(operacoes.subtracao(10,-4)).toBe(14);
    });

});

