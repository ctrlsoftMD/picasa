/* Russian (UTF-8) initialisation for the jQuery UI date picker plugin. */
/* Written by Andrew Stromnov (stromnov@gmail.com). */
jQuery(function($){
	$.datepicker.regional['ru'] = {
		closeText: '?�?�??N�N�N�N?',
		prevText: '&#x3c;?YN�?�??',
		nextText: '???�?�??&#x3e;',
		currentText: '???�????????N?',
		monthNames: ['???????�N�N?','?�?�??N�?�?�N?','???�N�N�','????N�?�?�N?','???�??','??NZ??N?',
		'??NZ?�N?','??????N?N?N�','???�??N�N??�N�N?','?z??N�N??�N�N?','????N??�N�N?','?�?�???�?�N�N?'],
		monthNamesShort: ['??????','?�?�??','???�N�','????N�','???�??','??NZ??',
		'??NZ?�','??????','???�??','?z??N�','????N?','?�?�??'],
		dayNames: ['????N???N�?�N??�??N??�','???????�???�?�N???????','??N�??N�??????','N?N�?�???�','N�?�N�???�N�??','??N?N�????N�?�','N?N??�?�??N�?�'],
		dayNamesShort: ['??N???','??????','??N�N�','N?N�??','N�N�??','??N�??','N??�N�'],
		dayNamesMin: ['?�N?','?Y??','?�N�','??N�','?�N�','?YN�','???�'],
		weekHeader: '???�??',
		dateFormat: 'dd.mm.yy',
		firstDay: 1,
		isRTL: false,
		showMonthAfterYear: false,
		yearSuffix: ''};
	$.datepicker.setDefaults($.datepicker.regional['ru']);
});