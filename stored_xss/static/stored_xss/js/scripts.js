var sanitizeForm = function () {
	document.getElementById("comment-id").value = document.getElementById("comment-id").value.replace(/[^\w. ]/gi, function (c) {
		return '&#' + c.charCodeAt(0) + ';';
	});
};

var delete_comment = function (id) 
{
	const xhr = new XMLHttpRequest()
    const method = 'DELETE'
    // /learn/stored_xss/level2
    level = window.location.pathname.split('/')[3]
    const url = `${level}_delete_comment/${id}`
    const csrftoken = getCookie('csrftoken')
    
    xhr.open(method, url)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    xhr.onload = () => 
    {
      document.getElementById(`comment${id}`).remove();
    }
    xhr.send()
}

var delete_image = function (id) 
{
	const xhr = new XMLHttpRequest()
    const method = 'DELETE'
    const url = `level3_delete_image/${id}`
    const csrftoken = getCookie('csrftoken')
    
    xhr.open(method, url)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    xhr.onload = () => 
    {
      document.getElementById(`image${id}`).remove();
    }
    xhr.send()
}