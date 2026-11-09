---
symbol: "CXCL13"
type: "gene"
col: 7960
ensembl_id: "ENSG00000156234"
name: "C-X-C motif chemokine ligand 13"
location: "4q21.1"
module: 26
arm: "+"
pooled_cpm: 3.28
n_lines_expressing: 42
n_dd_up: 33
n_dd_down: 8
n_dd_up_clean: 28
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CXCL13

*C-X-C motif chemokine ligand 13* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.21× (z +17.0, q 0e+00, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.198× (z -13.6, q 3e-39, down in 31 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAM]] (+0.79, fdr 7e-06), [[LINC02398]] (+0.75, fdr 7e-06), [[NEB]] (+0.74, fdr 7e-06); moves opposite to [[COPG2]] (-0.61, fdr 1e-05), [[DSCC1]] (-0.59, fdr 1e-05), [[AP3M2]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01917]] → it (grade B ⚠); 11 go from it, the strongest it → [[BTBD10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.21×** | +17.0 | 0e+00 | 19/25 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.93×** | +11.0 | 8e-26 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.68×** | +10.9 | 2e-25 | 24/32 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.42×** | +10.3 | 9e-23 | 18/25 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.64×** | +10.0 | 1e-21 | 3/6 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **8.41×** | +9.3 | 1e-18 | 25/30 (LoVo, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +9.1 | 6e-18 | 18/27 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.97×** | +8.0 | 9e-14 | 15/38 (LS 180, NCI-H460, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.47×** | +7.6 | 2e-12 | 26/37 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +7.0 | 1e-10 | 4/15 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.03×** | +5.9 | 2e-07 | 17/32 (LS 180, A498, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.88×** | +5.3 | 6e-06 | 11/38 (NCI-H460, A498, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.1 | 1e-05 | 9/26 (LS 180, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.78×** | +4.7 | 1e-04 | 12/26 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +4.3 | 6e-04 | 10/38 (LoVo, A498, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.001 | 5/39 (A-427, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 3/38 (HOP62, BT-474, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.002 | 7/35 (LoVo, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.004 | 5/39 (LoVo, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.006 | 2/37 (NCI-H2030, LS 180) | rises with dose | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.198×** | -13.6 | 3e-39 | 31/39 (NCI-H1573, HCT15, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.478×** | -6.2 | 2e-07 | 18/38 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.718×** | -3.9 | 0.015 | 10/40 (C-33 A, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **0.658×** | -3.4 | 0.088 | 11/15 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.465×** | -3.4 | 0.088 | 9/23 (NCI-H1792, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.680×** | -3.3 | 0.097 | 8/37 (A-427, HCT15, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.762×** | -3.2 | 0.097 | 6/37 (AN3 CA, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.673×** | -3.2 | 0.098 | 7/38 (HS-578T, A498, …) | top dose only | plate-row cell shift |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.693× | -3.1 | 0.13 | 7/38 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.78 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0155× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0972× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 4.63 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +12.3) | [[Malotilate (drug)]] 0.5 µM 0.0644× (z -9.4) |
| [[C32 (line)]] | wt | 6.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +12.0) | — |
| [[LoVo (line)]] | wt | 3.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 5.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0786× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.977 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAM]] | +0.79 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[LINC02398]] | +0.75 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[NEB]] | +0.74 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.73 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[FSIP2-AS1]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[GRK7]] | +0.70 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[HSD17B3]] | +0.70 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[LINC02763]] | +0.70 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SLC26A7]] | +0.70 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[LINC01208]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG2]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[DSCC1]] | -0.59 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.59 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[GTF2E2]] | -0.58 | -0.55 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01917]] | B | LINC01917 activity raises CXCL13's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.76× lower at baseline in the lines without LINC01917 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises CXCL13's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.02× lower at baseline in the lines without FSIP2-AS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC00504]] | B | LINC00504 activity raises CXCL13's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.41× lower at baseline in the lines without LINC00504 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTBD10]] | B | CXCL13 activity lowers BTBD10's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without CXCL13 | 0.004 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[LINC01618]] | B | CXCL13 activity raises LINC01618's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without CXCL13 | 0.027 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[CASS4]] | B | CXCL13 activity raises CASS4's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without CXCL13 | 0.028 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[LINC02937]] | B | CXCL13 activity raises LINC02937's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without CXCL13 | 0.030 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[ITFG2-AS1]] | B | CXCL13 activity raises ITFG2-AS1's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without CXCL13 | 0.039 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[CMYA5]] | B | CXCL13 activity raises CMYA5's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 2.07× lower at baseline in the lines without CXCL13 | 0.051 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[DNAI7]] | B | CXCL13 activity raises DNAI7's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without CXCL13 | 0.059 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[HULC]] | B | CXCL13 activity raises HULC's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.34× lower at baseline in the lines without CXCL13 | 0.069 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[PRR4]] | B | CXCL13 activity raises PRR4's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without CXCL13 | 0.077 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[C21orf62-AS1]] | B | CXCL13 activity raises C21orf62-AS1's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without CXCL13 | 0.082 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[LINC01762]] | B | CXCL13 activity raises LINC01762's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without CXCL13 | 0.090 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.7, 16.4); signed map (23.8, 1.7). **Vector** length 67.1, 12.3% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +10.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +4.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.7 | -13.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | -2.4 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.3 | -3.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine ligand 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:77,511,753-77,611,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLC, BCA-1, BLR1L, ANGIE, ANGIE2; previously SCYB13 |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION |
| Reactome | 7 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [O43927](https://www.uniprot.org/uniprotkb/O43927) (C-X-C motif chemokine 13):

> Chemotactic for B-lymphocytes but not for T-lymphocytes, monocytes and neutrophils. Does not induce calcium release in B-lymphocytes. Binds to BLR1/CXCR5.

**Summary**, from NCBI Gene [10563](https://www.ncbi.nlm.nih.gov/gene/10563):

> B lymphocyte chemoattractant, independently cloned and named Angie, is an antimicrobial peptide and CXC chemokine strongly expressed in the follicles of the spleen, lymph nodes, and Peyer's patches. It preferentially promotes the migration of B lymphocytes (compared to T cells and macrophages), apparently by stimulating calcium influx into, and chemotaxis of, cells expressing Burkitt's lymphoma receptor 1 (BLR-1). It may therefore function in the homing of B lymphocytes to follicles. [provided …

**Accessions** — [HGNC:10639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10639) · Entrez [10563](https://www.ncbi.nlm.nih.gov/gene/10563) · UniProt [O43927](https://www.uniprot.org/uniprotkb/O43927) · Ensembl [ENSG00000156234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156234)

## Data

Gene col 7960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7960); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7960]; `tensor/DDL_lfc|DDL_z.npy` [7960]; `embed/gene_vectors.npy` [7960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7960 or target_col == 7960). Every well: [[CXCL13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCL13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
