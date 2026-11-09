---
symbol: "NSDHL"
type: "gene"
col: 7175
ensembl_id: "ENSG00000147383"
name: "NAD(P) dependent 3-beta-hydroxysteroid dehydrogenase NSDHL"
location: "Xq28"
module: 86
arm: "+"
pooled_cpm: 16.55
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# NSDHL

*NAD(P) dependent 3-beta-hydroxysteroid dehydrogenase NSDHL* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 1.55× (z +11.4, q 2e-27, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.493× (z -18.4, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSMO1]] (+0.74, fdr 7e-06), [[HMGCR]] (+0.69, fdr 7e-06), [[TIMM10B]] (+0.68, fdr 7e-06); moves opposite to [[LINC02340]] (-0.59, fdr 7e-06), [[APLF]] (-0.58, fdr 1e-05), [[PIM3]] (-0.57, fdr 1e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BCAP31]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **1.55×** | +11.4 | 2e-27 | 31/48 (NCI-H2030, HOP62, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +11.3 | 3e-27 | 36/48 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.53×** | +11.2 | 7e-27 | 38/48 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +9.6 | 8e-20 | 32/46 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +8.4 | 3e-15 | 29/48 (SW1417, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +8.2 | 2e-14 | 33/48 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +7.8 | 5e-13 | 31/47 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +7.7 | 1e-12 | 24/36 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +7.1 | 8e-11 | 24/43 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +6.5 | 4e-09 | 23/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +5.7 | 5e-07 | 18/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.37×** | +5.6 | 9e-07 | 19/47 (A498, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.6 | 1e-06 | 20/47 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.37×** | +5.5 | 1e-06 | 18/48 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.21×** | +4.9 | 4e-05 | 18/48 (NCI-H1573, J82, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.016 | 5/48 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.020 | 6/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.028 | 7/48 (A498, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.493×** | -18.4 | 0e+00 | 41/47 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.474×** | -13.2 | 2e-37 | 39/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -8.5 | 3e-15 | 29/46 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -7.9 | 4e-13 | 29/46 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.745×** | -7.6 | 2e-12 | 29/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.689×** | -6.8 | 7e-10 | 23/46 (H4, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.692×** | -6.8 | 1e-09 | 24/46 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -6.1 | 8e-08 | 19/47 (SW480, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.757×** | -5.1 | 2e-05 | 16/48 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.759×** | -5.1 | 2e-05 | 18/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.823×** | -3.3 | 0.051 | 13/44 (C-33 A, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.841× | -3.2 | 0.071 | 8/48 (AN3 CA, A498, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.846× | -3.1 | 0.088 | 7/47 (SW1417, RKO, …) | inconsistent across doses | position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.888× | -3.1 | 0.088 | 9/48 (PANC-1, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 30.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0692× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.252× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 17.0 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 3.10× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.9) |
| [[A-172 (line)]] | wt | 17.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.269× (z -9.0) |
| [[H4 (line)]] | wt | 13.2 | 0 | 2 | — | [[CP21R7 (drug)]] 0.05 µM 0.0506× (z -10.8) |
| [[HOP62 (line)]] | alt | 17.3 | 1 | 1 | [[Cepharanthine (drug)]] 5 µM 2.39× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -14.5) |
| [[KATO III (line)]] | alt | 28.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.2) |
| [[PANC-1 (line)]] | alt | 33.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.6) |
| [[RKO (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.357× (z -8.6) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -8.7) |
| [[A498 (line)]] | wt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0911× (z -9.7) ⚠ toxic |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -11.5) |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0986× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.6) |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -8.6) |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.0) |
| [[SNU-423 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.1) |
| [[SW480 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +11.3) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSMO1]] | +0.74 | +0.79 / +0.66 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 997 |
| [[HMGCR]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 791 |
| [[TIMM10B]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[DHCR7]] | +0.67 | +0.66 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 966 |
| [[FDPS]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 832 |
| [[EFCAB14]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SCD]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[GDAP2]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ERG28]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 | STRING 912 |
| [[FDFT1]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 961 |
| [[CYP51A1]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 989 |
| [[MAN2B2]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02340]] | -0.59 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[APLF]] | -0.58 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[PIM3]] | -0.57 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SKIL]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | -0.53 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[NANOS3]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[STAT5A]] | -0.53 | -0.49 / -0.43 | both halves | 4e-05 |  |
| [[LEKR1]] | -0.53 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[CCDC125]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD26]] | -0.52 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[SGO1-AS1]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[FAM200B]] | -0.52 | -0.60 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAP31]] | C | BCAP31's natural level strengthens NSDHL's drug response | BCAP31's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.52; direction not clear | 0.067 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.8, -48.0); signed map (-52.5, 31.1). **Vector** length 104, 23.5% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.53 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.54 to 16); *Lanosterol biosynthesis* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.3 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +5.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.6 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +7.1 |
|  | [[Berbamine (drug)]] 5 µM |  | +4.3 | +11.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.9 | -18.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NAD(P) dependent 3-beta-hydroxysteroid dehydrogenase NSDHL |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:152,830,967-152,869,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XAP104, H105e3, SDR31E1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, FATTY_ACID_METABOLISM, GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway); Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15738](https://www.uniprot.org/uniprotkb/Q15738) (Sterol-4-alpha-carboxylate 3-dehydrogenase, decarboxylating):

> Catalyzes the NAD(P)(+)-dependent oxidative decarboxylation of the C4 methyl groups of 4-alpha-carboxysterols in post-squalene cholesterol biosynthesis (By similarity). Also plays a role in the regulation of the endocytic trafficking of EGFR (By similarity).

**Summary**, from NCBI Gene [50814](https://www.ncbi.nlm.nih.gov/gene/50814):

> The protein encoded by this gene is localized in the endoplasmic reticulum and is involved in cholesterol biosynthesis. Mutations in this gene are associated with CHILD syndrome, which is a X-linked dominant disorder of lipid metabolism with disturbed cholesterol biosynthesis, and typically lethal in males. Alternatively spliced transcript variants with differing 5' UTR have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13398) · Entrez [50814](https://www.ncbi.nlm.nih.gov/gene/50814) · UniProt [Q15738](https://www.uniprot.org/uniprotkb/Q15738) · Ensembl [ENSG00000147383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147383)

## Data

Gene col 7175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7175); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7175]; `tensor/DDL_lfc|DDL_z.npy` [7175]; `embed/gene_vectors.npy` [7175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7175 or target_col == 7175). Every well: [[NSDHL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSDHL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
