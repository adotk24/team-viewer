import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom"
import { addingPlayer } from "../../store/player"
import './AddPlayer.css'


const AddPlayer = () => {
    const { teamId } = useParams()
    const history = useHistory()
    const dispatch = useDispatch()
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [height, setHeight] = useState('')
    const [position, setPosition] = useState('')
    const [number, setNumber] = useState('')
    const [year, setYear] = useState('')
    const [errors, setErrors] = useState([])

    useEffect(() => {
        const validationErrors = []
        if (!firstName || firstName.length <= 2 || firstName.length >= 30) validationErrors.push('Must have First Name between 3 and 30 characters')
        if (!lastName || lastName.length <= 2 || lastName.length >= 30) validationErrors.push('Must have Last Name between 3 and 30 characters')
        if (!height || height <= 48 || height >= 96) validationErrors.push('Must have height between 48 and 96 inches')
        if (!position || position.length >= 30) validationErrors.push('Must have Position Name less than 30 characters')
        if (!number || number < 0 || number > 99) validationErrors.push('Must have Number between 0 and 99')
        if (!year) validationErrors.push('Must have Year')
        setErrors(validationErrors)
    }, [firstName, lastName, height, position, number, year])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const formValues = { firstName, lastName, height, position, number, year }
        const newPlayer = await dispatch(addingPlayer(teamId, formValues))
        if (newPlayer) history.push(`/teams/players/${newPlayer.id}`)
    }
    return (
        <div className="addPlayerContainer">
            <div className="addPlayerHeader">
                Create a new Player!
            </div>
            <form className="player-form" onSubmit={handleSubmit}>
                <label>
                    <input
                        type='text'
                        placeholder='First Name'
                        className="addfirstNameInput"
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='text'
                        placeholder='Last Name'
                        className="addLastNameInput"
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='integer'
                        placeholder='Height'
                        className="addHeightInput"
                        value={height}
                        onChange={(e) => setHeight(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='text'
                        placeholder='Position'
                        className="addPositionInput"
                        value={position}
                        onChange={(e) => setPosition(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='integer'
                        placeholder='Number'
                        className="addNumberInput"
                        value={number}
                        onChange={(e) => setNumber(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='integer'
                        placeholder='Year'
                        className="addYearInput"
                        value={year}
                        onChange={(e) => setYear(e.target.value)}
                        required />
                </label>
                <button type="submit"
                    className="editPlayerBtn"
                    disabled={errors.length > 0}>
                    ADD PLAYER
                </button>
                <ul className="editPlayerErrors">
                    {errors.map(e => (
                        <li key={e}>{e}</li>
                    ))}
                </ul>
            </form>
        </div>
    )
}

export default AddPlayer
