---
symbol: "MTA1"
type: "gene"
col: 11351
ensembl_id: "ENSG00000182979"
name: "metastasis associated 1"
location: "14q32.33"
module: 18
arm: "+"
pooled_cpm: 41.36
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MTA1

*metastasis associated 1* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +15.8, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 2.59×, NCI-H460 2.29×, NCI-H1792 3.30×, LoVo 2.31×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 3.84×, SW480 2.39×, CFPAC-1 2.44×, HT-29 2.89×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 2.34×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.565× (z -13.0, q 5e-36, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAZAP1]] (+0.76, fdr 7e-06), [[CTBP1]] (+0.71, fdr 1e-05), [[CPNE7]] (+0.69, fdr 7e-06); moves opposite to [[NDUFA7]] (-0.65, fdr 1e-05), [[IFI27L2]] (-0.62, fdr 2e-05), [[LGALS1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11351.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 2.59×, NCI-H460 2.29×, NCI-H1792 3.30×, LoVo 2.31×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 3.84×, SW480 2.39×, CFPAC-1 2.44×, HT-29 2.89×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 2.34×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +15.8 | 0e+00 | 44/45 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +12.4 | 5e-33 | 36/41 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +11.5 | 2e-28 | 34/44 (NCI-H2347, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +6.1 | 2e-07 | 26/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +4.6 | 4e-04 | 15/48 (CFPAC-1, J82, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.005 | 18/46 (HS-578T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.9 | 0.010 | 18/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.3 | 0.060 | 5/48 (A498, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.565×** | -13.0 | 5e-36 | 42/48 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.603×** | -11.5 | 2e-28 | 41/48 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.607×** | -11.4 | 8e-28 | 37/48 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -11.1 | 2e-26 | 35/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.800×** | -7.2 | 6e-11 | 25/48 (RKO, AN3 CA, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.758×** | -6.3 | 2e-08 | 25/48 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.751×** | -6.3 | 3e-08 | 29/48 (NCI-H23, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.772×** | -5.9 | 3e-07 | 23/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.785×** | -5.5 | 2e-06 | 25/47 (SNU-1, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -5.2 | 1e-05 | 19/48 (RKO, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.801×** | -5.1 | 2e-05 | 24/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.687×** | -4.5 | 3e-04 | 19/49 (SNU-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -4.2 | 0.001 | 17/48 (HCT15, CHP-212, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.848× | -3.8 | 0.007 | 18/48 (SNU-1, PANC-1, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.960× | -3.3 | 0.043 | 0/48 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 74.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.408× (z -10.3) |
| [[SW480 (line)]] | alt | 54.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +13.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.479× (z -10.1) |
| [[LoVo (line)]] | wt | 48.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +15.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.499× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 47.9 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.387× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.406× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 37.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.34× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 47.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.2) |
| [[HT-29 (line)]] | alt | 33.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 40.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.512× (z -8.9) |
| [[RKO (line)]] | wt | 43.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.360× (z -9.2) |
| [[SW48 (line)]] | wt | 106 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -10.4) |
| [[A-427 (line)]] | wt | 66.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.37× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 48.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -8.8) |
| [[AN3 CA (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 81.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 35.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 45.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 1271 (line)]] | alt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0550× (z -9.6) |
| [[A-172 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAZAP1]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[CTBP1]] | +0.71 | +0.50 / +0.73 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[CPNE7]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[GTPBP6]] | +0.67 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[SCRIB]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[U2AF2]] | +0.66 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[BRD9]] | +0.65 | +0.48 / +0.72 | both halves | 2e-05 | pathway: ATP-dependent chromatin remodelers |
| [[AGPAT3]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[GNL3L]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.63 | +0.49 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA7]] | -0.65 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[IFI27L2]] | -0.62 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[LGALS1]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.59 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[BTG1]] | -0.57 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[TCEAL8]] | -0.57 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[ING2]] | -0.56 | -0.34 / -0.58 | both halves | 1e-04 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[RNF181]] | -0.56 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[OCEL1]] | -0.55 | -0.28 / -0.59 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.560). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-17.2, -26.2); signed map (-12.3, -33.9). **Vector** length 92.8, 20.2% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +15.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +11.5 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.2 | +4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -11.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.6 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | metastasis associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,419,820-105,470,729 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | GATA zinc finger domain containing; Myb/SANT domain containing; NuRD complex subunits |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 31 pathways, smallest: SUMOylation of transcription factors; Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13330](https://www.uniprot.org/uniprotkb/Q13330) (Metastasis-associated protein MTA1):

> Transcriptional coregulator which can act as both a transcriptional corepressor and coactivator. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. In the NuRD complex, regulates transcription of its targets by modifying the acetylation status of the target chromatin and cofactor accessibility to the target DNA. In conjunction with other components of NuRD, acts as a transcriptional corepressor of BRCA1, ESR1, TFF1 and CDKN1A. Acts as …

**Summary**, from NCBI Gene [9112](https://www.ncbi.nlm.nih.gov/gene/9112):

> This gene encodes a protein that was identified in a screen for genes expressed in metastatic cells, specifically, mammary adenocarcinoma cell lines. Expression of this gene has been correlated with the metastatic potential of at least two types of carcinomas although it is also expressed in many normal tissues. The role it plays in metastasis is unclear. It was initially thought to be the 70kD component of a nucleosome remodeling deacetylase complex, NuRD, but it is more likely that this …

**Accessions** — [HGNC:7410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7410) · Entrez [9112](https://www.ncbi.nlm.nih.gov/gene/9112) · UniProt [Q13330](https://www.uniprot.org/uniprotkb/Q13330) · Ensembl [ENSG00000182979](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182979)

## Data

Gene col 11351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11351); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11351]; `tensor/DDL_lfc|DDL_z.npy` [11351]; `embed/gene_vectors.npy` [11351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11351 or target_col == 11351). Every well: [[MTA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
