import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom"
import './PlayerDetail.css'
import { getOnePlayer } from "../../store/player";

const PlayerDetail = () => {
    const { playerId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setLoaded] = useState(false)

    const player = useSelector(state => state.player.onePlayer)


    useEffect(() => {
        dispatch(getOnePlayer(playerId)).then(() => {
            setLoaded(true)
        })
    }, [dispatch, playerId])


    const heightConvert = num => {
        let feet = Math.floor(num / 12)
        let inches = num % feet
        return `${feet}' ${inches}`
    }

    return isLoaded && (

        <div className="playerDetailContainer">
            <button>Edit This Player</button>
            <button>Delete This Player</button>
            <h1>{player.firstName} {player.lastName}</h1>
            <div> {heightConvert(player.height)} {player.position} #{player.number} {player.year}</div>
        </div>
    )
}


export default PlayerDetail
