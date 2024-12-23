import React from 'react';
import { View, Text, Pressable } from 'react-native';
import styles from '../../../styles/HomeStyles';

interface SignupPanelProps {
    navigation: any,
}

function SignupPanel({ navigation }: SignupPanelProps) {
    function closeSignupPanel() {
        navigation.navigate("Account");
    }

    return (
        <View style={ styles.signupPanel }>
            <Pressable onPressOut={ () => closeSignupPanel() }>
                <Text>
                    ← Back
                </Text>
            </Pressable>

            <Text>
                Sign Up
            </Text>
        </View>
    )
}

export default SignupPanel;