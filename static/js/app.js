function App() {
    const { Container, Row, Col } = ReactBootstrap;

    return (
        <Container>
        <div className="window mt-5">
          <div className="flex">
          </div>
          <div style={{"overflow-y": "scroll", "height": "500px"}} className="text_container">
            <ListCommands />
          </div>
        </div>
        </Container>
    );
}

function ListCommands() {
    const [data, setData] = React.useState(null);
    const messagesEndRef = React.useRef(null);

    const scrollToBottom = () => {
      messagesEndRef.current.scrollIntoView();
    }

    React.useEffect(() => {
      const interval = setInterval(() => {
        fetch('/commands')
            .then(r => r.json())
            .then(setData)
            .then(scrollToBottom());
      }, 1000);
      return () => clearInterval(interval);
    }, []);

    if (data === null) return 'Loading...';

    const commands = data.commands

    return (
        <React.Fragment>
            {commands.length === 0 && (
                <p className="mb-0">$ </p>
            )}
            {commands.map(command => (
                <p className="mb-0">{command}</p>
            ))}
            <div ref={messagesEndRef} />
        </React.Fragment>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
