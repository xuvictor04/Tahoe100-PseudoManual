---
symbol: "SPART-AS1"
type: "gene"
col: 4199
ensembl_id: "ENSG00000120664"
name: "SPART antisense RNA 1"
location: "13q13.3"
module: 83
arm: "+"
pooled_cpm: 3.08
n_lines_expressing: 34
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 66
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# SPART-AS1

*SPART antisense RNA 1* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +9.3, q 5e-18, up in 18 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.102× (z -21.6, q 0e+00, down in 29 of 30 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP5S1]] (+0.69, fdr 2e-05), [[LANCL2]] (+0.69, fdr 2e-05), [[UBE2D3-AS1]] (+0.68, fdr 7e-05); moves opposite to [[WASF3]] (-0.63, fdr 1e-04), [[AFDN]] (-0.61, fdr 4e-05), [[PCMT1]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPART]] → it (grade C ⚠); 66 go from it, the strongest it → cells under [[Bortezomib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +9.3 | 5e-18 | 18/22 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +8.7 | 6e-16 | 14/23 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +6.0 | 4e-07 | 13/24 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.3 | 0.002 | 8/16 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.010 | 8/29 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +3.4 | 0.072 | 9/30 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.3 | 0.072 | 1/6 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.092 | 10/28 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.11 | 5/30 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.102×** | -21.6 | 0e+00 | 29/30 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.152×** | -17.8 | 0e+00 | 28/29 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.159×** | -17.4 | 0e+00 | 27/30 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.240×** | -13.5 | 2e-39 | 27/30 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.367×** | -9.5 | 3e-19 | 19/25 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.610×** | -6.6 | 4e-09 | 18/30 (NCI-H2347, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.266×** | -6.6 | 5e-09 | 17/28 (A-172, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.731×** | -4.2 | 0.002 | 11/28 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.646×** | -4.1 | 0.002 | 10/27 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **0.652×** | -3.9 | 0.006 | 5/26 (A549, SK-MEL-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.035 | 7/27 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.690×** | -3.4 | 0.035 | 7/26 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.709×** | -3.1 | 0.077 | 8/24 (C32, RPMI-7951, …) | top dose only |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.723×** | -3.1 | 0.087 | 5/30 (A-427, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.09 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +14.6) | [[Belinostat (drug)]] 5 µM 0.0190× (z -19.7) |
| [[J82 (line)]] | alt | 10.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.0736× (z -13.2) |
| [[C32 (line)]] | wt | 5.38 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0460× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 7.84 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0155× (z -17.2) |
| [[NCI-H2347 (line)]] | alt | 3.77 | 0 | 3 | — | [[Tucidinostat (drug)]] 5 µM 0.128× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 7.32 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0247× (z -12.4) |
| [[SW 900 (line)]] | alt | 6.57 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0280× (z -12.7) |
| [[A498 (line)]] | wt | 6.92 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -9.6) |
| [[HOP62 (line)]] | alt | 3.87 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0410× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 6.19 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0630× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 6.82 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0227× (z -13.8) |
| [[PANC-1 (line)]] | alt | 3.33 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +8.6) | [[Belinostat (drug)]] 5 µM 0.0274× (z -16.0) |
| [[SNU-1 (line)]] | wt | 6.88 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0328× (z -9.9) |
| [[A-172 (line)]] | wt | 3.30 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0587× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 3.66 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0775× (z -9.0) |
| [[A-427 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.215 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.210 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 18 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP5S1]] | +0.69 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[LANCL2]] | +0.69 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[UBE2D3-AS1]] | +0.68 | +0.58 / +0.37 | both halves | 7e-05 | same gene group |
| [[MPDU1]] | +0.67 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PBLD]] | +0.67 | +0.48 / +0.26 | both halves | 4e-04 |  |
| [[PCBP1-AS1]] | +0.67 | +0.47 / +0.30 | both halves | 2e-04 | same gene group |
| [[EFCAB2]] | +0.66 | +0.46 / +0.32 | both halves | 2e-04 |  |
| [[ZFY]] | +0.66 | +0.62 / +0.22 | both halves | 6e-04 |  |
| [[LINC00571]] | +0.66 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[ATF5]] | +0.66 | +0.47 / +0.29 | both halves | 2e-04 |  |
| [[KPTN]] | +0.65 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[FAM151B]] | +0.65 | +0.54 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.63 | -0.49 / -0.32 | both halves | 1e-04 |  |
| [[AFDN]] | -0.61 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PCMT1]] | -0.60 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[OSTF1]] | -0.60 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ATP13A2]] | -0.60 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SDHAF3]] | -0.60 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[MINK1]] | -0.59 | -0.48 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[METAP1]] | -0.59 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[SERAC1]] | -0.58 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[LYPLA1]] | -0.58 | -0.54 / -0.29 | both halves | 3e-04 |  |
| [[LPCAT4]] | -0.57 | -0.47 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[LRFN3]] | -0.57 | -0.36 / -0.26 | both halves | 4e-04 |  |
| [[TNK2]] | -0.57 | -0.31 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPART]] | C | SPART activity raises SPART-AS1's level | lines that do not express SPART (15) vs lines expressing it (35) | 3.70× lower at baseline in the lines without SPART | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC169, SPART-AS1, FIGN; co-absent with the target; its own permutation p |

### Downstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 0, C 66. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bortezomib (drug)]] 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Bortezomib 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.78× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[AZD2858 (drug)]] 5 µM | C | SPART-AS1 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.31× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM | C | SPART-AS1 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.24× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[Sulfatinib (drug)]] 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Sulfatinib 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.19× the cells of the other lines | 0.010 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.29× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[5-Azacytidine (drug)]] 5 µM | C | SPART-AS1 activity lowers the cells' numbers under 5-Azacytidine 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.25× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[Menadione (drug)]] 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.15× the cells of the other lines | 0.014 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.24× the cells of the other lines | 0.018 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[Penfluridol (drug)]] 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.16× the cells of the other lines | 0.019 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[c-Kit-IN-1 (drug)]] 5 µM | C | SPART-AS1 activity lowers the cells' numbers under c-Kit-IN-1 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.33× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[Furosemide (drug)]] 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.15× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| cells under [[Ixazomib (drug)]] 0.05 µM | C | SPART-AS1 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.24× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.5, 9.9); signed map (20.6, -7.0). **Vector** length 68.5, 14.9% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.2 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.9 | -17.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -13.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -17.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -21.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | SPART antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q13.3 — chr13:36,346,431-36,369,601 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C13orf43, SPG20OS, SPG20-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [P0CW21](https://www.uniprot.org/uniprotkb/P0CW21) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39933) · Entrez [100507135](https://www.ncbi.nlm.nih.gov/gene/100507135) · UniProt [P0CW21](https://www.uniprot.org/uniprotkb/P0CW21) · Ensembl [ENSG00000120664](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120664)

## Data

Gene col 4199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4199); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4199]; `tensor/DDL_lfc|DDL_z.npy` [4199]; `embed/gene_vectors.npy` [4199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4199 or target_col == 4199). Every well: [[SPART-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPART-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
