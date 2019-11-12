import random
import click

dict_data = eval(open('dict.txt', 'r', encoding='utf-8').read())

greetings_input = ["hello", 'hi', "hey", "chào", "xin chào", "chào bạn", "chào mày","ê"]
greetings_response = ["hé lô", "xin chào", "chào mày", "chào ku", "chào bạn ^^"]
thanks_input = ["thanks", "thank you", "ty"]
thanks_response = ["ko có chi", "có gì đâu", "ko có gì đâu nà"]

def response(user_response):
    bot_response = ''
    if user_response in greetings_input:
        bot_response = random.choice(greetings_response)
        return bot_response
    if user_response in thanks_input:
        bot_response = random.choice(thanks_response)
        return bot_response

    if user_response in dict_data:
        bot_response = (dict_data[user_response])
        return bot_response

    if user_response == "#edit":
        print ("Bot: hãy nhập từ cần sửa")
        user_edit = input()
        if user_edit in dict_data:
            print ("Bot: muốn sửa thành gì?")
            user_edit_suggest = input()
            dict_data[user_edit] = user_edit_suggest
            with open('dict.txt', 'w', encoding='utf-8') as data:
                data.write(str(dict_data).replace(', ',',\n '))
                bot_response = "cảm ơn mày đã sửa " + (user_edit) + " thành " + (user_edit_suggest)
                return bot_response
        else:
            bot_response = "ko tìm thấy từ cần sửa"
            return bot_response

    else:
        if click.confirm("Bot: cái này tao ko biết. mày có thể chỉ tao ko?", default=True):
            print ("Bot: nó nghĩa là gì?")
            user_new_suggest = input()
            dict_data[user_response] = user_new_suggest
            with open('dict.txt', 'w', encoding='utf-8') as data:
                data.write(str(dict_data).replace(', ',',\n '))
                bot_response = "cảm ơn mày. thì ra " + (user_response) + " là " + (user_new_suggest)
                return bot_response
        else:
            bot_response = "ko thì thôi"
            return bot_response

flag = True
print ("Bot: hi! tao là bot. mày cần tao giúp gì?")
while (flag == True):
    user_response = input()
    user_response = user_response.lower()
    
    if(user_response == "bye"):
        flag = False
        print ("Bot: bảo trọng nha mày. bye...")

    else:
        print ("Bot:", (response(user_response)))