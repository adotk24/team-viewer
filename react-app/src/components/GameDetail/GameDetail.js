import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getStatsBygame } from "../../store/stat";
import './GameDetail.css'
import { getOneGame } from '../../store/game';
import { IndiGames } from "../IndiGames/IndiGames";
import { getAllUserTeams } from '../../store/team';
import GameDetailRow from '../GameDetailRow/GameDetailRow';

const GameDetail = () => {
    const { gameId } = useParams()
    const dispatch = useDispatch()
    const [isLoaded, setLoaded] = useState(false)
    const stats = useSelector(state => Object.values(state.stat.allStats))
    const game = useSelector(state => state.game.oneGame)
    const user = useSelector(state => state.session.user)
    const gameScore = useSelector(state => state.stat.oneScore)
    const [gameFound, setGameFound] = useState(false)
    const [scoreFound, setScoreFound] = useState(false)
    // let team1;
    // let team2;
    const [team1, setTeam1] = useState(null)
    const [team2, setTeam2] = useState(null)
    const [team1score, setTeam1score] = useState('')
    const [team2score, setTeam2score] = useState('')
    if (gameFound) {
        setTeam1(game.Game[0].team1)
        setTeam2(game.Game[0].team2)
        setGameFound(false)
        setScoreFound(true)
    }

    if (scoreFound) {
        for (let key in gameScore) {
            if (key == team1.id) setTeam1score(gameScore[key])
            if (key == team2.id) setTeam2score(gameScore[key])
        }
        setScoreFound(false)
        setLoaded(true)
    }

    useEffect(() => {
        dispatch(getStatsBygame(gameId)).then(() => {
            dispatch(getOneGame(gameId)).then(() => {
                dispatch(getAllUserTeams(user.id)).then(() =>
                    setGameFound(true))
            })
        })
    }, [dispatch, gameId])



    return isLoaded && (
        <div className='gamedetailcontainer'>
            <div className='gamedetailtop'>
                <div>{team1score}{team1.mascot} VS {team2.mascot}{team2score}</div>
                {/* <div>Testing Still</div> */}
            </div>
        </div>

    )
}


export default GameDetail
