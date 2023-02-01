def return_gallows(trys, message):
    stage1 = f"""          _________
          |       |
                  |
                  |
                  |         {message}
                  |
                  |
                  |
          -----------------"""

    stage2 = f"""          _________
          |       |
         (_)      |
                  |
                  |         {message}
                  |
                  |
                  |
          -----------------"""

    stage3 = f"""          _________
          |       |
         (_)      |
          |       |
          |       |         {message}
                  |
                  |
                  |
          -----------------"""

    stage4 = f"""          _________
          |       |
         (_)      |
          |---    |
          |       |         {message}
                  |
                  |
                  |
          -----------------"""

    stage5 = f"""          _________
          |       |
         (_)      |
       ---|---    |
          |       |         {message}
                  |
                  |
                  |
          -----------------"""

    stage6 = f"""          _________
          |       |
         (_)      |
       ---|---    |
          |       |         {message}
           \      |
            \     |
                  |
          -----------------"""

    stage7 = f"""          _________
          |       |
         (_)      |
       ---|---    |
          |       |         {message}
         / \      |
        /   \     |
                  |
          -----------------"""

    stages = [stage1, stage2, stage3, stage4, stage5, stage6, stage7]
    return stages[trys]
