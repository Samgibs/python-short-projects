import cmd

class MyCmdInterpreter(cmd.Cmd):
    prompt = '>> '  # Set the command prompt

    def do_greet(self, arg):
        """Greet the user. Usage: greet [name]"""
        if arg:
            print(f"Hello, {arg}!")
        else:
            print("Hello!")

    def do_exit(self, arg):
        """Exit the command interpreter."""
        print("Exiting...")
        return True  # This will exit the interpreter

if __name__ == '__main__':
    my_cmd = MyCmdInterpreter()
    my_cmd.cmdloop()