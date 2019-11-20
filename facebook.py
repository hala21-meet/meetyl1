 list1=[posts]
 list2=[users]
 class user():
	def __init__(self,name,email,password,friends_list,posts):
		self.name = name
		self.email= email 
		self.password = password 
		self.friends_list = friends_list
		self.posts =posts
	def add_friend(self,email):
		self.friends_list.append(email)
		print (self.name + 'has added' + email+ 'as a friend')
	def remove_friend(self,email):
		self.friends_list.remove(email)
		print (self.name + 'has removed' + email + 'as a friend')
	def post (self,text):
		self.posts.append(text)
		print (self.name + 'has posted' + text)
		def get_userInfo (self):
		print ('Name:' + self.name +'Email:' + self.email + 'Password:'+self.password + 'Friends:' + str (self.friends_list )+ 'Posts:' + str (self.posts) )

		class Post(object):
			def __init__(self,name,caption,comments=[]):
				self.name = name 
				self.caption= caption
				self.comments=[]
			def add_caption(self,caption_text):
				self.caption_text=caption_text 
				self.caption_text.append(caption_text):
				print(self.name+"has added"+email + " as a friend")
			def remove_friend (self,email)
			self.friends_list.remove(email)
			print(self.name +_self.name + 
				"

user1= user("Hala","hala99@meet.mit.edu","myhiddenpassword123",[],[])
user2= user("Grandma","grandma44@meet.mit.edu","honeybooboo",[],[])
user1.add_friend('hala99@meet.mit.edu')
user1.post('snowing')
user1.get_userInfo()  













