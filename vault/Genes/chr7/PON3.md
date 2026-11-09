---
symbol: "PON3"
type: "gene"
col: 2675
ensembl_id: "ENSG00000105852"
name: "paraoxonase 3"
location: "7q21.3"
module: 8
arm: "+"
pooled_cpm: 4.28
n_lines_expressing: 28
n_dd_up: 23
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PON3

*paraoxonase 3* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.74× (z +14.1, q 3e-42, up in 5 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +9.9, q 1e-20, up in 9 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.609× (z -5.3, q 5e-05, down in 8 of 22 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.436× (z -4.8, q 2e-04, down in 9 of 22 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGA]] (+0.66, fdr 1e-05), [[TARID]] (+0.66, fdr 1e-05), [[HAVCR1]] (+0.61, fdr 4e-05); moves opposite to [[MARK3]] (-0.41, fdr 2e-04), [[DRAP1]] (-0.39, fdr 4e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[STEAP2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.74×** | +14.1 | 3e-42 | 5/9 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +10.0 | 4e-21 | 4/12 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +9.9 | 1e-20 | 9/18 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +8.9 | 1e-16 | 9/17 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.0 | 2e-13 | 8/13 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +6.5 | 9e-09 | 13/26 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.6 | 2e-06 | 7/26 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.42×** | +5.5 | 3e-06 | 11/25 (A-427, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.56×** | +4.9 | 6e-05 | 9/21 (SW 900, NCI-H2347, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.7 | 1e-04 | 9/25 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.7 | 1e-04 | 10/24 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.3 | 7e-04 | 2/18 (HEC-1-A, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.007 | 4/18 (SW 900, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.38×** | +3.6 | 0.015 | 1/24 (Panc 03.27) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.016 | 1/18 (A-427) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.023 | 5/26 (AsPC-1, SW 900, …) | all doses, flat |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.023 | 3/17 (A498, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.041 | 3/26 (A498, SW48, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.047 | 2/17 (NCI-H2030, SW 900) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.047 | 5/21 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **1.30×** | +2.9 | 0.095 | 0/25 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.609×** | -5.3 | 5e-05 | 8/22 (NCI-H2030, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.637×** | -5.0 | 1e-04 | 14/26 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -4.8 | 2e-04 | 9/22 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.663×** | -4.6 | 6e-04 | 6/22 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -4.3 | 0.002 | 12/22 (SW 900, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -4.2 | 0.002 | 13/24 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -3.9 | 0.009 | 12/20 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.718×** | -3.7 | 0.015 | 8/24 (A498, A549, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.713×** | -3.4 | 0.043 | 9/25 (COLO 205, A549, …) | rises with dose |  |
| [[Lopinavir (drug)]] 0.5 µM |  | **0.743×** | -3.3 | 0.048 | 0/25 | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.055 | 4/26 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.753×** | -3.2 | 0.070 | 6/26 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.51 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0956× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0683× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 4.71 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.118× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGA]] | +0.66 | +0.62 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[TARID]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[HAVCR1]] | +0.61 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[ITIH2]] | +0.60 | +0.48 / +0.39 | both halves | 6e-05 | **novel candidate** |
| [[POU5F1]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[IGFBP1]] | +0.56 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[PON2]] | +0.52 | +0.32 / +0.52 | both halves | 2e-04 | pathway: Arachidonate metabolism; STRING 691; ⚠ **readthrough risk**: this gene lies 8.5 kb 3′ of PON2 on the same strand (can correlate by spillover, not regulation) |
| [[TIMD4]] | +0.52 | +0.58 / +0.27 | both halves | 3e-04 |  |
| [[ABCC6]] | +0.51 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[CP]] | +0.51 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[F5]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[C3]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PLSCR4]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARK3]] | -0.41 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[DRAP1]] | -0.39 | -0.24 / -0.38 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PON3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ITIH2]] | B | ITIH2 activity raises PON3's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.68× lower at baseline in the lines without ITIH2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[MANSC1]] | B | MANSC1 activity raises PON3's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.13× lower at baseline in the lines without MANSC1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[PLSCR4]] | B | PLSCR4 activity raises PON3's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without PLSCR4 | 0.086 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[VSTM2L]] | B | VSTM2L activity raises PON3's level | lines that do not express VSTM2L (20) vs lines expressing it (30) | 1.21× lower at baseline in the lines without VSTM2L | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF829, PKD2L2-DT, ZNF625; maybe low, not absent |
| [[STEAP2-AS1]] | B | STEAP2-AS1 activity raises PON3's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 2.34× lower at baseline in the lines without STEAP2-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent |
| [[NCMAP]] | C | NCMAP activity raises PON3's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.53× lower at baseline in the lines without NCMAP | 0.032 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent; co-absent with the target |
| [[FGA]] | C | FGA activity raises PON3's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.80× lower at baseline in the lines without FGA | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[NR5A2]] | C | NR5A2 activity raises PON3's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 2.54× lower at baseline in the lines without NR5A2 | 0.048 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; co-absent with the target |
| [[FGB]] | C | FGB activity raises PON3's level | lines that do not express FGB (42) vs lines expressing it (8) | 3.11× lower at baseline in the lines without FGB | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises PON3's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.43× lower at baseline in the lines without STEAP4 | 0.065 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP2-AS1]] | B | PON3 activity raises STEAP2-AS1's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without PON3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[DAPK2]] | B | PON3 activity raises DAPK2's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.13× lower at baseline in the lines without PON3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[PON2]] | B | PON3 activity raises PON2's level | lines that do not express PON3 (22) vs lines expressing it (28) | 1.79× lower at baseline in the lines without PON3 | 0.049 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[CSGALNACT1]] | B | PON3 activity raises CSGALNACT1's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without PON3 | 0.054 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[PLEKHA7]] | B | PON3 activity raises PLEKHA7's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without PON3 | 0.068 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[BATF]] | B | PON3 activity raises BATF's level | lines that do not express PON3 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without PON3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[EPS8]] | B | PON3 activity raises EPS8's level | lines that do not express PON3 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without PON3 | 0.092 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[GPR37]] | B | PON3 activity raises GPR37's level | lines that do not express PON3 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without PON3 | 0.098 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[NR5A2]] | C | PON3 activity raises NR5A2's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.74× lower at baseline in the lines without PON3 | 0.066 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.388). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.4, 44.1); signed map (52.2, 26.8). **Vector** length 40.5, 6.66% of its response variance represented; |z| ≥ 3 in 636 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.0 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -4.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | paraoxonase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:95,359,872-95,396,375 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Paraoxonases |
| Reactome | 6 pathways, smallest: Atorvastatin ADME; Synthesis of 5-eicosatetraenoic acids; Arachidonate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15166](https://www.uniprot.org/uniprotkb/Q15166) (Serum paraoxonase/lactonase 3):

> Has low activity towards the organophosphate paraxon and aromatic carboxylic acid esters. Rapidly hydrolyzes lactones such as statin prodrugs (e.g. lovastatin). Hydrolyzes aromatic lactones and 5- or 6-member ring lactones with aliphatic substituents but not simple lactones or those with polar substituents.

**Summary**, from NCBI Gene [5446](https://www.ncbi.nlm.nih.gov/gene/5446):

> This gene is a member of the paraoxonase family and lies in a cluster on chromosome 7 with the other two family members. The encoded protein is secreted into the bloodstream and associates with high-density lipoprotein (HDL). The protein also rapidly hydrolyzes lactones and can inhibit the oxidation of low-density lipoprotein (LDL), a function that is believed to slow the initiation and progression of atherosclerosis. Alternatively spliced variants which encode different protein isoforms have …

**Accessions** — [HGNC:9206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9206) · Entrez [5446](https://www.ncbi.nlm.nih.gov/gene/5446) · UniProt [Q15166](https://www.uniprot.org/uniprotkb/Q15166) · Ensembl [ENSG00000105852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105852)

## Data

Gene col 2675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2675); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2675]; `tensor/DDL_lfc|DDL_z.npy` [2675]; `embed/gene_vectors.npy` [2675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2675 or target_col == 2675). Every well: [[PON3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PON3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
