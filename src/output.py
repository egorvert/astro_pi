class OutputController:
	"""
		Controller that manages data collected being saved to local files\n
		Data should be saved on collection such that an unexpected error will
		not destroy all previously collected data
		
		:param con: Reference to main controller
		:type con: main.Controller
	"""
	def __init__(self, con):
		self.con = con

	def record_result(self, data):
		"""
			Records a result and saves it to the current records file

			:param data: Data to record
		"""
		pass
