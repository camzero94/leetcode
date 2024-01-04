from collections import defaultdict

class ListNode:
	def __init__(self, val:int, next = None, prev = None):
		self.val = val 
		self.next = next 
		self.prev = prev

class LinkedList:
	def __init__(self, cap: int):
		self.head = None
		self.tail = None
		self.cap = cap
		self.curr_cap = 0
	def add_2_list(self,val):
		new_node = ListNode(val)
		if not self.tail and not self.head:
			new_node.next = None
			new_node.prev = None
			self.head = new_node
			self.tail = new_node
		else:	
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def remove_from_list(self,ptr_val:ListNode):

		pass

class LRUCache:
	def __init__(self, capacity: int):
		self.key_storage = defaultdict(list)
		self.link_listed = LinkedList(capacity)

	# When  Return the value of the key if the key exists, otherwise return -1 
	def get(self, key: int) -> int:
		# Get value and ptr to cache linked list
		val, idx_cache= self.key_storage[key]	

		# Case Node is at the head
		if not idx_cache.prev :
			pass
		else:
			idx_cache.next = self.head
			self.tail = idx_cache.prev
			idx_cache.prev = None
			self.tail.next = None
			self.head = idx_cache

		return val
        
	def put(self, key: int, value: int) -> None:
		# # Get value and ptr to cache linked list
		# val, idx_cache= self.key_storage[key]	
		# # Create new node
		# # Insert val in the linked list if first node 
		# new_node = ListNode(val)
		# if not self.head and not self.tail: 
		# 	self.head = new_node	
		# 	self.tail= new_node	
		# 	self.curr_cap += 1 
		# elif self.curr_cap < self.cap:
		pass
        


if __name__ == "__main__":

	link_list = LinkedList(5)
	link_list.add_2_list(1)
	link_list.add_2_list(2)
	link_list.add_2_list(3)
	link_list.add_2_list(4)

	curr = link_list.tail
	while curr:
		print(curr.val)
		curr = curr.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

