---
symbol: "PIP4K2C"
type: "gene"
col: 9385
ensembl_id: "ENSG00000166908"
name: "phosphatidylinositol-5-phosphate 4-kinase type 2 gamma"
location: "12q13.3"
module: 2
arm: "+"
pooled_cpm: 20.72
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PIP4K2C

*phosphatidylinositol-5-phosphate 4-kinase type 2 gamma* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +15.8, q 0e+00, up in 39 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.226×, NCI-H23 0.285×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.189×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change); [[TAK-901 (drug)]] 0.5 µM in 1 line (Hs 766T 0.0605×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHRS1]] (+0.65, fdr 1e-05), [[HECTD3]] (+0.63, fdr 2e-05), [[PCBP4]] (+0.58, fdr 1e-05); moves opposite to [[HNRNPC]] (-0.49, fdr 3e-05), [[SMC4]] (-0.46, fdr 3e-05), [[SRSF10]] (-0.45, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +15.8 | 0e+00 | 39/45 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +13.7 | 4e-40 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +11.9 | 3e-30 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +10.7 | 9e-25 | 41/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +8.4 | 4e-15 | 30/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +8.3 | 1e-14 | 35/42 (NCI-H2030, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +7.9 | 3e-13 | 26/44 (COLO 205, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +7.9 | 3e-13 | 33/47 (LoVo, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +7.7 | 8e-13 | 33/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +6.9 | 3e-10 | 26/48 (SW480, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.48×** | +6.8 | 5e-10 | 20/38 (PANC-1, HEC-1-A, …) | two highest doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.2 | 2e-08 | 24/45 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.7 | 5e-07 | 2/48 (MIA PaCa-2, HepG2/C3A) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.6 | 1e-06 | 26/48 (KATO III, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.4 | 2e-06 | 22/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.2 | 7e-06 | 24/48 (HEC-1-A, RKO, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.8 | 5e-05 | 16/44 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +4.7 | 8e-05 | 17/44 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 2e-04 | 16/43 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +4.4 | 3e-04 | 20/48 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9385.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.226×, NCI-H23 0.285×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.189×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change); [[TAK-901 (drug)]] 0.5 µM in 1 line (Hs 766T 0.0605×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.7 | 0.15 | 12/48 (RKO, LoVo, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.770× | -3.3 | 0.32 | 12/47 (C32, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.1 | 5 | 0 | [[Belinostat (drug)]] 5 µM 3.15× (z +11.2) | — |
| [[LoVo (line)]] | wt | 23.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 30.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[NCI-H460 (line)]] | wt | 15.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[A-427 (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Hs 766T (line)]] | wt | 9.49 | 0 | 1 | — | [[TAK-901 (drug)]] 0.5 µM 0.0605× (z -9.2) |
| [[HT-29 (line)]] | alt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 21.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 37.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.8) | — |
| [[A-172 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[PCBP4]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ZBTB34]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SHARPIN]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CDS2]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 | pathway: Phospholipid metabolism |
| [[ESYT1]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CAPN10]] | +0.54 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[FAM219B]] | +0.54 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[TESK1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[TMEM183A]] | +0.52 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CACNB3]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPC]] | -0.49 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SMC4]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SRSF10]] | -0.45 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SERBP1]] | -0.45 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZNF644]] | -0.44 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[PMFBP1]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[KIAA0586]] | -0.44 | -0.49 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIP4K2C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.3, -21.2); signed map (-47.8, -10.7). **Vector** length 78.6, 15.9% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.3 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +15.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.5 | +4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | +0.9 |
|  | [[Darinaparsin (drug)]] 0.5 µM |  | -1.3 | -1.1 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-5-phosphate 4-kinase type 2 gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,591,174-57,603,418 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22055; previously PIP5K2C |
| Gene groups (HGNC) | Phosphatidylinositol-5-phosphate 4-kinase type 2 family |
| Reactome | 13 pathways, smallest: Synthesis of PIPs in the nucleus; PI5P Regulates TP53 Acetylation; Regulation of TP53 Activity through Acetylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBX8](https://www.uniprot.org/uniprotkb/Q8TBX8) (Phosphatidylinositol 5-phosphate 4-kinase type-2 gamma):

> Phosphatidylinositol 5-phosphate 4-kinase with low enzymatic activity. May be a GTP sensor, has higher GTP-dependent kinase activity than ATP-dependent kinase activity. PIP4Ks negatively regulate insulin signaling through a catalytic-independent mechanism. They interact with PIP5Ks and suppress PIP5K-mediated PtdIns(4,5)P2 synthesis and insulin-dependent conversion to PtdIns(3,4,5)P3.

**Summary**, from NCBI Gene [79837](https://www.ncbi.nlm.nih.gov/gene/79837):

> Enables 1-phosphatidylinositol-4-phosphate 5-kinase activity and identical protein binding activity. Involved in 1-phosphatidyl-1D-myo-inositol 4,5-bisphosphate biosynthetic process; negative regulation of insulin receptor signaling pathway; and positive regulation of autophagosome assembly. Located in autophagosome and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23786) · Entrez [79837](https://www.ncbi.nlm.nih.gov/gene/79837) · UniProt [Q8TBX8](https://www.uniprot.org/uniprotkb/Q8TBX8) · Ensembl [ENSG00000166908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166908)

## Data

Gene col 9385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9385); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9385]; `tensor/DDL_lfc|DDL_z.npy` [9385]; `embed/gene_vectors.npy` [9385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9385 or target_col == 9385). Every well: [[PIP4K2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP4K2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
