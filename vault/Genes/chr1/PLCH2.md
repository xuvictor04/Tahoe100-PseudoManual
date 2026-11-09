---
symbol: "PLCH2"
type: "gene"
col: 7381
ensembl_id: "ENSG00000149527"
name: "phospholipase C eta 2"
location: "1p36.32"
module: 34
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PLCH2

*phospholipase C eta 2* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.44× (z +10.9, q 6e-25, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +5.8, q 1e-06, up in 1 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.469× (z -5.8, q 4e-06, down in 13 of 22 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.539× (z -4.7, q 6e-04, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM8]] (+0.60, fdr 1e-05), [[RAC2]] (+0.60, fdr 1e-05), [[CYTH4]] (+0.59, fdr 2e-05); moves opposite to [[CHPT1]] (-0.51, fdr 2e-05), [[SPECC1L]] (-0.50, fdr 3e-05), [[STXBP5]] (-0.50, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RAC2]] → it (grade B ⚠); 5 go from it, the strongest it → [[MFNG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.44×** | +10.9 | 6e-25 | 1/5 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +6.8 | 3e-09 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.8 | 1e-06 | 1/18 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +5.5 | 5e-06 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +4.8 | 2e-04 | 3/18 (HepG2/C3A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.003 | 8/21 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +3.8 | 0.012 | 3/22 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +3.8 | 0.012 | 5/21 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.6 | 0.023 | 0/9 | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.55×** | +3.3 | 0.055 | 1/13 (CFPAC-1) | inconsistent across doses | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.78×** | +3.1 | 0.094 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.49× | +3.0 | 0.11 | 1/14 (COLO 205) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7381.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.469×** | -5.8 | 4e-06 | 13/22 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.539×** | -4.7 | 6e-04 | 14/22 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -4.5 | 0.001 | 13/22 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.557×** | -4.3 | 0.002 | 11/21 (PANC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.586×** | -4.1 | 0.005 | 15/21 (LOX-IMVI, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.601×** | -3.9 | 0.008 | 12/19 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -3.7 | 0.019 | 14/20 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.716×** | -3.6 | 0.019 | 3/22 (SW1417, COLO 205, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.637× | -3.2 | 0.10 | 3/22 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.670× | -3.1 | 0.12 | 11/22 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.664× | -3.0 | 0.12 | 10/21 (H4, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.665× | -3.0 | 0.12 | 5/22 (HOP62, A-172, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.677× | -3.0 | 0.12 | 1/21 (NCI-H1573) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -13.2) |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0742× (z -9.2) |
| [[HOP62 (line)]] | alt | 5.37 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0652× (z -8.6) |
| [[HT-29 (line)]] | alt | 5.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0960× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 7.10 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0202× (z -13.2) |
| [[SW480 (line)]] | alt | 2.83 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0352× (z -12.1) |
| [[A-172 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.695 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.876 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.714 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM8]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[RAC2]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CYTH4]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[GNA15]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PTGS1]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[SLC45A3]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[LRFN5]] | +0.56 | +0.49 / +0.64 | both halves | 2e-05 |  |
| [[RAP1GAP]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[MAP2K3]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[KRT15]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CSF1R]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SPECC1L]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[STXBP5]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[NCOA6]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[AK3]] | -0.47 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[SGMS1]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[GNAQ]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 | STRING 589 |
| [[SNX13]] | -0.45 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[DIPK1A]] | -0.45 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[VRK2]] | -0.45 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[KPNA3]] | -0.45 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[PTPMT1]] | -0.44 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC2]] | B | RAC2 activity raises PLCH2's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without RAC2 | 0.042 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[VAV1]] | C | VAV1 activity raises PLCH2's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without VAV1 | 0.096 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFNG]] | B | PLCH2 activity raises MFNG's level | lines that do not express PLCH2 (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without PLCH2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent |
| [[CYTH4]] | B | PLCH2 activity raises CYTH4's level | lines that do not express PLCH2 (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without PLCH2 | 0.069 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent |
| [[TNFRSF10B]] | B | PLCH2 activity weakens TNFRSF10B's drug response | lines that do not express PLCH2 (26) vs lines expressing it (22) | the lines without PLCH2 respond 1.00× as strongly (z diff -0.40); strongest at Idarubicin (hydrochloride) 5 µM: 1.67x vs 1.20x (z diff -3.3) | 0.076 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[CDC42BPG]] | B | PLCH2 activity raises CDC42BPG's level | lines that do not express PLCH2 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without PLCH2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent |
| [[DIPK1A]] | B | PLCH2 activity lowers DIPK1A's level | lines that do not express PLCH2 (26) vs lines expressing it (24) | 1.45× higher at baseline in the lines without PLCH2 | 0.096 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.416). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.6, -0.2); signed map (0.1, 48.0). **Vector** length 51.6, 12.0% of its response variance represented; |z| ≥ 3 in 620 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C eta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:2,425,980-2,505,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0450, PLCeta2, RP3-395M20.1, PLC-eta2; previously PLCL4 |
| Gene groups (HGNC) | Phospholipases; EF-hand domain containing |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O75038](https://www.uniprot.org/uniprotkb/O75038) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase eta-2):

> The production of the second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3) is mediated by activated phosphatidylinositol-specific phospholipase C enzymes. This phospholipase activity is very sensitive to calcium. May be important for formation and maintenance of the neuronal network in the postnatal brain (By similarity).

**Summary**, from NCBI Gene [9651](https://www.ncbi.nlm.nih.gov/gene/9651):

> PLCH2 is a member of the PLC-eta family of the phosphoinositide-specific phospholipase C (PLC) superfamily of enzymes that cleave PtdIns(4,5) P2 to generate second messengers inositol 1,4,5-trisphosphate and diacylglycerol (Zhou et al., 2005 [PubMed 16107206]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:29037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29037) · Entrez [9651](https://www.ncbi.nlm.nih.gov/gene/9651) · UniProt [O75038](https://www.uniprot.org/uniprotkb/O75038) · Ensembl [ENSG00000149527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149527)

## Data

Gene col 7381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7381); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7381]; `tensor/DDL_lfc|DDL_z.npy` [7381]; `embed/gene_vectors.npy` [7381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7381 or target_col == 7381). Every well: [[PLCH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
