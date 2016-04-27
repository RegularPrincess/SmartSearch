from MVC import Controller
from MVC import Model
from MVC import View
from business import MasterMiner
from business import WebMiner

business_model = WebMiner.WebMiner()
model = Model.Model(business_model)

view_impl = MasterMiner.MasterMiner()
view = View.View(view_impl)

Controller.mvc_run(model, view)