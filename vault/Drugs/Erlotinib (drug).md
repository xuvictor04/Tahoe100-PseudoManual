---
drug: "Erlotinib"
type: "drug"
salt_base: "Erlotinib"
targets: "EGFR"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 186
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Erlotinib

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 186 / 4 / 108; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.19 / 0.15.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C4 | 35 / 151 | — | +0.66 | -0.8/-0.9/-0.7 | — |
| 0.5 µM | [[Plate 08]]:C4 | 0 / 4 | — | +0.52 | -0.1/+0.4/+1.0 | — |
| 5 µM | [[Plate 09]]:C4 | 57 / 51 | — | -0.21 | -2.1/-0.9/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (35 genes, none with an alert; 12 shown): [[CUL2]] 1.22× (z +3.7, 13/48 lines), [[TNKS2]] 1.23× (z +3.7, 29/48 lines), [[NAXD]] 1.37× (z +3.5, 18/46 lines), [[LIN7C]] 1.36× (z +3.5, 30/48 lines), [[ZNF84]] 1.21× (z +3.5, 9/47 lines), [[MTERF3]] 1.25× (z +3.5, 3/47 lines), [[SMG1P3]] 1.50× (z +3.4, 10/45 lines), [[RPP30]] 1.24× (z +3.3, 7/47 lines), [[ZNF256]] 1.44× (z +3.2, 2/31 lines), [[PEX5]] 1.23× (z +3.2, 4/47 lines), [[USP9X]] 1.21× (z +3.2, 25/48 lines), [[CAPRIN1]] 1.24× (z +3.2, 26/48 lines)

**5 µM** (57 genes, none with an alert; 12 shown): [[PSAT1]] 1.43× (z +4.4, 17/39 lines), [[ADM2]] 1.59× (z +4.1, 8/31 lines), [[FAM219B]] 1.32× (z +4.0, 10/47 lines), [[ZSCAN25]] 1.32× (z +3.9, 14/47 lines), [[VAMP3]] 1.22× (z +3.9, 17/47 lines), [[AHNAK]] 1.36× (z +3.9, 39/45 lines), [[SLC35F6]] 1.46× (z +3.8, 13/47 lines), [[LAMP3]] 1.40× (z +3.8, 6/27 lines), [[ALDH1L2]] 1.34× (z +3.8, 6/24 lines), [[BEST1]] 1.49× (z +3.8, 16/44 lines), [[SLC1A5]] 1.24× (z +3.7, 16/46 lines), [[ZNF318]] 1.24× (z +3.7, 15/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (151 genes, none with an alert; 12 shown): [[UTY]] 0.711× (z -5.4, 0/17 lines), [[CCND2]] 0.632× (z -5.1, 0/11 lines), [[SLCO1B3]] 0.755× (z -4.7, 1/20 lines), [[MIR4307HG]] 0.521× (z -4.2, 2/13 lines), [[VSTM4]] 0.579× (z -4.2, 1/17 lines), [[PCSK1]] 0.556× (z -4.1, 0/6 lines), [[PXN-AS1]] 0.668× (z -4.1, 6/45 lines), [[CST6]] 0.391× (z -4.1, 0/6 lines), [[RASGEF1A]] 0.612× (z -4.0, 2/19 lines), [[LINC02327]] 0.588× (z -4.0, 0/5 lines), [[COX7B2]] 0.536× (z -4.0, 0/5 lines), [[BARX1]] 0.456× (z -3.9, 5/16 lines)

**0.5 µM** (4 genes, none with an alert): [[VILL]] 0.690× (z -3.4, 6/29 lines), [[FAM124A]] 0.745× (z -3.3, 3/32 lines), [[LINC00941]] 0.748× (z -3.0, 6/38 lines), [[TMEM92-AS1]] 0.742× (z -2.8, 3/31 lines)

**5 µM** (51 genes, none with an alert; 12 shown): [[ATP2A1]] 0.642× (z -5.4, 21/44 lines), [[ENSG00000254732]] 0.692× (z -4.7, 19/47 lines), [[LAG3]] 0.541× (z -4.5, 11/27 lines), [[ENSG00000255639]] 0.641× (z -4.5, 18/43 lines), [[CACNA1B]] 0.682× (z -4.4, 10/28 lines), [[LINC02968]] 0.681× (z -4.2, 4/19 lines), [[WDR62]] 0.743× (z -4.2, 16/45 lines), [[GSK3B-DT]] 0.705× (z -3.9, 20/45 lines), [[SYCE1L]] 0.672× (z -3.8, 14/40 lines), [[ADORA1]] 0.643× (z -3.8, 14/33 lines), [[ZSWIM4]] 0.803× (z -3.8, 14/47 lines), [[TMEM217]] 0.648× (z -3.7, 16/42 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 025]] (+3.0), [[Module 020]] (+2.7), [[Module 029]] (+2.6) | [[Module 048]] (-2.6), [[Module 024]] (-2.2), [[Module 002]] (-2.1) |
| 0.5 µM | — | — |
| 5 µM | [[Module 025]] (+2.1) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[CHP-212 (line)]] (1.35), [[AN3 CA (line)]] (1.30), [[SW 1271 (line)]] (1.27), [[LOX-IMVI (line)]] (1.21) · weakest: [[NCI-H2347 (line)]] (0.743), [[SW 1088 (line)]] (0.759), [[SHP-77 (line)]] (0.806) |
| 0.5 µM | — | — |
| 5 µM | [[NCI-H2030 (line)]] (-3.2), [[Hs 766T (line)]] (-3.1) | [[BT-474 (line)]] (1.48), [[A-427 (line)]] (1.33), [[RPMI-7951 (line)]] (1.32), [[COLO 205 (line)]] (1.31) · weakest: [[MIA PaCa-2 (line)]] (0.600), [[SW 1271 (line)]] (0.602), [[SW1417 (line)]] (0.631) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Fenofibrate (drug)]] (+0.95, unclear); [[Benproperine (phosphate) (drug)]] (+0.92, unclear); [[Lucanthone (drug)]] (+0.86, unclear); [[Anethole trithione (drug)]] (+0.80, unclear); [[Tucatinib (drug)]] (+0.79, EGFR/ERBB inhibitor); [[MK-8353 (drug)]] (+0.78, Other MAPK inhibitor); [[Paclitaxel (drug)]] (+0.76, Microtubule inhibitor, ⚠ only 3 significant genes); [[Rutin (trihydrate) (drug)]] (+0.75, unclear); [[Encorafenib (drug)]] (+0.74, RAF inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 15 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PIP5K1B]] | 0.05 µM | B | PIP5K1B activity raises the cells' numbers under Erlotinib 0.05 µM (protects the cells) | lines that do not express PIP5K1B (33) vs lines expressing it (15) | the lines without PIP5K1B: 0.79× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[FMNL1-DT]] | 0.05 µM | B | FMNL1-DT activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express FMNL1-DT (23) vs lines expressing it (25) | the lines without FMNL1-DT: 1.25× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[C2orf74]] | 0.05 µM | C | C2orf74 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.27× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[FIGN]] | 0.05 µM | C | FIGN activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.23× the cells of the other lines | 0.011 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[NR3C1]] | 0.05 µM | C | NR3C1 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.28× the cells of the other lines | 0.013 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[SPART-AS1]] | 0.05 µM | C | SPART-AS1 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.22× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[SIX1]] | 0.05 µM | C | SIX1 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.26× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| [[ENSG00000286964]] | 0.05 µM | C | ENSG00000286964 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.26× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[LIFR]] | 0.05 µM | C | LIFR activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.24× the cells of the other lines | 0.029 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| [[ENSG00000214265]], [[SNHG14]], [[SNRPN]] | 0.05 µM | C | ENSG00000214265, SNHG14, SNRPN activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.24× the cells of the other lines | 0.029 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| [[TBC1D9]] | 0.05 µM | C | TBC1D9 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express TBC1D9 (6) vs lines expressing it (42) | the lines without TBC1D9: 1.32× the cells of the other lines | 0.042 | ⚠ tissue-confounded; across organs; also absent: SIX1, TRPC1, MTERF1 |
| [[ZNF772]] | 0.05 µM | C | ZNF772 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express ZNF772 (11) vs lines expressing it (36) | the lines without ZNF772: 1.23× the cells of the other lines | 0.047 | ⚠ tissue-confounded; across organs; co-occurs with APC, TGFBR2; also absent: ENSG00000268163, SNRPN, DNAAF9 |
| [[RNF150]] | 0.05 µM | C | RNF150 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express RNF150 (16) vs lines expressing it (32) | the lines without RNF150: 1.20× the cells of the other lines | 0.057 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SNRPN, BVES, MPDZ |
| [[ENSG00000268163]] | 0.05 µM | C | ENSG00000268163 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000268163 (12) vs lines expressing it (36) | the lines without ENSG00000268163: 1.23× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: ZNF772, SNRPN, DNAAF9; maybe low, not absent |
| [[SLC36A4]] | 0.05 µM | C | SLC36A4 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express SLC36A4 (5) vs lines expressing it (43) | the lines without SLC36A4: 1.31× the cells of the other lines | 0.070 | ⚠ tissue-confounded; across organs; co-occurs with CTNNB1; also absent: KLHL5, FBXL2, SIX4 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Erlotinib"
- `tables/drugdoses.parquet` — dd in 423, 424, 425
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
