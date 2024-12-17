import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Home from './components/home/Home';
import Library from './components/library/Library';
import VibeMaker from './components/home/VibeMaker';
import AccountPanel from './components/home/account/AccountPanel';
import LoginPanel from './components/home/account/LoginPanel';
import SignupPanel from './components/home/account/SignupPanel';
import DeleteAccountPanel from './components/home/account/DeleteAccountPanel';

function App() {
  const Stack = createNativeStackNavigator();

  return (
    <NavigationContainer>
       <Stack.Navigator initialRouteName="Home">
          <Stack.Screen name="Home" component={ Home } options={{ headerShown: false }} />
          <Stack.Screen name="AccountPanel" component={ AccountPanel } options={{ headerShown: false }} />
          <Stack.Screen name="LoginPanel" component={ LoginPanel } options={{ headerShown: false }} />
          <Stack.Screen name="VibeMaker" component={ VibeMaker } options={{ headerShown: false }} />

          <Stack.Screen name="Library" component={ Library } options={{ headerShown: false }} />
       </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;