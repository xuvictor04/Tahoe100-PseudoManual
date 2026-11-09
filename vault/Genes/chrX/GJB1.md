---
symbol: "GJB1"
type: "gene"
col: 9816
ensembl_id: "ENSG00000169562"
name: "gap junction protein beta 1"
location: "Xq13.1"
module: 27
arm: "+"
pooled_cpm: 3.71
n_lines_expressing: 12
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 60
direction_downstream: 74
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# GJB1

*gap junction protein beta 1* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.57× (z +11.5, q 8e-28, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.75× (z +4.4, q 0.001, up in 2 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Irinotecan (hydrochloride) (drug)]] 0.5 µM: 0.500× (z -3.9, q 0.066, down in 0 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (SW480 0.0290×, KATO III 0.0233×, LS 180 0.0377×, HT-29 0.0757×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW480 0.0344×, KATO III 0.0366×, HT-29 0.0540×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.0777×, KATO III 0.0746×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 0.0523×, KATO III 0.0917×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLRN3]] (+0.84, fdr 7e-06), [[VWA2]] (+0.81, fdr 7e-06), [[VSNL1]] (+0.80, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[LINC01091]] → it (grade B ⚠); 74 go from it, the strongest it → [[LINC00511]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.57×** | +11.5 | 8e-28 | 3/4 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.85×** | +7.5 | 2e-11 | 4/7 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.64×** | +6.7 | 5e-09 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.53×** | +5.2 | 3e-05 | 2/7 (SW480, C32) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +4.4 | 0.001 | 2/10 (SW480, HT-29) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.96×** | +4.0 | 0.005 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.7 | 0.016 | 2/8 (C32, HepG2/C3A) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.92×** | +3.6 | 0.019 | 3/8 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 5 µM |  | **1.58×** | +3.6 | 0.019 | 1/10 (KATO III) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.020 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.4 | 0.033 | 1/6 (HT-29) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +3.2 | 0.060 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.2 | 0.060 | 1/10 (C32) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.34×** | +3.2 | 0.063 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.1 | 0.067 | 2/9 (LS 180, C32) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.71×** | +3.0 | 0.098 | 3/10 (SK-MEL-2, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9816.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (SW480 0.0290×, KATO III 0.0233×, LS 180 0.0377×, HT-29 0.0757×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW480 0.0344×, KATO III 0.0366×, HT-29 0.0540×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.0777×, KATO III 0.0746×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 0.0523×, KATO III 0.0917×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.500×** | -3.9 | 0.066 | 0/10 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.516× | -3.4 | 0.19 | 4/10 (SW480, C32, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.558× | -3.2 | 0.21 | 9/10 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.563× | -3.2 | 0.21 | 8/10 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.9 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0344× (z -28.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0777× (z -21.3) |
| [[KATO III (line)]] | alt | 35.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0366× (z -21.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0233× (z -17.5) |
| [[HT-29 (line)]] | alt | 6.77 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0540× (z -15.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0757× (z -9.6) |
| [[LS 180 (line)]] | wt | 4.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0377× (z -10.1) |
| [[A-172 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.468 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLRN3]] | +0.84 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[VWA2]] | +0.81 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[VSNL1]] | +0.80 | +0.74 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.78 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[EDAR]] | +0.77 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[KCNE3]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TFF3]] | +0.77 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.77 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[NKD1]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[FGD5]] | +0.74 | +0.64 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 2, C 58. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | LINC01091 activity raises GJB1's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without LINC01091 | 0.076 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity raises GJB1's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without MCF2L | 0.089 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[AZGP1]] | C | AZGP1 activity raises GJB1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.95× lower at baseline in the lines without AZGP1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises GJB1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.16× lower at baseline in the lines without TFF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[F5]] | C | F5 activity raises GJB1's level | lines that do not express F5 (39) vs lines expressing it (11) | 2.20× lower at baseline in the lines without F5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises GJB1's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.91× lower at baseline in the lines without TMEM139 | 0.007 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |
| [[LINC01622]] | C | LINC01622 activity raises GJB1's level | lines that do not express LINC01622 (27) vs lines expressing it (23) | 2.56× lower at baseline in the lines without LINC01622 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GJB1, LINC02008, PROX1-AS1; maybe low, not absent; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises GJB1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.90× lower at baseline in the lines without GPX2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[PROM1]] | C | PROM1 activity raises GJB1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.54× lower at baseline in the lines without PROM1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises GJB1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.24× lower at baseline in the lines without KRT23 | 0.010 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises GJB1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.00× lower at baseline in the lines without KRT5 | 0.011 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises GJB1's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 2.57× lower at baseline in the lines without LINC01819 | 0.013 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 11, C 63. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00511]] | B | GJB1 activity raises LINC00511's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 4.89× lower at baseline in the lines without GJB1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[SLC12A2]] | B | GJB1 activity raises SLC12A2's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.62× lower at baseline in the lines without GJB1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[PLEKHS1]] | B | GJB1 activity raises PLEKHS1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.83× lower at baseline in the lines without GJB1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[FGD3]] | B | GJB1 activity raises FGD3's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.35× lower at baseline in the lines without GJB1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[MANSC1]] | B | GJB1 activity raises MANSC1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.65× lower at baseline in the lines without GJB1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[MAML2]] | B | GJB1 activity raises MAML2's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.53× lower at baseline in the lines without GJB1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[BCAR3-AS1]] | B | GJB1 activity raises BCAR3-AS1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 1.81× lower at baseline in the lines without GJB1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[MCF2L]] | B | GJB1 activity raises MCF2L's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.54× lower at baseline in the lines without GJB1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[FGFR4]] | B | GJB1 activity raises FGFR4's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.22× lower at baseline in the lines without GJB1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[LINC01091]] | B | GJB1 activity raises LINC01091's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.40× lower at baseline in the lines without GJB1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[PHACTR3]] | B | GJB1 activity raises PHACTR3's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 1.78× lower at baseline in the lines without GJB1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[AZGP1]] | C | GJB1 activity raises AZGP1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 10.88× lower at baseline in the lines without GJB1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, 46.2); signed map (63.2, 13.2). **Vector** length 48.7, 20.7% of its response variance represented; |z| ≥ 3 in 294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.2 |
| fall | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.4 | -2.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.4 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | gap junction protein beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,212,811-71,225,516 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CX32; previously CMTX1, CMTX |
| Gene groups (HGNC) | Gap junction proteins |
| Reactome | 9 pathways, smallest: Oligomerization of connexins into connexons; Transport of connexins along the secretory pathway; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P08034](https://www.uniprot.org/uniprotkb/P08034) (Gap junction beta-1 protein):

> One gap junction consists of a cluster of closely packed pairs of transmembrane channels, the connexons, through which materials of low MW diffuse from one cell to a neighboring cell.

**Summary**, from NCBI Gene [2705](https://www.ncbi.nlm.nih.gov/gene/2705):

> This gene encodes a member of the gap junction protein family. The gap junction proteins are membrane-spanning proteins that assemble to form gap junction channels that facilitate the transfer of ions and small molecules between cells. According to sequence similarities at the nucleotide and amino acid levels, the gap junction proteins are divided into two categories, alpha and beta. Mutations in this gene cause X-linked Charcot-Marie-Tooth disease, an inherited peripheral neuropathy. …

**Accessions** — [HGNC:4283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4283) · Entrez [2705](https://www.ncbi.nlm.nih.gov/gene/2705) · UniProt [P08034](https://www.uniprot.org/uniprotkb/P08034) · Ensembl [ENSG00000169562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169562)

## Data

Gene col 9816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9816); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9816]; `tensor/DDL_lfc|DDL_z.npy` [9816]; `embed/gene_vectors.npy` [9816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9816 or target_col == 9816). Every well: [[GJB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GJB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
