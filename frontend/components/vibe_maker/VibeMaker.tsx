import React, { useState } from 'react';
import { Text, TextInput, View, Pressable } from 'react-native';
import styles from '../../styles/HomeStyles';

import Navbar from '../Navbar';

interface VibeMakerProps {
    navigation: any;
}

function VibeMaker({ navigation }: VibeMakerProps) {
    const [vibeName, setVibeName] = useState("");
    const [vibeColor, setVibeColor] = useState("gray");
    const [vibePrompt, setVibePrompt] = useState("");

    const colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray"];

    function closeVibeMaker() {
        navigation.navigate("Home");
    }

    function createVibe() {
        // TODO: Pull danceability, energy, and valence from PyTorch
        const newVibe: Vibe = {
            name: vibeName,
            color: vibeColor
        };

        // TODO: Update state and DB
        closeVibeMaker();
    }

    return (
        <>
            <View style={ styles.vibeMaker }>
                <View style={ styles.vibeMakerTopBar }>
                    <Pressable onPressOut={ () => closeVibeMaker() }>
                        <Text>
                            ← Back
                        </Text>
                    </Pressable>
                </View>

                <View>
                    <Text>
                        o_o
                    </Text>
                </View>

                <View>
                    <Text>
                        Name
                    </Text>

                    <TextInput value={ vibeName }
                               onChangeText={ (text) => setVibeName(text) }/>
                </View>

                <View>
                    <Text>
                        Color
                    </Text>

                    { colors.map((color) => (
                        <Pressable
                            key={`color-${color}`}
                            onPressOut={ () => setVibeColor(color) }>
                        </Pressable>
                    )) }
                </View>

                <View>
                    <Text>
                        What's the vibe?
                    </Text>

                    <TextInput value={ vibePrompt }
                               onChangeText={ (text) => setVibePrompt(text) }/>
                </View>

                <Pressable style={ styles.makeItButton }
                           onPressOut={ () => createVibe() }>
                    <Text style={ styles.makeItButtonText }>
                        Make It!
                    </Text>
                </Pressable>
            </View>

            <Navbar navigation={ navigation }/>
        </>
    )
}

export default VibeMaker;