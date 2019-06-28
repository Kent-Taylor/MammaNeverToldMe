document.getElementById("post-btn").addEventListener('click', send);

function send() {
    let postTitle = document.getElementById("postTitle").value;
    let postContent = document.getElementById("postContent").value;

    if (postTitle != '' || postContent != '') {
        console.log(postTitle);
        console.log(postContent);        
    } else {
        console.log('Please fill out Text Area')
    }
}

