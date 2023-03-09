def get_grade(s1, s2, s3):
    result = s1 + s2 + s3
    promedio=result // 3
    if 90 <= promedio <= 100:
        return "A"
    elif 80 <= promedio < 90:
        return "B"
    elif 70 <= promedio< 80	:
        return "C"
    elif 60 <= promedio < 70	:
        return "D"
    else :
        return "F"
