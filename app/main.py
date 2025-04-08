def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return None
    if command[0] != "cp":
        return None
    try:
        with (open(command[1], "r") as file_in,
              open(command[-1], "x") as file_out):
            file_out.write(file_in.read())
    except FileExistsError:
        pass
    except FileNotFoundError:
        pass
