"use strict";

class Nav extends React.Component {
    constructor(){
        super();

        this.state = {
            name:'_'
        };
    }

    render(){
        return (
        <span><h1>react component nav bar</h1></span>
        );
        
    }
}

ReactDOM.render(
<Nav />,
document.getElementById('bar')
);