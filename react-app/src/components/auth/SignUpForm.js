import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { NavLink, Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import './SignUpForm.css'

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    const validation = [];
    if (password !== repeatPassword) validation.push('Passwords Must Match')
    if (!email.includes('@')) validation.push("Invalid email.")
    if (!username) validation.push('Need Username')

    setErrors(validation)
    if (password === repeatPassword && email.includes('@')) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data)
      }
    }
  };

  // useEffect(() => {
  //   const validation = []
  //   if (!email.includes('@')) validation.push("Invalid email.")
  //   if (password !== repeatPassword) validation.push('Passwords Must Match')
  //   setErrors(validation)
  // }, [email, password, repeatPassword])

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <div className='sign-up-form-container'>
      <form className='sign-up-form' onSubmit={onSignUp}>
        <div className='sign-up-form-header'>Create Account</div>
        <div className='sign-up-errors'>
          {errors.map((error, ind) => (
            <div key={ind}>{error}</div>
          ))}
        </div>
        <div className='sign-up-username-input'>
          <label>User Name</label>
          <input
            type='text'
            name='username'
            onChange={updateUsername}
            value={username}
            className='username-input-signup'
            placeholder='User Name'
          ></input>
        </div>
        <div className='sign-up-email-input'>
          <label>Email</label>
          <input
            type='text'
            name='email'
            onChange={updateEmail}
            value={email}
            className='email-input-signup'
            placeholder='Email Address'
          ></input>
        </div>
        <div className='sign-up-password-input'>
          <label>Password</label>
          <input
            type='password'
            name='password'
            onChange={updatePassword}
            value={password}
            placeholder='Password'
            className='password-input-signup'
          ></input>
        </div>
        <div className='sign-up-password-input'>
          <label>Repeat</label>
          <input
            type='password'
            name='repeat_password'
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
            className='password-input-signup'
            placeholder='Repeat Password'
          ></input>
        </div>
        <button type='submit' className='signupsubmit'>Sign Up</button>
        <NavLink to={'/login'} exact={true}>
          <button className='createAccountFromLogin'>Already Have an Account?</button>
        </NavLink>
      </form>
    </div>
  );
};

export default SignUpForm;
