function xss() {
    var xhr = new XMLHttpRequest();
    const method = 'POST'
    const url = ''
    xhr.open(method,url)
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    xhr.onload = () => {
        alert("Congratulations!")
      };
    xhr.send()
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}