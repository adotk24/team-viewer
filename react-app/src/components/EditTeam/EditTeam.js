import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import './EditTeam.css'
import { getOneTeam } from "../../store/team";
import { edittingTeam } from "../../store/team";

const EditTeam = () => {
    const { teamId } = useParams()
    const history = useHistory()
    const findEditThisTeam = useSelector(state => {
        console.log('THIS IS MY STATE', state)
        return state.team.oneTeam
    })
    const editThisTeam = findEditThisTeam[0]
    const dispatch = useDispatch()


    useEffect(() => {
        dispatch(getOneTeam(teamId))
    }, [dispatch, teamId])

    const [name, setName] = useState(editThisTeam?.name)
    const [mascot, setMascot] = useState(editThisTeam?.mascot)
    const [city, setCity] = useState(editThisTeam?.city)
    const [state, setState] = useState(editThisTeam?.state)
    const [year, setYear] = useState(editThisTeam?.year)
    const [errors, setErrors] = useState([])

    useEffect(() => {
        const validationErrors = []
        if (!name || name.length <= 2 || name.length >= 50) validationErrors.push('Must have a name between 3 and 50 characters')
        if (!mascot || mascot.length <= 2 || mascot.length >= 50) validationErrors.push('Must have a mascot between 3 and 50 characters')
        if (!city || city.length <= 2 || city.length >= 50) validationErrors.push('Must have city between 3 and 50 characters')
        if (!state || state.length <= 2 || state.length >= 50) validationErrors.push('Must have state between 3 and 50 characters')
        if (!year) validationErrors.push('Must include a year')
        setErrors(validationErrors)
    }, [name, mascot, city, state, year])

    useEffect(() => {
        setName(editThisTeam?.name)
        setMascot(editThisTeam?.mascot)
        setCity(editThisTeam?.city)
        setState(editThisTeam?.state)
        setYear(editThisTeam?.year)
    }, [editThisTeam])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const formValues = { name, mascot, city, state, year }
        const edittedTeam = await dispatch(edittingTeam(formValues, editThisTeam.id))
        if (edittedTeam) history.push(`/teams/${edittedTeam.id}`)
    }

    return (
        <div className="addTeamContainer">
            <div className="addTeamHeader">
                Edit your team here!
            </div>
            <form className="team-form" onSubmit={handleSubmit}>
                <div className="team-form-input">
                    <label>Name</label>
                    <input
                        type='text'
                        placeholder='Name'
                        className="addTeamInput"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required />
                </div>

                <div className="team-form-input">
                    <label>Mascot</label>
                    <input
                        type='text'
                        placeholder='Mascot'
                        className="addTeamInput"
                        value={mascot}
                        onChange={(e) => setMascot(e.target.value)}
                        required />
                </div>

                <div className="team-form-input">
                    <label>City</label>
                    <input
                        type='text'
                        placeholder='city'
                        className="addTeamInput"
                        value={city}
                        onChange={(e) => setCity(e.target.value)}
                        required />
                </div>

                <div className="team-form-input">
                    <label>State</label>
                    <input
                        type='text'
                        placeholder='State'
                        className="addTeamInput"
                        value={state}
                        onChange={(e) => setState(e.target.value)}
                        required />
                </div>

                <div className="team-form-input">
                    <label>Year</label>
                    <input
                        type='integer'
                        placeholder='Year'
                        className="addTeamInput"
                        value={year}
                        onChange={(e) => setYear(e.target.value)}
                        required />
                </div>
                <button type='submit'
                    className="submit-add-team"
                    disabled={errors.length > 0}>
                    EDIT TEAM
                </button>
                <ul className="addTeamErrors">
                    {errors.map(e => (
                        <li key={e}>{e}</li>
                    ))}
                </ul>
            </form>
        </div>
    )
}

export default EditTeam
