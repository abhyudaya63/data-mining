def minkowski(rating1, rating2, r):
    "Computes the Minkowski distance."
    distance = 0
    Ratings = False
    for key in rating1:
        if key in rating2:
            distance +=
            pow(abs(rating1[key] - rating2[key]), r)
            commonRatings = True
            if commonRatings:
                return pow(distance, 1/r)
            else:
                return 0
