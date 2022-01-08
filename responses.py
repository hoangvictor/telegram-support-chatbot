from coin_api import *


def responses_cases(input):
    user_message = str(input).lower()

    if user_message in ("hello", "hi"):
        return "Hi, I'm here to help you!"

    if user_message in ("who are you", "who are you?"):
        return "I'm your bot manager"

    if user_message in ("i love you", "love you", "<3"):
        return "Me too"

    if "coin" in user_message:
        t = user_message.split()
        if len(t) == 2 and t[0] == "coin":
            return coin_price_response(t[1])

    return "I don't understand what you want to say"
