---
symbol: "MT1F"
type: "gene"
col: 12587
ensembl_id: "ENSG00000198417"
name: "metallothionein 1F"
location: "16q13"
module: 113
arm: "+"
pooled_cpm: 6.3
n_lines_expressing: 33
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 16
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# MT1F

*metallothionein 1F* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Chlorhexidine (diacetate) (drug)]] 5 µM: 3.53× (z +9.4, q 3e-18, up in 24 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.341× (z -5.7, q 8e-06, down in 23 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1M]] (+0.79, fdr 7e-06, ⚠ same locus), [[MT1X]] (+0.77, fdr 7e-06, ⚠ same locus), [[MT1E]] (+0.76, fdr 7e-06, ⚠ same locus), [[CEBPB]] (+0.71, fdr 7e-06), [[IRS2]] (+0.70, fdr 7e-06), [[ID1]] (+0.66, fdr 3e-05); moves opposite to [[C2CD3]] (-0.53, fdr 7e-05), [[HCFC1]] (-0.51, fdr 3e-05), [[UBE2V1]] (-0.51, fdr 3e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 16 go from it, the strongest it → [[GRAMD2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **3.53×** | +9.4 | 3e-18 | 24/31 (NCI-H2030, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **2.16×** | +5.8 | 2e-06 | 14/28 (HOP62, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +5.0 | 1e-04 | 9/20 (SNU-423, LS 180, …) | two highest doses | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.12×** | +4.0 | 0.010 | 15/30 (NCI-H460, A549, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.17×** | +3.9 | 0.010 | 16/30 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.08×** | +3.9 | 0.011 | 14/30 (AsPC-1, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.013 | 17/31 (BT-474, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.99×** | +3.6 | 0.019 | 14/29 (NCI-H1573, A549, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.97×** | +3.6 | 0.020 | 11/21 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.61×** | +3.6 | 0.020 | 16/31 (A549, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +3.5 | 0.022 | 2/6 (SNU-423, NCI-H2030) | two highest doses | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.94×** | +3.5 | 0.022 | 13/30 (A549, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.037 | 12/31 (NCI-H2030, COLO 205, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.87×** | +3.3 | 0.039 | 16/30 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.85×** | +3.3 | 0.042 | 15/29 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.78×** | +3.1 | 0.079 | 13/30 (A549, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.341×** | -5.7 | 8e-06 | 23/31 (SW1417, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.391×** | -5.0 | 2e-04 | 24/30 (KATO III, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.404×** | -4.8 | 3e-04 | 22/30 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.409×** | -4.5 | 0.001 | 21/31 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -4.2 | 0.003 | 16/30 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.458×** | -3.9 | 0.009 | 16/29 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.512×** | -3.5 | 0.034 | 16/30 (HCT15, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -3.3 | 0.075 | 16/26 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.313× | -3.1 | 0.12 | 9/25 (Panc 03.27, A549, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.565× | -3.0 | 0.15 | 10/25 (NCI-H1573, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 38.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +13.5) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 11.4× (z +11.3) | — |
| [[J82 (line)]] | alt | 29.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.37× (z +14.2) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[SW480 (line)]] | alt | 5.03 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +12.1) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 5.12× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +10.5) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[HOP62 (line)]] | alt | 12.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +16.5) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[Hs 766T (line)]] | wt | 3.21 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +8.8) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[NCI-H460 (line)]] | wt | 2.78 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0259× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 9.77 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -9.2) |
| [[SNU-423 (line)]] | alt | 5.11 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +9.7) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[SW1417 (line)]] | alt | 3.44 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0375× (z -9.2) |
| [[A-172 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1M]] | +0.79 | +0.75 / +0.85 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 858; ⚠ same locus (23.8 kb, same strand: neighbours can correlate without regulation) |
| [[MT1X]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 995; ⚠ same locus (21.8 kb, same strand: neighbours can correlate without regulation) |
| [[MT1E]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 797; ⚠ same locus (30.6 kb, same strand: neighbours can correlate without regulation) |
| [[CEBPB]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MT2A]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 772; ⚠ same locus (48.2 kb, same strand: neighbours can correlate without regulation) |
| [[IRS2]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MT1A]] | +0.67 | +0.51 / +0.74 | both halves | 1e-05 | same gene group; pathway: Metallothioneins bind metals; ⚠ same locus (17.6 kb, same strand: neighbours can correlate without regulation) |
| [[ID1]] | +0.66 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[TLR2]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[MAOA]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[IRX3]] | +0.65 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ARL4A]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.62 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SAA1]] | +0.62 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[KLF9]] | +0.60 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD3]] | -0.53 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[HCFC1]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[UBE2V1]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[PGRMC1]] | -0.51 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[FSTL1]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[STMP1]] | -0.49 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ANXA10]] | -0.48 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[STX16]] | -0.48 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[MOB1A]] | -0.47 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[POMGNT1]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises MT1F's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[SLPI]] | B | SLPI activity raises MT1F's level | lines that do not express SLPI (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without SLPI | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[PSMB5]] | B | PSMB5 activity raises MT1F's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FKBP1B]] | B | FKBP1B activity raises MT1F's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without FKBP1B | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |
| [[SGPP2]] | B | SGPP2 activity raises MT1F's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without SGPP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[MT1G]] | C | MT1G activity raises MT1F's level | lines that do not express MT1G (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without MT1G | 0.037 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1; co-absent with the target |
| [[CCL20]] | C | CCL20 activity raises MT1F's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without CCL20 | 0.073 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRAMD2B]] | B | MT1F activity raises GRAMD2B's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.77× lower at baseline in the lines without MT1F | 0.023 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[AVPI1]] | B | MT1F activity raises AVPI1's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without MT1F | 0.026 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[FGD4]] | B | MT1F activity raises FGD4's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without MT1F | 0.026 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[FKBP1B]] | B | MT1F activity raises FKBP1B's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without MT1F | 0.027 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[SLPI]] | B | MT1F activity raises SLPI's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without MT1F | 0.033 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[KIF13B]] | B | MT1F activity raises KIF13B's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.78× lower at baseline in the lines without MT1F | 0.042 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[SGPP2]] | B | MT1F activity raises SGPP2's level | lines that do not express MT1F (17) vs lines expressing it (33) | 3.06× lower at baseline in the lines without MT1F | 0.046 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[PKP2]] | B | MT1F activity raises PKP2's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.90× lower at baseline in the lines without MT1F | 0.063 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[ESYT2]] | B | MT1F activity raises ESYT2's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.34× lower at baseline in the lines without MT1F | 0.071 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[JPH2]] | B | MT1F activity raises JPH2's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.30× lower at baseline in the lines without MT1F | 0.077 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[AMN]] | B | MT1F activity raises AMN's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.69× lower at baseline in the lines without MT1F | 0.084 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[HCFC1]] | B | MT1F activity lowers HCFC1's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.22× higher at baseline in the lines without MT1F | 0.089 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.1, 13.6); signed map (14.7, 31.1). **Vector** length 73.0, 18.9% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +5.7 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +3.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +3.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.9 | +3.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +4.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Ivermectin (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | metallothionein 1F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,657,731-56,660,698 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MT1 |
| Gene groups (HGNC) | Metallothioneins |
| Reactome | 3 pathways, smallest: Metallothioneins bind metals; Response to metal ions; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [P04733](https://www.uniprot.org/uniprotkb/P04733) (Metallothionein-1F):

> Metallothioneins have a high content of cysteine residues that bind various heavy metals; these proteins are transcriptionally regulated by both heavy metals and glucocorticoids.

**Summary**, from NCBI Gene [4494](https://www.ncbi.nlm.nih.gov/gene/4494):

> Predicted to enable zinc ion binding activity. Involved in cellular response to cadmium ion and cellular response to zinc ion. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7398) · Entrez [4494](https://www.ncbi.nlm.nih.gov/gene/4494) · UniProt [P04733](https://www.uniprot.org/uniprotkb/P04733) · Ensembl [ENSG00000198417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198417)

## Data

Gene col 12587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12587); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12587]; `tensor/DDL_lfc|DDL_z.npy` [12587]; `embed/gene_vectors.npy` [12587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12587 or target_col == 12587). Every well: [[MT1F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT1F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
