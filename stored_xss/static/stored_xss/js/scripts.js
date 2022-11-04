var sanitizeForm = function () {
	document.getElementById("comment-id").value = document.getElementById("comment-id").value.replace(/[^\w. ]/gi, function (c) {
		return '&#' + c.charCodeAt(0) + ';';
	});
};