---
symbol: "HHAT"
type: "gene"
col: 609
ensembl_id: "ENSG00000054392"
name: "hedgehog acyltransferase"
location: "1q32.2"
module: 68
arm: "+"
pooled_cpm: 26.42
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 34
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# HHAT

*hedgehog acyltransferase* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +5.2, q 1e-04, up in 23 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.270× (z -14.6, q 3e-45, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM227B]] (+0.67, fdr 1e-05), [[ZMAT1]] (+0.63, fdr 2e-05), [[WAKMAR2]] (+0.61, fdr 4e-05); moves opposite to [[LRRC42]] (-0.58, fdr 8e-05), [[PHKA2]] (-0.56, fdr 7e-05), [[ANKRD27]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ZMAT1]] → it (grade B ⚠); 4 go from it, the strongest it → [[CLEC2D]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.2 | 1e-04 | 23/44 (SW480, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.041 | 21/44 (LoVo, LS 180, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.044 | 14/44 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.38×** | +3.6 | 0.044 | 12/44 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.096 | 19/44 (A-427, A-172, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.34× | +3.1 | 0.17 | 16/43 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.32× | +3.1 | 0.17 | 11/43 (PANC-1, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.270×** | -14.6 | 3e-45 | 39/44 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.368×** | -11.1 | 3e-26 | 37/43 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.375×** | -10.9 | 2e-25 | 38/43 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.399×** | -10.2 | 3e-22 | 38/43 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.401×** | -10.2 | 4e-22 | 32/42 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.406×** | -10.0 | 1e-21 | 34/43 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.449×** | -8.9 | 4e-17 | 35/44 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.467×** | -8.5 | 2e-15 | 35/44 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.475×** | -8.3 | 7e-15 | 33/43 (COLO 205, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.488×** | -8.0 | 9e-14 | 32/44 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.507×** | -7.3 | 2e-11 | 24/43 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.540×** | -6.5 | 5e-09 | 28/44 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.572×** | -6.0 | 1e-07 | 26/44 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.601×** | -5.7 | 6e-07 | 24/43 (NCI-H23, SNU-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.395×** | -5.4 | 3e-06 | 24/44 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.456×** | -4.6 | 1e-04 | 23/41 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.769×** | -4.1 | 0.001 | 22/44 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.493×** | -4.1 | 0.001 | 22/44 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.703×** | -3.9 | 0.002 | 20/43 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.629×** | -3.7 | 0.005 | 15/44 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 55.4 | 0 | 16 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0638× (z -20.5) |
| [[NCI-H460 (line)]] | wt | 54.0 | 0 | 14 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 66.9 | 0 | 11 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0684× (z -10.7) |
| [[A-427 (line)]] | wt | 93.4 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -11.9) |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -14.0) |
| [[A549 (line)]] | wt | 38.1 | 0 | 8 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.112× (z -11.9) |
| [[H4 (line)]] | wt | 32.4 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0337× (z -16.8) |
| [[SNU-1 (line)]] | wt | 35.3 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0742× (z -13.3) |
| [[C-33 A (line)]] | alt | 41.1 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0724× (z -14.4) |
| [[A-172 (line)]] | wt | 22.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 2.91× (z +8.5) | — |
| [[A498 (line)]] | wt | 17.4 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.91× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 31.3 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.277× (z -9.2) |
| [[LoVo (line)]] | wt | 12.5 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.161× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 31.8 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -12.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.219× (z -9.4) |
| [[SNU-423 (line)]] | alt | 44.0 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.231× (z -10.2) |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.245× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.121× (z -9.3) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.138× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 37.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.240× (z -9.0) |
| [[C32 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 54.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0948× (z -9.1) |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0718× (z -10.8) |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -14.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -8.6) |
| [[SW480 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -9.0) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM227B]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ZMAT1]] | +0.63 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[WAKMAR2]] | +0.61 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[MIR1915HG]] | +0.61 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[LACC1]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[C1QTNF1-AS1]] | +0.59 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[APLF]] | +0.58 | +0.65 / +0.34 | both halves | 1e-04 |  |
| [[ACTA2]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[EYS]] | +0.58 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[EIF1B-AS1]] | +0.58 | +0.65 / +0.27 | both halves | 3e-04 |  |
| [[F8]] | +0.57 | +0.61 / +0.30 | both halves | 2e-04 |  |
| [[COL28A1]] | +0.57 | +0.62 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC42]] | -0.58 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[PHKA2]] | -0.56 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[ANKRD27]] | -0.53 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[LPCAT4]] | -0.51 | -0.59 / -0.20 | both halves | 7e-04 |  |
| [[TSEN54]] | -0.51 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[SLC35A3]] | -0.50 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[IMPDH1]] | -0.50 | -0.55 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMAT1]] | B | ZMAT1 activity raises HHAT's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.90× lower at baseline in the lines without ZMAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[AGA-DT]] | B | AGA-DT activity raises HHAT's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.69× lower at baseline in the lines without AGA-DT | 0.048 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[BASP1-AS1]] | B | BASP1-AS1 activity raises HHAT's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.07× lower at baseline in the lines without BASP1-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[NTN1]] | B | NTN1 activity raises HHAT's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without NTN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[DRAM1]] | B | DRAM1 activity raises HHAT's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.62× lower at baseline in the lines without DRAM1 | 0.072 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[NBEAP1]] | B | NBEAP1 activity lowers HHAT's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.10× higher at baseline in the lines without NBEAP1 | 0.096 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B |
| [[FRG1-DT]] | C | FRG1-DT activity raises HHAT's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 3.40× lower at baseline in the lines without FRG1-DT | 0.056 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent; co-absent with the target |
| [[YBX3]] | C | YBX3 activity raises HHAT's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without YBX3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |
| [[DPH6-DT]] | C | DPH6-DT activity raises HHAT's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 3.17× lower at baseline in the lines without DPH6-DT | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLEC2D]] | C | HHAT activity raises CLEC2D's level | lines that do not express HHAT (4) vs lines expressing it (46) | 3.42× lower at baseline in the lines without HHAT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01341, C2orf92, GDAP1; maybe low, not absent; its own permutation p |
| [[ZFHX2]] | C | HHAT activity raises ZFHX2's level | lines that do not express HHAT (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without HHAT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01341, C2orf92, GDAP1; maybe low, not absent; its own permutation p |
| [[TRAM2-AS1]] | C | HHAT activity raises TRAM2-AS1's level | lines that do not express HHAT (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without HHAT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01341, C2orf92, GDAP1; maybe low, not absent; its own permutation p |
| [[EIF1B-AS1]] | C | HHAT activity raises EIF1B-AS1's level | lines that do not express HHAT (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without HHAT | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01341, C2orf92, GDAP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.1, 29.3); signed map (34.7, -9.6). **Vector** length 99.5, 28.2% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.1 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +4.9 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.1 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | hedgehog acyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:210,328,252-210,676,296 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10724, MART-2, MART2, Skn, ski, rasp, sit, GUP2 |
| Gene groups (HGNC) | Membrane bound O-acyltransferase family |
| Reactome | 4 pathways, smallest: Hh mutants abrogate ligand secretion; Hedgehog ligand biogenesis; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VTY9](https://www.uniprot.org/uniprotkb/Q5VTY9) (Protein-cysteine N-palmitoyltransferase HHAT):

> Palmitoyl acyltransferase that catalyzes N-terminal palmitoylation of hedgehog (DHH, IHH or SHH) morphogens, promoting their maturation. Promotes the transfer of palmitoyl-CoA from the cytoplasmic to the luminal side of the endoplasmic reticulum membrane, where hedgehog palmitoylation occurs. Required for hedgehog signaling during limb development (By similarity). Plays a role in proper testis cord formation and the differentiation of Leydig cells.

**Summary**, from NCBI Gene [55733](https://www.ncbi.nlm.nih.gov/gene/55733):

> 'Skinny hedgehog' (SKI1) encodes an enzyme that acts within the secretory pathway to catalyze amino-terminal palmitoylation of 'hedgehog' (see MIM 600725).[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:18270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18270) · Entrez [55733](https://www.ncbi.nlm.nih.gov/gene/55733) · UniProt [Q5VTY9](https://www.uniprot.org/uniprotkb/Q5VTY9) · Ensembl [ENSG00000054392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054392)

## Data

Gene col 609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 609); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 609]; `tensor/DDL_lfc|DDL_z.npy` [609]; `embed/gene_vectors.npy` [609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 609 or target_col == 609). Every well: [[HHAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HHAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
