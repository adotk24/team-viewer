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
    const sortedPlayers = findPlayers.sort((a, b) => {
        if (a.number < b.number) return -1
        else if (a.number > b.number) return 1
        else return 0
    })
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
            <div className="oneTeamBanner">
                Welcome to the Team Viewer for your {team?.name} {team?.mascot}
            </div>
            <div className="rosterHeader">
                YOUR {team?.name.toUpperCase()} {team?.mascot.toUpperCase()}
            </div>

            <div className="roster">
                <div>Number</div>
                <div>Name</div>
                <div>Height</div>
                <div>Position</div>
                <div>Year</div>
            </div>
            {sortedPlayers.map(player => (
                <div className="roster-player-grid">
                    <div>{player.number}</div>
                    <NavLink to={`/teams/players/${player.id}`}>
                        <div>{player.firstName} {player.lastName}</div></NavLink>
                    <div>{heightConvert(player.height)}</div>
                    <div>{player.position}</div>
                    <div>{player.year}</div>

                </div>
            ))}
            {user?.id == team?.userId &&
                <NavLink to={`/teams/${teamId}/addPlayer`}>
                    <button
                        className="roster-add-player-btn"
                    > Add Player
                    </button>
                </NavLink>
            }
        </div>
    )
}


export default Roster
