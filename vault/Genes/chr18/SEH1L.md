---
symbol: "SEH1L"
type: "gene"
col: 1425
ensembl_id: "ENSG00000085415"
name: "SEH1 like nucleoporin"
location: "18p11.21"
module: 18
arm: "+"
pooled_cpm: 59.02
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SEH1L

*SEH1 like nucleoporin* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.77× (z +10.1, q 3e-21, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.774× (z -6.4, q 1e-07, down in 27 of 47 measured lines) ⚠ cell-cycle shift, explains ~19% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.747× (z -4.9, q 3e-04, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDN1]] (+0.73, fdr 7e-06), [[CAD]] (+0.72, fdr 7e-06), [[MRPS25]] (+0.72, fdr 7e-06); moves opposite to [[SLC4A1AP]] (-0.64, fdr 7e-06), [[ASB8]] (-0.62, fdr 7e-06), [[CDKN1B]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BEGAIN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +10.1 | 3e-21 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +10.1 | 3e-21 | 43/47 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +9.9 | 1e-20 | 37/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +9.5 | 2e-19 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.69×** | +9.3 | 2e-18 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +8.0 | 1e-13 | 35/46 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.88×** | +5.8 | 4e-07 | 34/47 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +5.3 | 1e-05 | 31/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.2 | 1e-05 | 25/43 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +4.9 | 5e-05 | 24/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.4 | 5e-04 | 23/44 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.006 | 19/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.008 | 16/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.011 | 21/47 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.021 | 17/47 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.774×** | -6.4 | 1e-07 | 27/47 (RKO, LoVo, …) | top dose only | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.747×** | -4.9 | 3e-04 | 25/46 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -4.8 | 3e-04 | 23/47 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.791×** | -4.4 | 0.001 | 22/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.772×** | -4.3 | 0.002 | 22/47 (SW480, RKO, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.789×** | -4.1 | 0.003 | 21/47 (A498, NCI-H23, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.796×** | -4.0 | 0.005 | 22/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.802×** | -3.9 | 0.008 | 22/46 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.809×** | -3.7 | 0.013 | 16/46 (BT-474, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.858× | -3.6 | 0.015 | 16/47 (SW480, CHP-212, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.839× | -3.5 | 0.027 | 13/47 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.821×** | -3.3 | 0.044 | 19/46 (LoVo, SW480, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.744×** | -3.2 | 0.051 | 17/47 (SW1417, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.860× | -3.1 | 0.080 | 18/47 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.840× | -3.1 | 0.084 | 9/47 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 94.2 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.91× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.90× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -12.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[PANC-1 (line)]] | alt | 80.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 50.4 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.82× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 2.73× (z +9.2) | — |
| [[RKO (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -16.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[AN3 CA (line)]] | alt | 60.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[LoVo (line)]] | wt | 46.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.73× (z +9.9) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[NCI-H1573 (line)]] | alt | 33.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 130 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.5) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 43.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 66.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.73× (z +9.2) ⚠ unreliable plate only | — |
| [[KATO III (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LS 180 (line)]] | wt | 50.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.4) ⚠ cell-cycle shift, explains ~19% of this change |
| [[MIA PaCa-2 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.52× (z +8.7) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 54.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.444× (z -8.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SNU-1 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDN1]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[CAD]] | +0.72 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[MRPS25]] | +0.72 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 | pathway: tRNA processing |
| [[URB1]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[GART]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[TUBGCP4]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[UBE2G2]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[AHCY]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[CARNMT1]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[DKC1]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A1AP]] | -0.64 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[ASB8]] | -0.62 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[CDKN1B]] | -0.61 | -0.65 / -0.57 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[CIR1]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[KMT2A]] | -0.58 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[XRN1]] | -0.57 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.57 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[GOLGB1]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PI4KB]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[GPBP1]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[CDKN2C]] | -0.55 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEGAIN]] | B | BEGAIN activity raises SEH1L's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without BEGAIN | 0.009 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[CENPV]] | B | CENPV activity raises SEH1L's level | lines that do not express CENPV (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without CENPV | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.2, -36.9); signed map (-4.0, -51.7). **Vector** length 116, 32.8% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.65 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | +4.7 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +4.2 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.9 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | +0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -6.0 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.0 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | SEH1 like nucleoporin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:12,947,133-12,987,536 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEH1A, SEH1B, Seh1, SEC13L |
| Gene groups (HGNC) | WD repeat domain containing; Nucleoporins; GATOR2 subcomplex |
| Reactome | 87 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EE3](https://www.uniprot.org/uniprotkb/Q96EE3) (Nucleoporin SEH1):

> Component of the Nup107-160 subcomplex of the nuclear pore complex (NPC). The Nup107-160 subcomplex is required for the assembly of a functional NPC. The Nup107-160 subcomplex is also required for normal kinetochore microtubule attachment, mitotic progression and chromosome segregation. This subunit plays a role in recruitment of the Nup107-160 subcomplex to the kinetochore.; As a component of the GATOR2 complex, functions as an activator of the amino acid-sensing branch of the mTORC1 signaling …

**Summary**, from NCBI Gene [81929](https://www.ncbi.nlm.nih.gov/gene/81929):

> The protein encoded by this gene is part of a nuclear pore complex, Nup107-160. This protein contains WD repeats and shares 34% amino acid identity with yeast Seh1 and 30% identity with yeast Sec13. All constituents of the Nup107-160 complex, including this protein, specifically localize to kinetochores in mitosis. Two alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30379) · Entrez [81929](https://www.ncbi.nlm.nih.gov/gene/81929) · UniProt [Q96EE3](https://www.uniprot.org/uniprotkb/Q96EE3) · Ensembl [ENSG00000085415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085415)

## Data

Gene col 1425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1425); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1425]; `tensor/DDL_lfc|DDL_z.npy` [1425]; `embed/gene_vectors.npy` [1425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1425 or target_col == 1425). Every well: [[SEH1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEH1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
