---
symbol: "SPATA33"
type: "gene"
col: 9477
ensembl_id: "ENSG00000167523"
name: "spermatogenesis associated 33"
location: "16q24.3"
module: 51
arm: "-"
pooled_cpm: 11.5
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SPATA33

*spermatogenesis associated 33* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.15× (z +21.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.678× (z -6.9, q 3e-09, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMG1P5]] (+0.68, fdr 1e-05), [[OGG1]] (+0.67, fdr 7e-06), [[BCL7C]] (+0.61, fdr 1e-05); moves opposite to [[FUNDC1]] (-0.60, fdr 1e-05), [[ATRX]] (-0.60, fdr 3e-05), [[ZMYM4]] (-0.59, fdr 2e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.15×** | +21.2 | 0e+00 | 47/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.90×** | +19.6 | 0e+00 | 45/48 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.55×** | +17.3 | 0e+00 | 41/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +14.5 | 3e-45 | 35/39 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +12.9 | 9e-36 | 33/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +9.0 | 2e-17 | 31/43 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +8.3 | 6e-15 | 24/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.60×** | +8.3 | 7e-15 | 24/45 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.59×** | +7.9 | 2e-13 | 14/26 (PANC-1, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +6.6 | 2e-09 | 18/47 (SW480, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.41×** | +6.3 | 1e-08 | 16/47 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +4.8 | 7e-05 | 9/47 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.6 | 2e-04 | 15/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 3e-04 | 14/46 (SW480, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.26×** | +4.2 | 0.001 | 15/45 (SW480, NCI-H460, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.043 | 5/43 (A498, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.678×** | -6.9 | 3e-09 | 23/47 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -6.4 | 4e-08 | 19/46 (A-172, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -6.2 | 1e-07 | 21/47 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.612×** | -4.7 | 3e-04 | 12/47 (A-172, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.615×** | -4.7 | 3e-04 | 12/42 (HepG2/C3A, C32, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -4.6 | 4e-04 | 17/45 (hTERT-HPNE, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.810×** | -3.9 | 0.009 | 11/47 (HS-578T, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.817×** | -3.7 | 0.014 | 9/47 (NCI-H2030, SW 900, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.829×** | -3.5 | 0.035 | 6/46 (COLO 205, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.822× | -3.1 | 0.11 | 13/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.727× | -3.1 | 0.11 | 10/42 (SW480, HepG2/C3A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 26.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -19.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.195× (z -13.1) |
| [[A498 (line)]] | wt | 19.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +10.6) | — |
| [[SW480 (line)]] | alt | 11.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.83× (z +9.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.32× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 9.01 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.84× (z +8.7) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.177× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.241× (z -10.0) |
| [[LoVo (line)]] | wt | 9.46 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.49× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 9.53 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 7.44 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0703× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 7.99 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.56× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.05× (z +10.1) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.171× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 9.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 8.99 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0865× (z -9.4) |
| [[SNU-423 (line)]] | alt | 8.70 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P5]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[OGG1]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[BCL7C]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | +0.60 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[TELO2]] | +0.60 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CORO7]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[PXMP2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SMPD4BP]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GFOD2]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[ZNF250]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SRD5A1]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SDHAP2]] | +0.58 | +0.37 / +0.62 | both halves | 8e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUNDC1]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ATRX]] | -0.60 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[ZMYM4]] | -0.59 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[CLCN3]] | -0.58 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[PSMD4]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ASF1A]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[CAPS2]] | -0.57 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TLR6]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[SYNE1]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[THOC7]] | -0.56 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ACOT13]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MRPL45]] | -0.55 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRG1]] | B | NRG1 activity raises SPATA33's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 1.29× lower at baseline in the lines without NRG1 | 0.056 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23 |
| [[PSMB5]] | B | PSMB5 activity raises SPATA33's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.485). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-3.3, -0.2); signed map (-44.0, -2.4). **Vector** length 81.5, 15.3% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +14.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +17.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +9.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +21.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.1 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,657,740-89,671,272 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31606; previously C16orf55 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N06](https://www.uniprot.org/uniprotkb/Q96N06) (Spermatogenesis-associated protein 33):

> Plays an important role in sperm motility and male fertility (By similarity). Required for sperm midpiece flexibility and for the localization of sperm calcineurin to the mitochondria (By similarity). Promotes mitophagy as well as acts as an autophagy mediator in male germline cells (By similarity). Links damaged mitochondria to autophagosomes via its binding to the outer mitochondrial membrane protein VDAC2, as well as to key autophagy machinery component ATG16L1 (By similarity).

**Summary**, from NCBI Gene [124045](https://www.ncbi.nlm.nih.gov/gene/124045):

> Predicted to be involved in mitophagy. Predicted to act upstream of or within fertilization; flagellated sperm motility; and intracellular protein localization. Predicted to be located in sperm mitochondrial sheath. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26463) · Entrez [124045](https://www.ncbi.nlm.nih.gov/gene/124045) · UniProt [Q96N06](https://www.uniprot.org/uniprotkb/Q96N06) · Ensembl [ENSG00000167523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167523)

## Data

Gene col 9477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9477); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9477]; `tensor/DDL_lfc|DDL_z.npy` [9477]; `embed/gene_vectors.npy` [9477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9477 or target_col == 9477). Every well: [[SPATA33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
