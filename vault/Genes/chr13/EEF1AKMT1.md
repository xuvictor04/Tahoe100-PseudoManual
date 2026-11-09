---
symbol: "EEF1AKMT1"
type: "gene"
col: 7435
ensembl_id: "ENSG00000150456"
name: "EEF1A lysine methyltransferase 1"
location: "13q12.11"
module: 38
arm: "+"
pooled_cpm: 14.86
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# EEF1AKMT1

*EEF1A lysine methyltransferase 1* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.16× (z +11.2, q 2e-26, up in 37 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +10.6, q 8e-24, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.428× (z -12.9, q 5e-35, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDI2-AS1]] (+0.76, fdr 7e-06), [[CDKL1]] (+0.71, fdr 7e-06), [[PLAC8L1]] (+0.69, fdr 1e-05); moves opposite to [[PLEKHH3]] (-0.61, fdr 7e-05), [[HMGN3]] (-0.59, fdr 2e-04), [[KBTBD3]] (-0.59, fdr 5e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLFNL1-AS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +11.2 | 2e-26 | 37/43 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.6 | 8e-24 | 34/46 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +7.2 | 7e-11 | 25/46 (HT-29, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.61×** | +7.2 | 7e-11 | 32/47 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.58×** | +6.6 | 6e-09 | 24/46 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +5.4 | 7e-06 | 18/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.27×** | +5.1 | 2e-05 | 20/48 (NCI-H2347, A498, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 2e-04 | 19/45 (LoVo, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.4 | 8e-04 | 12/48 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.7 | 0.012 | 2/48 (LoVo, AN3 CA) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.036 | 8/46 (SHP-77, SW 900, …) | inconsistent across doses |  |
| [[Finasteride (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.056 | 7/46 (A498, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.428×** | -12.9 | 5e-35 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.459×** | -11.8 | 1e-29 | 32/46 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.491×** | -10.4 | 6e-23 | 31/42 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.544×** | -9.2 | 4e-18 | 27/46 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -8.2 | 3e-14 | 30/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.682×** | -5.6 | 2e-06 | 22/47 (A-427, PANC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.513×** | -5.3 | 1e-05 | 20/43 (HCT15, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.717×** | -5.0 | 3e-05 | 21/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.565×** | -4.5 | 4e-04 | 15/48 (SW48, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.776×** | -3.7 | 0.012 | 12/47 (SW 1271, H4, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.064 | 7/48 (BT-474, SW 1088, …) | rises with dose |  |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.820× | -3.0 | 0.12 | 8/48 (NCI-H2030, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 4 (2 ⚠) | — | [[Hesperidin (drug)]] 5 µM 0.0677× (z -11.7) |
| [[HT-29 (line)]] | alt | 13.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.191× (z -10.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 27.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0473× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -13.6) |
| [[SW480 (line)]] | alt | 18.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -12.2) |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -9.2) |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -12.7) |
| [[RKO (line)]] | wt | 32.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 5.41 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0778× (z -9.6) |
| [[C-33 A (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -11.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0787× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0791× (z -10.2) |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0787× (z -13.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -11.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -10.3) ⚠ toxic |
| [[SW1417 (line)]] | alt | 9.24 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0607× (z -14.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDI2-AS1]] | +0.76 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[CDKL1]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.69 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[BAAT]] | +0.69 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SNAPC5]] | +0.69 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[LINC01355]] | +0.68 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[GTPBP4]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[BEND3]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ARL9]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PPIEL]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[MYH3]] | +0.67 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.67 | +0.67 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHH3]] | -0.61 | -0.68 / -0.38 | both halves | 7e-05 |  |
| [[HMGN3]] | -0.59 | -0.63 / -0.30 | both halves | 2e-04 |  |
| [[KBTBD3]] | -0.59 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CAT]] | -0.59 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[SLC25A23]] | -0.56 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[ALAD]] | -0.56 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[CYP46A1]] | -0.56 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[DCTN3]] | -0.56 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[DAAM1]] | -0.55 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLFNL1-AS1]] | C | SLFNL1-AS1 activity raises EEF1AKMT1's level | lines that do not express SLFNL1-AS1 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without SLFNL1-AS1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FAM182B, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.6, -12.3); signed map (16.7, 3.9). **Vector** length 88.7, 18.1% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.6 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +7.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.0 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.0 | +7.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -11.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -12.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.4 | -5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | EEF1A lysine methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:20,728,731-20,773,961 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously N6AMT2 |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 1 pathways, smallest: Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVE0](https://www.uniprot.org/uniprotkb/Q8WVE0) (EEF1A lysine methyltransferase 1):

> Protein N-lysine methyltransferase that selectively catalyzes the trimethylation of EEF1A at 'Lys-79'.

**Summary**, from NCBI Gene [221143](https://www.ncbi.nlm.nih.gov/gene/221143):

> Enables protein-lysine N-methyltransferase activity. Involved in peptidyl-lysine methylation. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27351) · Entrez [221143](https://www.ncbi.nlm.nih.gov/gene/221143) · UniProt [Q8WVE0](https://www.uniprot.org/uniprotkb/Q8WVE0) · Ensembl [ENSG00000150456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150456)

## Data

Gene col 7435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7435); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7435]; `tensor/DDL_lfc|DDL_z.npy` [7435]; `embed/gene_vectors.npy` [7435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7435 or target_col == 7435). Every well: [[EEF1AKMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1AKMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
