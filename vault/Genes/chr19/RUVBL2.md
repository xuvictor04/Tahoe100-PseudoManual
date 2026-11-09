---
symbol: "RUVBL2"
type: "gene"
col: 11380
ensembl_id: "ENSG00000183207"
name: "RuvB like AAA ATPase 2"
location: "19q13.33"
module: 60
arm: "+"
pooled_cpm: 35.16
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# RUVBL2

*RuvB like AAA ATPase 2* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (23 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.67× (z +14.4, q 4e-44, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.0803×; ⚠ cell-cycle shift, explains ~69% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D22A]] (+0.59, fdr 8e-05), [[HSP90AA2P]] (+0.58, fdr 1e-05), [[HSP90AB3P]] (+0.57, fdr 3e-05); moves opposite to [[UBXN2A]] (-0.55, fdr 1e-04), [[SESN1]] (-0.55, fdr 1e-05), [[SPPL2A]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 23 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.67×** | +14.4 | 4e-44 | 47/48 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.91×** | +11.8 | 1e-29 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.57×** | +10.4 | 3e-23 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.51×** | +10.1 | 5e-22 | 43/48 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.29×** | +9.2 | 6e-18 | 36/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.07×** | +8.0 | 1e-13 | 44/48 (A498, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.05×** | +7.9 | 2e-13 | 42/47 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.74×** | +6.1 | 7e-08 | 37/47 (KATO III, AsPC-1, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.93×** | +6.1 | 7e-08 | 31/48 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +5.5 | 2e-06 | 31/48 (NCI-H1792, A549, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.65×** | +5.3 | 5e-06 | 28/40 (A498, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **1.63×** | +5.2 | 9e-06 | 32/47 (SHP-77, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.59×** | +5.1 | 1e-05 | 33/48 (KATO III, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +4.6 | 2e-04 | 33/47 (SW1417, A-172, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **1.49×** | +4.4 | 4e-04 | 30/46 (HOP62, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +3.5 | 0.014 | 23/48 (RKO, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.81×** | +3.4 | 0.016 | 27/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.34×** | +2.8 | 0.086 | 16/47 (HOP62, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.30×** | +2.8 | 0.095 | 13/48 (AsPC-1, SW1417, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11380.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.0803×; ⚠ cell-cycle shift, explains ~69% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.817× | -3.2 | 0.53 | 18/48 (HS-578T, PANC-1, …) | rises with dose | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | 0.588× | -3.1 | 0.53 | 20/48 (A-427, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.7 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.55× (z +11.2) | — |
| [[A498 (line)]] | wt | 43.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.51× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.90× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.19× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.97× (z +8.9) | — |
| [[RKO (line)]] | wt | 43.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.31× (z +10.3) | — |
| [[A-427 (line)]] | wt | 45.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.99× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0803× (z -19.1) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A549 (line)]] | wt | 38.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.94× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 24.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.76× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 54.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.51× (z +10.0) | — |
| [[KATO III (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 22.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 43.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 25.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.77× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 24.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.29× (z +8.5) | — |
| [[A-172 (line)]] | wt | 13.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.45× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 22.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.84× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 30.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.38× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.57× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 60.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.93× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 24.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 27.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.2× (z +15.7) | — |
| [[hTERT-HPNE (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 50.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +23.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.78× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 28.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.23× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 37.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.01× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D22A]] | +0.59 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[HSP90AA2P]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[HSP90AB3P]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PWWP3A]] | +0.57 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[HK1]] | +0.56 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[EIPR1]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[HMBS]] | +0.55 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[STIP1]] | +0.55 | +0.61 / +0.48 | both halves | 2e-05 | STRING 766 |
| [[ZNF473]] | +0.54 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[EPS15L1]] | +0.54 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[GYS1]] | +0.54 | +0.36 / +0.50 | both halves | 1e-04 | ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[POLR3H]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[NUDC]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 | STRING 550 |

## Genes that move opposite

*34 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN2A]] | -0.55 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[SESN1]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SPPL2A]] | -0.54 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[DRAM1]] | -0.51 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[ZMAT3]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[RXYLT1]] | -0.51 | -0.30 / -0.26 | both halves | 4e-04 |  |
| [[N4BP2L1]] | -0.50 | -0.37 / -0.24 | both halves | 4e-04 |  |
| [[RNF146]] | -0.49 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[LARP1B]] | -0.49 | -0.52 / -0.24 | both halves | 5e-04 |  |
| [[OGFRL1]] | -0.49 | -0.19 / -0.44 | ⚠ not reproduced | 8e-04 |  |
| [[ABCA10]] | -0.48 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[DNAI4]] | -0.48 | -0.35 / -0.26 | both halves | 4e-04 |  |
| [[PPM1D]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.9, -23.5); signed map (-27.3, -27.9). **Vector** length 78.8, 21.3% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.9 | +14.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.3 | +11.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.9 | +6.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.6 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +8.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.1 | +1.0 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.5 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -3.0 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -1.9 | +3.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.6 | -0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RuvB like AAA ATPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,993,562-49,015,970 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RVB2, TIP48, TIP49b, Reptin52, ECP51, TIH2, INO80J, Rvb2 |
| Gene groups (HGNC) | AAA ATPases; INO80 complex subunits; Helicases; SRCAP complex subunits; R2TP complex; Tip60/Nua4 histone acetyltransferase complex subunits |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; Telomere Maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y230](https://www.uniprot.org/uniprotkb/Q9Y230) (RuvB-like 2):

> Possesses single-stranded DNA-stimulated ATPase and ATP-dependent DNA helicase (5' to 3') activity; hexamerization is thought to be critical for ATP hydrolysis and adjacent subunits in the ring-like structure contribute to the ATPase activity. Component of the NuA4 histone acetyltransferase complex which is involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. This modification may both alter nucleosome -DNA interactions and …

**Summary**, from NCBI Gene [10856](https://www.ncbi.nlm.nih.gov/gene/10856):

> This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the LHB gene, in the opposite orientation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10475) · Entrez [10856](https://www.ncbi.nlm.nih.gov/gene/10856) · UniProt [Q9Y230](https://www.uniprot.org/uniprotkb/Q9Y230) · Ensembl [ENSG00000183207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183207)

## Data

Gene col 11380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11380); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11380]; `tensor/DDL_lfc|DDL_z.npy` [11380]; `embed/gene_vectors.npy` [11380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11380 or target_col == 11380). Every well: [[RUVBL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUVBL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
