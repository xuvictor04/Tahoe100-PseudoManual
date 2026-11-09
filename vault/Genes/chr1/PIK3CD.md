---
symbol: "PIK3CD"
type: "gene"
col: 10139
ensembl_id: "ENSG00000171608"
name: "phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit delta"
location: "1p36.22"
module: 206
arm: "+"
pooled_cpm: 14.08
n_lines_expressing: 42
n_dd_up: 34
n_dd_down: 13
n_dd_up_clean: 26
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 16
direction_downstream: 5
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# PIK3CD

*phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit delta* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.54× (z +21.5, q 0e+00, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.722× (z -5.3, q 6e-05, down in 16 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDPD5]] (+0.66, fdr 7e-06), [[CLIP2]] (+0.65, fdr 7e-06), [[N4BP3]] (+0.64, fdr 7e-06); moves opposite to [[MFSD14A]] (-0.51, fdr 2e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); 5 go from it, the strongest it → [[KLC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.54×** | +21.5 | 0e+00 | 33/38 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.76×** | +16.6 | 0e+00 | 38/40 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +14.5 | 1e-45 | 35/39 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +14.3 | 6e-44 | 35/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +14.2 | 8e-44 | 35/40 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +12.4 | 2e-33 | 26/38 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.3 | 8e-23 | 23/39 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +10.0 | 2e-21 | 12/19 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +8.4 | 3e-15 | 25/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +8.0 | 8e-14 | 24/39 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +6.7 | 9e-10 | 17/40 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 3e-09 | 22/37 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +6.3 | 1e-08 | 18/39 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.3 | 1e-08 | 13/30 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +5.6 | 9e-07 | 16/38 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.8 | 6e-05 | 11/40 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **1.20×** | +4.2 | 6e-04 | 11/40 (LOX-IMVI, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.722×** | -5.3 | 6e-05 | 16/39 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.763×** | -4.4 | 0.003 | 11/39 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.833×** | -4.2 | 0.004 | 16/40 (SW 900, LOX-IMVI, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.774×** | -4.2 | 0.004 | 13/39 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -4.0 | 0.008 | 4/40 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.785×** | -3.9 | 0.008 | 12/39 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.792×** | -3.8 | 0.012 | 12/39 (H4, SNU-423, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.048 | 9/39 (SNU-423, HOP62, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.064 | 10/40 (HOP62, SW48, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.073 | 9/39 (SNU-423, HOP62, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.690×** | -3.2 | 0.073 | 8/35 (HS-578T, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.824×** | -3.2 | 0.073 | 7/39 (CFPAC-1, HOP62, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.825×** | -3.1 | 0.073 | 7/40 (HOP62, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.079 | 10/40 (CFPAC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 47.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +22.9) | — |
| [[HOP62 (line)]] | alt | 49.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +24.7) | — |
| [[HS-578T (line)]] | alt | 17.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.2) | — |
| [[LoVo (line)]] | wt | 6.61 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 11.4× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 43.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +20.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 6.70 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.72× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.05× (z +8.7) | — |
| [[J82 (line)]] | alt | 28.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +16.8) | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.2) | — |
| [[A-427 (line)]] | wt | 18.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.207× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 5.23 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 15.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -9.0) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SW480 (line)]] | alt | 14.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.24× (z +8.7) | — |
| [[A-172 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDPD5]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 | pathway: PI Metabolism |
| [[CLIP2]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[N4BP3]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KLC3]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ARVCF]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SEMA7A]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SNX9]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 | STRING 660 |
| [[NDRG4]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[HMGA1]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[FGFR1]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 | pathway: Constitutive Signaling by Aberrant PI3K in Cancer; STRING 924 |
| [[SMS]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CALB2]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14A]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises PIK3CD's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without BCL2A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[FMNL1]] | B | FMNL1 activity raises PIK3CD's level | lines that do not express FMNL1 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without FMNL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, WIPF1, SOGA3 |
| [[AKT3]] | B | AKT3 activity raises PIK3CD's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without AKT3 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[IL11]] | B | IL11 activity raises PIK3CD's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.39× lower at baseline in the lines without IL11 | 0.027 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[IL23A]] | B | IL23A activity raises PIK3CD's level | lines that do not express IL23A (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without IL23A | 0.029 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[LINC00973]] | B | LINC00973 activity raises PIK3CD's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without LINC00973 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |
| [[RAB3B]] | B | RAB3B activity raises PIK3CD's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 2.31× lower at baseline in the lines without RAB3B | 0.051 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[LRRC49]] | B | LRRC49 activity raises PIK3CD's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.39× lower at baseline in the lines without LRRC49 | 0.051 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[SLC35F1]] | B | SLC35F1 activity raises PIK3CD's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 2.45× lower at baseline in the lines without SLC35F1 | 0.056 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[LPCAT2]] | B | LPCAT2 activity raises PIK3CD's level | lines that do not express LPCAT2 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without LPCAT2 | 0.056 | ⚠ within organs, on part of the lines; also absent: E2F7, PARD3B |
| [[FMNL1-DT]] | B | FMNL1-DT activity raises PIK3CD's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 2.33× lower at baseline in the lines without FMNL1-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[IGDCC4]] | B | IGDCC4 activity raises PIK3CD's level | lines that do not express IGDCC4 (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without IGDCC4 | 0.073 | ⚠ within organs, on part of the lines; also absent: C19orf18, ENSG00000176593, LINC02813; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLC3]] | B | PIK3CD activity raises KLC3's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 1.97× lower at baseline in the lines without PIK3CD | 0.033 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[RGPD8]] | B | PIK3CD activity raises RGPD8's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without PIK3CD | 0.045 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[PPP4R4]] | B | PIK3CD activity raises PPP4R4's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 3.71× lower at baseline in the lines without PIK3CD | 0.048 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[BCAS4]] | B | PIK3CD activity raises BCAS4's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without PIK3CD | 0.052 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[ZBTB46]] | B | PIK3CD activity raises ZBTB46's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without PIK3CD | 0.055 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.1, -2.4); signed map (-1.9, 43.8). **Vector** length 90.1, 19.6% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +21.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +4.0 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -3.2 | -5.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -4.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.6 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:9,629,889-9,729,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p110D |
| Gene groups (HGNC) | Phosphatidylinositol 3-kinase family |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 34 pathways, smallest: Co-stimulation by ICOS; Erythropoietin activates Phosphoinositide-3-kinase (PI3K); Interleukin receptor SHC signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O00329](https://www.uniprot.org/uniprotkb/O00329) (Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit delta isoform):

> Phosphoinositide-3-kinase (PI3K) phosphorylates phosphatidylinositol (PI) and its phosphorylated derivatives at position 3 of the inositol ring to produce 3-phosphoinositides. Uses ATP and PtdIns(4,5)P2 (phosphatidylinositol 4,5-bisphosphate) to generate phosphatidylinositol 3,4,5-trisphosphate (PIP3). PIP3 plays a key role by recruiting PH domain-containing proteins to the membrane, including AKT1 and PDPK1, activating signaling cascades involved in cell growth, survival, proliferation, …

**Summary**, from NCBI Gene [5293](https://www.ncbi.nlm.nih.gov/gene/5293):

> Phosphoinositide 3-kinases (PI3Ks) phosphorylate inositol lipids and are involved in the immune response. The protein encoded by this gene is a class I PI3K found primarily in leukocytes. Like other class I PI3Ks (p110-alpha p110-beta, and p110-gamma), the encoded protein binds p85 adapter proteins and GTP-bound RAS. However, unlike the other class I PI3Ks, this protein phosphorylates itself, not p85 protein.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:8977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8977) · Entrez [5293](https://www.ncbi.nlm.nih.gov/gene/5293) · UniProt [O00329](https://www.uniprot.org/uniprotkb/O00329) · Ensembl [ENSG00000171608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171608)

## Data

Gene col 10139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10139); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10139]; `tensor/DDL_lfc|DDL_z.npy` [10139]; `embed/gene_vectors.npy` [10139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10139 or target_col == 10139). Every well: [[PIK3CD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3CD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
