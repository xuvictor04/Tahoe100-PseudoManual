---
symbol: "SRD5A1"
type: "gene"
col: 7003
ensembl_id: "ENSG00000145545"
name: "steroid 5 alpha-reductase 1"
location: "5p15.31"
module: 16
arm: "-"
pooled_cpm: 39.73
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SRD5A1

*steroid 5 alpha-reductase 1* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.63× (z +11.8, q 1e-29, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.446× (z -27.6, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD3]] (+0.66, fdr 1e-05), [[PIGF]] (+0.65, fdr 1e-05), [[ABCB10]] (+0.64, fdr 7e-06); moves opposite to [[METTL18]] (-0.66, fdr 7e-06), [[HNRNPH2]] (-0.66, fdr 8e-06), [[ZNF155]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +11.8 | 1e-29 | 38/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +11.8 | 1e-29 | 36/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +10.6 | 5e-24 | 34/48 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +9.5 | 4e-19 | 27/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.4 | 5e-19 | 32/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +9.4 | 5e-19 | 25/38 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +8.8 | 9e-17 | 33/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +8.2 | 2e-14 | 25/45 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.1 | 8e-11 | 29/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +6.9 | 4e-10 | 26/48 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.7 | 6e-07 | 20/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +4.7 | 1e-04 | 21/48 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +4.5 | 2e-04 | 14/48 (A498, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.21×** | +4.4 | 4e-04 | 16/47 (C-33 A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +4.3 | 7e-04 | 7/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 18/48 (RKO, A-427, …) | rises with dose |  |
| [[Neratinib (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.015 | 2/48 (NCI-H661, HCT15) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.3 | 0.033 | 7/48 (A-427, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.054 | 6/47 (NCI-H2030, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Trimetrexate (drug)]] 5 µM |  | 1.10× | +3.1 | 0.058 | 5/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.446×** | -27.6 | 0e+00 | 45/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -16.8 | 0e+00 | 43/48 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.596×** | -12.6 | 3e-34 | 36/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -12.2 | 3e-32 | 37/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -9.8 | 2e-20 | 29/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.718×** | -8.1 | 5e-14 | 24/48 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.721×** | -8.0 | 1e-13 | 27/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.579×** | -7.0 | 2e-10 | 25/48 (A-427, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.771×** | -6.3 | 1e-08 | 24/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.772×** | -6.3 | 2e-08 | 24/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -5.3 | 6e-06 | 22/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.816×** | -5.0 | 3e-05 | 23/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.5 | 0.017 | 17/48 (SNU-1, HS-578T, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.869× | -3.4 | 0.023 | 9/48 (A498, C-33 A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.862× | -3.4 | 0.028 | 9/47 (A-172, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.882× | -3.1 | 0.073 | 10/48 (C-33 A, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -27.8) |
| [[A-427 (line)]] | wt | 51.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -19.4) |
| [[SW480 (line)]] | alt | 48.0 | 3 (1 ⚠) | 3 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -14.9) |
| [[A-172 (line)]] | wt | 68.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -16.9) |
| [[A549 (line)]] | wt | 37.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.7) |
| [[HOP62 (line)]] | alt | 62.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -25.5) |
| [[LoVo (line)]] | wt | 42.5 | 1 | 3 | [[Panobinostat (drug)]] 5 µM 2.26× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 21.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -29.8) |
| [[Panc 03.27 (line)]] | alt | 45.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.7) |
| [[SW1417 (line)]] | alt | 48.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.379× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.8) |
| [[H4 (line)]] | wt | 31.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0658× (z -15.8) |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -15.9) |
| [[J82 (line)]] | alt | 74.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 29.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 58.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 25.6 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.8) ⚠ cell-cycle shift, explains ~18% of this change | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.0) |
| [[A498 (line)]] | wt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.9) |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.120× (z -9.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 50.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.8) |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -8.6) |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.5) |
| [[HS-578T (line)]] | alt | 52.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.3) |
| [[HT-29 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.0) |
| [[KATO III (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 37.7 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 46.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.193× (z -9.1) |
| [[SNU-423 (line)]] | alt | 49.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.1) |
| [[C32 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[PIGF]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ABCB10]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ANKRD36B]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[STX2]] | +0.62 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[ANKRD27]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MFN1]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[IMPDH1]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ZNF250]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SGTB]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MXRA7]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | -0.66 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[HNRNPH2]] | -0.66 | -0.68 / -0.58 | both halves | 8e-06 |  |
| [[ZNF155]] | -0.65 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.64 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.64 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[ATXN7L1]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[EPC2]] | -0.63 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.62 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.62 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[CASC9]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[LARP7]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[RBM23]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SRD5A1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.7, 11.7); signed map (-47.0, -4.9). **Vector** length 106, 26.1% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +11.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.9 | +4.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.9 | -27.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -16.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -12.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | steroid 5 alpha-reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.31 — chr5:6,633,290-6,676,539 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Steroid 5-alpha reductase family |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Androgen biosynthesis; Metabolism of steroid hormones; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [P18405](https://www.uniprot.org/uniprotkb/P18405) (3-oxo-5-alpha-steroid 4-dehydrogenase 1):

> Catalyzes the irreversible stereospecific reduction of the delta 4,5 bond (double bond between carbons 4 and 5) of various 3-oxo steroids (3-keto steroids) producing their 5alpha dihydro-3-oxo forms. Converts testosterone into 5-alpha-dihydrotestosterone (DHT), a more potent androgen as it is the preferred ligand for androgen receptor (AR) transactivation, making this reaction a key step in male sexual differentiation during development. Besides testosterone, it can also act on other steroids, …

**Summary**, from NCBI Gene [6715](https://www.ncbi.nlm.nih.gov/gene/6715):

> Steroid 5-alpha-reductase (EC 1.3.99.5) catalyzes the conversion of testosterone into the more potent androgen, dihydrotestosterone (DHT). Also see SRD5A2 (MIM 607306).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:11284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11284) · Entrez [6715](https://www.ncbi.nlm.nih.gov/gene/6715) · UniProt [P18405](https://www.uniprot.org/uniprotkb/P18405) · Ensembl [ENSG00000145545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145545)

## Data

Gene col 7003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7003); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7003]; `tensor/DDL_lfc|DDL_z.npy` [7003]; `embed/gene_vectors.npy` [7003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7003 or target_col == 7003). Every well: [[SRD5A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRD5A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
