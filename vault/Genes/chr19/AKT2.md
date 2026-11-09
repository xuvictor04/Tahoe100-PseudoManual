---
symbol: "AKT2"
type: "gene"
col: 2564
ensembl_id: "ENSG00000105221"
name: "AKT serine/threonine kinase 2"
location: "19q13.2"
module: 157
arm: "+"
pooled_cpm: 71.95
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 5
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# AKT2

*AKT serine/threonine kinase 2* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.41× (z +8.1, q 3e-13, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.528× (z -15.0, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LENG8]] (+0.70, fdr 9e-06), [[LY6G5B]] (+0.68, fdr 1e-05), [[CCNL2]] (+0.66, fdr 7e-05); moves opposite to [[C17orf58]] (-0.56, fdr 5e-05), [[PSMA7]] (-0.55, fdr 1e-05), [[HPF1]] (-0.53, fdr 3e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 5 go from it, the strongest it → [[MMGT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +8.1 | 3e-13 | 31/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +7.8 | 1e-12 | 29/44 (HEC-1-A, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +7.6 | 8e-12 | 28/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +7.5 | 9e-12 | 29/40 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +6.4 | 2e-08 | 28/49 (RPMI-7951, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.5 | 4e-06 | 22/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.14× | +4.4 | 7e-04 | 9/48 (LS 180, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.003 | 19/48 (PANC-1, RPMI-7951, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.014 | 19/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.043 | 11/47 (MIA PaCa-2, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | 1.16× | +3.3 | 0.043 | 9/48 (NCI-H23, LS 180, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.3 | 0.047 | 15/43 (LOX-IMVI, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.051 | 13/47 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.066 | 14/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.10× | +3.1 | 0.066 | 1/48 (COLO 205) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 1.10× | +3.1 | 0.066 | 1/48 (NCI-H1792) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.528×** | -15.0 | 0e+00 | 43/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.540×** | -14.5 | 1e-45 | 42/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.583×** | -12.7 | 9e-35 | 41/48 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.653×** | -9.6 | 7e-20 | 38/48 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -8.7 | 4e-16 | 36/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.704×** | -8.3 | 1e-14 | 34/48 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -7.9 | 3e-13 | 38/48 (SW1417, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.730×** | -7.4 | 8e-12 | 28/47 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.837× | -5.9 | 2e-07 | 24/48 (HOP62, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.798×** | -5.3 | 6e-06 | 26/48 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.693×** | -4.5 | 3e-04 | 20/48 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.821×** | -4.4 | 5e-04 | 16/47 (SHP-77, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.827×** | -4.2 | 1e-03 | 18/48 (Hs 766T, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.843× | -4.0 | 0.002 | 14/48 (SNU-1, RKO, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.890× | -3.9 | 0.004 | 23/48 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Altretamine (drug)]] 5 µM |  | 0.855× | -3.6 | 0.013 | 11/48 (HOP62, A549, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.867× | -3.4 | 0.024 | 9/48 (LS 180, HT-29, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 586 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 1.90× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.486× (z -12.3) |
| [[HT-29 (line)]] | alt | 57.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -13.7) |
| [[KATO III (line)]] | alt | 47.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.420× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 27.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.3) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.8) | — |
| [[RKO (line)]] | wt | 44.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -10.0) |
| [[A-427 (line)]] | wt | 40.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -10.6) |
| [[A498 (line)]] | wt | 38.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.441× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 75.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.43× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 50.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.6) ⚠ cell-cycle shift, explains ~13% of this change | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 41.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +24.6) ⚠ cell-cycle shift, explains ~13% of this change | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.0) |
| [[A-172 (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.2) ⚠ cell-cycle shift, explains ~13% of this change |
| [[C32 (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +14.9) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[CFPAC-1 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -9.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[COLO 205 (line)]] | alt | 38.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.295× (z -8.8) |
| [[HOP62 (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +9.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.357× (z -9.3) |
| [[LS 180 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H1573 (line)]] | alt | 21.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.8) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[NCI-H23 (line)]] | alt | 34.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 57.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.1) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[SHP-77 (line)]] | alt | 62.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -14.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG8]] | +0.70 | +0.57 / +0.76 | both halves | 9e-06 | **novel candidate** |
| [[LY6G5B]] | +0.68 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[CCNL2]] | +0.66 | +0.38 / +0.71 | both halves | 7e-05 |  |
| [[GET4]] | +0.65 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[MTA2]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[U2AF2]] | +0.63 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[BAG6]] | +0.63 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[RMRP]] | +0.62 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PLXNB1]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CDK5RAP3]] | +0.61 | +0.46 / +0.73 | both halves | 3e-05 |  |
| [[INPPL1]] | +0.61 | +0.53 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 607 |
| [[SRSF1]] | +0.61 | +0.39 / +0.58 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C17orf58]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[PSMA7]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 | pathway: Apoptosis |
| [[HPF1]] | -0.53 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[CMAS]] | -0.53 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[NOL7]] ⚠ | -0.53 | -0.36 / -0.49 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PUS3]] | -0.52 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[PET117]] | -0.52 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[GADD45GIP1]] | -0.51 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[ZNF280B]] | -0.51 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[NDUFA7]] | -0.51 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[LSM10]] | -0.51 | -0.34 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMGT1]] | B | [[AKT1]], AKT2, [[AKT3]] activity raises MMGT1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[GTF3C4]] | B | [[AKT1]], AKT2, [[AKT3]] activity raises GTF3C4's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[HSPA13]] | B | [[AKT1]], AKT2, [[AKT3]] activity raises HSPA13's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[TWF1]] | B | [[AKT1]], AKT2, [[AKT3]] activity raises TWF1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ZHX1]] | B | [[AKT1]], AKT2, [[AKT3]] activity raises ZHX1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.7, -24.4); signed map (-15.9, -32.7). **Vector** length 93.9, 21.0% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.6 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -2.4 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.0 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -7.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | AKT serine/threonine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,230,317-40,285,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKBβ |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes; AKT kinase family |
| Hallmark sets | MYOGENESIS, KRAS_SIGNALING_UP, APICAL_JUNCTION |
| Reactome | 88 pathways, smallest: AKT-mediated inactivation of FOXO1A; Activation of AKT2; Inhibition of TSC complex formation by AKT (PKB) |
| Matched by | ensembl_id |

**Function**, from UniProt [P31751](https://www.uniprot.org/uniprotkb/P31751) (RAC-beta serine/threonine-protein kinase):

> Serine/threonine kinase closely related to AKT1 and AKT3. All 3 enzymes, AKT1, AKT2 and AKT3, are collectively known as AKT kinase. AKT regulates many processes including metabolism, proliferation, cell survival, growth and angiogenesis, through the phosphorylation of a range of downstream substrates. Over 100 substrates have been reported so far, although for most of them, the precise AKT kinase catalyzing the reaction was not specified. AKT regulates glucose uptake by mediating …

**Summary**, from NCBI Gene [208](https://www.ncbi.nlm.nih.gov/gene/208):

> This gene is a putative oncogene encoding a protein belonging to a subfamily of serine/threonine kinases containing SH2-like (Src homology 2-like) domains, which is involved in signaling pathways. The gene serves as an oncogene in the tumorigenesis of cancer cells For example, its overexpression contributes to the malignant phenotype of a subset of human ductal pancreatic cancers. The encoded protein is a general protein kinase capable of phophorylating several known proteins, and has also been …

**Accessions** — [HGNC:392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:392) · Entrez [208](https://www.ncbi.nlm.nih.gov/gene/208) · UniProt [P31751](https://www.uniprot.org/uniprotkb/P31751) · Ensembl [ENSG00000105221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105221)

## Data

Gene col 2564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2564); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2564]; `tensor/DDL_lfc|DDL_z.npy` [2564]; `embed/gene_vectors.npy` [2564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2564 or target_col == 2564). Every well: [[AKT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
