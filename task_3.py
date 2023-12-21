class PointsForPlace:

    @staticmethod
    def get_points_for_place(place):
        if not isinstance(place, int):
            print(f'Место - целое число')
        else:
            if place > 100:
                print(f'Баллы начисляются только первым 100 участникам')
            elif place < 1:
                print(f'Спортсмен не может занять нулевое или отрицательное место')
            else:
                points = 101 - place
                return points


class PointsForMeters:

    @staticmethod
    def get_points_for_meters(meters):
        if not isinstance(meters, int):
            print(f'Метры - должны быть целым числом')
        else:
            if meters < 0:
                print(f'Количество метров не может быть отрицательным')
            else:
                points = meters * 0.5
                return points


class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        points_of_place = self.get_points_for_place(place)
        points_of_meters = self.get_points_for_meters(meters)
        total = points_of_meters + points_of_place
        return total


points = 0

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
