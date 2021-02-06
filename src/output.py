class OutputController:
	"""
		Controller that manages data collected being saved to local files\n
		Data should be saved on collection such that an unexpected error will
		not destroy all previously collected data
	"""
	def __init__(self, con):
		self.con = con

	def record_result(self, data):
		pass
