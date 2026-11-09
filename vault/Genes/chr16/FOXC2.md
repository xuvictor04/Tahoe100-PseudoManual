---
symbol: "FOXC2"
type: "gene"
col: 10741
ensembl_id: "ENSG00000176692"
name: "forkhead box C2"
location: "16q24.1"
module: 98
arm: "+"
pooled_cpm: 6.99
n_lines_expressing: 17
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 25
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# FOXC2

*forkhead box C2* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.18× (z +10.9, q 5e-25, up in 6 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.526× (z -4.4, q 0.007, down in 9 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.162×; ⚠ cell-cycle shift, explains ~51% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 0.137×; ⚠ cell-cycle shift, explains ~47% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (PANC-1 0.237×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA10]] (+0.74, fdr 7e-06), [[IRX3]] (+0.72, fdr 7e-06), [[SRGN]] (+0.66, fdr 7e-06); moves opposite to [[SIRLNT]] (-0.64, fdr 1e-05), [[LINC01411]] (-0.58, fdr 1e-05), [[ADAMTS16]] (-0.57, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 25 go from it, the strongest it → [[LINC00536]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.18×** | +10.9 | 5e-25 | 6/13 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **5.05×** | +9.4 | 1e-18 | 1/10 (hTERT-HPNE) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.24×** | +7.8 | 8e-13 | 0/10 | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.80×** | +6.3 | 3e-08 | 0/10 | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.42×** | +5.9 | 4e-07 | 8/14 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.35×** | +5.7 | 1e-06 | 12/14 (HS-578T, H4, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.83×** | +5.7 | 1e-06 | 8/13 (A498, HS-578T, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +5.3 | 8e-06 | 6/11 (NCI-H2030, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **2.45×** | +5.2 | 1e-05 | 5/12 (SNU-423, HS-578T, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.13×** | +5.0 | 3e-05 | 10/14 (HS-578T, H4, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.96×** | +4.5 | 4e-04 | 1/14 (H4) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +4.0 | 0.002 | 4/13 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.002 | 11/14 (HS-578T, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.00×** | +4.0 | 0.002 | 1/14 (LS 180) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.0 | 0.003 | 6/14 (SNU-423, HS-578T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.79×** | +3.9 | 0.004 | 11/14 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +3.8 | 0.004 | 13/14 (HS-578T, A-172, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.77×** | +3.8 | 0.004 | 12/14 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.75×** | +3.7 | 0.006 | 8/13 (HS-578T, A498, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.006 | 10/14 (HS-578T, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.009 | 1/14 (CFPAC-1) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.71×** | +3.6 | 0.009 | 10/14 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.79×** | +3.4 | 0.017 | 1/14 (A498) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.54×** | +2.9 | 0.092 | 12/14 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Flutamide (drug)]] 5 µM |  | **1.54×** | +2.8 | 0.092 | 5/14 (PANC-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10741.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.162×; ⚠ cell-cycle shift, explains ~51% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 0.137×; ⚠ cell-cycle shift, explains ~47% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (PANC-1 0.237×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.526×** | -4.4 | 0.007 | 9/15 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.530×** | -4.0 | 0.020 | 9/14 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.590× | -3.4 | 0.14 | 0/14 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 45.8 | 7 (1 ⚠) | 0 | [[Budesonide (drug)]] 0.05 µM 6.31× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 29.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -12.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2030 (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -15.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A-172 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.695 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.430 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA10]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[IRX3]] | +0.72 | +0.62 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SRGN]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CSF3]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[DNER]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MT1E]] | +0.64 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[PTX3]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ADAMTS9]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[FOXL1]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 | same gene group; STRING 563; ⚠ same locus (6.6 kb, same strand: neighbours can correlate without regulation) |
| [[ZMYND8]] | +0.60 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[SH3RF3]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CCND3]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRLNT]] | -0.64 | -0.54 / -0.68 | both halves | 1e-05 | **novel candidate** |
| [[LINC01411]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ADAMTS16]] | -0.57 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[IGFN1]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[PSG9]] | -0.52 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[IGFBP3]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CPA4]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[VSTM4]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[LINC00536]] | -0.48 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[C5orf46]] | -0.46 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[TIMP3]] | -0.46 | -0.40 / -0.41 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ANXA10]] | -0.45 | -0.37 / -0.46 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises FOXC2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[TSC22D3]] | B | TSC22D3 activity raises FOXC2's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without TSC22D3 | 0.093 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[FOXL1]] | C | FOXL1 activity raises FOXC2's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 3.24× lower at baseline in the lines without FOXL1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A; co-absent with the target |
| [[EDIL3]] | C | EDIL3 activity raises FOXC2's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 3.16× lower at baseline in the lines without EDIL3 | 0.031 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[SRGN]] | C | SRGN activity raises FOXC2's level | lines that do not express SRGN (30) vs lines expressing it (20) | 3.60× lower at baseline in the lines without SRGN | 0.035 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |
| [[CPA4]] | C | CPA4 activity raises FOXC2's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without CPA4 | 0.086 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises FOXC2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.97× lower at baseline in the lines without LINC01411 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 10, C 15. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00536]] | B | FOXC2 activity raises LINC00536's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.63× lower at baseline in the lines without FOXC2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[ADPRHL1]] | B | FOXC2 activity raises ADPRHL1's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 1.61× lower at baseline in the lines without FOXC2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[TSC22D3]] | B | FOXC2 activity raises TSC22D3's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without FOXC2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[LRIG1]] | B | FOXC2 activity raises LRIG1's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 1.79× lower at baseline in the lines without FOXC2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | FOXC2 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FOXC2 (33) vs lines expressing it (15) | the lines without FOXC2: 1.18× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[TGFBR2]] | B | FOXC2 activity raises TGFBR2's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without FOXC2 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[ANGPTL4]] | B | FOXC2 activity raises ANGPTL4's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without FOXC2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[DUSP1]] | B | FOXC2 activity raises DUSP1's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.12× lower at baseline in the lines without FOXC2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[MT2A]] | B | FOXC2 activity raises MT2A's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without FOXC2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[IGFBP3]] | B | FOXC2 activity raises IGFBP3's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 3.88× lower at baseline in the lines without FOXC2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[LINC01411]] | C | FOXC2 activity raises LINC01411's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 6.53× lower at baseline in the lines without FOXC2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[SRGN]] | C | FOXC2 activity raises SRGN's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 6.63× lower at baseline in the lines without FOXC2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.5, 14.6); signed map (16.0, 31.4). **Vector** length 60.9, 22.3% of its response variance represented; |z| ≥ 3 in 432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +3.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +2.6 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.6 | +3.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.8 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -2.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.3 | +6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:86,566,829-86,569,728 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MFH-1; previously FKHL14 |
| Gene groups (HGNC) | Forkhead boxes |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Formation of intermediate mesoderm; Formation of the ureteric bud; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99958](https://www.uniprot.org/uniprotkb/Q99958) (Forkhead box protein C2):

> Transcriptional activator.

**Summary**, from NCBI Gene [2303](https://www.ncbi.nlm.nih.gov/gene/2303):

> This gene belongs to the forkhead family of transcription factors which is characterized by a distinct DNA-binding forkhead domain. The specific function of this gene has not yet been determined; however, it may play a role in the development of mesenchymal tissues. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3801) · Entrez [2303](https://www.ncbi.nlm.nih.gov/gene/2303) · UniProt [Q99958](https://www.uniprot.org/uniprotkb/Q99958) · Ensembl [ENSG00000176692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176692)

## Data

Gene col 10741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10741); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10741]; `tensor/DDL_lfc|DDL_z.npy` [10741]; `embed/gene_vectors.npy` [10741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10741 or target_col == 10741). Every well: [[FOXC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
