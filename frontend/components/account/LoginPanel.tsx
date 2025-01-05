import React from 'react';
import { View, Text, Pressable } from 'react-native';
import styles from '../../../styles/HomeStyles';

interface LoginPanelProps {
    navigation: any,
}

function LoginPanel({ navigation }: LoginPanelProps) {
    function closeLoginPanel() {
        navigation.navigate("Account");
    }

    return (
        <View style={ styles.loginPanel }>
            <Pressable onPressOut={ () => closeLoginPanel() }>
                <Text>
                    ← Back
                </Text>
            </Pressable>

            <Text>
                Log In
            </Text>
        </View>
    )
}

export default LoginPanel;