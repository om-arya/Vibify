import React from 'react';
import { View, Pressable } from 'react-native';
import styles from '../styles/HomeStyles';

import Navbar from './Navbar';

const Home: React.FC<any> = ({ navigator }) => {
    function openVibeMaker() {
        
    }

    return (
        <View style={styles.home}>
            <Pressable onPressOut={() => openVibeMaker()}></Pressable>
            <Navbar />
        </View>
    )
}

export default Home;