import React from 'react';
import { Text, View, ScrollView } from 'react-native';
import styles from '../styles/VibeMakerStyles';


const VibeMaker: React.FC = () => {
    return (
        <ScrollView style={styles.vibeMaker}>
            <Text>Hello!</Text>
        </ScrollView>
    )
}

export default VibeMaker;