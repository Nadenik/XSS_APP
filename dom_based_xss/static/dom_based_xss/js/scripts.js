window.onload=function(){
    document.getElementById('tweetForm').addEventListener("submit", handleTweetSubmit);
  }


function handleTweetSubmit(e)
{
    e.preventDefault()
    const form_data = new FormData(e.target);
    const tweet_text = form_data.get("tweetText");
    document.getElementById('tweet-container').innerHTML += prepare_tweet(tweet_text)
}

function prepare_tweet(tweet)
{
    return `<div class="m-2">${tweet}</div>`
}