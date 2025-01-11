import React from 'react';
import { View, Text, Pressable, Switch } from 'react-native';
import styles from '../../styles/HomeStyles';

interface AccountPanelProps {
    navigation: any,
}

function AccountPanel({ navigation }: AccountPanelProps) {
    function closeAccountPanel() {
        navigation.navigate("Home");
    }

    function openSignupPanel() {
        navigation.navigate("Signup");
    }

    function openLoginPanel() {
        navigation.navigate("Login");
    }

    function openDeleteAccountPanel() {
        navigation.navigate("DeleteAccount");
    }

    return (
        <View style={ styles.accountPanel }>
            <Pressable onPressOut={ () => closeAccountPanel() }>
                <Text>
                    ← Back
                </Text>
            </Pressable>

            <Pressable onPressOut={ () => openSignupPanel() }>
                <Text>
                    Sign Up
                </Text>
            </Pressable>

            <Pressable onPressOut={ () => openLoginPanel() }>
                <Text>
                    Log In
                </Text>
            </Pressable>

            <Pressable onPressOut={ () => openDeleteAccountPanel() }>
                <Text>
                    Delete Account
                </Text>
            </Pressable>
        </View>
    )
}

export default AccountPanel;