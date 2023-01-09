import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom"
import { addingPlayer } from "../../store/player"
import './AddPlayer.css'
import { getOneTeam } from "../../store/team";


const AddPlayer = () => {
    const { teamId } = useParams()
    const findTeam = useSelector(state => state.team.oneTeam)
    const team = findTeam[0]
    const history = useHistory()
    const dispatch = useDispatch()
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [height, setHeight] = useState('')
    const [position, setPosition] = useState('')
    const [number, setNumber] = useState('')
    const [year, setYear] = useState('Freshman')
    const [errors, setErrors] = useState([])
    // useEffect(() => {
    //     const validationErrors = []
    //     if (!firstName || firstName.length <= 2) validationErrors.push('First Name must have at least 3 characters')
    //     if (!lastName || lastName.length <= 2) validationErrors.push('Last Name must have at least 3 characters')
    //     if (!height || height < 48 || height > 96) validationErrors.push('Must have height between 48 and 96 inches')
    //     if (!position) validationErrors.push('Must have Position Name')
    //     if (number === null || number < 0 || number > 99) validationErrors.push('Must have Number between 0 and 99')
    //     if (!year) validationErrors.push('Must have Year')
    //     setErrors(validationErrors)
    // }, [firstName, lastName, height, position, number, year])

    useEffect(() => {
        dispatch(getOneTeam(teamId))
    }, [dispatch])


    const handleSubmit = async (e) => {
        e.preventDefault()
        const validationErrors = []
        if (!firstName || firstName.length <= 2) validationErrors.push('First Name must have at least 3 characters')
        if (!lastName || lastName.length <= 2) validationErrors.push('Last Name must have at least 3 characters')
        if (!height || height < 48 || height > 96) validationErrors.push('Must have height between 48 and 96 inches')
        if (!position) validationErrors.push('Must have Position Name')
        if (number === null || number < 0 || number > 99) validationErrors.push('Must have Number between 0 and 99')
        if (!year) validationErrors.push('Must have Year')
        setErrors(validationErrors)
        const formValues = { firstName, lastName, height, position, number, year }
        if (!errors.length) {
            const newPlayer = await dispatch(addingPlayer(teamId, formValues))
            if (newPlayer) history.push(`/teams/players/${newPlayer.id}`)
        }
    }
    return (
        <div className="addPlayerContainer">
            <div className="oneTeamBanner">
                Welcome to the Team Viewer for your {team?.name} {team?.mascot}
            </div>
            <div className="player-form-div">
                <div className="addPlayerHeader">
                    Create a new Player!
                </div>
                <ul className="editPlayerErrors">
                    {errors.map(e => (
                        <li key={e}>{e}</li>
                    ))}
                </ul>
                <form className="player-form" onSubmit={handleSubmit}>
                    <div className="player-form-input">
                        <label>First Name</label>
                        <input
                            type='text'
                            placeholder='First Name'
                            className="player-input-box"
                            value={firstName}
                            onChange={(e) => setFirstName(e.target.value)}
                            maxLength={30}
                            required />
                    </div>
                    <div className="player-form-input">
                        <label>Last Name</label>
                        <input
                            type='text'
                            placeholder='Last Name'
                            className="player-input-box"
                            value={lastName}
                            onChange={(e) => setLastName(e.target.value)}
                            maxLength={30}
                            required />
                    </div>

                    <div className="player-form-input">

                        <label>Height(in)</label>
                        <input
                            type='number'
                            placeholder='Height'
                            className="player-input-box"
                            value={height}
                            max={96}
                            min={48}
                            onChange={(e) => setHeight(e.target.value)}
                            required />
                    </div>

                    <div className="player-form-input">
                        <label>Position</label>
                        <input
                            type='text'
                            placeholder='Position'
                            className="player-input-box"
                            value={position}
                            maxLength={30}

                            onChange={(e) => setPosition(e.target.value)}
                            required />
                    </div>

                    <div className="player-form-input">
                        <label>
                            Number
                        </label>
                        <input
                            type='number'
                            placeholder='Number'
                            className="player-input-box"
                            value={number}
                            max={99}
                            min={0}
                            onChange={(e) => setNumber(e.target.value)}
                            required />
                    </div>

                    <div className="player-form-input">
                        <label>Year</label>
                        <select
                            type='integer'
                            placeholder='Year'
                            className="player-input-box"
                            value={year}
                            onChange={(e) => setYear(e.target.value)}
                            required >
                            <option>Freshman</option>
                            <option>Sophomore</option>
                            <option>Junior</option>
                            <option>Senior</option>
                        </select>
                    </div>

                    <button type="submit"
                        className="editPlayerBtn"
                        disabled={errors.length > 0}>
                        ADD PLAYER
                    </button>
                </form>
            </div>
        </div>
    )
}

export default AddPlayer
