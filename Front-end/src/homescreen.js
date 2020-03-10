import React, { Component } from "react";
import {
    View,
    Text,
    StyleSheet,
    Dimensions,
    StatusBar
} from "react-native";
import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import SearchScreen from "./searchscreen";
import Carousel from "./carousel";
import Icon from "react-native-vector-icons/Ionicons";


const { height, width } = Dimensions.get('window')

class HomeScreen extends Component {

    render() {
        console.disableYellowBox = true;

        return (
            <View >

                <StatusBar translucent backgroundColor="transparent" />
                <View style={{}} >
                    <Carousel />
                </View>

                <View style={{ position: 'absolute', zIndex: 2000 }}>
                    <Text style={{ left: 10, top: 230, color: 'white', fontSize: 40, fontWeight: 'bold' }}>
                        Get Emotion Based Movie Recommendations.
                    </Text>
                </View>
                <View style={{ position: 'absolute', zIndex: 3000, top: height / 2 + 10, left: width - 45 }}>
                    <Icon onPress={() => this.props.navigation.navigate('Search')} style={[{ color: 'white', backgroundColor: 'red', borderRadius: 17, padding: 4 }]} size={60} name={'ios-arrow-forward'} />
                </View>

            </View>
        );
    }


}

const Navigator = createStackNavigator({
    Home: {
        screen: HomeScreen,
        navigationOptions: {
            headerTitle: <Text style={{ fontSize: 20, padding: 10, fontWeight: 'bold', color: 'red' }}>EMOVIZ</Text>
        }
    },
    Search: {
        screen: SearchScreen,
        navigationOptions: {


        }
    }



});

const MainNavigator = createAppContainer(Navigator);
export default MainNavigator;

const styles = StyleSheet.create({
    placeHolder: {
        flex: 1,
        marginTop: 40,
        alignItems: 'center',
        justifyContent: 'center'
    }
});