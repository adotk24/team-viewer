import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getStatsBygame } from "../../store/stat";
import { getOneGame } from '../../store/game';
import { IndiGames } from "../IndiGames/IndiGames";
import { getAllUserTeams } from '../../store/team';
import './GameDetailRow.css'
import { getAllPlayers } from '../../store/player';

const GameDetailRow = ({ playerId, gameId, teamId }) => {
    const dispatch = useDispatch()
    const [isLoaded, setLoaded] = useState(false)
    const stats = useSelector(state => Object.values(state.stat.allStats))
    const players = useSelector(state => Object.values(state.player.allPlayers))
    const [statFound, setStatFound] = useState(false)
    const [playerStat, setPlayerStat] = useState(null)
    const [playerName, setPlayerName] = useState(null)
    const user = useSelector(state => state.session.user)
    useEffect(() => {
        dispatch(getStatsBygame(gameId)).then((dispatch(getAllPlayers(teamId))))
            .then((setStatFound(true)))
    }, [dispatch, gameId, teamId])
    if (statFound && players.length) {
        stats.forEach(stat => {
            if (stat.playerid == playerId) {
                setPlayerStat(stat)
            }
        })
        players.forEach(player => {
            if (player.id == playerId) {
                setPlayerName(player)
            }
        })
        setStatFound(false)
        setLoaded(true)
    }
    console.log('IN GAME DETAIL ROW', playerStat)
    return isLoaded && playerStat && (
        <div className='gameRows'>
            <NavLink to={`/teams/players/${playerStat.player.id}`}>
                #{playerStat?.player.number}{playerStat?.player.firstName} {playerStat?.player.lastName} {playerStat?.points} POINTS {playerStat?.assists} ASSISTS {playerStat?.rebounds} REBOUNDS
            </NavLink>
            {playerStat?.team?.userId == user?.id &&
                <div className='rowUserFunctions'>
                    <button>Edit Stat</button>
                    <button>Delete Stat</button>
                </div>
            }
        </div>
    )
}

export default GameDetailRow
