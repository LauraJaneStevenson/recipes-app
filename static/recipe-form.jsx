
"use strict";

class RecipeForm extends React.Component {
    constructor() {
        super();

        this.state = {
            ingredients: [],
            instructions: []
        };

        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {

        this.setState({ingredients: this.state.ingredients.push()})
    }

    render() {
        return(
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                    Name:
                  <input type="text"/>
                </label>
                <input type="submit" value="Submit" />
              </form>

            </div>

        );

    }
        
}

ReactDOM.render(
    <RecipeForm />,
    document.getElementById('recipe-form')
);