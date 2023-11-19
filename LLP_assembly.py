import machine

@micropython.asm_thumb
def led_blink():
    ldr(r0, ptr16[0x50202000])  # Load the base address of GPIO
    ldr(r1, [r0, 0x04])        # Load the address of GPIO output set register
    mov(r2, 0x01)              # Set bit 0 (GPIO 0) to 1
    str(r2, [r1, 0])           # Store the value to the output set register
    label(loop)
    mov(r3, 1000000)           # Delay for 1 second (approximately)
    label(delay)
    sub(r3, 1)
    cmp(r3, 0)
    bne(delay)
    mov(r2, 0x00)              # Set bit 0 (GPIO 0) to 0
    str(r2, [r1, 0])           # Store the value to the output set register
    b(loop)

led_blink()
