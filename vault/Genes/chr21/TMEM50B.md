---
symbol: "TMEM50B"
type: "gene"
col: 6604
ensembl_id: "ENSG00000142188"
name: "transmembrane protein 50B"
location: "21q22.11"
module: 40
arm: "+"
pooled_cpm: 42.93
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# TMEM50B

*transmembrane protein 50B* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.17× (z +13.8, q 2e-40, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.651× (z -7.4, q 5e-11, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBFA2T2]] (+0.71, fdr 7e-06), [[PIK3C2A]] (+0.67, fdr 7e-06), [[GMCL1]] (+0.67, fdr 7e-06); moves opposite to [[ZNF155]] (-0.71, fdr 7e-06), [[ZNF260]] (-0.70, fdr 9e-06), [[MGA]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +13.8 | 2e-40 | 45/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +13.0 | 2e-36 | 41/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +12.1 | 3e-31 | 44/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +11.9 | 3e-30 | 47/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.6 | 1e-15 | 34/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.6 | 4e-09 | 33/49 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.00×** | +6.5 | 9e-09 | 39/48 (A-427, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.014 | 15/48 (LOX-IMVI, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +3.7 | 0.014 | 20/48 (C-33 A, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.5 | 0.027 | 21/47 (NCI-H1792, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.21×** | +3.5 | 0.029 | 17/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.057 | 8/48 (H4, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.651×** | -7.4 | 5e-11 | 34/48 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -7.4 | 5e-11 | 36/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.692×** | -6.3 | 6e-08 | 27/48 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.731×** | -5.6 | 4e-06 | 26/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.573×** | -5.2 | 2e-05 | 29/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.752×** | -5.1 | 4e-05 | 25/48 (KATO III, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.764×** | -4.8 | 1e-04 | 25/48 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -4.3 | 0.001 | 25/49 (A549, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.769×** | -4.3 | 0.001 | 22/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **0.787×** | -4.1 | 0.002 | 20/47 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.840× | -4.0 | 0.003 | 15/48 (KATO III, SW1417, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.796×** | -3.8 | 0.006 | 17/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.810×** | -3.6 | 0.012 | 16/49 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.815×** | -3.6 | 0.012 | 13/48 (J82, LS 180, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.815×** | -3.5 | 0.016 | 16/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.858× | -3.5 | 0.017 | 14/48 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.857× | -3.5 | 0.017 | 17/48 (HT-29, SW 1088, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.819×** | -3.4 | 0.017 | 15/49 (A498, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 62.2 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 28.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 83.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 27.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 31.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 43.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 51.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.7) | [[Harringtonine (drug)]] 0.5 µM 0.404× (z -8.7) |
| [[LoVo (line)]] | wt | 51.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 34.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -12.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 27.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +9.7) | [[Temsirolimus (drug)]] 0.5 µM 0.156× (z -9.6) |
| [[A498 (line)]] | wt | 51.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 54.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.174× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 32.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.5) | — |
| [[H4 (line)]] | wt | 47.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 70.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.375× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 54.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.7) | — |
| [[SW480 (line)]] | alt | 40.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.1) | — |
| [[A-427 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | +0.71 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PIK3C2A]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[IFI27L1]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.66 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[MAX]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SGK3]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CRELD2]] | +0.65 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ZNF710-AS1]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[KDELR1]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[GPR107]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[SRP54-AS1]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF155]] | -0.71 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[ZNF260]] | -0.70 | -0.57 / -0.68 | both halves | 9e-06 |  |
| [[MGA]] | -0.70 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[ZNF268]] | -0.68 | -0.61 / -0.71 | both halves | 7e-06 |  |
| [[ZNF317]] | -0.68 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[RIF1]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NOL11]] | -0.67 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.67 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[COA7]] | -0.67 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[ZC3H4]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[CSTF2T]] | -0.66 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[RPL7L1]] | -0.66 | -0.57 / -0.65 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM50B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TSPYL5]] | B | TSPYL5 activity lowers TMEM50B's level | lines that do not express TSPYL5 (36) vs lines expressing it (14) | 1.21× higher at baseline in the lines without TSPYL5 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000241168, LINC02999, LINC01205 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-31.9, 11.9); signed map (-42.8, 13.4). **Vector** length 113, 29.0% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +13.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +12.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +13.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +11.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +3.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.0 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.0 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.7 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -6.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.9 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 50B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,432,485-33,479,974 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C21orf4 |
| Matched by | ensembl_id |

UniProt [P56557](https://www.uniprot.org/uniprotkb/P56557) carries no function annotation.

**Summary**, from NCBI Gene [757](https://www.ncbi.nlm.nih.gov/gene/757):

> Predicted to be involved in late endosome to vacuole transport via multivesicular body sorting pathway. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1280) · Entrez [757](https://www.ncbi.nlm.nih.gov/gene/757) · UniProt [P56557](https://www.uniprot.org/uniprotkb/P56557) · Ensembl [ENSG00000142188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142188)

## Data

Gene col 6604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6604); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6604]; `tensor/DDL_lfc|DDL_z.npy` [6604]; `embed/gene_vectors.npy` [6604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6604 or target_col == 6604). Every well: [[TMEM50B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM50B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
