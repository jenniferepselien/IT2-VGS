import json

with open('twitter.json', 'r', encoding='utf-8') as file:
    twitter_users = json.load(file)


sorted_users = sorted(twitter_users, key=lambda user: user['followers'], reverse=True)


top_10_users = sorted_users[:10]


print("Topp 10 brukere med flest følgere på Twitter:")
for user in top_10_users:
    print(f"\nBruker: {user['username']}")
    print(f"Antall følgere: {user['followers']}")
    print(f"Antall tweets: {user['tweets']}")
    print(f"Antall de følger: {user['following']}")
    followers_to_following_ratio = user['followers'] / user['following']
    print(f"Følgere/Følger-ratio: {followers_to_following_ratio:.2f}")

