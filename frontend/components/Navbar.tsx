import React from 'react';
import { View, Text, Pressable } from 'react-native';
import Ionicons from '@expo/vector-icons/Ionicons';
import styles from '../styles/MainStyles';

interface NavbarProps {
    navigation: any,
}

function Navbar({ navigation }: NavbarProps) {
    function openHome() {
        navigation.navigate("Home");
    }

    function openLibrary() {
        navigation.navigate("Library");
    }

    return (
        <View style={ styles.navbar }>
            <Pressable style={ styles.navbarButton }
                       onPressOut={ () => openHome() }>
                <Ionicons name="home" size={32} color="white" />
                <Text style={ styles.navbarButtonLabel }>Home</Text>
            </Pressable>

            <Pressable style={ styles.navbarButton }
                       onPressOut={ () => openLibrary() }>
                <Ionicons name="grid-outline" size={32} color="white" />
                <Text style={ styles.navbarButtonLabel }>Library</Text>
            </Pressable>
        </View>
    )
}

export default Navbar;