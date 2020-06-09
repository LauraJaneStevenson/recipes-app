
"use strict";

class Recipe extends React.Component {
    constructor() {
        super();

        this.state = {
            name:"",
            description: "",
            instructions: ""
        };   
    }

    componentDidMount() {
        const ID = document.querySelector('#recipe_id');
        console.log(ID.getAttribute('value'));
        $.get('/get_recipe.json', { recipe_id: ID.getAttribute('value') },(result) => {
            
            this.setState({ name:result.name,description:result.description, instructions:result.instructions });
            
        });
    }


    render() {
        return(
            <div>
            <h2>{this.state.name}</h2>
            <p>{this.state.description}</p>
            <p>{this.state.instructions}</p>
            </div>

        );

    }
        
}

ReactDOM.render(
    <Recipe />,
    document.getElementById('recipe')
);