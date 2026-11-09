---
symbol: "CYP4F3"
type: "gene"
col: 11827
ensembl_id: "ENSG00000186529"
name: "cytochrome P450 family 4 subfamily F member 3"
location: "19p13.12"
module: 8
arm: "+"
pooled_cpm: 6.01
n_lines_expressing: 21
n_dd_up: 39
n_dd_down: 7
n_dd_up_clean: 27
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 47
direction_downstream: 79
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CYP4F3

*cytochrome P450 family 4 subfamily F member 3* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.63× (z +13.1, q 2e-36, up in 9 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 2.99× (z +8.8, q 1e-16, up in 16 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.484× (z -6.2, q 3e-07, down in 15 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PROM2]] (+0.69, fdr 7e-06), [[TTC22]] (+0.67, fdr 1e-05), [[CYP4F12]] (+0.67, fdr 7e-06, ⚠ same locus), [[IGFL2-AS1]] (+0.63, fdr 7e-06); moves opposite to [[TBCCD1]] (-0.49, fdr 7e-05), [[PFN1]] (-0.48, fdr 4e-05), [[VEGFC]] (-0.48, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 47 arrows point to it, the strongest [[TSPAN4]] → it (grade B ⚠); 79 go from it, the strongest it → [[GCLC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.63×** | +13.1 | 2e-36 | 9/13 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.20×** | +11.8 | 1e-29 | 3/6 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.68×** | +10.3 | 1e-22 | 4/7 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.99×** | +8.8 | 1e-16 | 16/17 (HEC-1-A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.33×** | +7.2 | 7e-11 | 17/18 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.14×** | +6.5 | 9e-09 | 13/18 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.4 | 6e-06 | 5/13 (LS 180, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +5.3 | 1e-05 | 13/19 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.83×** | +5.2 | 1e-05 | 11/19 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.51×** | +5.0 | 4e-05 | 11/19 (COLO 205, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +4.4 | 5e-04 | 9/16 (LS 180, HEC-1-A, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.60×** | +4.3 | 1e-03 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.2 | 0.001 | 4/15 (CFPAC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.53×** | +4.1 | 0.001 | 6/15 (NCI-H1573, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.002 | 12/19 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.004 | 9/18 (NCI-H1573, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **2.27×** | +3.7 | 0.008 | 6/17 (NCI-H1573, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.015 | 10/17 (Panc 03.27, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.015 | 3/19 (A-172, A549, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.015 | 11/17 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.49×** | +3.4 | 0.018 | 7/17 (A498, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.020 | 8/17 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.77×** | +3.3 | 0.020 | 4/17 (AsPC-1, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -6.2 | 3e-07 | 15/18 (COLO 205, SW1417, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.506×** | -5.9 | 9e-07 | 16/19 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.506×** | -5.9 | 9e-07 | 14/19 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.624×** | -3.9 | 0.013 | 11/18 (COLO 205, LS 180, …) | top dose only | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.639×** | -3.9 | 0.013 | 9/17 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.562×** | -3.4 | 0.065 | 3/19 (LS 180, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.479×** | -3.3 | 0.076 | 2/18 (HepG2/C3A, A498) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 41.1 | 2 | 10 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.06× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0736× (z -15.2) |
| [[SW1417 (line)]] | alt | 77.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -15.7) |
| [[LS 180 (line)]] | wt | 23.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0402× (z -24.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0785× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 44.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0340× (z -24.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.165× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 3.06 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 17.0× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 7.32 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 5.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -9.1) |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.836 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROM2]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[TTC22]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[CYP4F12]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 | same gene group; pathway: Biological oxidations; ⚠ same locus (10.2 kb, same strand: neighbours can correlate without regulation) |
| [[IGFL2-AS1]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ABCC2]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[AKR1C1]] | +0.63 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[AKR1C3]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 | pathway: Arachidonate metabolism |
| [[FUT2]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[GCNT3]] | +0.60 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[LINC01559]] | +0.59 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[ADCY4]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[SLC44A4]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[DNM1]] | +0.58 | +0.65 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCCD1]] | -0.49 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[PFN1]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[VEGFC]] | -0.48 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[TSPAN4]] | -0.47 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[NT5E]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[UACA]] | -0.47 | -0.51 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 7, C 40. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN4]] | B | TSPAN4 activity lowers CYP4F3's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 5.32× higher at baseline in the lines without TSPAN4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[STK31]] | B | STK31 activity lowers CYP4F3's level | lines that do not express STK31 (6) vs lines expressing it (44) | 3.13× higher at baseline in the lines without STK31 | 0.032 | ⚠ within organs, on part of the lines; also absent: HPSE, LTBP4, STRIP2; maybe low, not absent |
| [[AKR1C3]] | B | AKR1C3 activity raises CYP4F3's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.40× lower at baseline in the lines without AKR1C3 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[MYH14]] | B | MYH14 activity raises CYP4F3's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.13× lower at baseline in the lines without MYH14 | 0.064 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises CYP4F3's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without SLC44A3-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CYP4F3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SPATA6L]] | B | SPATA6L activity raises CYP4F3's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.15× lower at baseline in the lines without SPATA6L | 0.097 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[CYP4F12]] | C | CYP4F12 activity raises CYP4F3's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 4.48× lower at baseline in the lines without CYP4F12 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |
| [[LINC02967]] | C | LINC02967 activity raises CYP4F3's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 3.58× lower at baseline in the lines without LINC02967 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises CYP4F3's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 4.02× lower at baseline in the lines without RAB25 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises CYP4F3's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.69× lower at baseline in the lines without CYP4F11 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[C6orf132]] | C | C6orf132 activity raises CYP4F3's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.23× lower at baseline in the lines without C6orf132 | 0.002 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |

### Downstream of this gene

*79 arrows, 79 of them with an alert ⚠; grade A 0, B 27, C 52. Shown: the 12 strongest; 67 more arrows (67 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCLC]] | B | CYP4F3 activity raises GCLC's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without CYP4F3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[MYH14]] | B | CYP4F3 activity raises MYH14's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 4.50× lower at baseline in the lines without CYP4F3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[ELMO3]] | B | CYP4F3 activity raises ELMO3's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.37× lower at baseline in the lines without CYP4F3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[LINC01504]] | B | CYP4F3 activity raises LINC01504's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without CYP4F3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[PLCH1]] | B | CYP4F3 activity raises PLCH1's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.83× lower at baseline in the lines without CYP4F3 | 0.006 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[SLC44A3-AS1]] | B | CYP4F3 activity raises SLC44A3-AS1's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without CYP4F3 | 0.006 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[PROM2]] | B | CYP4F3 activity raises PROM2's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.34× lower at baseline in the lines without CYP4F3 | 0.007 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[HGD]] | B | CYP4F3 activity raises HGD's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without CYP4F3 | 0.007 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[GAREM1]] | B | CYP4F3 activity raises GAREM1's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without CYP4F3 | 0.010 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[SLC44A3-AS1]] | B | CYP4F3 activity strengthens SLC44A3-AS1's drug response | lines that do not express CYP4F3 (18) vs lines expressing it (18) | the lines without CYP4F3 respond 0.65× as strongly (z diff +1.87); strongest at Homoharringtonine 0.5 µM: 0.50x vs 0.21x (z diff +4.2) | 0.014 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; target measured in part of the lines; artifact flags |
| [[TMEM184A]] | B | CYP4F3 activity raises TMEM184A's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.31× lower at baseline in the lines without CYP4F3 | 0.018 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[LINC02580]] | B | CYP4F3 activity raises LINC02580's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without CYP4F3 | 0.019 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.9, 54.0); signed map (60.9, 4.9). **Vector** length 58.1, 15.3% of its response variance represented; |z| ≥ 3 in 580 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.2 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 4 subfamily F member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,640,897-15,662,825 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYP4F; previously LTB4H |
| Gene groups (HGNC) | Cytochrome P450 family 4 |
| Reactome | 10 pathways, smallest: Fatty acids; Miscellaneous substrates; Eicosanoids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08477](https://www.uniprot.org/uniprotkb/Q08477) (Cytochrome P450 4F3):

> A cytochrome P450 monooxygenase involved in the metabolism of various endogenous substrates, including fatty acids and their oxygenated derivatives (oxylipins). Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (CPR; NADPH-ferrihemoprotein reductase). May play a role in inactivation of pro-inflammatory and anti-inflammatory oxylipins during the …

**Summary**, from NCBI Gene [4051](https://www.ncbi.nlm.nih.gov/gene/4051):

> This gene, CYP4F3, encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This protein localizes to the endoplasmic reticulum. The enzyme starts the process of inactivating and degrading leukotriene B4, a potent mediator of inflammation. This gene is part of a cluster of cytochrome P450 genes on chromosome 19. Another member …

**Accessions** — [HGNC:2646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2646) · Entrez [4051](https://www.ncbi.nlm.nih.gov/gene/4051) · UniProt [Q08477](https://www.uniprot.org/uniprotkb/Q08477) · Ensembl [ENSG00000186529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186529)

## Data

Gene col 11827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11827); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11827]; `tensor/DDL_lfc|DDL_z.npy` [11827]; `embed/gene_vectors.npy` [11827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11827 or target_col == 11827). Every well: [[CYP4F3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP4F3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
