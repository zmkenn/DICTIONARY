DATA = {
    "ALGORITHM": "A step-by-step procedure for solving a problem.",
    "BIOS": "A program used by a computer's microprocessor to start the system after power-on.",
    "BYTE": "A data unit consisting of eight bits.",
    "CACHE": "A fast storage area for frequently accessed data.",
    "CLOCK SPEED": "The rate at which a CPU executes instructions, measured in cycles per second.",
    "CAPACITOR": "A component that stores and releases electrical energy.",
    "COMPILER": "A tool that converts high-level programming code into machine code.",
    "DATABASE": "An organized collection of data stored electronically.",
    "DEBUGGING": "The process of identifying and resolving errors in software or hardware.",
    "DIODE": "A component that allows current to flow in only one direction.",
    "DIGITAL LOGIC": "The foundation of digital circuits, based on logic gates.",
    "ETHERNET": "A wired communication technology for networking devices.",
    "FAN": "A cooling device that prevents overheating in computers.",
    "FIRMWARE": "Software embedded in hardware to control its functions.",
    "HEATSINK": "A device that dissipates heat from computer components.",
    "KERNEL": "The core of an operating system, managing hardware and processes.",
    "LATENCY": "The delay between an input and its response in a system.",
    "LOGIC GATE": "A basic building block of digital circuits, used for logical operations.",
    "MACHINE LEARNING": "A field of AI that enables systems to learn from data.",
    "MOTHERBOARD": "The main circuit board that connects all computer components.",
    "MULTITHREADING": "A technique that allows a program to run multiple tasks concurrently.",
    "NETWORK PROTOCOL": "Rules that define data transmission over a network.",
    "OVERCLOCKING": "Increasing a CPU’s speed beyond factory settings for better performance.",
    "PARALLEL COMPUTING": "A computing method where multiple processors work on tasks simultaneously.",
    "PIPELINING": "A technique where multiple instructions are processed in stages for efficiency.",
    "SATA": "An interface for connecting storage devices like SSDs and HDDs.",
    "SEMAPHORE": "A programming tool for managing concurrent processes safely.",
    "THREAD": "A sequence of instructions that a CPU executes independently.",
    "TRANSCEIVER": "A device that can both send and receive data signals.",
    "VIRTUALIZATION": "A technology that allows multiple virtual systems to run on a single physical machine."
}

while True:
    a = input("Enter a term: ")
    print(DATA.get(a, "Word not found."))