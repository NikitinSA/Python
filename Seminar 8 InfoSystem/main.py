import view
import logger as lg
import adding as add


lg.logging.info('Start')
add.init_data_base('employees_base.csv')
view.ls_menu()