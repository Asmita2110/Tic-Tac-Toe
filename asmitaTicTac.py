game_list=[[2,2,2],
           [2,2,2],
           [2,2,2]]


def Display_game(game_list):
  for li in game_list:
    print(li)

  

# def choose_player(num):
#     # If player 1 is select
#     if num==1:
#       print('play 1 can play')
#       return 1

#     # If player 2 is select
#     elif num==2:
#       print('play 2 can play')
#       return 2

#     # Invalid player select then return -1.
#     else:
#       print('invalid choice,only 2 players allowed')
#       return -1

def position_choice(num,row_no,column_no):
#   player=choose_player(num)

  # Player 1's turn is there
  if num==1:
   if row_no in range(0,3) and column_no in range(0,3):
     if game_list[row_no][column_no]==0 or  game_list[row_no][column_no]==1:
       print('already chosen')
     else:
        game_list[row_no][column_no]=1
      

  # Player 0's turn is there
  else:
   if row_no in range(0,3) and column_no in range(0,3):
     if game_list[row_no][column_no]==0 or game_list[row_no][column_no]==1:
       print('already chosen')
     else:
       game_list[row_no][column_no]=0

  # Print game board
  Display_game(game_list=game_list)

def game_status(game_list, Flag):

    # Check for player 0 win
    # Row wise checking
    i=0
    while i<3:
      if game_list[i][0]==0 and game_list[i][1]==0 and game_list[i][2]==0:
        print(f"Player 0 is won ..!!")
        Flag = True
        return Flag


      else:
        i=i+1

    # Column wise checking
    j=0
    while j<3:
      if game_list[0][j]==0 and game_list[1][j]==0 and game_list[2][j]==0:
        print(f"Player 0 is won ..!!")
        Flag=True
        return Flag


      else:
        j=j+1

    # Left Diagonal Checking
    if game_list[0][0]==0 and game_list[1][1]==0 and game_list[2][2]==0:
      print(f"Player 0 is won ..!!")
      Flag=True
      return Flag

    # Right Diagonal Checking
    if game_list[0][2]==0 and game_list[1][1]==0 and game_list[2][0]==0:
      print(f"Player 0 is won ..!!")
      Flag=True
      return Flag
      


    # check for player 1 win
    # row wise checking
    i=0
    while i<3:
      if game_list[i][0]==1 and game_list[i][1]==1 and game_list[i][2]==1:
        print(f"Player 1 is won ..!!")
        Flag = True
        return Flag


      else:
        i=i+1

    # Column wise checking
    j=0
    while j<3:
      if game_list[0][j]==1 and game_list[1][j]==1 and game_list[2][j]==1:
        print(f"Player 1 is won ..!!")
        Flag=True
        return Flag


      else:
        j=j+1

    # Left Diagonal Checking
    if game_list[0][0]==1 and game_list[1][1]==1 and game_list[2][2]==1:
      print(f"Player 1 is won ..!!")
      Flag=True
      return Flag

    # Right Diagonal Checking
    if game_list[0][2]==1 and game_list[1][1]==1 and game_list[2][0]==1:
      print(f"Player 1 is won ..!!")
      Flag=True
      return Flag

    
    return Flag


if __name__ == "__main__":
    turn = 1
    
    while(True):
        if turn == 1:
            print("\nPlayer 1 turn\n")
            row_num = int(input("Enter row number : "))
            col_num = int(input("Enter col number : "))
            # Mark that position on game board if it not marked
            position_choice(1, row_no=row_num, column_no=col_num)
            print("----------------------------------------")

        else:
            print("\nPlayer 0 turn\n")
            row_num = int(input("Enter row number : "))
            col_num = int(input("Enter col number : "))
            # Mark that position on game board if it not marked
            position_choice(0, row_no=row_num, column_no=col_num)
            print("----------------------------------------")


        if(game_status(game_list=game_list, Flag=False)):
            print("Match Complete ")
            break
        turn = 1 - turn
