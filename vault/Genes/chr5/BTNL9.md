---
symbol: "BTNL9"
type: "gene"
col: 9192
ensembl_id: "ENSG00000165810"
name: "butyrophilin like 9"
location: "5q35.3"
module: 176
arm: "+"
pooled_cpm: 6.45
n_lines_expressing: 26
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 13
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# BTNL9

*butyrophilin like 9* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.02× (z +16.1, q 0e+00, up in 22 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.537× (z -9.1, q 4e-17, down in 21 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCOLN2]] (+0.60, fdr 1e-05), [[KBTBD11]] (+0.57, fdr 2e-05), [[CACNA1D]] (+0.56, fdr 1e-05); moves opposite to [[PPP1R7]] (-0.53, fdr 3e-05), [[RBM42]] (-0.51, fdr 3e-05), [[MORN2]] (-0.49, fdr 1e-04).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[C2orf72]] → it (grade B ⚠); 13 go from it, the strongest it → [[KBTBD11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.02×** | +16.1 | 0e+00 | 22/24 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.86×** | +11.0 | 9e-26 | 7/13 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.48×** | +9.5 | 3e-19 | 17/23 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +8.4 | 5e-15 | 1/4 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +8.1 | 4e-14 | 13/22 (NCI-H460, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +6.6 | 3e-09 | 3/7 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.8 | 1e-04 | 7/16 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.4 | 8e-04 | 0/17 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +3.7 | 0.011 | 9/24 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.5 | 0.031 | 6/22 (HT-29, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +3.1 | 0.093 | 1/22 (AsPC-1) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.34× | +3.1 | 0.11 | 2/23 (NCI-H460, SW 900) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.50× | +3.0 | 0.11 | 1/17 (KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.537×** | -9.1 | 4e-17 | 21/22 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.554×** | -6.0 | 6e-07 | 16/23 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -5.8 | 1e-06 | 17/22 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.412×** | -4.9 | 2e-04 | 12/21 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -4.1 | 0.004 | 13/23 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -3.7 | 0.018 | 17/23 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.721×** | -3.5 | 0.044 | 15/24 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.724×** | -3.4 | 0.045 | 11/24 (A498, A549, …) | top dose only |  |
| [[Pimozide (drug)]] 5 µM |  | 0.751× | -3.0 | 0.15 | 2/24 (AsPC-1, A549) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.2 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0811× (z -32.0) |
| [[HT-29 (line)]] | alt | 36.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -20.7) |
| [[LoVo (line)]] | wt | 19.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -12.3) |
| [[A-427 (line)]] | wt | 29.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0589× (z -10.8) |
| [[A549 (line)]] | wt | 4.62 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0269× (z -13.5) |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -9.4) |
| [[KATO III (line)]] | alt | 8.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 9.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -10.8) |
| [[SNU-1 (line)]] | wt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -9.8) |
| [[A-172 (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.974 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCOLN2]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[KBTBD11]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CACNA1D]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[CGREF1]] | +0.53 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MEGF11]] | +0.53 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RNF157]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ASIC1]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[OTUD7A]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MED12L]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SYN2]] | +0.52 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TTPA]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R7]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[RBM42]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MORN2]] | -0.49 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[MTFR1L]] | -0.48 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[DNAL4]] | -0.47 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[GPATCH1]] | -0.47 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ZZEF1]] | -0.46 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[OSCP1]] | -0.46 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[MPV17]] | -0.45 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[BBOF1]] | -0.44 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[SPAG16]] | -0.44 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[SYNRG]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf72]] | B | C2orf72 activity raises BTNL9's level | lines that do not express C2orf72 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without C2orf72 | 0.087 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CMBL, TPPP |
| [[GRID1]] | B | GRID1 activity raises BTNL9's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.41× lower at baseline in the lines without GRID1 | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[NR5A2]] | C | NR5A2 activity raises BTNL9's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 2.18× lower at baseline in the lines without NR5A2 | 0.014 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; co-absent with the target |
| [[CPNE7]] | C | CPNE7 activity raises BTNL9's level | lines that do not express CPNE7 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without CPNE7 | 0.095 | ⚠ within organs, on part of the lines; also absent: BTNL9, HSBP1L1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KBTBD11]] | B | BTNL9 activity raises KBTBD11's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without BTNL9 | 0.007 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[PRKCQ]] | B | BTNL9 activity raises PRKCQ's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without BTNL9 | 0.014 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[WNK2]] | B | BTNL9 activity raises WNK2's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.63× lower at baseline in the lines without BTNL9 | 0.036 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[KNDC1]] | B | BTNL9 activity raises KNDC1's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without BTNL9 | 0.038 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[RAP1GAP2]] | B | BTNL9 activity raises RAP1GAP2's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.11× lower at baseline in the lines without BTNL9 | 0.046 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[GNAL]] | B | BTNL9 activity raises GNAL's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.18× lower at baseline in the lines without BTNL9 | 0.047 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[UCK2]] | B | BTNL9 activity raises UCK2's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 1.52× lower at baseline in the lines without BTNL9 | 0.059 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[DNAL4]] | B | BTNL9 activity lowers DNAL4's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 1.16× higher at baseline in the lines without BTNL9 | 0.063 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[MLXIPL]] | B | BTNL9 activity raises MLXIPL's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without BTNL9 | 0.081 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[C2orf72]] | B | BTNL9 activity raises C2orf72's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 1.56× lower at baseline in the lines without BTNL9 | 0.095 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[CRACD]] | B | BTNL9 activity raises CRACD's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.31× lower at baseline in the lines without BTNL9 | 0.099 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[CPNE7]] | C | BTNL9 activity raises CPNE7's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without BTNL9 | 0.019 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B; co-absent with the target |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.9, 42.0); signed map (30.1, 26.8). **Vector** length 54.6, 12.2% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +16.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.9 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +0.9 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -1.7 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -0.9 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | butyrophilin like 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:181,040,225-181,061,521 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32535, BTN8 |
| Gene groups (HGNC) | Butyrophilins; V-set domain containing |
| Reactome | 2 pathways, smallest: Butyrophilin (BTN) family interactions; Adaptive Immune System |
| Matched by | ensembl_id |

UniProt [Q6UXG8](https://www.uniprot.org/uniprotkb/Q6UXG8) carries no function annotation.

**Summary**, from NCBI Gene [153579](https://www.ncbi.nlm.nih.gov/gene/153579):

> Predicted to enable signaling receptor binding activity. Predicted to be involved in T cell receptor signaling pathway and regulation of cytokine production. Predicted to be located in plasma membrane. Predicted to be active in external side of plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24176) · Entrez [153579](https://www.ncbi.nlm.nih.gov/gene/153579) · UniProt [Q6UXG8](https://www.uniprot.org/uniprotkb/Q6UXG8) · Ensembl [ENSG00000165810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165810)

## Data

Gene col 9192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9192); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9192]; `tensor/DDL_lfc|DDL_z.npy` [9192]; `embed/gene_vectors.npy` [9192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9192 or target_col == 9192). Every well: [[BTNL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTNL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
