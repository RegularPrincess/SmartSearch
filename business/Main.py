from MVC import Controller
from business import StackoverflowCrawler
from business import StumpView

model = StackoverflowCrawler.StackoverflowCrawler()
view = StumpView.StumpView()

Controller.mvc_run(model,view)