import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Redirect, useHistory } from 'react-router-dom';
import { login } from '../../store/session';
import * as sessionActions from '../../store/session'
import './LoginForm.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory()
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  // const [errorsShow, setErrorsShown] = useState(false);

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      const validation = []
      if (!email.includes('@')) validation.push("Invalid email.")
      setErrors(validation)
      setErrors(data);
    }
  };
  // useEffect(() => {
  // }, [email])

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }
  const handleDemoUserSubmit = async (e) => {
    e.preventDefault(0)
    dispatch(sessionActions.login('demo@aa.io', 'password'))
    history.goBack()
    // .catch(
    // async (res) => {
    // const data = await res.json();
    // if (data && data.errors) {
    // return setErrors(data.errors)
    // }
    // }
    // );
  }

  return (
    <div className='log-in-form-container'>
      <form className='log-in-form' onSubmit={onLogin}>
        <div className='log-in-form-header'>
          Sign In
        </div>
        <div className='login-errors'>
          {errors &&
            errors.map((error, ind) => (
              <div key={ind}>{error}</div>
            ))}
        </div>
        <div className='login-email-input'>
          <label htmlFor='email'>Email</label>
          <input
            name='email'
            type='text'
            placeholder='Email'
            value={email}
            onChange={updateEmail}
            className='email-input-login'
          />
        </div>
        <div className='login-password-input'>
          <label htmlFor='password'>Password</label>
          <input
            name='password'
            type='password'
            placeholder='Password'
            value={password}
            onChange={updatePassword}
            className='password-input-login'
          />
        </div>
        <button className='login-form-submit' type='submit'>Sign In</button>
        <button className="DemoUserButton" onClick={handleDemoUserSubmit}>Demo User</button>

        <NavLink to={'/sign-up'} exact={true}>
          <button className='createAccountFromLogin'>Create An Account</button>
        </NavLink>
      </form>
    </div>
  );
};

export default LoginForm;
