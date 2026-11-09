---
symbol: "SEPHS2"
type: "gene"
col: 11065
ensembl_id: "ENSG00000179918"
name: "selenophosphate synthetase 2"
location: "16p11.2"
module: 7
arm: "+"
pooled_cpm: 23.31
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SEPHS2

*selenophosphate synthetase 2* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.11× (z +7.4, q 5e-11, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.407× (z -9.0, q 9e-17, down in 33 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.489× (z -7.2, q 2e-10, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF2S2]] (+0.62, fdr 1e-05), [[PPP1R3D]] (+0.61, fdr 7e-06), [[KDM4A]] (+0.60, fdr 9e-06); moves opposite to [[CPSF6]] (-0.54, fdr 4e-05), [[SKA2]] (-0.51, fdr 1e-04), [[DHFR]] (-0.51, fdr 0.001, ⚠ one half only (not replicated)), [[PRKACA]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CHAC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +7.4 | 5e-11 | 41/47 (A498, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +7.4 | 5e-11 | 38/48 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.2 | 9e-08 | 29/47 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.86×** | +6.2 | 9e-08 | 34/48 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +5.8 | 8e-07 | 32/44 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.3 | 9e-06 | 9/48 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.7 | 2e-04 | 30/48 (HEC-1-A, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +4.4 | 6e-04 | 27/48 (A-172, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.48×** | +3.9 | 0.006 | 24/47 (CFPAC-1, A549, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.012 | 22/47 (A-427, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.012 | 19/47 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.012 | 22/48 (CFPAC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.029 | 17/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.36×** | +3.0 | 0.092 | 17/47 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.0 | 0.092 | 16/47 (NCI-H1573, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11065.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.407×** | -9.0 | 9e-17 | 33/46 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -7.2 | 2e-10 | 35/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -7.1 | 2e-10 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -6.0 | 3e-07 | 31/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.386×** | -5.0 | 6e-05 | 15/24 (HT-29, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.617×** | -4.9 | 1e-04 | 28/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.663×** | -4.2 | 0.003 | 21/41 (Panc 03.27, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.004 | 22/47 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.689×** | -3.8 | 0.011 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tadalafil (drug)]] 5 µM |  | **0.688×** | -3.6 | 0.016 | 22/47 (NCI-H2030, Panc 03.27, …) | top dose only | position effect removed |
| [[Baicalin (drug)]] 5 µM |  | **0.787×** | -3.4 | 0.029 | 18/48 (Hs 766T, RKO, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0823× (z -16.0) |
| [[PANC-1 (line)]] | alt | 36.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -16.4) |
| [[A-427 (line)]] | wt | 59.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.6) |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0666× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.266× (z -9.1) |
| [[KATO III (line)]] | alt | 90.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.245× (z -11.0) |
| [[LS 180 (line)]] | wt | 22.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 23.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.36× (z +9.8) | — |
| [[A549 (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.100× (z -8.7) |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0917× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 48.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -10.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -14.1) |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2S2]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PPP1R3D]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[KDM4A]] | +0.60 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[RDH14]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GCC1]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SESN2]] | +0.59 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[DDIT3]] | +0.59 | +0.38 / +0.67 | both halves | 6e-05 |  |
| [[SART3]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MIEF1]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[XBP1]] | +0.58 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[TRIB3]] | +0.58 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[LSM10]] | +0.57 | +0.40 / +0.65 | both halves | 5e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF6]] | -0.54 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[SKA2]] | -0.51 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[DHFR]] | -0.51 | -0.16 / -0.66 | ⚠ one half (not replicated) | 0.001 |  |
| [[PRKACA]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ARL6IP6]] | -0.50 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[EIF4EBP2]] | -0.50 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[LMNB2]] | -0.49 | -0.22 / -0.54 | both halves | 6e-04 |  |
| [[LENG8]] | -0.48 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[FAM81A]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHAC1]] | B | CHAC1 activity raises SEPHS2's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without CHAC1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-46.3, -5.3); signed map (-8.7, -9.3). **Vector** length 101, 26.7% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.6 | +7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.4 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +1.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -10.1 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -10.0 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.0 | -2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -9.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.6 | -5.0 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -1.4 | -0.5 |
|  | [[Pentagastrin (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | selenophosphate synthetase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,443,631-30,445,874 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPS2, SPS2b |
| Gene groups (HGNC) | Selenoproteins |
| Reactome | 3 pathways, smallest: Selenocysteine synthesis; Selenoamino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99611](https://www.uniprot.org/uniprotkb/Q99611) (Selenide, water dikinase 2):

> Selenophosphate synthase that generates the selenium donor for selenocysteine biosynthesis by catalyzing formation of selenophosphate from selenide and ATP.

**Summary**, from NCBI Gene [22928](https://www.ncbi.nlm.nih.gov/gene/22928):

> This gene encodes an enzyme that catalyzes the production of monoselenophosphate (MSP) from selenide and ATP. MSP is the selenium donor required for synthesis of selenocysteine (Sec), which is co-translationally incorporated into selenoproteins at in-frame UGA codons that normally signal translation termination. The 3' UTRs of selenoprotein mRNAs contain a conserved stem-loop structure, the Sec insertion sequence (SECIS) element, which is necessary for the recognition of UGA as a Sec codon …

**Accessions** — [HGNC:19686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19686) · Entrez [22928](https://www.ncbi.nlm.nih.gov/gene/22928) · UniProt [Q99611](https://www.uniprot.org/uniprotkb/Q99611) · Ensembl [ENSG00000179918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179918)

## Data

Gene col 11065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11065); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11065]; `tensor/DDL_lfc|DDL_z.npy` [11065]; `embed/gene_vectors.npy` [11065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11065 or target_col == 11065). Every well: [[SEPHS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPHS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
