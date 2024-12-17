import React from 'react';
import { View, Text, Pressable } from 'react-native';
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
            <Pressable onPressOut={ () => openHome() }>
                <Text style={ styles.navbarText }>Home</Text>
            </Pressable>

            <Pressable onPressOut={ () => openLibrary() }>
                <Text style={ styles.navbarText }>Library</Text>
            </Pressable>
        </View>
    )
}

export default Navbar;