<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Linux | Home</title>
		<!-- CSS -->
	    <link href="css/bootstrap-responsive.min.css" rel="stylesheet">
	    <link href="css/bootstrap.min.css" rel="stylesheet">
	    <link href="css/sweetalert.css" rel="stylesheet">
        <link href="css/style.css" rel="stylesheet">
        <link href="css/cover.css" rel="stylesheet">
		<link href='https://fonts.googleapis.com/css?family=PT+Sans+Narrow:400,700' rel='stylesheet' type='text/css'>
        <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Oswald:400,700" rel="stylesheet">
        
	    <!-- Scripts --> 	
	    <script src="js/jquery-2.1.3.min.js"></script>
	    <script src="js/bootstrap.min.js"></script>
	    <script src="js/sweet-alert.js"></script>
	    <script src="js/script.js"></script>
	</head>
	<body>
    <header>
            <p class="logo">Linux</p>
            <nav>
                <a href="index.php">Home</a>
                <a href="#">Sobre</a>
            </nav>
        
        <div class="banner2">
            <div class="heading_content">
                <h1>Distribuições GNU/Linux</h1>
                <a href="banco.php#consulta" class="btn">Consultas SQL</a>
            </div>
            
            <div class="banner_bg">
                    <img src="img/gnu-linux-f.png" alt="Tux" class="linux-logo">
            </div>
        </div>
        </header>
		<div id="wrapper">
        

			<div id="content" class="col-lg-offset-1 col-lg-10">
				<ul class="nav nav-tabs" role="tablist">
					<li role="presentation" class="active"><a href="#usuario" aria-controls="usuario" role="tab" data-toggle="tab">Usuários</a></li>
					<li role="presentation"><a href="#distro" aria-controls="distro" role="tab" data-toggle="tab">Distros</a></li>
					<li role="presentation"><a href="#consulta" aria-controls="consulta" role="tab" data-toggle="tab">Faça Sua Consulta</a></li>
				</ul>

				<!-- Tab panes -->
				<div class="tab-content">
					<div role="tabpanel" class="tab-pane active" id="usuario"><?php include 'usuario.php'?></div>
					<div role="tabpanel" class="tab-pane" id="distro"><?php include 'consulta_distro.php'?></div>
					<div role="tabpanel" class="tab-pane" id="consulta">
						<div class="form-group col-lg-8">
							<br/>
							<label for="consulta">Digite sua consulta:</label>
							<textarea class="form-control" rows="6" id="consulta_text">SELECT * FROM distro</textarea>
							<br/>
							<button type='button' id='consultar' class='btn btn-primary'>
								<span>Consultar</span>
							</button>
						</div>
						<div class="col-lg-4">
							<br/>
							<label for="diagrama_er">Modelo Relacional:</label>
							<a href="#" id="diagrama_er" class="thumbnail">
								<img src="img/Relacional.png" alt="Diagrama ER">
							</a>
							<div id="image_modal" class="modal fade" tabindex="-1" role="dialog" aria-hidden="true">
								<div id="image_container" class="modal-content">
									<div class="modal-body">
										<div>
											<a id="modal_image_close" href="#" class="icon_close">
											<span class="glyphicon glyphicon-remove"></span>
											</a>
										</div>
										<img src="img/Relacional.png" class="img-responsive">
									</div>
								</div>
							</div>
						</div>				
					</div>
				</div>
				<div id="push"></div>			
			</div>
			
		</div>
		<div id="footer" class="col-lg-12">
			<div class="col-lg-2">
				<img src="img/dcc.png" class="footer-img" alt="Logo DCC">
			</div>
			<div class="col-lg-offset-1 col-lg-2 mt-8">
				<span>Introdução a Banco de Dados.</span><br/>
				<span>Prof. Mirella Moro</span><br/>
				<span>2018/2</span>
			</div>
			<div class="col-lg-2">
				<span>Deiziane Silva</span><br/>
				<span>Guilherme Torres</span><br/>
				<span>Hiago Souza</span>
			</div>
			<div class="col-lg-2">
				<p>Dados fictícios com o propósito de uso apenas para disciplina.</p>
			</div>
			<div class="col-lg-offset-1 col-lg-2">
				<img src="img/ufmg2.png" class="footer-img" alt="Logo UFMG">
			</div>
		</div>
	</body>
</html>
