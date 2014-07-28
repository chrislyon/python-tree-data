import cmd

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

    ## Fonction Liste
    def do_list(self, line):
        self.not_yet(line)

    def help_list(self):
        print "list / ls : liste le contenu du dossier"

    ## Exemple
    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    TreeData().cmdloop()
