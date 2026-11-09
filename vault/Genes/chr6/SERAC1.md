---
symbol: "SERAC1"
type: "gene"
col: 4328
ensembl_id: "ENSG00000122335"
name: "serine active site containing 1"
location: "6q25.3"
module: 159
arm: "+"
pooled_cpm: 14.83
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# SERAC1

*serine active site containing 1* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.11× (z +19.7, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.740× (z -5.0, q 3e-04, down in 16 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.758× (z -4.6, q 9e-04, down in 15 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX7]] (+0.75, fdr 1e-05), [[CRLF3]] (+0.75, fdr 7e-06), [[SLC9A6]] (+0.75, fdr 1e-05); moves opposite to [[PCBP1-AS1]] (-0.70, fdr 5e-05), [[MPDU1]] (-0.70, fdr 1e-05), [[USP11]] (-0.69, fdr 3e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **3.11×** | +19.7 | 0e+00 | 44/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.88×** | +18.4 | 0e+00 | 46/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +14.6 | 0e+00 | 44/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.85×** | +10.7 | 1e-24 | 34/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +10.3 | 1e-22 | 38/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +7.4 | 2e-11 | 31/47 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +7.2 | 4e-11 | 27/46 (SK-MEL-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +7.2 | 4e-11 | 30/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.9 | 4e-10 | 21/47 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.3 | 1e-08 | 20/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +6.2 | 3e-08 | 16/47 (LoVo, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +5.2 | 8e-06 | 18/48 (HS-578T, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.1 | 0.002 | 17/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.8 | 0.005 | 11/40 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.23×** | +3.7 | 0.009 | 14/47 (A498, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.011 | 11/46 (HOP62, HT-29, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.039 | 4/47 (SNU-423, J82, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.039 | 7/48 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.040 | 5/48 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.740×** | -5.0 | 3e-04 | 16/31 (SW1417, HT-29, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -4.6 | 9e-04 | 15/47 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.774×** | -4.5 | 0.001 | 15/38 (C-33 A, NCI-H2030, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -4.2 | 0.004 | 18/48 (A-427, NCI-H2347, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.805×** | -3.8 | 0.018 | 9/47 (AN3 CA, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.861× | -3.7 | 0.022 | 18/47 (LoVo, J82, …) | top dose only | composition shift |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.804×** | -3.6 | 0.022 | 9/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -3.6 | 0.026 | 4/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.818×** | -3.5 | 0.029 | 7/47 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.821×** | -3.4 | 0.034 | 11/47 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.874× | -3.3 | 0.047 | 10/48 (CHP-212, H4, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.698×** | -3.3 | 0.050 | 11/47 (Panc 03.27, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.838× | -3.1 | 0.093 | 5/48 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.841× | -3.0 | 0.10 | 7/47 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.842× | -3.0 | 0.10 | 4/47 (NCI-H2030, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 16.6 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.42× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -8.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 16.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.213× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 13.1 | 2 | 0 | [[Belinostat (drug)]] 5 µM 4.31× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 14.7 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.19× (z +9.5) | — |
| [[SW480 (line)]] | alt | 25.9 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.63× (z +10.3) | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.115× (z -8.5) |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -10.6) ⚠ cell-cycle shift, explains ~17% of this change |
| [[LS 180 (line)]] | wt | 16.0 | 1 | 0 | [[Belinostat (drug)]] 5 µM 4.03× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 9.99 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | +0.75 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.75 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.75 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[BLVRA]] | +0.73 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TSPAN33]] | +0.72 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[STRN]] | +0.72 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[PACC1]] | +0.69 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.69 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.68 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[PEDS1]] | +0.68 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[KIF3A]] | +0.67 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PSMD9]] | +0.66 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBP1-AS1]] | -0.70 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[MPDU1]] | -0.70 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[USP11]] | -0.69 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[SON]] | -0.67 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[MEPCE]] | -0.66 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[UBE3B]] | -0.65 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | -0.65 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.65 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[UBE2D3-AS1]] | -0.64 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[PCNX4-DT]] | -0.64 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[CYB5D1]] | -0.63 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[LINC00571]] | -0.63 | -0.57 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises SERAC1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without TSPAN33 | 0.050 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[DNMT3B]] | C | DNMT3B activity raises SERAC1's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.56× lower at baseline in the lines without DNMT3B | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.838). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.6, 1.8); signed map (-38.4, -5.2). **Vector** length 86.4, 17.2% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.1 | +19.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +10.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +14.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +18.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +7.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +6.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.4 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -5.0 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | serine active site containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:158,109,519-158,168,280 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14917 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JX3](https://www.uniprot.org/uniprotkb/Q96JX3) (Protein SERAC1):

> Facilitates the transport of serine from the cytosol to the mitochondria by interacting with and stabilizing Sideroflexin-1 (SFXN1), a mitochondrial serine transporter, playing a fundamental role in the one-carbon cycle responsible for the synthesis of nucleotides needed for mitochondrial DNA replication. Plays an important role in the phosphatidylglycerol (PG) remodeling that is essential for both mitochondrial function and intracellular cholesterol trafficking. Specifically involved in the …

**Summary**, from NCBI Gene [84947](https://www.ncbi.nlm.nih.gov/gene/84947):

> The protein encoded by this gene is a phosphatidylglycerol remodeling protein found at the interface of mitochondria and endoplasmic reticula, where it mediates phospholipid exchange. The encoded protein plays a major role in mitochondrial function and intracellular cholesterol trafficking. Defects in this gene are a cause of 3-methylglutaconic aciduria with deafness, encephalopathy, and Leigh-like syndrome (MEGDEL). Two transcript variants, one protein-coding and the other non-protein coding, …

**Accessions** — [HGNC:21061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21061) · Entrez [84947](https://www.ncbi.nlm.nih.gov/gene/84947) · UniProt [Q96JX3](https://www.uniprot.org/uniprotkb/Q96JX3) · Ensembl [ENSG00000122335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122335)

## Data

Gene col 4328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4328); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4328]; `tensor/DDL_lfc|DDL_z.npy` [4328]; `embed/gene_vectors.npy` [4328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4328 or target_col == 4328). Every well: [[SERAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
