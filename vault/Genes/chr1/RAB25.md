---
symbol: "RAB25"
type: "gene"
col: 5362
ensembl_id: "ENSG00000132698"
name: "RAB25, member RAS oncogene family"
location: "1q22"
module: 44
arm: "+"
pooled_cpm: 5.77
n_lines_expressing: 17
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 84
direction_downstream: 110
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# RAB25

*RAB25, member RAS oncogene family* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.17× (z +13.8, q 1e-40, up in 5 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.40× (z +4.2, q 0.002, up in 3 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.605× (z -4.4, q 0.006, down in 12 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (LS 180 0.266×, LoVo 0.244×, KATO III 0.257×, HT-29 0.321×, …); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.301×, LoVo 0.261×, CFPAC-1 0.282×, COLO 205 0.290×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 0.157×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.280×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLDN3]] (+0.76, fdr 7e-06), [[ELMO3]] (+0.70, fdr 1e-05), [[CKMT1A]] (+0.70, fdr 1e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 84 arrows point to it, the strongest [[TMEM30B]] → it (grade C ⚠); 110 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.17×** | +13.8 | 1e-40 | 5/8 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.69×** | +11.4 | 1e-27 | 5/13 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +6.1 | 1e-07 | 7/15 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +6.1 | 1e-07 | 1/11 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.2 | 2e-05 | 1/14 (SW1417) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.3 | 0.002 | 1/15 (NCI-H1573) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.25×** | +4.2 | 0.002 | 2/14 (BT-474, Panc 03.27) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.2 | 0.002 | 1/14 (COLO 205) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 3/15 (HCT15, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.1 | 0.003 | 2/14 (KATO III, SW48) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.004 | 1/15 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +3.8 | 0.007 | 0/15 | top dose only | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.92×** | +3.4 | 0.033 | 2/14 (NCI-H1573, LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.88×** | +3.3 | 0.046 | 5/15 (LoVo, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.051 | 4/14 (LoVo, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5362.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (LS 180 0.266×, LoVo 0.244×, KATO III 0.257×, HT-29 0.321×, …); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.301×, LoVo 0.261×, CFPAC-1 0.282×, COLO 205 0.290×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 0.157×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.280×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.605×** | -4.4 | 0.006 | 12/15 (NCI-H2347, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ivermectin (drug)]] 5 µM |  | 0.684× | -3.3 | 0.23 | 0/15 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -13.1) |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -10.4) |
| [[KATO III (line)]] | alt | 18.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -11.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 22.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -9.1) |
| [[A-172 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.416 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLDN3]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 | STRING 452 |
| [[ELMO3]] | +0.70 | +0.74 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[CKMT1A]] | +0.70 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.70 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[SLC44A4]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[FXYD3]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 | STRING 405 |
| [[CLDN7]] | +0.67 | +0.66 / +0.57 | both halves | 8e-06 | STRING 679 |
| [[CKMT1B]] | +0.66 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[TSPAN1]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MPZL2]] | +0.65 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[LGALS4]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PROM2]] | +0.64 | +0.70 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 0, C 84. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM30B]] | C | TMEM30B activity raises RAB25's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 10.99× lower at baseline in the lines without TMEM30B | 6e-07 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises RAB25's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 9.15× lower at baseline in the lines without TMPRSS4 | 3e-06 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises RAB25's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 9.05× lower at baseline in the lines without TMEM125 | 7e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises RAB25's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 7.88× lower at baseline in the lines without MAL2 | 7e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[S100A14]] | C | S100A14 activity raises RAB25's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 8.01× lower at baseline in the lines without S100A14 | 1e-05 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[ST14]] | C | ST14 activity raises RAB25's level | lines that do not express ST14 (32) vs lines expressing it (18) | 8.03× lower at baseline in the lines without ST14 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises RAB25's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 6.54× lower at baseline in the lines without MPZL2 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises RAB25's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 6.50× lower at baseline in the lines without BSPRY | 4e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[PRSS8]] | C | PRSS8 activity raises RAB25's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 8.10× lower at baseline in the lines without PRSS8 | 6e-05 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; co-absent with the target |
| [[ESRP1]] | C | ESRP1 activity raises RAB25's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 7.15× lower at baseline in the lines without ESRP1 | 6e-05 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |
| [[GALNT3]] | C | GALNT3 activity raises RAB25's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 6.38× lower at baseline in the lines without GALNT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises RAB25's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 5.44× lower at baseline in the lines without P2RY2 | 1e-04 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |

### Downstream of this gene

*110 arrows, 110 of them with an alert ⚠; grade A 0, B 25, C 85. Shown: the 12 strongest; 98 more arrows (98 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | RAB25 activity raises FAM83E's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 5.16× lower at baseline in the lines without RAB25 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[KRTCAP3]] | B | RAB25 activity raises KRTCAP3's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 3.45× lower at baseline in the lines without RAB25 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[ARHGEF16]] | B | RAB25 activity raises ARHGEF16's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 3.96× lower at baseline in the lines without RAB25 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[ELMO3]] | B | RAB25 activity raises ELMO3's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without RAB25 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[FUT2]] | B | RAB25 activity raises FUT2's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.62× lower at baseline in the lines without RAB25 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[MANSC1]] | B | RAB25 activity raises MANSC1's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.85× lower at baseline in the lines without RAB25 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[AMN]] | B | RAB25 activity raises AMN's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.49× lower at baseline in the lines without RAB25 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[VILL]] | B | RAB25 activity raises VILL's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without RAB25 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | RAB25 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express RAB25 (33) vs lines expressing it (15) | the lines without RAB25: 1.18× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | RAB25 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express RAB25 (33) vs lines expressing it (15) | the lines without RAB25: 0.74× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[FAM83E]] | B | RAB25 activity weakens FAM83E's drug response | lines that do not express RAB25 (21) vs lines expressing it (15) | (z diff -2.10); strongest at Homoharringtonine 5 µM: 1.83x vs 0.43x (z diff -8.1) | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; target measured in part of the lines; artifact flags |
| cells under [[Afatinib (drug)]] 0.5 µM | B | RAB25 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express RAB25 (33) vs lines expressing it (15) | the lines without RAB25: 1.14× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.3, 53.2); signed map (62.6, 6.4). **Vector** length 36.4, 10.6% of its response variance represented; |z| ≥ 3 in 202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.8 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.8 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB25, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,061,160-156,070,504 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CATX-8 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P57735](https://www.uniprot.org/uniprotkb/P57735) (Ras-related protein Rab-25):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB25 regulates epithelial cell differentiation, proliferation and survival, thereby playing key roles …

**Summary**, from NCBI Gene [57111](https://www.ncbi.nlm.nih.gov/gene/57111):

> The protein encoded by this gene is a member of the RAS superfamily of small GTPases. The encoded protein is involved in membrane trafficking and cell survival. This gene has been found to be a tumor suppressor and an oncogene, depending on the context. Two variants, one protein-coding and the other not, have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:18238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18238) · Entrez [57111](https://www.ncbi.nlm.nih.gov/gene/57111) · UniProt [P57735](https://www.uniprot.org/uniprotkb/P57735) · Ensembl [ENSG00000132698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132698)

## Data

Gene col 5362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5362); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5362]; `tensor/DDL_lfc|DDL_z.npy` [5362]; `embed/gene_vectors.npy` [5362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5362 or target_col == 5362). Every well: [[RAB25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
