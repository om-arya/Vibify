import React from 'react';
import { View, Text, Pressable } from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import styles from '../../styles/HomeStyles';

import { Vibe } from '../../api/VibeAPI';

import Navbar from '../Navbar';
import VibeCard from './VibeCard';

interface HomeProps {
    navigation: any;
}

function Home({ navigation }: HomeProps) {
    const samplevibe1: Vibe = {
        name: "Bob",
        color: "green",
        danceability: 4,
        energy: 5,
        valence: 6,
    };

    const samplevibe2: Vibe = {
        name: "Steve",
        color: "red",
        danceability: 9,
        energy: 10,
        valence: 8,
    };

    const vibes: Vibe[] = [samplevibe1, samplevibe2]; // TODO: Pull vibes from SessionState

    const noVibesMessage = "You don't have any vibes!"

    async function openVibeMaker() {
        navigation.navigate("VibeMaker");
    }

    function openAccountPanel() {
        navigation.navigate("Account");
    }

    return (
        <>
            <View style={ styles.home }>
                <View style={ styles.homeTopBar }>
                    <Pressable style={ styles.accountButton }
                            onPressOut={ () => openAccountPanel() }>
                        <MaterialCommunityIcons name="account" size={ 24 } color="black" />
                    </Pressable>
                </View>

                <Pressable style={ styles.createVibeButton }
                           onPressOut={ () => openVibeMaker() }>
                    <Text style={ styles.createVibeButtonText }>
                        + Create Vibe
                    </Text>
                </Pressable>

                { vibes.length === 0 &&
                    <View>
                        <Text>
                            { noVibesMessage }
                        </Text>
                    </View> }

                { vibes.map((vibe) => (
                    <VibeCard name={ vibe.name } color={ vibe.color } />
                )) }
            </View>

            <Navbar navigation={ navigation }/>
        </>
    )
}

export default Home;