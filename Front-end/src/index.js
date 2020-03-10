import React, { Component } from "react";
import { 
    View,
    Text,
    StyleSheet
} from "react-native";
import MainNavigator from "./homescreen";

class App extends Component {
    render() {
        return (
            
                <MainNavigator/>
            
        );
    }
}
export default App;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center'
    }
});