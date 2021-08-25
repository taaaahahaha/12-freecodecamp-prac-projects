# Taaha Multani @ https://github.com/taaaahahaha
# (C) Kylie Ying @ https://www.github.com/kying18 

def madlib():
    body_part = input("Body part: ")
    verb = input("Verb: ")
    adj = list(i for i in input("Five Adjectives: ").split())
    noun = list(i for i in input("Two Nouns: ").split())
    noun_plural = list(i for i in input("Two Plural Nouns: ").split())

    
    madlib = f"I love computer programming because it's {adj[0]}! The journey to becoming a \
good programmer starts with hope in your mind and a dream in your {body_part}. Through blood, \
sweat, and {noun_plural[0]}, hopefully it never ends. Yes, once you learn to {verb}, it becomes \
a part of your life identity and you can become a super {adj[1]} hacker. Knowledge of programming \
lets you take control of your {noun[0]}. You can create your own personal {noun_plural[1]}, anything \
from developing {adj[2]} software to analyzing data and making predictions about the {noun[1]}. You can \
maybe even recreate Jarvis and make him extra {adj[3]}. I hope you'll start your {adj[4]} journey by \
coding with Kylie :)"

    print(madlib)

if __name__=='__main__':
    madlib()
