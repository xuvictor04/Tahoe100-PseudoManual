---
symbol: "FSTL3"
type: "gene"
col: 948
ensembl_id: "ENSG00000070404"
name: "follistatin like 3"
location: "19p13.3"
module: 98
arm: "+"
pooled_cpm: 16.79
n_lines_expressing: 43
n_dd_up: 54
n_dd_down: 13
n_dd_up_clean: 45
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# FSTL3

*follistatin like 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 54 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.75× (z +17.0, q 0e+00, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.428× (z -7.8, q 5e-12, down in 28 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROS1]] (+0.68, fdr 7e-06), [[CDV3]] (+0.65, fdr 7e-06), [[MAFB]] (+0.64, fdr 1e-05); moves opposite to [[AP3M2]] (-0.54, fdr 3e-05), [[RNF168]] (-0.53, fdr 2e-05), [[INTS4]] (-0.51, fdr 3e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SYNPO]] → it (grade B ⚠); 5 go from it, the strongest it → [[PIEZO1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 54 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.75×** | +17.0 | 0e+00 | 31/41 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **4.89×** | +13.9 | 3e-41 | 33/40 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +10.2 | 2e-22 | 26/32 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +9.7 | 6e-20 | 19/23 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +8.8 | 2e-16 | 29/38 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.50×** | +8.3 | 9e-15 | 33/40 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.25×** | +6.9 | 3e-10 | 24/41 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.07×** | +6.4 | 1e-08 | 25/39 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +6.0 | 1e-07 | 17/27 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +5.7 | 7e-07 | 22/40 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.70×** | +5.6 | 9e-07 | 22/40 (NCI-H460, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.85×** | +5.6 | 1e-06 | 25/40 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.83×** | +5.5 | 2e-06 | 23/39 (A498, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.77×** | +5.0 | 3e-05 | 23/39 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.71×** | +4.8 | 5e-05 | 20/39 (A498, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.71×** | +4.8 | 5e-05 | 26/37 (A498, AsPC-1, …) | two highest doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.07×** | +4.7 | 9e-05 | 22/37 (LS 180, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.62×** | +4.6 | 1e-04 | 18/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.67×** | +4.5 | 2e-04 | 18/40 (A-172, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.428×** | -7.8 | 5e-12 | 28/40 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.500×** | -6.1 | 3e-07 | 27/39 (A-427, LoVo, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.281×** | -6.1 | 3e-07 | 25/38 (Hs 766T, H4, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.535×** | -5.7 | 1e-06 | 23/40 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.557×** | -5.4 | 9e-06 | 23/41 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.626×** | -4.1 | 0.004 | 19/40 (A-172, A498, …) | inconsistent across doses | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | **0.632×** | -4.1 | 0.004 | 20/40 (A-427, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Rifaximin (drug)]] 0.5 µM |  | **0.645×** | -4.0 | 0.004 | 22/40 (hTERT-HPNE, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.466×** | -3.7 | 0.016 | 17/40 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.666×** | -3.6 | 0.019 | 14/39 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.785×** | -3.2 | 0.080 | 13/41 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.520×** | -3.1 | 0.084 | 13/41 (LoVo, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.05 µM |  | **0.716×** | -3.1 | 0.094 | 11/39 (SW 900, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.706× | -3.0 | 0.10 | 13/40 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 0.05 µM |  | 0.678× | -3.0 | 0.10 | 9/40 (SW480, SW48, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.8 | 16 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +24.4) | — |
| [[A-172 (line)]] | wt | 109 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +30.0) | — |
| [[A549 (line)]] | wt | 20.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +18.9) | — |
| [[PANC-1 (line)]] | alt | 9.74 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 59.2× (z +31.6) | — |
| [[LoVo (line)]] | wt | 40.6 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.115× (z -13.4) |
| [[SNU-423 (line)]] | alt | 11.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +14.8) | — |
| [[HEC-1-A (line)]] | alt | 4.89 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 61.0× (z +19.3) | — |
| [[HepG2_C3A (line)]] | wt | 74.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +22.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.91 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 20.5× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 18.4× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.0346× (z -14.5) |
| [[A-427 (line)]] | wt | 18.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.08× (z +9.3) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +16.7) | — |
| [[CFPAC-1 (line)]] | alt | 5.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 72.1× (z +19.4) | — |
| [[HOP62 (line)]] | alt | 16.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0192× (z -11.2) |
| [[J82 (line)]] | alt | 19.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +22.3) | — |
| [[KATO III (line)]] | alt | 6.75 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 22.6× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.163× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 6.83 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 7.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.8× (z +17.5) | — |
| [[CHP-212 (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 8.94 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.69× (z +9.6) | — |
| [[RKO (line)]] | wt | 9.13 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0721× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 11.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 53.5× (z +12.9) | — |
| [[SW 900 (line)]] | alt | 7.78 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 16.7× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROS1]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[CDV3]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MAFB]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[BCL9L]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CUX1]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[HACD1]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FOSL2]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ADPRHL1]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[MT1M]] | +0.57 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[DGKH]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CFLAR]] | +0.57 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[CAV1]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3M2]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[RNF168]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[INTS4]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[WWTR1]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 | pathway: Signaling by TGFB family members |
| [[CCNJL]] | -0.49 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ETV5]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TCP10L]] | -0.49 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[NIF3L1]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SLC46A3]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[NUDT21]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[OTUB2]] | -0.46 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[ARMC9]] | -0.46 | -0.37 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNPO]] | B | SYNPO activity raises FSTL3's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.49× lower at baseline in the lines without SYNPO | 0.031 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FSTL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIEZO1]] | B | FSTL3 activity raises PIEZO1's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without FSTL3 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |
| [[AMOTL2]] | B | FSTL3 activity raises AMOTL2's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without FSTL3 | 0.045 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |
| [[TMEM43]] | B | FSTL3 activity raises TMEM43's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without FSTL3 | 0.071 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |
| [[CDV3]] | B | FSTL3 activity raises CDV3's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.21× lower at baseline in the lines without FSTL3 | 0.082 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |
| [[FOXN2]] | B | FSTL3 activity raises FOXN2's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without FSTL3 | 0.088 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.2, 13.9); signed map (20.0, 28.7). **Vector** length 125, 36.4% of its response variance represented; |z| ≥ 3 in 1,249 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +8.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.3 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.2 | +4.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.7 | +5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.7 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.3 | +4.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.2 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -6.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -0.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | follistatin like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:676,392-683,392 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLRG, FSRP |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: Antagonism of Activin by Follistatin; Signaling by Activin; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95633](https://www.uniprot.org/uniprotkb/O95633) (Follistatin-related protein 3):

> Isoform 1 or the secreted form is a binding and antagonizing protein for members of the TGF-beta family, such as activin, BMP2 and MSTN. Inhibits activin A-, activin B-, BMP2- and MSDT-induced cellular signaling; more effective on activin A than on activin B. Involved in bone formation; inhibits osteoclast differentiation. Involved in hematopoiesis; involved in differentiation of hemopoietic progenitor cells, increases hematopoietic cell adhesion to fibronectin and seems to contribute to the …

**Summary**, from NCBI Gene [10272](https://www.ncbi.nlm.nih.gov/gene/10272):

> Follistatin-like 3 is a secreted glycoprotein of the follistatin-module-protein family. It may have a role in leukemogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3973) · Entrez [10272](https://www.ncbi.nlm.nih.gov/gene/10272) · UniProt [O95633](https://www.uniprot.org/uniprotkb/O95633) · Ensembl [ENSG00000070404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070404)

## Data

Gene col 948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 948); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 948]; `tensor/DDL_lfc|DDL_z.npy` [948]; `embed/gene_vectors.npy` [948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 948 or target_col == 948). Every well: [[FSTL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSTL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
