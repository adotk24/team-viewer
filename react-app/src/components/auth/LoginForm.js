import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import * as sessionActions from '../../store/session'
import './LoginForm.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  // const [errorsShow, setErrorsShown] = useState(false);

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };
  useEffect(() => {
    const validation = []
    if (!email.includes('@')) validation.push("Invalid email.")
    setErrors(validation)
  }, [email])

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }
  const handleDemoUserSubmit = (e) => {

    e.preventDefault()
    return dispatch(sessionActions.login({ email: "demo@aa.io", password: 'password' }))
      .catch(
        async (res) => {
          const data = await res.json();
          if (data && data.errors) {
            return setErrors(data.errors)
          }
        }
      );
  }

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   setErrorsShown(true)

  //   if (!errors.length) {
  //     return dispatch(sessionActions.login({ email, password }))
  //       .then((res) => {
  //         if (res.errors) setErrors(res.errors)
  //         console.log('COMPONENT', res.errors)
  //       })
  //       .catch(
  //         async (res) => {
  //           const data = await res.json();
  //           if (data && data.errors) {
  //             setErrors(data.errors)
  //           }
  //         }
  //       );
  //   };
  // }
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
