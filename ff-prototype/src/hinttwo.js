import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import ImageExampleBordered from './hintpic';
import './hint.css';
import HintCardTwo from './hintcontenttwo'


function hintoverview() {
    return (
        <div className="background">
            <ImageExampleBordered />
            <div className="center">
                <HintCardTwo />
            </div>
        </div>
    );
}

export default hintoverview;

