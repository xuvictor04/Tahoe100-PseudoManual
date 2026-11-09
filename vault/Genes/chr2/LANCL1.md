---
symbol: "LANCL1"
type: "gene"
col: 3666
ensembl_id: "ENSG00000115365"
name: "LanC like glutathione S-transferase 1"
location: "2q34"
module: 29
arm: "+"
pooled_cpm: 70.15
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 27
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# LANCL1

*LanC like glutathione S-transferase 1* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.76× (z +11.7, q 9e-29, up in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.42× (z +9.9, q 6e-21, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.429× (z -17.3, q 0e+00, down in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.548× (z -16.9, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM237]] (+0.66, fdr 1e-05), [[MANEA]] (+0.66, fdr 7e-06), [[RBL2]] (+0.65, fdr 1e-05); moves opposite to [[UBE2CP5]] (-0.69, fdr 7e-06), [[ZBTB7A]] (-0.67, fdr 7e-06), [[SPATC1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +11.7 | 9e-29 | 37/46 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +11.5 | 6e-28 | 32/41 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +9.9 | 6e-21 | 34/47 (J82, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +6.4 | 3e-08 | 25/42 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.5 | 6e-06 | 25/47 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +5.1 | 3e-05 | 27/47 (LoVo, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +4.5 | 5e-04 | 23/47 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.001 | 22/47 (NCI-H1573, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.21×** | +3.9 | 0.005 | 18/47 (LS 180, SW1417, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.016 | 13/46 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.17× | +3.3 | 0.048 | 14/47 (RKO, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.429×** | -17.3 | 0e+00 | 44/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.548×** | -16.9 | 0e+00 | 43/47 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.474×** | -15.3 | 0e+00 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.510×** | -13.8 | 6e-41 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -10.5 | 1e-23 | 35/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.600×** | -10.4 | 2e-23 | 37/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.467×** | -8.1 | 3e-14 | 34/48 (SHP-77, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -7.1 | 7e-11 | 29/47 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.697×** | -7.1 | 9e-11 | 31/47 (PANC-1, AN3 CA, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -7.1 | 9e-11 | 31/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -6.7 | 1e-09 | 30/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.725×** | -6.2 | 3e-08 | 25/47 (SHP-77, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -5.9 | 2e-07 | 30/47 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -5.9 | 2e-07 | 26/46 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -4.8 | 5e-05 | 22/47 (J82, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.665×** | -4.4 | 4e-04 | 23/47 (LOX-IMVI, C32, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.666×** | -4.3 | 4e-04 | 19/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.745×** | -4.3 | 5e-04 | 18/47 (J82, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 67.6 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 88.8 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -15.5) |
| [[NCI-H1573 (line)]] | alt | 117 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 8.31× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -18.5) |
| [[SW480 (line)]] | alt | 49.4 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -21.7) |
| [[HOP62 (line)]] | alt | 38.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 613 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -20.2) |
| [[A498 (line)]] | wt | 39.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.2) |
| [[H4 (line)]] | wt | 72.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 57.8 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 29.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.295× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.9) |
| [[LS 180 (line)]] | wt | 50.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.357× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 40.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -18.5) |
| [[A-172 (line)]] | wt | 61.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.445× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 56.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.1) |
| [[AN3 CA (line)]] | alt | 71.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.209× (z -8.5) |
| [[HS-578T (line)]] | alt | 49.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.391× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.527× (z -9.0) |
| [[J82 (line)]] | alt | 47.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 58.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 98.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.3) |
| [[SHP-77 (line)]] | alt | 84.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -11.6) |
| [[SNU-423 (line)]] | alt | 36.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -11.1) |
| [[SW1417 (line)]] | alt | 49.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -11.0) |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.0) |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0662× (z -10.4) |
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.2) |
| [[KATO III (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -11.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 54.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.4) |
| [[SNU-1 (line)]] | wt | 52.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.262× (z -9.2) |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.6) |
| [[A-427 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM237]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[MANEA]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RBL2]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SCP2]] | +0.64 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[PRDX3]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[DLD]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[BBS2]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MDH1]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[IARS2]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ECHS1]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ATP5F1A]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2CP5]] | -0.69 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ZBTB7A]] | -0.67 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[SPATC1]] | -0.64 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[IL12RB2]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[APRG1]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[MASP2]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[SMBD1P]] | -0.60 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[CEACAM19]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[EFNA2]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[HYAL1]] | -0.59 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[LIME1]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers LANCL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.8, -18.5); signed map (-19.8, -40.9). **Vector** length 93.3, 24.1% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.7 | +9.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.3 | +0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.3 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.2 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -10.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | +0.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | LanC like glutathione S-transferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:210,427,131-210,477,652 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p40; previously GPR69A |
| Gene groups (HGNC) | LanC like family |
| Matched by | ensembl_id |

**Function**, from UniProt [O43813](https://www.uniprot.org/uniprotkb/O43813) (Glutathione S-transferase LANCL1):

> Functions as a glutathione transferase. Catalyzes conjugation of the glutathione (GSH) to artificial substrates 1-chloro-2,4-dinitrobenzene (CDNB) and p-nitrophenyl acetate. Mitigates neuronal oxidative stress during normal postnatal development and in response to oxidative stresses probably through GSH antioxidant defense mechanism (By similarity). May play a role in EPS8 signaling. Binds glutathione.

**Summary**, from NCBI Gene [10314](https://www.ncbi.nlm.nih.gov/gene/10314):

> This gene encodes a loosely associated peripheral membrane protein related to the LanC family of bacterial membrane-associated proteins involved in the biosynthesis of antimicrobial peptides. This protein may play a role as a peptide-modifying enzyme component in eukaryotic cells. Previously considered a member of the G-protein-coupled receptor superfamily, this protein is now in the LanC family. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided …

**Accessions** — [HGNC:6508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6508) · Entrez [10314](https://www.ncbi.nlm.nih.gov/gene/10314) · UniProt [O43813](https://www.uniprot.org/uniprotkb/O43813) · Ensembl [ENSG00000115365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115365)

## Data

Gene col 3666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3666); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3666]; `tensor/DDL_lfc|DDL_z.npy` [3666]; `embed/gene_vectors.npy` [3666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3666 or target_col == 3666). Every well: [[LANCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LANCL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
