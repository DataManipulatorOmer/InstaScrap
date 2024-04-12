from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

# Function to fetch and display Instagram profile information
def get_profile_info(username):
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, username)
    profile_info = {
        "username": profile.username,
        "user_id": profile.userid,
        "num_posts": profile.mediacount,
        "followers": profile.followers,
        "followees": profile.followees,
        "bio": profile.biography,
        "external_url": profile.external_url
    }
    return profile_info

@app.route('/profile', methods=['GET'])
def profile():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Please provide a valid Instagram username."}), 400
    try:
        profile_info = get_profile_info(username)
        return jsonify(profile_info), 200
    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({"error": "Profile not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
