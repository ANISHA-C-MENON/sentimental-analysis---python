import React, { Component } from "react";
import {
    View,
    Text,
    StyleSheet,
    Dimensions
} from "react-native";
import Slideshow from 'react-native-image-slider-show';

const { height, width } = Dimensions.get('window')

export default class SlideshowTest extends Component {
    constructor(props) {
        super(props);

        this.state = {
            position: 5,
            interval: null,
            dataSource: [
                {
                    // title: 'Title 1',
                    // caption: 'Caption 1',
                    url: 'https://wallpapers.moviemania.io/phone/movie/400928/e132e0/gifted-phone-wallpaper.jpg?w=1520&h=2662&q=90&dl=gifted_e132_1520x2662.jpg'
                }, {
                    // title: 'Title 2',
                    // caption: 'Caption 2',
                    url: 'https://wallpapers.moviemania.io/phone/movie/72976/3ffa0f/lincoln-phone-wallpaper.jpg?w=1520&h=2662&q=90&dl=lincoln_3ffa_1520x2662.jpg',
                   
                }, {
                    // title: 'Title 3',
                    // caption: 'Caption 3',
                    url: 'https://wallpapers.moviemania.io/phone/movie/296096/7347da/me-before-you-phone-wallpaper.jpg?w=1520&h=2662&q=90&dl=me-before-you_7347_1520x2662.jpg',

                },
                {
                    // title: 'Title 4',
                    // caption: 'Caption 4',
                    url: 'https://wallpapers.moviemania.io/phone/tv/66732/5e1bd9/stranger-things-phone-wallpaper.jpg?w=1520&h=2662&q=90&dl=stranger-things_5e1b_1520x2662.jpg',

                },
                {
                    // title: 'Title 5',
                    // caption: 'Caption 5',
                    url: 'https://wallpapers.moviemania.io/phone/movie/391713/9ca52b/lady-bird-phone-wallpaper.jpg?w=1520&h=2662&q=90&dl=lady-bird_9ca5_1520x2662.jpg',

                },
                {
                    // title: 'Title 6',
                    // caption: 'Caption 6',
                    url: 'https://wallpapers.moviemania.io/phone/movie/475557/d4c34f/joker-phone-wallpaper.jpg?w=1520&h=2662&q=90&dl=joker_d4c3_1520x2662.jpg',

                },
                {
                    // title: 'Title 7',
                    // caption: 'Caption 7',
                    url: 'https://wallpapers.moviemania.io/phone/movie/420818/3ff634/the-lion-king-phone-wallpaper.jpg?w=1520&h=2662&q=90&dl=the-lion-king_3ff6_1520x2662.jpg',

                },
                {
                    // title: 'Title 8',
                    // caption: 'Caption 8',
                    url: 'https://wallpapers.moviemania.io/phone/movie/313369/004232/la-la-land-phone-wallpaper.jpg?w=1520&h=2662&q=90&dl=la-la-land_0042_1520x2662.jpg',

                },

            ],
        };
    }

    componentWillMount() {
        this.setState({
            interval: setInterval(() => {
                this.setState({
                    position: this.state.position === this.state.dataSource.length ? 0 : this.state.position + 1
                });
            }, 5000)
        });
    }

    componentWillUnmount() {
        clearInterval(this.state.interval);
    }

    render() {
        return (
            <View style={{  }}>
                <Slideshow
                    dataSource={this.state.dataSource}
                    height={height}
                    arrowSize={0}
                    indicatorSize={0}
                    containerStyle={{ justifyContent:'center', alignItems:'center' }}
                    position={this.state.position}
                    onPositionChanged={position => this.setState({ position })} />
            </View>

        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center'
    }
});