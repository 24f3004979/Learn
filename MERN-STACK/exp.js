// Async functionality of JS
function delay(seconds) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Timed dataset fetch information string");
    }, seconds * 1000);
  });
}

async function main() {
  let elapsed = 0;
  let finished = false; // Initialization
  let result = null;

  console.log("Async opreation starting");

  delay(4).then((output) => {
    result = output;
    finished = true;
  });
  const counterInterval = setInterval(() => {
    elapsed++;
    console.log(`Elapsed time : ${elapsed}`);

    if (finished) {
      console.log("Task finished");
      console.log(result);

      clearInterval(counterInterval);
    }
  }, 1000);
}

main();
