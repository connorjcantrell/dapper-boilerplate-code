from pyteal import *


def approval_program():
    on_creation = Seq(
        [
            App.globalPut( Bytes("Creator"), Txn.sender() ),
            Return( Int(1) ),
        ]
    )

    is_creator = Txn.sender() == App.globalGet( Bytes("Creator") )
    delete_application = Seq(
        [
            Assert(is_creator == Int(1) ),
            Return(Int(1)),
        ]
    )

    update_application = Seq(
        [
            Assert(is_creator == Int(1) ),
            Return(Int(1)),
        ]
    )

    on_closeout = Seq(
        Return(Int(1))
    )

    on_opt_in = Seq(
        Return(Int(1))
    )


    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.DeleteApplication,delete_application],
        [Txn.on_completion() == OnComplete.UpdateApplication, update_application],
        [Txn.on_completion() == OnComplete.CloseOut, on_closeout],
        [Txn.on_completion() == OnComplete.OptIn, on_opt_in],
    )

    return program 

if __name__ == "__main__":
    try:
        with open("../public/approval_program.teal", "w") as f:
            compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
            f.write(compiled)
    except FileNotFoundError:
        # TODO: Handle gracefully
        print(FileNotFoundError)
