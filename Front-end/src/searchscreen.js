import React, { Component } from "react";
import { 
    View,
    Text,
    StyleSheet,
    ScrollView,
    FlatList,
    TextInput,
    TouchableWithoutFeedback
} from "react-native";
import axios from 'axios';

export default class SearchScreen extends Component {

    state = {
        loading: true,
        data: [],
    };


    componentDidMount() {


    }

    render() {


        return (
            <ScrollView >
               

                <View style={styles.container}>
                    <TextInput placeholder="How You Feeling Today ?"
                        onChangeText={text => this.setState({ search: text })}
                        style={{ marginTop: 30, backgroundColor: '#ccc', marginLeft: 10, marginRight: 10, borderRadius:18, padding:10 }} onSubmitEditing={() => {

                            this.setState({
                                data: []
                            })
                            axios.get(`https://secure-castle-31038.herokuapp.com/${this.state.search}`)
                                .then(response => {
                                //    console.log(`https://secure-castle-31038.herokuapp.com/${this.state.search}`)
                                  //  const array = Object.values(response.data);
                                 //   console.log(array)

                                    this.setState({ data: Object.values(response.data) });
                                })
                                .catch(error => {
                                    console.log(error);
                                });
                        }}
                    />
                    <Text style={{ marginTop:10, padding: 12, color: 'red', fontSize: 18, fontWeight: 'bold' }}>RECOMMENDED MOVIES</Text>
                    <FlatList
                        showsVerticalScrollIndicator={false}
                        horizontal={false}
                        data={this.state.data}
                        extraData={this.state.data}
                        keyExtractor={(item, index) => index.toString()}
                        renderItem={({ item, index }) => this.renderList(item, index)}
                    />
                </View>



            </ScrollView>
        );
    }

    renderList(item, index) {

        return (
            <TouchableWithoutFeedback
                onPress={() => {
                    this.setState(previousIndex => {
                        return {
                            selectedTopTapBarIndex: index
                        };
                    });
                }}>
                <View style={{ justifyContent: 'center', flex: 1, padding: 7 }}>
                    <Text style={
                        {
                            //justifyContent: 'center',
                            marginLeft: 10,
                            backgroundColor: 'white',
                            borderWidth: 0,
                            //elevation: 3,
                            borderRadius: 0,
                            color: 'black',
                            fontSize: 15,
                            fontWeight: 'bold',
                        }}>
                        {item['Name']}
                    </Text>

                </View>
            </TouchableWithoutFeedback>
        );
    }

}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        
    }
});