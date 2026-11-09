---
symbol: "MIIP"
type: "gene"
col: 3823
ensembl_id: "ENSG00000116691"
name: "migration and invasion inhibitory protein"
location: "1p36.22"
module: 2
arm: "+"
pooled_cpm: 5.53
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MIIP

*migration and invasion inhibitory protein* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.54× (z +10.7, q 1e-23, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.603× (z -5.9, q 2e-06, down in 17 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.0651×, PANC-1 0.288×); [[Radotinib (drug)]] 0.5 µM in 1 line (HS-578T 0.0713×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0599×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.0718×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE21]] (+0.66, fdr 1e-05), [[GIT1]] (+0.66, fdr 1e-05), [[CCNQ]] (+0.66, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.54, fdr 1e-04), [[OCIAD1]] (-0.52, fdr 1e-04), [[C11orf58]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BTBD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.54×** | +10.7 | 1e-23 | 37/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +9.1 | 3e-17 | 32/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.4 | 3e-11 | 16/23 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +6.2 | 7e-08 | 28/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.1 | 1e-07 | 21/40 (CFPAC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +6.0 | 2e-07 | 22/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.7 | 1e-06 | 13/30 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +5.5 | 2e-06 | 22/45 (LS 180, J82, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.59×** | +4.9 | 6e-05 | 6/11 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.6 | 2e-04 | 7/16 (SW1417, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +4.2 | 0.002 | 5/28 (SK-MEL-2, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.005 | 3/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.007 | 11/41 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.7 | 0.010 | 5/22 (J82, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.6 | 0.014 | 7/30 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.014 | 8/41 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.016 | 11/43 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.080 | 6/45 (HT-29, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3823.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.0651×, PANC-1 0.288×); [[Radotinib (drug)]] 0.5 µM in 1 line (HS-578T 0.0713×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0599×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.0718×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -5.9 | 2e-06 | 17/37 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -3.6 | 0.093 | 11/44 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 5.55 | 0 | 2 | — | [[Regorafenib (drug)]] 0.05 µM 0.0629× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 3.37 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0599× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0651× (z -9.8) |
| [[HS-578T (line)]] | alt | 6.76 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0713× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 8.41 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 9.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -8.7) |
| [[SHP-77 (line)]] | alt | 6.59 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0718× (z -9.9) |
| [[A-172 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE21]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[GIT1]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.66 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[BRF1]] | +0.65 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[TBC1D24]] | +0.64 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.63 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.62 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[MPST]] | +0.61 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[RNF38]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[LDLRAP1]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MPZL1]] | +0.60 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.54 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[OCIAD1]] | -0.52 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[C11orf58]] | -0.51 | -0.41 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTBD6]] | B | BTBD6 activity lowers MIIP's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.25× higher at baseline in the lines without BTBD6 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |
| [[DNMT3B]] | C | DNMT3B activity raises MIIP's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without DNMT3B | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.4, -19.8); signed map (-41.3, -2.4). **Vector** length 54.2, 7.35% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +10.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.8 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.7 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +4.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | migration and invasion inhibitory protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:12,019,466-12,032,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12438, IIp45 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JXC2](https://www.uniprot.org/uniprotkb/Q5JXC2) (Migration and invasion-inhibitory protein):

> Inhibits glioma cells invasion and down-regulates adhesion- and motility-associated genes such as NFKB2 and ICAM1. Exhibits opposing effects to IGFBP2 on cell invasion.

**Summary**, from NCBI Gene [60672](https://www.ncbi.nlm.nih.gov/gene/60672):

> This gene encodes a protein that interacts with the oncogene protein insulin-like growth factor binding protein 2 and may function as an inhibitor of cell migration and invasion. This protein also interacts with the cell division protein 20 and may be involved in regulating mitotic progression. This protein may function as a tumor suppressor by inhibiting the growth or certain cancers. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:25715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25715) · Entrez [60672](https://www.ncbi.nlm.nih.gov/gene/60672) · UniProt [Q5JXC2](https://www.uniprot.org/uniprotkb/Q5JXC2) · Ensembl [ENSG00000116691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116691)

## Data

Gene col 3823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3823); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3823]; `tensor/DDL_lfc|DDL_z.npy` [3823]; `embed/gene_vectors.npy` [3823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3823 or target_col == 3823). Every well: [[MIIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
