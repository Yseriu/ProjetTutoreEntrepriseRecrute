<!doctype html>
<html lang="fr">
	<head>
	  <meta charset="utf-8">
	  <title>Chez Tux, emplois facile</title>
	  <link rel="stylesheet" href="assets/css/style.css">
	</head>
	<body>
	  
	  <header id="menu">
	  	<?php include("templates/menu.php"); ?>					
	  </header>
	  
	  <section id="topHeader">
	  	<h1>réseau, sécurité</h1>
	  	<span class="puce"><b>45</b> résultats trouvé</span>
	  </section>
	  
	  <section id="bodyPage">
	  	<nav>
	  		<h4>affiner sa recherche</h4>
	  		<ul>
	  			<li>
	  				<h5>Activité</h5>
	  				<ul class="sousMenu">
	  					<li><label><input class="searchField" name="chk:Securite" type="checkbox">Sécurité</label><span>2</span></li>
	  					<li><label><input class="searchField" name="chk:Environnement" type="checkbox">Environnement</label><span>4</span></li>
	  					<li><label><input class="searchField" name="chk:BDD" type="checkbox">Base de données</label><span>6</span></li>
	  					<li><label><input class="searchField" name="chk:Telephonie" type="checkbox">Téléphonie</label><span>5</span></li>
	  				</ul>
	  			</li>
	  			<li>
	  				<h5>Niveau étude requis</h5>
	  				<ul class="sousMenu">
	  					<li><label><input class="searchField" name="chk:+2" type="checkbox">+2 (DUT)</label></li>
	  					<li><label><input class="searchField" name="chk:+3" type="checkbox">+3 (Licence)</label></li>
	  					<li><label><input class="searchField" name="chk:+5" type="checkbox">+5 (Master)</label></li>
	  					<li><label><input class="searchField" name="chk:+8" type="checkbox">+8 (Doctorat)</label></li>
	  				</ul>
	  			</li>
	  			<li>
	  				<h5>Localisation</h5>
	  				<input type="text" id="localisationInput" class="searchField" name="txt:localisation" placeholder="Code postale, Ville, Pays"/>
	  				<ul id="localisationResults" class="autocompletionText">
	  					<!-- RESULTAT DE L'AUTOCOMPLETION LOCATISATION -->
	  				</ul>
	  			</li>
	  			<li>
	  				<h5>Salaire</h5>
	  				<input type="text"/>
	  			</li>
	  		</ul>
	  	</nav>
	  	<section>
	  		<h2>Liste des resultats</h2>
		  	<ul id="searchResult">
		  		
		  	</ul>

	  	</section>
	  </section>
	  
	</body>
	<script src="assets/js/jquery.js"></script>
	<script src="assets/js/script.js"></script>
	<script type="text/javascript">
		$( document ).ready(function() {
			_reloadResearch();
		});
	</script>
</html>