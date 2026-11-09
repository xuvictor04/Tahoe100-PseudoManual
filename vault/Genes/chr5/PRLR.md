---
symbol: "PRLR"
type: "gene"
col: 3467
ensembl_id: "ENSG00000113494"
name: "prolactin receptor"
location: "5p13.2"
module: 9
arm: "+"
pooled_cpm: 6.0
n_lines_expressing: 21
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PRLR

*prolactin receptor* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.15× (z +15.5, q 0e+00, up in 14 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0672×, BT-474 0.211×; ⚠ cell-cycle shift, explains ~12% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0549×); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.0654×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.187×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0951×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUT9]] (+0.65, fdr 1e-05), [[PGR]] (+0.60, fdr 1e-05), [[GPNMB]] (+0.57, fdr 2e-05); moves opposite to [[CES1]] (-0.51, fdr 4e-05), [[CCM2]] (-0.51, fdr 3e-05), [[S100A8]] (-0.51, fdr 6e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01091]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PRKG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.15×** | +15.5 | 0e+00 | 14/17 (J82, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.71×** | +14.8 | 0e+00 | 7/8 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.78×** | +14.3 | 6e-44 | 2/3 (J82, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +13.4 | 1e-38 | 6/15 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +10.5 | 8e-24 | 4/5 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +10.3 | 6e-23 | 5/16 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.49×** | +8.7 | 3e-16 | 12/15 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.30×** | +8.0 | 1e-13 | 10/15 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.4 | 1e-08 | 2/13 (SW1417, NCI-H1573) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +6.1 | 7e-08 | 8/16 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +5.1 | 2e-05 | 4/16 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.62×** | +4.8 | 7e-05 | 2/6 (J82, BT-474) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +4.6 | 2e-04 | 4/16 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.0 | 0.003 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 0/15 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.0 | 0.003 | 5/17 (J82, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.9 | 0.003 | 5/16 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.006 | 4/17 (BT-474, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.045 | 6/16 (HOP62, NCI-H23, …) | top dose only |  |
| [[Trimetrexate (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.045 | 1/15 (NCI-H1573) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.045 | 3/16 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3467.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0672×, BT-474 0.211×; ⚠ cell-cycle shift, explains ~12% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0549×); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.0654×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.187×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0951×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 5 µM |  | 0.688× | -3.4 | 0.36 | 6/15 (BT-474, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 152 | 0 | 10 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0549× (z -12.4) |
| [[J82 (line)]] | alt | 13.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.54× (z +11.1) | — |
| [[A498 (line)]] | wt | 1.70 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.5 µM 0.0482× (z -8.7) |
| [[BT-474 (line)]] | alt | 226 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -8.8) ⚠ cell-cycle shift, explains ~12% of this change |
| [[A-172 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.887 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.899 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUT9]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PGR]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 639 |
| [[GPNMB]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[DCDC2]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[FREM2]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PPARGC1A]] | +0.52 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ZNF711]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SELENOP]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[ERBB4]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PDE8B]] | +0.50 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[PLXDC2]] | +0.50 | +0.30 / +0.44 | both halves | 2e-04 |  |
| [[RERG]] | +0.49 | +0.40 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CES1]] | -0.51 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[CCM2]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[S100A8]] | -0.51 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[FBH1]] | -0.50 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[S100A9]] | -0.44 | -0.53 / -0.30 | both halves | 2e-04 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[ADCK5]] | -0.43 | -0.30 / -0.30 | both halves | 2e-04 |  |
| [[DOCK5]] | -0.43 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[LINC01440]] | -0.42 | -0.48 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | LINC01091 activity raises PRLR's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without LINC01091 | 0.093 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[LINC02147]] | C | LINC02147 activity raises PRLR's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without LINC02147 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent; co-absent with the target |
| [[UGT2B7]] | C | UGT2B7 activity raises PRLR's level | lines that do not express UGT2B7 (37) vs lines expressing it (13) | 1.49× lower at baseline in the lines without UGT2B7 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A1, AFP, RHEX; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG1]] | C | PRLR activity raises PRKG1's level | lines that do not express PRLR (29) vs lines expressing it (21) | 2.78× lower at baseline in the lines without PRLR | 0.045 | ⚠ within organs, on part of the lines; also absent: DSCAM, CTNND2, AFP; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.9, 36.5); signed map (44.8, 31.3). **Vector** length 41.0, 9.21% of its response variance represented; |z| ≥ 3 in 452 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +14.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.2 | -0.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -1.0 | +0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.8 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | +0.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.7 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | prolactin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:35,048,756-35,230,487 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 3 pathways, smallest: Prolactin receptor signaling; Growth hormone receptor signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [P16471](https://www.uniprot.org/uniprotkb/P16471) (Prolactin receptor):

> This is a receptor for the anterior pituitary hormone prolactin (PRL). Acts as a prosurvival factor for spermatozoa by inhibiting sperm capacitation through suppression of SRC kinase activation and stimulation of AKT. Isoform 4 is unable to transduce prolactin signaling. Isoform 6 is unable to transduce prolactin signaling.

**Summary**, from NCBI Gene [5618](https://www.ncbi.nlm.nih.gov/gene/5618):

> This gene encodes a receptor for the anterior pituitary hormone, prolactin, and belongs to the type I cytokine receptor family. Prolactin-dependent signaling occurs as the result of ligand-induced dimerization of the prolactin receptor. Several alternatively spliced transcript variants encoding different membrane-bound and soluble isoforms have been described for this gene, which may function to modulate the endocrine and autocrine effects of prolactin in normal tissue and cancer. [provided by …

**Accessions** — [HGNC:9446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9446) · Entrez [5618](https://www.ncbi.nlm.nih.gov/gene/5618) · UniProt [P16471](https://www.uniprot.org/uniprotkb/P16471) · Ensembl [ENSG00000113494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113494)

## Data

Gene col 3467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3467); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3467]; `tensor/DDL_lfc|DDL_z.npy` [3467]; `embed/gene_vectors.npy` [3467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3467 or target_col == 3467). Every well: [[PRLR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRLR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
