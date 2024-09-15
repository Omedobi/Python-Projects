---

# Internet Speed Test Script

This Python script tests the internet connection speed (download speed, upload speed, and ping) using the `speedtest-cli` library. The results are displayed in megabits per second (Mbps) for download and upload speeds, and in milliseconds (ms) for ping.

## Requirements

Before running the script, you need to install the `speedtest-cli` library.

### Installation

To install the necessary package, run the following command:

```bash
pip install speedtest-cli
```

## Usage

1. Clone this repository or download the script.

2. Install the required package (`speedtest-cli`), as mentioned above.

3. Run the Python script:

   ```bash
   python <script_name>.py
   ```

   The script will perform the following:
   - Measure the **download speed** in Mbps.
   - Measure the **upload speed** in Mbps.
   - Measure the **ping** (latency) in milliseconds.


## How it Works

- The script creates an instance of the `Speedtest` class from the `speedtest-cli` library.
- The download speed is measured in bits per second, then converted to Mbps.
- The upload speed is also measured in bits per second, then converted to Mbps.
- The ping is measured in milliseconds to assess the latency of your connection.

## Notes

- Ensure that you are connected to the internet.
- The speedtest will use some amount of your internet data to perform the test, so make sure you have sufficient data available if on a metered connection.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
