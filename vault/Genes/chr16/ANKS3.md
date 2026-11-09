---
symbol: "ANKS3"
type: "gene"
col: 9599
ensembl_id: "ENSG00000168096"
name: "ankyrin repeat and sterile alpha motif domain containing 3"
location: "16p13.3"
module: 52
arm: "+"
pooled_cpm: 34.26
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# ANKS3

*ankyrin repeat and sterile alpha motif domain containing 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.23× (z +3.9, q 0.042, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.481× (z -13.8, q 9e-41, down in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.513× (z -12.2, q 1e-31, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAT9]] (+0.79, fdr 7e-06), [[LCMT1]] (+0.77, fdr 7e-06), [[TMEM120B]] (+0.74, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.72, fdr 7e-06), [[EIF4G2]] (-0.69, fdr 7e-06), [[DDX3X]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.042 | 20/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.042 | 12/48 (A-172, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.088 | 19/48 (SW480, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.21 | 13/47 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9599.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.481×** | -13.8 | 9e-41 | 38/45 (H4, A498, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.490×** | -12.5 | 3e-33 | 29/42 (hTERT-HPNE, A498, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -12.2 | 1e-31 | 41/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.560×** | -11.0 | 7e-26 | 37/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.601×** | -9.3 | 2e-18 | 26/39 (A-172, AsPC-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -8.6 | 7e-16 | 28/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -7.7 | 1e-12 | 29/48 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.762×** | -7.3 | 3e-11 | 32/48 (COLO 205, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.776×** | -6.8 | 8e-10 | 29/48 (NCI-H2347, SNU-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.786×** | -6.4 | 7e-09 | 23/47 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.752×** | -5.4 | 4e-06 | 25/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.758×** | -5.2 | 8e-06 | 24/47 (LS 180, SNU-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -5.1 | 2e-05 | 23/48 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.761×** | -5.0 | 3e-05 | 23/47 (LoVo, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.775×** | -4.8 | 6e-05 | 24/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -4.5 | 2e-04 | 21/48 (KATO III, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -4.3 | 4e-04 | 23/47 (H4, NCI-H661, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -4.1 | 0.001 | 16/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.819×** | -3.8 | 0.005 | 12/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.847× | -3.1 | 0.036 | 18/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.890× | -3.1 | 0.040 | 8/48 (A-172, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 45.3 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.133× (z -17.2) |
| [[A498 (line)]] | wt | 65.7 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -17.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.280× (z -14.0) |
| [[A-172 (line)]] | wt | 47.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0784× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -11.7) |
| [[SNU-1 (line)]] | wt | 44.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.193× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 35.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -10.5) |
| [[A549 (line)]] | wt | 43.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.284× (z -9.9) |
| [[C32 (line)]] | wt | 31.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.248× (z -9.8) |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.246× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0590× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.241× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.202× (z -17.9) |
| [[PANC-1 (line)]] | alt | 41.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.399× (z -9.3) |
| [[A-427 (line)]] | wt | 30.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -14.3) |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.298× (z -9.7) |
| [[H4 (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0692× (z -15.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 35.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.346× (z -9.1) |
| [[LoVo (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 34.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.369× (z -8.5) |
| [[SHP-77 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.129× (z -8.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 28.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.297× (z -9.4) |
| [[SW 900 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -9.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -10.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAT9]] | +0.79 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.77 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.74 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NAA35]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[SOCS7]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.70 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[DPH7]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[DRD4]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[MIGA2]] | +0.68 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[SNU13]] | +0.68 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[YIPF2]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.72 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.69 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[DDX3X]] | -0.65 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[NXT2]] | -0.64 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[NCOA4]] | -0.63 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[IL6ST]] | -0.63 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[YWHAE]] | -0.62 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[RAP2C]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MAPRE1]] | -0.60 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.60 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.59 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ANKS3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RBM24]] | B | RBM24 activity strengthens ANKS3's drug response | lines that do not express RBM24 (23) vs lines expressing it (25) | the lines without RBM24 respond 0.75× as strongly (z diff +1.06); strongest at Dinaciclib 5 µM: 0.72x vs 0.41x (z diff +3.7) | 0.068 | ⚠ within organs, on part of the lines; also absent: SRGN, P3H2, FMN2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (0.6, -15.6); signed map (-37.3, 1.3). **Vector** length 112, 28.9% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.8 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.4 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -13.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and sterile alpha motif domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,696,510-4,734,378 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1977, FLJ32345, FLJ32767 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZW76](https://www.uniprot.org/uniprotkb/Q6ZW76) (Ankyrin repeat and SAM domain-containing protein 3):

> May be involved in vasopressin signaling in the kidney.

**Summary**, from NCBI Gene [124401](https://www.ncbi.nlm.nih.gov/gene/124401):

> Predicted to be located in cytoplasm. Predicted to be active in cilium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29422) · Entrez [124401](https://www.ncbi.nlm.nih.gov/gene/124401) · UniProt [Q6ZW76](https://www.uniprot.org/uniprotkb/Q6ZW76) · Ensembl [ENSG00000168096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168096)

## Data

Gene col 9599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9599); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9599]; `tensor/DDL_lfc|DDL_z.npy` [9599]; `embed/gene_vectors.npy` [9599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9599 or target_col == 9599). Every well: [[ANKS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
