from dicelib import dice

dice_list = []

for _ in range(0, 5):
    new_dice = dice.Dice()
    new_dice.roll()
    dice_list.append(new_dice)

print(sum(dice_list))
