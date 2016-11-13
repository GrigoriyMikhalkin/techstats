import React from 'react'
import ReactDOM from 'react-dom'

var CommentBox = React.createClass({
    getInitialState: function() {

    }
    render: function() {
	return (
	    <div className="commentBox">
		Hello, World
	    </div>
	);
    }
});

ReactDOM.render(
    <CommentBox />,
    document.getElementById("content")
);
