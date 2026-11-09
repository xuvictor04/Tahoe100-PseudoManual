---
symbol: "PFKFB2"
type: "gene"
col: 4461
ensembl_id: "ENSG00000123836"
name: "6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 2"
location: "1q32.1"
module: 126
arm: "+"
pooled_cpm: 22.56
n_lines_expressing: 49
n_dd_up: 34
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# PFKFB2

*6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.40× (z +20.8, q 0e+00, up in 34 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +15.5, q 0e+00, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Larotrectinib (drug)]] 5 µM: 0.861× (z -3.6, q 0.066, down in 11 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0919×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YOD1]] (+0.56, fdr 2e-05, ⚠ same locus), [[AP1G2-AS1]] (+0.56, fdr 2e-05), [[RYR2]] (+0.53, fdr 2e-04), [[CTC1]] (+0.51, fdr 5e-04); moves opposite to [[TMEM11]] (-0.53, fdr 4e-05), [[POP7]] (-0.49, fdr 1e-04), [[ISCA2]] (-0.49, fdr 4e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DSC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.40×** | +20.8 | 0e+00 | 34/37 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.57×** | +20.8 | 0e+00 | 28/30 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +17.6 | 0e+00 | 33/34 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +15.5 | 0e+00 | 32/45 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +13.9 | 7e-42 | 35/44 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.38×** | +7.7 | 1e-12 | 23/47 (PANC-1, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +6.6 | 3e-09 | 26/46 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.5 | 5e-09 | 23/39 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.2 | 3e-08 | 25/45 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 1e-07 | 23/46 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.6 | 1e-06 | 21/45 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 1e-06 | 22/45 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +5.5 | 2e-06 | 22/46 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.3 | 5e-06 | 19/46 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +4.5 | 3e-04 | 16/46 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 7e-04 | 13/46 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 8e-04 | 12/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Berbamine (drug)]] 5 µM |  | 1.19× | +4.1 | 0.001 | 12/48 (HT-29, COLO 205, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.002 | 15/47 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.007 | 15/45 (Panc 03.27, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.010 | 10/44 (NCI-H1573, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.018 | 4/47 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4461.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0919×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | 0.861× | -3.6 | 0.066 | 11/47 (COLO 205, LS 180, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **0.801×** | -3.6 | 0.066 | 11/46 (CHP-212, J82, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.812×** | -3.6 | 0.066 | 3/46 (RPMI-7951, KATO III, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 0.866× | -3.0 | 0.37 | 4/48 (NCI-H2122, C32, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 16.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.33× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 17.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +12.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 49.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 27.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.11× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +11.5) | — |
| [[A-427 (line)]] | wt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +13.9) | — |
| [[A549 (line)]] | wt | 9.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.64× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 12.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.45× (z +9.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0919× (z -10.2) |
| [[HT-29 (line)]] | alt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.2) | — |
| [[J82 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 139 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 15 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YOD1]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[AP1G2-AS1]] | +0.56 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[RYR2]] | +0.53 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[HFM1]] | +0.51 | +0.18 / +0.56 | ⚠ one half (not replicated) | 9e-04 |  |
| [[CTC1]] | +0.51 | +0.24 / +0.63 | both halves | 5e-04 |  |
| [[SNHG22]] | +0.51 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[RMRP]] | +0.50 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[CROCC]] | +0.50 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[LINC01090]] | +0.49 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[UBQLN4]] | +0.49 | +0.29 / +0.53 | both halves | 2e-04 |  |
| [[ZC3H3]] | +0.48 | +0.15 / +0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[KLHL21]] | +0.47 | +0.48 / +0.36 | both halves | 9e-05 |  |
| [[TNS2-AS1]] | +0.47 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[TPP1]] | +0.47 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[LSS]] | +0.47 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[POP7]] | -0.49 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[ISCA2]] | -0.49 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[ABT1]] | -0.48 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[MTF2]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[AGGF1]] | -0.47 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[GPATCH11]] | -0.47 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[MTLN]] ⚠ | -0.47 | -0.24 / -0.49 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CEBPZ]] | -0.46 | -0.22 / -0.55 | both halves | 6e-04 |  |
| [[TOMM70]] | -0.46 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[FBXO45]] | -0.46 | -0.21 / -0.50 | both halves | 6e-04 |  |
| [[PRPF4]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[SDHAF1]] | -0.45 | -0.24 / -0.47 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSC2]] | B | DSC2 activity raises PFKFB2's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without DSC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[COL17A1]] | B | COL17A1 activity raises PFKFB2's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without COL17A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.461). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.8, 23.3); signed map (32.6, -20.1). **Vector** length 89.7, 18.9% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.4 | +20.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.0 | +20.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +17.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +13.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.1 | +7.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +0.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.2 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.8 | -3.6 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:207,034,366-207,081,024 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase family |
| Reactome | 4 pathways, smallest: Regulation of glycolysis by fructose 2,6-bisphosphate metabolism; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O60825](https://www.uniprot.org/uniprotkb/O60825) (6-phosphofructo-2-kinase/fructose-2,6-bisphosphatase 2):

> Synthesis and degradation of fructose 2,6-bisphosphate.

**Summary**, from NCBI Gene [5208](https://www.ncbi.nlm.nih.gov/gene/5208):

> The protein encoded by this gene is involved in both the synthesis and degradation of fructose-2,6-bisphosphate, a regulatory molecule that controls glycolysis in eukaryotes. The encoded protein has a 6-phosphofructo-2-kinase activity that catalyzes the synthesis of fructose-2,6-bisphosphate, and a fructose-2,6-biphosphatase activity that catalyzes the degradation of fructose-2,6-bisphosphate. This protein regulates fructose-2,6-bisphosphate levels in the heart, while a related enzyme encoded …

**Accessions** — [HGNC:8873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8873) · Entrez [5208](https://www.ncbi.nlm.nih.gov/gene/5208) · UniProt [O60825](https://www.uniprot.org/uniprotkb/O60825) · Ensembl [ENSG00000123836](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123836)

## Data

Gene col 4461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4461); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4461]; `tensor/DDL_lfc|DDL_z.npy` [4461]; `embed/gene_vectors.npy` [4461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4461 or target_col == 4461). Every well: [[PFKFB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFKFB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
