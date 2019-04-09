import records
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
DB_NAME = 'nbastats.db'

db = records.Database('sqlite:///{}'.format(DB_NAME))
players = db.query('select br_name from players')

all_stats = db.query(
    'select name, mp, fg, fga, fg_pct, fg3, fg3_pct, ft, fta, ft_pct, orb, drb, trb, ast, stl, blk,tov, pts from stats')
