    .org $8000

    lda #$ff
    sta $6000

    .org $fffc
    .word $8000
    .word $0000