import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from "react-router-dom";
import { deletingStat, getStatsBygame } from "../../store/stat";
import { getOneGame } from '../../store/game';
import { IndiGames } from "../IndiGames/IndiGames";
import { getAllUserTeams } from '../../store/team';
import './GameDetailRow.css'
import { getAllPlayers } from '../../store/player';

const GameDetailRow = ({ playerId, gameId, teamId }) => {
    const history = useHistory()
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
    if (playerStat) {
        console.log(playerStat.player)
    }
    return isLoaded && playerStat && (
        <div className='gameRows'>
            <NavLink to={`/teams/players/${playerStat.player.id}`}>
                {/* #{playerStat?.player.number}{playerStat?.player.firstName} {playerStat?.player.lastName} {playerStat?.points} POINTS {playerStat?.assists} ASSISTS {playerStat?.rebounds} REBOUNDS */}
                <div className='teamdetailrowgrid'>
                    <div>{playerStat?.player.number}</div>
                    <div>{playerStat?.player.lastName}, {playerStat?.player.firstName}</div>
                    <div>{playerStat?.points}</div>
                    <div>{playerStat?.rebounds}</div>
                    <div>{playerStat?.assists}</div>
                </div>
            </NavLink>
            {playerStat?.team?.userId == user?.id &&
                <div className='rowUserFunctions'>
                    <NavLink to={`/game/${gameId}/${teamId}/${playerStat.player.id}/editStat`}>
                        <button className='statfunctions'>Edit Stat</button>
                    </NavLink>
                    <button
                        className='statfunctions'
                        onClick={async (e) => {
                            e.preventDefault()
                            const deleted = await dispatch(deletingStat(playerStat.id))
                            if (deleted) window.location.reload()

                        }}
                    >Delete Stat</button>
                </div>
            }
        </div>
    )
}

export default GameDetailRow
