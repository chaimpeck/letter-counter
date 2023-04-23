const App = () => {
  const [distResult, setDistResult] = React.useState();
  const wordsTextAreaRef = React.useRef();
  const handleSubmit = (e) => {
    if (wordsTextAreaRef.current) {
      fetch("/get-letter-dist", {
        method: "POST",
        body: wordsTextAreaRef.current.value,
      })
        .then((r) => r.json())
        .then((res) => setDistResult(res));
    }
  };

  return (
    <div class="container-fluid">
      <div class="row">
        <div class="col">
          <h2>Enter Words</h2>
          <p>
            <label for="words">Enter list of words:</label>
          </p>
          <textarea
            ref={wordsTextAreaRef}
            name="words"
            rows="20"
            cols="50"
          ></textarea>
          <br />
          <input type="submit" value="Submit" onClick={handleSubmit} />
        </div>
        <div class="col">
          {distResult ? (
            <div>
              <h2>Letters</h2>
              <figure class="figure">
                <img
                  src={`data:image/png;base64,${distResult.plot}`}
                  class="figure-img img-fluid rounded"
                  alt="..."
                />
                <figcaption class="figure-caption">
                  % Distribution of letters
                </figcaption>
              </figure>
              <h3>Actual Counts:</h3>
              <pre>
                {Object.keys(distResult.letter_counts).map((letter) => {
                  return `${letter}: ${distResult.letter_counts[letter]}\n`;
                })}
              </pre>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
};

ReactDOM.render(<App />, document.querySelector("#root"));
