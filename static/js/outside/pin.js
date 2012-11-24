var oo = oo || {}; oo.vars.pin = oo.vars.pin || {};

/*


    Magic
    =====

*/
oo.magic = oo.magic || {};
oo.magic.pin.add = function( result )


/*


    Pin Restful API
    ===============

*/
oo.api.pin = {};

oo.api.pin.add = function( param ){
	$.ajax( $.extend( oo.api.settings.get,{
		url: oods.urls.add_pin, ds.vars.survey.id ),
		data: typeof params == "undefined"? { limit: ds.vars.survey.more.user_selection.limit }: params, 
		success:function(result){
			ds.log( "[ds.m.api.assistant.get_unanswered_messages] result:", result );
			ds.m.api.process( result, ds.m.magic.survey.get_user_selection );
		}
	}));
}
