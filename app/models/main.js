import fs from 'node:fs/promises'

async function fetchTeamPlayers(teamID) {
  const url = `https://nfl-api-data.p.rapidapi.com/nfl-player-listing/v1/data?id=${teamID}`;
  const options = {
    method: 'GET',
    headers: {
      'x-rapidapi-key': '844a373d8cmsh8d3365be61f9441p1e34d5jsn417d1d90f490',
      'x-rapidapi-host': 'nfl-api-data.p.rapidapi.com'
    }
  };

  try {
    const response = await fetch(url, options);
    const result = await response.text();
    return result;
  } catch (error) {
    console.error(error);
  }
}
const teamsMap = {}

const teamsFile = './teams.json';
const contents = await fs.readFile(teamsFile, { encoding: 'utf-8' });
const data = JSON.parse(contents);

await fs.mkdir('./teams');

for (const team of data.teams) {
  teamsMap[team.abbreviation] = parseInt(team.id); 
  const teamDir = `./teams/${team.name.toLowerCase()}`;
  await fs.mkdir(teamDir);
  const playerJSON = await fetchTeamPlayers(team.id);
  fs.writeFile(`${teamDir}/players.json`, playerJSON);
}

