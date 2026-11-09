---
symbol: "CYRIA"
type: "gene"
col: 12480
ensembl_id: "ENSG00000197872"
name: "CYFIP related Rac1 interactor A"
location: "2p24.2"
module: 14
arm: "+"
pooled_cpm: 12.09
n_lines_expressing: 26
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 24
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CYRIA

*CYFIP related Rac1 interactor A* — 2p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 5.82× (z +29.8, q 0e+00, up in 22 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.782× (z -4.2, q 0.019, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBB2B]] (+0.65, fdr 1e-05), [[CADM1]] (+0.64, fdr 7e-06), [[SH3BP5]] (+0.64, fdr 9e-06); moves opposite to [[ACAD9]] (-0.62, fdr 4e-05), [[TIMM23B-AGAP6]] (-0.59, fdr 1e-05), [[DUS2]] (-0.58, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MIR155HG]] → it (grade B ⚠); 3 go from it, the strongest it → [[FGFR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **5.82×** | +29.8 | 0e+00 | 22/23 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **5.73×** | +20.9 | 0e+00 | 23/24 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.18×** | +19.7 | 0e+00 | 18/24 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.05×** | +19.4 | 0e+00 | 22/23 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.41×** | +17.8 | 0e+00 | 21/24 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.34×** | +17.6 | 0e+00 | 20/23 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +14.3 | 1e-44 | 14/20 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.31×** | +9.2 | 4e-18 | 18/23 (SW1417, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +7.9 | 2e-13 | 1/11 (LOX-IMVI) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.60×** | +5.6 | 9e-07 | 9/23 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +5.4 | 4e-06 | 7/21 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.0 | 3e-05 | 9/18 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +4.7 | 9e-05 | 9/22 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.47×** | +4.6 | 1e-04 | 3/23 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.67×** | +4.4 | 4e-04 | 4/23 (NCI-H1573, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.001 | 8/22 (hTERT-HPNE, HEC-1-A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.003 | 6/23 (HS-578T, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -4.2 | 0.019 | 17/21 (SW 900, SW1417, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -3.9 | 0.022 | 12/23 (SW1417, A-172, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.797×** | -3.8 | 0.022 | 6/23 (A498, SW 900, …) | rises with dose |  |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.735×** | -3.7 | 0.024 | 2/23 (RPMI-7951, SW480) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | **0.735×** | -3.7 | 0.024 | 2/24 (SW1417, A498) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -3.7 | 0.024 | 2/24 (Hs 766T, RPMI-7951) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.033 | 13/24 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.750×** | -3.4 | 0.041 | 9/22 (A498, SW 900, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.048 | 7/23 (A498, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.757×** | -3.3 | 0.048 | 8/24 (NCI-H2030, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.752×** | -3.3 | 0.054 | 7/22 (A498, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.775× | -3.0 | 0.11 | 8/22 (A498, SW 900, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 15.3 | 6 | 1 | [[Tucidinostat (drug)]] 5 µM 8.50× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -12.8) |
| [[SW480 (line)]] | alt | 3.64 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 12.4× (z +15.0) | — |
| [[A498 (line)]] | wt | 121 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.9) | [[Clobetasol propionate (drug)]] 0.5 µM 0.245× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 9.47 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.43× (z +9.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.195× (z -12.8) |
| [[LoVo (line)]] | wt | 8.78 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.99× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 26.5 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.93× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0517× (z -13.8) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -12.0) |
| [[A-172 (line)]] | wt | 40.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 42.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.5) |
| [[A549 (line)]] | wt | 6.08 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.09× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 5.00 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.36× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 3.04 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.61× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 5.87 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -9.8) |
| [[SW 900 (line)]] | alt | 36.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -15.0) |
| [[A-427 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB2B]] | +0.65 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CADM1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SH3BP5]] | +0.64 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[CDK18]] | +0.63 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TMCC2]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[STARD5]] | +0.62 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[RTN4RL2]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TPPP]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.61 | +0.29 / +0.61 | both halves | 2e-04 |  |
| [[CGNL1]] | +0.61 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NDRG4]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[WDFY1]] | +0.61 | +0.43 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAD9]] | -0.62 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[TIMM23B-AGAP6]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[DUS2]] | -0.58 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ALG8]] | -0.58 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[DNAAF10]] | -0.58 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[MSANTD2]] | -0.57 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[MCM3AP]] | -0.57 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.56 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[HCFC1]] | -0.56 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[MIATNB]] | -0.55 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[LARP4B]] | -0.55 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[PIGG]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR155HG]] | B | MIR155HG activity raises CYRIA's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without MIR155HG | 0.059 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[LPCAT2]] | B | LPCAT2 activity raises CYRIA's level | lines that do not express LPCAT2 (9) vs lines expressing it (41) | 2.17× lower at baseline in the lines without LPCAT2 | 0.069 | ⚠ within organs, on part of the lines; also absent: E2F7, PARD3B |
| [[NGF]] | B | NGF activity raises CYRIA's level | lines that do not express NGF (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without NGF | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1 |
| [[RRAD]] | C | RRAD activity raises CYRIA's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without RRAD | 0.027 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGFR1]] | B | CYRIA activity raises FGFR1's level | lines that do not express CYRIA (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without CYRIA | 0.057 | ⚠ within organs, on part of the lines; also absent: PTGS2, ATP10A, VCAN |
| [[TOP1]] | B | CYRIA activity raises TOP1's level | lines that do not express CYRIA (24) vs lines expressing it (26) | 1.17× lower at baseline in the lines without CYRIA | 0.085 | ⚠ within organs, on part of the lines; also absent: PTGS2, ATP10A, VCAN |
| [[RRAD]] | C | CYRIA activity raises RRAD's level | lines that do not express CYRIA (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without CYRIA | 0.086 | ⚠ within organs, on part of the lines; also absent: PTGS2, ATP10A, VCAN; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.417). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, 0.5); signed map (-1.8, 20.4). **Vector** length 66.6, 16.6% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +29.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +17.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +17.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +4.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.4 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.9 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | CYFIP related Rac1 interactor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.2 — chr2:16,549,459-16,666,331 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566A1524, FLJ11080, CYRI-A; previously FAM49A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0Q0](https://www.uniprot.org/uniprotkb/Q9H0Q0) (CYFIP-related Rac1 interactor A):

> May negatively regulate RAC1 signaling and RAC1-driven cytoskeletal remodeling (Probable). May regulate chemotaxis, cell migration and epithelial polarization by controlling the polarity, plasticity, duration and extent of protrusions (Probable).

**Summary**, from NCBI Gene [81553](https://www.ncbi.nlm.nih.gov/gene/81553):

> Predicted to enable small GTPase binding activity. Predicted to be involved in regulation of actin filament polymerization. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25373) · Entrez [81553](https://www.ncbi.nlm.nih.gov/gene/81553) · UniProt [Q9H0Q0](https://www.uniprot.org/uniprotkb/Q9H0Q0) · Ensembl [ENSG00000197872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197872)

## Data

Gene col 12480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12480); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12480]; `tensor/DDL_lfc|DDL_z.npy` [12480]; `embed/gene_vectors.npy` [12480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12480 or target_col == 12480). Every well: [[CYRIA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYRIA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
