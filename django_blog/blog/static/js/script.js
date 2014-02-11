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
})

