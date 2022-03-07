// javascript functions for the SDS project
$(document).ready(function() {
	// click a button to show a list be letter
	$(".browse").click(function () {
		let letter = $(this).attr('data-char');
		$('.letter').addClass('hidden');
		$('#' + letter).removeClass('hidden');
	});
	// search for resources via data on the page
	$("#search").on('input', function () {
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
	$(".showReport").click(function (e) {
		e.preventDefault();
		$(".showHide").hide();
		$(this).nextAll(".showHide").toggle(); // requires element with class 'showHide' is a following sibling
	});
})