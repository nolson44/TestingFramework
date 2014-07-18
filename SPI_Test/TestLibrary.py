import subprocess

class TestLibrary:
	"""
	This test uses the subprocess method, Popen, to run the executable, ch, and open a pipe
	to ch's stdin and stdout. The communicate method send the parameter to stdin and returns
	a tuple, (stdout, stderr). The results of stdout are compared to the expected output. If
	they do not match, then the test fails.
	"""
	def match_input_to_output(self, givenInput, expectedOutput):
		process = subprocess.Popen("./ch", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		output = process.communicate(givenInput)
		if not output[0] == expectedOutput:
			raise AssertionError("Input did not match output.")

