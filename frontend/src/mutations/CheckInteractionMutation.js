import graphql from 'babel-plugin-relay/macro';

export default graphql`
  mutation CheckInteractionMutation($p1: Upload!, $p2: Upload!) {
    checkInteraction(p1: $p1, p2: $p2) {
      prescription1Id
      prescription2Id
      status
      details
    }
  }
`;