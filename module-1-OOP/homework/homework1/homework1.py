class FootbalClub:
    name = ''
    city = ''
    tournament_score = 0

class Championship:
    country = ''
    championship_name = ''
    participants = list()
    
    def add_club(self, club):
        self.participants.append(club)

    def get_worst_team(self):
        worst_club = self.participants[0]

        for current_club in self.participants:
            if current_club.tournament_score < worst_club.tournament_score:
                worst_club = current_club

        print(f'The worst club of championship is {worst_club.name}, score - {worst_club.tournament_score}.')


Liverpool = FootbalClub()
Liverpool.name = 'Liverpool'
Liverpool.city = 'Liverpool'
Liverpool.tournament_score = 100


Real = FootbalClub()
Real.name = 'RealMadrid'
Real.city = 'Madrid'
Real.tournament_score = 115


Dynamo = FootbalClub()
Dynamo.name = 'Dynamo Kyiv'
Dynamo.city = 'Kyiv'
Dynamo.tournament_score = 80


Premier_league = Championship()
Premier_league.country = 'England'
Premier_league.championship_name = 'England Premier League'
Premier_league.add_club(Liverpool)
Premier_league.add_club(Real)
Premier_league.add_club(Dynamo)


Premier_league.get_worst_team()