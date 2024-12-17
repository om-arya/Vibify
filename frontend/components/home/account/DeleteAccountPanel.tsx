import React from 'react';
import { View, Text, Pressable } from 'react-native';
import styles from '../../../styles/HomeStyles';

interface DeleteAccountPanelProps {
    navigation: any,
}

function DeleteAccountPanel({ navigation }: DeleteAccountPanelProps) {
    function closeDeleteAccountPanel() {
        navigation.navigate("Account");
    }

    return (
        <View>
            <Pressable onPressOut={ () => closeDeleteAccountPanel() }>
                <Text>
                    ← Back
                </Text>
            </Pressable>

            <Text>
                Delete Account
            </Text>
        </View>
    )
}

export default DeleteAccountPanel;