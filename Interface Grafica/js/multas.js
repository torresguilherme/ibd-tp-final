$(document).ready(function() {
	showMore();

	searchTables();

	openERDiagram();
	
	$("#consultar").click(function(){
		consultaAjaxRequest("consulta_usuario.php", $("#consulta"));
	});
	
});

function openERDiagram(){
	$('#diagrama_er').click(function (event) {
		$('#image_modal').modal('show');
	});

	$('#image_modal').click(function (event) {
		$('#image_modal').modal('hide');
	});

	$('#image_container').click(function (event) {
		event.stopPropagation();
	});

	$('#modal_image_close').click(function(event){
		$('#image_modal').modal('hide');
	});
}

function showMore(){
	$("#mostrar_usuario").click(function(){
		ajaxRequest("usuario.php", $("#usuario"), "POST");
	});

	$("#mostrar_infracao_gravidade").click(function(){
		ajaxRequest("infracao_gravidade.php", $("#infracao_gravidade"), "POST");
	});

	
}

function showLess(){
	$("#mostrar_menos_usuario").click(function(){
		ajaxRequest("usuario.php", $("#usuario"), "GET");
	});

	$("#mostrar_menos_infracao_gravidade").click(function(){
		ajaxRequest("infracao_gravidade.php", $("#infracao_gravidade"), "GET");
	});

}

function searchTables(){
	searchByTable($(".usuario"), $(".usuario_search"));
 	searchByTable($(".infracao_gravidade"), $(".infracao_gravidade_search"));
	searchByTable($(".consulta"), $(".consulta_search"));
}

function consultaAjaxRequest(url, selector){
	showAlert("loading", "");

	$.ajax({
		method: "POST",
		url: url,
		data: { query: $('#consulta_text').val() },
		success: function (data) {
			if(data == "denied"){
				showAlert("denied", "");		
			} else if (data == "no_results"){
				showAlert("no_results", "");
			} else if (data.split(':')[0] == "Erro") {
				showAlert("query_error", data);
			} else {
				var aba_consulta = $("#consulta").html();
				var sql = $('#consulta_text').val();
				selector.html(data);
				searchTables();
				swal.close();
				$("#nova_consulta").click(function(){
					$("#consulta").html(aba_consulta);
					$('#consulta_text').html(sql);
					$("#consultar").click(function(){
						consultaAjaxRequest("consulta_usuario.php", $("#consulta"));
					});
					openERDiagram();
				});
			}
		}
	});

}

function ajaxRequest(url, selector, type){
	if(type === "POST"){
		showAlert("loading");
	}

	$.ajax({
		method: type,
		url: url,
		success: function (data) {
			selector.html(data);

			if(type === "POST"){
				swal.close();
				showLess();
			} else {
				showMore();
			}

			searchTables();
		}
	});
}

function showAlert(type, message){
	if(type=="loading"){
		swal({
			title: "Recuperando Informações...",
			showConfirmButton: false,
			imageUrl: "img/loading.gif"
		});
	} else if(type=="denied") {
		swal({  
			title: 'Consulta não aceita!',   
			text: 'Só é possível utilizar comandos de seleção.',
			type: 'error'
		});
	} else if(type=="no_results") {
		swal({  
			title: 'Consulta sem resultados!',   
			text: 'Sua consulta não retornou nenhum resultado.',
			imageUrl: 'img/sad.png'
		});
	} else if(type=="query_error") {
		swal({  
			title: 'Erro na sintaxe da consulta!',   
			text: message,
			imageUrl: 'img/sad.png'
		});
	}
}

function searchByTable(table, input){
	if (table.length > 0) {
		input.keyup(function () {
			var inputs = (input);
			searchByColumn(inputs);
		});

		function searchByColumn(inputs) {
			table.find('tr').removeClass('hide');
			inputs.each(function () {
				var idx = $(this).parent().index();
				var searchVal = $(this).val();
				if (searchVal != "") {
					table.find('tr').not('.hide').each(function (index, row) {
						var allDataPerRow = $(row).find('td').eq(idx);
						if (allDataPerRow.length > 0) {
							var found = false;
							allDataPerRow.each(function (index, td) {
							var regExp = new RegExp(searchVal, "i");
								if (regExp.test($(td).text()) || $(td).text() === "") {
									found = true;
									return false;
								}
							});

							if (found === true) {
								$(row).removeClass('hide');
							} else {
								$(row).addClass('hide');
							}
						}
					});
				}
			});
		}
 	}
}
