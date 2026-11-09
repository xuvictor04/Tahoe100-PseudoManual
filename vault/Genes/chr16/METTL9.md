---
symbol: "METTL9"
type: "gene"
col: 12318
ensembl_id: "ENSG00000197006"
name: "methyltransferase 9, His-X-His N1(pi)-histidine"
location: "16p12.2"
module: 168
arm: "+"
pooled_cpm: 59.47
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# METTL9

*methyltransferase 9, His-X-His N1(pi)-histidine* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.70× (z +13.1, q 2e-36, up in 29 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +10.6, q 6e-24, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.423× (z -31.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD3]] (+0.65, fdr 7e-06), [[RCN2]] (+0.63, fdr 1e-05), [[RPA1]] (+0.62, fdr 1e-05); moves opposite to [[HDAC9]] (-0.62, fdr 1e-05), [[RTL6]] (-0.61, fdr 7e-06), [[NSRP1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +13.1 | 2e-36 | 29/41 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +12.7 | 1e-34 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +10.6 | 6e-24 | 31/48 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +8.8 | 1e-16 | 29/47 (PANC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +6.5 | 7e-09 | 28/49 (COLO 205, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +6.5 | 1e-08 | 25/45 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **1.21×** | +4.6 | 3e-04 | 21/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.20× | +4.5 | 5e-04 | 23/50 (HEC-1-A, RKO, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.17× | +3.9 | 0.006 | 14/48 (C32, RPMI-7951, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.16× | +3.8 | 0.007 | 17/48 (PANC-1, KATO III, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.008 | 18/48 (C32, PANC-1, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.021 | 14/48 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.032 | 13/47 (HEC-1-A, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.14× | +3.3 | 0.040 | 10/48 (NCI-H1792, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.423×** | -31.4 | 0e+00 | 47/48 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.510×** | -17.4 | 0e+00 | 44/48 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.580×** | -13.5 | 2e-39 | 43/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -10.9 | 2e-25 | 42/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -8.5 | 2e-15 | 36/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -8.2 | 2e-14 | 31/48 (C32, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.803×** | -5.7 | 1e-06 | 23/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.808×** | -5.5 | 2e-06 | 26/48 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.829×** | -4.9 | 7e-05 | 20/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.840× | -4.4 | 5e-04 | 14/50 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.848× | -4.3 | 9e-04 | 16/47 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.842× | -4.3 | 9e-04 | 15/47 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.956× | -4.3 | 9e-04 | 3/49 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -4.0 | 0.002 | 14/48 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.867× | -3.8 | 0.006 | 17/49 (NCI-H1573, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.899× | -3.5 | 0.018 | 15/48 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.790×** | -3.1 | 0.065 | 5/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.916× | -3.0 | 0.078 | 10/48 (NCI-H1573, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 146 | 3 | 4 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.74× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 78.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -19.9) |
| [[HepG2_C3A (line)]] | wt | 137 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -17.2) |
| [[LoVo (line)]] | wt | 40.7 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 60.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -20.2) |
| [[SW480 (line)]] | alt | 81.0 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.11× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -18.6) |
| [[A-427 (line)]] | wt | 65.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -19.2) |
| [[COLO 205 (line)]] | alt | 85.8 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.40× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.0) |
| [[A-172 (line)]] | wt | 39.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.8) |
| [[A498 (line)]] | wt | 66.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -11.6) |
| [[A549 (line)]] | wt | 68.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 61.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -11.3) |
| [[C32 (line)]] | wt | 73.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -14.2) |
| [[CHP-212 (line)]] | wt | 96.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -14.7) |
| [[HS-578T (line)]] | alt | 40.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.2) |
| [[hTERT-HPNE (line)]] | wt | 63.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.6) |
| [[LOX-IMVI (line)]] | wt | 64.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.2) |
| [[LS 180 (line)]] | wt | 51.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 61.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 52.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -18.7) |
| [[NCI-H2347 (line)]] | alt | 43.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -14.6) |
| [[PANC-1 (line)]] | alt | 52.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +10.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 60.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.9) |
| [[SNU-1 (line)]] | wt | 48.1 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.371× (z -9.2) |
| [[SNU-423 (line)]] | alt | 49.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.0) |
| [[SW 900 (line)]] | alt | 67.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -10.5) |
| [[AN3 CA (line)]] | alt | 98.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -19.9) |
| [[BT-474 (line)]] | alt | 43.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.99× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 51.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.5) |
| [[H4 (line)]] | wt | 62.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.1) |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -10.4) |
| [[HOP62 (line)]] | alt | 50.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -20.5) |
| [[Hs 766T (line)]] | wt | 54.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 46.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -11.6) |
| [[J82 (line)]] | alt | 44.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -15.7) |
| [[KATO III (line)]] | alt | 57.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.2) |
| [[SHP-77 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.17× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 69.0 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.5 µM 0.0627× (z -9.7) |
| [[SW1417 (line)]] | alt | 70.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.9) |
| [[SW48 (line)]] | wt | 47.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.5) |
| [[C-33 A (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 | same gene group; STRING 489 |
| [[RCN2]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[RPA1]] | +0.62 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PIGN]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[PHB2]] | +0.61 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[RNF4]] | +0.61 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[SLC41A3]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[GDAP2]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SNHG30]] | +0.59 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[MTRR]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ARHGEF7]] | +0.58 | +0.70 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC9]] | -0.62 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[RTL6]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.59 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[OSGIN1]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[OXTR]] | -0.58 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[JUND]] | -0.57 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[RNF223]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TUBB2A]] | -0.57 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[DUSP8]] | -0.57 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[MAPK1IP1L]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | -0.56 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[SYNPO]] | -0.56 | -0.63 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises METTL9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-11.8, -14.0); signed map (-49.0, -6.4). **Vector** length 113, 29.9% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +6.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +5.5 | +4.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.0 | -1.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.9 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.9 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | -0.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.5 | -17.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.5 | -10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.7 | -31.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.6 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.4 | -8.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 9, His-X-His N1(pi)-histidine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:21,597,218-21,657,471 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DREV1 |
| Gene groups (HGNC) | 7BS protein methyltransferases; 7BS protein histidine methyltransferases; Histidine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1A3](https://www.uniprot.org/uniprotkb/Q9H1A3) (Protein-L-histidine N-pros-methyltransferase):

> Protein-histidine N-methyltransferase that specifically catalyzes 1-methylhistidine (pros-methylhistidine) methylation of target proteins. Specifically methylates the second His of proteins with a His-x-His (HxH) motif (where 'x' is preferably a small amino acid), while exploiting the first one as a recognition signature. Catalyzes methylation of target proteins such as S100A9, NDUFB3, SLC39A5, SLC39A7, ARMC6 and DNAJB12; 1-methylhistidine modification may affect the binding of zinc and other …

**Summary**, from NCBI Gene [51108](https://www.ncbi.nlm.nih.gov/gene/51108):

> Enables protein-L-histidine N-pros-methyltransferase activity. Predicted to be involved in methylation. Is active in endoplasmic reticulum and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24586) · Entrez [51108](https://www.ncbi.nlm.nih.gov/gene/51108) · UniProt [Q9H1A3](https://www.uniprot.org/uniprotkb/Q9H1A3) · Ensembl [ENSG00000197006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197006)

## Data

Gene col 12318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12318); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12318]; `tensor/DDL_lfc|DDL_z.npy` [12318]; `embed/gene_vectors.npy` [12318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12318 or target_col == 12318). Every well: [[METTL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
