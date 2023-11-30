// templates/postdelete.js
document.addEventListener("DOMContentLoaded", function() {
    const deleteBtn = document.getElementById("deleteBtn");
    deleteBtn.addEventListener("click", function() {
        if (confirm("Are you sure you want to delete this post?")) {
            // Implement the logic to delete the post using AJAX or a form submission
            alert("Post deleted!");
            window.location.href = "{% url 'postlist' %}";
        }
    });
});
