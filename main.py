import instaloader
import argparse
from colorama import *
init()

def get_profile_info(username):

    loader = instaloader.Instaloader()

    try:

        profile = instaloader.Profile.from_username(loader.context, username)


        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")
        print(f"Private: {profile.is_private}")
        print(f"Verified: {profile.is_verified}")
        print(f"Profile URL: https://www.instagram.com/{profile.username}/")


        if not profile.is_private:
            print("\nRecent Posts:")
            for post in profile.get_posts():
                print(f"- Post URL: https://www.instagram.com/p/{post.shortcode}/")
                print(f"  Likes: {post.likes}")
                print(f"  Comments: {post.comments}")
                print(f"  Caption: {post.caption}")
                print(f"  Date: {post.date}")
                print()

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Profile '{username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():

    parser = argparse.ArgumentParser(description="Instagram OSINT Tool")
    parser.add_argument("username", type=str, help="Instagram username to gather information about")
    args = parser.parse_args()


    get_profile_info(args.username)

if __name__ == "__main__":
    main()