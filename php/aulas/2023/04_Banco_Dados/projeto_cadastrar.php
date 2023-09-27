<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Cadastrar Projeto</h1>
    <form action="projeto_registro_bd.php" method="post">
    <p>
        <label for="codigo">Código</label>
        <input type="text" name="codigo" id="codigo" />
    </p>
    <p>
        <label for="nome">Nome</label>
        <input type="text" name="nome" id="nome" />
    </p>
    <p>
        <label for="data">Data de Início</label>
        <input type="text" name="data_inicio" id="data" />
    </p>
    <p>
        <label for="valor">Valor</label>
        <input type="number" name="valor" id="valor" step="0,01"/>
    </p>
    <p>
        <input type="submit" value="Enviar" />
    </p>
    </form>
</body>
</html>