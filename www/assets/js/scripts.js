$( document ).ready(function() {
    
    
	$("#localisationInput").keyup(function(){
		_autocompletion("load/localisation.html", "#localisationResults", $(this))
	}).focus(function(){
		_autocompletion("load/localisation.html", "#localisationResults", $(this))
	}).focusout(function(){
		$("#localisationResults").hide();
	});

	$('.searchField').change(function(){
		_reloadResearch();
	}).keyup(function(){
		_reloadResearch();
	});

});

function _reloadResearch(){
	var dataSearch = {}; 

	$(".searchField").each(function(){
		var valArray = $(this).val();
		if ($(this).attr("name").slice(0,3) == "chk"){
			if ($(this).is(':checked')){ valArray = "on"; } else { valArray = "off"; }
		}
		dataSearch[$(this).attr("name")] = valArray;
	});
	
	$.ajax({
        url : "load/search.html",
        type : "GET",
        data: dataSearch
    }).done(function(data) {
    	$("#searchResult").html(data);
    	$("#searchResult").show();
   	});
   	//$( "#searchResult" ).load("load/search.html");
}

function _autocompletion(page, resultatContent, inputField){
	if ($(inputField).val().length > 0) {
		$.ajax({
	        url : page,
	        type : "GET",
	        data: { search: $(inputField).val() }
	    }).done(function(data) {
	    	$(resultatContent).html(data);
	    	$(resultatContent).css('width', $(inputField).width() + 7);
	    	$(resultatContent).show();
	   	});
	} else {
		$(resultatContent).hide();
	}
}