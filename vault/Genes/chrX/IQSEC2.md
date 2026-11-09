---
symbol: "IQSEC2"
type: "gene"
col: 4518
ensembl_id: "ENSG00000124313"
name: "IQ motif and Sec7 domain ArfGEF 2"
location: "Xp11.22"
module: 30
arm: "+"
pooled_cpm: 20.8
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# IQSEC2

*IQ motif and Sec7 domain ArfGEF 2* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.27× (z +5.0, q 4e-04, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.278× (z -38.7, q 0e+00, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASAP3]] (+0.66, fdr 1e-05), [[MFSD9]] (+0.65, fdr 1e-05), [[MYPOP]] (+0.65, fdr 1e-05); moves opposite to [[HIVEP2]] (-0.60, fdr 3e-05), [[CDK6-AS1]] (-0.59, fdr 3e-05), [[CGGBP1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PRRC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +5.0 | 4e-04 | 16/44 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.25×** | +4.6 | 0.001 | 14/44 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.005 | 12/44 (A549, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.005 | 11/45 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.005 | 10/44 (Hs 766T, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +4.0 | 0.005 | 7/45 (AsPC-1, A549, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.20×** | +4.0 | 0.005 | 15/45 (HOP62, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.9 | 0.006 | 9/45 (HEC-1-A, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.9 | 0.006 | 10/45 (PANC-1, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.9 | 0.006 | 9/45 (Hs 766T, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.16× | +3.8 | 0.008 | 8/45 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.18× | +3.3 | 0.039 | 6/43 (NCI-H23, Hs 766T, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.044 | 2/45 (KATO III, PANC-1) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.054 | 5/45 (PANC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.079 | 9/45 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.079 | 4/45 (Panc 03.27, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.14× | +3.0 | 0.084 | 7/45 (HEC-1-A, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.084 | 5/45 (HOP62, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.278×** | -38.7 | 0e+00 | 40/44 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.296×** | -25.0 | 0e+00 | 39/44 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.323×** | -24.1 | 0e+00 | 39/43 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -21.7 | 0e+00 | 43/45 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -19.2 | 0e+00 | 33/43 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.443×** | -17.4 | 0e+00 | 34/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.468×** | -16.2 | 0e+00 | 40/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -15.0 | 0e+00 | 37/45 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -14.1 | 1e-43 | 37/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -11.4 | 4e-28 | 27/44 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -10.8 | 2e-25 | 32/45 (NCI-H460, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.618×** | -9.5 | 9e-20 | 21/32 (HT-29, A-172, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -8.8 | 6e-17 | 25/45 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.666×** | -8.7 | 2e-16 | 21/38 (NCI-H1573, A-427, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.690×** | -7.9 | 1e-13 | 24/45 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -5.6 | 6e-07 | 18/42 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -5.1 | 1e-05 | 15/45 (A-172, Hs 766T, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.712×** | -3.8 | 0.003 | 7/44 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.0 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -26.1) |
| [[LoVo (line)]] | wt | 23.5 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.3) |
| [[A-172 (line)]] | wt | 39.8 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -28.4) |
| [[KATO III (line)]] | alt | 29.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -23.9) |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -16.7) |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -14.5) |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -14.1) |
| [[C32 (line)]] | wt | 15.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.5) |
| [[H4 (line)]] | wt | 39.4 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0578× (z -16.6) |
| [[Hs 766T (line)]] | wt | 32.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -14.7) |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.5) |
| [[PANC-1 (line)]] | alt | 19.5 | 1 (1 ⚠) | 4 | [[Belinostat (drug)]] 5 µM 2.56× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -20.4) |
| [[A549 (line)]] | wt | 32.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -17.5) |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -11.0) |
| [[HT-29 (line)]] | alt | 28.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -22.6) |
| [[NCI-H1573 (line)]] | alt | 25.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0976× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.156× (z -13.4) |
| [[SW 900 (line)]] | alt | 32.1 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.5) |
| [[A-427 (line)]] | wt | 24.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -11.6) |
| [[A498 (line)]] | wt | 19.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0633× (z -24.4) |
| [[J82 (line)]] | alt | 14.8 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -11.7) |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.8) |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 2 | — | [[Pimozide (drug)]] 0.05 µM 0.0816× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.4) |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.3) |
| [[SW480 (line)]] | alt | 16.1 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 9.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -18.1) |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0955× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.8) |
| [[RKO (line)]] | wt | 9.46 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -8.7) ⚠ cell-cycle shift, explains ~69% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -11.1) |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -9.0) |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASAP3]] | +0.66 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MFSD9]] | +0.65 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CAMK2G]] | +0.64 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[CLINT1]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CC2D1A]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RTCA]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[USP35]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PLD3]] | +0.60 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[MKRN2]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SDHAP1]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2]] | -0.60 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[CDK6-AS1]] | -0.59 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CGGBP1]] | -0.58 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[EP300]] | -0.58 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.57 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[NFKB1]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PHF19]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[PPP1R1C]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PNRC2]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[HNRNPK]] | -0.56 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[HIVEP1]] | -0.55 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[CACNA2D1]] | -0.55 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRC1]] | C | IQSEC2 activity raises PRRC1's level | lines that do not express IQSEC2 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without IQSEC2 | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, ARHGAP10, UGDH; maybe low, not absent |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.2, -6.5); signed map (-36.3, -5.0). **Vector** length 79.9, 16.8% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | +6.1 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +0.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -19.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -16.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -25.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -38.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -24.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif and Sec7 domain ArfGEF 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:53,225,828-53,321,350 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0522, BRAG1, IQ-ArfGEF; previously MRX1, MRX78, MRX18 |
| Gene groups (HGNC) | IQSEC ARFGEF family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JU85](https://www.uniprot.org/uniprotkb/Q5JU85) (IQ motif and SEC7 domain-containing protein 2):

> Is a guanine nucleotide exchange factor (GEF) for small GTPases of the ARF family, promoting activation of specific ARFs through exchange of GDP for GTP. In vitro, it has GEF activity towards ARF1 and ARF6. Is involved in the regulation of synaptic transmission and plasticity, controlling trafficking and removal of AMPA receptors GRIA2/GLUA2 and GRIA3/GLUA3 at synapses. Additionally, it may regulate the assembly of the post-synaptic density in a Ca(2+)-dependent manner, operating independently …

**Summary**, from NCBI Gene [23096](https://www.ncbi.nlm.nih.gov/gene/23096):

> This gene encodes a guanine nucleotide exchange factor for the ARF family of small GTP-binding proteins. The encoded protein is a component of the postsynaptic density at excitatory synapses, and may play a critical role in cytoskeletal and synaptic organization through the activation of selected ARF substrates including ARF1 and ARF6. Mutations in this gene have been implicated in nonsyndromic X-linked cognitive disability. Alternatively spliced transcript variants encoding multiple isoforms …

**Accessions** — [HGNC:29059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29059) · Entrez [23096](https://www.ncbi.nlm.nih.gov/gene/23096) · UniProt [Q5JU85](https://www.uniprot.org/uniprotkb/Q5JU85) · Ensembl [ENSG00000124313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124313)

## Data

Gene col 4518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4518); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4518]; `tensor/DDL_lfc|DDL_z.npy` [4518]; `embed/gene_vectors.npy` [4518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4518 or target_col == 4518). Every well: [[IQSEC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQSEC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
