<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

    if($_POST["operacao"]=="soma"){
        echo "<p>".($_POST["numero1"] + $_POST["numero2"])."</p>";
    }else{
        if($_POST["operacao"]=="subtracao"){
            echo "<p>".($_POST["numero1"] - $_POST["numero2"])."</p>";
        }else{
            if($_POST["operacao"]=="multiplicacao"){
                echo "<p>".($_POST["numero1"] * $_POST["numero2"])."</p>";
            }else{
                if($_POST["operacao"]=="divisao"){
                    echo "<p>".($_POST["numero1"] / $_POST["numero2"])."</p>";
                }else{
                    echo "<p>Operação Inválida</p>";
                }
            }
        }
    }

    $lista_disciplinas = $_POST["disciplinas"];

    foreach($lista_disciplinas as $disc){
        echo "<p>$disc</p>";
    }
    

    ?>
</body>
</html>