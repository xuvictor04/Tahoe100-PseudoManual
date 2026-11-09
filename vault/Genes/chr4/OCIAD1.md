---
symbol: "OCIAD1"
type: "gene"
col: 3035
ensembl_id: "ENSG00000109180"
name: "OCIA domain containing 1"
location: "4p11"
module: 77
arm: "-"
pooled_cpm: 96.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# OCIAD1

*OCIA domain containing 1* — 4p11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +17.7, q 0e+00, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.60× (z +10.8, q 7e-25, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.632× (z -10.8, q 1e-24, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT13]] (+0.76, fdr 7e-06), [[CHURC1]] (+0.75, fdr 7e-06), [[TIA1]] (+0.74, fdr 1e-05); moves opposite to [[SMG1P2]] (-0.70, fdr 7e-06), [[RNF4]] (-0.69, fdr 7e-06), [[PAQR4]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +17.7 | 0e+00 | 44/49 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +14.7 | 0e+00 | 44/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +14.6 | 0e+00 | 39/44 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +11.4 | 5e-28 | 37/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +10.8 | 7e-25 | 42/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +10.4 | 2e-23 | 40/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +7.1 | 9e-11 | 33/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +5.4 | 5e-06 | 29/48 (C32, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +5.3 | 6e-06 | 27/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +5.0 | 4e-05 | 26/47 (NCI-H2347, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | **1.20×** | +4.2 | 0.001 | 23/47 (LOX-IMVI, SHP-77, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | 1.18× | +4.0 | 0.003 | 20/48 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.009 | 20/48 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.15× | +3.4 | 0.028 | 19/48 (RKO, LoVo, …) | top dose only | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.077 | 12/47 (RPMI-7951, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.085 | 15/48 (A-172, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3035.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.632×** | -10.8 | 1e-24 | 45/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.676×** | -9.3 | 5e-18 | 40/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.726×** | -7.6 | 6e-12 | 39/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.772×** | -6.1 | 1e-07 | 37/48 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.836× | -6.0 | 3e-07 | 21/49 (CHP-212, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.711×** | -4.2 | 0.002 | 25/49 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.841× | -4.1 | 0.003 | 19/48 (SW 900, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.844× | -3.8 | 0.008 | 23/48 (C32, H4, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.906× | -3.3 | 0.058 | 5/48 (H4, SNU-1, …) | top dose only |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.872× | -3.2 | 0.070 | 7/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.080 | 16/48 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 81.4 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +11.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 116 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 88.2 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.84× (z +10.5) | [[Belinostat (drug)]] 5 µM 0.549× (z -10.2) |
| [[A-172 (line)]] | wt | 92.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +15.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 95.2 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 2.03× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.522× (z -8.7) |
| [[SW 900 (line)]] | alt | 163 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.84× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.531× (z -8.8) |
| [[HS-578T (line)]] | alt | 69.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +8.9) | — |
| [[LoVo (line)]] | wt | 99.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.29× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -10.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A-427 (line)]] | wt | 109 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.35× (z +10.1) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.233× (z -9.7) |
| [[A498 (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +13.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 146 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +11.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.549× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 118 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 66.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +16.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 80.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 91.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 82.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +12.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 68.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +13.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +15.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 87.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 96.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 68.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -18.0) ⚠ cell-cycle shift, explains ~19% of this change |
| [[COLO 205 (line)]] | alt | 87.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +10.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 83.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 86.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 84.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 61.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 83.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 57.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | +0.76 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[CHURC1]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[TIA1]] | +0.74 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[LZIC]] | +0.74 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[LARP7]] | +0.73 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[AIMP1]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[C11orf58]] | +0.73 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.72 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[ZMYM4]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.71 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[TRMT10B]] | +0.70 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[MAPK1IP1L]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P2]] | -0.70 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[RNF4]] | -0.69 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[PAQR4]] | -0.67 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[TAF5L]] | -0.67 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[KATNB1]] | -0.67 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.66 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[TSEN54]] | -0.66 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.66 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[TBC1D24]] | -0.65 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.64 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[CYTH3]] | -0.64 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[GFOD2]] | -0.64 | -0.67 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises OCIAD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HLA-V-1]] | B | HLA-V-1 activity raises OCIAD1's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.20× lower at baseline in the lines without HLA-V-1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[AGA-DT]] | B | AGA-DT activity raises OCIAD1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without AGA-DT | 0.091 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-24.8, 8.7); signed map (9.3, -23.4). **Vector** length 107, 30.2% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +11.8 | +14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.9 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +17.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.4 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -6.4 | -6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -10.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -7.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -4.5 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -0.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.4 | +0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | OCIA domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p11 — chr4:48,805,212-48,861,817 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20455, TPA018, OCIA, Asrij |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX40](https://www.uniprot.org/uniprotkb/Q9NX40) (OCIA domain-containing protein 1):

> Maintains stem cell potency (By similarity). Increases STAT3 phosphorylation and controls ERK phosphorylation (By similarity). May act as a scaffold, increasing STAT3 recruitment onto endosomes (By similarity). Involved in integrin-mediated cancer cell adhesion and colony formation in ovarian cancer.

**Summary**, from NCBI Gene [54940](https://www.ncbi.nlm.nih.gov/gene/54940):

> Predicted to be involved in several processes, including hematopoietic stem cell homeostasis; positive regulation of receptor signaling pathway via JAK-STAT; and regulation of stem cell differentiation. Located in membrane and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16074) · Entrez [54940](https://www.ncbi.nlm.nih.gov/gene/54940) · UniProt [Q9NX40](https://www.uniprot.org/uniprotkb/Q9NX40) · Ensembl [ENSG00000109180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109180)

## Data

Gene col 3035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3035); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3035]; `tensor/DDL_lfc|DDL_z.npy` [3035]; `embed/gene_vectors.npy` [3035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3035 or target_col == 3035). Every well: [[OCIAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OCIAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
