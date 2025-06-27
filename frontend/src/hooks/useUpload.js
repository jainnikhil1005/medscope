import { commitMutation } from 'react-relay';
import graphql from 'babel-plugin-relay/macro';
import RelayEnvironment from '../RelayEnvironment';

const mutation = graphql`
  mutation CheckInteractionMutation($p1: Upload!, $p2: Upload!) {
    checkInteraction(p1: $p1, p2: $p2) {
      prescription1Id
      prescription2Id
      status
      details
    }
  }
`;

