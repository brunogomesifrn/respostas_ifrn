import '@testing-library/react-native/extend-expect';
import {render, screen, fireEvent} from '@testing-library/react-native';
import React from 'react';

import Index from '../../../src/telas/Index'
import App from '../../../App';

describe("Testes de Componentes", () => {

    test("Testar se a tela Index abre de forma independente", () => {
        render(<Index />);
    });

    test("Testar se Index abre através de App", () => {
        render(<App />);
    });

    test("Testar se o texto de index apareceu", () => {
        render(<App />);
        expect(screen.getByText("Calculadora do BG")).toBeOnTheScreen();
    });

    test("Testar se o botão de index apareceu", () => {
        render(<App />);
        const componente = screen.getByText("Calculadora");
        expect(componente).toBeOnTheScreen();
    });

    test("Testar se o botão de index apareceu pelo ID", () => {
        render(<App />);
        expect(screen.getByTestId("calc")).toBeOnTheScreen();
    });

});

describe("Teste de navegação", ()=>{

    test("Testar se botão de Index abre a tela Calculadora", () => {
        render(<App />);
        fireEvent.press(screen.getByTestId("calc"));
        expect(screen.getByTestId("tela")).toBeOnTheScreen();
    });

});