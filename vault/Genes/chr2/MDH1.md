---
symbol: "MDH1"
type: "gene"
col: 287
ensembl_id: "ENSG00000014641"
name: "malate dehydrogenase 1"
location: "2p15"
module: 25
arm: "+"
pooled_cpm: 39.91
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MDH1

*malate dehydrogenase 1* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +16.4, q 0e+00, up in 44 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.59× (z +6.8, q 6e-10, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.711× (z -5.0, q 3e-04, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM106C]] (+0.65, fdr 1e-05), [[CAND1]] (+0.65, fdr 7e-06), [[PGM2]] (+0.64, fdr 7e-06); moves opposite to [[EXD3]] (-0.64, fdr 7e-06), [[KCNJ14]] (-0.63, fdr 1e-05), [[FBXO10]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.05×** | +16.4 | 0e+00 | 44/46 (A549, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.40×** | +12.4 | 8e-33 | 38/39 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.91×** | +8.8 | 2e-16 | 35/42 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.82×** | +8.8 | 2e-16 | 41/48 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.77×** | +8.4 | 6e-15 | 41/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.71×** | +7.9 | 3e-13 | 38/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.60×** | +6.9 | 3e-10 | 41/48 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +6.9 | 3e-10 | 31/48 (A549, NCI-H2347, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +6.8 | 6e-10 | 41/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.45×** | +5.5 | 3e-06 | 28/47 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.44×** | +5.2 | 1e-05 | 32/48 (A-172, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 23/48 (A-172, A549, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +3.8 | 0.006 | 22/47 (C32, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.29×** | +3.6 | 0.011 | 18/48 (A-172, NCI-H23, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~87% of this change | **1.28×** | +3.5 | 0.016 | 21/47 (SNU-423, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.038 | 18/48 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.042 | 15/48 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.088 | 11/48 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.088 | 14/48 (HT-29, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 287.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.711×** | -5.0 | 3e-04 | 28/48 (SNU-423, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.718×** | -4.9 | 3e-04 | 31/48 (SW1417, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.768×** | -3.9 | 0.020 | 26/48 (HepG2/C3A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 37.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LOX-IMVI (line)]] | wt | 35.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 40.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A498 (line)]] | wt | 55.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A549 (line)]] | wt | 43.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HOP62 (line)]] | alt | 32.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[KATO III (line)]] | alt | 44.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1792 (line)]] | alt | 52.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 65.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H460 (line)]] | wt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[PANC-1 (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 41.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SNU-423 (line)]] | alt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[COLO 205 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HCT15 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[Hs 766T (line)]] | wt | 26.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HS-578T (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HT-29 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LoVo (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LS 180 (line)]] | wt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[Panc 03.27 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-427 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM106C]] | +0.65 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CAND1]] | +0.65 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[PGM2]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[ZMYM3]] | +0.64 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[COPS6]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[IARS2]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[LANCL1]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SCOC]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[EIF2AK1]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SCARB2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[COX11]] | +0.60 | +0.59 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[RBL2]] | +0.59 | +0.45 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXD3]] | -0.64 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[KCNJ14]] | -0.63 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FBXO10]] | -0.61 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CDR2]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[MAFG]] | -0.58 | -0.40 / -0.60 | both halves | 4e-05 |  |
| [[EIF3J]] | -0.58 | -0.40 / -0.59 | both halves | 4e-05 |  |
| [[ZKSCAN2-DT]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[UBE2CP5]] | -0.57 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[PLEKHN1]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[NUTM2A-AS1]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[C19orf18]] | -0.56 | -0.21 / -0.66 | both halves | 7e-04 |  |
| [[CLCF1]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MDH1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GGH]] | B | GGH activity raises MDH1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without GGH | 0.054 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[CYB5A]] | B | CYB5A activity raises MDH1's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.14× lower at baseline in the lines without CYB5A | 0.071 | ⚠ within organs, on part of the lines; also absent: FGF11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.4, -17.7); signed map (-19.6, -41.4). **Vector** length 80.8, 20.0% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.4 | +3.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.8 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | +2.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -0.2 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | malate dehydrogenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:63,588,609-63,607,197 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Malate dehydrogenases |
| Hallmark sets | FATTY_ACID_METABOLISM, GLYCOLYSIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Malate-aspartate shuttle; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P40925](https://www.uniprot.org/uniprotkb/P40925) (Malate dehydrogenase, cytoplasmic):

> Catalyzes the reduction of aromatic alpha-keto acids in the presence of NADH. Plays essential roles in the malate-aspartate shuttle and the tricarboxylic acid cycle, important in mitochondrial NADH supply for oxidative phosphorylation. Catalyzes the reduction of 2-oxoglutarate to 2-hydroxyglutarate, leading to elevated reactive oxygen species (ROS).

**Summary**, from NCBI Gene [4190](https://www.ncbi.nlm.nih.gov/gene/4190):

> This gene encodes an enzyme that catalyzes the NAD/NADH-dependent, reversible oxidation of malate to oxaloacetate in many metabolic pathways, including the citric acid cycle. Two main isozymes are known to exist in eukaryotic cells: one is found in the mitochondrial matrix and the other in the cytoplasm. This gene encodes the cytosolic isozyme, which plays a key role in the malate-aspartate shuttle that allows malate to pass through the mitochondrial membrane to be transformed into oxaloacetate …

**Accessions** — [HGNC:6970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6970) · Entrez [4190](https://www.ncbi.nlm.nih.gov/gene/4190) · UniProt [P40925](https://www.uniprot.org/uniprotkb/P40925) · Ensembl [ENSG00000014641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000014641)

## Data

Gene col 287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 287); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 287]; `tensor/DDL_lfc|DDL_z.npy` [287]; `embed/gene_vectors.npy` [287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 287 or target_col == 287). Every well: [[MDH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
