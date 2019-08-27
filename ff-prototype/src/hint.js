import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import ImageExampleBordered from './hintpic';
import './hint.css';
import CardExampleGroups from './hintcontent'


function hintoverview() {
    return (
        <div className="background">
            <ImageExampleBordered />
            <div className="center">
                <CardExampleGroups />
            </div>
        </div>
    );
}

export default hintoverview;

