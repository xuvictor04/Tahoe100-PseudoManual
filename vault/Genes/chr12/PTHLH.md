---
symbol: "PTHLH"
type: "gene"
col: 1507
ensembl_id: "ENSG00000087494"
name: "parathyroid hormone like hormone"
location: "12p11.22"
module: 81
arm: "+"
pooled_cpm: 9.16
n_lines_expressing: 30
n_dd_up: 14
n_dd_down: 30
n_dd_up_clean: 9
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 26
direction_downstream: 31
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# PTHLH

*parathyroid hormone like hormone* — 12p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.40× (z +12.5, q 5e-33, up in 14 of 25 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 3.23× (z +11.4, q 1e-27, up in 20 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (none with an alert); the strongest is [[Budesonide (drug)]] 5 µM: 0.374× (z -9.9, q 1e-20, down in 19 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HBEGF]] (+0.73, fdr 7e-06), [[IL11]] (+0.69, fdr 7e-06), [[FZD8]] (+0.68, fdr 7e-06); moves opposite to [[COPS8]] (-0.61, fdr 9e-06), [[ACSL1]] (-0.60, fdr 8e-06), [[CCND3]] (-0.58, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[SOX9]] → it (grade B ⚠); 31 go from it, the strongest it → [[FAM107B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.40×** | +12.5 | 5e-33 | 14/25 (PANC-1, HT-29, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.23×** | +11.4 | 1e-27 | 20/25 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +10.0 | 4e-21 | 16/25 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +8.0 | 1e-13 | 16/24 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +5.6 | 2e-06 | 9/26 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +5.6 | 2e-06 | 7/24 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.76×** | +5.3 | 1e-05 | 6/17 (SW 900, NCI-H1792, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.0 | 4e-05 | 9/26 (NCI-H460, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.58×** | +4.6 | 3e-04 | 6/24 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.5 | 4e-04 | 10/28 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.45×** | +3.6 | 0.017 | 0/13 | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.056 | 6/25 (HOP62, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.1 | 0.084 | 5/16 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.095 | 5/26 (NCI-H1792, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, none with an alert; shown: the 15 strongest. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | **0.374×** | -9.9 | 1e-20 | 19/27 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.375×** | -9.9 | 1e-20 | 21/26 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.442×** | -8.2 | 4e-14 | 18/25 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.454×** | -7.9 | 3e-13 | 21/25 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.465×** | -7.7 | 1e-12 | 18/24 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.469×** | -7.6 | 2e-12 | 19/25 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.485×** | -7.3 | 3e-11 | 17/26 (A-172, HOP62, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.503×** | -6.9 | 3e-10 | 17/26 (HOP62, SW 900, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.518×** | -6.6 | 2e-09 | 18/25 (HOP62, SW 900, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.639×** | -6.4 | 1e-08 | 17/25 (HOP62, A-172, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.547×** | -6.1 | 6e-08 | 17/26 (HOP62, SW 900, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.549×** | -5.8 | 3e-07 | 14/25 (HOP62, RPMI-7951, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -5.5 | 1e-06 | 14/26 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.589×** | -5.3 | 4e-06 | 18/25 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.568×** | -5.3 | 5e-06 | 16/24 (HOP62, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 32.2 | 0 | 17 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0872× (z -14.5) |
| [[Hs 766T (line)]] | wt | 133 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0422× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0534× (z -16.2) |
| [[A-172 (line)]] | wt | 9.11 | 0 | 3 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0739× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 2 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0239× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.208× (z -8.5) |
| [[PANC-1 (line)]] | alt | 6.67 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.76× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 11.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +8.9) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 8.97 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +9.0) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HepG2_C3A (line)]] | wt | 5.22 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +9.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HS-578T (line)]] | alt | 8.00 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0978× (z -9.2) |
| [[HT-29 (line)]] | alt | 4.44 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +9.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 3.89 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0412× (z -9.3) |
| [[SW 900 (line)]] | alt | 9.55 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.117× (z -8.6) |
| [[SW480 (line)]] | alt | 5.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +9.5) | — |
| [[A-427 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.880 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HBEGF]] | +0.73 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[IL11]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 | STRING 763 |
| [[FZD8]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[DPF3]] | +0.67 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ANXA10]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CSMD2]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MDGA1]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CD44]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[IL1B]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 | STRING 455 |
| [[LINC00973]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PKIA]] | +0.64 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[FAM107B]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8]] | -0.61 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[ACSL1]] | -0.60 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[CCND3]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SAA1]] | -0.56 | -0.65 / -0.48 | both halves | 2e-05 | same gene group; pathway: GPCR ligand binding |
| [[ARMC8]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ADGRG2]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[TSC22D3]] | -0.53 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[NNMT]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[STOM]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[IRAK3]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[PID1]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 14, C 12. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX9]] | B | SOX9 activity raises PTHLH's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.63× lower at baseline in the lines without SOX9 | 0.007 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[FAM107B]] | B | FAM107B activity raises PTHLH's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.59× lower at baseline in the lines without FAM107B | 0.012 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[PRSS23]] | B | PRSS23 activity raises PTHLH's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.52× lower at baseline in the lines without PRSS23 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[ABCA13]] | B | ABCA13 activity raises PTHLH's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without ABCA13 | 0.032 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |
| [[IGFBP6]] | B | IGFBP6 activity raises PTHLH's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 2.25× lower at baseline in the lines without IGFBP6 | 0.049 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[TIMP3]] | B | TIMP3 activity weakens PTHLH's drug response | lines that do not express TIMP3 (16) vs lines expressing it (12) | the lines without TIMP3 respond 1.18× as strongly (z diff -1.07); strongest at Homoharringtonine 5 µM: 2.76x vs 0.84x (z diff -7.1) | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; target measured in part of the lines; artifact flags |
| [[SLIT2]] | B | SLIT2 activity raises PTHLH's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without SLIT2 | 0.057 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1 |
| [[SHISAL1]] | B | SHISAL1 activity raises PTHLH's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without SHISAL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[NR3C1]] | B | NR3C1 activity lowers PTHLH's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TIMP3]] | B | TIMP3 activity raises PTHLH's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without TIMP3 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[LRRC49]] | B | LRRC49 activity raises PTHLH's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without LRRC49 | 0.069 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[CD44]] | B | CD44 activity raises PTHLH's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.51× lower at baseline in the lines without CD44 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 15, C 16. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM107B]] | B | PTHLH activity raises FAM107B's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 3.83× lower at baseline in the lines without PTHLH | 0.004 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[PRSS23]] | B | PTHLH activity raises PRSS23's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.96× lower at baseline in the lines without PTHLH | 0.007 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[SYNJ2]] | B | PTHLH activity raises SYNJ2's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without PTHLH | 0.018 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[SOX9]] | B | PTHLH activity raises SOX9's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without PTHLH | 0.023 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[EHD1]] | B | PTHLH activity raises EHD1's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 1.42× lower at baseline in the lines without PTHLH | 0.024 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[CD44]] | B | PTHLH activity raises CD44's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 3.42× lower at baseline in the lines without PTHLH | 0.029 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[HRH1]] | B | PTHLH activity raises HRH1's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without PTHLH | 0.042 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[TPBG]] | B | PTHLH activity raises TPBG's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.49× lower at baseline in the lines without PTHLH | 0.056 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[CXCL8]] | B | PTHLH activity raises CXCL8's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 3.98× lower at baseline in the lines without PTHLH | 0.063 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[STK10]] | B | PTHLH activity raises STK10's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 1.81× lower at baseline in the lines without PTHLH | 0.070 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[IER3]] | B | PTHLH activity raises IER3's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 1.88× lower at baseline in the lines without PTHLH | 0.074 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[LINC01605]] | B | PTHLH activity raises LINC01605's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without PTHLH | 0.074 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.0, 12.3); signed map (17.8, 49.9). **Vector** length 89.2, 26.0% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.59 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.8 | +12.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.3 | -7.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.3 | -7.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.2 | -7.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.1 | -9.9 |

## What is on record

|  |  |
|---|---|
| Name | parathyroid hormone like hormone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.22 — chr12:27,958,084-27,972,733 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTHRP, HHM, PLP, PTHR |
| Gene groups (HGNC) | Receptor ligands; Neuropeptides |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: Class B/2 (Secretin family receptors); G alpha (s) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P12272](https://www.uniprot.org/uniprotkb/P12272) (Parathyroid hormone-related protein):

> Neuroendocrine peptide which is a critical regulator of cellular and organ growth, development, migration, differentiation and survival and of epithelial calcium ion transport. Acts by binding to its receptor, PTH1R, activating G protein-coupled receptor signaling. Regulates endochondral bone development and epithelial-mesenchymal interactions during the formation of the mammary glands and teeth (By similarity). Required for skeletal homeostasis. Promotes mammary mesenchyme differentiation and …

**Summary**, from NCBI Gene [5744](https://www.ncbi.nlm.nih.gov/gene/5744):

> The protein encoded by this gene is a member of the parathyroid hormone family. This hormone, via its receptor, PTHR1, regulates endochondral bone development and epithelial-mesenchymal interactions during the formation of the mammary glands and teeth. It is responsible for most cases of humoral hypercalcemia of malignancy, and mutations in this gene are associated with brachydactyly type E2 (BDE2). Alternatively spliced transcript variants have been found for this gene. There is also evidence …

**Accessions** — [HGNC:9607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9607) · Entrez [5744](https://www.ncbi.nlm.nih.gov/gene/5744) · UniProt [P12272](https://www.uniprot.org/uniprotkb/P12272) · Ensembl [ENSG00000087494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087494)

## Data

Gene col 1507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1507); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1507]; `tensor/DDL_lfc|DDL_z.npy` [1507]; `embed/gene_vectors.npy` [1507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1507 or target_col == 1507). Every well: [[PTHLH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTHLH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
