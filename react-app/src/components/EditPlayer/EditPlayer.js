import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import './EditPlayer.css'
import { getOnePlayer, edittingPlayer } from "../../store/player";
import { getOneTeam } from "../../store/team";

const EditPlayer = () => {
    const { playerId } = useParams()
    const history = useHistory()
    const player = useSelector(state => state.player.onePlayer)
    const dispatch = useDispatch()
    const findTeam = useSelector(state => state.team.oneTeam)
    const team = findTeam[0]


    useEffect(() => {
        dispatch(getOneTeam(player.teamId))
    }, [dispatch])

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
        if (!firstName || firstName.length <= 2) validationErrors.push('First Name must have at least 3 characters')
        if (!lastName || lastName.length <= 2 || lastName.length >= 30) validationErrors.push('Last Name must have at least 3 characters')
        if (!height || height < 48 || height > 96) validationErrors.push('Must have height between 48 and 96 inches')
        if (!position) validationErrors.push('Must have Position')
        if (number === null || number < 0 || number > 99) validationErrors.push('Must have Number between 0 and 99')
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
        if (!errors.length) {
            const edittedPlayer = await dispatch(edittingPlayer(player.teamId, player.id, values))
            if (edittedPlayer) history.push(`/teams/players/${edittedPlayer.id}`)
        }
    }

    return (
        <div className="addPlayerContainer">
            <div className="oneTeamBanner">
                Welcome to the Team Viewer for your {team?.name} {team?.mascot}
            </div>
            <div className="player-form-div">
                <div className="addPlayerHeader">
                    Edit Player Here!
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
                            placeholder="First Name"
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
                            placeholder="Last Name"
                            className="player-input-box"
                            maxLength={30}
                            value={lastName}
                            onChange={(e) => setLastName(e.target.value)}
                            required />
                    </div>
                    <div className="player-form-input">
                        <label>Height(in)</label>
                        <input
                            type='number'
                            placeholder="Height"
                            className="player-input-box"
                            max={96}
                            min={48}
                            value={height}
                            onChange={(e) => setHeight(e.target.value)}
                            required />
                    </div>
                    <div className="player-form-input">
                        <label>Position</label>
                        <input
                            type='text'
                            placeholder="Position"
                            className="player-input-box"
                            maxLength={30}
                            value={position}
                            onChange={(e) => setPosition(e.target.value)}
                            required />
                    </div>
                    <div className="player-form-input">
                        <label>Number</label>
                        <input
                            type='number'
                            placeholder="Number"
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
                            placeholder="Year"
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
                        EDIT PLAYER
                    </button>
                </form>
            </div >
        </div >
    )
}

export default EditPlayer
