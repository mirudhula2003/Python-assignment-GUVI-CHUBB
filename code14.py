import re

def extract_hashtags(post):
    hashtags = re.findall(r'#\w+', post)
    unique = sorted(set(hashtags))
    return unique
post = "learning is #fun and learning #python is even more #fun. #ai #machine"

unique = extract_hashtags(post)
print(unique)

