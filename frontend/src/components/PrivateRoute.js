import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';

const PrivateRoute = ({ component: Component, ...rest }) => {
  const { authData } = useAuth();

  return (
    <Route
      {...rest}
      render={props =>
        authData ? (
          <Component {...props} />
        ) : (
          <Redirect to={{ pathname: '/login', state: { from: props.location } }} />
        )
      }
    />
  );
};

export default PrivateRoute;