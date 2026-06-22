import React, { useEffect, useState } from 'react';
import { View, Text, Button } from 'react-native';

export default function CursosScreen() {
    const API_CURSOS = 'http://192.168.1.146:8000/api/v1/cursos/';
    const [cursos, setCursos] = useState([]);
    const [pagina, setPagina] = useState(1);
    const [totalPaginas, setTotalPaginas] = useState(1);

    async function carregarCursos(numeroPagina) {
        
        const response = await fetch(API_CURSOS+"listar/pag/?page="+numeroPagina);

        const data = await response.json();

        setCursos(data.results);
        setPagina(data.current_page);
        setTotalPaginas(data.total_pages);
    }

    useEffect(() => {
        carregarCursos(1);
    }, []);

    return (
        <View>

            <Text>
                Página {pagina} de {totalPaginas}
            </Text>

            {cursos.map((curso) => (
                <Text key={curso.id}>
                    {curso.titulo}
                </Text>
            ))}

            <Button
                title="Anterior"
                disabled={pagina === 1}
                onPress={() => carregarCursos(pagina - 1)}
            />

            <Button
                title="Próxima"
                disabled={pagina === totalPaginas}
                onPress={() => carregarCursos(pagina + 1)}
            />

        </View>
    );
}