---
symbol: "IL1R2"
type: "gene"
col: 3698
ensembl_id: "ENSG00000115590"
name: "interleukin 1 receptor type 2"
location: "2q11.2"
module: 73
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 27
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 47
direction_downstream: 39
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# IL1R2

*interleukin 1 receptor type 2* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.57× (z +16.6, q 0e+00, up in 13 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (LoVo 0.0809×, NCI-H1573 0.0739×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0527×; ⚠ cell-cycle shift, explains ~98% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0649×; ⚠ cell-cycle shift, explains ~78% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.238×); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.165×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (LoVo 0.176×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOSTRIN]] (+0.64, fdr 1e-05), [[LAMC2]] (+0.63, fdr 1e-05), [[SCEL]] (+0.61, fdr 2e-05); moves opposite to [[CEP43]] (-0.45, fdr 4e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 47 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 39 go from it, the strongest it → [[LAMA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.57×** | +16.6 | 0e+00 | 13/17 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.01×** | +10.4 | 5e-23 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.67×** | +9.6 | 1e-19 | 3/6 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.31×** | +9.1 | 1e-17 | 5/15 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.76×** | +7.6 | 3e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.06×** | +6.4 | 2e-08 | 13/24 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.3 | 8e-06 | 4/15 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +4.6 | 3e-04 | 1/7 (KATO III) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +4.0 | 0.004 | 5/20 (HS-578T, KATO III, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.37×** | +3.8 | 0.007 | 6/11 (Panc 03.27, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.93×** | +3.8 | 0.007 | 1/10 (NCI-H1573) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.09×** | +3.7 | 0.011 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.87×** | +3.6 | 0.012 | 4/21 (HT-29, HS-578T, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.75×** | +3.5 | 0.021 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.040 | 9/17 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.061 | 3/24 (KATO III, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.63×** | +3.0 | 0.076 | 4/19 (AsPC-1, NCI-H1792, …) | two highest doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (LoVo 0.0809×, NCI-H1573 0.0739×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0527×; ⚠ cell-cycle shift, explains ~98% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0649×; ⚠ cell-cycle shift, explains ~78% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.238×); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.165×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (LoVo 0.176×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 62.2 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0527× (z -15.0) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 1.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 68.9× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0739× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.977 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOSTRIN]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[LAMC2]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SCEL]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[DSG4]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[LINC02582]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[KLK10]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[GJB3]] | +0.59 | +0.43 / +0.61 | both halves | 4e-05 |  |
| [[OSBP2]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[AMN]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[F3]] | +0.56 | +0.50 / +0.42 | both halves | 4e-05 | same gene group |
| [[SERPINB5]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LAMA3]] | +0.56 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP43]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 18, C 29. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises IL1R2's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.75× lower at baseline in the lines without F3 | 0.038 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[CEACAM1]] | B | CEACAM1 activity raises IL1R2's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without CEACAM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[EPHA1]] | B | EPHA1 activity raises IL1R2's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without EPHA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[ZNF365]] | B | ZNF365 activity raises IL1R2's level | lines that do not express ZNF365 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without ZNF365 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000285837, CHSY3, FLT1 |
| [[LINC02582]] | B | LINC02582 activity raises IL1R2's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.44× lower at baseline in the lines without LINC02582 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[EHF]] | B | EHF activity raises IL1R2's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.91× lower at baseline in the lines without EHF | 0.053 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[XACT]] | B | XACT activity raises IL1R2's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without XACT | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[LINC02327]] | B | LINC02327 activity raises IL1R2's level | lines that do not express LINC02327 (41) vs lines expressing it (9) | 1.75× lower at baseline in the lines without LINC02327 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000258028, LINC02566, ENSG00000289605 |
| [[LYPD3]] | B | LYPD3 activity raises IL1R2's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without LYPD3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[IL2RG]] | B | IL2RG activity raises IL1R2's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.74× lower at baseline in the lines without IL2RG | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[LAMA3]] | B | LAMA3 activity raises IL1R2's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without LAMA3 | 0.066 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[EPS8L1]] | B | EPS8L1 activity raises IL1R2's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without EPS8L1 | 0.073 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 20, C 19. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | IL1R2 activity raises LAMA3's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 4.03× lower at baseline in the lines without IL1R2 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[MET]] | B | IL1R2 activity raises MET's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.81× lower at baseline in the lines without IL1R2 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[PRDM1]] | B | IL1R2 activity raises PRDM1's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.60× lower at baseline in the lines without IL1R2 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[GALNT9]] | B | IL1R2 activity raises GALNT9's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 1.81× lower at baseline in the lines without IL1R2 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[EPS8L1]] | B | IL1R2 activity raises EPS8L1's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.81× lower at baseline in the lines without IL1R2 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | IL1R2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express IL1R2 (23) vs lines expressing it (25) | the lines without IL1R2: 0.76× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[F3]] | B | IL1R2 activity raises F3's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.61× lower at baseline in the lines without IL1R2 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[LANCL3]] | B | IL1R2 activity raises LANCL3's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 1.96× lower at baseline in the lines without IL1R2 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| cells under [[Terfenadine (drug)]] 0.5 µM | B | IL1R2 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express IL1R2 (23) vs lines expressing it (25) | the lines without IL1R2: 0.73× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[NOSTRIN]] | B | IL1R2 activity raises NOSTRIN's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 1.93× lower at baseline in the lines without IL1R2 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[CRYBG2]] | B | IL1R2 activity raises CRYBG2's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.43× lower at baseline in the lines without IL1R2 | 0.046 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[PRSS3]] | B | IL1R2 activity raises PRSS3's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.69× lower at baseline in the lines without IL1R2 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.3, 52.1); signed map (3.2, 37.0). **Vector** length 45.6, 9.44% of its response variance represented; |z| ≥ 3 in 536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +16.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +3.8 |
|  | [[vincristine (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +1.0 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Vandetanib (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:101,991,960-102,028,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD121b; previously IL1RB |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing; Interleukin receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, IL2_STAT5_SIGNALING |
| Reactome | 5 pathways, smallest: Interleukin-10 signaling; Interleukin-1 signaling; Interleukin-1 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P27930](https://www.uniprot.org/uniprotkb/P27930) (Interleukin-1 receptor type 2):

> Non-signaling receptor for IL1A, IL1B and IL1RN. Reduces IL1B activities. Serves as a decoy receptor by competitive binding to IL1B and preventing its binding to IL1R1. Also modulates cellular response through non-signaling association with IL1RAP after binding to IL1B. IL1R2 (membrane and secreted forms) preferentially binds IL1B and poorly IL1A and IL1RN. The secreted IL1R2 recruits secreted IL1RAP with high affinity; this complex formation may be the dominant mechanism for neutralization of …

**Summary**, from NCBI Gene [7850](https://www.ncbi.nlm.nih.gov/gene/7850):

> The protein encoded by this gene is a cytokine receptor that belongs to the interleukin 1 receptor family. This protein binds interleukin alpha (IL1A), interleukin beta (IL1B), and interleukin 1 receptor, type I(IL1R1/IL1RA), and acts as a decoy receptor that inhibits the activity of its ligands. Interleukin 4 (IL4) is reported to antagonize the activity of interleukin 1 by inducing the expression and release of this cytokine. This gene and three other genes form a cytokine receptor gene …

**Accessions** — [HGNC:5994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5994) · Entrez [7850](https://www.ncbi.nlm.nih.gov/gene/7850) · UniProt [P27930](https://www.uniprot.org/uniprotkb/P27930) · Ensembl [ENSG00000115590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115590)

## Data

Gene col 3698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3698); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3698]; `tensor/DDL_lfc|DDL_z.npy` [3698]; `embed/gene_vectors.npy` [3698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3698 or target_col == 3698). Every well: [[IL1R2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1R2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
