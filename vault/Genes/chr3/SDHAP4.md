---
symbol: "SDHAP4"
type: "gene"
col: 13175
ensembl_id: "ENSG00000214135"
name: "SDHA pseudogene 4"
location: "3q29"
module: 168
arm: "+"
pooled_cpm: 6.89
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# SDHAP4

*SDHA pseudogene 4* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.45× (z +3.8, q 0.078, up in 14 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.374× (z -14.2, q 5e-43, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP1]] (+0.83, fdr 7e-06), [[PMS2P3-1]] (+0.78, fdr 7e-06), [[SDHAP4-1]] (+0.77, fdr 7e-06, ⚠ same locus), [[RNF4]] (+0.75, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.75, fdr 7e-06), [[BPTF]] (-0.72, fdr 7e-06), [[LZIC]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CLCN4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SDHAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.078 | 14/46 (RKO, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 1.26× | +3.3 | 0.16 | 8/47 (LS 180, CFPAC-1, …) | top dose only | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.3 | 0.16 | 6/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.41× | +3.2 | 0.18 | 2/18 (HEC-1-A, HT-29) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 1.36× | +3.1 | 0.19 | 11/47 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 1.35× | +3.0 | 0.20 | 8/47 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.374×** | -14.2 | 5e-43 | 34/40 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.372×** | -10.1 | 2e-21 | 35/39 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.363×** | -10.0 | 5e-21 | 36/44 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.432×** | -8.6 | 2e-15 | 33/46 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.615×** | -5.0 | 8e-05 | 23/43 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.676×** | -4.0 | 0.006 | 15/47 (HOP62, A-172, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.698×** | -3.7 | 0.019 | 15/40 (HS-578T, BT-474, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.728× | -3.0 | 0.18 | 9/39 (BT-474, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0547× (z -22.8) |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0612× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 7.21 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.8) |
| [[HOP62 (line)]] | alt | 9.02 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -11.5) |
| [[J82 (line)]] | alt | 7.91 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -13.1) |
| [[A498 (line)]] | wt | 5.32 | 0 | 1 | — | [[Ralimetinib dimesylate (drug)]] 0.5 µM 0.0495× (z -10.0) |
| [[A549 (line)]] | wt | 4.90 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0727× (z -8.8) |
| [[COLO 205 (line)]] | alt | 9.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -10.2) |
| [[Hs 766T (line)]] | wt | 7.26 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0926× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 6.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0769× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 9.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.6) |
| [[PANC-1 (line)]] | alt | 5.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -8.8) |
| [[SNU-423 (line)]] | alt | 7.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -11.3) |
| [[SW 900 (line)]] | alt | 6.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0913× (z -8.9) |
| [[SW480 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | +0.83 | +0.88 / +0.75 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.77 | +0.80 / +0.72 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RNF4]] | +0.75 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[CDS2]] | +0.75 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.75 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[RPA1]] | +0.75 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.74 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[ABHD17A]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.72 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[PIK3R2]] | +0.71 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[NUDT21]] | +0.71 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.75 | -0.79 / -0.59 | both halves | 7e-06 |  |
| [[BPTF]] | -0.72 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[LZIC]] | -0.70 | -0.79 / -0.51 | both halves | 1e-05 |  |
| [[CUX1]] | -0.67 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.66 | -0.73 / -0.48 | both halves | 2e-05 |  |
| [[ATXN7L1]] | -0.66 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[ST7L]] | -0.66 | -0.78 / -0.43 | both halves | 3e-05 |  |
| [[CFLAR-AS1]] | -0.65 | -0.72 / -0.52 | both halves | 1e-05 |  |
| [[ZNF518A]] | -0.65 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[DARS1]] | -0.65 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.65 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[ZNF638]] | -0.65 | -0.52 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCN4]] | B | CLCN4 activity raises SDHAP4's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without CLCN4 | 0.010 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RASGRF1]] | B | RASGRF1 activity raises SDHAP4's level | lines that do not express RASGRF1 (18) vs lines expressing it (32) | 1.34× lower at baseline in the lines without RASGRF1 | 0.014 | ⚠ within organs, on part of the lines; also absent: RORC, MIR4280HG, TMEM40; maybe low, not absent |
| [[ZNF667-AS1]] | B | ZNF667-AS1 activity raises SDHAP4's level | lines that do not express ZNF667-AS1 (34) vs lines expressing it (16) | 1.09× lower at baseline in the lines without ZNF667-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF667, ADAMTS2, LINC02566 |
| [[SFTPA2]] | C | SFTPA2 activity raises SDHAP4's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 1.33× lower at baseline in the lines without SFTPA2 | 0.088 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP1]] | C | SDHAP4's natural level strengthens SDHAP1's drug response | SDHAP4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.35; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.902). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.4, -15.2); signed map (-39.3, -11.1). **Vector** length 71.1, 11.5% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | -0.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.9 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -14.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.4 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SDHA pseudogene 4 |
| Locus type | pseudogene |
| Location | 3q29 — chr3:197,619,740-197,627,848 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55782) · Entrez [220729](https://www.ncbi.nlm.nih.gov/gene/220729) · Ensembl [ENSG00000214135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214135)

## Data

Gene col 13175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13175); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13175]; `tensor/DDL_lfc|DDL_z.npy` [13175]; `embed/gene_vectors.npy` [13175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13175 or target_col == 13175). Every well: [[SDHAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
