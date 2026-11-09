---
symbol: "PHF8"
type: "gene"
col: 10321
ensembl_id: "ENSG00000172943"
name: "PHD finger protein 8"
location: "Xp11.22"
module: 26
arm: "+"
pooled_cpm: 48.99
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PHF8

*PHD finger protein 8* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.38× (z +16.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.741× (z -5.6, q 1e-05, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKT1S1]] (+0.76, fdr 1e-05), [[FBXL19-AS1]] (+0.72, fdr 2e-05), [[ATN1]] (+0.67, fdr 9e-05); moves opposite to [[DENND6A]] (-0.66, fdr 1e-05), [[NDUFA12]] (-0.66, fdr 4e-05), [[SLC15A4]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.38×** | +16.1 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +15.0 | 0e+00 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +10.6 | 5e-24 | 37/48 (HOP62, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +10.5 | 2e-23 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +9.9 | 3e-21 | 42/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.9 | 5e-17 | 36/47 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.2 | 3e-14 | 34/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +7.2 | 5e-11 | 31/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.9 | 3e-10 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +5.9 | 3e-07 | 30/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.6 | 9e-07 | 24/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 4e-05 | 23/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.6 | 2e-04 | 24/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 6e-04 | 19/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.001 | 22/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.741×** | -5.6 | 1e-05 | 30/48 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.746×** | -5.5 | 1e-05 | 27/48 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.749×** | -5.4 | 1e-05 | 25/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -5.1 | 5e-05 | 25/48 (SHP-77, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -3.7 | 0.022 | 21/48 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.832×** | -3.4 | 0.053 | 19/47 (A-427, SHP-77, …) | inconsistent across doses | composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.716×** | -3.3 | 0.088 | 14/48 (SNU-423, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.887× | -3.2 | 0.097 | 13/48 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -3.1 | 0.11 | 15/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.850× | -3.1 | 0.12 | 15/48 (NCI-H1573, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 56.9 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +20.3) | — |
| [[HOP62 (line)]] | alt | 53.8 | 7 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.51× (z +16.1) | [[Lonafarnib (drug)]] 5 µM 0.220× (z -8.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 88.7 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +13.8) | [[Lonafarnib (drug)]] 5 µM 0.237× (z -10.3) ⚠ toxic |
| [[LoVo (line)]] | wt | 51.8 | 4 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.412× (z -10.3) |
| [[KATO III (line)]] | alt | 62.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 47.2 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 51.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.4) | — |
| [[RKO (line)]] | wt | 83.3 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A498 (line)]] | wt | 26.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +15.8) | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.95× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 66.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.58× (z +15.4) | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 39.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 54.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 65.6 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.6) | — |
| [[A-172 (line)]] | wt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[A-427 (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A549 (line)]] | wt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +15.4) | — |
| [[C-33 A (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -14.1) ⚠ toxic |
| [[C32 (line)]] | wt | 47.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.74× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 50.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 50.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 48.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 55.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.205× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 61.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 160 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1S1]] | +0.76 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | +0.72 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ATN1]] | +0.67 | +0.37 / +0.67 | both halves | 9e-05 |  |
| [[PHF2]] | +0.66 | +0.40 / +0.60 | both halves | 5e-05 | same gene group; pathway: Chromatin modifying enzymes; STRING 512 |
| [[CCDC90B-AS1]] | +0.64 | +0.44 / +0.28 | both halves | 3e-04 |  |
| [[KMT2E-AS1]] | +0.64 | +0.53 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[HCFC1]] | +0.63 | +0.41 / +0.48 | both halves | 4e-05 | pathway: Chromatin modifying enzymes; STRING 970 |
| [[EFCAB2]] | +0.62 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[GALNT7-DT]] | +0.62 | +0.37 / +0.27 | both halves | 3e-04 |  |
| [[ATXN1L]] | +0.62 | +0.40 / +0.32 | both halves | 2e-04 | STRING 623 |
| [[SETD1B]] | +0.61 | +0.46 / +0.30 | both halves | 2e-04 | pathway: Chromatin modifying enzymes; STRING 583 |
| [[PTOV1-AS1]] | +0.61 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[C2orf49-DT]] | +0.61 | +0.41 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND6A]] | -0.66 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[NDUFA12]] | -0.66 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SLC15A4]] | -0.66 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[STX7]] | -0.65 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[LCMT1]] | -0.62 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[YIF1B]] | -0.62 | -0.46 / -0.26 | both halves | 4e-04 |  |
| [[MMS19]] | -0.62 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[HEATR6]] | -0.62 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[VEZT]] | -0.60 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[TBCB]] | -0.60 | -0.51 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[HEATR5B]] | -0.60 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[NBPF3]] | -0.60 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[TAMM41]] | -0.59 | -0.49 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PHF8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PHF8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.3, 12.2); signed map (23.8, -4.6). **Vector** length 85.4, 19.5% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +4.8 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +15.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +0.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.6 | -0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | -0.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:53,936,676-54,048,958 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF422, KIAA1111, JHDM1F, KDM7B |
| Gene groups (HGNC) | PHD finger proteins; Lysine demethylase 7 family |
| Reactome | 8 pathways, smallest: HDMs demethylate histones; Condensation of Prophase Chromosomes; Mitotic Prophase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPP1](https://www.uniprot.org/uniprotkb/Q9UPP1) (Histone lysine demethylase PHF8):

> Histone lysine demethylase with selectivity for mono- and dimethylated residues. It plays an essential role in cell cycle progression and rDNA transcription. Demethylates mono- and dimethylated histone H3 'Lys-9' residue (H3K9Me1 and H3K9Me2) and monomethylated histone H4 'Lys-20' residue (H4K20Me1). Acts as a transcription activator as H3K9Me1, H3K9Me2, H3K27Me2 and H4K20Me1 are epigenetic repressive marks. Displays a very low intrinsic activity toward dimethylated H3 'Lys-27' (H3K27Me2). May …

**Summary**, from NCBI Gene [23133](https://www.ncbi.nlm.nih.gov/gene/23133):

> The protein encoded by this gene is a histone lysine demethylase that preferentially acts on histones in the monomethyl or dimethyl states. The encoded protein requires Fe(2+) ion, 2-oxoglutarate, and oxygen for its catalytic activity. The protein has an N-terminal PHD finger and a central Jumonji C domain. This gene is thought to function as a transcription activator. Defects in this gene are a cause of syndromic X-linked Siderius type intellectual disability (MRXSSD) and over-expression of …

**Accessions** — [HGNC:20672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20672) · Entrez [23133](https://www.ncbi.nlm.nih.gov/gene/23133) · UniProt [Q9UPP1](https://www.uniprot.org/uniprotkb/Q9UPP1) · Ensembl [ENSG00000172943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172943)

## Data

Gene col 10321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10321); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10321]; `tensor/DDL_lfc|DDL_z.npy` [10321]; `embed/gene_vectors.npy` [10321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10321 or target_col == 10321). Every well: [[PHF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
