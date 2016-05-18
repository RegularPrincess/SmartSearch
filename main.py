from MVC import controller
from MVC import stackoverflowCrawler
from MVC import consoleView

model = stackoverflowCrawler.StackoverflowCrawler()
view = consoleView.ConsoleView()

controller.mvc_run(model, view)
