users =[]
posts =[]
class user():
	def __init__(self,name,email,password,friends_list,posts):
		self.name = name
		self.email= email 
		self.password = password 
		self.friends_list = friends_list
		self.posts =posts
		user.append(self)
	def add_friend(self,email):
		self.friends_list.append(email)
		print (self.name + 'has added' + email+ 'as a friend')
	def remove_friend(self,email):
		self.friends_list.remove(email)
		print (self.name + 'has removed' + email + 'as a friend')
	def post (self,text):
		self.posts.append(text)
		print (self.name + 'has posted' + text)
		users.append(posts)
	def get_userInfo (self):
		print ('Name:' + self.name +'Email:' + self.email + 'Password:'+self.password + 'Friends:' + str (self.friends_list )+ 'Posts:' + str (self.posts))
class Post(object):
	def __init__(self,name,caption,comments=[],likes):
		self.name = name 
		self.caption= caption
		self.comment_text=[]
		self.likes=0
	def add_caption(self,caption_text):
		self.caption=caption_text
		print(self.name+"has added"+ caption_text)
	def remove_friend (self,email):
		self.friends_list.remove(email)
		print(self.name + "has removed"+ email +  " as a friend")
	def add_comment (self,comment_text):
		self.comment= comment_text 
		print(self.name + "has added" + comment_text)  
	def add_likes (self):
		pass


user1= user("Hala","hala99@meet.mit.edu","myhiddenpassword123",[],[])
user2= user("Grandma","grandma44@meet.mit.edu","honeybooboo",[],[])
user1.add_friend('hala99@meet.mit.edu')
user1.post('snowing')
user1.get_userInfo()  













