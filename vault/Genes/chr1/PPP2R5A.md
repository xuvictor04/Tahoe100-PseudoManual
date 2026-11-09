---
symbol: "PPP2R5A"
type: "gene"
col: 814
ensembl_id: "ENSG00000066027"
name: "protein phosphatase 2 regulatory subunit B'alpha"
location: "1q32.3"
module: 204
arm: "+"
pooled_cpm: 73.39
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# PPP2R5A

*protein phosphatase 2 regulatory subunit B'alpha* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +7.5, q 4e-11, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.744× (z -5.5, q 2e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNOT6L]] (+0.68, fdr 7e-06), [[ARL3]] (+0.65, fdr 7e-06), [[LNX2]] (+0.64, fdr 1e-05); moves opposite to [[EMG1]] (-0.62, fdr 9e-06), [[ZNF202]] (-0.61, fdr 1e-05), [[ZNF195]] (-0.60, fdr 1e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +7.5 | 4e-11 | 33/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.8 | 2e-06 | 31/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.1 | 5e-05 | 29/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.5 | 9e-04 | 23/47 (NCI-H23, LS 180, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +4.4 | 0.001 | 25/48 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.002 | 22/48 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.17× | +4.1 | 0.003 | 19/48 (A-427, RKO, …) | top dose only | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.7 | 0.018 | 14/48 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.021 | 20/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.033 | 16/49 (RKO, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 1.35× | +3.0 | 0.13 | 18/48 (A498, J82, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.744×** | -5.5 | 2e-05 | 29/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -5.4 | 2e-05 | 26/45 (SHP-77, A-172, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.763×** | -5.2 | 3e-05 | 25/49 (A-172, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -5.0 | 7e-05 | 29/48 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -4.2 | 0.003 | 20/43 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.817×** | -3.9 | 0.008 | 21/48 (A-172, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.770×** | -3.6 | 0.024 | 19/48 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.885× | -3.4 | 0.049 | 17/48 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -3.3 | 0.068 | 18/44 (SK-MEL-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.849× | -3.2 | 0.076 | 20/49 (SHP-77, SW 900, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | 0.844× | -3.2 | 0.076 | 17/47 (CFPAC-1, NCI-H2030, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.799×** | -3.1 | 0.087 | 17/47 (AN3 CA, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.854× | -3.1 | 0.092 | 19/48 (NCI-H2347, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 66.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.371× (z -9.6) |
| [[SW480 (line)]] | alt | 74.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 92.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +14.9) | — |
| [[PANC-1 (line)]] | alt | 82.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +12.3) | — |
| [[RKO (line)]] | wt | 49.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 71.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 66.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.354× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 66.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.02× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT6L]] | +0.68 | +0.71 / +0.67 | both halves | 7e-06 | pathway: Intracellular signaling by second messengers |
| [[ARL3]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[LNX2]] | +0.64 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PLAG1]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[FNBP1L]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[RCOR3]] | +0.62 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D12]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[CAT]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[USP33]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[GTF2IP4]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMG1]] | -0.62 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[ZNF202]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ZNF195]] | -0.60 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[METTL1]] | -0.59 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[GTPBP4]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[REXO1]] | -0.57 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[ZNF562]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PUS1]] | -0.56 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TAF2]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.56 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[SLC35C2]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[DHX37]] | -0.55 | -0.61 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDS1]] | B | CDS1 activity raises PPP2R5A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.24× lower at baseline in the lines without CDS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers PPP2R5A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.8, -12.2); signed map (-21.9, 16.3). **Vector** length 110, 29.4% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.6 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit B'alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,285,410-212,361,853 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PR61A, B56A, B56alpha |
| Gene groups (HGNC) | Protein phosphatase 2 regulatory subunits; Armadillo like helical domain containing; Small nucleolar RNA protein coding host genes |
| Reactome | 56 pathways, smallest: APC truncation mutants have impaired AXIN binding; AXIN missense mutants destabilize the destruction complex; Signaling by AMER1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15172](https://www.uniprot.org/uniprotkb/Q15172) (Serine/threonine-protein phosphatase 2A 56 kDa regulatory subunit alpha isoform):

> The B regulatory subunit might modulate substrate selectivity and catalytic activity, and might also direct the localization of the catalytic enzyme to a particular subcellular compartment.

**Summary**, from NCBI Gene [5525](https://www.ncbi.nlm.nih.gov/gene/5525):

> The product of this gene belongs to the phosphatase 2A regulatory subunit B family. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The B regulatory subunit might modulate substrate selectivity and catalytic activity. This …

**Accessions** — [HGNC:9309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9309) · Entrez [5525](https://www.ncbi.nlm.nih.gov/gene/5525) · UniProt [Q15172](https://www.uniprot.org/uniprotkb/Q15172) · Ensembl [ENSG00000066027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066027)

## Data

Gene col 814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 814); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 814]; `tensor/DDL_lfc|DDL_z.npy` [814]; `embed/gene_vectors.npy` [814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 814 or target_col == 814). Every well: [[PPP2R5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
