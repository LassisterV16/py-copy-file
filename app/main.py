def copy_file(command: str) -> None:
    if command[:2] == "cp":
        command = command.split()
        try:
            with (open(command[1], "r") as file_in,
                  open(command[-1], "x") as file_out):
                file_out.write(file_in.read())
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass
