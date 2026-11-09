---
symbol: "ZNF815P"
type: "gene"
col: 14049
ensembl_id: "ENSG00000235944"
name: "zinc finger protein 815, pseudogene"
location: "7p22.1"
module: 191
arm: "+"
pooled_cpm: 2.69
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# ZNF815P

*zinc finger protein 815, pseudogene* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 11.4× (z +21.8, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.374× (z -8.8, q 7e-16, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNG7]] (+0.60, fdr 1e-05), [[COL26A1]] (+0.57, fdr 7e-06), [[MAP4K2]] (+0.55, fdr 5e-04); moves opposite to [[RAB28]] (-0.58, fdr 4e-05), [[ATR]] (-0.55, fdr 1e-04), [[SNTB2]] (-0.54, fdr 8e-05).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC88B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **11.4×** | +21.8 | 0e+00 | 42/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.25×** | +18.3 | 0e+00 | 27/33 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.46×** | +18.0 | 0e+00 | 40/43 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.68×** | +11.7 | 3e-29 | 36/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +10.6 | 5e-24 | 22/33 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +8.8 | 2e-16 | 25/44 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.6 | 2e-12 | 2/2 (A498, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +7.6 | 3e-12 | 17/31 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.13×** | +6.8 | 9e-10 | 17/44 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +6.5 | 5e-09 | 13/38 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.2 | 4e-08 | 8/15 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.99×** | +6.2 | 4e-08 | 17/45 (A498, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +4.9 | 5e-05 | 11/37 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.77×** | +4.8 | 7e-05 | 8/39 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +4.6 | 2e-04 | 3/5 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.004 | 9/39 (HEC-1-A, SW48, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.030 | 1/42 (SW 900) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.031 | 0/47 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.374×** | -8.8 | 7e-16 | 26/46 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.470×** | -6.8 | 4e-09 | 23/41 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.475×** | -6.7 | 4e-09 | 19/41 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.592×** | -4.7 | 4e-04 | 14/37 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.613×** | -4.1 | 0.004 | 9/41 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **0.735×** | -3.9 | 0.009 | 14/43 (C-33 A, C32, …) | top dose only |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.677×** | -3.2 | 0.081 | 8/38 (LoVo, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.698×** | -3.2 | 0.081 | 11/23 (SHP-77, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.699×** | -3.2 | 0.081 | 11/45 (A-172, C-33 A, …) | all doses, stronger at high dose |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **0.703×** | -3.2 | 0.088 | 6/30 (LoVo, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.48 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 189× (z +21.9) | — |
| [[A549 (line)]] | wt | 1.96 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 135× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 4.58 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +11.7) | — |
| [[KATO III (line)]] | alt | 3.55 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 70.6× (z +12.9) | — |
| [[A498 (line)]] | wt | 3.42 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 24.4× (z +12.1) | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 29.7× (z +9.4) | — |
| [[A-427 (line)]] | wt | 2.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0369× (z -9.2) |
| [[H4 (line)]] | wt | 2.65 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 121× (z +9.6) | — |
| [[LoVo (line)]] | wt | 1.86 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 25.3× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 3.61 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 13.3× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.95 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0307× (z -9.6) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 2.83 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.1× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 1.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.6× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 1.32 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 71.1× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 5.01 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 38.9× (z +10.7) | — |
| [[A-172 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.737 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG7]] | +0.60 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[COL26A1]] | +0.57 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[MAP4K2]] | +0.55 | +0.23 / +0.65 | both halves | 5e-04 |  |
| [[SUGT1P4-STRA6LP]] | +0.54 | +0.40 / +0.42 | both halves | 4e-05 |  |
| [[TMC3-AS1]] | +0.54 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[LINC00888-1]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[VAV1]] | +0.53 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[TBCE]] | +0.53 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[CCDC88B]] | +0.52 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[SPTBN4]] | +0.52 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[KLKP1-1]] | +0.52 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LINC00624]] | +0.52 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB28]] | -0.58 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ATR]] | -0.55 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[SNTB2]] | -0.54 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[C2CD3]] | -0.52 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[FBXW7]] | -0.51 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[NR2C2]] | -0.51 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[SNRPB]] | -0.50 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[E2F3]] | -0.50 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[TMEM11-DT]] | -0.50 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[PKP4]] | -0.48 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[TOR1A]] | -0.48 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[LRRC69]] | -0.47 | -0.42 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC88B]] | B | CCDC88B activity raises ZNF815P's level | lines that do not express CCDC88B (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without CCDC88B | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: TSPAN15, ENSG00000287306; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.9, 4.8); signed map (25.9, 17.2). **Vector** length 55.6, 7.73% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +18.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +0.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 815, pseudogene |
| Locus type | pseudogene |
| Location | 7p22.1 — chr7:5,823,207-5,847,743 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ38969; previously ZNF815 |
| Matched by | ensembl_id |

UniProt [A8K554](https://www.uniprot.org/uniprotkb/A8K554) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22029) · Entrez [401303](https://www.ncbi.nlm.nih.gov/gene/401303) · UniProt [A8K554](https://www.uniprot.org/uniprotkb/A8K554) · Ensembl [ENSG00000235944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235944)

## Data

Gene col 14049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14049); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14049]; `tensor/DDL_lfc|DDL_z.npy` [14049]; `embed/gene_vectors.npy` [14049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14049 or target_col == 14049). Every well: [[ZNF815P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF815P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
