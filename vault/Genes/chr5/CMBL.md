---
symbol: "CMBL"
type: "gene"
col: 8908
ensembl_id: "ENSG00000164237"
name: "carboxymethylenebutenolidase homolog"
location: "5p15.2"
module: 45
arm: "+"
pooled_cpm: 26.33
n_lines_expressing: 41
n_dd_up: 14
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# CMBL

*carboxymethylenebutenolidase homolog* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.92× (z +11.6, q 3e-28, up in 24 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.65× (z +5.7, q 3e-06, up in 26 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.256× (z -21.5, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM7SF3]] (+0.63, fdr 1e-05), [[GAMT]] (+0.59, fdr 1e-05), [[FAM210B]] (+0.57, fdr 1e-05); moves opposite to [[SMIM12]] (-0.53, fdr 3e-05), [[RNF34]] (-0.51, fdr 2e-05), [[LRWD1]] (-0.47, fdr 7e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABL1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[EPHX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +11.6 | 3e-28 | 24/28 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +10.6 | 5e-24 | 33/35 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +5.7 | 3e-06 | 26/39 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.0 | 8e-05 | 20/30 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.9 | 1e-04 | 18/37 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.34×** | +4.7 | 3e-04 | 20/39 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +4.5 | 5e-04 | 22/39 (KATO III, J82, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.011 | 20/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.020 | 17/39 (A-427, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.022 | 18/38 (HCT15, A-427, …) | top dose only | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **1.81×** | +3.5 | 0.025 | 13/38 (NCI-H1792, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.77×** | +3.3 | 0.038 | 13/37 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +3.3 | 0.047 | 13/39 (SW480, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.099 | 13/39 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.256×** | -21.5 | 0e+00 | 37/38 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.283×** | -14.1 | 1e-42 | 34/38 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.380×** | -10.4 | 6e-23 | 35/39 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.421×** | -9.7 | 6e-20 | 32/39 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.492×** | -7.9 | 3e-13 | 32/39 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -7.3 | 3e-11 | 27/39 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.521×** | -7.3 | 3e-11 | 30/38 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -6.8 | 9e-10 | 30/38 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.585×** | -6.0 | 2e-07 | 25/39 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.612×** | -5.5 | 3e-06 | 28/39 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.614×** | -5.4 | 3e-06 | 22/39 (A-427, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.617×** | -5.4 | 4e-06 | 26/39 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.714×** | -5.3 | 5e-06 | 25/39 (CHP-212, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.627×** | -5.2 | 8e-06 | 25/38 (NCI-H460, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.672×** | -4.3 | 8e-04 | 21/38 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.501×** | -4.0 | 0.002 | 20/38 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 72.3 | 1 | 9 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.37× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.1) |
| [[HT-29 (line)]] | alt | 35.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0781× (z -25.7) |
| [[LoVo (line)]] | wt | 51.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -24.3) |
| [[PANC-1 (line)]] | alt | 26.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 42.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -20.7) |
| [[Panc 03.27 (line)]] | alt | 28.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -19.3) |
| [[SNU-423 (line)]] | alt | 23.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -17.1) |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 23.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.9) |
| [[H4 (line)]] | wt | 34.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.5) |
| [[HCT15 (line)]] | alt | 40.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -16.5) |
| [[LS 180 (line)]] | wt | 73.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 54.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -16.9) |
| [[RKO (line)]] | wt | 29.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0712× (z -22.4) |
| [[A498 (line)]] | wt | 72.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 33.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -21.7) |
| [[Hs 766T (line)]] | wt | 33.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -20.9) |
| [[NCI-H1573 (line)]] | alt | 20.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.91× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 9.24 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -11.2) |
| [[SW48 (line)]] | wt | 56.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.1) |
| [[A-172 (line)]] | wt | 23.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.32× (z +10.1) ⚠ toxic | — |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -8.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -8.5) |
| [[KATO III (line)]] | alt | 11.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 20.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -21.3) |
| [[SW480 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -16.9) |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM7SF3]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GAMT]] | +0.59 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[FAM210B]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[QPRT]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CCNG1]] | +0.56 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SNRPN]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PRXL2A]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SCP2]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[CDC40]] | +0.54 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[APOBEC3C]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[TCEA3]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[RAVER2]] | +0.52 | +0.57 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM12]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[RNF34]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[LRWD1]] | -0.47 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[TLNRD1]] | -0.47 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[EPOP]] | -0.46 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[TUBB6]] | -0.44 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[CCDC71L]] | -0.44 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[SAMD4A]] | -0.43 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[RUBCN]] | -0.43 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[CC2D1B]] | -0.42 | -0.47 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity lowers CMBL's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.5% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHX2]] | B | CMBL activity raises EPHX2's level | lines that do not express CMBL (9) vs lines expressing it (41) | 1.78× lower at baseline in the lines without CMBL | 0.013 | ⚠ within organs, on part of the lines; also absent: C2orf72 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.4, -7.7); signed map (-26.8, -4.0). **Vector** length 91.7, 24.8% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.0 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.4 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +4.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.1 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -14.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -5.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.4 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | carboxymethylenebutenolidase homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:10,275,875-10,307,902 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23617 |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DG6](https://www.uniprot.org/uniprotkb/Q96DG6) (Carboxymethylenebutenolidase homolog):

> Cysteine hydrolase whose endogenous substrates and physiological function are unknown. Catalyzes the hydrolytic activation of several ester-based prodrugs, by cleaving the dioxolone ring to yield their respective active metabolites, diacetyl and CO2. Can thus convert the prodrugs Olmesartan medoxomil and Azilsartan medoxomil into their active metabolites (Olmesartan and Azilsartan), two angiotensin receptor blockers. Is also able to activate beta-lactam antibiotics Faropenem medoxomil and …

**Summary**, from NCBI Gene [134147](https://www.ncbi.nlm.nih.gov/gene/134147):

> CMBL (EC 3.1.1.45) is a cysteine hydrolase of the dienelactone hydrolase family that is highly expressed in liver cytosol. CMBL preferentially cleaves cyclic esters, and it activates medoxomil-ester prodrugs in which the medoxomil moiety is linked to an oxygen atom (Ishizuka et al., 2010 [PubMed 20177059]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:25090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25090) · Entrez [134147](https://www.ncbi.nlm.nih.gov/gene/134147) · UniProt [Q96DG6](https://www.uniprot.org/uniprotkb/Q96DG6) · Ensembl [ENSG00000164237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164237)

## Data

Gene col 8908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8908); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8908]; `tensor/DDL_lfc|DDL_z.npy` [8908]; `embed/gene_vectors.npy` [8908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8908 or target_col == 8908). Every well: [[CMBL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMBL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
