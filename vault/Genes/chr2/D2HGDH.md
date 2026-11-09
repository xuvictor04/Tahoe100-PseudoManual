---
symbol: "D2HGDH"
type: "gene"
col: 11146
ensembl_id: "ENSG00000180902"
name: "D-2-hydroxyglutarate dehydrogenase"
location: "2q37.3"
module: 10
arm: "+"
pooled_cpm: 14.95
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# D2HGDH

*D-2-hydroxyglutarate dehydrogenase* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.36× (z +3.8, q 0.031, up in 14 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.388× (z -16.6, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.280× (z -15.8, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TKFC]] (+0.61, fdr 1e-05), [[ADAMTS13]] (+0.57, fdr 4e-05), [[SLC2A11]] (+0.54, fdr 2e-05); moves opposite to [[RHOC]] (-0.46, fdr 4e-05), [[ARPC5]] (-0.45, fdr 5e-05), [[DYNLRB1]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.031 | 14/46 (KATO III, C-33 A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.031 | 14/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.031 | 11/47 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.031 | 14/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.032 | 14/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.059 | 12/46 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.085 | 14/47 (HOP62, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.388×** | -16.6 | 0e+00 | 39/47 (MIA PaCa-2, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.280×** | -15.8 | 0e+00 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.299×** | -15.0 | 0e+00 | 40/45 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.346×** | -13.1 | 3e-37 | 44/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.358×** | -12.7 | 5e-35 | 43/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.393×** | -11.6 | 6e-29 | 37/45 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.451×** | -9.9 | 6e-21 | 38/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.490×** | -8.8 | 8e-17 | 36/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.483×** | -8.6 | 3e-16 | 36/47 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.275×** | -8.4 | 3e-15 | 38/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.292×** | -8.0 | 8e-14 | 30/44 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.552×** | -6.9 | 2e-10 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.558×** | -6.8 | 5e-10 | 29/47 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.588×** | -6.5 | 2e-09 | 27/46 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.579×** | -6.5 | 3e-09 | 25/43 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.598×** | -6.0 | 7e-08 | 26/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -5.3 | 4e-06 | 25/46 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.796×** | -4.0 | 0.002 | 20/47 (COLO 205, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.759×** | -3.4 | 0.021 | 11/48 (SNU-423, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.5 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -19.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -18.1) |
| [[LoVo (line)]] | wt | 18.0 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -22.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0629× (z -18.4) |
| [[SW480 (line)]] | alt | 13.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.1000× (z -13.5) |
| [[HT-29 (line)]] | alt | 17.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.205× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -12.6) |
| [[A-427 (line)]] | wt | 19.7 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.192× (z -10.5) |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 3 (2 ⚠) | — | [[Bendamustine (drug)]] 5 µM 0.0753× (z -11.1) |
| [[H4 (line)]] | wt | 18.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0750× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -9.1) |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0727× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.106× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 17.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 16.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -8.9) |
| [[A-172 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -12.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -12.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0437× (z -15.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -10.2) |
| [[HS-578T (line)]] | alt | 7.36 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0555× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0633× (z -11.1) |
| [[KATO III (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0503× (z -14.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 9.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -9.5) |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TKFC]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ADAMTS13]] | +0.57 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[SLC2A11]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PGAP3]] | +0.51 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[CDK10]] | +0.51 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[PGAP2]] | +0.51 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[TRIM66]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PCYOX1L]] | +0.49 | +0.54 / +0.43 | both halves | 4e-05 | same gene group |
| [[B4GAT1-DT]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[IDUA]] | +0.48 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[C1QTNF6]] | +0.47 | +0.61 / +0.33 | both halves | 1e-04 |  |
| [[WDR31]] | +0.47 | +0.48 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOC]] | -0.46 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ARPC5]] | -0.45 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[DYNLRB1]] | -0.43 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[EMC4]] | -0.41 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[CLIC1]] | -0.40 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[RP2]] | -0.39 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[MRPL13]] | -0.39 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[PSMD10]] | -0.38 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[TMOD3]] | -0.38 | -0.24 / -0.51 | both halves | 4e-04 |  |
| [[ZNF106]] | -0.37 | -0.26 / -0.31 | both halves | 4e-04 |  |
| [[DSG2]] | -0.37 | -0.31 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity strengthens D2HGDH's drug response | lines that do not express ZNF594-DT (7) vs lines expressing it (41) | the lines without ZNF594-DT respond 0.59× as strongly (z diff +2.45); strongest at Digitoxin 5 µM: 0.66x vs 0.24x (z diff +4.6) | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1; target measured in part of the lines; artifact flags |
| [[RDM1P5]] | B | RDM1P5 activity strengthens D2HGDH's drug response | lines that do not express RDM1P5 (7) vs lines expressing it (41) | the lines without RDM1P5 respond 0.49× as strongly (z diff +2.63); strongest at Homoharringtonine 5 µM: 0.72x vs 0.35x (z diff +4.7) | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RDM1P5]] | B | RDM1P5 activity raises D2HGDH's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without RDM1P5 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers D2HGDH's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ZNF594-DT]] | B | ZNF594-DT activity raises D2HGDH's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.52× lower at baseline in the lines without ZNF594-DT | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.201). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-29.1, 23.9); signed map (18.2, -43.0). **Vector** length 52.0, 8.27% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.4 | -16.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | D-2-hydroxyglutarate dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,734,602-241,768,816 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC25181, D2HGD, FLJ42195 |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Interconversion of 2-oxoglutarate and 2-hydroxyglutarate; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N465](https://www.uniprot.org/uniprotkb/Q8N465) (D-2-hydroxyglutarate dehydrogenase, mitochondrial):

> Catalyzes the oxidation of D-2-hydroxyglutarate (D-2-HG) to alpha-ketoglutarate. Also catalyzes the oxidation of other D-2-hydroxyacids, such as D-malate (D-MAL) and D-lactate (D-LAC). Exhibits high activities towards D-2-HG and D-MAL but a very weak activity towards D-LAC.

**Summary**, from NCBI Gene [728294](https://www.ncbi.nlm.nih.gov/gene/728294):

> This gene encodes D-2hydroxyglutarate dehydrogenase, a mitochondrial enzyme belonging to the FAD-binding oxidoreductase/transferase type 4 family. This enzyme, which is most active in liver and kidney but also active in heart and brain, converts D-2-hydroxyglutarate to 2-ketoglutarate. Mutations in this gene are present in D-2-hydroxyglutaric aciduria, a rare recessive neurometabolic disorder causing developmental delay, epilepsy, hypotonia, and dysmorphic features. [provided by RefSeq, Jul …

**Accessions** — [HGNC:28358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28358) · Entrez [728294](https://www.ncbi.nlm.nih.gov/gene/728294) · UniProt [Q8N465](https://www.uniprot.org/uniprotkb/Q8N465) · Ensembl [ENSG00000180902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180902)

## Data

Gene col 11146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11146); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11146]; `tensor/DDL_lfc|DDL_z.npy` [11146]; `embed/gene_vectors.npy` [11146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11146 or target_col == 11146). Every well: [[D2HGDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/D2HGDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
