---
symbol: "STK31"
type: "gene"
col: 12179
ensembl_id: "ENSG00000196335"
name: "serine/threonine kinase 31"
location: "7p15.3"
module: 27
arm: "+"
pooled_cpm: 2.51
n_lines_expressing: 44
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# STK31

*serine/threonine kinase 31* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +14.8, q 0e+00, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.552× (z -5.5, q 2e-05, down in 17 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (KATO III 0.0524×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0694×; ⚠ cell-cycle shift, explains ~45% of this change); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (HT-29 0.0693×); [[Pemetrexed (drug)]] 5 µM in 1 line (LS 180 0.0864×); [[Verteporfin (drug)]] 5 µM in 1 line (KATO III 0.108×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAR3-AS1]] (+0.65, fdr 1e-05), [[GNA14]] (+0.64, fdr 1e-05), [[LINC02580]] (+0.63, fdr 7e-06); moves opposite to [[TOP3A]] (-0.47, fdr 4e-05), [[TUBGCP5]] (-0.47, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RNF144A]] → it (grade B ⚠); 3 go from it, the strongest it → [[GNB4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +14.8 | 0e+00 | 15/23 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +11.8 | 1e-29 | 3/3 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.72×** | +11.3 | 4e-27 | 3/4 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +11.1 | 1e-26 | 4/10 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +10.3 | 1e-22 | 25/39 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.93×** | +8.6 | 6e-16 | 15/38 (LS 180, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +8.6 | 7e-16 | 20/37 (PANC-1, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.88×** | +8.2 | 1e-14 | 14/39 (LS 180, SW 900, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +6.3 | 2e-08 | 10/38 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.4 | 5e-06 | 1/19 (SW480) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +5.2 | 8e-06 | 11/37 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.2 | 8e-06 | 10/28 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +4.9 | 4e-05 | 10/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.67×** | +4.7 | 8e-05 | 9/41 (HT-29, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.69×** | +4.6 | 2e-04 | 4/29 (A-427, A549, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +4.5 | 2e-04 | 9/26 (NCI-H661, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.011 | 5/31 (Hs 766T, SW480, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.012 | 3/29 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.025 | 1/35 (NCI-H2347) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12179.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (KATO III 0.0524×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0694×; ⚠ cell-cycle shift, explains ~45% of this change); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (HT-29 0.0693×); [[Pemetrexed (drug)]] 5 µM in 1 line (LS 180 0.0864×); [[Verteporfin (drug)]] 5 µM in 1 line (KATO III 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -5.5 | 2e-05 | 17/34 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.584×** | -5.0 | 2e-04 | 18/40 (KATO III, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 0.707× | -3.2 | 0.24 | 5/36 (A498, C32, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.723× | -3.0 | 0.36 | 4/39 (H4, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 9.40 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0524× (z -12.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.108× (z -8.7) |
| [[LS 180 (line)]] | wt | 5.43 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0694× (z -10.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Pemetrexed (drug)]] 5 µM 0.0864× (z -8.8) |
| [[HT-29 (line)]] | alt | 4.80 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0693× (z -9.0) |
| [[A-172 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.736 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.666 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.822 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.754 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.845 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAR3-AS1]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GNA14]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[LINC02580]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[GLDN]] | +0.59 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[MUC20]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[AXDND1]] | +0.57 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[LNCRNA-IUR]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ITGB2]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[SLC40A1]] | +0.57 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MIR4713HG]] | +0.56 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[FCGRT]] | +0.56 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[MGAM2]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP3A]] | -0.47 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TUBGCP5]] | -0.47 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF144A]] | B | RNF144A activity lowers STK31's level | lines that do not express RNF144A (7) vs lines expressing it (43) | 2.09× higher at baseline in the lines without RNF144A | 0.062 | ⚠ within organs, on part of the lines; also absent: PTPRU |
| [[RBM47]] | B | RBM47 activity weakens STK31's drug response | lines that do not express RBM47 (17) vs lines expressing it (23) | the lines without RBM47 respond 0.99× as strongly (z diff +0.05); strongest at Panobinostat 0.5 µM: 2.64x vs 1.23x (z diff -1.7) | 0.068 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNB4]] | B | STK31 activity raises GNB4's level | lines that do not express STK31 (6) vs lines expressing it (44) | 2.89× lower at baseline in the lines without STK31 | 0.026 | ⚠ within organs, on part of the lines; also absent: HPSE, LTBP4, STRIP2; maybe low, not absent |
| [[CYP4F3]] | B | STK31 activity lowers CYP4F3's level | lines that do not express STK31 (6) vs lines expressing it (44) | 3.13× higher at baseline in the lines without STK31 | 0.032 | ⚠ within organs, on part of the lines; also absent: HPSE, LTBP4, STRIP2; maybe low, not absent |
| [[GAL3ST2]] | B | STK31 activity lowers GAL3ST2's level | lines that do not express STK31 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without STK31 | 0.073 | ⚠ within organs, on part of the lines; also absent: HPSE, LTBP4, STRIP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, 50.6); signed map (63.2, 2.1). **Vector** length 37.2, 4.11% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +8.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -5.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,710,203-23,832,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TDRD8, SgK396 |
| Gene groups (HGNC) | Tudor domain containing; STK31 kinase family |
| Matched by | ensembl_id |

UniProt [Q9BXU1](https://www.uniprot.org/uniprotkb/Q9BXU1) carries no function annotation.

**Summary**, from NCBI Gene [56164](https://www.ncbi.nlm.nih.gov/gene/56164):

> This gene is similar to a mouse gene that encodes a putative protein kinase with a tudor domain, and shows testis-specific expression. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11407) · Entrez [56164](https://www.ncbi.nlm.nih.gov/gene/56164) · UniProt [Q9BXU1](https://www.uniprot.org/uniprotkb/Q9BXU1) · Ensembl [ENSG00000196335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196335)

## Data

Gene col 12179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12179); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12179]; `tensor/DDL_lfc|DDL_z.npy` [12179]; `embed/gene_vectors.npy` [12179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12179 or target_col == 12179). Every well: [[STK31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
