---
symbol: "CABLES2"
type: "gene"
col: 7403
ensembl_id: "ENSG00000149679"
name: "Cdk5 and Abl enzyme substrate 2"
location: "20q13.33"
module: 85
arm: "+"
pooled_cpm: 8.78
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# CABLES2

*Cdk5 and Abl enzyme substrate 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.48× (z +19.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.503× (z -10.3, q 3e-22, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.71, fdr 1e-05), [[GNAI2]] (+0.68, fdr 9e-05), [[SNN]] (+0.68, fdr 1e-05); moves opposite to [[ANKRD18B]] (-0.68, fdr 1e-04), [[KICS2]] (-0.67, fdr 3e-05), [[RWDD2B]] (-0.67, fdr 6e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BMPR1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.48×** | +19.5 | 0e+00 | 47/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.26×** | +18.4 | 0e+00 | 44/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.79×** | +16.0 | 0e+00 | 44/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +9.1 | 8e-18 | 31/44 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +8.9 | 4e-17 | 29/47 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +5.2 | 1e-05 | 16/46 (Hs 766T, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.019 | 9/39 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.032 | 9/39 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.4 | 0.041 | 11/48 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.24×** | +3.3 | 0.058 | 8/36 (SW480, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.503×** | -10.3 | 3e-22 | 31/45 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.564×** | -9.0 | 9e-17 | 26/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -7.0 | 5e-10 | 21/38 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.766×** | -5.9 | 6e-07 | 20/44 (A-172, SW48, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.693×** | -5.7 | 1e-06 | 21/42 (A-172, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.533×** | -5.1 | 3e-05 | 13/45 (HOP62, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -5.1 | 3e-05 | 8/48 (HT-29, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.729×** | -4.9 | 6e-05 | 16/46 (A549, A-172, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -4.0 | 0.003 | 14/41 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.739×** | -3.6 | 0.016 | 13/43 (C32, A-427, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.3 | 0.045 | 18/43 (SW 900, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.061 | 11/47 (A-427, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.081 | 15/43 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.824×** | -3.0 | 0.096 | 8/46 (SW480, HepG2/C3A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.0 | 0.096 | 9/48 (A-172, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -13.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.133× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 6.94 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.49× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 22.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.30× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.193× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0959× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 4.01 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0694× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0946× (z -9.2) ⚠ toxic |
| [[SW 900 (line)]] | alt | 7.49 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 6.66 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0524× (z -8.5) |
| [[SW480 (line)]] | alt | 7.84 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +9.0) | — |
| [[A-427 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.71 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.68 | +0.50 / +0.37 | both halves | 9e-05 |  |
| [[SNN]] | +0.68 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[CEP131]] | +0.68 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[SLC27A1]] | +0.68 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[IGSF8]] | +0.67 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[CARHSP1]] | +0.66 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[STK32C]] | +0.66 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[RAB40B]] | +0.66 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[FBXL16]] | +0.65 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[HSDL1]] | +0.65 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[EFNA4]] | +0.65 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18B]] | -0.68 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[KICS2]] | -0.67 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[RWDD2B]] | -0.67 | -0.60 / -0.21 | both halves | 6e-04 |  |
| [[ARRDC3-AS1]] | -0.66 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[THOC7]] | -0.65 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.64 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[PKN2-AS1]] | -0.64 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[TIMMDC1]] | -0.64 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[MCTS1]] | -0.63 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TASOR]] | -0.63 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | -0.63 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[LINC01340]] | -0.62 | -0.53 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPR1B]] | B | BMPR1B activity lowers CABLES2's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.42× higher at baseline in the lines without BMPR1B | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[HDAC6]] | B | HDAC6 activity lowers CABLES2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PBX4]] | C | PBX4 activity raises CABLES2's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without PBX4 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (3.2, -1.3); signed map (-39.2, -3.1). **Vector** length 79.0, 14.0% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +18.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +19.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +16.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +8.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +5.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | Cdk5 and Abl enzyme substrate 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,388,634-62,407,285 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ908M14.2, ik3-2; previously C20orf150 |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTV7](https://www.uniprot.org/uniprotkb/Q9BTV7) (CDK5 and ABL1 enzyme substrate 2):

> Unknown. Probably involved in G1-S cell cycle transition.

**Summary**, from NCBI Gene [81928](https://www.ncbi.nlm.nih.gov/gene/81928):

> Predicted to be involved in cell division and regulation of cell cycle. Predicted to act upstream of or within several processes, including DNA damage response, signal transduction by p53 class mediator; gastrulation; and in utero embryonic development. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16143) · Entrez [81928](https://www.ncbi.nlm.nih.gov/gene/81928) · UniProt [Q9BTV7](https://www.uniprot.org/uniprotkb/Q9BTV7) · Ensembl [ENSG00000149679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149679)

## Data

Gene col 7403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7403); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7403]; `tensor/DDL_lfc|DDL_z.npy` [7403]; `embed/gene_vectors.npy` [7403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7403 or target_col == 7403). Every well: [[CABLES2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CABLES2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
