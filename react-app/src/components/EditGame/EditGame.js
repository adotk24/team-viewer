import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import './EditGame.css'
import { edittingGame, getOneGame } from "../../store/game";

const EditGame = () => {
    const { gameId } = useParams()
    const history = useHistory()
    const dispatch = useDispatch()
    const findGame = useSelector(state => state.game.oneGame)
    const [loaded, setLoaded] = useState(false)
    let [values, setValues] = useState(false)
    useEffect(() => {
        dispatch(getOneGame(gameId)).then(() => {
            setLoaded(true)
            if (findGame && findGame.Game) {
                const game = findGame.Game[0]
                const gameSplit = game.datetime.split(' ')
                const day = gameSplit[1]
                const month = getMonth(gameSplit[2])
                const year = gameSplit[3]
                const time = gameSplit[4]
                const datetime = (`${year}-${month}-${day}T${time}`)
                setDatetime(datetime)
                setValues(true)
            }
        })
    }, [gameId])
    // useEffect(() => {
    //     dispatch(getOneGame(gameId)).then(() => {
    //         isLoaded(true)
    //     })
    // }, [gameId])


    let [datetime, setDatetime] = useState('2020-01-01T00:00')
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

    // useEffect(() => {
    //     setDatetime(datetime)
    // }, [datetime])


    // if (loaded && !values) {
    //     game = findGame.Game[0]
    //     const gameSplit = game.datetime.split(' ')
    //     day = gameSplit[1]
    //     month = getMonth(gameSplit[2])
    //     year = gameSplit[3]
    //     time = gameSplit[4]
    //     datetime = (`${year}-${month}-${day}T${time}`)
    //     console.log('VALUES', values)
    //     setValues(true)
    //     console.log('VALUES POST', values)
    // }


    console.log('RIGHT BEFORE RETURN', datetime)
    return loaded && values && (
        < div className="game-form-container" >
            <form className="game-form">
                <input
                    type='datetime-local'
                    placeholder='datetime'
                    value={datetime}
                    onChange={(e) => setDatetime(e.target.value)}
                ></input>
            </form>
        </div >
    )
}

export default EditGame
