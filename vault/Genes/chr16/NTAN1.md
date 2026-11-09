---
symbol: "NTAN1"
type: "gene"
col: 8038
ensembl_id: "ENSG00000157045"
name: "N-terminal asparagine amidase"
location: "16p13.11"
module: 30
arm: "+"
pooled_cpm: 16.2
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# NTAN1

*N-terminal asparagine amidase* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.74× (z +9.8, q 8e-20, up in 26 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.35× (z +7.6, q 8e-12, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.276× (z -32.2, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOSPD3]] (+0.75, fdr 7e-06), [[CDS2]] (+0.75, fdr 7e-06), [[SNX3]] (+0.72, fdr 7e-06); moves opposite to [[ST7L]] (-0.72, fdr 7e-06), [[ERCC6L2]] (-0.71, fdr 1e-05), [[WARS2-AS1]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +9.8 | 8e-20 | 26/41 (A-427, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.7 | 5e-12 | 17/27 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +7.6 | 8e-12 | 29/48 (SHP-77, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 0.002 | 19/48 (HT-29, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.002 | 14/47 (A-427, C32, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.007 | 11/46 (A-427, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.009 | 13/48 (HS-578T, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +3.8 | 0.011 | 13/47 (H4, CFPAC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +3.7 | 0.012 | 6/46 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.020 | 17/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.020 | 8/48 (BT-474, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.020 | 17/47 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.035 | 7/43 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +3.3 | 0.039 | 10/47 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.20×** | +3.3 | 0.039 | 11/43 (NCI-H2347, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.276×** | -32.2 | 0e+00 | 43/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.272×** | -22.2 | 0e+00 | 43/47 (A549, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.331×** | -19.5 | 0e+00 | 42/46 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.531×** | -11.2 | 8e-27 | 32/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.536×** | -11.0 | 3e-26 | 37/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -9.3 | 1e-18 | 28/46 (HepG2/C3A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -9.3 | 1e-18 | 33/48 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.602×** | -9.0 | 2e-17 | 29/46 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.693×** | -6.5 | 6e-09 | 21/48 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -5.3 | 5e-06 | 19/48 (LS 180, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.745×** | -5.2 | 1e-05 | 16/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Gallic acid (drug)]] 5 µM |  | **0.831×** | -4.6 | 2e-04 | 9/48 (SK-MEL-2, A498, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -4.3 | 8e-04 | 14/45 (LOX-IMVI, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.635×** | -4.2 | 0.001 | 12/45 (A498, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.801×** | -3.9 | 0.003 | 13/46 (HCT15, CHP-212, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.883× | -3.1 | 0.067 | 12/48 (BT-474, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 37.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -22.8) |
| [[HepG2_C3A (line)]] | wt | 53.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -17.6) |
| [[A549 (line)]] | wt | 16.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.5) |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.4) |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.9) |
| [[PANC-1 (line)]] | alt | 23.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -18.4) |
| [[A498 (line)]] | wt | 20.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.8) |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 2 | — | [[Isocorydine (drug)]] 0.5 µM 0.0378× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -11.7) |
| [[J82 (line)]] | alt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.6) |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0789× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.3) |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.0) |
| [[SW480 (line)]] | alt | 9.94 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -14.4) |
| [[A-427 (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 1 | — | [[Clopidogrel (drug)]] 0.5 µM 0.0689× (z -9.2) |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.3) |
| [[C32 (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.2) |
| [[H4 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0943× (z -8.9) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.182× (z -10.1) |
| [[HT-29 (line)]] | alt | 4.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -12.0) |
| [[KATO III (line)]] | alt | 9.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 9.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.139× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 8.73 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -8.8) |
| [[SW1417 (line)]] | alt | 9.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -11.0) |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[CDS2]] | +0.75 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[SNX3]] | +0.72 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[HSPB11]] | +0.70 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[GET1]] | +0.70 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.69 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[SDHAP4]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[STX7]] | +0.68 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[SGTB]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.67 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[USP35]] | +0.67 | +0.67 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | -0.72 | -0.75 / -0.60 | both halves | 7e-06 |  |
| [[ERCC6L2]] | -0.71 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.68 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[R3HDM2]] | -0.67 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[POGLUT1]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[ZC3H7B]] | -0.66 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[CHTOP]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[ERCC4]] | -0.65 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.65 | -0.74 / -0.45 | both halves | 3e-05 |  |
| [[CPSF2]] | -0.63 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | -0.62 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[TIA1]] | -0.62 | -0.67 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises NTAN1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.70× lower at baseline in the lines without STARD9 | 0.022 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[SNTA1]] | B | SNTA1 activity raises NTAN1's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without SNTA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.733). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.3, -8.8); signed map (-37.9, -10.0). **Vector** length 96.1, 21.0% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.1 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.8 | -22.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -19.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -32.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Brimonidine (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | N-terminal asparagine amidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,037,854-15,056,079 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AB6](https://www.uniprot.org/uniprotkb/Q96AB6) (Protein N-terminal asparagine amidohydrolase):

> N-terminal asparagine deamidase that mediates deamidation of N-terminal asparagine residues to aspartate. Required for the ubiquitin-dependent turnover of intracellular proteins that initiate with Met-Asn. These proteins are acetylated on the retained initiator methionine and can subsequently be modified by the removal of N-acetyl methionine by acylaminoacid hydrolase (AAH). Conversion of the resulting N-terminal asparagine to aspartate by NTAN1/PNAD renders the protein susceptible to …

**Summary**, from NCBI Gene [123803](https://www.ncbi.nlm.nih.gov/gene/123803):

> The protein encoded by this gene functions in a step-wise process of protein degradation through the N-end rule pathway. This protein acts as a tertiary destabilizing enzyme that deamidates N-terminal L-Asn residues on proteins to produce N-terminal L-Asp. L-Asp substrates are subsequently conjugated to L-Arg, which is recognized by specific E3 ubiquitin ligases and targeted to the proteasome. Pseudogenes of this gene are located on the long arms of chromosomes 8, 10 and 12. Alternative …

**Accessions** — [HGNC:29909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29909) · Entrez [123803](https://www.ncbi.nlm.nih.gov/gene/123803) · UniProt [Q96AB6](https://www.uniprot.org/uniprotkb/Q96AB6) · Ensembl [ENSG00000157045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157045)

## Data

Gene col 8038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8038); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8038]; `tensor/DDL_lfc|DDL_z.npy` [8038]; `embed/gene_vectors.npy` [8038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8038 or target_col == 8038). Every well: [[NTAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
