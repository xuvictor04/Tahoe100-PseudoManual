---
symbol: "ARHGAP42"
type: "gene"
col: 9201
ensembl_id: "ENSG00000165895"
name: "Rho GTPase activating protein 42"
location: "11q22.1"
module: 66
arm: "+"
pooled_cpm: 120.11
n_lines_expressing: 37
n_dd_up: 20
n_dd_down: 31
n_dd_up_clean: 19
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 26
direction_downstream: 15
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# ARHGAP42

*Rho GTPase activating protein 42* — 11q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.02× (z +9.9, q 2e-20, up in 21 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.349× (z -15.6, q 0e+00, down in 30 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRK]] (+0.68, fdr 7e-06), [[KMO]] (+0.67, fdr 1e-05), [[TNFRSF21]] (+0.64, fdr 7e-06); moves opposite to [[MMS19]] (-0.57, fdr 1e-05), [[IMPDH1]] (-0.55, fdr 2e-05), [[SNX14]] (-0.55, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[TNFRSF21]] → it (grade B ⚠); 15 go from it, the strongest it → [[ZNF549]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +9.9 | 2e-20 | 21/35 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.50×** | +7.1 | 5e-10 | 20/36 (LoVo, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +6.6 | 6e-09 | 16/35 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +5.6 | 4e-06 | 23/34 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 7e-05 | 22/35 (HOP62, SW 900, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 7e-05 | 19/34 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 6e-04 | 18/35 (HOP62, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.5 | 6e-04 | 15/35 (SNU-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +4.4 | 7e-04 | 20/35 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 22/37 (HOP62, SW 900, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.005 | 21/35 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.025 | 17/36 (HOP62, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.026 | 19/37 (HOP62, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.044 | 14/35 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.044 | 12/36 (HOP62, Panc 03.27, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.349×** | -15.6 | 0e+00 | 30/35 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.359×** | -15.1 | 0e+00 | 30/35 (SW48, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.362×** | -15.0 | 0e+00 | 32/35 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -9.7 | 4e-20 | 28/36 (SW48, AsPC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.665×** | -6.0 | 2e-07 | 25/35 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.667×** | -5.8 | 7e-07 | 24/35 (SW48, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -5.7 | 7e-07 | 24/35 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.694×** | -5.2 | 1e-05 | 19/31 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.557×** | -4.5 | 4e-04 | 23/35 (SW48, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.819×** | -4.2 | 0.002 | 18/35 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.757×** | -4.1 | 0.002 | 21/35 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.591×** | -4.1 | 0.002 | 18/35 (SW48, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.762×** | -4.0 | 0.003 | 19/35 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.763×** | -4.0 | 0.003 | 19/35 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.768×** | -3.9 | 0.004 | 19/35 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.780×** | -3.7 | 0.008 | 18/35 (NCI-H1792, AsPC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.840× | -3.6 | 0.008 | 17/36 (A549, CHP-212, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.783×** | -3.6 | 0.009 | 18/35 (Hs 766T, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 811 | 1 | 18 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -25.7) |
| [[SW48 (line)]] | wt | 513 | 1 | 12 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 8.87× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -22.6) |
| [[NCI-H1792 (line)]] | alt | 252 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0802× (z -20.5) |
| [[KATO III (line)]] | alt | 353 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -23.0) |
| [[NCI-H2347 (line)]] | alt | 224 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -19.9) |
| [[SW1417 (line)]] | alt | 308 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -18.2) |
| [[A-172 (line)]] | wt | 37.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +21.1) | — |
| [[A498 (line)]] | wt | 70.9 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -9.9) |
| [[LoVo (line)]] | wt | 181 | 2 | 4 | [[TAK-901 (drug)]] 5 µM 12.6× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.122× (z -17.6) |
| [[LS 180 (line)]] | wt | 241 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -20.5) |
| [[SW480 (line)]] | alt | 151 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -17.3) |
| [[A549 (line)]] | wt | 178 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 185 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -12.3) |
| [[HT-29 (line)]] | alt | 207 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0992× (z -16.3) |
| [[BT-474 (line)]] | alt | 136 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.8) | [[Belinostat (drug)]] 0.5 µM 0.213× (z -12.3) |
| [[CHP-212 (line)]] | wt | 139 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -12.6) |
| [[HOP62 (line)]] | alt | 58.8 | 3 | 0 | [[Trametinib (drug)]] 5 µM 3.53× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 59.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -11.4) |
| [[RKO (line)]] | wt | 88.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.229× (z -13.3) |
| [[SNU-423 (line)]] | alt | 86.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -11.0) |
| [[SW 900 (line)]] | alt | 130 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -13.7) |
| [[J82 (line)]] | alt | 38.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 31.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 88.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.1) |
| [[SNU-1 (line)]] | wt | 41.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 80.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -8.5) |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[NCI-H1573 (line)]] | alt | 48.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.227× (z -8.7) |
| [[A-427 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 28.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 24.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 20.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[KMO]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF21]] | +0.64 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CASC9]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[MYPN]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ITGB8]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[GATA6]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[AKR1B1]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DMRTA1]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ARAP2]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 | pathway: CDC42 GTPase cycle |
| [[RASEF]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMS19]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[IMPDH1]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SNX14]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SEC14L2]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[CROCCP3]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[GLRX]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[NBPF15]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MAP2K1]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SRD5A1]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[HDHD5]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[YEATS2]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ZDHHC9]] | -0.52 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 24, C 2. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF21]] | B | TNFRSF21 activity raises ARHGAP42's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.59× lower at baseline in the lines without TNFRSF21 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[ATP1B1]] | B | ATP1B1 activity raises ARHGAP42's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.29× lower at baseline in the lines without ATP1B1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[AMIGO2]] | B | AMIGO2 activity raises ARHGAP42's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.78× lower at baseline in the lines without AMIGO2 | 0.008 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[RASEF]] | B | RASEF activity raises ARHGAP42's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.60× lower at baseline in the lines without RASEF | 0.009 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[NHS]] | B | NHS activity raises ARHGAP42's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.40× lower at baseline in the lines without NHS | 0.015 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[FRK]] | B | FRK activity raises ARHGAP42's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without FRK | 0.016 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[ITGB8]] | B | ITGB8 activity raises ARHGAP42's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without ITGB8 | 0.019 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[ITGB8]] | B | ITGB8 activity strengthens ARHGAP42's drug response | lines that do not express ITGB8 (11) vs lines expressing it (25) | the lines without ITGB8 respond 0.71× as strongly (z diff +1.75); strongest at Idarubicin (hydrochloride) 5 µM: 0.74x vs 0.49x (z diff +4.1) | 0.026 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5; target measured in part of the lines; artifact flags |
| [[GALNT5]] | B | GALNT5 activity raises ARHGAP42's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 3.06× lower at baseline in the lines without GALNT5 | 0.038 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[PTPRR]] | B | PTPRR activity raises ARHGAP42's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without PTPRR | 0.042 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[HNF4G]] | B | HNF4G activity raises ARHGAP42's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.14× lower at baseline in the lines without HNF4G | 0.052 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[PELI2]] | B | PELI2 activity strengthens ARHGAP42's drug response | lines that do not express PELI2 (10) vs lines expressing it (26) | the lines without PELI2 respond 0.85× as strongly (z diff +1.08); strongest at Idarubicin (hydrochloride) 5 µM: 0.72x vs 0.50x (z diff +3.0) | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28; target measured in part of the lines; artifact flags |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF549]] | B | ARHGAP42 activity lowers ZNF549's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 3.18× higher at baseline in the lines without ARHGAP42 | 0.016 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[BMP2]] | B | ARHGAP42 activity raises BMP2's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without ARHGAP42 | 0.036 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[GATA6]] | B | ARHGAP42 activity raises GATA6's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 3.18× lower at baseline in the lines without ARHGAP42 | 0.039 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[PTPRR]] | B | ARHGAP42 activity raises PTPRR's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.75× lower at baseline in the lines without ARHGAP42 | 0.044 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[GALNT5]] | B | ARHGAP42 activity raises GALNT5's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 3.70× lower at baseline in the lines without ARHGAP42 | 0.052 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[SLCO3A1]] | B | ARHGAP42 activity raises SLCO3A1's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.67× lower at baseline in the lines without ARHGAP42 | 0.056 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[ATP1B1]] | B | ARHGAP42 activity raises ATP1B1's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without ARHGAP42 | 0.056 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[NHS]] | B | ARHGAP42 activity raises NHS's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.89× lower at baseline in the lines without ARHGAP42 | 0.062 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[GLRX]] | B | ARHGAP42 activity weakens GLRX's drug response | lines that do not express ARHGAP42 (7) vs lines expressing it (33) | the lines without ARHGAP42 respond 1.36× as strongly (z diff -1.80); strongest at Cobimetinib 5 µM: 0.38x vs 0.65x (z diff -3.6) | 0.068 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TNFRSF21]] | B | ARHGAP42 activity raises TNFRSF21's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without ARHGAP42 | 0.082 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[SH3RF1]] | B | ARHGAP42 activity raises SH3RF1's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without ARHGAP42 | 0.089 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[ALCAM]] | B | ARHGAP42 activity raises ALCAM's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without ARHGAP42 | 0.090 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 19.2); signed map (46.2, 14.8). **Vector** length 131, 40.8% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.0 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.2 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.1 | +3.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.5 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.7 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.1 — chr11:100,687,288-100,993,941 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32810, GRAF3, AD031; previously TMEM133 |
| Gene groups (HGNC) | AH/BAR family Rho GTPase activating proteins; SH3 domain containing |
| Reactome | 8 pathways, smallest: RAC2 GTPase cycle; RAC3 GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NI28](https://www.uniprot.org/uniprotkb/A6NI28) (Rho GTPase-activating protein 42):

> May influence blood pressure by functioning as a GTPase-activating protein for RHOA in vascular smooth muscle.

**Summary**, from NCBI Gene [143872](https://www.ncbi.nlm.nih.gov/gene/143872):

> This gene encodes a Rho GTPase-activating protein (RhoGAP), and member of the GRAF or BAR-PH family of proteins. Expression of this gene is enriched in vascular smooth muscle cells and the encoded protein inhibits RhoA activity to regulate vascular tone and control blood pressure. A mutation in the first intron of this gene modulates its expression and is associated with reduced blood pressure in human patients with borderline hypertension. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:26545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26545) · Entrez [143872](https://www.ncbi.nlm.nih.gov/gene/143872) · UniProt [A6NI28](https://www.uniprot.org/uniprotkb/A6NI28) · Ensembl [ENSG00000165895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165895)

## Data

Gene col 9201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9201); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9201]; `tensor/DDL_lfc|DDL_z.npy` [9201]; `embed/gene_vectors.npy` [9201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9201 or target_col == 9201). Every well: [[ARHGAP42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
