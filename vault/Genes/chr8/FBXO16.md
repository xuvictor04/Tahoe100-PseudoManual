---
symbol: "FBXO16"
type: "gene"
col: 13168
ensembl_id: "ENSG00000214050"
name: "F-box protein 16"
location: "8p21.1"
module: 49
arm: "+"
pooled_cpm: 28.37
n_lines_expressing: 41
n_dd_up: 18
n_dd_down: 38
n_dd_up_clean: 18
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# FBXO16

*F-box protein 16* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.22× (z +10.5, q 7e-23, up in 30 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.193× (z -21.6, q 0e+00, down in 39 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLPH3L]] (+0.70, fdr 7e-06), [[COG6]] (+0.67, fdr 1e-05), [[ACBD3]] (+0.66, fdr 1e-05); moves opposite to [[PRRC2B]] (-0.57, fdr 2e-05), [[DDX5]] (-0.57, fdr 4e-05), [[ZMYND11]] (-0.56, fdr 5e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[VWDE]] → it (grade B ⚠); 5 go from it, the strongest it → [[SLC31A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.22×** | +10.5 | 7e-23 | 30/39 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +9.8 | 4e-20 | 36/39 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +8.8 | 3e-16 | 29/39 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +8.8 | 3e-16 | 33/39 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +7.9 | 4e-13 | 33/39 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +7.4 | 2e-11 | 32/39 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +5.8 | 7e-07 | 24/39 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.29×** | +5.7 | 1e-06 | 22/39 (SK-MEL-2, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +5.2 | 2e-05 | 21/39 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 5e-05 | 20/39 (C-33 A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 3e-04 | 18/39 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.003 | 13/39 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.011 | 16/38 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.011 | 10/39 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.014 | 10/39 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.193×** | -21.6 | 0e+00 | 39/39 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.237×** | -18.4 | 0e+00 | 38/39 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.248×** | -18.3 | 0e+00 | 38/39 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.241×** | -18.2 | 0e+00 | 38/39 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.318×** | -14.4 | 4e-45 | 33/37 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.536×** | -10.9 | 1e-25 | 29/38 (A-427, A498, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.240×** | -9.8 | 1e-20 | 31/40 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.273×** | -8.9 | 4e-17 | 29/38 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.512×** | -8.4 | 4e-15 | 30/39 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.520×** | -8.2 | 2e-14 | 26/38 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.527×** | -8.1 | 3e-14 | 27/38 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.601×** | -6.7 | 1e-09 | 22/38 (RPMI-7951, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.643×** | -5.8 | 3e-07 | 21/36 (LoVo, COLO 205, …) | two highest doses | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.652×** | -5.6 | 8e-07 | 23/39 (NCI-H460, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.656×** | -5.5 | 1e-06 | 20/39 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.664×** | -5.4 | 3e-06 | 21/39 (H4, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.3 | 5e-06 | 23/39 (SNU-423, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.662×** | -5.2 | 7e-06 | 21/38 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.676×** | -4.8 | 4e-05 | 21/38 (HEC-1-A, AN3 CA, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -4.3 | 4e-04 | 19/39 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -4.3 | 4e-04 | 19/39 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 62.6 | 0 | 14 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0204× (z -23.3) |
| [[SW480 (line)]] | alt | 54.6 | 0 | 11 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0992× (z -20.4) |
| [[A498 (line)]] | wt | 51.4 | 1 | 8 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.36× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -14.4) |
| [[A-172 (line)]] | wt | 22.6 | 4 | 4 | [[Panobinostat (drug)]] 5 µM 5.91× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -12.8) |
| [[COLO 205 (line)]] | alt | 58.9 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0584× (z -15.3) |
| [[LoVo (line)]] | wt | 75.6 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0602× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 28.6 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -11.9) |
| [[A549 (line)]] | wt | 23.6 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +8.6) | [[Digitoxin (drug)]] 0.5 µM 0.118× (z -13.7) |
| [[HCT15 (line)]] | alt | 77.3 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0544× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0667× (z -14.7) |
| [[LS 180 (line)]] | wt | 73.7 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0230× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0550× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 24.4 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.148× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 29.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 43.6 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0993× (z -14.2) |
| [[A-427 (line)]] | wt | 42.2 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 28.0 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0951× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 54.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0723× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 41.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -10.1) |
| [[SHP-77 (line)]] | alt | 51.6 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -17.8) |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -9.9) |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -11.6) |
| [[HOP62 (line)]] | alt | 19.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.30× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -11.6) |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0842× (z -10.7) |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0455× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.171× (z -9.6) |
| [[RKO (line)]] | wt | 16.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +16.7) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SNU-423 (line)]] | alt | 8.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0625× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 9.91 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -9.5) |
| [[SW48 (line)]] | wt | 37.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0723× (z -12.1) |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLPH3L]] | +0.70 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[COG6]] | +0.67 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.66 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[GBF1]] | +0.66 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SSR2]] | +0.66 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[SRP54]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.65 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[EAF2]] | +0.64 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MANF]] | +0.64 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[TMEM263]] | +0.64 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EIF2AK3]] | +0.64 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GORASP2]] | +0.63 | +0.43 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2B]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[DDX5]] | -0.57 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[ZMYND11]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[HIPK3]] | -0.56 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[TOR1A]] | -0.56 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[UBTF]] | -0.56 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[AVEN]] | -0.55 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[SLC39A10]] | -0.55 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[TULP4]] | -0.54 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[DOCK1]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZNF124]] | -0.53 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[LRRK1]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VWDE]] | B | VWDE activity raises FBXO16's level | lines that do not express VWDE (22) vs lines expressing it (28) | 1.64× lower at baseline in the lines without VWDE | 0.091 | ⚠ within organs, on part of the lines; also absent: RBM11, L3MBTL4, RPS6KA6 |
| [[ERLEC1]] | C | ERLEC1's natural level strengthens FBXO16's drug response | ERLEC1's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.39; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC31A1]] | B | FBXO16 activity lowers SLC31A1's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without FBXO16 | 0.034 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |
| [[SWI5]] | B | FBXO16 activity lowers SWI5's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.24× higher at baseline in the lines without FBXO16 | 0.040 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |
| [[KDELR2]] | B | FBXO16 activity lowers KDELR2's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.41× higher at baseline in the lines without FBXO16 | 0.044 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |
| [[HM13]] | B | FBXO16 activity lowers HM13's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.35× higher at baseline in the lines without FBXO16 | 0.057 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |
| [[PGM3]] | B | FBXO16 activity lowers PGM3's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.43× higher at baseline in the lines without FBXO16 | 0.058 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, -35.3); signed map (-53.1, 12.2). **Vector** length 102, 28.9% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +7.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.8 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.7 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +5.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -14.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.6 | -8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -18.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -5.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:28,348,287-28,490,278 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX16 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX29](https://www.uniprot.org/uniprotkb/Q8IX29) (F-box only protein 16):

> Substrate recognition component of an SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex that mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Functions as a putative tumor suppressor by targeting nuclear beta-catenin/CTNNB1 for degradation independently of upstream activating signals, thereby inhibiting epithelial-to-mesenchymal transition. Controls the ubiquitination and degradation of hnRNPL. Negatively regulates NF-kappa-B signaling by …

**Summary**, from NCBI Gene [157574](https://www.ncbi.nlm.nih.gov/gene/157574):

> This gene encodes a member of the F-box protein family, members of which are characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into three classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein …

**Accessions** — [HGNC:13618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13618) · Entrez [157574](https://www.ncbi.nlm.nih.gov/gene/157574) · UniProt [Q8IX29](https://www.uniprot.org/uniprotkb/Q8IX29) · Ensembl [ENSG00000214050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214050)

## Data

Gene col 13168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13168); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13168]; `tensor/DDL_lfc|DDL_z.npy` [13168]; `embed/gene_vectors.npy` [13168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13168 or target_col == 13168). Every well: [[FBXO16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
