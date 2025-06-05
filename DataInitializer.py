import service.UserService as user_service
import service.CommentService as comment_service


def populate_empty_db():
    if len(user_service.get_all()) > 0 or len(comment_service.get_all()) > 0:
        return

    data = __get_data()

    for user in data:
        first_name = user["first_name"]
        last_name = user["last_name"]
        comments = user["comments"]
        author_id = str(user_service.add_user(first_name, last_name).user_id.value)

        for comment in comments:
            comment_service.add_comment(author_id, comment)


def __get_data():
    return [
        {
            "first_name": "Albert",
            "last_name": "Einstein",
            "comments": [
                "Life is like riding a bicycle. To keep your balance, you must keep moving.",
                "Imagination is more important than knowledge."
            ]
        },
        {
            "first_name": "Oscar",
            "last_name": "Wilde",
            "comments": [
                "Be yourself; everyone else is already taken.",
                "Always forgive your enemies; nothing annoys them so much."
            ]
        },
        {
            "first_name": "Mahatma",
            "last_name": "Gandhi",
            "comments": [
                "Be the change that you wish to see in the world.",
                "The best way to find yourself is to lose yourself in the service of others."
            ]
        },
        {
            "first_name": "Martin",
            "last_name": "Luther King",
            "comments": [
                "Injustice anywhere is a threat to justice everywhere.",
                "The time is always right to do what is right."
            ]
        },
        {
            "first_name": "Winston",
            "last_name": "Churchill",
            "comments": [
                "Success is not final, failure is not fatal: It is the courage to continue that counts.",
                "If you're going through hell, keep going."
            ]
        },
        {
            "first_name": "Nelson",
            "last_name": "Mandela",
            "comments": [
                "It always seems impossible until it’s done.",
                "Education is the most powerful weapon which you can use to change the world."
            ]
        },
        {
            "first_name": "Mark",
            "last_name": "Twain",
            "comments": [
                "The secret of getting ahead is getting started.",
                "Whenever you find yourself on the side of the majority, it is time to pause and reflect."
            ]
        },
        {
            "first_name": "Eleanor",
            "last_name": "Roosevelt",
            "comments": [
                "No one can make you feel inferior without your consent.",
                "The future belongs to those who believe in the beauty of their dreams."
            ]
        },
        {
            "first_name": "Steve",
            "last_name": "Jobs",
            "comments": [
                "Innovation distinguishes between a leader and a follower.",
                "Your work is going to fill a large part of your life."
            ]
        },
        {
            "first_name": "Theodore",
            "last_name": "Roosevelt",
            "comments": [
                "Believe you can and you're halfway there."
            ]
        },
        {
            "first_name": "Confucius",
            "last_name": "",
            "comments": [
                "It does not matter how slowly you go as long as you do not stop.",
                "Everything has beauty, but not everyone sees it."
            ]
        },
        {
            "first_name": "Benjamin",
            "last_name": "Franklin",
            "comments": [
                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                "An investment in knowledge pays the best interest."
            ]
        },
        {
            "first_name": "Leonardo",
            "last_name": "da Vinci",
            "comments": [
                "Simplicity is the ultimate sophistication."
            ]
        },
        {
            "first_name": "Helen",
            "last_name": "Keller",
            "comments": [
                "Alone we can do so little; together we can do so much."
            ]
        },
        {
            "first_name": "Stephen",
            "last_name": "Hawking",
            "comments": [
                "Intelligence is the ability to adapt to change."
            ]
        },
        {
            "first_name": "Mother",
            "last_name": "Teresa",
            "comments": [
                "If you judge people, you have no time to love them."
            ]
        },
        {
            "first_name": "Dalai",
            "last_name": "Lama",
            "comments": [
                "Happiness is not something ready made. It comes from your own actions."
            ]
        },
        {
            "first_name": "Aristotle",
            "last_name": "",
            "comments": [
                "We are what we repeatedly do. Excellence, then, is not an act, but a habit."
            ]
        },
        {
            "first_name": "Blaise",
            "last_name": "Pascal",
            "comments": [
                "The heart has its reasons which reason knows nothing of."
            ]
        }
    ]
