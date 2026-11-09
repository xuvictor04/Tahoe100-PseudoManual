---
drug: "Docetaxel"
type: "drug"
salt_base: "Docetaxel"
targets: ""
moa_fine: "Microtubule inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 7282
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Docetaxel

*Microtubule inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 7282 / 101 / 134; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.21 / 0.64.
> Flags by dose: low cells (technical?); transcription drop; cell-cycle shift / cell-cycle shift / -. ⚠ 0.05 µM: transcription drop; cell-cycle shift; 0.5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F1 | 5,258 / 2,024 | — | -1.67 | +3.9/+8.6/+4.6 | ⚠ transcription drop; cell-cycle shift · low cells (technical?) |
| 0.5 µM | [[Plate 05]]:F1 | 78 / 23 | — | +0.28 | +2.0/+4.4/+1.1 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 14]]:F1 | 114 / 20 | 0.898 | -0.13 | +0.8/+4.2/+1.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5258 genes, 5,258 with an alert ⚠; the drug-dose carries ⚠ transcription drop; cell-cycle shift; 12 shown): [[TUBB]] ⚠ 2.34× (z +11.1, 46/47 lines; transcription drop; cell-cycle shift (explains ~23% here)), [[CCNB1]] ⚠ 2.43× (z +11.0, 45/47 lines; transcription drop; cell-cycle shift, explains ~67% of this change), [[AURKA]] ⚠ 2.18× (z +10.7, 40/47 lines; transcription drop; cell-cycle shift, explains ~66% of this change), [[VMA21]] ⚠ 1.88× (z +10.6, 37/46 lines; transcription drop; cell-cycle shift (explains ~24% here)), [[KNSTRN]] ⚠ 1.86× (z +10.0, 34/42 lines; transcription drop; cell-cycle shift, explains ~54% of this change), [[PLK1]] ⚠ 2.16× (z +9.9, 34/45 lines; transcription drop; cell-cycle shift, explains ~63% of this change), [[TACC3]] ⚠ 1.76× (z +9.9, 39/47 lines; transcription drop; cell-cycle shift, explains ~77% of this change), [[ARHGAP11A]] ⚠ 1.81× (z +9.6, 40/45 lines; transcription drop; cell-cycle shift, explains ~68% of this change), [[LIN28B]] ⚠ 1.90× (z +9.5, 1/16 lines; transcription drop; cell-cycle shift (explains ~4% here)), [[ITGB6]] ⚠ 1.84× (z +9.5, 1/16 lines; transcription drop; cell-cycle shift (explains ~4% here)), [[TUBA4A]] ⚠ 2.96× (z +9.3, 27/32 lines; transcription drop; position correction uncertain; cell-cycle shift (explains ~20% here)), [[CENPA]] ⚠ 1.50× (z +9.3, 30/45 lines; transcription drop; cell-cycle shift, explains ~50% of this change)

**0.5 µM** (78 genes, 66 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 22 shown): [[TUBA1A]] 2.06× (z +7.5, 36/38 lines; cell-cycle shift (explains ~8% here)), [[TUBB]] 1.74× (z +7.2, 47/48 lines; cell-cycle shift (explains ~18% here)), [[AURKA]] ⚠ 1.54× (z +6.0, 32/48 lines; cell-cycle shift, explains ~60% of this change), [[CCNB1]] ⚠ 1.62× (z +5.9, 32/47 lines; cell-cycle shift, explains ~62% of this change), [[KNSTRN]] ⚠ 1.43× (z +5.8, 22/47 lines; cell-cycle shift, explains ~47% of this change), [[CEP55]] ⚠ 1.45× (z +5.7, 31/46 lines; cell-cycle shift, explains ~53% of this change), [[TUBA4A]] ⚠ 1.94× (z +5.7, 25/35 lines; position correction uncertain; cell-cycle shift (explains ~17% here)), [[TUBB4B]] ⚠ 1.96× (z +5.2, 45/49 lines; cell-cycle shift, explains ~41% of this change), [[HMMR]] ⚠ 1.63× (z +5.1, 33/48 lines; cell-cycle shift, explains ~67% of this change), [[SGO2]] ⚠ 1.37× (z +5.0, 27/48 lines; cell-cycle shift, explains ~75% of this change), [[TACC3]] ⚠ 1.33× (z +5.0, 26/48 lines; cell-cycle shift, explains ~78% of this change), [[CENPE]] ⚠ 1.33× (z +4.9, 30/49 lines; cell-cycle shift, explains ~91% of this change), [[ZDHHC16]] 1.31× (z +4.7, 11/47 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000198211]] 1.49× (z +4.6, 28/46 lines; cell-cycle shift (explains ~12% here)), [[ZNF441]] 1.28× (z +3.4, 8/41 lines; cell-cycle shift (explains ~0% here)), [[TMEM140]] 1.41× (z +3.2, 7/38 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000246090]] 1.32× (z +3.2, 9/46 lines; cell-cycle shift (explains ~7% here)), [[SAMD9]] 1.45× (z +3.1, 25/38 lines; cell-cycle shift (explains ~6% here)), [[TRIM6]] 1.31× (z +2.9, 3/30 lines; cell-cycle shift (explains ~3% here)), [[FKBP5]] 1.22× (z +2.9, 4/42 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000282988]] 1.39× (z +2.9, 7/42 lines; cell-cycle shift (explains ~13% here)), [[NMI]] 1.27× (z +2.9, 11/44 lines; cell-cycle shift (explains ~4% here))

**5 µM** (114 genes, 1 with an alert ⚠; 13 shown): [[TUBA1A]] 2.35× (z +12.6, 37/38 lines), [[TUBB]] 1.80× (z +10.8, 47/47 lines), [[TUBA4A]] ⚠ 2.05× (z +8.7, 32/35 lines; position correction uncertain), [[ENSG00000198211]] 1.59× (z +7.6, 41/46 lines), [[TUBB4B]] 1.96× (z +7.4, 47/48 lines), [[TUBA1B]] 1.85× (z +6.8, 44/47 lines), [[CCNB1]] 1.44× (z +6.4, 36/47 lines), [[PLK1]] 1.37× (z +5.9, 25/48 lines), [[KNSTRN]] 1.28× (z +5.6, 24/48 lines), [[H2BC6]] 1.43× (z +5.3, 13/48 lines), [[TUBA1C]] 1.34× (z +5.2, 33/48 lines), [[H2BC5]] 1.38× (z +5.1, 24/48 lines), [[AURKA]] 1.32× (z +5.1, 25/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2024 genes, 2,024 with an alert ⚠; the drug-dose carries ⚠ transcription drop; cell-cycle shift; 12 shown): [[MT-ND4]] ⚠ 0.185× (z -16.8, 48/48 lines; transcription drop; cell-cycle shift (explains ~0% here)), [[MT-CO2]] ⚠ 0.230× (z -16.7, 47/47 lines; transcription drop; cell-cycle shift (explains ~4% here)), [[MT-CO1]] ⚠ 0.221× (z -16.6, 48/48 lines; transcription drop; cell-cycle shift (explains ~0% here)), [[MT-ND5]] ⚠ 0.186× (z -15.8, 48/48 lines; transcription drop; cell-cycle shift (explains ~0% here)), [[MTATP6P1]] ⚠ 0.0783× (z -15.4, 48/48 lines; transcription drop; cell-cycle shift (explains ~3% here)), [[MT-RNR2]] ⚠ 0.223× (z -13.5, 48/48 lines; transcription drop; cell-cycle shift (explains ~4% here)), [[MT-RNR1]] ⚠ 0.100× (z -13.4, 48/48 lines; transcription drop; cell-cycle shift (explains ~5% here)), [[MT-ATP6]] ⚠ 0.208× (z -13.0, 48/48 lines; transcription drop; cell-cycle shift (explains ~0% here)), [[MT-ND1]] ⚠ 0.199× (z -12.9, 47/48 lines; transcription drop; cell-cycle shift (explains ~0% here)), [[MT-CYB]] ⚠ 0.271× (z -12.9, 48/48 lines; transcription drop; cell-cycle shift (explains ~0% here)), [[ENSG00000271204]] ⚠ 0.480× (z -12.0, 33/40 lines; transcription drop; cell-cycle shift (explains ~8% here)), [[DLG1]] ⚠ 0.661× (z -11.9, 43/48 lines; transcription drop; cell-cycle shift (explains ~5% here))

**0.5 µM** (23 genes, 11 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 19 shown): [[CCDC40]] ⚠ 0.624× (z -5.2, 25/46 lines; position correction uncertain; cell-cycle shift (explains ~14% here)), [[DPY19L2P3]] ⚠ 0.749× (z -4.0, 7/44 lines; cell-cycle shift, explains ~20% of this change), [[ARHGAP8]] ⚠ 0.823× (z -3.8, 2/26 lines; cell-cycle shift, explains ~27% of this change), [[SFI1]] ⚠ 0.830× (z -3.8, 13/48 lines; cell-cycle shift, explains ~47% of this change), [[AGR3]] 0.488× (z -3.8, 6/6 lines; cell-cycle shift (explains ~0% here)), [[NOTCH3]] ⚠ 0.777× (z -3.6, 8/34 lines; cell-cycle shift, explains ~20% of this change), [[KIRREL3]] 0.743× (z -3.5, 6/12 lines; cell-cycle shift (explains ~0% here)), [[CHURC1-FNTB]] ⚠ 0.824× (z -3.5, 6/48 lines; cell-cycle shift, explains ~31% of this change), [[COL4A4]] 0.771× (z -3.4, 3/19 lines; cell-cycle shift (explains ~9% here)), [[ZNF474]] 0.687× (z -3.4, 9/38 lines; cell-cycle shift (explains ~7% here)), [[NHSL1-AS1]] 0.723× (z -3.3, 9/36 lines; cell-cycle shift (explains ~17% here)), [[SCARB1]] ⚠ 0.826× (z -3.3, 12/48 lines; cell-cycle shift, explains ~38% of this change), [[LPCAT4]] 0.812× (z -3.2, 12/47 lines; cell-cycle shift (explains ~0% here)), [[MIR23AHG]] 0.735× (z -3.2, 20/48 lines; cell-cycle shift (explains ~3% here)), [[ENSG00000286016]] 0.780× (z -3.1, 6/18 lines; cell-cycle shift (explains ~6% here)), [[ENSG00000254732]] 0.791× (z -3.1, 8/48 lines; cell-cycle shift (explains ~7% here)), [[EYA2]] 0.804× (z -2.8, 4/14 lines; cell-cycle shift (explains ~0% here)), [[TNFRSF19]] 0.793× (z -2.8, 9/28 lines; cell-cycle shift (explains ~4% here)), [[PLCXD1]] 0.792× (z -2.8, 8/35 lines; cell-cycle shift (explains ~5% here))

**5 µM** (20 genes, 1 with an alert ⚠; 13 shown): [[CCDC40]] ⚠ 0.631× (z -7.2, 30/47 lines; position correction uncertain), [[CHST7]] 0.803× (z -4.4, 11/47 lines), [[ADAMTS2]] 0.793× (z -4.2, 4/18 lines), [[NPIPB12]] 0.757× (z -3.9, 8/43 lines), [[ENSG00000230021]] 0.818× (z -3.7, 18/48 lines), [[GOLT1B]] 0.826× (z -3.7, 26/48 lines), [[USP21]] 0.817× (z -3.7, 13/48 lines), [[ZNF474]] 0.755× (z -3.6, 9/40 lines), [[SEC24D]] 0.803× (z -3.5, 29/48 lines), [[PDXDC2P]] 0.826× (z -3.4, 20/48 lines), [[ENSG00000237550]] 0.739× (z -3.4, 10/48 lines), [[TENM2]] 0.831× (z -3.4, 7/15 lines), [[KIRREL3]] 0.819× (z -3.4, 6/12 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 002]] (+6.1), [[Module 095]] (+5.3), [[Module 022]] (+4.5) | [[Module 200]] (-6.1), [[Module 185]] (-5.8), [[Module 230]] (-5.7) |
| 0.5 µM | [[Module 022]] (+2.2) | — |
| 5 µM | [[Module 032]] (+2.4), [[Module 068]] (+2.3), [[Module 022]] (+2.1) | [[Module 171]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[RPMI-7951 (line)]] (-8.4), [[AsPC-1 (line)]] (-7.6), [[hTERT-HPNE (line)]] (-5.8), [[HOP62 (line)]] (-5.7), [[A-172 (line)]] (-4.6) | [[SW 1271 (line)]] (1.86), [[SW 1088 (line)]] (1.37), [[SW 900 (line)]] (1.33), [[HOP62 (line)]] (1.24) · weakest: [[C-33 A (line)]] (0.369), [[NCI-H1573 (line)]] (0.511), [[SHP-77 (line)]] (0.581) |
| 0.5 µM | [[RKO (line)]] (-4.8) | [[HT-29 (line)]] (1.90), [[NCI-H1792 (line)]] (1.66), [[NCI-H2030 (line)]] (1.60), [[CFPAC-1 (line)]] (1.41) · weakest: [[AsPC-1 (line)]] (0.377), [[A498 (line)]] (0.382), [[A-427 (line)]] (0.473) |
| 5 µM | [[RKO (line)]] (-6.4) | [[NCI-H1792 (line)]] (1.52), [[CFPAC-1 (line)]] (1.31), [[HT-29 (line)]] (1.31), [[HOP62 (line)]] (1.28) · weakest: [[A-427 (line)]] (0.464), [[SNU-1 (line)]] (0.546), [[BT-474 (line)]] (0.558) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: transcription drop; cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[LY-2584702 (tosylate salt) (drug)]] (+0.73, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[XRK3F2 (drug)]] (+0.71, unclear); [[Torkinib (drug)]] (+0.68, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[AZD2858 (drug)]] (+0.64, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Pemigatinib (drug)]] (+0.61, Other TK inhibitor); [[Imiquimod (maleate) (drug)]] (+0.61, unclear); [[Erdafitinib (drug)]] (+0.60, Other TK inhibitor, ⚠ only 6 significant genes); [[Pyridoxine (drug)]] (+0.59, unclear); [[OTS514 (drug)]] (+0.56, Other MAPK inhibitor); [[DT-061 (drug)]] (+0.53, unclear); [[Ferulic acid (drug)]] (+0.53, Other TK inhibitor); [[Canagliflozin (drug)]] (+0.53, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 37 arrows, 37 of them with an alert ⚠; grade A 0, B 25, C 12. Shown: the 15 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[TRIM2]] | 5 µM | B | TRIM2 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express TRIM2 (15) vs lines expressing it (33) | the lines without TRIM2: 0.92× the cells of the other lines | 0.060 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[FUT9]] | 0.05 µM | B | FUT9 activity raises the cells' numbers under Docetaxel 0.05 µM (protects the cells) | lines that do not express FUT9 (40) vs lines expressing it (8) | the lines without FUT9: 0.83× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[ADGRD1]] | 5 µM | B | ADGRD1 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express ADGRD1 (37) vs lines expressing it (11) | the lines without ADGRD1: 0.86× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5 |
| [[TSPAN13]] | 5 µM | B | TSPAN13 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express TSPAN13 (13) vs lines expressing it (35) | the lines without TSPAN13: 0.88× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| [[PRAME]] | 5 µM | B | PRAME activity lowers the cells' numbers under Docetaxel 5 µM (makes them more sensitive) | lines that do not express PRAME (25) vs lines expressing it (23) | the lines without PRAME: 1.08× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[NNT]], [[NNT-AS1]] | 5 µM | B | NNT, NNT-AS1 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express NNT, NNT-AS1 (6) vs lines expressing them (42) | the lines without NNT, NNT-AS1: 0.85× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-absent genes |
| [[ZNF608]] | 5 µM | B | ZNF608 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express ZNF608 (12) vs lines expressing it (36) | the lines without ZNF608: 0.87× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |
| [[VENTXP1]] | 0.5 µM | B | VENTXP1 activity raises the cells' numbers under Docetaxel 0.5 µM (protects the cells) | lines that do not express VENTXP1 (12) vs lines expressing it (36) | the lines without VENTXP1: 0.87× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |
| [[RASSF5]] | 5 µM | B | RASSF5 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express RASSF5 (5) vs lines expressing it (43) | the lines without RASSF5: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[FAAH2]] | 5 µM | B | FAAH2 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.90× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[SLC19A3]] | 0.5 µM | B | SLC19A3 activity lowers the cells' numbers under Docetaxel 0.5 µM (makes them more sensitive) | lines that do not express SLC19A3 (36) vs lines expressing it (12) | the lines without SLC19A3: 1.16× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, MTND1P23, LINC00824 |
| [[HRH1]] | 0.05 µM | B | HRH1 activity lowers the cells' numbers under Docetaxel 0.05 µM (makes them more sensitive) | lines that do not express HRH1 (10) vs lines expressing it (38) | the lines without HRH1: 1.75× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[DUSP10]] | 0.05 µM | B | DUSP10 activity lowers the cells' numbers under Docetaxel 0.05 µM (makes them more sensitive) | lines that do not express DUSP10 (11) vs lines expressing it (37) | the lines without DUSP10: 1.58× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[ENSG00000286385]] | 0.05 µM | B | ENSG00000286385 activity raises the cells' numbers under Docetaxel 0.05 µM (protects the cells) | lines that do not express ENSG00000286385 (35) vs lines expressing it (13) | the lines without ENSG00000286385: 0.93× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01205, MGAT4C, MAGEB2 |
| [[FBXW10B]] | 0.05 µM | B | FBXW10B activity lowers the cells' numbers under Docetaxel 0.05 µM (makes them more sensitive) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 1.31× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[SGSH]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity raises SGSH's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[MZT1]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity lowers MZT1's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[ENSG00000287352]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity lowers ENSG00000287352's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[RAB28]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity raises RAB28's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Data

- `tables/drugs.parquet` — drug == "Docetaxel"
- `tables/drugdoses.parquet` — dd in 368, 369, 370
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
