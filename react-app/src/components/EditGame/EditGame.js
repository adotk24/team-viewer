import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import './EditGame.css'
import { edittingGame, getOneGame } from "../../store/game";
import { getAllTeams } from "../../store/team";
const EditGame = () => {
    const { gameId } = useParams()
    const history = useHistory()
    const dispatch = useDispatch()
    const findGame = useSelector(state => state.game.oneGame)
    const [datetime, setDatetime] = useState(null)
    const [isLoaded, setLoaded] = useState(false)
    const findTeams = useSelector(state => Object.values(state.team.allTeams))
    const [team1, setTeam1] = useState(null)
    const [team2, setTeam2] = useState(null)
    const [errors, setErrors] = useState([])
    const [team1id, setTeam1id] = useState(null)
    const [team2id, setTeam2id] = useState(null)
    useEffect(() => {
        dispatch(getOneGame(gameId)).then(() => {
            dispatch(getAllTeams()).then(() => { setLoaded(true) })
        })
    }, [dispatch, gameId])

    useEffect(() => {
        if (findGame && findGame.Game) {
            const game = findGame.Game[0]
            const gameSplit = game.datetime.split(' ')
            const day = gameSplit[1]
            const month = getMonth(gameSplit[2])
            const year = gameSplit[3]
            const time = gameSplit[4]
            const datetime = (`${year}-${month}-${day}T${time}`)
            setDatetime(datetime)
            setTeam1(game.team1.name)
            setTeam2(game.team2.name)
            setTeam1id(game.team1.id)
            setTeam2id(game.team2.id)

        }
    }, [findGame])


    const getMonth = (str) => {
        if (str == 'Jan') return '01'
        if (str == 'Feb') return '02'
        if (str == 'Mar') return '03'
        if (str == 'Apr') return '04'
        if (str == 'May') return '05'
        if (str == 'Jun') return '06'
        if (str == 'Jul') return '07'
        if (str == 'Aug') return '08'
        if (str == 'Sep') return '09'
        if (str == 'Oct') return '10'
        if (str == 'Nov') return '11'
        if (str == 'Dec') return '12'
    }


    useEffect(() => {
        const validationErrors = []
        if (team1 == team2) validationErrors.push("Team can't face itself!")
        setErrors(validationErrors)
    }, [team1, team2, team2id, team1id])

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
        let gameId = findGame.Game[0].id || null
        // if (findGame.Game) gameId = findGame.Game[0].id
        if (findGame) {
            gameId = findGame.Game[0].id
        }
        const values = { year, month, day, hour, minute, team1id, team2id }
        const edittedGame = await dispatch(edittingGame(gameId, values))
        if (edittedGame) history.push(`/teams/${team1id}`)
    }

    return datetime && isLoaded && team1id && (
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
                    placeholder={team1}
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
                    placeholder={team2}
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
                    Edit Game
                </button>
            </form>
        </div >
    )
}
export default EditGame
// import { useEffect, useState } from "react";
// import { useDispatch, useSelector } from "react-redux"
// import { NavLink, useParams, useHistory } from "react-router-dom";
// import './EditGame.css'
// import { edittingGame, getOneGame } from "../../store/game";

// const EditGame = () => {
//     const { gameId } = useParams()
//     const history = useHistory()
//     const dispatch = useDispatch()
//     const findGame = useSelector(state => state.game.oneGame)
//     const [loaded, setLoaded] = useState(false)
//     let [values, setValues] = useState(false)
//     let [datetime, setDatetime] = useState('')
//     useEffect(() => {
//         dispatch(getOneGame(gameId)).then(() => {
//             setLoaded(true)
//             if (findGame && findGame.Game) {
//                 const game = findGame.Game[0]
//                 const gameSplit = game.datetime.split(' ')
//                 const day = gameSplit[1]
//                 const month = getMonth(gameSplit[2])
//                 const year = gameSplit[3]
//                 const time = gameSplit[4]
//                 const datetime = (`${year}-${month}-${day}T${time}`)
//                 setDatetime(datetime)
//                 setValues(true)
//             }
//         })
//     }, [dispatch, findGame])



//     const getMonth = (str) => {
//         if (str == 'Jan') return '01'
//         if (str == 'Feb') return '02'
//         if (str == 'Mar') return '03'
//         if (str == 'Apr') return '04'
//         if (str == 'May') return '05'
//         if (str == 'Jun') return '06'
//         if (str == 'Jul') return '07'
//         if (str == 'Aug') return '08'
//         if (str == 'Sep') return '09'
//         if (str == 'Oct') return '10'
//         if (str == 'Nov') return '11'
//         if (str == 'Dec') return '12'
//     }

//     return loaded && values && (
//         < div className="game-form-container" >
//             <form className="game-form">
//                 <input
//                     type='datetime-local'
//                     placeholder='datetime'
//                     value={datetime}
//                     onChange={(e) => setDatetime(e.target.value)}
//                 ></input>
//             </form>
//         </div >
//     )
// }

// export default EditGame
// import { useEffect, useState } from "react";
// import { useDispatch, useSelector } from "react-redux"
// import { NavLink, useParams, useHistory } from "react-router-dom";
// import './EditGame.css'
// import { edittingGame, getOneGame } from "../../store/game";

// const EditGame = () => {
//     const { gameId } = useParams()
//     const history = useHistory()
//     const dispatch = useDispatch()
//     const findGame = useSelector(state => state.game.oneGame)
//     let [datetime, setDatetime] = useState(null)

//     useEffect(() => {
//         dispatch(getOneGame(gameId))
//     }, [gameId])

//     useEffect(() => {
//         setDatetime(findGame && findGame.Game ? findGame.Game[0].datetime : null)
//     }, [findGame])

//     const getMonth = (str) => {
//         if (str == 'Jan') return '01'
//         if (str == 'Feb') return '02'
//         if (str == 'Mar') return '03'
//         if (str == 'Apr') return '04'
//         if (str == 'May') return '05'
//         if (str == 'Jun') return '06'
//         if (str == 'Jul') return '07'
//         if (str == 'Aug') return '08'
//         if (str == 'Sep') return '09'
//         if (str == 'Oct') return '10'
//         if (str == 'Nov') return '11'
//         if (str == 'Dec') return '12'
//     }

//     return datetime && (
//         < div className="game-form-container" >
//             <form className="game-form">
//                 <input
//                     type='datetime-local'
//                     placeholder='datetime'
//                     value={datetime}
//                     onChange={(e) => setDatetime(e.target.value)}
//                 ></input>
//             </form>
//         </div >
//     )
// }

// export default EditGame
