<?php
  setcookie('etatswitch', 'non-secu')
  ?>
<!DOCTYPE html>
<html>

<head>
    <title>IHM Panneau Solaire</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script type="text/javascript" src="js/gauge.min.js"></script>
    <script src="js/switch.js"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="bootstrap-5.dist/css/bootstrap.min.css">
</head>

<body>
    <h1>IHM Panneau Solaire</h1>
    <div class="topnav" id="myTopnav">
        <a href="#home" class="active">Home</a>
        <a href="#Modepanneau">Mode du Panneau Solaire</a>
        <a href="#MM">Valeur du Vent</a>
        <a href="#about" id="automatique">Mode Sécurisé</a>
        <a href="javascript:void(0);" class="icon" onclick="myFunction()">
            <i class="fa fa-bars"></i>
        </a>
    </div>

    <div style="padding-left:16px">
        <div id="Modepanneau">
            <h2 id="modepanel">Mode du Panneau Solaire</h2>
            <input type="button" value="Mode Automatique" id="auto" onclick="cacherauto()" class="btn btn-primary">
            <input type="button" value="Mode Manuel" id="manu" onclick="affichermanu()" class="btn btn-primary">
        </div>
        <div id="value">
            <h2>Valeur du vent à Toulouse</h2>
            <h2 id="VM"><small>Vent Moyen : 15.28 m.s</small></h2>
            <h2 id="VR"><small>Vent en Rafale : 18 m.s</small></h2>
            <h2 id="DV"><small>Direction du vent : NW (315°)</small></h2>
            <!--<img src="image/rosedesvent.jpg"class="img-responsive" alt="Responsive image">-->

        </div>
        <div id="MM">
        </div>
        <div id="automatiqueswitch">
            <h2>Mode :</h2>
            <h3 id="etatSwitch" class="color1">Non sécurisé</h3>
            <label class="switch">
                <input type="checkbox">
                <div class="slider"></div>
            </label>
            <?php
            if(isset($_COOKIE['user_id'])){
                echo 'Votre ID de session est le ' .$_COOKIE['user_id'];
            }
        ?>
        </div>
        <canvas id="myChart"></canvas>
        <canvas id="myChart1"></canvas>
</body>
<div>
    <script type="text/javascript" src="js/script.js"></script>
    <script type="text/javascript" src="js/chart.js"></script>
    <script type="text/javascript" src="js/chart1.js"></script>
    <script type="text/javascript" src="js/Chart.min.js"></script>
</div>

</html>