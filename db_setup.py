from sqlalchemy import create_engine, Table, Column, MetaData, Integer, String, Float, exc

DATABASE = 'nbastatstest'
TABLE_NAMES = ['teams', 'players', 'yearly_stats', 'game_log']

TEAMS = {'Atlanta Hawks': 'ATL', 'Boston Celtics': 'BOS', 'Brooklyn Nets': 'BRK', 'Charlotte Hornets': 'CHO',
         'Chicago Bulls': 'CHI', 'Cleveland Cavaliers': 'CLE', 'Dallas Mavericks': 'DAL', 'Denver Nuggets': 'DEN',
         'Detroit Pistons': 'DET', 'Golden State Warriors': 'GSW', 'Houston Rockets': 'HOU', 'Indiana Pacers': 'IND',
         'Los Angeles Clippers': 'LAC', 'Los Angeles Lakers': 'LAL', 'Memphis Grizzlies': 'MEM', 'Miami Heat': 'MIA',
         'Milwaukee Bucks': 'MIL', 'Minnesota Timberwolves': 'MIN', 'New Orleans Pelicans': 'NOP',
         'New York Knicks': 'NYK', 'Oklahoma City Thunder': 'OKC', 'Orlando Magic': 'ORL',
         'Philadelphia 76ers': 'PHI', 'Phoenix Suns': 'PHO', 'Portland Trail Blazers': 'POR',
         'Sacramento Kings': 'SAC', 'San Antonio Spurs': 'SAS', 'Toronto Raptors': 'TOR', 'Utah Jazz': 'UTA',
         'Washington Wizards': 'WAS'}

STATS = ['mp', 'fg', 'fga', 'fg_pct', 'fg3', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk',
         'tov', 'pts']


def nbastats_db_setup(db_engine):
    metadata = MetaData()

    Table('teams', metadata, Column('team_name', String, primary_key=True), Column('abbr', String),)

    Table('players', metadata, Column('br_name', String, primary_key=True), Column('name', String),
          Column('href', String), Column('position', String), Column('age', Integer), Column('team', String),)

    Table('yearly_stats', metadata,
          Column('year', String,), Column('br_name', String),
          *(Column(column_name, Float) for column_name in STATS))

    metadata.create_all(db_engine)


def populate_teams_table(db_engine):
    m = MetaData()
    teams = Table('teams', m, Column('team_name', String), Column('abbr', String),)
    x = [{'team_name': k, 'abbr': v} for k, v in TEAMS.items()]
    ins = teams.insert()
    try:
        db_engine.execute(ins, *x)
    except exc.IntegrityError:
        print('Teams table should be static and has already been populated')


if __name__ == '__main__':
    db = create_engine('sqlite:///{}'.format(DATABASE + '.db'))
    nbastats_db_setup(db)
    populate_teams_table(db)
