---
symbol: "MTERF1"
type: "gene"
col: 4852
ensembl_id: "ENSG00000127989"
name: "mitochondrial transcription termination factor 1"
location: "7q21.2"
module: 89
arm: "+"
pooled_cpm: 56.77
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# MTERF1

*mitochondrial transcription termination factor 1* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.23× (z +4.1, q 0.013, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.383× (z -13.5, q 6e-39, down in 40 of 44 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.709× (z -4.8, q 7e-05, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZKSCAN4]] (+0.60, fdr 1e-05), [[APTX]] (+0.60, fdr 1e-05), [[GPN2]] (+0.58, fdr 1e-05); moves opposite to [[STRBP]] (-0.53, fdr 5e-05), [[MAPK8]] (-0.53, fdr 8e-05), [[CRACD]] (-0.50, fdr 5e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPM2AIP1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[C9orf85]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.013 | 25/44 (HEC-1-A, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.36×** | +4.1 | 0.013 | 25/43 (SW480, A-172, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.050 | 22/43 (C32, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.20 | 18/43 (C32, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.25× | +3.1 | 0.20 | 18/44 (NCI-H23, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.383×** | -13.5 | 6e-39 | 40/44 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.420×** | -12.2 | 6e-32 | 39/44 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.431×** | -11.4 | 7e-28 | 33/44 (PANC-1, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.448×** | -10.9 | 2e-25 | 40/43 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.517×** | -9.3 | 2e-18 | 38/44 (H4, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.563×** | -8.1 | 6e-14 | 37/44 (BT-474, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.679×** | -7.7 | 1e-12 | 28/43 (hTERT-HPNE, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.565×** | -7.4 | 7e-12 | 27/40 (C32, SHP-77, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.630×** | -6.5 | 5e-09 | 25/45 (NCI-H23, PANC-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.704×** | -4.9 | 4e-05 | 25/44 (PANC-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -4.8 | 7e-05 | 28/44 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **0.715×** | -4.5 | 3e-04 | 23/39 (NCI-H1573, NCI-H1792, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -4.5 | 3e-04 | 28/45 (CFPAC-1, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | **0.730×** | -4.4 | 4e-04 | 27/44 (HOP62, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -4.4 | 5e-04 | 27/43 (SW 1271, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.749×** | -3.9 | 0.003 | 23/43 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.751×** | -3.9 | 0.003 | 25/44 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.773×** | -3.6 | 0.008 | 24/43 (CFPAC-1, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.796×** | -3.2 | 0.033 | 20/44 (CFPAC-1, H4, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.729×** | -3.2 | 0.035 | 19/44 (KATO III, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.654×** | -3.1 | 0.040 | 15/44 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.662×** | -3.0 | 0.050 | 15/42 (H4, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.0 | 0.060 | 18/44 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.814×** | -2.8 | 0.093 | 16/44 (J82, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 154 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.346× (z -9.1) |
| [[PANC-1 (line)]] | alt | 62.8 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -18.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.464× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0704× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[NCI-H1573 (line)]] | alt | 170 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0514× (z -31.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[NCI-H460 (line)]] | wt | 37.0 | 1 | 6 (6 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.364× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 64.8 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.1) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 69.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -20.2) ⚠ cell-cycle shift, explains ~81% of this change |
| [[hTERT-HPNE (line)]] | wt | 92.0 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -21.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SNU-423 (line)]] | alt | 56.0 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.8) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SW 900 (line)]] | alt | 69.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -16.2) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A549 (line)]] | wt | 40.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[BT-474 (line)]] | alt | 67.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 99.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[SW480 (line)]] | alt | 63.9 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.195× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 77.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[H4 (line)]] | wt | 51.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.117× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 30.6 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.91× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.364× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 59.0 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -14.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 129 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.79× (z +10.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -16.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 1088 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0665× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 45.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.1) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HepG2_C3A (line)]] | wt | 40.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 84.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -12.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 51.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[KATO III (line)]] | alt | 31.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.322× (z -8.8) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 61.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SK-MEL-2 (line)]] | alt | 60.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.40× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -10.0) ⚠ toxic |
| [[C-33 A (line)]] | alt | 70.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -11.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HS-578T (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -10.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -8.6) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0628× (z -8.6) |
| [[SW 1271 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0825× (z -10.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN4]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[APTX]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[GPN2]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CBLL1]] | +0.56 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[MTERF4]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 | STRING 783 |
| [[TBP]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ZNF529-AS1]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SLC25A17]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[UTP23]] | +0.54 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[ZBTB6]] | +0.54 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[ADAM20P1]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRBP]] | -0.53 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[MAPK8]] | -0.53 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[CRACD]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[SVIP]] | -0.50 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[KHDRBS3]] | -0.49 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[ARL15]] | -0.48 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[EPB41L2]] | -0.48 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MAGI1]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[EML6]] | -0.47 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[IGSF3]] | -0.47 | -0.39 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPM2AIP1]] | C | EPM2AIP1 activity raises MTERF1's level | lines that do not express EPM2AIP1 (3) vs lines expressing it (47) | 4.72× lower at baseline in the lines without EPM2AIP1 | 0.022 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MLF1, ADAL, TTC30A |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C9orf85]] | C | MTERF1 activity lowers C9orf85's level | lines that do not express MTERF1 (4) vs lines expressing it (46) | 1.04× higher at baseline in the lines without MTERF1 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with EP300, RNF43, B2M; also absent: TBC1D9, RBMS1, SIX1 |

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.1, 8.8); signed map (0.7, -3.4). **Vector** length 89.3, 24.5% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.7 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.9 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial transcription termination factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:91,692,008-91,880,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MTERF |
| Gene groups (HGNC) | Mitochondrial nucleoid associated proteins |
| Reactome | 4 pathways, smallest: Mitochondrial transcription; Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99551](https://www.uniprot.org/uniprotkb/Q99551) (Transcription termination factor 1, mitochondrial):

> Transcription termination factor. Binds to a 28 bp region within the tRNA(Leu(uur)) gene at a position immediately adjacent to and downstream of the 16S rRNA gene; this region comprises a tridecamer sequence critical for directing accurate termination. Binds DNA along the major grove and promotes DNA bending and partial unwinding. Promotes base flipping. Transcription termination activity appears to be polarized with highest specificity for transcripts initiated on the light strand.

**Summary**, from NCBI Gene [7978](https://www.ncbi.nlm.nih.gov/gene/7978):

> This gene encodes a mitochondrial transcription termination factor. This protein participates in attenuating transcription from the mitochondrial genome; this attenuation allows higher levels of expression of 16S ribosomal RNA relative to the tRNA gene downstream. The product of this gene has three leucine zipper motifs bracketed by two basic domains that are all required for DNA binding. There is evidence that, for this protein, the zippers participate in intramolecular interactions that …

**Accessions** — [HGNC:21463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21463) · Entrez [7978](https://www.ncbi.nlm.nih.gov/gene/7978) · UniProt [Q99551](https://www.uniprot.org/uniprotkb/Q99551) · Ensembl [ENSG00000127989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127989)

## Data

Gene col 4852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4852); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4852]; `tensor/DDL_lfc|DDL_z.npy` [4852]; `embed/gene_vectors.npy` [4852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4852 or target_col == 4852). Every well: [[MTERF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTERF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
