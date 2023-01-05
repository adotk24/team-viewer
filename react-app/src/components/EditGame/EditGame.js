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
    const [matchup, setMatchup] = useState(null)


    useEffect(() => {
        dispatch(getOneGame(gameId)).then(() => {
            dispatch(getAllTeams()).then(() => {
                setLoaded(true)
            })
        })
    }, [gameId])

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
            // console.log('GAME', game)
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

    const handleSubmit = async (e) => {
        e.preventDefault()
        console.log('submit', datetime)

    }

    return datetime && isLoaded && (
        < div className="game-form-container" >
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
                    value={team1}
                    onChange={(e) => setTeam1(e.target.value)}>
                    {findTeams.map(e => (
                        <option>{e.name}</option>
                    ))}
                </select>

                <label>Team 2</label>
                <select
                    className="game-team-input"
                    placeholder={team2}
                    value={team2}
                    onChange={(e) => setTeam2(e.target.value)}>
                    {findTeams.map(e => (
                        <option>{e.name}</option>
                    ))}
                </select>
                <button type='submit'
                    className="submit-add-game">
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
