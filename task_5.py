class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses
        self.total_am_points = None


class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        print(f'Футбольных побед:{self.victories}')

    def number_of_draws(self):
        print(f'Футбольных ничьих:{self.draws}')

    def number_of_losses(self):
        print(f'Футбольных поражений:{self.losses}')

    def total_points(self):
        self.total_am_points = 3*self.victories + self.draws
        print(f'Общее количество очков:{self.total_am_points}')


class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        print(f'Хокейных побед:{self.victories}')

    def number_of_draws(self):
        print(f'Хокейных ничьих:{self.draws}')

    def number_of_losses(self):
        print(f'Хокейных поражений:{self.losses}')

    def total_points(self):
        self.total_am_points = 2 * self.victories + self.draws
        print(f'Общее количество очков:{self.total_am_points}')


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)
for team in (football_team, hockey_team):
    team.number_of_wins()
    team.number_of_draws()
    team.number_of_losses()
    team.total_points()
