/*
 * b is for Blaise. handle blaise survey errors / dummy behaviours
 */
ds.b = {};
/*

    ========================
    ---- INITIALISATION ----
    ========================

*/
	
ds.b.init = function(){


	// add intit function
	ds.resize();
	$( window ).on("resize", ds.resize );
	// initialize events
	$(document).on("touchstart", ".ds-button,.ds-input, .ds-retinic", ds.b.magic.touchstart );
	
	$(document).on("touchstart",".dww", ds.b.magic.wheel.touchstart );
	$(window).on("touchend", ds.b.magic.touchend );
	$(document).on("click", ds.b.magic.touchclick );
	
	//.dww.
	$(document).on("touchstart",".ds-enumeration", ds.b.magic.enumeration.touchstart );
	$(document).on("touchend",".ds-enumeration", ds.b.magic.enumeration.touchend );
	$(document).on("click", "input[type=checkbox]", function(event){event.preventDefault();});

	// intialize datescrollers
	$(".ds-date").scroller({
	preset: 'date',
	    theme: 'android-ics light',
	    display: 'modal',
	    setText:'selectionner',
	    cancelText:'annuler',
	    mode: 'scroller',
	    dateFormat:'dd/mm/yyyy',
	    dayText:'jour',
	    monthText: 'mois',
	    yearText:'Annee',
	    monthNames:ds.vars.full_months.fr,
	    dateOrder: 'D ddMMyy',
	    width: 105,
	    dayNamesShort:[ 'Dim.', 'Lun.', 'Mar.', 'Mer.', 'Jeu.', 'Ven.', 'Sam.' ]
	}).click(function(){
	    $("input[type=date]").scroller('show'); 
	    return false;
	});

	// show all input

	$(".answer input").addClass("in"); 
	$("#question-info").addClass("in");

	ds.b.magic.enumeration.init();
	$(".mini-section").show();//( "fast");
	$(".ds-button").show();
	$("#blaise-lower-panel").show();
}


/*

    ===============
    ---- MAGIC ----
    ===============
*/

ds.b.magic = {};
ds.b.magic.uninvalidate = function(){
	$(".invalid").removeClass("invalid");	
}
ds.b.magic.touchstart = function( event ){
	var el = $(this);
	el.addClass("touched");

	if( event.currentTarget.className.indexOf("ds-retinic") != -1 ){
 		el.children().addClass("touched");	
 	}

 	
 	
	ds.b.magic.uninvalidate();
	
	// start timer for touchstart( because of people leaving their fingers on the bttons...)
	clearTimeout(  ds.b.magic._touchtimer );
	ds.b.magic._touchtimer = setTimeout( ds.b.magic.touchwait, 600 );
	ds.b.magic._touched = el;
	
	//event.preventDefault();
	

}
ds.b.magic.touchwait = function( ){
	ds.b.magic._touched.trigger("click");
	ds.b.magic._touched.removeClass("touched");
}


ds.b.magic.touchclick = function(event){
	clearTimeout(  ds.b.magic._touchtimer );
	if( typeof ds.b.magic._touched != "undefined" ){
		
		if( ds.b.magic._touched.hasClass("ds-lock") != -1 ){
 			ds.magic.lock();
 		}

		if(  ds.b.magic._touched.hasClass("ds-loading") != -1 ){
	 		ds.toast( ds.i18n.translate("loading"),{stayTime:5000, cleanup:true});
	 	}
	 	
	}
	ds.b.magic._touched = undefined;
	
	
}
ds.b.magic.touchend= function( event ){
	$(".touched").removeClass("touched");
}

ds.b.magic.wheel = {}
ds.b.magic.wheel.touchstart = function(event){
	$( this ).addClass("touched");
}


ds.b.magic.enumeration = {};

ds.b.magic.enumeration.init = function(){
	try{
		$("input:checked").parent().addClass("selected");

	} catch( e ){

	}

}
ds.b.magic.enumeration.touchstart = function(event){
	$(".touched").removeClass("touched");
	$(this).addClass("touched");
}
ds.b.magic.enumeration.touchend = function(event){
	// alert("touched!");
	var el = $(this);

	// check data-multiple-limit on parent
	

	// RADIO BUTTON
	if( el.find("[type=radio]").length ){
		ds.log("jejeje");
		el.siblings().removeClass("selected");
		el.addClass("selected");
		el.children("input").attr("checked","checked");
	} else if( el.find("[type=checkbox]").length ){
		var checkbox = el.children("input");
		checkbox.attr("checked",!checkbox.attr("checked"));

		if( checkbox.attr("checked") ) 
			el.addClass("selected");
		else
			el.removeClass("selected");
		//if ( el.parent().attr('data-multiple-limit') && el.parent().find("input:checked").length > el.parent().attr('data-multiple-limit') ){
		//	ds.toast("deux choix possibles!", ds.i18n.translate("error") );
		//}

	}
	event.stopImmediatePropagation();
}
/*

    ===============
    ---- ERROR ----
    ===============
*/

ds.b.error = {};
ds.b.error.init = function(){

	// load ds.vars
	ds.log("[ds.b.error.init]", ds.vars.errors );
	ds.toast( ds.i18n.translate("form errors"),ds.i18n.translate("warning"),{cleanup:true});	
}

/*

    ==================
    ---- phonegap ----
    ==================
*/
ds.b.gap = { status:"online"}
ds.b.gap.init= function(){
	$(document).on("offline", ds.b.gap.offline );
	$(document).on("online", ds.b.gap.online );

}
ds.b.gap.online = function(){
	ds.b.gap.status = "online";
}

ds.b.gap.offline = function(){
	ds.b.gap.status = "offline";
	ds.toast( ds.i18n.translate("check internet connection"), ds.i18n.translate("offline device"), {stayTime   : 5000, cleanup: true} );
} 


/*

    ==================
    ---- phonegap ----
    ==================
*/
