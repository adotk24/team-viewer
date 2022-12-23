import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getAllPlayers } from '../../store/player'
import { getOneTeam } from "../../store/team";
import './Roster.css'


const Roster = () => {
    const { teamId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const findPlayers = useSelector(state => Object.values(state.player.allPlayers))
    const user = useSelector(state => state.session.user)
    const findTeam = useSelector(state => state.team.oneTeam)

    const team = findTeam[0]

    const [isLoaded, setLoaded] = useState(false)
    useEffect(() => {
        dispatch(getAllPlayers(teamId)).then(() => {
            setLoaded(true)
        })
    }, [dispatch, teamId])
    useEffect(() => {
        dispatch(getOneTeam(teamId)).then(() => {
            setLoaded(true)
        })
    }, [dispatch, teamId])
    const heightConvert = num => {
        let feet = Math.floor(num / 12)
        let inches = num - (feet * 12)
        return `${feet}' ${inches}`
    }

    return isLoaded && (
        <div className="rostercontainer">
            <div className="rosterHeader">
                Roster
            </div>
            {user?.id == team.userId &&
                <NavLink to={`/teams/${teamId}/addPlayer`}>
                    <button> Add Player
                    </button>
                </NavLink>
            }
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
