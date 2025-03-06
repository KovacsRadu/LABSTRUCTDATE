from seminarul_1.domain.car_entity import Masina
from seminarul_1.repository.list_entity import CarOperations
from seminarul_1.service.service_data import ServiceOperations
from seminarul_1.ui.user_interface import run

CarOperations = CarOperations()
ServiceOperations = ServiceOperations(CarOperations)
run(ServiceOperations)

