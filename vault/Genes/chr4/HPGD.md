---
symbol: "HPGD"
type: "gene"
col: 8876
ensembl_id: "ENSG00000164120"
name: "15-hydroxyprostaglandin dehydrogenase"
location: "4q34.1"
module: 55
arm: "+"
pooled_cpm: 14.64
n_lines_expressing: 20
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 46
direction_downstream: 70
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# HPGD

*15-hydroxyprostaglandin dehydrogenase* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.78× (z +15.1, q 0e+00, up in 7 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +4.9, q 1e-04, up in 7 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.508× (z -5.8, q 3e-06, down in 14 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD17B2]] (+0.66, fdr 3e-05), [[TSPAN1]] (+0.62, fdr 1e-05), [[CLIC5]] (+0.60, fdr 1e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[SPATA6L]] → it (grade B ⚠); 70 go from it, the strongest it → [[PELI1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.78×** | +15.1 | 0e+00 | 7/11 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.12×** | +14.6 | 1e-45 | 11/15 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.17×** | +11.8 | 8e-30 | 8/13 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.9 | 1e-04 | 7/18 (KATO III, SW1417, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.8 | 1e-04 | 2/16 (A549, SW1417) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.64×** | +4.5 | 8e-04 | 9/18 (SHP-77, SW 900, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.63×** | +4.4 | 1e-03 | 4/18 (SHP-77, AsPC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.004 | 10/18 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.067 | 1/18 (SW 900) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.089 | 8/18 (Hs 766T, A549, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -5.8 | 3e-06 | 14/18 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.579×** | -4.8 | 4e-04 | 14/17 (SW48, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.633×** | -4.1 | 0.009 | 15/18 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.642×** | -3.9 | 0.013 | 10/18 (LoVo, SW48, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.650×** | -3.8 | 0.016 | 14/18 (LoVo, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.646×** | -3.8 | 0.016 | 12/18 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.682×** | -3.4 | 0.057 | 7/18 (BT-474, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.782× | -3.1 | 0.16 | 5/18 (LoVo, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 397 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.122× (z -14.3) |
| [[LoVo (line)]] | wt | 89.0 | 2 (2 ⚠) | 10 (6 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +11.1) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.111× (z -14.4) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.217× (z -9.7) |
| [[SW480 (line)]] | alt | 12.7 | 1 (1 ⚠) | 9 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 69.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0759× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0841× (z -10.3) |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0223× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -9.7) |
| [[A549 (line)]] | wt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.7× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 29.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -9.2) |
| [[KATO III (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B2]] | +0.66 | +0.57 / +0.46 | both halves | 3e-05 | same gene group; STRING 690 |
| [[TSPAN1]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PROM1]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[KCNE3]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[FOXQ1]] | +0.59 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[FXYD3]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GPX2]] | +0.59 | +0.56 / +0.43 | both halves | 3e-05 | pathway: Arachidonate metabolism |
| [[SKAP1]] | +0.59 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[ST6GALNAC1]] | +0.58 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[KRT23]] | +0.58 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[TMEM45B]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 1, C 45. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATA6L]] | B | SPATA6L activity raises HPGD's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without SPATA6L | 0.022 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[C1orf116]] | C | C1orf116 activity raises HPGD's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.17× lower at baseline in the lines without C1orf116 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[FOXQ1]] | C | FOXQ1 activity raises HPGD's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 4.61× lower at baseline in the lines without FOXQ1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; co-absent with the target |
| [[TMC5]] | C | TMC5 activity raises HPGD's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 4.75× lower at baseline in the lines without TMC5 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4; co-absent with the target |
| [[CATSPERB]] | C | CATSPERB activity raises HPGD's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 4.90× lower at baseline in the lines without CATSPERB | 0.005 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14; co-absent with the target |
| [[SHROOM3]] | C | SHROOM3 activity raises HPGD's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 3.61× lower at baseline in the lines without SHROOM3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT; co-absent with the target |
| [[TSPAN1]] | C | TSPAN1 activity raises HPGD's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 4.17× lower at baseline in the lines without TSPAN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises HPGD's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.42× lower at baseline in the lines without ITGB6 | 0.008 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises HPGD's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 4.99× lower at baseline in the lines without TTC22 | 0.008 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises HPGD's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 6.23× lower at baseline in the lines without CLIC5 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises HPGD's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 4.58× lower at baseline in the lines without HNF4A | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises HPGD's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.64× lower at baseline in the lines without P2RY2 | 0.009 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |

### Downstream of this gene

*70 arrows, 70 of them with an alert ⚠; grade A 0, B 13, C 57. Shown: the 12 strongest; 58 more arrows (58 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PELI1]] | B | HPGD activity raises PELI1's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without HPGD | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[ZNF503-AS1]] | B | HPGD activity raises ZNF503-AS1's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without HPGD | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[GAREM1]] | B | HPGD activity raises GAREM1's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without HPGD | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[BAG1]] | B | HPGD activity raises BAG1's level | lines that do not express HPGD (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without HPGD | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[BCL2L15]] | B | HPGD activity raises BCL2L15's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.85× lower at baseline in the lines without HPGD | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[SLC44A5]] | B | HPGD activity raises SLC44A5's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without HPGD | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| cells under [[Pimozide (drug)]] 0.05 µM | B | HPGD activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express HPGD (30) vs lines expressing it (18) | the lines without HPGD: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| cells under [[Trifluridine (drug)]] 5 µM | B | HPGD activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express HPGD (30) vs lines expressing it (18) | the lines without HPGD: 0.91× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[LMO7]] | B | HPGD activity raises LMO7's level | lines that do not express HPGD (30) vs lines expressing it (20) | 3.69× lower at baseline in the lines without HPGD | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[SPATA6L]] | B | HPGD activity raises SPATA6L's level | lines that do not express HPGD (30) vs lines expressing it (20) | 3.04× lower at baseline in the lines without HPGD | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | HPGD activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express HPGD (30) vs lines expressing it (18) | the lines without HPGD: 1.16× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | HPGD activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express HPGD (30) vs lines expressing it (18) | the lines without HPGD: 0.90× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.8, 56.8); signed map (61.0, 7.8). **Vector** length 62.0, 17.9% of its response variance represented; |z| ≥ 3 in 591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | +0.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | 15-hydroxyprostaglandin dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.1 — chr4:174,490,175-174,523,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR36C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | ANDROGEN_RESPONSE, FATTY_ACID_METABOLISM |
| Reactome | 10 pathways, smallest: Biosynthesis of Lipoxins (LX); Biosynthesis of D-series resolvins; Biosynthesis of E-series 18(S)-resolvins |
| Matched by | ensembl_id |

**Function**, from UniProt [P15428](https://www.uniprot.org/uniprotkb/P15428) (15-hydroxyprostaglandin dehydrogenase):

> Catalyzes the NAD-dependent dehydrogenation (oxidation) of a broad array of hydroxylated polyunsaturated fatty acids (mainly eicosanoids and docosanoids, including prostaglandins, lipoxins and resolvins), yielding their corresponding keto (oxo) metabolites. Decreases the levels of the pro-proliferative prostaglandins such as prostaglandin E2 (whose activity is increased in cancer because of an increase in the expression of cyclooxygenase 2) and generates oxo-fatty acid products that can …

**Summary**, from NCBI Gene [3248](https://www.ncbi.nlm.nih.gov/gene/3248):

> This gene encodes a member of the short-chain nonmetalloenzyme alcohol dehydrogenase protein family. The encoded enzyme is responsible for the metabolism of prostaglandins, which function in a variety of physiologic and cellular processes such as inflammation. Mutations in this gene result in primary autosomal recessive hypertrophic osteoarthropathy and cranioosteoarthropathy. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:5154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5154) · Entrez [3248](https://www.ncbi.nlm.nih.gov/gene/3248) · UniProt [P15428](https://www.uniprot.org/uniprotkb/P15428) · Ensembl [ENSG00000164120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164120)

## Data

Gene col 8876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8876); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8876]; `tensor/DDL_lfc|DDL_z.npy` [8876]; `embed/gene_vectors.npy` [8876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8876 or target_col == 8876). Every well: [[HPGD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPGD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
