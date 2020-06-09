
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
        
        $.get('/get_recipe.json', { recipe_id: 1 },(result) => {
            alert(`${result.instructions}`);
            this.setState({ name:result.name,description:result.description, instructions:result.instructions });
            console.log(result.name)
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