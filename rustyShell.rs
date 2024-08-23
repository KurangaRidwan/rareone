use std::io::{stdin, stdout, Write};
use std::process::{Command, Stdio};

fn read_command() -> String {
    let mut input = String::new();
    stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().to_string()
}

fn main() {
    println!("Welcome to the Rust shell!");

    loop {
        print!(">> ");
        stdout().flush().unwrap();

        let command = read_command();
        if command.is_empty() {
            continue;
        }

        let mut args = command.split_whitespace().collect::<Vec<_>>();
        let program = args.remove(0);

        let output = Command::new(program)
            .args(args)
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit())
            .spawn()
            .unwrap()
            .wait_with_output()
            .unwrap();

        println!("Exit status: {}", output.status.code().unwrap_or(-1));
    }
}