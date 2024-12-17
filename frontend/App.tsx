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
          <Stack.Screen name="Account" component={ AccountPanel } options={{ headerShown: false }} />
          <Stack.Screen name="Signup" component={ SignupPanel } options={{ headerShown: false, presentation: 'modal' }} />
          <Stack.Screen name="Login" component={ LoginPanel } options={{ headerShown: false, presentation: 'modal' }} />
          <Stack.Screen name="DeleteAccount" component={ DeleteAccountPanel } options={{ headerShown: false, presentation: 'modal' }} />
          <Stack.Screen name="VibeMaker" component={ VibeMaker } options={{ headerShown: false, presentation: 'modal' }} />

          <Stack.Screen name="Library" component={ Library } options={{ headerShown: false, animation: 'none' }} />
       </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;