import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getStatsBygame } from "../../store/stat";
import { getOneGame } from '../../store/game';
import { IndiGames } from "../IndiGames/IndiGames";
import { getAllUserTeams } from '../../store/team';
import './GameDetailRow.css'


const GameDetailRow = () => {
    return (
        <div>Testing</div>
    )
}

export default GameDetailRow
