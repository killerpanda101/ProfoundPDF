css = '''
<style>
.chat-message {
    padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 10%;
}
.chat-message .avatar img {
  max-width: 50px;
  max-height: 50px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1rem;
  color: #fff;
}
footer {
	visibility: hidden;
	}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.icons8.com/carbon-copy/100/bot.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.icons8.com/laces/64/user.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''