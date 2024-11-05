from instagram_private_api import Client, ClientError

# Enter your Instagram username and password
username = 'your_username'
password = 'your_password'

# Initialize the Instagram API client
api = Client(username, password)

# Function to follow a user
def follow_user(user_id):
    try:
        api.friendships_create(user_id)
        print(f'Successfully followed user with ID: {user_id}')
    except ClientError as e:
        print(f'Error following user with ID: {user_id}. Error message: {e}')

# Function to unfollow a user
def unfollow_user(user_id):
    try:
        api.friendships_destroy(user_id)
        print(f'Successfully unfollowed user with ID: {user_id}')
    except ClientError as e:
        print(f'Error unfollowing user with ID: {user_id}. Error message: {e}')

# Function to like a post
def like_post(post_id):
    try:
        api.post_like(post_id)
        print(f'Successfully liked post with ID: {post_id}')
    except ClientError as e:
        print(f'Error liking post with ID: {post_id}. Error message: {e}')

# Function to unlike a post
def unlike_post(post_id):
    try:
        api.post_unlike(post_id)
        print(f'Successfully unliked post with ID: {post_id}')
    except ClientError as e:
        print(f'Error unliking post with ID: {post_id}. Error message: {e}')

# Function to comment on a post
def comment_on_post(post_id, comment_text):
    try:
        api.post_comment(post_id, comment_text)
        print(f'Successfully commented on post with ID: {post_id}')
    except ClientError as e:
        print(f'Error commenting on post with ID: {post_id}. Error message: {e}')

# Function to delete a comment on a post
def delete_comment(post_id, comment_id):
    try:
        api.delete_comment(post_id, comment_id)
        print(f'Successfully deleted comment with ID: {comment_id} on post with ID: {post_id}')
    except ClientError as e:
        print(f'Error deleting comment with ID: {comment_id} on post with ID: {post_id}. Error message: {e}')

# Example usage
user_id = '123456789'  # Replace with the user ID you want to follow/unfollow
post_id = 'abcdefghi'  # Replace with the post ID you want to like/unlike
comment_text = 'Great post!'  # Replace with your comment text
comment_id = 'jklmnopqr'  # Replace with the comment ID you want to delete

follow_user(user_id)
unfollow_user(user_id)
like_post(post_id)
unlike_post(post_id)
comment_on_post(post_id, comment_text)
delete_comment(post_id, comment_id)
