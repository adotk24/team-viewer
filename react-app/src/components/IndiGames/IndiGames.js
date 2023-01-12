import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import './IndiGames.css'
import { deletingGame } from "../../store/game";
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getStatsBygame } from "../../store/stat";


export const IndiGames = ({ game, team, user }) => {
    console.log('GAME', game)
    const dispatch = useDispatch()
    const [isLoaded, setLoaded] = useState(false)
    const [scoreUpdated, setScoreUpdated] = useState(false)
    const stats = useSelector(state => {
        return Object.values(state.stat.allStats)
    })
    let score1 = 0;
    let score2 = 0;
    if (isLoaded) {
        let team1id = game.team1.id
        let team2id = game.team2.id
        stats.forEach(stat => {
            console.log('stat', stat)
            stat.teamid == team1id ? score1 += stat.points : score2 += stat.points
        })
    }

    const getScores = (stats) => {
        let team1id = game.team1.id
        let team2id = game.team2.id
        stats.forEach(stat => {
            stat.teamid == team1id ? score1 += stat.points : score2 += stat.points
        })
    }

    useEffect(() => {
        console.log('DISPATACH', game.id)
        dispatch(getStatsBygame(game.id)).then(() => setLoaded(true))
    }, [dispatch, game.id])

    console.log('RIGHT BEFORE RETURN', stats)
    return isLoaded && (
        < div className="scheduleOneGame" >
            <div>{game.datetime}</div>
            <div className="scheduleMatchup">
                <div>{score1}{game.team1.mascot} VS {game.team2.mascot}{score2}</div>
            </div>
            {
                team[0].userId == user?.id &&
                <div className="gameFunctions">
                    <NavLink to={`schedule/game/${game.id}/edit`}>
                        <button
                            className="schedule-btn">Edit Game</button>
                    </NavLink>
                    <button
                        className="schedule-btn"
                        onClick={async (e) => {
                            e.preventDefault()
                            const deleted = await dispatch(deletingGame(game.id))
                            window.location.reload()
                        }}>
                        Delete Game
                    </button>
                </div>
            }
        </div>
    )
}
