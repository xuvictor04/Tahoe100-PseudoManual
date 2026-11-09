---
symbol: "GPR84-AS1"
type: "gene"
col: 15083
ensembl_id: "ENSG00000258086"
name: "GPR84, ZNF385A, ITGA5 and GTSF1 antisense RNA 1"
location: "12q13.13"
module: 21
arm: "+"
pooled_cpm: 7.87
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# GPR84-AS1

*GPR84, ZNF385A, ITGA5 and GTSF1 antisense RNA 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.22× (z +16.9, q 0e+00, up in 36 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.768× (z -4.0, q 0.039, down in 9 of 48 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-423 0.0620×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.153×; ⚠ toxic; cell-cycle shift, explains ~13% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0865×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (SNU-1 0.0669×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL23A1]] (+0.68, fdr 8e-06), [[CCN4]] (+0.66, fdr 7e-06), [[ITGA5]] (+0.65, fdr 7e-06, ⚠ same locus), [[NUP210L]] (+0.63, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02885]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +16.9 | 0e+00 | 36/42 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.94×** | +16.2 | 0e+00 | 36/45 (SW480, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +14.7 | 0e+00 | 26/44 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +10.8 | 3e-25 | 23/31 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +10.2 | 2e-22 | 13/22 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.4 | 5e-19 | 10/16 (NCI-H2030, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +6.6 | 4e-09 | 20/45 (NCI-H1573, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.1 | 7e-08 | 19/45 (HOP62, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.7 | 7e-07 | 18/40 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.4 | 3e-06 | 18/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.0 | 3e-05 | 14/48 (Panc 03.27, KATO III, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.9 | 4e-05 | 11/28 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +4.5 | 2e-04 | 11/43 (HS-578T, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 2e-04 | 11/47 (A498, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.2 | 1e-03 | 12/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.003 | 9/45 (hTERT-HPNE, A-172, …) | two highest doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.009 | 10/46 (A498, SW480, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.013 | 5/45 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.019 | 4/45 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.029 | 5/42 (NCI-H23, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15083.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-423 0.0620×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.153×; ⚠ toxic; cell-cycle shift, explains ~13% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0865×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (SNU-1 0.0669×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.768×** | -4.0 | 0.039 | 9/48 (Panc 03.27, RKO, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.820× | -3.0 | 0.56 | 4/48 (SNU-423, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 6.40 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +12.1) | [[Canagliflozin (drug)]] 0.05 µM 0.0865× (z -9.1) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~13% of this change |
| [[A498 (line)]] | wt | 7.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 5.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 5.67 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.22× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 3.77 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.5× (z +9.7) | — |
| [[LoVo (line)]] | wt | 5.46 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.49× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 7.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 6.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 5.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 9.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 4.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 8.23 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.45× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0669× (z -9.0) |
| [[SNU-423 (line)]] | alt | 8.85 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0620× (z -13.0) |
| [[SW480 (line)]] | alt | 8.01 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.22× (z +10.8) | — |
| [[A-427 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL23A1]] | +0.68 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[CCN4]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ITGA5]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NUP210L]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PLCG1-AS1]] | +0.63 | +0.52 / +0.55 | both halves | 1e-05 | same gene group |
| [[ESR2]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SEC1P]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[RYR1]] | +0.61 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[ABHD15-AS1]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 | same gene group |
| [[ZNF451-AS1]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 | same gene group |
| [[SLC27A6]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[HPSE2]] | +0.60 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[AMZ1]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02885]] | B | LINC02885 activity raises GPR84-AS1's level | lines that do not express LINC02885 (15) vs lines expressing it (35) | 1.27× lower at baseline in the lines without LINC02885 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC01399, PCDHB2, ENSG00000258168; maybe low, not absent |
| [[DENND2A]] | B | DENND2A activity raises GPR84-AS1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.35× lower at baseline in the lines without DENND2A | 0.093 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[ITGA5]] | B | ITGA5 activity raises GPR84-AS1's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without ITGA5 | 0.094 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, 24.2); signed map (24.9, 14.6). **Vector** length 73.6, 12.3% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | GPR84, ZNF385A, ITGA5 and GTSF1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q13.13 — chr12:54,353,792-54,466,985 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC01154 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56187) · Entrez [102724050](https://www.ncbi.nlm.nih.gov/gene/102724050) · Ensembl [ENSG00000258086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258086)

## Data

Gene col 15083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15083); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15083]; `tensor/DDL_lfc|DDL_z.npy` [15083]; `embed/gene_vectors.npy` [15083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15083 or target_col == 15083). Every well: [[GPR84-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR84-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
