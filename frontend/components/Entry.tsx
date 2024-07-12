import React from 'react';
import { StyleSheet, View, Text, Button } from 'react-native';
import { StatusBar } from 'expo-status-bar';

const Entry: React.FC<any> = ({ navigation }) => {
    return (
        <View style={styles.form}>
            <Text style={styles.formText}>
                Please sign in.
            </Text>
            <Button
                title="Go to Home"
                onPress={() => navigation.navigate('Home')}
            />
        </View>
    )
}

const styles = StyleSheet.create({
    form: {
        backgroundColor: "black",
    },
    formText: {
        color: "white"
    }
})

export default Entry;