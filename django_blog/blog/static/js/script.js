$(document).ready(function(){		
	$("#id_wording").markdown({
		autofocus:false,
		savable:false,
		width:768,	
		iconlibrary:'fa',	
		onPreview: function(e) {
		    var previewContent
		    var $textarea = $('#id_wording'),
		    convert = new Markdown.Converter().makeHtml;
		    previewContent = convert($textarea.val());
		    

		    return previewContent
		 },
	});

	// Exibe Imagem no post
	var img_href = $('.file-upload').find('a').attr('href');
	var img_tag = '<img src="' + img_href + '" width="270" height="160" alt="admin img">';
	$('.file-upload').prepend(img_tag);

	//preview Imagem
	$('#id_img_post').change(function(){		
		// $('.file-upload').html('');
		$('#preview-img').remove()
		mostraImagem($(this.files));

	})


})

//Mostra a Imagem utilizando a API FILE do html5
function mostraImagem(files){
	//Seleciona elemento
	div_img = document.getElementsByClassName('field-img_post');

	//Pega a primeira posição do objeto file do input
	var file = files[0];
	//Cria uma imagem
	var img = document.createElement("img");
	img.setAttribute('style','margin:20px 0 0 180px; float:left;');
	img.setAttribute('width','270');
	img.setAttribute('width','160');
	img.setAttribute('id','preview-img')
	img.file = file;

	div_img[0].appendChild(img)
	// Mostra 
	console.dir(file)
	
	// Cria um leitor
	var reader = new FileReader();
	reader.onload = (function(aImg) {return function(e) {aImg.src = e.target.result;};})(img);
	reader.readAsDataURL(file);
}
