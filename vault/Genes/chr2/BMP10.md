---
symbol: "BMP10"
type: "gene"
col: 8654
ensembl_id: "ENSG00000163217"
name: "bone morphogenetic protein 10"
location: "2p13.3"
module: 102
arm: "+"
pooled_cpm: 5.02
n_lines_expressing: 3
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/102", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# BMP10

*bone morphogenetic protein 10* — 2p13.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.05× (z +7.2, q 3e-10, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.0399×; ⚠ cell-cycle shift, explains ~98% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.168×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-1 0.0857×; ⚠ cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.117×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.280×).
> Its strongest partners by |cos| (73 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02099]] (+0.90, fdr 7e-06), [[LINC01257]] (+0.51, fdr 3e-05), [[SLC38A4]] (+0.51, fdr 5e-05); moves opposite to [[IQCA1]] (-0.46, fdr 1e-04), [[AGTR1]] (-0.35, fdr 3e-04), [[SEC16B]] (-0.35, fdr 2e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[AHSG]] → it (grade C ⚠); 9 go from it, the strongest it → [[PIWIL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.05×** | +7.2 | 3e-10 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.84×** | +6.8 | 4e-09 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.45×** | +5.5 | 6e-06 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +4.8 | 2e-04 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.53×** | +4.0 | 0.007 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +3.7 | 0.022 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 2.10× | +3.1 | 0.13 | 0/1 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.0399×; ⚠ cell-cycle shift, explains ~98% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.168×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-1 0.0857×; ⚠ cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.117×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.280×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 491 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0399× (z -15.3) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -10.2) |
| [[A-172 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.413 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02099]] | +0.90 | +0.86 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[LINC01257]] | +0.51 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SLC38A4]] | +0.51 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[LINC01203]] | +0.47 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[GPM6B]] | +0.45 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[LINC02643]] | +0.43 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[FENDRR]] | +0.41 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[MEOX2]] | +0.40 | +0.20 / +0.50 | ⚠ one half (not replicated) | 8e-04 |  |
| [[FBLN2]] | +0.40 | +0.45 / +0.31 | both halves | 2e-04 | pathway: Elastic fibre formation |
| [[MLIP]] | +0.40 | +0.38 / +0.39 | both halves | 6e-05 |  |
| [[SLC47A1]] | +0.39 | +0.43 / +0.23 | both halves | 5e-04 |  |
| [[RIPOR2]] | +0.38 | +0.43 / +0.31 | both halves | 2e-04 |  |
| [[PDGFRA]] | +0.37 | +0.37 / +0.43 | both halves | 8e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCA1]] | -0.46 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[AGTR1]] | -0.35 | -0.28 / -0.27 | both halves | 3e-04 |  |
| [[SEC16B]] | -0.35 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[LINC02315]] | -0.34 | -0.29 / -0.28 | both halves | 3e-04 |  |
| [[ITIH2]] | -0.33 | -0.21 / -0.32 | both halves | 7e-04 |  |
| [[AHSG]] | -0.33 | -0.12 / -0.27 | ⚠ not reproduced | 0.002 |  |
| [[GCAWKR]] | -0.32 | -0.33 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[ZNF334]] | -0.32 | -0.31 / -0.26 | both halves | 4e-04 |  |
| [[SLC15A1]] | -0.32 | -0.25 / -0.24 | both halves | 4e-04 |  |
| [[ATP10A]] | -0.32 | -0.28 / -0.27 | both halves | 3e-04 |  |
| [[ZNF630]] | -0.32 | -0.23 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[PLCH2]] | -0.31 | -0.26 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[EPCAM-DT]] | -0.31 | -0.24 / -0.31 | both halves | 4e-04 |  |
| [[JAK3]] | -0.31 | -0.34 / -0.23 | both halves | 5e-04 |  |
| [[ADCY4]] | -0.30 | -0.23 / -0.21 | both halves | 6e-04 |  |
| [[FXYD2]] | -0.30 | -0.30 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHSG]] | C | AHSG activity raises BMP10's level | lines that do not express AHSG (45) vs lines expressing it (5) | 1.56× lower at baseline in the lines without AHSG | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises BMP10's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 1.22× lower at baseline in the lines without ITIH2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[LINC01956]] | C | LINC01956 activity raises BMP10's level | lines that do not express LINC01956 (38) vs lines expressing it (12) | 1.09× lower at baseline in the lines without LINC01956 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01440, SYT4, LINC03000; co-absent with the target |
| [[LINC00457]] | C | LINC00457 activity lowers BMP10's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.03× higher at baseline in the lines without LINC00457 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIWIL1]] | C | BMP10 activity raises PIWIL1's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 9.23× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[AHSG]] | C | BMP10 activity raises AHSG's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 3.51× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[LINC00276]] | C | BMP10 activity raises LINC00276's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 3.47× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; its own permutation p |
| [[MEOX2]] | C | BMP10 activity raises MEOX2's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 2.42× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[ITIH2]] | C | BMP10 activity raises ITIH2's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 2.26× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[GPM6B]] | C | BMP10 activity raises GPM6B's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 1.68× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; its own permutation p |
| [[GNAT3]] | C | BMP10 activity raises GNAT3's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 1.60× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[LINC00457]] | C | BMP10 activity raises LINC00457's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 1.54× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[LINC01956]] | C | BMP10 activity raises LINC01956's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 1.52× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.222). A single-armed module: all its genes lie on one side of its main direction.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (16.4, 35.3); signed map (29.8, 21.7). **Vector** length 10.7, 7.61% of its response variance represented; |z| ≥ 3 in 41 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +0.5 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +0.4 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.4 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.3 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.3 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +0.2 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.2 | -0.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +0.2 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +0.2 | -1.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -0.3 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -0.3 | +7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.2 | +0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.2 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.2 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.2 | +1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:68,860,909-68,871,397 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Bone morphogenetic proteins |
| Reactome | 5 pathways, smallest: Signaling by BMP; Molecules associated with elastic fibres; Elastic fibre formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95393](https://www.uniprot.org/uniprotkb/O95393) (Bone morphogenetic protein 10):

> Required for maintaining the proliferative activity of embryonic cardiomyocytes by preventing premature activation of the negative cell cycle regulator CDKN1C/p57KIP and maintaining the required expression levels of cardiogenic factors such as MEF2C and NKX2-5. Acts as a ligand for ACVRL1/ALK1, BMPR1A/ALK3 and BMPR1B/ALK6, leading to activation of SMAD1, SMAD5 and SMAD8 transcription factors. Inhibits endothelial cell migration and growth. May reduce cell migration and cell matrix adhesion in …

**Summary**, from NCBI Gene [27302](https://www.ncbi.nlm.nih.gov/gene/27302):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate the mature protein, which binds to the activin receptor-like kinase 1 (ALK1) and plays important roles in cardiovascular development including cardiomyocyte …

**Accessions** — [HGNC:20869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20869) · Entrez [27302](https://www.ncbi.nlm.nih.gov/gene/27302) · UniProt [O95393](https://www.uniprot.org/uniprotkb/O95393) · Ensembl [ENSG00000163217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163217)

## Data

Gene col 8654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8654); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8654]; `tensor/DDL_lfc|DDL_z.npy` [8654]; `embed/gene_vectors.npy` [8654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8654 or target_col == 8654). Every well: [[BMP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
