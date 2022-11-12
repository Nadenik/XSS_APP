window.onload=function(){
    document.getElementById('textForm').addEventListener("submit", handleTweetSubmit);
  }


function handleTweetSubmit(e)
{
    e.preventDefault()
    const myForm = e.target
    const form_data = new FormData(myForm)
    const method = 'POST'
    const url = `level1/create`
    const csrftoken = getCookie('csrftoken')
    const xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.responseType = "json"
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    xhr.onload = () => 
    {   if (xhr.status === 200)
        {
        const text = form_data.get("text");
        document.getElementById('text-container').innerHTML += prepare_tweet(text, xhr.response.id)
        }
        else{
            console.log("error occured")
        }
    }
    console.log(form_data)
    xhr.send(form_data)
}



function prepare_tweet(text, id)
{
    return `<div id=device${id} class='col-12 py-3 mb-4 border-top border-bottom'><p>
    ${text}
   <br><a href='' button type="button" class="btn btn-danger" >Delete</a></div>`
}


var delete_text = function (id) 
{
	const xhr = new XMLHttpRequest()
    const method = 'DELETE'
    const url = `level1/delete/${id}`
    const csrftoken = getCookie('csrftoken')
    
    xhr.open(method, url)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    xhr.onload = () => 
    {
      document.getElementById(`text${id}`).remove();
    }
    xhr.send()
}