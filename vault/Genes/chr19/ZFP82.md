---
symbol: "ZFP82"
type: "gene"
col: 11155
ensembl_id: "ENSG00000181007"
name: "ZFP82 zinc finger protein"
location: "19q13.12"
module: 129
arm: "+"
pooled_cpm: 12.61
n_lines_expressing: 30
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# ZFP82

*ZFP82 zinc finger protein* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.41× (z +5.9, q 2e-06, up in 10 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.81× (z +5.6, q 8e-06, up in 13 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.476× (z -18.7, q 0e+00, down in 24 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF569]] (+0.73, fdr 7e-06), [[ZNF566]] (+0.69, fdr 7e-06, ⚠ same locus), [[ZNF571]] (+0.68, fdr 9e-06), [[ZNF527]] (+0.66, fdr 1e-05); moves opposite to [[ATP11C]] (-0.53, fdr 4e-05), [[KDM6A]] (-0.44, fdr 2e-04), [[RFX3]] (-0.44, fdr 8e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[ZNF461]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.9 | 2e-06 | 10/19 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +5.6 | 8e-06 | 13/28 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 4e-05 | 11/28 (NCI-H2347, SW 900, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.22×** | +5.0 | 6e-05 | 12/28 (CFPAC-1, HOP62, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.6 | 4e-04 | 12/28 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.3 | 0.002 | 9/26 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.004 | 13/28 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.0 | 0.004 | 0/28 | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.043 | 6/28 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.059 | 11/28 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.3 | 0.059 | 8/28 (NCI-H2347, A498, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.476×** | -18.7 | 0e+00 | 24/27 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.497×** | -12.0 | 1e-30 | 22/27 (HOP62, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.574×** | -9.5 | 3e-19 | 21/27 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.756×** | -4.8 | 2e-04 | 14/26 (CHP-212, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.760×** | -4.7 | 3e-04 | 11/28 (A498, HOP62, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.794×** | -4.1 | 0.004 | 12/28 (HOP62, SNU-423, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.010 | 10/27 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.808×** | -3.8 | 0.010 | 10/28 (HOP62, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.868× | -3.6 | 0.022 | 7/28 (HOP62, H4, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.844× | -3.0 | 0.14 | 6/28 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 44.0 | 6 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +23.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.13× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -10.1) |
| [[C32 (line)]] | wt | 34.7 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -17.2) |
| [[HOP62 (line)]] | alt | 30.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 31.4 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +9.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -13.0) |
| [[J82 (line)]] | alt | 44.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +15.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.5) |
| [[SW 900 (line)]] | alt | 24.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -10.7) |
| [[A549 (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -9.6) |
| [[AN3 CA (line)]] | alt | 48.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -14.7) |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -15.2) |
| [[C-33 A (line)]] | alt | 59.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 9.44 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.41× (z +10.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.125× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -8.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H1792 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.112× (z -8.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -8.5) |
| [[A-172 (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.928 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.961 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.990 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF569]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF566]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 | same gene group; ⚠ same locus (26.5 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF571]] | +0.68 | +0.66 / +0.57 | both halves | 9e-06 | same gene group |
| [[ZNF527]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 | same gene group |
| [[ZNF567]] | +0.65 | +0.68 / +0.50 | both halves | 1e-05 | same gene group |
| [[ZNF420]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZNF790-AS1]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[ZNF559]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 | same gene group |
| [[ZNF461]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 | same gene group |
| [[ZNF45]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 | same gene group |
| [[ZNF875]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 | same gene group |
| [[FITM2]] | +0.55 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[CENATAC]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | -0.53 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[KDM6A]] | -0.44 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[RFX3]] | -0.44 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[PEAK1]] | -0.43 | -0.34 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZFP82's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MICU3]] | C | MICU3 activity raises ZFP82's level | lines that do not express MICU3 (19) vs lines expressing it (31) | 5.15× lower at baseline in the lines without MICU3 | 0.049 | ⚠ within organs, on part of the lines; co-absent genes; also absent: BVES-AS1, EVL, MIR130AHG; co-absent with the target |
| [[ZNF354C]] | C | ZNF354C activity raises ZFP82's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 4.67× lower at baseline in the lines without ZNF354C | 0.095 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF461]] | B | ZFP82 activity raises ZNF461's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 2.69× lower at baseline in the lines without ZFP82 | 0.016 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG |
| [[POLR3A]] | B | ZFP82 activity raises POLR3A's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 1.09× lower at baseline in the lines without ZFP82 | 0.063 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG |
| [[CDC16]] | B | ZFP82 activity lowers CDC16's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 1.28× higher at baseline in the lines without ZFP82 | 0.064 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG |
| [[RBM18]] | B | ZFP82 activity lowers RBM18's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 1.32× higher at baseline in the lines without ZFP82 | 0.075 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG |
| [[MICU3]] | C | ZFP82 activity raises MICU3's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 5.97× lower at baseline in the lines without ZFP82 | 0.086 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG; co-absent with the target |

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.4, -2.9); signed map (-18.2, -17.0). **Vector** length 60.9, 12.4% of its response variance represented; |z| ≥ 3 in 603 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.0 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +4.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -9.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -18.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | -1.7 | -4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ZFP82 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,383,120-36,418,644 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45380, KIAA1948; previously ZNF545 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N141](https://www.uniprot.org/uniprotkb/Q8N141) (Zinc finger protein 82 homolog):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [284406](https://www.ncbi.nlm.nih.gov/gene/284406):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28682) · Entrez [284406](https://www.ncbi.nlm.nih.gov/gene/284406) · UniProt [Q8N141](https://www.uniprot.org/uniprotkb/Q8N141) · Ensembl [ENSG00000181007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181007)

## Data

Gene col 11155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11155); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11155]; `tensor/DDL_lfc|DDL_z.npy` [11155]; `embed/gene_vectors.npy` [11155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11155 or target_col == 11155). Every well: [[ZFP82 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP82.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
