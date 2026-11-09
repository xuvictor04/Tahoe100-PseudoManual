---
symbol: "VGLL3"
type: "gene"
col: 13048
ensembl_id: "ENSG00000206538"
name: "vestigial like family member 3"
location: "3p12.1"
module: 120
arm: "+"
pooled_cpm: 29.76
n_lines_expressing: 20
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# VGLL3

*vestigial like family member 3* — 3p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.72× (z +18.2, q 0e+00, up in 13 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +12.6, q 3e-34, up in 4 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.776× (z -4.2, q 0.013, down in 6 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.143×, LOX-IMVI 0.260×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.170×; ⚠ cell-cycle shift, explains ~85% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H2347 0.166×; ⚠ cell-cycle shift, explains ~34% of this change); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H2347 0.204×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.463×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPM4]] (+0.55, fdr 4e-05), [[RBMS1]] (+0.54, fdr 3e-05), [[IGF2BP2]] (+0.54, fdr 2e-05); moves opposite to [[PDE8A]] (-0.49, fdr 4e-05), [[AZIN2]] (-0.46, fdr 5e-05), [[NGLY1]] (-0.45, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[STARD13]] → it (grade B ⚠); 7 go from it, the strongest it → [[THBS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.72×** | +18.2 | 0e+00 | 13/18 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +14.2 | 2e-43 | 14/16 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +12.6 | 3e-34 | 4/19 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +11.5 | 3e-28 | 12/17 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +8.8 | 2e-16 | 8/18 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.43×** | +5.9 | 3e-07 | 10/19 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +5.4 | 6e-06 | 7/19 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.52×** | +4.9 | 7e-05 | 5/18 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.7 | 1e-04 | 7/18 (A549, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 0.001 | 10/18 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 0.001 | 8/18 (NCI-H1573, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +4.1 | 0.002 | 7/18 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.41×** | +4.0 | 0.003 | 3/18 (HS-578T, H4, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.003 | 5/18 (HS-578T, SNU-423, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.003 | 6/18 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.008 | 8/18 (hTERT-HPNE, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.017 | 4/18 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.017 | 8/18 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.017 | 8/18 (hTERT-HPNE, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.024 | 7/19 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13048.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.143×, LOX-IMVI 0.260×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.170×; ⚠ cell-cycle shift, explains ~85% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H2347 0.166×; ⚠ cell-cycle shift, explains ~34% of this change); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H2347 0.204×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.463×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.776×** | -4.2 | 0.013 | 6/18 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.737× | -3.5 | 0.15 | 7/18 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.753× | -3.4 | 0.15 | 2/18 (HS-578T, CFPAC-1) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.31 | 1/18 (H4) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 289 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -19.6) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.204× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 73.5 | 3 (1 ⚠) | 0 | [[Peretinoin (drug)]] 5 µM 5.36× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 13.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +14.5) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[J82 (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -9.7) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.79 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM4]] | +0.55 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[RBMS1]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[IGF2BP2]] | +0.54 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[AHNAK]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[AOX1]] | +0.52 | +0.43 / +0.55 | both halves | 4e-05 |  |
| [[GPR87]] | +0.52 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[ACOT9]] | +0.52 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[CCBE1]] | +0.51 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[DDAH1]] | +0.51 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[STARD13]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[COL12A1]] | +0.51 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[LPP]] | +0.50 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE8A]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[AZIN2]] | -0.46 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[NGLY1]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CFAP36]] | -0.43 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[NQO2]] | -0.42 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[UBE2O]] | -0.42 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[RBCK1]] | -0.40 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[CRY2]] | -0.40 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD13]] | B | STARD13 activity lowers VGLL3's level | lines that do not express STARD13 (7) vs lines expressing it (43) | 1.71× higher at baseline in the lines without STARD13 | 0.054 | ⚠ within organs, on part of the lines |
| [[THBS1]] | B | THBS1 activity raises VGLL3's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 3.36× lower at baseline in the lines without THBS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[PRDM1]] | C | PRDM1 activity raises VGLL3's level | lines that do not express PRDM1 (15) vs lines expressing it (35) | 4.13× lower at baseline in the lines without PRDM1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PCED1B, AMIGO2, NRP1; co-absent with the target |
| [[KRT81]] | C | KRT81 activity raises VGLL3's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 3.29× lower at baseline in the lines without KRT81 | 0.083 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS1]] | B | VGLL3 activity raises THBS1's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without VGLL3 | 0.021 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882 |
| [[CACNA1C]] | B | VGLL3 activity weakens CACNA1C's drug response | lines that do not express VGLL3 (22) vs lines expressing it (14) | the lines without VGLL3 respond 1.88× as strongly (z diff -1.94); strongest at Idarubicin (hydrochloride) 5 µM: 2.59x vs 1.31x (z diff -4.0) | 0.074 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882; target measured in part of the lines; artifact flags |
| [[ST6GALNAC5]] | B | VGLL3 activity raises ST6GALNAC5's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 1.66× lower at baseline in the lines without VGLL3 | 0.088 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882 |
| [[PARVA]] | B | VGLL3 activity raises PARVA's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 1.50× lower at baseline in the lines without VGLL3 | 0.091 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882 |
| [[ADAM9]] | B | VGLL3 activity raises ADAM9's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 1.51× lower at baseline in the lines without VGLL3 | 0.093 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882 |
| [[PRDM1]] | C | VGLL3 activity raises PRDM1's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 3.24× lower at baseline in the lines without VGLL3 | 0.004 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882; co-absent with the target |
| [[KRT81]] | C | VGLL3 activity raises KRT81's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 4.15× lower at baseline in the lines without VGLL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.5, 17.5); signed map (19.8, 34.6). **Vector** length 69.8, 22.0% of its response variance represented; |z| ≥ 3 in 525 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +18.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +11.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +5.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +4.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.0 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +8.8 |
| fall | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.6 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -0.3 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.6 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | vestigial like family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p12.1 — chr3:86,876,388-86,991,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VGL-3 |
| Gene groups (HGNC) | Vestigial like family |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MV65](https://www.uniprot.org/uniprotkb/A8MV65) (Transcription cofactor vestigial-like protein 3):

> May act as a specific coactivator for the mammalian TEFs.

**Summary**, from NCBI Gene [389136](https://www.ncbi.nlm.nih.gov/gene/389136):

> Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24327) · Entrez [389136](https://www.ncbi.nlm.nih.gov/gene/389136) · UniProt [A8MV65](https://www.uniprot.org/uniprotkb/A8MV65) · Ensembl [ENSG00000206538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206538)

## Data

Gene col 13048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13048); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13048]; `tensor/DDL_lfc|DDL_z.npy` [13048]; `embed/gene_vectors.npy` [13048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13048 or target_col == 13048). Every well: [[VGLL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VGLL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
