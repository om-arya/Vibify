import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Home from './components/Home';
import VibeMaker from './components/VibeMaker';

export default function App() {
  const Stack = createNativeStackNavigator();

  return (
    <NavigationContainer>
       <Stack.Navigator initialRouteName="Home">
          <Stack.Screen name="Home" component={ Home } />
          <Stack.Screen name="VibeMaker" component={ VibeMaker } />
       </Stack.Navigator>
    </NavigationContainer>
  );
}