---
symbol: "PHGDH"
type: "gene"
col: 1705
ensembl_id: "ENSG00000092621"
name: "phosphoglycerate dehydrogenase"
location: "1p12"
module: 63
arm: "+"
pooled_cpm: 34.97
n_lines_expressing: 45
n_dd_up: 37
n_dd_down: 22
n_dd_up_clean: 30
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# PHGDH

*phosphoglycerate dehydrogenase* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 0.5 µM: 2.55× (z +11.3, q 7e-27, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.407× (z -15.7, q 0e+00, down in 36 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSAT1]] (+0.92, fdr 7e-06), [[ASNS]] (+0.90, fdr 7e-06), [[AARS1]] (+0.85, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.55×** | +11.3 | 7e-27 | 41/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +11.1 | 4e-26 | 35/41 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.39×** | +10.7 | 2e-24 | 40/43 (C-33 A, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.21×** | +9.8 | 2e-20 | 41/43 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.72×** | +9.5 | 3e-19 | 37/43 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.2 | 2e-14 | 19/33 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.56×** | +7.8 | 5e-13 | 36/43 (SW480, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +7.4 | 8e-12 | 32/42 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.78×** | +7.1 | 8e-11 | 35/43 (C-33 A, hTERT-HPNE, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.49×** | +7.0 | 2e-10 | 30/43 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.71×** | +6.6 | 2e-09 | 30/43 (C-33 A, Panc 03.27, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.68×** | +6.3 | 2e-08 | 28/43 (HCT15, LS 180, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +5.8 | 2e-07 | 22/38 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 7e-05 | 28/43 (NCI-H2030, C-33 A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.48×** | +4.6 | 1e-04 | 29/43 (C-33 A, BT-474, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +4.4 | 4e-04 | 21/43 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 18/43 (SW480, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.002 | 16/43 (BT-474, SHP-77, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.003 | 18/43 (C32, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.003 | 19/43 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.407×** | -15.7 | 0e+00 | 36/42 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.433×** | -10.1 | 1e-21 | 30/42 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.519×** | -8.1 | 1e-13 | 33/43 (LoVo, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -6.7 | 3e-09 | 31/43 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.585×** | -6.5 | 9e-09 | 31/42 (HCT15, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.608×** | -6.1 | 8e-08 | 29/43 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -4.7 | 2e-04 | 22/43 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -4.7 | 2e-04 | 25/43 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.688×** | -4.5 | 4e-04 | 22/43 (H4, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -4.3 | 9e-04 | 18/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -4.2 | 0.001 | 20/42 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.618×** | -4.2 | 0.001 | 22/43 (HS-578T, A498, …) | two highest doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.719×** | -4.1 | 0.002 | 22/43 (LS 180, HS-578T, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.793×** | -4.1 | 0.002 | 18/43 (LoVo, H4, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -3.8 | 0.005 | 22/43 (RKO, H4, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.719×** | -3.7 | 0.007 | 21/43 (HS-578T, J82, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 52.1 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -20.8) |
| [[H4 (line)]] | wt | 153 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -24.8) |
| [[LoVo (line)]] | wt | 103 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -21.9) |
| [[SNU-1 (line)]] | wt | 102 | 1 | 4 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.72× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 22.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -10.3) |
| [[HS-578T (line)]] | alt | 97.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.9) |
| [[HT-29 (line)]] | alt | 27.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 1 | 2 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.85× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.9) |
| [[LS 180 (line)]] | wt | 86.3 | 1 | 1 | [[Artesunate (drug)]] 5 µM 2.48× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.131× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 22.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -8.9) |
| [[RKO (line)]] | wt | 52.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.4) |
| [[SW480 (line)]] | alt | 35.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.4) |
| [[A-172 (line)]] | wt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.1) |
| [[A-427 (line)]] | wt | 24.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.263× (z -8.8) |
| [[A498 (line)]] | wt | 60.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -8.6) |
| [[A549 (line)]] | wt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.34× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.8) |
| [[C32 (line)]] | wt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.7) |
| [[HCT15 (line)]] | alt | 81.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -12.0) |
| [[Hs 766T (line)]] | wt | 37.7 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.55× (z +10.8) | — |
| [[J82 (line)]] | alt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.73× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 31.7 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.48× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.5) |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.2) |
| [[SW48 (line)]] | wt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.2) |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSAT1]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[ASNS]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 829 |
| [[AARS1]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | STRING 448 |
| [[GARS1]] | +0.84 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[MTHFD2]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 722 |
| [[XPOT]] | +0.83 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[MARS1]] | +0.82 | +0.83 / +0.79 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[IARS1]] | +0.81 | +0.83 / +0.79 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[CARS1]] | +0.81 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[CHAC1]] | +0.80 | +0.74 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TCEA1]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[YARS1]] | +0.79 | +0.80 / +0.81 | both halves | 7e-06 | STRING 500 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises PHGDH's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without ANK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[NUPR1]] | B | NUPR1 activity raises PHGDH's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without NUPR1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[PSAT1]] | B | PSAT1 activity raises PHGDH's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 3.45× lower at baseline in the lines without PSAT1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises PHGDH's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 3.9% of all compounds | 0.060 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BCAT1]] | B | BCAT1 activity raises PHGDH's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without BCAT1 | 0.088 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX |
| [[ASNSP1]] | B | ASNSP1 activity weakens PHGDH's drug response | lines that do not express ASNSP1 (31) vs lines expressing it (12) | the lines without ASNSP1 respond 1.15× as strongly (z diff -0.20); strongest at Dinaciclib 5 µM: 2.05x vs 1.18x (z diff -2.6) | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15; target measured in part of the lines; both ways; artifact flags |
| [[SLC1A4]] | C | SLC1A4 activity raises PHGDH's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 2.86× lower at baseline in the lines without SLC1A4 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.900). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, 47.8); signed map (-13.6, 24.5). **Vector** length 135, 42.5% of its response variance represented; |z| ≥ 3 in 1,179 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.79 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.79 to 9); *unfolded protein response* (hallmark, mean cos +0.77 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +9.2 | +10.7 |
|  | [[Artesunate (drug)]] 5 µM |  | +7.2 | +9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +9.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.5 | +7.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.5 | +7.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.1 | +6.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +5.6 | +6.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +5.3 | +7.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -8.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -15.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.4 | -4.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.2 | -6.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphoglycerate dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:119,648,411-119,744,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SERA, PGDH, PDG |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O43175](https://www.uniprot.org/uniprotkb/O43175) (D-3-phosphoglycerate dehydrogenase):

> Catalyzes the reversible oxidation of 3-phospho-D-glycerate to 3-phosphonooxypyruvate, the first step of the phosphorylated L-serine biosynthesis pathway. Also catalyzes the reversible oxidation of 2-hydroxyglutarate to 2-oxoglutarate and the reversible oxidation of (S)-malate to oxaloacetate.

**Summary**, from NCBI Gene [26227](https://www.ncbi.nlm.nih.gov/gene/26227):

> This gene encodes the enzyme which is involved in the early steps of L-serine synthesis in animal cells. L-serine is required for D-serine and other amino acid synthesis. The enzyme requires NAD/NADH as a cofactor and forms homotetramers for activity. Mutations in this gene have been found in a family with congenital microcephaly, psychomotor retardation and other symptoms. Multiple alternatively spliced transcript variants have been found, however the full-length nature of most are not known. …

**Accessions** — [HGNC:8923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8923) · Entrez [26227](https://www.ncbi.nlm.nih.gov/gene/26227) · UniProt [O43175](https://www.uniprot.org/uniprotkb/O43175) · Ensembl [ENSG00000092621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092621)

## Data

Gene col 1705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1705); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1705]; `tensor/DDL_lfc|DDL_z.npy` [1705]; `embed/gene_vectors.npy` [1705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1705 or target_col == 1705). Every well: [[PHGDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHGDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
