import sqlite3
from typing import List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_nft(contract_address: str) -> bool:
    """
    Add an NFT contract to the database.
    Returns True if successful, False otherwise.
    """
    try:
        with sqlite3.connect("agent.db") as con:
            cur = con.cursor()
            
            # Try to insert the NFT
            cur.execute("INSERT INTO nfts(contract) VALUES (?)", (contract_address,))
            con.commit()
            
            # Verify the insertion
            if cur.rowcount > 0:
                logger.info(f"Successfully added NFT: {contract_address}")
                return True
            else:
                logger.warning(f"No rows were inserted for NFT: {contract_address}")
                return False
                
    except sqlite3.IntegrityError as e:
        logger.error(f"NFT already exists or unique constraint failed: {str(e)}")
        return False
    except sqlite3.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")
        return False

def get_nfts() -> List[tuple]:
    """
    Retrieve all NFTs from the database.
    Returns empty list if no NFTs found or in case of error.
    """
    try:
        with sqlite3.connect("agent.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM nfts")
            results = cur.fetchall()

            return [row[1] for row in results]
            
    except sqlite3.Error as e:
        logger.error(f"Failed to retrieve NFTs: {str(e)}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error while retrieving NFTs: {str(e)}")
        return []