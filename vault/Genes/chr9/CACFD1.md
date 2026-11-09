---
symbol: "CACFD1"
type: "gene"
col: 8341
ensembl_id: "ENSG00000160325"
name: "calcium channel flower domain containing 1"
location: "9q34.2"
module: 2
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CACFD1

*calcium channel flower domain containing 1* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.65× (z +9.0, q 1e-16, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.31× (z +8.1, q 2e-13, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.610× (z -4.8, q 8e-04, down in 11 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHC2]] (+0.62, fdr 1e-05), [[KIAA1522]] (+0.61, fdr 1e-05), [[MBD6]] (+0.59, fdr 1e-05); moves opposite to [[ACTL6A]] (-0.61, fdr 3e-05), [[SUV39H2]] (-0.51, fdr 3e-05), [[GSTCD]] (-0.51, fdr 7e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PRR36]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.0 | 1e-16 | 2/3 (HT-29, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +8.1 | 2e-13 | 24/36 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +6.8 | 2e-09 | 4/14 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.4 | 9e-06 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.6 | 6e-04 | 3/11 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +3.8 | 0.011 | 3/23 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.67×** | +3.5 | 0.033 | 3/26 (A498, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.064 | 5/23 (A-172, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.2 | 0.084 | 4/12 (KATO III, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.57× | +3.1 | 0.11 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | 1.43× | +3.1 | 0.11 | 3/24 (LS 180, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8341.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.610×** | -4.8 | 8e-04 | 11/33 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -4.7 | 8e-04 | 11/25 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -4.4 | 0.002 | 9/32 (HT-29, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -4.3 | 0.002 | 10/25 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.734×** | -4.3 | 0.002 | 14/29 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -4.1 | 0.004 | 11/31 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.688×** | -3.6 | 0.023 | 11/47 (LoVo, hTERT-HPNE, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.692×** | -3.6 | 0.025 | 8/38 (SW480, LoVo, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.711×** | -3.3 | 0.059 | 9/42 (Panc 03.27, RPMI-7951, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.730× | -3.1 | 0.13 | 3/40 (SW48, HCT15, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.952 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.905 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.756 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.907 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHC2]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[KIAA1522]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[MBD6]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PIP4P1]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[AMDHD2]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ENGASE]] | +0.55 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[LZTS3]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[DDA1]] | +0.54 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[UAP1L1]] | +0.54 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[WBP2]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[MAP2K2]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PPM1M]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTL6A]] | -0.61 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[SUV39H2]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GSTCD]] | -0.51 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[DUT]] | -0.50 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[VRK1]] | -0.49 | -0.37 / -0.53 | both halves | 9e-05 |  |
| [[RECQL]] | -0.48 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TDP1]] | -0.48 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SRBD1]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[KNTC1]] | -0.48 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[ATAD5]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DDIAS]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TBC1D4]] | -0.48 | -0.37 / -0.49 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR36]] | B | PRR36 activity raises CACFD1's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.39× lower at baseline in the lines without PRR36 | 0.006 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[EPS8L2]] | B | EPS8L2 activity raises CACFD1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without EPS8L2 | 0.019 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[NOXA1]] | B | NOXA1 activity raises CACFD1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without NOXA1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[CAMSAP3]] | B | CAMSAP3 activity raises CACFD1's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.51× lower at baseline in the lines without CAMSAP3 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CACFD1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HMOX1]] | B | HMOX1 activity lowers CACFD1's level | lines that do not express HMOX1 (9) vs lines expressing it (41) | 1.42× higher at baseline in the lines without HMOX1 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.317). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-3.2, 30.7); signed map (-7.0, 18.5). **Vector** length 40.0, 4.21% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.5 | +8.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.2 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.3 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -0.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | calcium channel flower domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,459,965-133,470,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D9S2135, flower; previously C9orf7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGQ2](https://www.uniprot.org/uniprotkb/Q9UGQ2) (Calcium channel flower homolog):

> Transmembrane protein which mediates synaptic endocytosis and fitness-based cell culling. In response to different stimulus strengths, controls two major modes of synaptic vesicle (SV) retrieval in hippocampal neurons; Clathrin-mediated endocytosis (CME) in response to mild stimulation and activity-dependent bulk endocytosis (ADBE) in response to strong stimulation (By similarity). In cytotoxic T-lymphocytes (CTLs) facilitates calcium-dependent endocytosis of cytotoxic granules at the immuno …

**Summary**, from NCBI Gene [11094](https://www.ncbi.nlm.nih.gov/gene/11094):

> Predicted to be involved in vesicle-mediated transport. Predicted to act upstream of or within endocytosis. Predicted to be located in Golgi apparatus; cytoplasmic vesicle; and endoplasmic reticulum membrane. Predicted to be active in plasma membrane; synapse; and vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1365) · Entrez [11094](https://www.ncbi.nlm.nih.gov/gene/11094) · UniProt [Q9UGQ2](https://www.uniprot.org/uniprotkb/Q9UGQ2) · Ensembl [ENSG00000160325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160325)

## Data

Gene col 8341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8341); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8341]; `tensor/DDL_lfc|DDL_z.npy` [8341]; `embed/gene_vectors.npy` [8341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8341 or target_col == 8341). Every well: [[CACFD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACFD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
