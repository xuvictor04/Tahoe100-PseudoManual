---
symbol: "SRGN"
type: "gene"
col: 4379
ensembl_id: "ENSG00000122862"
name: "serglycin"
location: "10q22.1"
module: 104
arm: "+"
pooled_cpm: 71.83
n_lines_expressing: 20
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 42
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# SRGN

*serglycin* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.00× (z +9.4, q 2e-18, up in 15 of 18 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +6.1, q 1e-07, up in 12 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.257×, NCI-H460 0.230×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (A549 0.186×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTX3]] (+0.77, fdr 7e-06), [[FOXC2]] (+0.66, fdr 7e-06), [[CSF3]] (+0.63, fdr 7e-06); moves opposite to [[VSTM4]] (-0.66, fdr 7e-06), [[LINC01411]] (-0.58, fdr 2e-05), [[MIR493HG]] (-0.57, fdr 1e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SIRLNT]] → it (grade C ⚠); 42 go from it, the strongest it → [[LINC01119]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **5.00×** | +9.4 | 2e-18 | 15/18 (HOP62, H4, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.64×** | +7.4 | 5e-11 | 10/15 (PANC-1, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.37×** | +6.7 | 5e-09 | 14/15 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +6.1 | 1e-07 | 12/19 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.79×** | +6.1 | 1e-07 | 16/18 (A-172, SNU-423, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **2.21×** | +4.7 | 2e-04 | 14/18 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.28×** | +4.7 | 2e-04 | 18/19 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.3 | 0.001 | 8/17 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.03×** | +4.2 | 0.002 | 12/18 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.00×** | +4.1 | 0.002 | 11/18 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.004 | 16/18 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +3.9 | 0.004 | 17/19 (RPMI-7951, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.90×** | +3.8 | 0.006 | 12/18 (NCI-H2030, NCI-H460, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.91×** | +3.7 | 0.009 | 14/18 (A-172, J82, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +3.7 | 0.010 | 8/19 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.84×** | +3.6 | 0.010 | 14/18 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.75×** | +3.3 | 0.030 | 12/18 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.74×** | +3.2 | 0.038 | 13/18 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.046 | 8/18 (HOP62, PANC-1, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.73×** | +3.1 | 0.046 | 17/18 (A498, HS-578T, …) | top dose only | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **1.66×** | +2.9 | 0.099 | 13/19 (HS-578T, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4379.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.257×, NCI-H460 0.230×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (A549 0.186×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.583× | -3.2 | 0.60 | 14/18 (MIA PaCa-2, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 53.0 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 179 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +8.9) | — |
| [[A498 (line)]] | wt | 150 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.37× (z +10.0) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[J82 (line)]] | alt | 65.5 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.04× (z +11.0) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A549 (line)]] | wt | 121 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -8.8) |
| [[HOP62 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.14× (z +9.1) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H2030 (line)]] | alt | 290 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 324 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 186 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 254 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 499 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.61 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTX3]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[FOXC2]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CSF3]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SLC7A2]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CCND3]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[CAVIN2]] | +0.57 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[KLF9]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[NNMT]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SLC1A3]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[CSF1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[MTMR7]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ADAMTS9]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSTM4]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[MIR493HG]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[LINC01705]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ADAMTS14]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ADAMTS16]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[SPOCD1]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[INSYN2B]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[COL5A1]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[KCNMA1]] | -0.51 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[KCNK3]] | -0.50 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ZFP28]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRLNT]] | C | SIRLNT activity raises SRGN's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 13.64× lower at baseline in the lines without SIRLNT | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises SRGN's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 6.63× lower at baseline in the lines without FOXC2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[KCNMA1]] | C | KCNMA1 activity raises SRGN's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 8.17× lower at baseline in the lines without KCNMA1 | 0.004 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises SRGN's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 8.04× lower at baseline in the lines without LINC01411 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[DNER]] | C | DNER activity raises SRGN's level | lines that do not express DNER (32) vs lines expressing it (18) | 5.86× lower at baseline in the lines without DNER | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[PKD1L1-AS1]] | C | PKD1L1-AS1 activity raises SRGN's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 5.03× lower at baseline in the lines without PKD1L1-AS1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[CAVIN2]] | C | CAVIN2 activity raises SRGN's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 3.37× lower at baseline in the lines without CAVIN2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9; co-absent with the target |
| [[ARHGEF6]] | C | ARHGEF6 activity raises SRGN's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 4.57× lower at baseline in the lines without ARHGEF6 | 0.066 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent; co-absent with the target |
| [[IL1R1]] | C | IL1R1 activity raises SRGN's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 5.82× lower at baseline in the lines without IL1R1 | 0.084 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1; co-absent with the target |
| [[LOXL2]] | C | LOXL2 activity raises SRGN's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 5.57× lower at baseline in the lines without LOXL2 | 0.094 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises SRGN's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 4.37× lower at baseline in the lines without INSYN2B | 0.098 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 22, C 20. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01119]] | B | SRGN activity raises LINC01119's level | lines that do not express SRGN (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without SRGN | 0.013 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | SRGN activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.78× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | SRGN activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.23× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | B | SRGN activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.46× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Adagrasib (drug)]] 0.5 µM | B | SRGN activity lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.32× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Digitoxin (drug)]] 0.05 µM | B | SRGN activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.78× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Penfluridol (drug)]] 0.5 µM | B | SRGN activity lowers the cells' numbers under Penfluridol 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.52× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Naproxen (drug)]] 5 µM | B | SRGN activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.80× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[γ-Oryzanol (drug)]] 0.05 µM | B | SRGN activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.81× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Vismodegib (drug)]] 5 µM | B | SRGN activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.45× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Piroxicam (drug)]] 0.05 µM | B | SRGN activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.77× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | B | SRGN activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.41× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.5, 14.7); signed map (16.4, 31.3). **Vector** length 71.7, 28.3% of its response variance represented; |z| ≥ 3 in 475 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.8 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +4.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.4 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | serglycin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:69,088,103-69,104,805 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PPG; previously PRG, PRG1 |
| Gene groups (HGNC) | Proteoglycans |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P10124](https://www.uniprot.org/uniprotkb/P10124) (Serglycin):

> Plays a role in formation of mast cell secretory granules and mediates storage of various compounds in secretory vesicles. Required for storage of some proteases in both connective tissue and mucosal mast cells and for storage of granzyme B in T-lymphocytes. Plays a role in localizing neutrophil elastase in azurophil granules of neutrophils. Mediates processing of MMP2. Plays a role in cytotoxic cell granule-mediated apoptosis by forming a complex with granzyme B which is delivered to cells by …

**Summary**, from NCBI Gene [5552](https://www.ncbi.nlm.nih.gov/gene/5552):

> This gene encodes a protein best known as a hematopoietic cell granule proteoglycan. Proteoglycans stored in the secretory granules of many hematopoietic cells also contain a protease-resistant peptide core, which may be important for neutralizing hydrolytic enzymes. This encoded protein was found to be associated with the macromolecular complex of granzymes and perforin, which may serve as a mediator of granule-mediated apoptosis. Two transcript variants, only one of them protein-coding, have …

**Accessions** — [HGNC:9361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9361) · Entrez [5552](https://www.ncbi.nlm.nih.gov/gene/5552) · UniProt [P10124](https://www.uniprot.org/uniprotkb/P10124) · Ensembl [ENSG00000122862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122862)

## Data

Gene col 4379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4379); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4379]; `tensor/DDL_lfc|DDL_z.npy` [4379]; `embed/gene_vectors.npy` [4379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4379 or target_col == 4379). Every well: [[SRGN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRGN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
