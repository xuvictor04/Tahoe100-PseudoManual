---
symbol: "XKR6"
type: "gene"
col: 10042
ensembl_id: "ENSG00000171044"
name: "XK related 6"
location: "8p23.1"
module: 16
arm: "+"
pooled_cpm: 68.59
n_lines_expressing: 32
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# XKR6

*XK related 6* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.01× (z +10.8, q 3e-24, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.463× (z -16.8, q 0e+00, down in 28 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF780B]] (+0.59, fdr 1e-05), [[RANBP6]] (+0.59, fdr 1e-05), [[ZNF780A]] (+0.58, fdr 1e-05); moves opposite to [[TAF5]] (-0.58, fdr 1e-05), [[WHAMMP1]] (-0.57, fdr 1e-05), [[TMEM50B]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[NAV3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +10.8 | 3e-24 | 28/30 (HOP62, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +8.2 | 5e-14 | 21/30 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +7.7 | 4e-12 | 23/30 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.5 | 1e-08 | 23/30 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +5.0 | 8e-05 | 13/30 (HOP62, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 8e-05 | 19/30 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.24×** | +4.7 | 2e-04 | 15/30 (NCI-H460, A-427, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +4.5 | 6e-04 | 17/31 (RKO, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.035 | 11/30 (A-172, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.073 | 8/30 (KATO III, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.463×** | -16.8 | 0e+00 | 28/30 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.473×** | -11.1 | 4e-26 | 28/32 (C-33 A, RKO, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.488×** | -10.6 | 4e-24 | 28/30 (NCI-H23, H4, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.600×** | -7.6 | 6e-12 | 21/29 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.626×** | -7.2 | 6e-11 | 19/31 (C-33 A, KATO III, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.640×** | -6.9 | 6e-10 | 20/30 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.619×** | -6.8 | 7e-10 | 19/27 (KATO III, C-33 A, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.666×** | -6.3 | 3e-08 | 23/30 (KATO III, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.670×** | -5.9 | 2e-07 | 20/29 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.697×** | -5.5 | 2e-06 | 19/30 (PANC-1, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.707×** | -5.3 | 5e-06 | 22/30 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.718×** | -5.1 | 2e-05 | 17/30 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.738×** | -4.7 | 1e-04 | 19/30 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.735×** | -4.6 | 2e-04 | 16/26 (SNU-1, C-33 A, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.768×** | -4.1 | 0.002 | 18/30 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.788×** | -3.5 | 0.019 | 16/30 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -3.1 | 0.061 | 13/30 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.820×** | -3.0 | 0.070 | 16/30 (PANC-1, KATO III, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.872× | -3.0 | 0.088 | 9/30 (Hs 766T, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 70.2 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -17.2) |
| [[KATO III (line)]] | alt | 361 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 177 | 2 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -21.8) |
| [[NCI-H23 (line)]] | alt | 159 | 1 | 7 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -22.1) |
| [[RKO (line)]] | wt | 143 | 2 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.44× (z +9.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -14.1) |
| [[C-33 A (line)]] | alt | 300 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -17.9) |
| [[A-172 (line)]] | wt | 294 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -13.2) |
| [[A-427 (line)]] | wt | 80.7 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -11.0) |
| [[H4 (line)]] | wt | 329 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -16.4) |
| [[HT-29 (line)]] | alt | 91.3 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.44× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -11.9) |
| [[J82 (line)]] | alt | 74.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 217 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -14.8) |
| [[C32 (line)]] | wt | 91.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -14.6) |
| [[HOP62 (line)]] | alt | 33.6 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.09× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 45.1 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -10.0) |
| [[SNU-1 (line)]] | wt | 337 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0547× (z -30.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -17.0) |
| [[COLO 205 (line)]] | alt | 94.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -12.8) |
| [[Hs 766T (line)]] | wt | 64.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 20.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.95× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 57.4 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -10.4) |
| [[SW 900 (line)]] | alt | 57.2 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 42.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -10.5) |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -8.5) |
| [[A498 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.83 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF780B]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[RANBP6]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZNF780A]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[MRPL47]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ZNF880]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZNF121]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[MGA]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 | same gene group |
| [[MDM4]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RBAK]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[TRIM16]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ANAPC1P4]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[WHAMMP1]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.55 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SETD3]] | -0.53 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RNF38]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZFYVE21]] | -0.53 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[MTM1]] | -0.52 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[NARF]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PCMTD1]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[FCHO2]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises XKR6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers XKR6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV3]] | B | XKR6 activity raises NAV3's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without XKR6 | 0.050 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |
| [[ZFPM2-AS1]] | B | XKR6 activity raises ZFPM2-AS1's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 2.09× lower at baseline in the lines without XKR6 | 0.074 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |
| [[MIR181A1HG]] | B | XKR6 activity raises MIR181A1HG's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without XKR6 | 0.085 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |
| [[RRP15]] | B | XKR6 activity lowers RRP15's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 1.19× higher at baseline in the lines without XKR6 | 0.093 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |
| [[MMP16]] | B | XKR6 activity raises MMP16's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 2.14× lower at baseline in the lines without XKR6 | 0.096 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | XKR6 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express XKR6 (18) vs lines expressing it (30) | the lines without XKR6: 1.14× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.3, 15.5); signed map (0.6, -30.3). **Vector** length 89.9, 24.6% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.0 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +8.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +1.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -16.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.6 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | XK related 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:10,896,045-11,201,833 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C8orf7, C8orf21, C8orf5 |
| Gene groups (HGNC) | XK related family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q5GH73](https://www.uniprot.org/uniprotkb/Q5GH73) carries no function annotation.

**Summary**, from NCBI Gene [286046](https://www.ncbi.nlm.nih.gov/gene/286046):

> Predicted to be involved in apoptotic process involved in development; engulfment of apoptotic cell; and phosphatidylserine exposure on apoptotic cell surface. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27806) · Entrez [286046](https://www.ncbi.nlm.nih.gov/gene/286046) · UniProt [Q5GH73](https://www.uniprot.org/uniprotkb/Q5GH73) · Ensembl [ENSG00000171044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171044)

## Data

Gene col 10042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10042); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10042]; `tensor/DDL_lfc|DDL_z.npy` [10042]; `embed/gene_vectors.npy` [10042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10042 or target_col == 10042). Every well: [[XKR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XKR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
