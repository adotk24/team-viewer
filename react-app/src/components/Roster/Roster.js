import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getAllPlayers } from '../../store/player'
import './Roster.css'


const Roster = () => {
    const { teamId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const findPlayers = useSelector(state => Object.values(state.player.allPlayers))
    const [isLoaded, setLoaded] = useState(false)
    useEffect(() => {
        dispatch(getAllPlayers(teamId)).then(() => {
            setLoaded(true)
        })
    }, [dispatch, teamId])

    const heightConvert = num => {
        let feet = Math.floor(num / 12)
        let inches = num % feet
        return `${feet}' ${inches}`
    }

    return isLoaded && (
        <div className="rostercontainer">
            <div className="rosterHeader">
                Roster
            </div>
            <button> Add Player</button>
            {findPlayers.map(player => (
                <NavLink to={`/teams/players/${player.id}`}>
                    <div> {player.firstName} {player.lastName} {heightConvert(player.height)}
                        #{player.number} {player.position} {player.year}
                    </div>
                </NavLink>
            ))}
        </div>

    )
}


export default Roster
