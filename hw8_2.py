# .2 ערוך מדגם ממוצע גבהים של שחקני ה- NBA
# צור רשימה ריקה
# רוץ בלולאה וקלוט גבהי שחקנים ) float )בלולאה. אם הגובה שנקלט נמוך מ- 1.60 או
# גבוה מ - 3.0 התעלם, רמז: continue. כל גובה תקין הוסף לרשימה באמצעות append
# כאשר המשתמש יכניס גובה מינוס 999 צא מהלולאה
# בתום הלולאה הדפס-
# .1 כמה שחקנים נקלטו במדגם?
# .2 מהו הגובה של השחקן הכי גבוה?
# .3 מהו הגובה של השחקן הכי נמוך?
# .4 מהו ממוצע הגבהים של כל השחקנים?
# .5 כמה שחקנים יותר גבוהים מ - 2.0 מטר?
# .6 כמה שחקנים יותר גבוהים מהממוצע? )רמז: רוץ בלולאה על כל רשימת השחקנים ובדו ק
# עבור כל גובה אם הוא גדול מהממוצע שחישבת קודם. אם כן הגדל את מונה הגבהים ב - 1(
import statistics

players_height: list[float] = []
counter_more_2: int = 0
SENTINEL = -999

while True:
    height: float = float(input("enter your height: "))
    if height == SENTINEL:
        break
    if not 1.6 <= height <= 3:
        continue

    players_height.append(height)
    if height > 2.0:
        counter_more_2 += 1

if players_height:
    print(players_height)
    print(len(players_height), "players were accepted")
    print(max(players_height), "maximum height")
    print(min(players_height), "minimum height")
    print(counter_more_2, 'players are taller then 2 m')
    average_height: float = statistics.mean(players_height)
    print(average_height)
    counter_height_above_avg: int = 0
    for i in range(len(players_height)):
        if players_height[i] > average_height:
            counter_height_above_avg += 1
    print(counter_height_above_avg, "players above average")
