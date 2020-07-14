from pycricbuzz.cricbuzz import Cricbuzz
import asyncio

async def main():
    c = Cricbuzz()
    matches = await c.matches()
    firstMatchId = matches[0]['id']
    print(await c.matchinfo(firstMatchId))
    print('\n\n\n')
    print(await c.livescore(firstMatchId))
    print('\n\n\n')
    print(await c.scorecard(firstMatchId))
    print('\n\n\n')
    print(await c.commentary(firstMatchId))

asyncio.run(main())
