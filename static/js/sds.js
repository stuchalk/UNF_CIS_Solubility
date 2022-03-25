// javascript functions for the SDS project
$(document).ready(function() {
	// click a button to show a list be letter
	$(".browse").click(function () {
		let letter = $(this).attr('data-char');
		$('.letter').hide();
		$('#' + letter).show();
	});
	// search for resources via data on the page
	$("#search").on('input', function () {
		e.preventDefault();
		let val = $(this).val();
		let letters = $(".letter");
		if (val.length < 3) {
			letters.find("li").show();
			letters.hide();
			letters.first().show();
		} else {
			letters.show();
			letters.find("li").show();
			$("#results li:not(:contains('" + val + "'))").hide();
		}
	});
	// show the references for a system (authors/view)
	$(".system").click(function () {
		let sysid = $(this).attr('sysid');
		$(".refs").addClass('showHide');
		$("#" + sysid).toggleClass('showHide');
	});
	// used to show/hide critical evaluation text
	$(".toggle").click(function (e) {
		e.preventDefault();
		$(this).parents(".row").find(".sectionContent").toggle();
		if ($(this).text() === "-") {
			$(this).text("+");
		} else {
			$(this).text("-");
		}
	});
	// show reports in list (substances/view)
	$(".showreports").on('click', function (e) {
		e.preventDefault();
		$(".sysreports").hide();
		$(this).siblings(".sysreports").show();
	});
})