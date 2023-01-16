import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import './IndiGames.css'
import { deletingGame } from "../../store/game";
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getStatsBygame } from "../../store/stat";


export const IndiGames = ({ game, team, user }) => {

    const dispatch = useDispatch()
    const [isLoaded, setLoaded] = useState(false)
    const [scoreUpdated, setScoreUpdated] = useState(false)
    const stats = useSelector(state => Object.values(state.stat.allStats))
    const gameStats = useSelector(state => state.stat.allScores)

    const team1id = game?.team1.id
    const team2id = game?.team2.id

    const team1ScoreSetter = (team1Id) => {
        for (let key in gameStats[game.id]) {
            if (key == team1Id) return gameStats[game.id][key]
        }
        return null
    }

    const team2ScoreSetter = (team2Id) => {
        for (let key in gameStats[game.id]) {
            if (key == team2Id) return gameStats[game.id][key]
        }
        return null
    }
    useEffect(() => {
        dispatch(getStatsBygame(game.id)).then(() => setLoaded(true))
    }, [dispatch, game.id])


    const handleDeleteClick = async (e) => {
        e.preventDefault()
        await dispatch(deletingGame(game.id))
        window.location.reload()
    }

    const hasScore = () => {
        return team1ScoreSetter(team1id) && team2ScoreSetter(team2id)
    }
    return isLoaded && (
        < div className="scheduleOneGame" >
            <div>{game.datetime}</div>
            <div className="scheduleMatchup">
                {hasScore() &&
                    <NavLink to={`/game/${game.id}`}>
                        <div>{team1ScoreSetter(team1id)} {game.team1.mascot} VS {game.team2.mascot} {team2ScoreSetter(team2id)}</div>
                    </NavLink>
                }
                {
                    !hasScore() &&
                    <NavLink to={`/game/${game.id}`}>
                        <div>{game.team1.mascot} VS {game.team2.mascot}</div>
                    </NavLink>
                }
            </div>
            {
                team[0]?.userId == user?.id &&
                <div className="gameFunctions">
                    <NavLink to={`schedule/game/${game.id}/edit`}>
                        <button
                            className="schedule-btn">Edit Game</button>
                    </NavLink>
                    <button
                        className="schedule-btn"
                        onClick={handleDeleteClick}>
                        Delete Game
                    </button>
                </div>
            }
        </div >
    )
}
