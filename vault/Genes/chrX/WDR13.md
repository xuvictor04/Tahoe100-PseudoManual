---
symbol: "WDR13"
type: "gene"
col: 2192
ensembl_id: "ENSG00000101940"
name: "WD repeat domain 13"
location: "Xp11.23"
module: 35
arm: "+"
pooled_cpm: 15.22
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 16
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# WDR13

*WD repeat domain 13* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.83× (z +11.5, q 8e-28, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.393× (z -17.8, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADPRHL1]] (+0.64, fdr 1e-05), [[ATXN1L]] (+0.61, fdr 1e-05), [[TMEM43]] (+0.60, fdr 1e-05); moves opposite to [[MTF2]] (-0.52, fdr 3e-05), [[IFNAR2]] (-0.51, fdr 4e-05), [[PTMA]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +11.5 | 8e-28 | 33/46 (SW480, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +10.1 | 2e-21 | 23/37 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +9.0 | 3e-17 | 15/26 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 1e-04 | 17/47 (SHP-77, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 12/47 (SHP-77, SNU-423, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.28×** | +4.7 | 3e-04 | 16/48 (SHP-77, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +4.6 | 4e-04 | 11/32 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 4e-04 | 14/45 (SNU-1, AN3 CA, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 4e-04 | 16/45 (Hs 766T, SHP-77, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 5e-04 | 13/46 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +4.2 | 0.001 | 12/48 (NCI-H460, SHP-77, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.002 | 13/47 (SHP-77, PANC-1, …) | all doses, flat | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.003 | 14/46 (NCI-H460, SW480, …) | two highest doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.010 | 13/46 (A549, SHP-77, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.014 | 9/47 (SHP-77, NCI-H1573, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.016 | 6/43 (SNU-423, HT-29, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.016 | 11/48 (SHP-77, Hs 766T, …) | all doses, flat | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.4 | 0.020 | 3/48 (HS-578T, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.393×** | -17.8 | 0e+00 | 43/47 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.443×** | -15.5 | 0e+00 | 42/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -15.1 | 0e+00 | 42/48 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.510×** | -12.8 | 2e-35 | 37/45 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.511×** | -12.8 | 2e-35 | 39/48 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.460×** | -7.7 | 9e-13 | 31/48 (NCI-H460, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.686×** | -7.2 | 6e-11 | 25/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.723×** | -6.2 | 4e-08 | 23/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.717×** | -6.1 | 7e-08 | 20/47 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.729×** | -5.8 | 4e-07 | 22/45 (Panc 03.27, SW1417, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -4.9 | 5e-05 | 16/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.796×** | -4.3 | 7e-04 | 19/46 (H4, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.810×** | -4.0 | 0.003 | 13/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.677×** | -3.9 | 0.004 | 16/48 (A549, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.009 | 14/46 (AsPC-1, hTERT-HPNE, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.012 | 13/48 (AN3 CA, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.841× | -3.3 | 0.027 | 6/47 (CHP-212, J82, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.889× | -3.2 | 0.035 | 11/48 (LoVo, PANC-1, …) | top dose only |  |
| [[8-Hydroxyquinoline (drug)]] 0.05 µM |  | 0.856× | -3.0 | 0.061 | 0/48 | inconsistent across doses | position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.848× | -3.0 | 0.061 | 7/46 (HOP62, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.4 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.246× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -12.6) |
| [[HCT15 (line)]] | alt | 66.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -9.6) |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.148× (z -9.5) |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0887× (z -10.6) |
| [[H4 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0446× (z -13.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 7.36 | 0 | 1 | — | [[Rutin (trihydrate) (drug)]] 5 µM 0.0668× (z -8.8) |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.210× (z -9.2) |
| [[Hs 766T (line)]] | wt | 27.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.292× (z -8.5) |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -9.2) |
| [[SW 900 (line)]] | alt | 9.16 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.117× (z -9.5) |
| [[SW480 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADPRHL1]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ATXN1L]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[TMEM43]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ERMAP]] | +0.59 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[MC1R]] | +0.58 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[AKT1S1]] | +0.57 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[CSNK1D]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[PARD6G-AS1]] | +0.56 | +0.32 / +0.52 | both halves | 2e-04 |  |
| [[TG]] | +0.56 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[WDR45]] | +0.55 | +0.46 / +0.48 | both halves | 2e-05 | same gene group; STRING 528 |
| [[ZNF621]] | +0.55 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[SRRM2]] | +0.54 | +0.55 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTF2]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[IFNAR2]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PTMA]] | -0.51 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.51 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[RHOT1]] | -0.51 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[NR3C2]] | -0.51 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[SCML2]] | -0.50 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[FAM102B]] | -0.50 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[TMEM160]] | -0.49 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[STRBP]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[L2HGDH]] | -0.49 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[KIF3A]] | -0.49 | -0.27 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises WDR13's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.408). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.8, 10.2); signed map (12.9, -8.8). **Vector** length 76.9, 14.0% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.9 | +5.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.8 | +4.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +3.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -12.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -12.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | -17.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,590,042-48,608,869 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q9H1Z4](https://www.uniprot.org/uniprotkb/Q9H1Z4) carries no function annotation.

**Summary**, from NCBI Gene [64743](https://www.ncbi.nlm.nih.gov/gene/64743):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by Gly-His and Trp-Asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. A similar protein in mouse is thought to be a negative regulator of the …

**Accessions** — [HGNC:14352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14352) · Entrez [64743](https://www.ncbi.nlm.nih.gov/gene/64743) · UniProt [Q9H1Z4](https://www.uniprot.org/uniprotkb/Q9H1Z4) · Ensembl [ENSG00000101940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101940)

## Data

Gene col 2192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2192); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2192]; `tensor/DDL_lfc|DDL_z.npy` [2192]; `embed/gene_vectors.npy` [2192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2192 or target_col == 2192). Every well: [[WDR13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
