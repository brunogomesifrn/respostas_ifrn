/*
npx expo install @react-native-picker/picker
npx expo install expo-checkbox
*/
import {View,Text,FlatList,TextInput,Button,ScrollView} from 'react-native';
import { useState, useEffect } from 'react';
import { Picker } from '@react-native-picker/picker';
import Checkbox from 'expo-checkbox';

export default function Cursos() {

    const API_CURSOS = 'http://192.168.1.146:8000/api/v1/cursos/';
    const API_AREAS = 'http://192.168.1.146:8000/api/v1/areas/';
    const API_PUBLICOS = 'http://192.168.1.146:8000/api/v1/publicos/';

    const [cursos, setCursos] = useState([]);
    const [areas, setAreas] = useState([]);
    const [publicos, setPublicos] = useState([]);

    const [id, setId] = useState('');

    const [titulo, setTitulo] = useState('');
    const [resumo, setResumo] = useState('');
    const [cargaHoraria, setCargaHoraria] = useState('');
    const [dataInicio, setDataInicio] = useState('');
    const [vagas, setVagas] = useState('');

    const [areaSelecionada, setAreaSelecionada] = useState('');

    const [publicosSelecionados, setPublicosSelecionados] = useState([]);

    useEffect(() => {
        listarCursos();
        listarAreas();
        listarPublicos();
    }, []);

    async function listarCursos() {
        try {

            const resposta =
                await fetch(API_CURSOS + 'listar/');

            const dados =
                await resposta.json();

            setCursos(dados);

        } catch (erro) {
            console.log(erro);
        }
    }

    async function listarAreas() {
        try {

            const resposta =
                await fetch(API_AREAS + 'listar/');

            const dados =
                await resposta.json();

            setAreas(dados);

        } catch (erro) {
            console.log(erro);
        }
    }

    async function listarPublicos() {
        try {

            const resposta =
                await fetch(API_PUBLICOS + 'listar/');

            const dados =
                await resposta.json();

            setPublicos(dados);

        } catch (erro) {
            console.log(erro);
        }
    }

    async function adicionar() {
        console.log("Entrou em Inserir");
        const novoCurso = {
            titulo: titulo,
            resumo: resumo,
            carga_horaria: parseInt(cargaHoraria),
            data_inicio: dataInicio,
            vagas: parseInt(vagas),
            area: parseInt(areaSelecionada),
            publicos: publicosSelecionados
        };
        console.log(dataInicio);
        console.log(JSON.stringify(novoCurso, null, 2));
        const resposta = await fetch(API_CURSOS + 'inserir/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(novoCurso)
        });

        const dados = await resposta.json();

        console.log(dados);
        limparCampos();
        listarCursos();
    }

    function editar(item) {

        setId(item.id.toString());

        setTitulo(item.titulo);
        setResumo(item.resumo);

        setCargaHoraria(
            item.carga_horaria.toString()
        );

        setDataInicio(item.data_inicio);

        setVagas(
            item.vagas.toString()
        );

        setAreaSelecionada(
            item.area
        );

        setPublicosSelecionados(
            item.publicos
        );
    }

    async function atualizar() {

        const cursoAtualizado = {
            titulo: titulo,
            resumo: resumo,
            carga_horaria: parseInt(cargaHoraria),
            data_inicio: dataInicio,
            vagas: parseInt(vagas),
            area: parseInt(areaSelecionada),
            publicos: publicosSelecionados
        };

        await fetch(
            API_CURSOS + 'editar/' + id + '/',
            {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(cursoAtualizado)
            }
        );

        limparCampos();
        listarCursos();
    }

    async function remover(idRemover) {

        await fetch(
            API_CURSOS +
            'remover/' +
            idRemover +
            '/',
            {
                method: 'DELETE'
            }
        );

        limparCampos();
        listarCursos();
    }

    function limparCampos() {

        setId('');

        setTitulo('');
        setResumo('');
        setCargaHoraria('');
        setDataInicio('');
        setVagas('');

        setAreaSelecionada('');

        setPublicosSelecionados([]);
    }

    function selecionarPublico(idPublico) {

        if (
            publicosSelecionados.includes(idPublico)
        ) {

            setPublicosSelecionados(
                publicosSelecionados.filter(
                    id => id !== idPublico
                )
            );

        } else {

            setPublicosSelecionados([
                ...publicosSelecionados,
                idPublico
            ]);

        }
    }

    return (

        <ScrollView>

            <Text
                style={{
                    fontSize: 24,
                    marginBottom: 10
                }}
            >
                Cursos
            </Text>

            <Text>ID</Text>
            <TextInput
                value={id}
                onChangeText={setId}
            />

            <Text>Título</Text>
            <TextInput
                value={titulo}
                onChangeText={setTitulo}
            />

            <Text>Resumo</Text>
            <TextInput
                value={resumo}
                onChangeText={setResumo}
            />

            <Text>Carga Horária</Text>
            <TextInput
                value={cargaHoraria}
                onChangeText={setCargaHoraria}
                keyboardType="numeric"
            />

            <Text>Data de Início</Text>
            <TextInput
                value={dataInicio}
                onChangeText={setDataInicio}
                placeholder="2026-06-08"
            />

            <Text>Vagas</Text>
            <TextInput
                value={vagas}
                onChangeText={setVagas}
                keyboardType="numeric"
            />

            <Text>Área</Text>

            <Picker
                selectedValue={areaSelecionada}
                onValueChange={(valor) =>
                    setAreaSelecionada(valor)
                }
            >

                <Picker.Item
                    label="Selecione uma área"
                    value=""
                />

                {areas.map(area => (

                    <Picker.Item
                        key={area.id}
                        label={area.nome}
                        value={area.id}
                    />

                ))}

            </Picker>

            <Text>Públicos</Text>

            {publicos.map(publico => (

                <View
                    key={publico.id}
                    style={{
                        flexDirection: 'row',
                        alignItems: 'center'
                    }}
                >

                    <Checkbox
                        value={
                            publicosSelecionados.includes(
                                publico.id
                            )
                        }
                        onValueChange={() =>
                            selecionarPublico(
                                publico.id
                            )
                        }
                    />

                    <Text>
                        {' '}
                        {publico.nome}
                    </Text>

                </View>

            ))}

            <Button
                title="Adicionar"
                onPress={adicionar}
            />

            <Button
                title="Atualizar"
                onPress={atualizar}
            />

            <FlatList
                data={cursos}
                keyExtractor={(item) =>
                    item.id.toString()
                }
                renderItem={({ item }) => (

                    <View
                        style={{
                            marginTop: 20,
                            borderWidth: 1,
                            padding: 10
                        }}
                    >

                        <Text>
                            ID: {item.id}
                        </Text>

                        <Text>
                            Título: {item.titulo}
                        </Text>

                        <Text>
                            Vagas: {item.vagas}
                        </Text>

                        <Button
                            title="Editar"
                            onPress={() =>
                                editar(item)
                            }
                        />

                        <Button
                            title="Remover"
                            onPress={() =>
                                remover(item.id)
                            }
                        />

                    </View>

                )}
            />

        </ScrollView>
    );
}