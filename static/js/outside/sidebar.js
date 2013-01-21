var oo = oo || {}; oo.vars.sidebar = oo.vars.sidebar || {};

oo.sidebar = {  is_hidden:false, element:[] };
oo.sidebar.init = function(){
	oo.log("[oo.sidebar.init]");
	oo.sidebar.is_hidden = false;
	oo.sidebar.element = $("sidebar");
	$("#collapse-menu").click( oo.sidebar.collapse );
	$("#expand-menu").click( oo.sidebar.expand );

	var page_height = $(".page").first().height();
	var sidebar_height = $("#right-sidebar").height();

	$("#right-sidebar").height( Math.max( page_height,sidebar_height ) );
}

oo.sidebar.collapse = function(){
	oo.sidebar.element.addClass("collapsed");
	$("#collapse-menu").hide();
	$("#expand-menu").show();
}

oo.sidebar.expand = function(){
	oo.sidebar.element.removeClass("collapsed");
	$("#collapse-menu").show();
	$("#expand-menu").hide();
}

