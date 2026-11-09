---
symbol: "TNFRSF1A"
type: "gene"
col: 854
ensembl_id: "ENSG00000067182"
name: "TNF receptor superfamily member 1A"
location: "12p13.31"
module: 106
arm: "+"
pooled_cpm: 36.41
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 35
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# TNFRSF1A

*TNF receptor superfamily member 1A* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.27× (z +3.9, q 0.046, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.253× (z -23.1, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB7B]] (+0.63, fdr 7e-06), [[LTBR]] (+0.58, fdr 1e-05, ⚠ same locus), [[STK24]] (+0.53, fdr 1e-05), [[TNS2]] (+0.52, fdr 3e-05); moves opposite to [[CEP135]] (-0.40, fdr 9e-05), [[DTNA]] (-0.40, fdr 0.002, ⚠ not reproduced), [[PPP2R3A]] (-0.39, fdr 4e-04), [[SVIP]] (-0.39, fdr 6e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC16A5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.046 | 17/46 (MIA PaCa-2, LoVo, …) | two highest doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.071 | 12/45 (NCI-H2347, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.23× | +3.3 | 0.16 | 15/45 (MIA PaCa-2, AsPC-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.24 | 13/46 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.27 | 12/47 (A549, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.253×** | -23.1 | 0e+00 | 45/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.279×** | -21.5 | 0e+00 | 45/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.408×** | -21.3 | 0e+00 | 42/46 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.391×** | -15.8 | 0e+00 | 46/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.399×** | -14.9 | 0e+00 | 29/35 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.461×** | -13.1 | 5e-37 | 36/45 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.480×** | -12.3 | 4e-33 | 36/44 (Panc 03.27, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -8.5 | 1e-15 | 33/46 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.609×** | -8.4 | 4e-15 | 31/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -8.0 | 7e-14 | 33/45 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.646×** | -7.4 | 9e-12 | 31/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.649×** | -7.0 | 1e-10 | 28/46 (COLO 205, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -6.4 | 6e-09 | 27/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.670×** | -6.2 | 2e-08 | 22/37 (LS 180, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.699×** | -6.0 | 6e-08 | 26/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.601×** | -4.5 | 2e-04 | 20/47 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.762×** | -4.4 | 3e-04 | 20/46 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.772×** | -4.4 | 3e-04 | 20/45 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -4.2 | 6e-04 | 20/47 (RKO, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.842× | -4.1 | 8e-04 | 18/47 (SW 900, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.6 | 0.007 | 17/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.813×** | -3.5 | 0.008 | 13/47 (SNU-1, CHP-212, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.013 | 17/47 (SNU-423, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.4 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -19.7) |
| [[KATO III (line)]] | alt | 42.9 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -19.1) |
| [[LoVo (line)]] | wt | 38.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -16.7) |
| [[LS 180 (line)]] | wt | 42.4 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.156× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 78.4 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 30.7 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0946× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.179× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 62.6 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0380× (z -30.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.4) |
| [[SW480 (line)]] | alt | 31.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 38.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0694× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.142× (z -16.1) |
| [[HOP62 (line)]] | alt | 39.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -15.2) |
| [[Hs 766T (line)]] | wt | 52.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0630× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.221× (z -16.3) |
| [[HT-29 (line)]] | alt | 54.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 35.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -22.1) |
| [[NCI-H23 (line)]] | alt | 58.4 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0981× (z -20.7) |
| [[A-172 (line)]] | wt | 24.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0655× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -10.8) |
| [[A-427 (line)]] | wt | 26.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.5) |
| [[C32 (line)]] | wt | 31.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.0) |
| [[COLO 205 (line)]] | alt | 33.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 43.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -17.2) |
| [[SNU-423 (line)]] | alt | 33.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.204× (z -10.6) |
| [[SW 900 (line)]] | alt | 69.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -17.8) |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -13.5) |
| [[A498 (line)]] | wt | 47.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -9.3) |
| [[H4 (line)]] | wt | 46.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 24.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.1) |
| [[RKO (line)]] | wt | 38.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.3) |
| [[SNU-1 (line)]] | wt | 34.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.7) |
| [[BT-474 (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -11.9) |
| [[HCT15 (line)]] | alt | 46.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.259× (z -8.9) |
| [[J82 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0672× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.312× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 37.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -12.6) |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.228× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.5) |
| [[A549 (line)]] | wt | 36.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -11.5) |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0576× (z -10.1) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -9.5) |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -13.8) |
| [[SW48 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.183× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 13 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB7B]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[LTBR]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 841; ⚠ same locus (32.9 kb: neighbours can correlate without regulation) |
| [[STK24]] | +0.53 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TNS2]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[SHC1]] | +0.51 | +0.58 / +0.48 | both halves | 2e-05 | STRING 411 |
| [[ASCC1]] | +0.49 | +0.36 / +0.32 | both halves | 2e-04 |  |
| [[PSMA6]] | +0.49 | +0.49 / +0.42 | both halves | 4e-05 | pathway: TNFR2 non-canonical NF-kB pathway |
| [[TSKU]] | +0.48 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[B4GALT1]] | +0.47 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[ID1]] | +0.46 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[B4GALT5]] | +0.45 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[IFNGR1]] | +0.44 | +0.52 / +0.37 | both halves | 7e-05 | same gene group; pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 804 |
| [[COASY]] | +0.44 | +0.48 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP135]] | -0.40 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[DTNA]] | -0.40 | -0.14 / -0.41 | ⚠ not reproduced | 0.002 |  |
| [[PPP2R3A]] | -0.39 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[SVIP]] | -0.39 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[KPNA5]] | -0.37 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[CFAP20DC]] | -0.37 | -0.26 / -0.23 | both halves | 5e-04 |  |
| [[WSCD1]] | -0.37 | -0.21 / -0.36 | both halves | 7e-04 |  |
| [[DOP1B]] | -0.37 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[ARHGEF10]] | -0.37 | -0.27 / -0.36 | both halves | 3e-04 | pathway: Death Receptor Signaling |
| [[AADACP1]] | -0.36 | -0.22 / -0.31 | both halves | 6e-04 |  |
| [[JUN]] | -0.36 | -0.47 / -0.25 | both halves | 4e-04 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 729 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A5]] | B | SLC16A5 activity raises TNFRSF1A's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without SLC16A5 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[C1RL]] | C | C1RL activity raises TNFRSF1A's level | lines that do not express C1RL (3) vs lines expressing it (47) | 3.63× lower at baseline in the lines without C1RL | 9e-04 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: PHLDA1, CASP8, SP100 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, 18.7); signed map (20.9, 32.2). **Vector** length 81.4, 18.8% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.2 | -12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.5 | -14.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -2.9 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -21.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,328,757-6,342,114 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TNF-R, TNFAR, TNFR60, TNF-R-I, CD120a, TNF-R55; previously TNFR1 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, PI3K_AKT_MTOR_SIGNALING, XENOBIOTIC_METABOLISM |
| Reactome | 11 pathways, smallest: TNFR1-mediated ceramide production; TNFs bind their physiological receptors; TNFR1-induced proapoptotic signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P19438](https://www.uniprot.org/uniprotkb/P19438) (Tumor necrosis factor receptor superfamily member 1A):

> Receptor for TNF/TNFSF2 and LTA/TNFSF1, which activates the tumor necrosis factor-mediated (TNF) signaling pathway upon ligand-binding. The TNF signaling pathway acts as a master regulator of the immune system, which either (1) promotes cell survival and inflammation by activating the canonical NF-kappa-B pathway or (2) trigger programmed cell death (apoptosis and necroptosis). TNF/TNFSF2 and LTA/TNFSF1-binding induces formation of the complex I (TNF-R1 signaling complex also known as TNF-RSC), …

**Summary**, from NCBI Gene [7132](https://www.ncbi.nlm.nih.gov/gene/7132):

> This gene encodes a member of the TNF receptor superfamily of proteins. The encoded receptor is found in membrane-bound and soluble forms that interact with membrane-bound and soluble forms, respectively, of its ligand, tumor necrosis factor alpha. Binding of membrane-bound tumor necrosis factor alpha to the membrane-bound receptor induces receptor trimerization and activation, which plays a role in cell survival, apoptosis, and inflammation. Proteolytic processing of the encoded receptor …

**Accessions** — [HGNC:11916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11916) · Entrez [7132](https://www.ncbi.nlm.nih.gov/gene/7132) · UniProt [P19438](https://www.uniprot.org/uniprotkb/P19438) · Ensembl [ENSG00000067182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067182)

## Data

Gene col 854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 854); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 854]; `tensor/DDL_lfc|DDL_z.npy` [854]; `embed/gene_vectors.npy` [854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 854 or target_col == 854). Every well: [[TNFRSF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
