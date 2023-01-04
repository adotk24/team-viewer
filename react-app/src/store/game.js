const LOAD_ALL_GAMES_BY_TEAM = '/games/LOAD_ALL_GAMES_BY_TEAM'
const LOAD_ONE_GAME = '/games/LOAD_ONE_GAME'
const ADD_GAME = '/games/ADD_GAME'
const EDIT_GAME = '/games/EDIT_GAME'
const DELETE_GAME = '/games/DELETE_GAME'

const allGamesByTeam = games => {
    return {
        type: LOAD_ALL_GAMES_BY_TEAM, games
    }
}

const oneGame = game => {
    return {
        type: LOAD_ONE_GAME, game
    }
}

const addGame = game => {
    return {
        type: ADD_GAME, game
    }
}

const editGame = game => {
    return {
        type: EDIT_GAME, game
    }
}

const deleteGame = game => {
    return {
        type: DELETE_GAME, game
    }
}

export const getAllGamesByTeam = teamId => async dispatch => {
    const response = await fetch(`/api/games/team/${teamId}`)
    if (response.ok) {
        const games = await response.json()
        dispatch(allGamesByTeam(games))
        return games
    }
}

export const getOneGame = gameId => async dispatch => {
    const response = await fetch(`/api/games/${gameId}`)
    if (response.ok) {
        const game = await response.json()
        dispatch(oneGame(game))
        return game
    }
}

export const addingGame = (game) => async dispatch => {
    const response = await fetch(`/api/games/add`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(game)
    })
    if (response.ok) {
        const game = response.json()
        dispatch(addGame(game))
        return game
    }
}

export const edittingGame = (gameId, game) => async dispatch => {
    const response = await fetch(`/api/games/${gameId}/edit`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(game)
    })
    if (response.ok) {
        const game = response.json()
        dispatch(editGame(game))
        return game
    }
}

export const deletingGame = gameId => async dispatch => {
    const response = await fetch(`/api/games/${gameId}/delete`, { method: 'DELETE' })
    if (response.ok) {
        const game = await response.json()
        await dispatch(deleteGame(game))
        return game
    }
}

export default function reducer(state = { oneGame: {}, allGames: {} }, action) {
    switch (action.type) {
        case LOAD_ALL_GAMES_BY_TEAM: {
            const newState = { ...state, oneGame: { ...state.oneGame }, allGames: {} }
            action.games.Games.forEach(e => {
                newState.allGames[e.id] = e
            })
            return newState
        }
        case LOAD_ONE_GAME: {
            const newState = { ...state, oneGame: {}, allGames: { ...state.allGames } }
            newState.oneGame = action.game
            return newState
        }
        case ADD_GAME: {
            const newState = { ...state, oneGame: { ...state.oneGame }, allGames: { ...state.allGames } }
            newState.oneGame = action.game
            return newState
        }
        case EDIT_GAME: {
            const newState = { ...state, oneGame: { ...state.oneGame }, allGames: { ...state.allGames } }
            newState.allGames[action.game.id] = action.game
            newState.oneGame = action.game
            return newState
        }
        case DELETE_GAME: {
            const newState = { ...state, oneGame: { ...state.oneGame }, allGames: { ...state.allGames } }
            delete newState.allGames[action.game.id]
            return newState
        }
        default: return state
    }
}
