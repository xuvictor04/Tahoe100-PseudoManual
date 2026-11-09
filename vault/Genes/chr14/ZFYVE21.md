---
symbol: "ZFYVE21"
type: "gene"
col: 2012
ensembl_id: "ENSG00000100711"
name: "zinc finger FYVE-type containing 21"
location: "14q32.33"
module: 2
arm: "+"
pooled_cpm: 11.81
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ZFYVE21

*zinc finger FYVE-type containing 21* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +12.2, q 2e-31, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.452× (z -13.4, q 2e-38, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GIT1]] (+0.70, fdr 1e-05), [[ADCK5]] (+0.70, fdr 9e-06), [[FBH1]] (+0.70, fdr 7e-06); moves opposite to [[ATF7IP]] (-0.59, fdr 1e-05), [[ZNF155]] (-0.58, fdr 1e-05), [[ZNF260]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDE4D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +12.2 | 2e-31 | 33/44 (NCI-H2030, A549, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +7.6 | 7e-12 | 26/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +6.0 | 4e-07 | 17/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 8e-06 | 18/46 (LOX-IMVI, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.2 | 2e-05 | 14/38 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +4.9 | 1e-04 | 15/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +3.6 | 0.030 | 12/44 (RKO, SW480, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.22×** | +3.5 | 0.038 | 11/40 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.058 | 8/44 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.059 | 5/44 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.2 | 0.059 | 5/26 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.059 | 7/44 (CFPAC-1, SW 900, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.076 | 13/45 (NCI-H2030, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.452×** | -13.4 | 2e-38 | 35/46 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.273×** | -12.0 | 1e-30 | 37/48 (RKO, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.649×** | -10.7 | 1e-24 | 29/46 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.701×** | -8.8 | 2e-16 | 30/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -7.0 | 2e-10 | 10/48 (HCT15, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -6.7 | 2e-09 | 22/45 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.687×** | -5.9 | 3e-07 | 21/46 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -5.9 | 3e-07 | 20/47 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.543×** | -5.6 | 1e-06 | 22/43 (NCI-H2347, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.750×** | -5.1 | 2e-05 | 23/46 (HOP62, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.766×** | -4.7 | 1e-04 | 14/47 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.750×** | -4.5 | 3e-04 | 20/43 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.819×** | -3.5 | 0.020 | 10/48 (CHP-212, SW480, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.878× | -3.2 | 0.052 | 7/48 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.1 | 0.076 | 10/47 (HS-578T, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 13.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 10.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.0) |
| [[LoVo (line)]] | wt | 8.63 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 32.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.4) |
| [[A-172 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.3) |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.9) |
| [[H4 (line)]] | wt | 7.74 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0704× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.6) |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.7) |
| [[KATO III (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -8.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0673× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 5.29 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -8.5) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 7.31 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.194× (z -9.9) |
| [[RKO (line)]] | wt | 10.4 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0305× (z -9.2) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIT1]] | +0.70 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.70 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[FBH1]] | +0.70 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CAPN10]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MTM1]] | +0.67 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[MIIP]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RNF38]] | +0.63 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[SMG1P5]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SLC2A8]] | +0.62 | +0.28 / +0.68 | both halves | 3e-04 |  |
| [[CDR2L]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[RAB5B]] | +0.61 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[RUSC1]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF7IP]] | -0.59 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[ZNF155]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.57 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[SPTLC3]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[FOXP1]] | -0.56 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ZNF780B]] | -0.56 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CXCL2]] | -0.55 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[SRSF10]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[AIG1]] | -0.54 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[SENP1]] | -0.54 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4D]] | B | PDE4D activity lowers ZFYVE21's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.30× higher at baseline in the lines without PDE4D | 0.024 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.7, -20.6); signed map (-42.2, -1.9). **Vector** length 79.6, 14.2% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +5.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.7 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -13.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -8.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -3.5 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger FYVE-type containing 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,715,730-103,733,668 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2550, ZF21 |
| Gene groups (HGNC) | Zinc fingers FYVE-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ24](https://www.uniprot.org/uniprotkb/Q9BQ24) (Zinc finger FYVE domain-containing protein 21):

> Plays a role in cell adhesion, and thereby in cell motility which requires repeated formation and disassembly of focal adhesions. Regulates microtubule-induced PTK2/FAK1 dephosphorylation, an event important for focal adhesion disassembly, as well as integrin beta-1/ITGB1 cell surface expression.

**Summary**, from NCBI Gene [79038](https://www.ncbi.nlm.nih.gov/gene/79038):

> Predicted to enable zinc ion binding activity. Predicted to be located in endosome and focal adhesion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20760) · Entrez [79038](https://www.ncbi.nlm.nih.gov/gene/79038) · UniProt [Q9BQ24](https://www.uniprot.org/uniprotkb/Q9BQ24) · Ensembl [ENSG00000100711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100711)

## Data

Gene col 2012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2012); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2012]; `tensor/DDL_lfc|DDL_z.npy` [2012]; `embed/gene_vectors.npy` [2012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2012 or target_col == 2012). Every well: [[ZFYVE21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFYVE21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
