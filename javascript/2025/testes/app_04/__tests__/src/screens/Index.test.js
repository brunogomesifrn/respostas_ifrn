import { render, screen, fireEvent} from "@testing-library/react-native";

import App from "../../../App";

test("Testar se renderiza App.js", ()=>{
    render(<App />);
})

test("Verificar se Index abriu com o texto", ()=>{
    render(<App />);
    expect(screen.getByText("Tela Inicial")).toBeOnTheScreen();
})

test("Verificar se Index abriu com o botão", ()=>{
    render(<App />);
    expect(screen.getByTestId("b_contato"))
    .toBeOnTheScreen();
})

test("Verificar se Contato abriu", ()=>{
    render(<App />);
    fireEvent.press(screen.getByTestId("b_contato"));
    expect(screen.getByText("Tela de Contato")).
    toBeOnTheScreen();
});