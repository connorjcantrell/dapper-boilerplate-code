def clear_state_program():
    return Int(1)

if __name__ == "__main__":
    try:
        with open("../public/clear_state_program.teal", "w") as f:
            compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
            f.write(compiled)
    except FileNotFoundError:
        print(FileNotFoundError)
