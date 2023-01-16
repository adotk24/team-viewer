import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from "react-router-dom";
import './AddStat.css'
import { getAllPlayers } from '../../store/player';
import { addingStat, getStatsBygame } from '../../store/stat';
const AddStat = () => {
    const { gameId, teamId } = useParams()
    const game = useSelector(state => state.game.oneGame)
    const dispatch = useDispatch()
    const history = useHistory()
    const [errors, setErrors] = useState([])
    const [isLoaded, setLoaded] = useState(false)
    const [player, setPlayer] = useState('')
    const [points, setPoints] = useState(0)
    const [assists, setAssists] = useState(0)
    const [rebounds, setRebounds] = useState(0)
    const players = useSelector(state => Object.values(state.player.allPlayers))
    const curStats = useSelector(state => Object.values(state.stat.allStats))
    useEffect(() => {
        dispatch(getAllPlayers(teamId)).then(() => {
            dispatch(getStatsBygame(gameId))
        }).
            then(() => setLoaded(true))
    }, [dispatch, teamId])
    let availablePlayers = []
    let used = []
    if (curStats) {
        curStats.forEach(stat => {
            used.push(stat.playerid)
        })
    }

    if (curStats && players) {
        players.forEach(player => {
            if (!used.includes(player.id)) availablePlayers.push(player)
        })
        // setPlayer(availablePlayers[0])
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const validationErrors = []
        if (!player) validationErrors.push('Must choose a Player!')
        if (points === null) validationErrors.push('Must add Points!')
        if (assists === null) validationErrors.push('Must add Assists!')
        if (rebounds === null) validationErrors.push('Must add Rebounds!')
        setErrors(validationErrors)
        const formValues = { player, points, assists, rebounds }
        if (!errors.length) {
            console.log('HANDLE SUBMIT', formValues)
            const newStat = await dispatch(addingStat(gameId, teamId, formValues))
            if (newStat) history.goBack()
        }
    }



    console.log('INSIDE ADD STAT COMP', player)

    return (
        <div className='addStatContainer'>
            <form className='stat-form' onSubmit={handleSubmit}>
                <div className='stats-form-header'>Add a Stat</div>
                <div className='stat-formErrors'>
                    {errors.map(e => (
                        <li key={e}>{e}</li>
                    ))}
                </div>
                <div className='stat-form-input'>
                    <label>Player</label>
                    <select
                        className='stat-form-input'
                        value={player}
                        onChange={(e) => setPlayer(e.target.value)}
                    >
                        {availablePlayers.map(e => (
                            <option value={e.id}>{e.firstName} {e.lastName}</option>
                        ))}
                    </select>
                </div>
                <div className='stat-form-input'>
                    <label>Points</label>
                    <input
                        type='number'
                        placeholder='points'
                        className='stat-input-box'
                        value={points}
                        min={0}
                        onChange={(e) => setPoints(e.target.value)}
                        required />
                </div>
                <div className='stat-form-input'>
                    <label>Rebounds</label>
                    <input
                        type='number'
                        placeholder='rebounds'
                        className='stat-input-box'
                        value={rebounds}
                        min={0}
                        onChange={(e) => setRebounds(e.target.value)}
                        required />
                </div>
                <div className='stat-form-input'>
                    <label>Assists</label>
                    <input
                        type='number'
                        placeholder='assists'
                        className='stat-input-box'
                        value={assists}
                        min={0}
                        onChange={(e) => setAssists(e.target.value)}
                        required />
                </div>
                <button type='submit'
                    className='stat-form-button'
                    disabled={errors.length > 0}>
                    ADD STAT
                </button>
            </form>
        </div>
    )
}

export default AddStat
