import sqlite3
import psycopg2
# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_DfwUMu52SRGO@ep-gentle-paper-ac3zlw69-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
   return psycopg2.connect(DB_PATH)