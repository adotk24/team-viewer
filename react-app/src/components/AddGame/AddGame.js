import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useHistory } from "react-router-dom";
import './AddGame.css'
import { addingGame } from "../../store/game";
import { getAllTeams } from "../../store/team";

const AddGame = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [datetime, setDatetime] = useState('')
    const [team1, setTeam1] = useState('')
    const [team2, setTeam2] = useState('')
    const [team1id, setTeam1id] = useState('')
    const [team2id, setTeam2id] = useState('')
    const [errors, setErrors] = useState([])
    const [isLoaded, setLoaded] = useState(false)
    const findTeams = useSelector(state => Object.values(state.team.allTeams))
    useEffect(() => {
        dispatch(getAllTeams()).then(() => { setLoaded(true) })
    }, [dispatch])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const year = datetime.slice(0, 4)
        let month = datetime.slice(5, 7)
        if (month[0] == 0) month = datetime.slice(6, 7)
        let day = datetime.slice(8, 10)
        if (day[0] == 0) day = datetime.slice(9, 10)
        let hour = datetime.slice(11, 13)
        if (hour[0] == 0) hour = datetime.slice(12, 13)
        let minute = datetime.slice(14, 16)
        if (minute == '00') minute = "0"

        const values = { year, month, day, hour, minute, team1id, team2id }
        const addedGame = await dispatch(addingGame(values))
        if (addedGame) history.push(`/teams/${team1id}`)
    }


    // useEffect(() => {
    //     const validationErrors = []
    //     if (team1 == team2) validationErrors.push("Team can't face itself!")
    //     setErrors(validationErrors)
    // }, [team1, team2, team1id, team2id])

    return isLoaded && (
        < div className="game-form-container" >
            <ul className="game-formErrors">
                {errors.map(e => (
                    <li key={e}>{e}</li>
                ))}
            </ul>
            <form className="game-form" onSubmit={handleSubmit}>
                <label>Date + Time</label>
                <input
                    type='datetime-local'
                    value={datetime}
                    onChange={(e) => setDatetime(e.target.value)}
                    className='add-game-calendar'
                ></input>
                <label>Team 1</label>
                <select
                    className="game-team-input"
                    value={team1id}
                    onChange={(e) => setTeam1id(e.target.value)}>
                    {findTeams.map(e => (
                        <option
                            value={e.id}
                        >{e.name}</option>
                    ))}
                </select>
                <label>Team 2</label>
                <select
                    className="game-team-input-2"
                    value={team2id}
                    onChange={(e) => setTeam2id(e.target.value)}>
                    {findTeams.map(e => (
                        <option
                            value={e.id}
                        > {e.name}</option>
                    ))}
                </select>
                <button type='submit'
                    className="submit-add-game"
                    disabled={errors.length > 0}>
                    Add Game
                </button>
            </form>
        </div >
    )
}

export default AddGame