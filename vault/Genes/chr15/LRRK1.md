---
symbol: "LRRK1"
type: "gene"
col: 7787
ensembl_id: "ENSG00000154237"
name: "leucine rich repeat kinase 1"
location: "15q26.3"
module: 5
arm: "+"
pooled_cpm: 46.25
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# LRRK1

*leucine rich repeat kinase 1* — 15q26.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 3.33×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Furosemide (drug)]] 5 µM in 1 line (LS 180 2.15×).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.174× (z -25.8, q 0e+00, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMCO4]] (+0.73, fdr 7e-06), [[ALDH1A3-AS1]] (+0.67, fdr 1e-05, ⚠ same locus), [[ATR]] (+0.64, fdr 2e-05), [[MRM1]] (+0.63, fdr 3e-05); moves opposite to [[PJA2]] (-0.64, fdr 2e-05), [[INSIG2]] (-0.55, fdr 4e-05), [[PPP2R5B]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRDM5]] → it (grade B ⚠); 3 go from it, the strongest it → [[TMCO4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 3.33×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Furosemide (drug)]] 5 µM in 1 line (LS 180 2.15×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.27× | +3.5 | 0.22 | 11/38 (NCI-H2030, NCI-H2347, …) | all doses, flat |  |
| [[Finasteride (drug)]] 5 µM |  | 1.27× | +3.4 | 0.22 | 16/37 (hTERT-HPNE, SW480, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.27 | 11/38 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.1 | 0.27 | 10/38 (HEC-1-A, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7787.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.174×** | -25.8 | 0e+00 | 38/38 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.178×** | -25.5 | 0e+00 | 37/38 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.185×** | -24.9 | 0e+00 | 37/38 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.338×** | -22.6 | 0e+00 | 34/38 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.368×** | -14.8 | 0e+00 | 32/36 (HCT15, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.398×** | -13.6 | 3e-40 | 35/38 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.389×** | -13.3 | 3e-38 | 31/38 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.475×** | -10.6 | 3e-24 | 30/38 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.514×** | -9.8 | 6e-21 | 33/37 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -9.0 | 1e-17 | 25/38 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.662×** | -8.6 | 4e-16 | 31/38 (SW1417, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -8.5 | 1e-15 | 33/38 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.574×** | -8.2 | 1e-14 | 28/38 (SW48, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.391×** | -7.3 | 2e-11 | 32/38 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.621×** | -7.0 | 7e-11 | 26/37 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.420×** | -6.7 | 7e-10 | 26/37 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.654×** | -6.3 | 1e-08 | 25/38 (PANC-1, LS 180, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 70.2 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0653× (z -33.1) |
| [[SW480 (line)]] | alt | 43.7 | 0 | 14 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0756× (z -28.2) |
| [[HEC-1-A (line)]] | alt | 67.0 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -28.2) |
| [[PANC-1 (line)]] | alt | 114 | 0 | 13 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -25.5) |
| [[SW1417 (line)]] | alt | 76.8 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -22.4) |
| [[SW48 (line)]] | wt | 88.2 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0884× (z -18.9) |
| [[KATO III (line)]] | alt | 116 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0526× (z -28.0) |
| [[LoVo (line)]] | wt | 93.1 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -24.9) |
| [[LOX-IMVI (line)]] | wt | 46.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0988× (z -26.0) |
| [[LS 180 (line)]] | wt | 78.3 | 1 | 8 (1 ⚠) | [[Furosemide (drug)]] 5 µM 2.15× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.0996× (z -19.4) |
| [[Panc 03.27 (line)]] | alt | 58.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -22.8) |
| [[A-427 (line)]] | wt | 28.7 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.2) |
| [[HT-29 (line)]] | alt | 61.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.9) |
| [[J82 (line)]] | alt | 80.0 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.127× (z -17.9) |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.5) |
| [[C32 (line)]] | wt | 29.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -18.4) |
| [[HOP62 (line)]] | alt | 70.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -19.4) |
| [[AsPC-1 (line)]] | alt | 28.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -14.6) |
| [[HS-578T (line)]] | alt | 30.2 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.103× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0956× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -21.0) |
| [[A549 (line)]] | wt | 69.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.109× (z -17.2) |
| [[Hs 766T (line)]] | wt | 45.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 60.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -18.0) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -11.9) |
| [[A498 (line)]] | wt | 32.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.224× (z -11.9) |
| [[SNU-423 (line)]] | alt | 47.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -13.6) |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -9.8) |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0315× (z -19.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.0) |
| [[AN3 CA (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCO4]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ALDH1A3-AS1]] | +0.67 | +0.68 / +0.51 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ATR]] | +0.64 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[MRM1]] | +0.63 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[UTP20]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[RIN3]] | +0.63 | +0.38 / +0.72 | both halves | 6e-05 |  |
| [[FAR2]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.60 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[AVEN]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PRDM5]] | +0.58 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[GBX2-AS1]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[METTL8]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[ENOX2]] | +0.57 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.64 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[INSIG2]] | -0.55 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[PPP2R5B]] | -0.54 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[PFKFB4]] | -0.54 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[SAP30-DT]] | -0.54 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[HILPDA]] | -0.54 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RAB3A]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[NDRG1]] | -0.53 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[PLEKHH3]] | -0.53 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[FBXO16]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PIP4P2]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ANG]] | -0.52 | -0.46 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM5]] | B | PRDM5 activity raises LRRK1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without PRDM5 | 0.071 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[SEMA6A]] | B | SEMA6A activity lowers LRRK1's level | lines that do not express SEMA6A (18) vs lines expressing it (32) | 1.97× higher at baseline in the lines without SEMA6A | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000290588, NELL2, KSR2; maybe low, not absent |
| [[ME3]] | B | ME3 activity raises LRRK1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without ME3 | 0.081 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCO4]] | B | LRRK1 activity raises TMCO4's level | lines that do not express LRRK1 (10) vs lines expressing it (40) | 2.46× lower at baseline in the lines without LRRK1 | 0.047 | ⚠ within organs, on part of the lines; also absent: HRH1, ALS2CL, CTSZ; maybe low, not absent |
| [[ALDH1A3-AS1]] | B | LRRK1 activity raises ALDH1A3-AS1's level | lines that do not express LRRK1 (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without LRRK1 | 0.074 | ⚠ within organs, on part of the lines; also absent: HRH1, ALS2CL, CTSZ; maybe low, not absent |
| [[SEMA6A]] | B | LRRK1 activity lowers SEMA6A's level | lines that do not express LRRK1 (10) vs lines expressing it (40) | 3.06× higher at baseline in the lines without LRRK1 | 0.094 | ⚠ within organs, on part of the lines; also absent: HRH1, ALS2CL, CTSZ; maybe low, not absent |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.4, -31.7); signed map (4.0, -49.0). **Vector** length 93.2, 26.3% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.1 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -13.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -7.3 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:100,919,327-101,078,257 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23119, KIAA1790, ROCO1, RIPK6 |
| Gene groups (HGNC) | ROCO family; Leucine rich repeat kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q38SD2](https://www.uniprot.org/uniprotkb/Q38SD2) (Leucine-rich repeat serine/threonine-protein kinase 1):

> Serine/threonine-protein kinase which phosphorylates RAB proteins involved in intracellular trafficking. Phosphorylates RAB7A; this activity is dependent on protein kinase C (PKC) activation. Plays a role in the negative regulation of bone mass, acting through the maturation of osteoclasts (By similarity).

**Summary**, from NCBI Gene [79705](https://www.ncbi.nlm.nih.gov/gene/79705):

> This gene encodes a multi-domain protein that is a leucine-rich repeat kinase and a GDP/GTP binding protein. The encoded protein is thought to play a role in the regulation of bone mass. Mice lacking a similar gene showed severe osteopetrosis, increased bone mineralization and decreased bone resorption. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:18608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18608) · Entrez [79705](https://www.ncbi.nlm.nih.gov/gene/79705) · UniProt [Q38SD2](https://www.uniprot.org/uniprotkb/Q38SD2) · Ensembl [ENSG00000154237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154237)

## Data

Gene col 7787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7787); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7787]; `tensor/DDL_lfc|DDL_z.npy` [7787]; `embed/gene_vectors.npy` [7787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7787 or target_col == 7787). Every well: [[LRRK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
