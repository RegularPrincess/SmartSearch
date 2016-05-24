import sublime, sublime_plugin


class sublimeViewCommand(sublime_plugin.TextCommand):
	def get_query(self, edit):

		main_view = self.view
		raw_query = main_view.substr(main_view.sel()[0])
		query = queryProcessor.format_query(raw_query)
        return queryProcessor.compile_request(query) 


 	def choose_question(self, edit):
 		main_view = self.view
        number = int(main_view.substr(main_view.sel()[0])) - 1
        return number


    def print_questions(self, questions, edit):
        no = 1
        sublime.run_command("new_window", "dfgh")
		new_w =  sublime.active_window()
		new_view = new_w.new_file()
        for question in questions:
        	new_view.insert(edit, 0, no + question.title)
            no += 1
        return None


    def print_answer(self, answer, edit):
    	sublime.run_command("new_window", "dfgh")
		new_w =  sublime.active_window()
		new_view = new_w.new_file()
		new_view.insert(edit, 0, answer.body)
