import sqlite3
from typing import List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_token(contract_address: str) -> bool:
    """
    Add a token to the database.
    Returns True if successful, False otherwise.
    """
    try:
        with sqlite3.connect("agent.db") as con:
            cur = con.cursor()
            
            # Try to insert the token
            cur.execute("INSERT INTO erc20s(contract) VALUES (?)", (contract_address,))
            con.commit()
            
            # Verify the insertion
            if cur.rowcount > 0:
                logger.info(f"Successfully added token: {contract_address}")
                return True
            else:
                logger.warning(f"No rows were inserted for token: {contract_address}")
                return False
                
    except sqlite3.IntegrityError as e:
        logger.error(f"Token already exists or unique constraint failed: {str(e)}")
        return False
    except sqlite3.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")
        return False

def get_tokens() -> List[tuple]:
    """
    Retrieve all tokens from the database.
    Returns empty list if no tokens found or in case of error.
    """
    try:
        with sqlite3.connect("agent.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM erc20s")
            results = cur.fetchall()

            return [row[1] for row in results]
            
    except sqlite3.Error as e:
        logger.error(f"Failed to retrieve tokens: {str(e)}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error while retrieving tokens: {str(e)}")
        return []