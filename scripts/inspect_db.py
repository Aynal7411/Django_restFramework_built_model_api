import sqlite3
import pathlib
p = pathlib.Path('db.sqlite3')
print('db exists:', p.exists())
if not p.exists():
    raise SystemExit('db missing')
conn = sqlite3.connect(p)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
print('tables:', cur.fetchall())
cur.execute("PRAGMA table_info('snippets_snippet')")
rows = cur.fetchall()
print('snippet schema rows count:', len(rows))
for r in rows:
    print(r)
cur.execute("PRAGMA table_info('django_migrations')")
print('\ndjango_migrations schema:')
for r in cur.fetchall():
    print(r)
cur.execute("SELECT * FROM django_migrations ORDER BY id LIMIT 50")
print('\ndjango_migrations rows:')
cols = [d[0] for d in cur.description]
print('columns ->', cols)
for r in cur.fetchall():
    print(r)
conn.close()
