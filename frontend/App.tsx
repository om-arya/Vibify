import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Entry from './components/Entry';
import Home from './components/Home';
import VibeMaker from './components/VibeMaker';

export default function App() {
  const Stack = createNativeStackNavigator();

  return (
    <NavigationContainer>
       <Stack.Navigator initialRouteName="Entry" screenOptions={{ headerShown: false, gestureEnabled: false }}>
          <Stack.Screen name="Entry" component={ Entry } />
          <Stack.Screen name="Home" component={ Home } />
          <Stack.Screen name="VibeMaker" component={ VibeMaker } />
       </Stack.Navigator>
    </NavigationContainer>
  );
}