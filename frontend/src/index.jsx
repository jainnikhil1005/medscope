import React from 'react';
import { hydrate, render } from 'react-dom';
import App from './App';
import RelayEnvironment from './RelayEnvironment';
import { RelayEnvironmentProvider } from 'react-relay/hooks';

const rootElement = document.getElementById('root');
const renderFn = rootElement.hasChildNodes() ? hydrate : render;

renderFn(
  <RelayEnvironmentProvider environment={RelayEnvironment}>
    <App />
  </RelayEnvironmentProvider>,
  rootElement
);