from controllers.criarDB import create_database, create_tables
from views.menu import Menu
from views.splashscreen import splashscreen

create_database()
create_tables()

splashscreen()  

Menu()


