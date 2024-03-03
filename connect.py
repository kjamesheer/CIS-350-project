from PyQt5 import QtSql, QtGui


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('drink_recipe_table4.db')

    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                   QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtGui.QMessageBox.Cancel)

        return False

    query = QtSql.QSqlQuery()

    query.exec_("create table mixer_table(id int primary key, "
                "name varchar(40), type varchar(40))")

    query.exec_("insert into mixer_table values(101, 'sprite', 'pop')")
    query.exec_("insert into mixer_table values(102, 'coca-cola', 'pop')")
    query.exec_("insert into mixer_table values(103, 'orange juice', 'juice')")


    query.exec_("create table liquor_table(id int primary key, "
                "name varchar(40), type varchar(40))")

    query.exec_("insert into liquor_table values(201, 'smirnoff', 'vodka')")
    query.exec_("insert into liquor_table values(202, 'jack daniels', 'whiskey')")
    query.exec_("insert into liquor_table values(203, 'tanqueray', 'gin')")

    return True


if __name__ == '__main__':
    import sys

    app = QtGui.QGuiApplication(sys.argv)
    createDB()