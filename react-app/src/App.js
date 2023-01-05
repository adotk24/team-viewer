import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/Navigation/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import LandingPage from './components/LandingPage/LandingPage';
import AllTeams from './components/AllTeams/AllTeams';
import OneTeam from './components/TeamDetail/TeamDetail';
import AddTeam from './components/AddTeam/AddTeam';
import EditTeam from './components/EditTeam/EditTeam';
import Roster from './components/Roster/Roster';
import PlayerDetail from './components/PlayerDetail/PlayerDetail';
import EditPlayer from './components/EditPlayer/EditPlayer';
import AddPlayer from './components/AddPlayer/AddPlayer';
import UserTeams from './components/UserTeams/UserTeams';
import EditGame from './components/EditGame/EditGame';
import AddGame from './components/AddGame/AddGame';


function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <Route path='/' exact={true} >
          <LandingPage />
        </Route>
        <Route path='/user/team' exact={true} >
          <UserTeams />
        </Route>
        <Route path='/teams' exact={true} >
          <AllTeams />
        </Route>
        <Route path='/teams/team/add' exact={true}>
          <AddTeam />
        </Route>
        <Route path='/teams/:teamId/roster' exact={true}>
          <Roster />
        </Route>
        <Route path='/teams/:teamId/addPlayer' exact={true}>
          <AddPlayer />
        </Route>
        <Route path='/teams/players/:playerId' exact={true}>
          <PlayerDetail />
        </Route>
        <Route path='/teams/players/:playerId/edit' exact={true}>
          <EditPlayer />
        </Route>
        <Route path='/teams/:teamId' exact={true}>
          <OneTeam />
        </Route>
        <Route path='/teams/:teamId/edit' exact={true}>
          <EditTeam />
        </Route>
        <Route path='/teams/schedule/game/:gameId/edit' exact={true}>
          <EditGame />
        </Route>
        <Route path='/teams/schedule/game/add' exact={true}>
          <AddGame />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
