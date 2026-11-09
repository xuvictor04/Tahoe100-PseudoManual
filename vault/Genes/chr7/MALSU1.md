---
symbol: "MALSU1"
type: "gene"
col: 8024
ensembl_id: "ENSG00000156928"
name: "mitochondrial assembly of ribosomal large subunit 1"
location: "7p15.3"
module: 54
arm: "+"
pooled_cpm: 32.06
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MALSU1

*mitochondrial assembly of ribosomal large subunit 1* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.93× (z +7.5, q 2e-11, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.594× (z -5.7, q 7e-06, down in 23 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.781× (z -4.0, q 0.011, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (AN3 CA 0.0435×, SNU-1 0.193×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.247×, SW480 0.313×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.143×, A-172 0.240×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.399×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C15orf61]] (+0.77, fdr 1e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[ATP5MJ]] (+0.76, fdr 1e-05), [[MMS19]] (+0.76, fdr 7e-06), [[FAM193B]] (+0.75, fdr 7e-06); moves opposite to [[MAPRE1]] (-0.76, fdr 1e-05), [[ZNF655]] (-0.74, fdr 1e-05), [[CCDC200]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EID2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +7.5 | 2e-11 | 45/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.92×** | +7.5 | 2e-11 | 39/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.90×** | +7.4 | 3e-11 | 44/48 (SW480, Hs 766T, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.75×** | +6.4 | 2e-08 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.64×** | +5.6 | 2e-06 | 32/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +5.4 | 6e-06 | 35/49 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.6 | 4e-04 | 29/46 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 29/48 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +4.0 | 0.004 | 26/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.39×** | +3.8 | 0.008 | 24/48 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.41×** | +3.8 | 0.008 | 25/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.016 | 25/48 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.2 | 0.063 | 19/48 (HEC-1-A, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8024.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (AN3 CA 0.0435×, SNU-1 0.193×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.247×, SW480 0.313×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.143×, A-172 0.240×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.399×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.594×** | -5.7 | 7e-06 | 23/37 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.650×** | -4.5 | 0.002 | 27/42 (AN3 CA, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.629×** | -4.0 | 0.011 | 23/45 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.781×** | -4.0 | 0.011 | 25/48 (AN3 CA, SNU-1, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.749× | -3.3 | 0.11 | 21/48 (HT-29, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 185 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0435× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.399× (z -8.5) |
| [[A-172 (line)]] | wt | 38.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -10.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.71× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf61]] ⚠ | +0.77 | +0.50 / +0.79 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.76 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[MMS19]] | +0.76 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[FAM193B]] | +0.75 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[LSM2]] | +0.75 | +0.57 / +0.72 | both halves | 8e-06 |  |
| [[ELP2]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MHENCR]] | +0.74 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[MINCR]] | +0.74 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[CRYZL1]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[RBIS]] | +0.73 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.73 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[COX14]] | +0.73 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[CCZ1]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.76 | -0.55 / -0.81 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.74 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[CCDC200]] | -0.73 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[WDR1]] | -0.71 | -0.54 / -0.78 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | -0.71 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[CHMP3]] | -0.70 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[DDX5]] | -0.68 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[THOC6]] | -0.68 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.68 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[TRIP12]] | -0.68 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.67 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.67 | -0.52 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises MALSU1's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without EID2B | 0.036 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[STK26]] | B | STK26 activity lowers MALSU1's level | lines that do not express STK26 (5) vs lines expressing it (45) | 1.77× higher at baseline in the lines without STK26 | 0.056 | ⚠ across organs; maybe low, not absent |
| [[RECK]] | B | RECK activity raises MALSU1's level | lines that do not express RECK (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without RECK | 0.068 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[XKR8]] | B | XKR8 activity lowers MALSU1's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.34× higher at baseline in the lines without XKR8 | 0.093 | ⚠ within organs, on part of the lines; also absent: MORC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.844). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.1, -13.2); signed map (-34.8, 4.3). **Vector** length 100, 28.3% of its response variance represented; |z| ≥ 3 in 655 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial translation elongation* (reactome, mean cos +0.55 to 8); *Mitochondrial translation initiation* (reactome, mean cos +0.55 to 8); *Mitochondrial translation termination* (reactome, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.9 | +7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.2 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.1 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial assembly of ribosomal large subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,298,739-23,311,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mtRsfA; previously C7orf30 |
| Reactome | 3 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EH3](https://www.uniprot.org/uniprotkb/Q96EH3) (Mitochondrial assembly of ribosomal large subunit protein 1):

> Required for normal mitochondrial ribosome function and mitochondrial translation. May play a role in ribosome biogenesis by preventing premature association of the 28S and 39S ribosomal subunits (Probable). Interacts with mitochondrial ribosomal protein uL14m (MRPL14), probably blocking formation of intersubunit bridge B8, preventing association of the 28S and 39S ribosomal subunits (Probable). Addition to isolated mitochondrial ribosomal subunits partially inhibits translation, probably by …

**Summary**, from NCBI Gene [115416](https://www.ncbi.nlm.nih.gov/gene/115416):

> Enables mitochondrial large ribosomal subunit binding activity. Involved in mitochondrial large ribosomal subunit assembly and negative regulation of mitochondrial translation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21721) · Entrez [115416](https://www.ncbi.nlm.nih.gov/gene/115416) · UniProt [Q96EH3](https://www.uniprot.org/uniprotkb/Q96EH3) · Ensembl [ENSG00000156928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156928)

## Data

Gene col 8024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8024); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8024]; `tensor/DDL_lfc|DDL_z.npy` [8024]; `embed/gene_vectors.npy` [8024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8024 or target_col == 8024). Every well: [[MALSU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MALSU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
