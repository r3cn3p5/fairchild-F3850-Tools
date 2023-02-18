

opcodes = [

    # Accumulator Group
    ('SR',   0x12, 0, 1, '', 'SHIFT RIGHT ONE'),
    ('SR',   0x14, 0, 1, '', 'SHIFT RIGHT FOUR'),
    ('SL',   0x13, 0, 1, '', 'SHIFT LEFT ONE'),
    ('SL',   0x15, 0, 1, '', 'SHIFT LEFT FOUR'),

    ('COM',  0x18, 0, 1, '', 'ACC(ACC) \u2295'),
    ('LNK',  0x19, 0, 1, '', 'ACC<-(ACC)+CB'),
    ('INC',  0x1F, 0, 1, '', 'ACC<-(ACC)+1'),
    ('LIS',  0x70, 4, 1, '0x{0:01X}', 'ACC<-H\'i\''),
    ('CLR',  0x70, 0, 1, '', 'ACC<-H\'00\''),

    ('LI',   0x20, 0, 2, '0x{0:02X}', 'ACC<-H\'ii\''),
    ('NI',   0x21, 0, 2, '0x{0:02X}', 'ACC<-(ACC)^H\'ii\''),
    ('OI',   0x22, 0, 2, '0x{0:02X}', 'ACC<-(ACC)vH\'ii\''),
    ('XI',   0x23, 0, 2, '0x{0:02X}', 'ACC<-(ACC)\u2295H\'ii\''),
    ('AI',   0x24, 0, 2, '0x{0:02X}', 'ACC<-(ACC)+H\'ii\''),
    ('CI',   0x25, 0, 2, '0x{0:02X}', 'H\'ii\'<-(ACC)+1'),

    # Scratchpad Registers
    ('LR',   0x40, 4, 1, '0x{0:01X}', 'ACC<-(r)'),
    ('LR',   0x00, 0, 1, 'A,KU', 'ACC<-(r12)'),
    ('LR',   0x01, 0, 1, 'A,KL', 'ACC<-(r13)'),
    ('LR',   0x02, 0, 1, 'A,QU', 'ACC<-(r14)'),
    ('LR',   0x03, 0, 1, 'A,QL', 'ACC<-(r15)'),

    ('LR',   0x50, 4, 1, '0x{0:01X},A', 'r<(ACC)'),
    ('LR',   0x04, 0, 1, 'KU,A', 'r12<-(ACC)'),
    ('LR',   0x05, 0, 1, 'KL,A', 'r13<-(ACC)'),
    ('LR',   0x06, 0, 1, 'QU,A', 'r14<-(ACC)'),
    ('LR',   0x07, 0, 1, 'QL,A', 'r15<-(ACC)'),

    ('AS',   0xC0, 4, 1, '0x{0:01X}', 'ACC<-(ACC)+(r)(Binary)'),
    ('ASD',  0xD0, 4, 1, '0x{0:01X}', 'ACC<-(ACC)+(r)(Decimal)'),
    ('NS',   0xF0, 4, 1, '0x{0:01X}', 'ACC<-(ACC)^(r)'),
    ('XS',   0xE0, 4, 1, '0x{0:01X}', 'ACC<-(ACC)\u2295(r)'),
    ('DS',   0x30, 4, 1, '0x{0:01X}', 'r<-(r)+H\'FF\'(Decrement)'),

    # Data Counter
    ('LR',   0x0E, 0, 1, '', 'r14<-(DCU); r15<-(DCL)'),
    ('LR',   0x11, 0, 1, '', 'r10<-(DCU); r11<-(DCL)'),
    ('LR',   0x0F, 0, 1, '', '(DCU)<-r14; (DCL)<-r15'),
    ('LR',   0x10, 0, 1, '', '(DCU)<-r10; (DCL)<-r11'),
    ('DCI',  0x2A, 0, 3, '0x{0:04X}', 'DC<-H\'iiii\''),
    ('XDC',  0x2C, 0, 1, '', 'DC <-> DC1'),

    # Indirect Scratchpad
    ('LR',   0x0A, 0, 1, 'A,IS', 'ACC<-(ISAR)'),
    ('LR',   0x0B, 0, 1, 'IS,A', 'ISAR<-(ACC)'),
    ('LISU', 0x60, 3, 1, '0x{0:01X}', 'ISARU<-a'),
    ('LISL', 0x68, 3, 1, '0x{0:01X}', 'ISARL<-a'),

    # Memory Reference
    ('LM',   0x16, 0, 1, '', 'ACC<-((DC))'),
    ('ST',   0x17, 0, 1, '', '(DC)<-(ACC)'),
    ('AM',   0x88, 0, 1, '', 'ACC<-(ACC)+((DC))(Binary)'),
    ('AMD',  0x89, 0, 1, '', 'ACC<-(ACC)+((DC))(Decimal)'),
    ('NM',   0x8A, 0, 1, '', 'ACC<-(ACC)^((DC))'),
    ('OM',   0x8B, 0, 1, '', 'ACC<-(ACC)v((DC))'),
    ('XM',   0x8C, 0, 1, '', 'ACC<-(ACC)\u2295((DC))'),
    ('CM',   0x8D, 0, 1, '', '((DC)+(line above ACC)+1)'),

    # Status Register
    ('LR',   0x1D, 0, 1, 'W,J', 'W<-(r9)'),
    ('LR',   0x1E, 0, 1, 'J,W', 'r9<-(W)'),

    # Miscellaneous
    ('NOP',  0x1B, 0, 1, '', 'NO OPERATION'),

    # Program Counter
    ('LR',   0x08, 0, 1, 'K,P', 'r12<-(PC1U); r13<-(PC1L)'),
    ('LR',   0x09, 0, 1, 'P,K', 'PC1U<-(r12); PC1L<-(r13)'),
    ('LR',   0x0D, 0, 1, 'P0,Q', 'PC0U<-(r14); PC0L<-(r15)'),
    ('PK',   0x0C, 0, 1, '', 'PC0U<-(r12); PC0L<-(r13) and PC1<-(PC0) - Privileged Instruction'),
    ('PI',   0x28, 0, 3, '0x{0:04X}', 'PC1<-(PC0); PC0\'aaaa\' - Privileged Instruction'),
    ('POP',  0x1C, 0, 1, '', 'PC0<-(PC1); Privileged Instruction'),

    # Branch
    ('BR',   0x90, 0, 2, '0x{0:02X}', 'PC0<-((PC0)+1)+H\'aa\''),
    ('JMP',  0x29, 0, 3, '0x{0:04X}', 'PC0<-h\'aaaa\''),
    ('BT',   0x88, 3, 2, '0x{0:01X},0x{1:02X}', 'PC0<-(PC0)+H\'aa\'; if any test true - PC0<-(PC0)+2; if no test is true'),
    ('BP',   0x81, 0, 2, '0x{0:02X}', 'PC0<-((PC0)+1)+H\'aa\'; if SIGN=1 - PC0<-((PC0)+2); if SIGN=0'),
    ('BC',   0x82, 0, 2, '0x{0:02X}', 'PC0<-((PC0)+1)+H\'aa\'; if CARRY=1 - PC0<-((PC0)+2); if CARRY=0'),
    ('BZ',   0x84, 0, 2, '0x{0:02X}', 'PC0<-((PC0)+1)+H\'aa\'; if ZERO=1 - PC0<-((PC0)+2); if ZERO=0'),
    ('BM',   0x91, 0, 2, '0x{0:02X}', 'PC0<-((PC0)+1)+H\'aa\'; if SIGN=0 - PC0<-((PC0)+2); if SIGN=1'),
    ('BNC',  0x92, 0, 2, '0x{0:02X}', 'PC0<-((PC0)+1)+H\'aa\'; if CARRY=0 - PC0<-((PC0)+2); if CARRY=1'),
    ('BNZ',  0x94, 0, 2, '0x{0:02X}', 'PC0<-((PCO)+1)+H\'aa\'; if ZERO=0 - PC0<-((PCO)+2); if ZERO=1'),
    ('BF',   0x90, 4, 2, '0x{0:01X},0x{0:02X}', 'PCO<-((PC0)+1)+H\'aa\' - PC0<-(PC0)+2 if any status bit is 1'),
    ('BNO',  0x98, 0, 2, '0x{0:02X}', 'PC0<-((PC0)+1)+H\'aa\'; if OVF=0 - PC0<-(PC0)+2; if OVF=1'),
    ('BRZ',  0x8F, 0, 2, '0x{0:02X}', 'PC0<-((PC0)+1)+H\'aa\'; if ISAR!=7 - PC0<-(PC0)+2; if ISAR=7'),

    # Interrupt Control
    ('DI',   0x1A, 0, 1, '', 'DISABLE INTERRUPT'),
    ('EI',   0x1B, 0, 1, '', 'ENABLE INTERRUPT - Privileged Instruction'),

    # Input/Output
    ('INS',  0xA0, 4, 1, '0x{0:01X}', 'ACC<-(INPUT PORT a); Input Ports 00 to 0F only'),
    ('IN',   0x26, 0, 2, '0x{0:02X}', 'ACC<-(INPUT PORT a); Input Ports 04 through FF only'),
    ('OUTS', 0xB0, 4, 1, '0x{0:01X}', 'OUTPUT PORT a<-(ACC); Output ports 00 to 0F only'),
    ('OUT',  0x27, 0, 2, '0x{0:02X}', 'OUTPUT PORT aa<-(ACC); Output ports 04 through FF only')


]