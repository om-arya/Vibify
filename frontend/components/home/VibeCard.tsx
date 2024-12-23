import React from "react";
import { View, Text } from "react-native";

interface VibeCardProps {
    name: string;
    color: string;
}

function VibeCard({ name, color }: VibeCardProps) {
    return (
        <View key={`vibe-${name}`}>
            <View>
                <Text>
                    o_o
                </Text>
            </View>

            <Text>
                { name }
            </Text>
        </View>
    )
}

export default VibeCard;