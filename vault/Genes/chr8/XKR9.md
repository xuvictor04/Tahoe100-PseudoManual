---
symbol: "XKR9"
type: "gene"
col: 13321
ensembl_id: "ENSG00000221947"
name: "XK related 9"
location: "8q13.3"
module: 117
arm: "+"
pooled_cpm: 12.17
n_lines_expressing: 38
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# XKR9

*XK related 9* — 8q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.49× (z +4.9, q 7e-04, up in 13 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.410× (z -11.4, q 4e-27, down in 23 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.775× (z -4.6, q 3e-04, down in 13 of 34 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM229B]] (+0.54, fdr 4e-05), [[ME1]] (+0.52, fdr 2e-05), [[SOHLH2]] (+0.51, fdr 5e-05); moves opposite to [[LIX1L]] (-0.46, fdr 4e-05), [[CDKL5]] (-0.45, fdr 9e-05), [[PIN1]] (-0.44, fdr 5e-04).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPAG17]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CDKL5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +4.9 | 7e-04 | 13/34 (CFPAC-1, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.005 | 10/35 (SNU-423, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.013 | 8/35 (KATO III, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.013 | 11/35 (A-172, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.6 | 0.028 | 1/13 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.028 | 10/34 (SW480, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.5 | 0.028 | 6/34 (LOX-IMVI, J82, …) | top dose only | low cells (technical?) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.028 | 6/36 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.028 | 7/34 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.028 | 3/34 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.046 | 9/34 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.410×** | -11.4 | 4e-27 | 23/33 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.443×** | -10.4 | 1e-22 | 26/35 (PANC-1, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.507×** | -8.3 | 2e-14 | 20/34 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.571×** | -7.1 | 1e-10 | 21/35 (PANC-1, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.635×** | -5.8 | 8e-07 | 15/29 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.738×** | -5.5 | 4e-06 | 18/33 (LoVo, A498, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.683×** | -4.9 | 9e-05 | 19/34 (PANC-1, C32, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.775×** | -4.6 | 3e-04 | 13/34 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.710×** | -4.4 | 8e-04 | 13/35 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.708×** | -4.2 | 0.001 | 17/28 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.738×** | -3.9 | 0.006 | 8/35 (NCI-H661, C32, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.782× | -3.0 | 0.13 | 4/36 (SW 900, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 45.3 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0374× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 20.0 | 0 | 7 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0984× (z -18.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 47.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 12.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 24.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0890× (z -11.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.164× (z -8.6) |
| [[J82 (line)]] | alt | 11.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 42.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0248× (z -22.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0866× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 9.73 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0629× (z -15.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 9.09 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0948× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 6.72 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0777× (z -10.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0553× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM229B]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[ME1]] | +0.52 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[SOHLH2]] | +0.51 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[RNLS]] | +0.50 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[PLEKHS1]] | +0.49 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[SLC7A11]] | +0.48 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[FRMD3]] | +0.47 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[ANKRD18CP]] | +0.46 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[SP2-AS1]] | +0.46 | +0.50 / +0.31 | both halves | 2e-04 |  |
| [[PREX2]] | +0.46 | +0.35 / +0.42 | both halves | 1e-04 |  |
| [[TRIM16L]] | +0.46 | +0.39 / +0.37 | both halves | 8e-05 |  |
| [[ITGA9]] | +0.45 | +0.38 / +0.43 | both halves | 6e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIX1L]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CDKL5]] | -0.45 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[PIN1]] | -0.44 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[ACTR1B]] | -0.43 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[TOM1L2]] | -0.41 | -0.29 / -0.35 | both halves | 3e-04 |  |
| [[DEPDC7]] | -0.41 | -0.36 / -0.26 | both halves | 4e-04 |  |
| [[ICAM5]] | -0.41 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[HABP4]] | -0.40 | -0.29 / -0.32 | both halves | 3e-04 |  |
| [[SMTN]] | -0.40 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[B3GAT3]] | -0.40 | -0.36 / -0.18 | ⚠ not reproduced | 1e-03 |  |
| [[ITSN1]] | -0.40 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[MRNIP]] | -0.40 | -0.23 / -0.34 | both halves | 5e-04 |  |
| [[EFHC1]] | -0.39 | -0.32 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPAG17]] | B | SPAG17 activity lowers XKR9's level | lines that do not express SPAG17 (6) vs lines expressing it (44) | 2.23× higher at baseline in the lines without SPAG17 | 0.074 | ⚠ within organs, on part of the lines; also absent: NKAIN1, CEP85L, EMP3; maybe low, not absent |
| [[VEGFD]] | B | VEGFD activity raises XKR9's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without VEGFD | 0.091 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKL5]] | B | XKR9 activity raises CDKL5's level | lines that do not express XKR9 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without XKR9 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000285579; maybe low, not absent |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.8, 49.7); signed map (50.1, -11.1). **Vector** length 53.2, 8.50% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.1 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -1.5 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.4 | -8.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.4 | -7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.2 | -10.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -3.9 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | XK related 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.3 — chr8:70,669,339-70,790,371 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | XK related family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5GH70](https://www.uniprot.org/uniprotkb/Q5GH70) (XK-related protein 9):

> [XK-related protein 9, processed form]: Phospholipid scramblase that promotes phosphatidylserine exposure on apoptotic cell surface. Phosphatidylserine is a specific marker only present at the surface of apoptotic cells and acts as a specific signal for engulfment.

**Summary**, from NCBI Gene [389668](https://www.ncbi.nlm.nih.gov/gene/389668):

> Enables phospholipid scramblase activity. Involved in phosphatidylserine exposure on apoptotic cell surface. Predicted to be located in plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20937) · Entrez [389668](https://www.ncbi.nlm.nih.gov/gene/389668) · UniProt [Q5GH70](https://www.uniprot.org/uniprotkb/Q5GH70) · Ensembl [ENSG00000221947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221947)

## Data

Gene col 13321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13321); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13321]; `tensor/DDL_lfc|DDL_z.npy` [13321]; `embed/gene_vectors.npy` [13321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13321 or target_col == 13321). Every well: [[XKR9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XKR9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
