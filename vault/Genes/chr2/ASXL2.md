---
symbol: "ASXL2"
type: "gene"
col: 6828
ensembl_id: "ENSG00000143970"
name: "ASXL transcriptional regulator 2"
location: "2p23.3"
module: 30
arm: "-"
pooled_cpm: 135.87
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ASXL2

*ASXL transcriptional regulator 2* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.06× (z +15.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.620× (z -9.4, q 3e-18, down in 35 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.711× (z -7.3, q 6e-11, down in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 8 lines (NCI-H23 0.200×, A549 0.178×, NCI-H460 0.319×, SK-MEL-2 0.347×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.231×, SNU-1 0.132×, NCI-H23 0.266×, NCI-H2030 0.364×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.223×, NCI-H460 0.504×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED1]] (+0.73, fdr 7e-06), [[TRAPPC8]] (+0.72, fdr 7e-06), [[ATE1]] (+0.69, fdr 7e-06); moves opposite to [[OSBPL7]] (-0.66, fdr 1e-05), [[HSPB11]] (-0.62, fdr 2e-05), [[HACE1]] (-0.62, fdr 3e-05).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OSBPL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +15.5 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +14.0 | 8e-42 | 40/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +11.9 | 2e-30 | 44/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +11.1 | 1e-26 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +10.7 | 8e-25 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +10.4 | 4e-23 | 43/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +9.1 | 7e-18 | 43/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +8.0 | 7e-14 | 45/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +7.2 | 5e-11 | 37/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.8 | 4e-10 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +6.1 | 6e-08 | 39/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.5 | 2e-06 | 30/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.5 | 2e-06 | 21/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.002 | 25/47 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.008 | 22/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.016 | 18/48 (NCI-H460, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6828.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 8 lines (NCI-H23 0.200×, A549 0.178×, NCI-H460 0.319×, SK-MEL-2 0.347×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.231×, SNU-1 0.132×, NCI-H23 0.266×, NCI-H2030 0.364×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.223×, NCI-H460 0.504×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.620×** | -9.4 | 3e-18 | 35/45 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.711×** | -7.3 | 6e-11 | 45/49 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.714×** | -7.2 | 8e-11 | 35/49 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.717×** | -6.9 | 9e-10 | 30/44 (MIA PaCa-2, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -6.7 | 2e-09 | 35/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -5.7 | 1e-06 | 28/47 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.571×** | -5.3 | 7e-06 | 29/38 (A-172, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.813×** | -4.4 | 6e-04 | 24/48 (C32, NCI-H1573, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.903× | -3.1 | 0.11 | 6/48 (AsPC-1, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.868× | -3.1 | 0.12 | 20/48 (C32, SK-MEL-2, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 167 | 9 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +25.8) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -16.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 174 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +17.5) | — |
| [[A549 (line)]] | wt | 140 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -19.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 199 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -20.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 153 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.580× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 77.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 126 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +18.6) | — |
| [[HOP62 (line)]] | alt | 89.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +16.3) | — |
| [[HT-29 (line)]] | alt | 143 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -12.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 152 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.491× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 153 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +18.2) | — |
| [[A-427 (line)]] | wt | 262 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -20.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 138 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.432× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 89.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.0) | — |
| [[LS 180 (line)]] | wt | 128 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 125 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.2) | — |
| [[A498 (line)]] | wt | 129 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +18.3) | — |
| [[HCT15 (line)]] | alt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 100 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.66× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 57.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +17.1) | — |
| [[RKO (line)]] | wt | 172 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 120 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.398× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 136 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -18.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 117 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[CFPAC-1 (line)]] | alt | 71.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +11.0) | — |
| [[H4 (line)]] | wt | 72.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 242 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -9.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 99.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.482× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 168 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -15.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 281 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -20.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -13.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.226× (z -8.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 85.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.483× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 146 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +8.8) | — |
| [[SW48 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 141 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | +0.73 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC8]] | +0.72 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ATE1]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SON]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB40]] | +0.67 | +0.72 / +0.45 | both halves | 3e-05 | STRING 434 |
| [[ERCC6L2]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[NSD1]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ZFP91]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.65 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ENOX2]] | +0.65 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CUX1]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL7]] | -0.66 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.62 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HACE1]] | -0.62 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[RIMS3]] | -0.62 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[GPR160]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.60 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SEC23A]] | -0.60 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.60 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[AHDC1]] | -0.60 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PRRC1]] | -0.60 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[SKIC3]] | -0.59 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[SUGT1P4-STRA6LP]] | -0.59 | -0.59 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL7]] | B | OSBPL7 activity lowers ASXL2's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without OSBPL7 | 0.035 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[CDA]] | B | CDA activity lowers ASXL2's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.27× higher at baseline in the lines without CDA | 0.095 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-6.9, 3.7); signed map (19.1, -28.9). **Vector** length 124, 41.0% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.3 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.8 | +9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.3 | +15.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.1 | +10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +11.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.1 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -5.6 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.9 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.1 | -2.8 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ASXL transcriptional regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:25,733,753-25,878,487 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASXH2, FLJ10898, KIAA1685 |
| Reactome | 2 pathways, smallest: UCH proteinases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76L83](https://www.uniprot.org/uniprotkb/Q76L83) (Putative Polycomb group protein ASXL2):

> Putative Polycomb group (PcG) protein. PcG proteins act by forming multiprotein complexes, which are required to maintain the transcriptionally repressive state of homeotic genes throughout development. PcG proteins are not required to initiate repression, but to maintain it during later stages of development. They probably act via methylation of histones, rendering chromatin heritably changed in its expressibility (By similarity). Involved in transcriptional regulation mediated by ligand-bound …

**Summary**, from NCBI Gene [55252](https://www.ncbi.nlm.nih.gov/gene/55252):

> This gene encodes a member of a family of epigenetic regulators that bind various histone-modifying enzymes and are involved in the assembly of transcription factors at specific genomic loci. Naturally occurring mutations in this gene are associated with cancer in several tissue types (breast, bladder, pancreas, ovary, prostate, and blood). This gene plays an important role in neurodevelopment, cardiac function, adipogenesis, and osteoclastogenesis. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:23805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23805) · Entrez [55252](https://www.ncbi.nlm.nih.gov/gene/55252) · UniProt [Q76L83](https://www.uniprot.org/uniprotkb/Q76L83) · Ensembl [ENSG00000143970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143970)

## Data

Gene col 6828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6828); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6828]; `tensor/DDL_lfc|DDL_z.npy` [6828]; `embed/gene_vectors.npy` [6828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6828 or target_col == 6828). Every well: [[ASXL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASXL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
