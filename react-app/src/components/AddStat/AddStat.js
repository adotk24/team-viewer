import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from "react-router-dom";
import './AddStat.css'
import { getAllPlayers } from '../../store/player';
import { getStatsBygame } from '../../store/stat';
const AddStat = () => {
    const { gameId, teamId } = useParams()
    const game = useSelector(state => state.game.oneGame)
    const dispatch = useDispatch()
    const history = useHistory()
    const [errors, setErrors] = useState([])
    const [isLoaded, setLoaded] = useState(false)
    const players = useSelector(state => Object.values(state.player.allPlayers))
    const curStats = useSelector(state => {
        return Object.values(state.stat.allStats)
    })
    useEffect(() => {
        dispatch(getAllPlayers(teamId)).then(() => {
            dispatch(getStatsBygame(gameId))
        }).
            then(() => setLoaded(true))
    }, [dispatch, teamId])




    console.log(players)
    return (
        <div className='addStatContainer'>
            <form className='stat-form' onSubmit={null}>
                <div className='stats-form-header'>Add a Stat</div>
                <div className='stat-formErrors'>
                    {errors.map(e => (
                        <li key={e}>{e}</li>
                    ))}
                </div>
                <div className='stat-form-input'>
                    <label>Player</label>
                </div>
                <div className='stat-form-input'>
                    <label>Points</label>
                    <input
                        type='number'
                        placeholder='points'
                        className='stat-input-box'
                        value={null}
                        min={0}
                        required />
                </div>
                <div className='stat-form-input'>
                    <label>Rebounds</label>
                    <input
                        type='number'
                        placeholder='rebounds'
                        className='stat-input-box'
                        value={null}
                        min={0}
                        required />
                </div>
                <div className='stat-form-input'>
                    <label>Assists</label>
                    <input
                        type='number'
                        placeholder='assists'
                        className='stat-input-box'
                        value={null}
                        min={0}
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
