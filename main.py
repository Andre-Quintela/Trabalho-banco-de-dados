from controllers.criarDB import create_database, create_tables
create_database()
create_tables()
from views.menu import Menu
from views.splashscreen import splashscreen


splashscreen()  

Menu()


