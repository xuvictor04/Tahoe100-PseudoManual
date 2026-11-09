---
symbol: "TRPV4"
type: "gene"
col: 3199
ensembl_id: "ENSG00000111199"
name: "transient receptor potential cation channel subfamily V member 4"
location: "12q24.11"
module: 27
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 24
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 12
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# TRPV4

*transient receptor potential cation channel subfamily V member 4* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.83× (z +11.7, q 8e-29, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +8.6, q 1e-15, up in 1 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.602× (z -4.7, q 0.002, down in 12 of 15 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LOXL4]] (+0.60, fdr 3e-05), [[SLC30A10]] (+0.58, fdr 4e-05), [[F10]] (+0.57, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MILR1]] → it (grade B ⚠); 12 go from it, the strongest it → [[RGCC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.83×** | +11.7 | 8e-29 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +9.3 | 6e-18 | 2/10 (HOP62, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +8.6 | 1e-15 | 1/17 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +5.9 | 6e-07 | 7/20 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +5.7 | 1e-06 | 1/10 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +5.5 | 4e-06 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.65×** | +4.6 | 3e-04 | 5/7 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +4.0 | 0.004 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.7 | 0.015 | 1/14 (HOP62) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.019 | 0/12 | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.019 | 1/12 (HepG2/C3A) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.73×** | +3.5 | 0.019 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.019 | 7/16 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.034 | 3/18 (HOP62, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +3.3 | 0.038 | 3/11 (SW 900, HepG2/C3A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.042 | 3/18 (HOP62, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Posaconazole (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.050 | 1/18 (HT-29) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.071 | 4/19 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.071 | 0/19 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.071 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.45×** | +2.9 | 0.078 | 0/14 | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.079 | 2/20 (Hs 766T, SK-MEL-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.602×** | -4.7 | 0.002 | 12/15 (Panc 03.27, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.616×** | -4.4 | 0.003 | 9/19 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.627×** | -4.1 | 0.006 | 14/19 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -4.1 | 0.006 | 13/19 (SW480, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -4.0 | 0.006 | 11/20 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.684×** | -3.5 | 0.046 | 11/19 (SW480, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.713× | -3.1 | 0.15 | 8/20 (SW480, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.8 | 0 | 14 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -17.2) |
| [[Hs 766T (line)]] | wt | 46.1 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0735× (z -23.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -20.3) |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0806× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0424× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0824× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0318× (z -17.4) |
| [[SW1417 (line)]] | alt | 8.74 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.226× (z -10.0) |
| [[A-172 (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.973 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.651 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOXL4]] | +0.60 | +0.61 / +0.44 | both halves | 3e-05 | **novel candidate** |
| [[SLC30A10]] | +0.58 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[F10]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[APCDD1]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[OPRD1]] | +0.56 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ANO4]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 | pathway: Ion channel transport |
| [[JAKMIP2-AS1]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SHROOM4]] | +0.55 | +0.56 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[FGD5]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[FGF19]] | +0.52 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[RHOXF1-AS1]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ST18]] | +0.51 | +0.49 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MILR1]] | B | MILR1 activity raises TRPV4's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without MILR1 | 0.051 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[B3GNT7]] | B | B3GNT7 activity raises TRPV4's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 2.12× lower at baseline in the lines without B3GNT7 | 0.074 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[GPR143]] | B | GPR143 activity raises TRPV4's level | lines that do not express GPR143 (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without GPR143 | 0.074 | ⚠ within organs, on part of the lines; also absent: SHROOM2, DCDC2, SCN5A; maybe low, not absent |
| [[LINC02981]] | B | LINC02981 activity raises TRPV4's level | lines that do not express LINC02981 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without LINC02981 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PTPRZ1]] | C | PTPRZ1 activity raises TRPV4's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.80× lower at baseline in the lines without PTPRZ1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029; co-absent with the target |
| [[APCDD1]] | C | APCDD1 activity raises TRPV4's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.47× lower at baseline in the lines without APCDD1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[SHROOM4]] | C | SHROOM4 activity raises TRPV4's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without SHROOM4 | 0.063 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGCC]] | B | TRPV4 activity raises RGCC's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without TRPV4 | 0.024 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[GPR143]] | B | TRPV4 activity raises GPR143's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without TRPV4 | 0.034 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[IL19]] | B | TRPV4 activity raises IL19's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.56× lower at baseline in the lines without TRPV4 | 0.039 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[LINC02964]] | B | TRPV4 activity raises LINC02964's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.50× lower at baseline in the lines without TRPV4 | 0.058 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[ITGA9-AS1]] | B | TRPV4 activity raises ITGA9-AS1's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.63× lower at baseline in the lines without TRPV4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[JAKMIP2-AS1]] | B | TRPV4 activity raises JAKMIP2-AS1's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without TRPV4 | 0.068 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[PROX1-AS1]] | B | TRPV4 activity raises PROX1-AS1's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without TRPV4 | 0.083 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[LINC03042]] | B | TRPV4 activity raises LINC03042's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without TRPV4 | 0.097 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[TMEM163]] | C | TRPV4 activity raises TMEM163's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without TRPV4 | 0.012 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent; co-absent with the target |
| [[SHROOM4]] | C | TRPV4 activity raises SHROOM4's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without TRPV4 | 0.016 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent; co-absent with the target |
| [[LINC01622]] | C | TRPV4 activity raises LINC01622's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without TRPV4 | 0.020 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent; co-absent with the target |
| [[APCDD1]] | C | TRPV4 activity raises APCDD1's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without TRPV4 | 0.072 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 42.7); signed map (64.0, 16.6). **Vector** length 47.7, 10.6% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | +0.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily V member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,783,087-109,833,406 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OTRPC4, TRP12, VROAC, VRL-2, VR-OAC, CMT2C |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Transient receptor potential cation channel subfamily V |
| Reactome | 8 pathways, smallest: TRP channels; High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; Stimuli-sensing channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBA0](https://www.uniprot.org/uniprotkb/Q9HBA0) (Transient receptor potential cation channel subfamily V member 4):

> Non-selective calcium permeant cation channel involved in osmotic sensitivity and mechanosensitivity. Activation by exposure to hypotonicity within the physiological range exhibits an outward rectification. Also activated by heat, low pH, citrate and phorbol esters. Increase of intracellular Ca(2+) potentiates currents. Channel activity seems to be regulated by a calmodulin-dependent mechanism with a negative feedback mechanism. Promotes cell-cell junction formation in skin keratinocytes and …

**Summary**, from NCBI Gene [59341](https://www.ncbi.nlm.nih.gov/gene/59341):

> This gene encodes a member of the OSM9-like transient receptor potential channel (OTRPC) subfamily in the transient receptor potential (TRP) superfamily of ion channels. The encoded protein is a Ca2+-permeable, nonselective cation channel that is thought to be involved in the regulation of systemic osmotic pressure. Mutations in this gene are the cause of spondylometaphyseal and metatropic dysplasia and hereditary motor and sensory neuropathy type IIC. Multiple transcript variants encoding …

**Accessions** — [HGNC:18083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18083) · Entrez [59341](https://www.ncbi.nlm.nih.gov/gene/59341) · UniProt [Q9HBA0](https://www.uniprot.org/uniprotkb/Q9HBA0) · Ensembl [ENSG00000111199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111199)

## Data

Gene col 3199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3199); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3199]; `tensor/DDL_lfc|DDL_z.npy` [3199]; `embed/gene_vectors.npy` [3199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3199 or target_col == 3199). Every well: [[TRPV4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPV4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
