import React from 'react';
import { View, Text, Pressable } from 'react-native';
import styles from '../../styles/HomeStyles';

import { Vibe } from '../../api/VibeAPI';

import Navbar from '../Navbar';

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

    function openVibeMaker() {
        navigation.navigate("VibeMaker");
    }

    function openAccountPanel() {
        navigation.navigate("Account");
    }

    return (
        <>
            <View style={ styles.home }>
                <Pressable onPressOut={ () => openAccountPanel() }>
                    <Text>
                        Account
                    </Text>
                </Pressable>

                <Pressable onPressOut={ () => openVibeMaker() }>
                    <Text>
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
                    <View key={`vibe-${vibe.name}`}>
                        <View>
                            <Text>
                                o_o
                            </Text>
                        </View>

                        <Text>
                            { vibe.name }
                        </Text>
                    </View>
                )) }
            </View>

            <Navbar navigation={ navigation }/>
        </>
    )
}

export default Home;