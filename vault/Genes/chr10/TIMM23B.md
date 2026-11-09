---
symbol: "TIMM23B"
type: "gene"
col: 12821
ensembl_id: "ENSG00000204152"
name: "translocase of inner mitochondrial membrane 23 homolog B"
location: "10q11.23"
module: 36
arm: "+"
pooled_cpm: 40.33
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TIMM23B

*translocase of inner mitochondrial membrane 23 homolog B* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.18× (z +13.4, q 5e-38, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.767× (z -11.4, q 4e-27, down in 46 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.746× (z -5.1, q 1e-04, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 6 lines (NCI-H23 0.635×, MIA PaCa-2 0.654×, LoVo 0.714×, SW480 0.781×, …; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.104×, SNU-1 0.146×, NCI-H23 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.207×, HCT15 0.197×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.0884×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM23]] (+0.83, fdr 7e-06), [[TIMM23B-AGAP6]] (+0.69, fdr 7e-06, ⚠ read-through risk), [[B4GALT2]] (+0.67, fdr 7e-06), [[ARIH2]] (+0.63, fdr 1e-05); moves opposite to [[SDCBP]] (-0.67, fdr 7e-06), [[TENT5C]] (-0.58, fdr 1e-05), [[TOB1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.18×** | +13.4 | 5e-38 | 48/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.68×** | +12.0 | 1e-30 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **5.69×** | +11.1 | 4e-26 | 43/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +10.5 | 1e-23 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.07×** | +8.8 | 1e-16 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.06×** | +8.1 | 6e-14 | 37/45 (NCI-H1792, AsPC-1, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +7.8 | 7e-13 | 39/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +7.6 | 2e-12 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +7.2 | 4e-11 | 35/47 (BT-474, COLO 205, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +6.6 | 3e-09 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.69×** | +6.4 | 1e-08 | 31/48 (LS 180, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.66×** | +6.1 | 4e-08 | 38/48 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.64×** | +6.0 | 8e-08 | 36/48 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.9 | 1e-07 | 30/48 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.45×** | +5.7 | 5e-07 | 25/34 (NCI-H1573, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +5.5 | 1e-06 | 29/48 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +5.4 | 2e-06 | 32/48 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +4.7 | 7e-05 | 32/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.58×** | +4.0 | 0.002 | 24/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.78×** | +3.7 | 0.006 | 22/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.013 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.017 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12821.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 6 lines (NCI-H23 0.635×, MIA PaCa-2 0.654×, LoVo 0.714×, SW480 0.781×, …; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.104×, SNU-1 0.146×, NCI-H23 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.207×, HCT15 0.197×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.0884×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.767×** | -11.4 | 4e-27 | 46/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.746×** | -5.1 | 1e-04 | 30/48 (KATO III, SNU-1, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.734×** | -3.7 | 0.042 | 25/48 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.758×** | -3.4 | 0.092 | 22/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 64.6 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +14.8) | — |
| [[PANC-1 (line)]] | alt | 50.6 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 39.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 44.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 46.5 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.14× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +9.6) | — |
| [[LoVo (line)]] | wt | 42.8 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.2× (z +10.4) | [[Adagrasib (drug)]] 0.05 µM 0.654× (z -11.1) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 28.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.93× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 27.7 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.56× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +8.5) | — |
| [[A-427 (line)]] | wt | 46.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 35.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 33.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 45.3 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 8.37× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 32.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.79× (z +8.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +8.5) | — |
| [[KATO III (line)]] | alt | 24.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 16.6× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 80.1 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.15× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +11.5) | — |
| [[CHP-212 (line)]] | wt | 44.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0884× (z -9.7) |
| [[HOP62 (line)]] | alt | 26.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 28.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.8× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0518× (z -8.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23]] | +0.83 | +0.78 / +0.86 | both halves | 7e-06 | same gene group; STRING 545 |
| [[TIMM23B-AGAP6]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 | ⚠ **readthrough risk**: TIMM23B-AGAP6 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[B4GALT2]] | +0.67 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ARIH2]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SRM]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NOL10]] | +0.63 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[NUP42]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[XPO4]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ATAD3B]] | +0.60 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TYW1]] | +0.60 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SENP3]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[EIF3B]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PGS1]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.67 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[TENT5C]] | -0.58 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[TOB1]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[MYLIP]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[BTG1]] | -0.56 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[MEX3B]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[C21orf91]] | -0.53 | -0.40 / -0.63 | both halves | 4e-05 |  |
| [[SFR1]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RYBP]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ZNF217]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-4.9, -29.1); signed map (-45.7, -19.2). **Vector** length 81.2, 21.7% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.8 | +8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +13.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +11.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.3 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | +3.3 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.3 | +0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.7 | -3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -2.7 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 23 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:49,942,049-49,974,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA592B15.7 |
| Gene groups (HGNC) | TIM23 complex; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SRD1](https://www.uniprot.org/uniprotkb/Q5SRD1) (Mitochondrial import inner membrane translocase subunit Tim23B):

> May participate in the translocation of transit peptide-containing proteins across the mitochondrial inner membrane. the PAM complex (By similarity).

**Summary**, from NCBI Gene [100652748](https://www.ncbi.nlm.nih.gov/gene/100652748):

> Predicted to enable transmembrane protein transporter activity. Predicted to be involved in protein import into mitochondrial matrix. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23581) · Entrez [100652748](https://www.ncbi.nlm.nih.gov/gene/100652748) · UniProt [Q5SRD1](https://www.uniprot.org/uniprotkb/Q5SRD1) · Ensembl [ENSG00000204152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204152)

## Data

Gene col 12821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12821); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12821]; `tensor/DDL_lfc|DDL_z.npy` [12821]; `embed/gene_vectors.npy` [12821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12821 or target_col == 12821). Every well: [[TIMM23B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM23B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
