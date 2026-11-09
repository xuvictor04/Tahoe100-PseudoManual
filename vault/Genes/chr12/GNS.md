---
symbol: "GNS"
type: "gene"
col: 5739
ensembl_id: "ENSG00000135677"
name: "glucosamine (N-acetyl)-6-sulfatase"
location: "12q14.3"
module: 29
arm: "+"
pooled_cpm: 73.43
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# GNS

*glucosamine (N-acetyl)-6-sulfatase* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +12.1, q 8e-31, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +10.1, q 2e-21, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.651× (z -6.7, q 1e-08, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMP2]] (+0.84, fdr 7e-06), [[LAMP1]] (+0.83, fdr 7e-06), [[TPP1]] (+0.82, fdr 7e-06); moves opposite to [[EIF5B]] (-0.61, fdr 4e-05), [[ZNF593]] (-0.60, fdr 1e-04), [[BRIX1]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LGALS3BP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +12.1 | 8e-31 | 46/49 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +11.2 | 2e-26 | 40/43 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.1 | 2e-21 | 39/49 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +9.9 | 5e-21 | 46/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +9.7 | 4e-20 | 44/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +7.7 | 1e-12 | 32/45 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +7.7 | 2e-12 | 43/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +6.0 | 1e-07 | 29/48 (CFPAC-1, SW1417, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.5 | 3e-06 | 36/48 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.4 | 3e-06 | 2/49 (MIA PaCa-2, HOP62) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.3 | 7e-06 | 31/50 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +5.1 | 2e-05 | 41/49 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.9 | 4e-05 | 23/48 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.6 | 2e-04 | 26/48 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 5e-04 | 30/48 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.001 | 26/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.004 | 21/48 (SW480, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.010 | 22/48 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.011 | 19/48 (SW1417, BT-474, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.016 | 22/50 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.651×** | -6.7 | 1e-08 | 36/49 (C32, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.8 | 0.030 | 25/48 (AN3 CA, SK-MEL-2, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.722×** | -3.8 | 0.030 | 21/48 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.866× | -3.3 | 0.10 | 20/49 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.866× | -3.3 | 0.10 | 11/48 (MIA PaCa-2, Hs 766T, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.828× | -3.1 | 0.20 | 17/48 (RKO, HT-29, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 29.2 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.4) | — |
| [[LoVo (line)]] | wt | 50.7 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 53.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.33× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 119 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 79.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +11.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 68.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.4) | — |
| [[A498 (line)]] | wt | 94.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 63.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +10.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 54.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.23× (z +8.6) | — |
| [[J82 (line)]] | alt | 90.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 49.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 59.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 79.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +8.6) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.455× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 58.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 53.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.73× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 80.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 54.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.23× (z +8.8) | — |
| [[C32 (line)]] | wt | 110 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.318× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 67.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 53.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.105× (z -9.8) |
| [[Hs 766T (line)]] | wt | 48.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 75.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 72.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 54.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 84.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 82.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.11× (z +9.0) | — |
| [[SW 1088 (line)]] | alt | 89.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0473× (z -10.3) |
| [[SW1417 (line)]] | alt | 54.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.2) | — |
| [[A-172 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 99.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP2]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 | STRING 426 |
| [[LAMP1]] | +0.83 | +0.80 / +0.81 | both halves | 7e-06 | STRING 433 |
| [[TPP1]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 | STRING 622 |
| [[ATP6AP1]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SCARB2]] | +0.73 | +0.63 / +0.77 | both halves | 7e-06 | STRING 503 |
| [[PIGT]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[GRN]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 | STRING 442 |
| [[FKBP9]] | +0.67 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[ERLIN2]] | +0.67 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[IGF2R]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | pathway: trans-Golgi Network Vesicle Budding |
| [[GBA1]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PPT1]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5B]] | -0.61 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[ZNF593]] | -0.60 | -0.34 / -0.67 | both halves | 1e-04 |  |
| [[BRIX1]] | -0.58 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[RBM25]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[NSUN5P2-1]] ⚠ | -0.57 | -0.44 / -0.55 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PPP1R35]] ⚠ | -0.57 | -0.35 / -0.62 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXO45]] | -0.56 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[IWS1]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[PRPF38B]] | -0.55 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[KCNK6]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MRPL46]] | -0.53 | -0.20 / -0.60 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3BP]] | B | LGALS3BP activity strengthens GNS's drug response | lines that do not express LGALS3BP (7) vs lines expressing it (42) | the lines without LGALS3BP respond 0.60× as strongly (z diff +1.40); strongest at Dinaciclib 5 µM: 1.47x vs 2.14x (z diff +2.8) | 0.060 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-21.9, -20.6); signed map (-23.9, -36.3). **Vector** length 127, 39.8% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +11.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.5 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +7.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.5 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.9 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.3 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -4.8 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.3 | -6.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | glucosamine (N-acetyl)-6-sulfatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:64,713,445-64,759,431 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 13 pathways, smallest: Keratan sulfate degradation; Mucopolysaccharidoses; Keratan sulfate/keratin metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P15586](https://www.uniprot.org/uniprotkb/P15586) (N-acetylglucosamine-6-sulfatase):

> Hydrolyzes 6-sulfate groups in N-acetyl-d-glucosaminide units of heparin sulfate and keratan sulfate.

**Summary**, from NCBI Gene [2799](https://www.ncbi.nlm.nih.gov/gene/2799):

> The product of this gene is a lysosomal enzyme found in all cells. It is involved in the catabolism of heparin, heparan sulphate, and keratan sulphate. Deficiency of this enzyme results in the accumulation of undegraded substrate and the lysosomal storage disorder mucopolysaccharidosis type IIID (Sanfilippo D syndrome). Mucopolysaccharidosis type IIID is the least common of the four subtypes of Sanfilippo syndrome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4422) · Entrez [2799](https://www.ncbi.nlm.nih.gov/gene/2799) · UniProt [P15586](https://www.uniprot.org/uniprotkb/P15586) · Ensembl [ENSG00000135677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135677)

## Data

Gene col 5739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5739); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5739]; `tensor/DDL_lfc|DDL_z.npy` [5739]; `embed/gene_vectors.npy` [5739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5739 or target_col == 5739). Every well: [[GNS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
