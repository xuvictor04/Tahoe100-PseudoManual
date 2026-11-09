---
symbol: "IL17RB"
type: "gene"
col: 640
ensembl_id: "ENSG00000056736"
name: "interleukin 17 receptor B"
location: "3p21.1"
module: 27
arm: "+"
pooled_cpm: 5.56
n_lines_expressing: 28
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# IL17RB

*interleukin 17 receptor B* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.50× (z +19.3, q 0e+00, up in 17 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.764× (z -4.1, q 0.021, down in 6 of 24 measured lines) ⚠ cell-cycle shift, explains ~25% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.0324×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0547×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (COLO 205 0.168×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHDH]] (+0.70, fdr 7e-06, ⚠ same locus), [[MYB]] (+0.66, fdr 8e-06), [[HUNK]] (+0.60, fdr 3e-05), [[MBNL3]] (+0.56, fdr 1e-05); moves opposite to [[SELENOS]] (-0.43, fdr 2e-04), [[C18orf32]] (-0.43, fdr 2e-04), [[EDF1]] (-0.43, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CHDH]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.50×** | +19.3 | 0e+00 | 17/20 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.62×** | +12.6 | 3e-34 | 5/9 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +10.5 | 3e-23 | 5/12 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +10.4 | 4e-23 | 9/19 (NCI-H2347, BT-474, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.41×** | +9.6 | 9e-20 | 7/13 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +6.9 | 4e-10 | 10/22 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +6.3 | 2e-08 | 8/17 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.90×** | +6.3 | 2e-08 | 11/21 (SW480, LS 180, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.30×** | +4.8 | 1e-04 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.7 | 1e-04 | 9/24 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.5 | 3e-04 | 5/21 (BT-474, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 7/24 (HEC-1-A, BT-474, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.011 | 1/18 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.018 | 5/21 (LoVo, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.023 | 3/20 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.031 | 8/22 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 640.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.0324×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0547×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (COLO 205 0.168×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.764×** | -4.1 | 0.021 | 6/24 (SW480, COLO 205, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.736× | -3.3 | 0.25 | 7/23 (SW480, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0324× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0547× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 3.12 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +12.9) | [[Sunitinib (drug)]] 5 µM 0.0952× (z -9.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 8.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +10.9) | — |
| [[SW480 (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.9) | — |
| [[A-172 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.886 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHDH]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 | STRING 853; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[MYB]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[HUNK]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[MBNL3]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[DNAJC22]] | +0.56 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[DHRS4L2]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TTPA]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[DMC1]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[CCDC170]] | +0.52 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[PASK]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ASB4]] | +0.51 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[TYMS]] | +0.51 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[ASRGL1]] | +0.50 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOS]] | -0.43 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[C18orf32]] | -0.43 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[EDF1]] | -0.43 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[DAD1]] | -0.43 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[BCLAF3]] | -0.43 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[HID1]] | -0.42 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ALG2]] | -0.41 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[NOL7]] ⚠ | -0.41 | -0.34 / -0.33 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[FAM50A]] | -0.41 | -0.30 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IL17RB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYB]] | B | MYB activity raises IL17RB's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.09× lower at baseline in the lines without MYB | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748 |
| [[CHDH]] | C | CHDH activity raises IL17RB's level | lines that do not express CHDH (22) vs lines expressing it (28) | 3.58× lower at baseline in the lines without CHDH | 0.004 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[YBX2]] | C | YBX2 activity raises IL17RB's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without YBX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises IL17RB's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.98× lower at baseline in the lines without TFF3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHDH]] | C | IL17RB activity raises CHDH's level | lines that do not express IL17RB (22) vs lines expressing it (28) | 3.42× lower at baseline in the lines without IL17RB | 0.002 | ⚠ within organs, on part of the lines; also absent: CHDH, ESRP2, PRSS22; maybe low, not absent; co-absent with the target |
| [[WNK2]] | C | IL17RB activity raises WNK2's level | lines that do not express IL17RB (22) vs lines expressing it (28) | 3.08× lower at baseline in the lines without IL17RB | 0.062 | ⚠ within organs, on part of the lines; also absent: CHDH, ESRP2, PRSS22; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.441). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.9, 44.4); signed map (66.1, 14.1). **Vector** length 52.5, 12.0% of its response variance represented; |z| ≥ 3 in 488 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.6 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +0.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.0 | -4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | +1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 17 receptor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,846,568-53,865,794 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL17RH1, EVI27, CRL4; previously IL17BR |
| Gene groups (HGNC) | Interleukin receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Interleukin-17 signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRM6](https://www.uniprot.org/uniprotkb/Q9NRM6) (Interleukin-17 receptor B):

> Receptor for the pro-inflammatory cytokines IL17B and IL17E. May play a role in controlling the growth and/or differentiation of hematopoietic cells.

**Summary**, from NCBI Gene [55540](https://www.ncbi.nlm.nih.gov/gene/55540):

> The protein encoded by this gene is a cytokine receptor. This receptor specifically binds to IL17B and IL17E, but does not bind to IL17 and IL17C. This receptor has been shown to mediate the activation of NF-kappaB and the production of IL8 induced by IL17E. The expression of the rat counterpart of this gene was found to be significantly up-regulated during intestinal inflammation, which suggested the immunoregulatory activity of this receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18015) · Entrez [55540](https://www.ncbi.nlm.nih.gov/gene/55540) · UniProt [Q9NRM6](https://www.uniprot.org/uniprotkb/Q9NRM6) · Ensembl [ENSG00000056736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056736)

## Data

Gene col 640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 640); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 640]; `tensor/DDL_lfc|DDL_z.npy` [640]; `embed/gene_vectors.npy` [640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 640 or target_col == 640). Every well: [[IL17RB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL17RB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
