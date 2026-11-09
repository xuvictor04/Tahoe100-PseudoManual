---
symbol: "UBE2V1"
type: "gene"
col: 14413
ensembl_id: "ENSG00000244687"
name: "ubiquitin conjugating enzyme E2 V1"
location: "20q13.13"
module: 25
arm: "+"
pooled_cpm: 158.51
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# UBE2V1

*ubiquitin conjugating enzyme E2 V1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.94× (z +18.4, q 0e+00, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.32× (z +8.1, q 1e-13, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.710× (z -9.9, q 2e-20, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB1A]] (+0.68, fdr 1e-05), [[LIN7C]] (+0.67, fdr 4e-05), [[STMP1]] (+0.66, fdr 2e-05); moves opposite to [[TARS2]] (-0.67, fdr 1e-05), [[C1orf35]] (-0.64, fdr 4e-05), [[LEO1]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +18.4 | 0e+00 | 41/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +17.8 | 0e+00 | 44/49 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +10.4 | 7e-23 | 35/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +8.1 | 1e-13 | 33/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +6.9 | 5e-10 | 30/47 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +6.7 | 2e-09 | 28/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +6.5 | 5e-09 | 28/48 (SW 900, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +6.3 | 2e-08 | 31/48 (C-33 A, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +5.9 | 3e-07 | 24/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +5.7 | 6e-07 | 28/48 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +5.2 | 1e-05 | 23/48 (NCI-H2030, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +5.0 | 3e-05 | 19/48 (LS 180, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +4.4 | 5e-04 | 19/47 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.13× | +3.4 | 0.023 | 17/47 (LS 180, CFPAC-1, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.4 | 0.028 | 18/38 (NCI-H2347, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.12× | +3.1 | 0.070 | 3/48 (HOP62, NCI-H23, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.070 | 7/47 (COLO 205, SNU-1, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.077 | 14/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.710×** | -9.9 | 2e-20 | 41/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.715×** | -9.7 | 7e-20 | 35/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.811×** | -6.1 | 2e-07 | 27/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -5.2 | 3e-05 | 20/48 (J82, RPMI-7951, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.885× | -5.0 | 5e-05 | 20/49 (RKO, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.852× | -4.7 | 3e-04 | 19/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.867× | -4.1 | 0.003 | 18/48 (SW480, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 184 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 1.92× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.530× (z -11.7) |
| [[LoVo (line)]] | wt | 106 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 133 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 149 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +19.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.646× (z -8.5) |
| [[J82 (line)]] | alt | 340 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.12× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 125 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +14.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 155 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.07× (z +10.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +12.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 164 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +14.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 189 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.515× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 150 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.95× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 94.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +13.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 139 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +12.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.600× (z -10.1) |
| [[SNU-423 (line)]] | alt | 178 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +15.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +12.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +17.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 310 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 183 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +11.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.97× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.615× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 123 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.75× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +14.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 150 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 127 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.595× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 146 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.561× (z -8.5) |
| [[A-427 (line)]] | wt | 149 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.82× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +8.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 276 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.23× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +12.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 200 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -12.7) ⚠ cell-cycle shift, explains ~5% of this change |
| [[RPMI-7951 (line)]] | alt | 205 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 72.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.77× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +10.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 180 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 230 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | +0.68 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.67 | +0.40 / +0.73 | both halves | 4e-05 |  |
| [[STMP1]] | +0.66 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MMGT1]] | +0.64 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ARPP19]] | +0.63 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[CERS2]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[EEF1A1P5]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TWF1]] | +0.60 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[PPP2R1B]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Interleukin-17 signaling |
| [[STX16]] | +0.60 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[PEX19]] | +0.60 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[DHFR]] | +0.60 | +0.40 / +0.61 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 10 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARS2]] | -0.67 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[C1orf35]] | -0.64 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[LEO1]] | -0.61 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[ING2]] | -0.61 | -0.36 / -0.67 | both halves | 9e-05 |  |
| [[NUDT8]] | -0.60 | -0.27 / -0.68 | both halves | 3e-04 |  |
| [[RNF113A]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[SAC3D1]] | -0.59 | -0.33 / -0.64 | both halves | 1e-04 |  |
| [[MED19]] | -0.57 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[IMP3]] | -0.57 | -0.24 / -0.66 | both halves | 5e-04 |  |
| [[RASSF7]] | -0.56 | -0.18 / -0.61 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SMIM26]] ⚠ | -0.56 | -0.44 / -0.54 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NUDT22]] | -0.55 | -0.21 / -0.60 | both halves | 7e-04 |  |
| [[NCBP2AS2]] | -0.55 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.55 | -0.30 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UBE2V1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ATL3]] | C | ATL3 activity raises UBE2V1's level | lines that do not express ATL3 (3) vs lines expressing it (47) | 1.38× lower at baseline in the lines without ATL3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGAP10, IQSEC2, GNE; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.3, -20.7); signed map (-17.3, -37.0). **Vector** length 103, 26.9% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +5.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.4 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +2.3 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -9.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -9.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.3 | -0.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 V1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,081,124-50,115,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UEV-1, CROC-1, UEV1A, CROC1; previously UBE2V |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 53 pathways, smallest: TRAF6 mediated IRF7 activation in TLR7/8 or 9 signaling; IRAK1 recruits IKK complex; IRAK1 recruits IKK complex upon TLR7/8 or 9 stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13404](https://www.uniprot.org/uniprotkb/Q13404) (Ubiquitin-conjugating enzyme E2 variant 1):

> Has no ubiquitin ligase activity on its own. The UBE2V1-UBE2N heterodimer catalyzes the synthesis of non-canonical poly-ubiquitin chains that are linked through Lys-63. This type of poly-ubiquitination activates IKK and does not seem to involve protein degradation by the proteasome. Plays a role in the activation of NF-kappa-B mediated by IL1B, TNF, TRAF6 and TRAF2. Mediates transcriptional activation of target genes. Plays a role in the control of progress through the cell cycle and …

**Summary**, from NCBI Gene [7335](https://www.ncbi.nlm.nih.gov/gene/7335):

> Ubiquitin-conjugating E2 enzyme variant proteins constitute a distinct subfamily within the E2 protein family. They have sequence similarity to other ubiquitin-conjugating enzymes but lack the conserved cysteine residue that is critical for the catalytic activity of E2s. The protein encoded by this gene is located in the nucleus and can cause transcriptional activation of the human FOS proto-oncogene. It is thought to be involved in the control of differentiation by altering cell cycle …

**Accessions** — [HGNC:12494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12494) · Entrez [7335](https://www.ncbi.nlm.nih.gov/gene/7335) · UniProt [Q13404](https://www.uniprot.org/uniprotkb/Q13404) · Ensembl [ENSG00000244687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244687)

## Data

Gene col 14413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14413); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14413]; `tensor/DDL_lfc|DDL_z.npy` [14413]; `embed/gene_vectors.npy` [14413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14413 or target_col == 14413). Every well: [[UBE2V1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2V1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
