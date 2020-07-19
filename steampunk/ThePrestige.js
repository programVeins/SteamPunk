

import React, { useState } from 'react'

const ThePrestige = () => {

    const [director, setDirector] = useState('Nolan')
    const magic = ["The Pledge", "The Turn", "The Prestige"]

    return (
        <div className="container">
            <div className="section">
                <p> Every great magic trick consists of three parts or acts. And they are : </p>
                <br/>
                <ul>
                    {magic.map((act, index) => {
                        return(
                            <li>
                                {act}
                            </li>
                        );
                    })}
                </ul>
            </div>
        </div>
    )
}

export default ThePrestige