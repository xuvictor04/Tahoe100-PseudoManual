---
symbol: "PABPC1L"
type: "gene"
col: 2070
ensembl_id: "ENSG00000101104"
name: "poly(A) binding protein cytoplasmic 1 like"
location: "20q13.12"
module: 63
arm: "+"
pooled_cpm: 34.83
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# PABPC1L

*poly(A) binding protein cytoplasmic 1 like* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.77× (z +9.5, q 1e-18, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.777× (z -5.9, q 2e-06, down in 26 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.786× (z -4.7, q 6e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF2]] (+0.67, fdr 1e-05), [[GTPBP2]] (+0.64, fdr 7e-06), [[PIP5KL1]] (+0.60, fdr 9e-06); moves opposite to [[SCAF11]] (-0.60, fdr 1e-05), [[XPA]] (-0.58, fdr 3e-05), [[EFNA1]] (-0.52, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CHAC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +9.5 | 1e-18 | 37/48 (LoVo, C32, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.60×** | +7.8 | 2e-12 | 31/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +7.1 | 3e-10 | 35/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.34×** | +6.8 | 1e-09 | 30/48 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.49×** | +6.6 | 4e-09 | 31/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.43×** | +5.9 | 3e-07 | 29/47 (NCI-H2030, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +4.8 | 1e-04 | 22/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.31×** | +4.5 | 5e-04 | 22/47 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.28×** | +4.1 | 0.002 | 23/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.002 | 22/48 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.29×** | +4.0 | 0.003 | 17/45 (LOX-IMVI, RKO, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.007 | 16/48 (HEC-1-A, SNU-1, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.032 | 15/34 (NCI-H1573, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.059 | 17/48 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.1 | 0.080 | 14/48 (BT-474, LS 180, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.084 | 17/48 (SW480, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.777×** | -5.9 | 2e-06 | 26/47 (J82, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.737×** | -4.8 | 4e-04 | 22/48 (KATO III, J82, …) | rises with dose | composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.786×** | -4.7 | 6e-04 | 20/48 (SK-MEL-2, A-427, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.769×** | -4.3 | 0.002 | 20/48 (KATO III, HT-29, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.798×** | -3.7 | 0.023 | 18/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.654×** | -3.7 | 0.023 | 20/46 (H4, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -3.6 | 0.026 | 17/48 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.810×** | -3.5 | 0.038 | 9/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.814×** | -3.4 | 0.044 | 12/47 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.809×** | -3.4 | 0.044 | 14/47 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.820×** | -3.1 | 0.087 | 19/47 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 29.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -8.9) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.159× (z -8.8) |
| [[HT-29 (line)]] | alt | 49.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.06× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 56.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 25.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.80× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.334× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.221× (z -8.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 18.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.48× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.254× (z -10.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H23 (line)]] | alt | 69.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[PANC-1 (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 52.5 | 1 | 0 | [[Artesunate (drug)]] 5 µM 1.94× (z +9.8) | — |
| [[A-172 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF2]] | +0.67 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[GTPBP2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PIP5KL1]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[HSPA9]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[GOT1]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[IARS1]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[FAM53A]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MOCOS]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[MTHFD2]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SLC1A5]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[FERMT3]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TRIB3]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF11]] | -0.60 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[XPA]] | -0.58 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[EFNA1]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RAB9A]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[NFYB]] | -0.51 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PKN2]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[NDUFA5]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[MIER1]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[STXBP3]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TAPT1]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[KMT2A]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHAC1]] | B | CHAC1 activity raises PABPC1L's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without CHAC1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, 44.8); signed map (-10.8, 24.8). **Vector** length 106, 25.2% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.6 | +6.6 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.4 | +6.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.5 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -6.0 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -5.0 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.1 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) binding protein cytoplasmic 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,910,060-44,959,035 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1069P2.3, PABPC1L1, ePAB; previously C20orf119 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4VXU2](https://www.uniprot.org/uniprotkb/Q4VXU2) (Polyadenylate-binding protein 1-like):

> Poly(A)-binding protein involved in oocyte maturation and early embryo development. It is required for cytosolic mRNA polyadenylation and translational activation of maternally stored mRNA in oocytes (By similarity).

**Summary**, from NCBI Gene [80336](https://www.ncbi.nlm.nih.gov/gene/80336):

> This gene belongs to the polyadenylate-binding protein type-1 family of proteins. Members of this family bind to the polyA tails of mRNAs to regulate mRNA stability and translation. The mouse ortholog of this gene is required for female fertility. In human, expression of a functional protein is regulated by alternative splicing. The protein-coding splice variant for this gene is abundantly expressed in human oocytes, while a noncoding splice variant subject to nonsense-mediated decay is the …

**Accessions** — [HGNC:15797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15797) · Entrez [80336](https://www.ncbi.nlm.nih.gov/gene/80336) · UniProt [Q4VXU2](https://www.uniprot.org/uniprotkb/Q4VXU2) · Ensembl [ENSG00000101104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101104)

## Data

Gene col 2070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2070); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2070]; `tensor/DDL_lfc|DDL_z.npy` [2070]; `embed/gene_vectors.npy` [2070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2070 or target_col == 2070). Every well: [[PABPC1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PABPC1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
