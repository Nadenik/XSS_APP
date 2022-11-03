var sanitizeForm = function () {
	document.getElementById("search-text").value = document.getElementById("search-text").value.replace(/[^\w. ]/gi, function (c) {
		return '&#' + c.charCodeAt(0) + ';';
	});
};