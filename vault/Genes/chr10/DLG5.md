---
symbol: "DLG5"
type: "gene"
col: 7495
ensembl_id: "ENSG00000151208"
name: "discs large MAGUK scaffold protein 5"
location: "10q22.3"
module: 137
arm: "+"
pooled_cpm: 73.54
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# DLG5

*discs large MAGUK scaffold protein 5* — 10q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H2347 2.69×, HOP62 2.18×, CFPAC-1 1.88×, SW1417 1.70×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.34×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.204× (z -35.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM11]] (+0.77, fdr 7e-06), [[STRN4]] (+0.71, fdr 7e-06), [[FKRP]] (+0.70, fdr 1e-05); moves opposite to [[DPM1]] (-0.67, fdr 1e-05), [[ANKRD37]] (-0.66, fdr 1e-05), [[PIBF1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7495.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H2347 2.69×, HOP62 2.18×, CFPAC-1 1.88×, SW1417 1.70×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.34×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 1.17× | +3.5 | 0.28 | 11/48 (BT-474, CHP-212, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.204×** | -35.1 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.218×** | -33.6 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.285×** | -27.7 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -13.7 | 2e-40 | 37/49 (SW 900, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.540×** | -13.6 | 6e-40 | 43/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -8.0 | 8e-14 | 36/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.701×** | -7.1 | 8e-11 | 30/50 (SW480, SW 900, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.552×** | -6.8 | 5e-10 | 31/49 (J82, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.753×** | -5.7 | 8e-07 | 28/48 (HOP62, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.621×** | -5.5 | 2e-06 | 27/49 (LOX-IMVI, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -5.4 | 4e-06 | 24/48 (C-33 A, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.820×** | -4.4 | 6e-04 | 23/48 (LS 180, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.836× | -4.0 | 0.003 | 23/48 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | 0.844× | -3.4 | 0.027 | 19/47 (NCI-H23, SW 1271, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 0.850× | -3.3 | 0.043 | 20/47 (RKO, NCI-H2030, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.861× | -3.0 | 0.098 | 9/48 (Hs 766T, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 61.4 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.196× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 81.4 | 3 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +18.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -12.5) |
| [[SW480 (line)]] | alt | 86.5 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -32.5) |
| [[A-172 (line)]] | wt | 107 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -18.6) |
| [[HEC-1-A (line)]] | alt | 85.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -23.5) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0921× (z -23.9) |
| [[HS-578T (line)]] | alt | 46.2 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -15.7) |
| [[LoVo (line)]] | wt | 58.6 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -29.7) |
| [[LS 180 (line)]] | wt | 78.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -22.1) |
| [[NCI-H1573 (line)]] | alt | 99.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -21.5) |
| [[NCI-H23 (line)]] | alt | 45.3 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.176× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -21.6) |
| [[SNU-423 (line)]] | alt | 72.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -20.3) |
| [[SW1417 (line)]] | alt | 129 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -15.2) |
| [[SW48 (line)]] | wt | 92.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -16.1) |
| [[A-427 (line)]] | wt | 63.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.207× (z -17.2) |
| [[A549 (line)]] | wt | 70.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -19.0) |
| [[AsPC-1 (line)]] | alt | 74.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -15.9) |
| [[C32 (line)]] | wt | 67.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -15.3) |
| [[CFPAC-1 (line)]] | alt | 75.6 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -14.5) |
| [[CHP-212 (line)]] | wt | 135 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 91.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -15.9) |
| [[J82 (line)]] | alt | 40.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.171× (z -18.2) |
| [[KATO III (line)]] | alt | 58.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -23.7) |
| [[LOX-IMVI (line)]] | wt | 53.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.161× (z -18.8) |
| [[NCI-H1792 (line)]] | alt | 49.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -19.8) |
| [[NCI-H2030 (line)]] | alt | 87.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -14.6) |
| [[PANC-1 (line)]] | alt | 79.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -18.0) |
| [[RKO (line)]] | wt | 71.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -18.5) |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -14.6) |
| [[SNU-1 (line)]] | wt | 66.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -11.9) |
| [[SW 900 (line)]] | alt | 83.0 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -17.7) |
| [[A498 (line)]] | wt | 96.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -21.7) |
| [[AN3 CA (line)]] | alt | 147 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -12.4) |
| [[C-33 A (line)]] | alt | 101 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -19.0) |
| [[H4 (line)]] | wt | 55.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -12.6) |
| [[HCT15 (line)]] | alt | 93.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -14.7) |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.188× (z -17.4) |
| [[hTERT-HPNE (line)]] | wt | 59.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 64.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -21.2) |
| [[COLO 205 (line)]] | alt | 52.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 40.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -9.1) |
| [[BT-474 (line)]] | alt | 75.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -10.0) |
| [[SHP-77 (line)]] | alt | 29.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -9.7) |
| [[NCI-H2122 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM11]] | +0.77 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[STRN4]] | +0.71 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[FKRP]] | +0.70 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FAIM]] | +0.67 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[TXNRD2]] | +0.66 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SMARCB1]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[BRPF3]] | +0.66 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PRRC2B]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZNF236]] | +0.65 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PIEZO1]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.64 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[WIZ]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM1]] | -0.67 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.66 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[PIBF1]] | -0.64 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.62 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.62 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[UBA6]] | -0.62 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[INSIG2]] | -0.61 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[COG5]] | -0.61 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[TRPT1]] | -0.60 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[SLC2A3]] | -0.60 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MPG]] | -0.59 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[PJA2]] | -0.59 | -0.60 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DLG5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CHST3]] | C | CHST3 activity raises DLG5's level | lines that do not express CHST3 (4) vs lines expressing it (46) | 1.50× lower at baseline in the lines without CHST3 | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, RGS10, ENSG00000290876 |
| [[TMEM178A]] | C | TMEM178A activity raises DLG5's level | lines that do not express TMEM178A (3) vs lines expressing it (47) | 1.56× lower at baseline in the lines without TMEM178A | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MPP4, B4GALT1, LCA5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-7.4, 5.5); signed map (19.4, -32.5). **Vector** length 98.9, 25.1% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.7 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.9 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.8 | -0.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.5 | -27.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -35.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.0 | -13.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -5.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -8.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | discs large MAGUK scaffold protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:77,790,791-77,926,755 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P-dlg, KIAA0583 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 8 pathways, smallest: RHOV GTPase cycle; RHOU GTPase cycle; RND1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDM6](https://www.uniprot.org/uniprotkb/Q8TDM6) (MAGUK scaffold protein DLG5):

> Acts as a regulator of the Hippo signaling pathway. Negatively regulates the Hippo signaling pathway by mediating the interaction of MARK3 with STK3/4, bringing them together to promote MARK3-dependent hyperphosphorylation and inactivation of STK3 kinase activity toward LATS1. Positively regulates the Hippo signaling pathway by mediating the interaction of SCRIB with STK4/MST1 and LATS1 which is important for the activation of the Hippo signaling pathway. Involved in regulating cell …

**Summary**, from NCBI Gene [9231](https://www.ncbi.nlm.nih.gov/gene/9231):

> This gene encodes a member of the family of discs large (DLG) homologs, a subset of the membrane-associated guanylate kinase (MAGUK) superfamily. The MAGUK proteins are composed of a catalytically inactive guanylate kinase domain, in addition to PDZ and SH3 domains, and are thought to function as scaffolding molecules at sites of cell-cell contact. The protein encoded by this gene localizes to the plasma membrane and cytoplasm, and interacts with components of adherens junctions and the …

**Accessions** — [HGNC:2904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2904) · Entrez [9231](https://www.ncbi.nlm.nih.gov/gene/9231) · UniProt [Q8TDM6](https://www.uniprot.org/uniprotkb/Q8TDM6) · Ensembl [ENSG00000151208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151208)

## Data

Gene col 7495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7495); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7495]; `tensor/DDL_lfc|DDL_z.npy` [7495]; `embed/gene_vectors.npy` [7495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7495 or target_col == 7495). Every well: [[DLG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
