import '@testing-library/react-native/extend-expect';
import {render, screen, fireEvent} from '@testing-library/react-native';
import React from 'react';

import App from '../../../App';

describe("Testes de Componentes", () => {

    test("Verificar se Visor aparece", () => {
        render(<App />);
        fireEvent.press(screen.getByTestId("calc"));
        expect(screen.getByTestId("tela")).toBeOnTheScreen();
    });

    test("Verificar se visor está vazio de início", () => {
        render(<App />);
        fireEvent.press(screen.getByTestId("calc"));
        expect(screen.getByTestId("tela")).toHaveTextContent("");
    });

});


describe("Testes Unitários", () => {
    
    test("Verificar se o 1 aparece na tela ao pressionar o botão 1", () =>{
        render(<App />);
        fireEvent.press(screen.getByTestId("calc"));
        fireEvent.press(screen.getByText("1"));
        expect(screen.getByTestId("tela")).toHaveTextContent("1");
    });

    test("Verificar se 15+4=19", () => {
        render(<App />);
        fireEvent.press(screen.getByTestId("calc"));
        fireEvent.press(screen.getByText("1"));
        fireEvent.press(screen.getByText("5"));
        fireEvent.press(screen.getByText("+"));
        fireEvent.press(screen.getByText("4"));
        fireEvent.press(screen.getByText("="));
        expect(screen.getByTestId("tela")).toHaveTextContent("19");
    });

});


describe("Teste de Navegação", () => {
    
    test("Testar se texto apareceu", async () => {
        render(<App />);
        fireEvent.press(screen.getByTestId("calc"));
        const tela = await screen.getByText("Calculadora");
        expect(tela).toBeOnTheScreen();
    });

});