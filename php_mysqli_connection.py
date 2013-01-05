import sublime, sublime_plugin

class PhpMysqliConnectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		command = '<?php\n$mysql_server = "localhost";\n$mysql_user = "root";\n$mysql_password = "";\n$mysql_db = "DATABASE_NAME"; #replace with actual db name\n$mysqli = new mysqli($mysql_server, $mysql_user, $mysql_password, $mysql_db);\nif ($mysqli->connect_errno) {\n    printf("Connection failed: %s \\n", $mysqli->connect_error);\n    exit();\n}\n$mysqli->set_charset("utf8");\n?>'
		self.view.insert(edit, 0, command)
