---
symbol: "BCAR3-AS1"
type: "gene"
col: 13380
ensembl_id: "ENSG00000224093"
name: "BCAR3 antisense RNA 1"
location: "1p22.1"
module: 55
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 32
direction_downstream: 0
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# BCAR3-AS1

*BCAR3 antisense RNA 1* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +10.6, q 1e-23, up in 24 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.614× (z -5.3, q 6e-05, down in 17 of 42 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.652× (z -4.6, q 8e-04, down in 13 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPOAP1]] (+0.74, fdr 7e-06), [[C9orf152]] (+0.70, fdr 7e-06), [[ZNF503-AS1]] (+0.69, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[TFF3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +10.6 | 1e-23 | 24/33 (HS-578T, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +10.3 | 2e-22 | 8/17 (SHP-77, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +9.4 | 2e-18 | 1/3 (SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +9.1 | 1e-17 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.5 | 5e-06 | 5/17 (LOX-IMVI, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.4 | 0.001 | 8/42 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.002 | 2/45 (LoVo, KATO III) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.004 | 9/33 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.009 | 14/39 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.26×** | +3.6 | 0.017 | 4/43 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.062 | 4/42 (LS 180, LoVo, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.1 | 0.099 | 1/7 (SW480) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.614×** | -5.3 | 6e-05 | 17/42 (KATO III, HT-29, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -4.6 | 8e-04 | 13/43 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.644×** | -4.6 | 8e-04 | 14/38 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -4.0 | 0.008 | 12/41 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.695×** | -4.0 | 0.009 | 13/45 (SW480, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.709×** | -3.7 | 0.017 | 12/39 (SW480, BT-474, …) | all doses, flat |  |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.717×** | -3.6 | 0.023 | 10/42 (A549, SW 900, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.718×** | -3.6 | 0.023 | 9/42 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -3.2 | 0.073 | 12/42 (A-427, RPMI-7951, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.747× | -3.0 | 0.13 | 7/42 (COLO 205, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -11.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.355× (z -8.9) |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0947× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 5.58 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0495× (z -11.4) |
| [[HT-29 (line)]] | alt | 9.27 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0997× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~4% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.218× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 4.41 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0737× (z -9.8) |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -9.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H1573 (line)]] | alt | 4.40 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0849× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 1.95 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0799× (z -8.8) |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Artesunate (drug)]] 5 µM 0.223× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPOAP1]] | +0.74 | +0.66 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.70 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ZNF503-AS1]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 | same gene group |
| [[BTBD16]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.66 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[THBS4-AS1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 | same gene group |
| [[STK31]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CCDC162P]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[KCNE3]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[B3GAT1-DT]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[STPG4]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 31, C 1. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFF3]] | B | TFF3 activity raises BCAR3-AS1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.20× lower at baseline in the lines without TFF3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[GPX2]] | B | GPX2 activity raises BCAR3-AS1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without GPX2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[TOX3]] | B | TOX3 activity raises BCAR3-AS1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.76× lower at baseline in the lines without TOX3 | 0.006 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises BCAR3-AS1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without SPINT1-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[C9orf152]] | B | C9orf152 activity raises BCAR3-AS1's level | lines that do not express C9orf152 (32) vs lines expressing it (18) | 1.49× lower at baseline in the lines without C9orf152 | 0.008 | ⚠ within organs, on part of the lines; also absent: AGR3, MYO7B, KRT17; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity raises BCAR3-AS1's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without LINC01876 | 0.008 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[LINC01814]] | B | LINC01814 activity raises BCAR3-AS1's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 1.91× lower at baseline in the lines without LINC01814 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises BCAR3-AS1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without HNF1A-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[MUC6]] | B | MUC6 activity raises BCAR3-AS1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.95× lower at baseline in the lines without MUC6 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB |
| [[LINC00299]] | B | LINC00299 activity raises BCAR3-AS1's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without LINC00299 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2 |
| [[VIL1]] | B | VIL1 activity raises BCAR3-AS1's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 1.95× lower at baseline in the lines without VIL1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[LINC02253]] | B | LINC02253 activity raises BCAR3-AS1's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 1.92× lower at baseline in the lines without LINC02253 | 0.023 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 46.6); signed map (58.0, 13.4). **Vector** length 59.6, 7.88% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.1 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.6 | -5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.5 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | BCAR3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p22.1 — chr1:93,591,966-93,610,605 (+) |
| Ensembl biotype | lncRNA |
| Also known as | TP53LC19 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40093) · Entrez [100129046](https://www.ncbi.nlm.nih.gov/gene/100129046) · Ensembl [ENSG00000224093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224093)

## Data

Gene col 13380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13380); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13380]; `tensor/DDL_lfc|DDL_z.npy` [13380]; `embed/gene_vectors.npy` [13380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13380 or target_col == 13380). Every well: [[BCAR3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAR3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
