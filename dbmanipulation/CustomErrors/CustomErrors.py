class AppError(Exception): pass

class GeneralError(AppError):

    # define the error codes & messages here
    em = {1100: "You tried to delete a non backup table.", \
          1102: "Another here. Please verify.", \
          1103: "One more here. Please verify.", \
          1104: "That was idiotic. Please verify."}