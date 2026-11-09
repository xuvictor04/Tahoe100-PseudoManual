---
symbol: "ANKS6"
type: "gene"
col: 9075
ensembl_id: "ENSG00000165138"
name: "ankyrin repeat and sterile alpha motif domain containing 6"
location: "9q22.33"
module: 36
arm: "+"
pooled_cpm: 31.62
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ANKS6

*ankyrin repeat and sterile alpha motif domain containing 6* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.63× (z +9.6, q 5e-19, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.324× (z -31.5, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACC1]] (+0.78, fdr 7e-06), [[RRP1B]] (+0.77, fdr 7e-06), [[SIMC1]] (+0.74, fdr 7e-06); moves opposite to [[FBXO8]] (-0.68, fdr 7e-06), [[SGO1-AS1]] (-0.66, fdr 3e-05), [[CDKN1B]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LDLRAD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +9.6 | 5e-19 | 30/46 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +9.0 | 5e-17 | 29/47 (NCI-H1792, A-172, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +8.7 | 5e-16 | 28/47 (SNU-423, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +8.1 | 5e-14 | 30/47 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.54×** | +8.1 | 5e-14 | 29/43 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +7.5 | 6e-12 | 30/46 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +7.0 | 2e-10 | 20/47 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.28×** | +4.8 | 1e-04 | 17/46 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +4.7 | 2e-04 | 18/47 (A-172, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +4.3 | 0.001 | 19/46 (NCI-H460, A549, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.013 | 11/46 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.5 | 0.022 | 3/47 (A-172, HCT15, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.031 | 10/47 (A-172, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.034 | 13/45 (NCI-H460, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.3 | 0.040 | 9/46 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.042 | 11/45 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.043 | 7/47 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.055 | 10/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9075.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.324×** | -31.5 | 0e+00 | 41/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.478×** | -20.6 | 0e+00 | 40/46 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.433×** | -15.9 | 0e+00 | 35/47 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.527×** | -12.0 | 4e-31 | 30/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.552×** | -11.7 | 1e-29 | 29/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.362×** | -10.5 | 1e-23 | 36/47 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.699×** | -7.1 | 1e-10 | 25/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -5.9 | 3e-07 | 23/46 (HS-578T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.6 | 1e-06 | 24/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -5.1 | 2e-05 | 19/46 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -4.4 | 5e-04 | 16/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.804×** | -4.2 | 0.001 | 21/45 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.859× | -3.8 | 0.005 | 16/47 (J82, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.827×** | -3.8 | 0.007 | 10/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.832×** | -3.7 | 0.010 | 17/46 (NCI-H460, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.074 | 7/46 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Relugolix (drug)]] 0.5 µM |  | 0.853× | -3.0 | 0.091 | 4/47 (AsPC-1, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 57.5 | 0 | 10 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0929× (z -20.3) |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -23.6) |
| [[NCI-H460 (line)]] | wt | 38.6 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -27.3) |
| [[SW480 (line)]] | alt | 44.9 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -16.1) |
| [[A-172 (line)]] | wt | 35.6 | 1 | 6 | [[Belinostat (drug)]] 5 µM 2.60× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -22.9) |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0850× (z -17.4) |
| [[PANC-1 (line)]] | alt | 29.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -24.9) |
| [[A549 (line)]] | wt | 30.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -20.3) |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 38.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -22.3) |
| [[SW48 (line)]] | wt | 52.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.1) |
| [[A-427 (line)]] | wt | 27.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -13.4) |
| [[A498 (line)]] | wt | 42.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -20.7) |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.1) |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -15.8) |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -15.4) |
| [[J82 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.2) |
| [[LoVo (line)]] | wt | 68.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -24.1) |
| [[LOX-IMVI (line)]] | wt | 30.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -19.4) |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -19.3) |
| [[Panc 03.27 (line)]] | alt | 31.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.9) |
| [[SNU-423 (line)]] | alt | 22.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.5) |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.2) |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -11.1) |
| [[C-33 A (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -9.4) |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.3) |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.1) |
| [[KATO III (line)]] | alt | 42.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.7) |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.142× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.3) |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | +0.78 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[RRP1B]] | +0.77 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[SIMC1]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[TRABD]] | +0.70 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZNF692]] | +0.70 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PPM1F]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[NEIL2]] | +0.69 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GARNL3]] | +0.68 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[MCOLN2]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[NLE1]] | +0.68 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[POLR3G]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ARHGAP8]] | +0.67 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO8]] | -0.68 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[SGO1-AS1]] | -0.66 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[CDKN1B]] | -0.64 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | -0.63 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[ATOSA]] | -0.63 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[CGGBP1]] | -0.63 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | -0.63 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ABCA10]] | -0.63 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[USP11]] | -0.63 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[EFCAB6]] | -0.62 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CFAP418-AS1]] | -0.62 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[STAG2]] | -0.62 | -0.46 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAD3]] | B | LDLRAD3 activity raises ANKS6's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.85× lower at baseline in the lines without LDLRAD3 | 0.011 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TBX20]] | B | TBX20 activity raises ANKS6's level | lines that do not express TBX20 (32) vs lines expressing it (18) | 1.49× lower at baseline in the lines without TBX20 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02335, COX7B2, OLR1 |
| [[MCOLN2]] | B | MCOLN2 activity raises ANKS6's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.34× lower at baseline in the lines without MCOLN2 | 0.054 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[NT5M]] | B | NT5M activity raises ANKS6's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without NT5M | 0.057 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[TOP2A]] | B | TOP2A activity raises ANKS6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LNC-LBCS]] | B | LNC-LBCS activity raises ANKS6's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.18× lower at baseline in the lines without LNC-LBCS | 0.082 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[ABCA3]] | B | ABCA3 activity weakens ANKS6's drug response | lines that do not express ABCA3 (9) vs lines expressing it (38) | the lines without ABCA3 respond 1.33× as strongly (z diff -0.91); strongest at Panobinostat 5 µM: 2.38x vs 1.42x (z diff -2.9) | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[GARNL3]] | C | GARNL3 activity raises ANKS6's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[PPARGC1B]] | C | PPARGC1B activity raises ANKS6's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 2.61× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |
| [[ANKRD13B]] | C | ANKRD13B activity raises ANKS6's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without ANKRD13B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-8.1, -39.5); signed map (-9.6, -54.8). **Vector** length 113, 29.5% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.2 | +7.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +4.9 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.5 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +7.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +4.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.1 | -20.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -31.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.6 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -15.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and sterile alpha motif domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:98,731,329-98,796,965 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36928, NPHP16; previously SAMD6, ANKRD14 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing; Inversin complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DC2](https://www.uniprot.org/uniprotkb/Q68DC2) (Ankyrin repeat and SAM domain-containing protein 6):

> Required for renal function.

**Summary**, from NCBI Gene [203286](https://www.ncbi.nlm.nih.gov/gene/203286):

> This gene encodes a protein containing multiple ankyrin repeats and a SAM domain. It is thought that this protein may localize to the proximal region of the primary cilium, and may play a role in renal and cardiovascular development. Mutations in this gene have been shown to cause a form of nephronophthisis (NPHP16), a chronic tubulo-interstitial nephritis. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:26724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26724) · Entrez [203286](https://www.ncbi.nlm.nih.gov/gene/203286) · UniProt [Q68DC2](https://www.uniprot.org/uniprotkb/Q68DC2) · Ensembl [ENSG00000165138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165138)

## Data

Gene col 9075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9075); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9075]; `tensor/DDL_lfc|DDL_z.npy` [9075]; `embed/gene_vectors.npy` [9075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9075 or target_col == 9075). Every well: [[ANKS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
