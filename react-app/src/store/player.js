const LOAD_ALL_PLAYERS = '/players/LOAD_ALL_PLAYERS'
const LOAD_ONE_PLAYER = '/players/LOAD_ONE_PLAYER'
const ADD_PLAYER = '/players/ADD_PLAYER'
const EDIT_PLAYER = '/players/EDIT_PLAYER'
const DELETE_PLAYER = '/players/DELETE_PLAYER'

const allPlayers = players => {
    return {
        type: LOAD_ALL_PLAYERS, players
    }
}

const onePlayer = player => {
    return {
        type: LOAD_ONE_PLAYER, player
    }
}

const addPlayer = player => {
    return {
        type: ADD_PLAYER, player
    }
}

const deletePlayer = player => {
    return {
        type: DELETE_PLAYER, player
    }
}

const editPlayer = player => {
    return {
        type: EDIT_PLAYER, player
    }
}

export const getAllPlayers = teamId => async dispatch => {
    const response = await fetch(`/api/players/${teamId}`)
    if (response.ok) {
        const players = await response.json()
        console.log('STORE PLAYERS', players)
        dispatch(allPlayers(players))
    }
}

export const getOnePlayer = playerId => async dispatch => {
    const response = await fetch(`/api/players/player/${playerId}`)
    if (response.ok) {
        const player = await response.json()
        dispatch(onePlayer(player))
        return player
    }
}

export const addingPlayer = (teamId, player) => async dispatch => {
    const response = await fetch(`/api/players/${teamId}/add`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(player)

    })
    if (response.ok) {
        const player = response.json()
        dispatch(addPlayer(player))
        return player
    }
}

export const edittingPlayer = (teamId, playerId, player) => async dispatch => {
    const response = await fetch(`/api/players/${teamId}/${playerId}/edit`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(player)
    })
    if (response.ok) {
        const player = response.json()
        dispatch(editPlayer(player))
        return player
    }
}

export const deletingPlayer = id => async dispatch => {
    const response = await fetch(`/api/players//player/${id}/delete`, {
        method: 'DELETE'
    })
    if (response.ok) {
        const player = await response.json()
        await dispatch(deletePlayer(player))
        return player
    }
}

export default function reducer(state = { onePlayer: {}, allPlayers: {} }, action) {
    switch (action.type) {
        case LOAD_ALL_PLAYERS: {
            const newState = { onePlayer: {}, allPlayers: {} }
            action.players.Players.forEach(e => {
                newState.allPlayers[e.id] = e
            })
            return newState
        }
        case LOAD_ONE_PLAYER: {
            const newState = { onePlayer: {}, allPlayers: {} }
            newState.onePlayer = action.player
            return newState
        }
        case ADD_PLAYER: {
            const newState = { ...state, onePlayer: { ...state.onePlayer }, allPlayers: { ...state.allPlayers } }
            newState.onePlayer = action.player
            return newState
        }
        case EDIT_PLAYER: {
            const newState = { ...state, onePlayer: { ...state.onePlayer }, allPlayers: { ...state.allPlayers } }
            newState.allPlayers[action.player.id] = action.player
            newState.onePlayer = action.player
            return newState
        }
        case DELETE_PLAYER: {
            const newState = { ...state, onePlayer: { ...state.onePlayer }, allPlayers: { ...state.allPlayers } }
            delete newState.allPlayers[action.player.id]
            return newState
        }
        default: return state
    }
}
