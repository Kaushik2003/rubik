import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup():
    """
    Initialize database with proper table schemas including primary keys
    and appropriate constraints.
    """
    try:
        with sqlite3.connect("agent.db") as con:
            cur = con.cursor()
            
            # Wallet table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS wallet(
                    id INTEGER PRIMARY KEY,
                    info TEXT
                )
            """)
            
            # NFTs table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS nfts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    contract TEXT UNIQUE NOT NULL
                )
            """)
            
            # ERC20s table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS erc20s(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    contract TEXT UNIQUE NOT NULL
                )
            """)
            
            con.commit()
            logger.info("Database tables created successfully")
    except sqlite3.Error as e:
        logger.error(f"Failed to setup database: {str(e)}")
        raise