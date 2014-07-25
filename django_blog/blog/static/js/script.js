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

})

