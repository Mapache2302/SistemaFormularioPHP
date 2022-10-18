<?php
$NombreCompleto = ""
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <style>
            header {
                width: 80%;
                text-align: center;
                margin: auto;
                margin-top: -20px;
                padding: 5px;
                background-color:rgb(247, 188, 111);
                border-radius: 25px;
                max-width: 650px;
            }
            
            header h1 {
                margin-top: 8px;
                font-size:20px;
                font-family: Arial, Helvetica, sans-serif;
            }
            
            header p {
                line-height: 1px;
                margin-top: -5px;
                font-size: 16px;
                font-style: italic;
            }
            
            img {
                display: block;
                margin-left:auto;
                margin-right: auto;
            }
            
            body {
                background-color: rgb(241, 234, 231) ;
                font-family: sans-serif;
                padding: 20px;
            }
            
            .form1{
                width: 80%;
                margin: auto;
                text-align: center;
                margin-top: 15px;
                padding: 5px;
                background-color:moccasin;
                border-radius: 25px;
                max-width: 650px;
            }
            
            input[type=submit] {
                background-color: rgb(247, 188, 111);
                border: none;
                color: white;
                padding: 5px 35px;
                margin-top: 15px;
                margin-bottom: 15px;
                text-decoration: none;
                cursor: pointer;
            }
            
            input[type=text] {
                background-color: rgb(247, 247, 247);
                text-align: left;
                border: none;
                color: black;
                padding: 5px 25px;
                text-decoration: none;
            }
            
            .textCod {
                margin-left: 20px;
            }
            
            .form1 p {
                display: inline-block;
            }
            
            .nombres {
                text-align: center;
                width: 50%;
            }
            
            .resultNombres {
                text-align: left;
                width: 50%;
            }
            
            .form2 {
                width: 80%;
                margin: auto;   
                margin-top: 15px;
                text-align: center;
                padding: 5px;
                background-color:moccasin;
                border-radius: 25px;
                max-width: 650px;
            }
            
            input[type=radio]{
                vertical-align: middle;
                width: 15px;
                height: 15px;
                border-radius: 10px;
                background: none;
                border: 0;
                box-shadow: inset 0 0 0 1px;
                box-shadow: inset 0 0 0 1.5px;
                appearance: none;
                padding: 0;
                margin: 15px;
                transition: box-shadow 150ms cubic-bezier(.95,.15,.5,1.25);
                pointer-events: none;
                -webkit-tap-highlight-color: transparent;
            }
            
            label{
                padding: 6px;
                border-radius: 25px;
                display: inline-flex;
                cursor: pointer;
                transition: background .2s ease;
                margin: 8px 0;
                -webkit-tap-highlight-color: transparent;
                vertical-align: middle;
                display: inline-block;
                line-height: 1px;
                padding: 0 8px;
            }
            
            label:hover {
                background: rgb(255, 241, 216); 
            }
            
            input[type=radio]:focus {
                outline: none;
            }
            
            input[type=radio]:checked {
                color: darkorange;
                box-shadow: inset 0 0 0 5px;
            }
            
            legend {
                margin-left: 15%;
                margin-top: 25px;
                margin-bottom: 5px;
                font-size: 16px;
                font-family: Arial, Helvetica, sans-serif;
                text-align: left;
            }
            
            label {
                vertical-align: middle;
                display: inline-block;
                line-height: 20px;
                padding: 0 8px;
            }
            
            .form2 p {
                margin-left: 15.6%;
                margin-top: 24px;
                font-size: 16px;
                font-family: Arial, Helvetica, sans-serif;
                text-align: left;
            }
            
            hr{
                border: 0;
                width: 70%;
                max-width: 450px;
                height: 0;
                border-top: 1px solid rgba(0, 0, 0, 0.1);
                border-bottom: 1px solid rgba(255, 255, 255, 0.3);
            }
            
            input[type=text]{
                font-family: inherit;
                width: 65%;
                max-width: 650px;
                border: 0;
                border-bottom: 2px solid gray;
                outline: 0;
                font-size: 16px;
                color: black;
                padding: 7px 0;
                background: transparent;
                transition: border-color 0.2s;
            }
        </style>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>Evaluacion de Tesista/Ponente</title>
    </head>
    <body>
        <header>
            <img src="https://i.ytimg.com/vi/LiZSGpSVWBs/maxresdefault.jpg" alt="imgEscuelaPosgrado" width="85%">
            <h1>Sistema de Evaluación</h1>
            <p>Escuela de Posgrado</p>
        </header>
        <div class="form1" >
            <form action="index.php" method="POST"><!-- TODO: ACCION A REALIZAR PARA BUSCA ALUMNO-->
                <p>Código del Tesista: <input class="textCod" type="text" name="codigoAlumno" placeholder="Código Alumno" required><input type="Submit" name="buscar" value="Buscar"></p><br>
               
               <?php

                if(isset($_POST['buscar'])){
                   echo '<script type= "text/javascript">alert("Alumno encontrado")</script>';
                   $NombreCompleto = "Alumno encontrado";
                }
            
                ?>

                <p class="nombres">Nombres y Apellidos:</p><p class="resultNombres"><?php echo $NombreCompleto?></p>
            </form>

            
        </div>
        <div class="form2"> <!--TODO:ENVIAR A BASE DE DATOS Y A CORREO LA NOTA DEL ALUMNO-->
            <form action="index.php" method="POST">
                <legend>Originalidad</legend>
                <label><input type="radio" name="originalidad" value="1" required>1</label>
                <label><input type="radio" name="originalidad" value="2">2</label>
                <label><input type="radio" name="originalidad" value="3">3</label>
                <label><input type="radio" name="originalidad" value="4">4</label>
                <label><input type="radio" name="originalidad" value="5">5</label>
                <legend>Importancia</legend>
                <label><input type="radio" name="importancia" value="1" required>1</label>
                <label><input type="radio" name="importancia" value="2">2</label>
                <label><input type="radio" name="importancia" value="3">3</label>
                <label><input type="radio" name="importancia" value="4">4</label>
                <label><input type="radio" name="importancia" value="5">5</label>
                <legend>Coherencia</legend>
                <label><input type="radio" name="coherencia" value="1" required>1</label>
                <label><input type="radio" name="coherencia" value="2">2</label>
                <label><input type="radio" name="coherencia" value="3">3</label>
                <label><input type="radio" name="coherencia" value="4">4</label>
                <label><input type="radio" name="coherencia" value="5">5</label>
                <legend>Metodología</legend>
                <label><input type="radio" name="metodologia" value="1" required>1</label>
                <label><input type="radio" name="metodologia" value="2">2</label>
                <label><input type="radio" name="metodologia" value="3">3</label>
                <label><input type="radio" name="metodologia" value="4">4</label>
                <label><input type="radio" name="metodologia" value="5">5</label>
                <legend>Validez de resultados y condiciones</legend>
                <label><input type="radio" name="validez" value="1" required>1</label>
                <label><input type="radio" name="validez" value="2">2</label>
                <label><input type="radio" name="validez" value="3">3</label>
                <label><input type="radio" name="validez" value="4">4</label>
                <label><input type="radio" name="validez" value="5">5</label>
                <legend>Dominio del tema</legend>
                <label><input type="radio" name="dominio" value="1" required>1</label>
                <label><input type="radio" name="dominio" value="2">2</label>
                <label><input type="radio" name="dominio" value="3">3</label>
                <label><input type="radio" name="dominio" value="4">4</label>
                <label><input type="radio" name="dominio" value="5">5</label>
                <p style="position: relative; top: 15px">Anotar al menos dos sugerencias y/o recomendaciones</p>
                <input style="width: 70%; padding: 12px 30px; margin: 8px 0px; box-sizing: border-box;"type="text" name="recomendaciones" placeholder="Sugerencias y/o recomendaciones" required>
                <br><input style="position: relative; top: 15px" type="Submit" name="env" value="Enviar">

                <?php

                ini_set("display_errors", 1);
                error_reporting(E_ALL);
                $con = new mysqli("34.66.23.106", "root", "123", "epgWebPageDB");


                if (!$con)
                {
                    echo 'AAAAAAAAA';
                }

                if(isset($_POST['env'])){

                echo '¡Alumno encontrado!';
                }
                ?>



            </form>
        </div>
    </body>
</html>