import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from "react-router-dom";
import './EditStat.css'
import { getOnePlayer } from '../../store/player';
import { getStatsByPlayer } from '../../store/stat';
import { edittingStat } from '../../store/stat';
const EditStat = () => {
    const { gameId, teamId, playerId } = useParams()
    const history = useHistory()
    const dispatch = useDispatch()
    const player = useSelector(state => state.player.onePlayer)
    const stats = useSelector(state => Object.values(state.stat.allPlayerStats))
    const playerStat = stats[0]
    useEffect(() => {
        dispatch(getOnePlayer(playerId)).then(() => {
            dispatch(getStatsByPlayer(playerId))
        })
    }, [dispatch])

    const [points, setPoints] = useState(playerStat?.points)
    const [rebounds, setRebounds] = useState(playerStat?.rebounds)
    const [assists, setAssists] = useState(playerStat?.assists)
    const [errors, setErrors] = useState([])

    useEffect(() => {
        setPoints(playerStat?.points)
        setRebounds(playerStat?.rebounds)
        setAssists(playerStat?.assists)
    }, [playerStat])


    const handleSubmit = async (e) => {
        e.preventDefault()
        const values = { points, rebounds, assists }
        if (!errors.length) {
            const edittedStat = await dispatch(edittingStat(gameId, teamId, playerId, playerStat.id, values))
            if (edittedStat) history.goBack()
        }

    }


    return (
        <div className='editstatcontainer'>
            <div className='editStatHeader'>
                Editing Stats for {player.firstName} {player.lastName}
            </div>

            <form className='stat-form' onSubmit={handleSubmit}>
                <div className='stat-form-input'>
                    <label>Points</label>
                    <input
                        type='number'
                        placeholder='Points'
                        className='stat-input-box'
                        min={0}
                        value={points}
                        onChange={(e) => setPoints(e.target.value)}
                        required />
                </div>
                <div className='stat-form-input'>
                    <label>Rebounds</label>
                    <input
                        type='number'
                        placeholder='Rebounds'
                        className='stat-input-box'
                        min={0}
                        value={rebounds}
                        onChange={(e) => setRebounds(e.target.value)}
                        required />
                </div>
                <div className='stat-form-input'>
                    <label>Assists</label>
                    <input
                        type='number'
                        placeholder='Assists'
                        className='stat-input-box'
                        min={0}
                        value={assists}
                        onChange={(e) => setAssists(e.target.value)}
                        required />
                </div>
                <button type='submit'
                    className='editStatBtn'
                    disabled={errors.length > 0}>
                    EDIT STAT
                </button>
            </form>
        </div>
    )
}


export default EditStat
