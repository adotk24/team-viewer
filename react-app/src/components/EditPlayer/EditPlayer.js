import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import './EditPlayer.css'
import { getOnePlayer, edittingPlayer } from "../../store/player";

const EditPlayer = () => {
    const { playerId } = useParams()
    const history = useHistory()
    const player = useSelector(state => state.player.onePlayer)
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getOnePlayer(playerId))
    }, [dispatch, playerId])

    const [firstName, setFirstName] = useState(player?.firstName)
    const [lastName, setLastName] = useState(player?.lastName)
    const [height, setHeight] = useState(player?.height)
    const [position, setPosition] = useState(player?.position)
    const [number, setNumber] = useState(player?.number)
    const [year, setYear] = useState(player?.year)
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

    useEffect(() => {
        setFirstName(player?.firstName)
        setLastName(player?.lastName)
        setHeight(player?.height)
        setPosition(player?.position)
        setNumber(player?.number)
        setYear(player?.year)
    }, [player])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const values = { firstName, lastName, height, position, number, year }
        const edittedPlayer = await dispatch(edittingPlayer(player.teamId, player.id, values))
        if (edittedPlayer) history.push(`/teams/players/${edittedPlayer.id}`)
    }

    console.log('THIS IS MY PLAYERS STUFF', player.teamId, player)
    return (
        <div className="editPlayerContainer">
            <div className="editPlayerHeader">
                Edit Player Here!
            </div>
            <form className="edit-player-form" onSubmit={handleSubmit}>
                <label>
                    <input
                        type='text'
                        placeholder="First Name"
                        className="firstNameInput"
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='text'
                        placeholder="Last Name"
                        className="lastNameInput"
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='integer'
                        placeholder="Height"
                        className="heightInput"
                        value={height}
                        onChange={(e) => setHeight(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='text'
                        placeholder="Position"
                        className="positionInput"
                        value={position}
                        onChange={(e) => setPosition(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='integer'
                        placeholder="Number"
                        className="numberInput"
                        value={number}
                        onChange={(e) => setNumber(e.target.value)}
                        required />
                </label>
                <label>
                    <input
                        type='integer'
                        placeholder="Year"
                        className="playerYearInput"
                        value={year}
                        onChange={(e) => setYear(e.target.value)}
                        required />
                </label>
                <button type="submit"
                    className="editPlayerBtn"
                    disabled={errors.length > 0}>
                    EDIT PLAYER
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

export default EditPlayer
