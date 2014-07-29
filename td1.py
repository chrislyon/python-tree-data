import cmd
import h5py

DEFAULT_FILE = None

class TreeData(cmd.Cmd):

    """Simple command processor."""

    ## Fonction vide
    def not_yet(self, line):
        print "Not yet implemented : %s " % line

    def help_not_done(self):
        print "No help ... sorry "

    ### TODO
    # create / new
    # delete OBJET (recurse)
    # search (recurse)
    # set OBJET attribut = ""
    # show OBJET [attribut]

    ## Fonction
    def do_ex(self, line):
        self.not_yet(line)

    def help_ex(self):
        self.help_not_done()

    ## Fonction
    def do_create(self, line):
        global DEFAULT_FILE
        try:
            modele, name = line.split()
        except:
            self.help_create()
        modele = modele.upper()
        if modele == "FILE":
            print "CREATE FILE %s " % name
            fname = "%s.hdf5" % name
            f = h5py.File(fname, "w")
            if DEFAULT_FILE is None:
                DEFAULT_FILE = f
            print "File %s CREATED" % fname
        elif modele == "GROUP":
            print "CREATE GROUP %s " % name
            if DEFAULT_FILE:
                DEFAULT_FILE.create_group(name)
                print "GROUP %s CREATED" % name
            else:
                print "NO FILE"
        elif modele == "DATA":
            print "CREATE DATA %s" % name
        else:
            print "Modele inconnu ..."

    def help_create(self):
        print "Create MODELE NAME"

    ## Fonction Liste
    def print_name(self, name):
        print "- %s " % name

    def do_list(self, line):
        if not DEFAULT_FILE:
            print "NO File"
        else:
            DEFAULT_FILE.visit(self.print_name)

    def help_list(self):
        print "list / ls : liste le contenu du dossier"

    ## Exemple
    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        if DEFAULT_FILE is not None:
            DEFAULT_FILE.close()
        return True

if __name__ == '__main__':
    TreeData().cmdloop()
