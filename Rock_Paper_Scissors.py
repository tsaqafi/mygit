# Make a two-player Rock-paper-scissor

def Rock_Paper_Scissor(Player1, Player2):
    if Player1 == "Rock":
        if Player2 == "Rock":
            return input(print("Its Draw, want to play again? type 'Play' or type 'Quit' "))
        elif Player2 == "Paper":
            return input(print("Player 1 win. Again? type 'Play' or type 'Quit'"))
        elif Player2 == "Scissor":
            return input(print("Player 2 Lose, Again?t ype 'Play' or type 'Quit'"))
    if Player1 == "Paper":
        if Player2 == "Paper":
            return input(print("Its Draw, want to play again? type 'Play' or type 'Quit' "))
        elif Player2 == "Rock":
            return input(print("Player 1 win. Again? type 'Play' or type 'Quit'"))
        elif Player2 == "Scissor":
            return input(print("Player 2 lose, Again?t ype 'Play' or type 'Quit'"))
    if Player1 == "Scissor":
        if Player2 == "Scissor":
            return input(print("Its Draw, want to play again? type 'Play' or type 'Quit' "))
        elif Player2 == "Rock":
            return input(print("Player 1 win. Again? type 'Play' or type 'Quit'"))
        elif Player2 == "Paper":
            return input(print("Player 2 lose, Again?type 'Play' or type 'Quit'"))

Ans_str = input(print("Do you want to play rock paper scissor?, type 'Play' or 'Quit'"))
while Ans_str == "Play":
    Player1 = input(print("Player 1 please type 'Rock','Paper','Scissor'"))
    Player2 = input(print("Player 2 please type 'Rock','Paper','Scissor'"))
    Ans_str = Rock_Paper_Scissor(Player1,Player2)
else :
    print("Bye Bye")
