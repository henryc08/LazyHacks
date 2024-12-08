from lazyAI import ChatSession

session = ChatSession()

session.send_message("hello")
session.send_message("oh really")
session.send_message("amazing")
session.send_message("thanks")
session.send_message("good morning")

for msg in session.get_chat_history():
    a = str(msg.parts[0])
    if msg.role == "user":
        print("User: " + a[7:len(a)-2])
    elif msg.role == "model":
        print("Model: " + a[7:len(a)-2])
    
    