
document.getElementById("post-btn").addEventListener('click', send);

function send() {
    let postTitle = document.getElementById("postTitle").value;
    let postContent = document.getElementById("postContent").value;

    if (this.postTitle != '' && this.postContent != '') {        
        const dataSend = new main(postTitle, postContent);
        dataSend.datacheck();

    } else {
        console.log('Please fill out Text Area');

    datacheck()
}

    class main {
        constructor (postTitle, postContent) {
            this.postTitle = postTitle;
            this.postContent = postContent;
        }

        datacheck() {
            postTitle = this.postTitle;
            postContent = this.postContent;
            return jsonify(postTitle, postContent);
            }
        }
    }


