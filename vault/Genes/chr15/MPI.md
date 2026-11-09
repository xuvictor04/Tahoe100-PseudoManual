---
symbol: "MPI"
type: "gene"
col: 10962
ensembl_id: "ENSG00000178802"
name: "mannose phosphate isomerase"
location: "15q24.1"
module: 103
arm: "+"
pooled_cpm: 12.22
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# MPI

*mannose phosphate isomerase* — 15q24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.241× (z -25.5, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCKDK]] (+0.72, fdr 7e-06), [[MRPL17]] (+0.56, fdr 1e-05), [[NCKIPSD]] (+0.56, fdr 1e-05); moves opposite to [[FAM81A]] (-0.50, fdr 1e-04), [[FLJ40194]] (-0.47, fdr 1e-04), [[PP2D1]] (-0.46, fdr 9e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRIM68]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.31× | +3.4 | 0.27 | 6/47 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.3 | 0.27 | 1/48 (NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10962.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.241×** | -25.5 | 0e+00 | 44/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.311×** | -14.8 | 0e+00 | 43/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.335×** | -13.9 | 2e-41 | 41/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.371×** | -12.6 | 3e-34 | 37/45 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.508×** | -12.2 | 5e-32 | 38/44 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.424×** | -10.9 | 1e-25 | 34/43 (NCI-H1792, C-33 A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -10.1 | 5e-22 | 39/47 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.459×** | -9.5 | 1e-19 | 37/46 (PANC-1, SNU-1, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.258×** | -9.0 | 2e-17 | 32/47 (NCI-H1792, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.510×** | -8.2 | 1e-14 | 30/40 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.545×** | -7.7 | 7e-13 | 29/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.565×** | -7.3 | 2e-11 | 30/47 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.352×** | -6.9 | 2e-10 | 29/43 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.592×** | -6.7 | 1e-09 | 29/47 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.612×** | -6.2 | 2e-08 | 30/47 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.639×** | -5.7 | 4e-07 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.635×** | -5.5 | 2e-06 | 22/46 (CFPAC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.681×** | -4.9 | 3e-05 | 23/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0856× (z -29.6) |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0843× (z -24.6) |
| [[LOX-IMVI (line)]] | wt | 10.0 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0502× (z -15.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.207× (z -11.6) |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0450× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.5) |
| [[J82 (line)]] | alt | 14.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 24.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0431× (z -24.6) |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0302× (z -17.3) |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.6) |
| [[KATO III (line)]] | alt | 19.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.9) |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0845× (z -14.9) |
| [[RKO (line)]] | wt | 12.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0742× (z -12.9) |
| [[A-172 (line)]] | wt | 9.55 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -12.9) |
| [[A-427 (line)]] | wt | 9.38 | 0 | 2 (1 ⚠) | — | [[Brimonidine (drug)]] 0.5 µM 0.0452× (z -15.6) |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -13.3) |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.5) |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0443× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0903× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -11.5) |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -14.5) |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -13.6) |
| [[A549 (line)]] | wt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -16.7) |
| [[C32 (line)]] | wt | 8.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.5) |
| [[H4 (line)]] | wt | 14.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0687× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 5.80 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0465× (z -9.1) |
| [[Hs 766T (line)]] | wt | 8.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -10.0) |
| [[HS-578T (line)]] | alt | 9.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 9.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 7.97 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.1) |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0903× (z -9.0) |
| [[SW 900 (line)]] | alt | 5.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -9.2) |
| [[SW1417 (line)]] | alt | 8.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.1) |
| [[SW480 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.2) |
| [[A498 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCKDK]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 | pathway: Diseases of metabolism |
| [[MRPL17]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[NCKIPSD]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[THNSL1]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[LDHA]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[BNIP3]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CDPF1]] | +0.53 | +0.37 / +0.53 | both halves | 7e-05 |  |
| [[PRMT5]] | +0.53 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[CYBC1]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[GYS1]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[GPS1]] | +0.52 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[ZNF770]] | +0.52 | +0.37 / +0.56 | both halves | 7e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.50 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[FLJ40194]] | -0.47 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[PP2D1]] | -0.46 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[VSIG10]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[CRNDE]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PRSS48]] | -0.45 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[EOGT-DT]] | -0.44 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[CCDC65]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[FAM184B]] | -0.44 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[MAFG]] | -0.44 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[PPP1R15B-AS1]] | -0.43 | -0.29 / -0.44 | both halves | 3e-04 |  |
| [[LRRC37A16P]] | -0.42 | -0.26 / -0.33 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM68]] | C | TRIM68 activity raises MPI's level | lines that do not express TRIM68 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without TRIM68 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MNS1, ENSG00000283491, AGK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.3, -12.9); signed map (-37.0, 17.4). **Vector** length 57.5, 9.48% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +0.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.1 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -12.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.0 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -25.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | mannose phosphate isomerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,890,005-74,902,219 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 7 pathways, smallest: Synthesis of GDP-mannose; Diseases associated with glycosylation precursor biosynthesis; Synthesis of substrates in N-glycan biosythesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P34949](https://www.uniprot.org/uniprotkb/P34949) (Mannose-6-phosphate isomerase):

> Isomerase that catalyzes the interconversion of fructose-6-P and mannose-6-P and has a critical role in the supply of D-mannose derivatives required for many eukaryotic glycosylation reactions.

**Summary**, from NCBI Gene [4351](https://www.ncbi.nlm.nih.gov/gene/4351):

> Phosphomannose isomerase catalyzes the interconversion of fructose-6-phosphate and mannose-6-phosphate and plays a critical role in maintaining the supply of D-mannose derivatives, which are required for most glycosylation reactions. Mutations in the MPI gene were found in patients with carbohydrate-deficient glycoprotein syndrome, type Ib. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:7216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7216) · Entrez [4351](https://www.ncbi.nlm.nih.gov/gene/4351) · UniProt [P34949](https://www.uniprot.org/uniprotkb/P34949) · Ensembl [ENSG00000178802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178802)

## Data

Gene col 10962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10962); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10962]; `tensor/DDL_lfc|DDL_z.npy` [10962]; `embed/gene_vectors.npy` [10962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10962 or target_col == 10962). Every well: [[MPI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
