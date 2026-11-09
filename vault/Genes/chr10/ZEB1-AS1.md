---
symbol: "ZEB1-AS1"
type: "gene"
col: 14114
ensembl_id: "ENSG00000237036"
name: "ZEB1 antisense RNA 1"
location: "10p11.22"
module: 95
arm: "+"
pooled_cpm: 4.05
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# ZEB1-AS1

*ZEB1 antisense RNA 1* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.15× (z +35.2, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.545× (z -7.2, q 2e-10, down in 19 of 42 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF217-AS1]] (+0.67, fdr 4e-05), [[MAILR]] (+0.66, fdr 1e-04), [[PKN2-AS1]] (+0.66, fdr 1e-05); moves opposite to [[CAMK2G]] (-0.65, fdr 4e-05), [[CAPN7]] (-0.61, fdr 9e-05), [[WRAP73]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.15×** | +35.2 | 0e+00 | 38/38 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +13.4 | 2e-38 | 19/31 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +10.0 | 2e-21 | 25/40 (HOP62, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +9.3 | 2e-18 | 21/36 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +7.5 | 6e-12 | 10/21 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.8 | 9e-10 | 16/45 (HOP62, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.3 | 2e-08 | 16/43 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +6.1 | 7e-08 | 17/41 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.1 | 8e-08 | 4/7 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +6.0 | 1e-07 | 11/41 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +4.1 | 0.002 | 1/11 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 2/43 (HOP62, NCI-H2030) | top dose only | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.010 | 11/37 (CFPAC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **1.80×** | +3.6 | 0.011 | 2/25 (A498, A-172) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.011 | 7/40 (A-172, NCI-H2030, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.048 | 2/43 (SW 900, NCI-H23) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.545×** | -7.2 | 2e-10 | 19/42 (Panc 03.27, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -5.9 | 1e-06 | 17/44 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -5.4 | 1e-05 | 14/45 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.628×** | -5.2 | 2e-05 | 13/39 (MIA PaCa-2, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.683×** | -4.6 | 6e-04 | 13/42 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -4.4 | 1e-03 | 13/33 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -4.0 | 0.005 | 12/41 (SW480, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.19 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.199× (z -9.5) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -8.9) |
| [[A-172 (line)]] | wt | 7.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.40× (z +14.5) | — |
| [[J82 (line)]] | alt | 3.13 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +8.9) | [[Fenofibrate (drug)]] 5 µM 0.0686× (z -8.9) |
| [[SHP-77 (line)]] | alt | 4.95 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.94× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0817× (z -8.5) ⚠ toxic |
| [[A498 (line)]] | wt | 4.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +16.5) | — |
| [[A549 (line)]] | wt | 5.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 3.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 3.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 4.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +12.6) | — |
| [[Hs 766T (line)]] | wt | 6.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.82× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 5.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.93× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 3.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +13.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.90× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 6.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 4.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.21× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 5.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 3.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +14.0) | — |
| [[RKO (line)]] | wt | 7.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.42× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 3.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 3.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +10.6) | — |
| [[SW480 (line)]] | alt | 5.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.27× (z +16.2) | — |
| [[A-427 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF217-AS1]] | +0.67 | +0.41 / +0.47 | both halves | 4e-05 | same gene group |
| [[MAILR]] | +0.66 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | +0.66 | +0.55 / +0.49 | both halves | 1e-05 | same gene group |
| [[HAS2-AS1]] | +0.66 | +0.61 / +0.49 | both halves | 1e-05 | same gene group |
| [[ZBED5]] | +0.65 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.65 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[MAD2L1-DT]] | +0.64 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | +0.64 | +0.53 / +0.36 | both halves | 9e-05 | same gene group |
| [[UBE3B]] | +0.64 | +0.60 / +0.35 | both halves | 1e-04 |  |
| [[CDK6-AS1]] | +0.64 | +0.52 / +0.49 | both halves | 1e-05 | same gene group |
| [[WAKMAR2]] | +0.64 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[ERCC6L2-AS1]] | +0.64 | +0.58 / +0.28 | both halves | 3e-04 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK2G]] | -0.65 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CAPN7]] | -0.61 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[WRAP73]] | -0.58 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[DPY30]] | -0.57 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[MRPS34]] | -0.56 | -0.48 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZEB1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises ZEB1-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF407-AS1]] | C | ZNF407-AS1's natural level weakens ZEB1-AS1's drug response | ZNF407-AS1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.10; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[LINC01829]] | C | LINC01829 activity raises ZEB1-AS1's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without LINC01829 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |
| [[GNG12-AS1]] | C | GNG12-AS1 activity raises ZEB1-AS1's level | lines that do not express GNG12-AS1 (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without GNG12-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GALNT7, PARP11, DPP7; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (8.4, 14.2); signed map (24.2, -9.6). **Vector** length 63.1, 9.36% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +35.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +3.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.9 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ZEB1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p11.22 — chr10:31,206,278-31,320,447 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [220930](https://www.ncbi.nlm.nih.gov/gene/220930):

> This locus produces long non-coding RNA that is transcribed from a shared bi-directional promoter with zinc finger E-box binding homeobox 1 (ZEB1). This transcript binds lysine methyltransferase 2A and promotes histone modifications that are thought to promote expression of ZEB1. Expression of this gene is correlated with tumor progression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:42354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42354) · Entrez [220930](https://www.ncbi.nlm.nih.gov/gene/220930) · Ensembl [ENSG00000237036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237036)

## Data

Gene col 14114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14114); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14114]; `tensor/DDL_lfc|DDL_z.npy` [14114]; `embed/gene_vectors.npy` [14114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14114 or target_col == 14114). Every well: [[ZEB1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZEB1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
