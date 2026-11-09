---
symbol: "CEP97"
type: "gene"
col: 11292
ensembl_id: "ENSG00000182504"
name: "centrosomal protein 97"
location: "3q12.3"
module: 67
arm: "+"
pooled_cpm: 35.25
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CEP97

*centrosomal protein 97* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +9.0, q 2e-16, up in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.41× (z +7.8, q 1e-12, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.681× (z -8.8, q 7e-16, down in 34 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.634× (z -5.5, q 1e-05, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARPBP]] (+0.65, fdr 7e-06), [[NEIL3]] (+0.65, fdr 7e-06), [[CEP152]] (+0.63, fdr 1e-05); moves opposite to [[TMEM150A]] (-0.52, fdr 7e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NDC80]] → it (grade C ⚠); 1 goes from it, the strongest it → [[CCP110]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +9.0 | 2e-16 | 30/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +8.5 | 5e-15 | 2/48 (HOP62, MIA PaCa-2) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +7.8 | 1e-12 | 29/48 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +7.6 | 4e-12 | 31/48 (HepG2/C3A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.38×** | +7.4 | 2e-11 | 24/47 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +7.1 | 1e-10 | 24/48 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +6.9 | 4e-10 | 27/47 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +6.8 | 6e-10 | 29/48 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.34×** | +6.6 | 3e-09 | 27/48 (NCI-H23, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.33×** | +6.5 | 6e-09 | 25/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.65×** | +6.0 | 1e-07 | 25/46 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +5.9 | 2e-07 | 20/48 (LoVo, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +5.8 | 3e-07 | 20/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.27×** | +5.5 | 2e-06 | 23/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +5.3 | 4e-06 | 20/47 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.8 | 5e-05 | 20/48 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.054 | 6/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.0 | 0.055 | 12/48 (HOP62, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -8.8 | 7e-16 | 34/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.634×** | -5.5 | 1e-05 | 19/47 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.657×** | -5.0 | 9e-05 | 18/48 (SK-MEL-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.662×** | -4.9 | 1e-04 | 16/47 (Hs 766T, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.809×** | -4.5 | 8e-04 | 19/44 (J82, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.816×** | -4.3 | 0.002 | 16/47 (C32, NCI-H1573, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.818×** | -4.2 | 0.002 | 20/48 (HCT15, SK-MEL-2, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.719×** | -4.0 | 0.005 | 13/48 (PANC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -3.7 | 0.014 | 15/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.016 | 11/46 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.020 | 13/48 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.856× | -3.4 | 0.032 | 9/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.4 | 0.032 | 17/48 (PANC-1, H4, …) | rises with dose |  |
| [[Saquinavir (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.037 | 14/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.763×** | -3.2 | 0.044 | 16/47 (NCI-H460, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 55.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 69.7 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.570× (z -8.8) |
| [[AN3 CA (line)]] | alt | 74.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.200× (z -8.8) |
| [[H4 (line)]] | wt | 42.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 65.8 | 0 | 2 (2 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.273× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 27.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 98.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -9.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +8.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -8.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +9.1) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[LS 180 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +9.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -13.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARPBP]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[NEIL3]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CEP152]] | +0.63 | +0.72 / +0.50 | both halves | 1e-05 | pathway: Anchoring of the basal body to the plasma membrane; STRING 478 |
| [[OIP5]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SCML2]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PBK]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CKS1B]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[BUB3]] | +0.58 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[MIS18BP1]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CEP57L1]] | +0.58 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MPHOSPH9]] | +0.57 | +0.65 / +0.54 | both halves | 1e-05 | STRING 663 |
| [[CKAP2]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM150A]] | -0.52 | -0.58 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDC80]] | C | NDC80 activity raises CEP97's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without NDC80 | 0.025 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCP110]] | C | CEP97's natural level weakens CCP110's drug response | CEP97's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.14; direction not clear | 0.019 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.0, -53.1); signed map (-45.8, -40.6). **Vector** length 111, 27.4% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.51 to 12); *G2/M checkpoint* (hallmark, mean cos +0.50 to 9); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM |  | +5.0 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +6.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.3 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.0 | +5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.9 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Furosemide (drug)]] 0.5 µM |  | +2.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.3 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 97 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,724,534-101,770,562 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23047; previously LRRIQ2 |
| Reactome | 8 pathways, smallest: RHOV GTPase cycle; Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IW35](https://www.uniprot.org/uniprotkb/Q8IW35) (Centrosomal protein of 97 kDa):

> Acts as a key negative regulator of ciliogenesis in collaboration with CCP110 by capping the mother centriole thereby preventing cilia formation. Required for recruitment of CCP110 to the centrosome.

**Summary**, from NCBI Gene [79598](https://www.ncbi.nlm.nih.gov/gene/79598):

> Predicted to enable U2 snRNA binding activity and calmodulin binding activity. Involved in negative regulation of cilium assembly and regulation of mitotic spindle assembly. Located in centriole and centrosome. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26244) · Entrez [79598](https://www.ncbi.nlm.nih.gov/gene/79598) · UniProt [Q8IW35](https://www.uniprot.org/uniprotkb/Q8IW35) · Ensembl [ENSG00000182504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182504)

## Data

Gene col 11292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11292); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11292]; `tensor/DDL_lfc|DDL_z.npy` [11292]; `embed/gene_vectors.npy` [11292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11292 or target_col == 11292). Every well: [[CEP97 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP97.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
