<script>
    document.addEventListener('DOMContentLoaded', function () {
        fetchPosts();
    });

    function fetchPosts() {
        fetch('http://127.0.0.1:8000/blog/posts/')
            .then(response => response.json())
            .then(data => {
                const postList = document.getElementById('postList');
                postList.innerHTML = ''; 

                data.forEach(post => {
                    const listItem = document.createElement('li');
                    listItem.classList.add('col');
                    listItem.classList.add('mb-4');
                    listItem.innerHTML = `
                        <div class="card h-100">
                            <div class="card-body">
                                <h5 class="card-title">${post.title}</h5>
                                <p class="card-text">${post.content.length > 15 ? post.content.substring(0, 15) + '...' : post.content}</p>
                                <small class="text-muted">Created at: ${new Date(post.created_at).toLocaleString()}</small>
                                <button type="button" onclick="deletePost(${post.id})" class="btn btn-sm btn-danger delete-btn mt-2">Delete</button>
                            </div>
                        </div>
                    `;

                    postList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching posts:', error));
    }

    function createPost() {
        const title = document.getElementById('title').value;
        const content = document.getElementById('content').value;

        fetch('http://127.0.0.1:8000/blog/posts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, content }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Successfully created post:', data);
            fetchPosts(); 
        })
        .catch(error => console.error('Error creating post:', error));
    }
    
    function deletePost(postId) {
        fetch(`http://127.0.0.1:8000/blog/posts/${postId}/`, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.ok) {
                console.log('Successfully deleted post:', postId);
                fetchPosts(); 
            } else {
                console.error('Error deleting post:', response.statusText);
            }
        })
        .catch(error => console.error('Error deleting post:', error));
    }
</script>