---
symbol: "UBE2I"
type: "gene"
col: 2350
ensembl_id: "ENSG00000103275"
name: "ubiquitin conjugating enzyme E2 I"
location: "16p13.3"
module: 78
arm: "+"
pooled_cpm: 74.32
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# UBE2I

*ubiquitin conjugating enzyme E2 I* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +13.2, q 6e-37, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.64× (z +11.3, q 1e-27, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.823× (z -4.2, q 0.007, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.322×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.375×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Trimetrexate (drug)]] 0.05 µM in 1 line (NCI-H661 0.142×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYSL2]] (+0.50, fdr 7e-05), [[SPNS2]] (+0.49, fdr 9e-05), [[TTYH2]] (+0.47, fdr 3e-04); moves opposite to [[IWS1]] (-0.47, fdr 8e-05), [[MRPL32]] (-0.47, fdr 4e-05), [[ATAD2B]] (-0.46, fdr 3e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PDGFB]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SCAND1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 24 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.52×** | +13.2 | 6e-37 | 38/48 (LoVo, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.74×** | +12.4 | 1e-32 | 38/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.69×** | +11.7 | 2e-29 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +11.3 | 1e-27 | 44/49 (PANC-1, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.57×** | +9.7 | 2e-20 | 34/43 (A498, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +9.7 | 2e-20 | 42/48 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.52×** | +9.0 | 3e-17 | 37/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +8.4 | 3e-15 | 39/48 (LoVo, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.44×** | +8.0 | 5e-14 | 33/48 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.40×** | +7.2 | 3e-11 | 35/48 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +7.1 | 6e-11 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.35×** | +6.6 | 2e-09 | 28/48 (PANC-1, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +6.2 | 2e-08 | 35/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.32×** | +6.2 | 3e-08 | 40/49 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.31×** | +6.0 | 8e-08 | 26/48 (LOX-IMVI, SNU-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +5.0 | 1e-05 | 25/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.006 | 14/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.007 | 14/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.018 | 8/48 (MIA PaCa-2, HCT15, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.035 | 2/49 (hTERT-HPNE, SNU-1) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.037 | 6/49 (CFPAC-1, BT-474, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.051 | 11/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.053 | 12/48 (J82, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +2.8 | 0.073 | 15/47 (LOX-IMVI, SW48, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2350.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.322×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.375×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Trimetrexate (drug)]] 0.05 µM in 1 line (NCI-H661 0.142×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.823×** | -4.2 | 0.007 | 22/47 (CHP-212, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.826×** | -4.2 | 0.007 | 18/50 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 0.834× | -4.1 | 0.007 | 20/48 (AsPC-1, NCI-H2347, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.864× | -4.1 | 0.007 | 18/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.880× | -4.0 | 0.008 | 14/49 (SW480, HCT15, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.842× | -3.9 | 0.010 | 20/49 (H4, SW 900, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.838× | -3.7 | 0.015 | 19/49 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.893× | -3.6 | 0.020 | 13/48 (CFPAC-1, SW 900, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.855× | -3.5 | 0.023 | 15/48 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.856× | -3.5 | 0.023 | 15/48 (AsPC-1, J82, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.899× | -3.3 | 0.042 | 8/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.900× | -3.0 | 0.12 | 10/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.8 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.4) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[PANC-1 (line)]] | alt | 68.4 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.98× (z +10.4) | — |
| [[LoVo (line)]] | wt | 68.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.46× (z +11.5) | — |
| [[A498 (line)]] | wt | 75.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 84.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.2) ⚠ cell-cycle shift, explains ~53% of this change | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 63.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.31× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 67.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 76.7 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.84× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HEC-1-A (line)]] | alt | 81.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.96× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 50.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 94.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[AsPC-1 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[C32 (line)]] | wt | 68.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.1) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[HS-578T (line)]] | alt | 55.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +8.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 58.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.8) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[J82 (line)]] | alt | 86.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[KATO III (line)]] | alt | 88.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.11× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 58.2 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.63× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 81.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.8) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H661 (line)]] | alt | 57.8 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.142× (z -8.6) |
| [[SNU-423 (line)]] | alt | 98.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +16.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SW48 (line)]] | wt | 76.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SW480 (line)]] | alt | 100 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.00× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 88.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 87.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL2]] | +0.50 | +0.55 / +0.37 | both halves | 7e-05 | STRING 673 |
| [[SPNS2]] | +0.49 | +0.54 / +0.37 | both halves | 9e-05 |  |
| [[TTYH2]] | +0.47 | +0.47 / +0.29 | both halves | 3e-04 |  |
| [[RARA]] | +0.47 | +0.56 / +0.37 | both halves | 8e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 600 |
| [[SLC45A3]] | +0.47 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[CLIC1]] | +0.46 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[JPT2]] | +0.45 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[LAT]] | +0.43 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[SUN1]] | +0.43 | +0.39 / +0.36 | both halves | 1e-04 | pathway: Meiosis; STRING 528 |
| [[HCN2]] | +0.43 | +0.43 / +0.30 | both halves | 2e-04 |  |
| [[RTKN2]] | +0.43 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[NFE2L3]] | +0.43 | +0.51 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IWS1]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[MRPL32]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ATAD2B]] | -0.46 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[CDC37L1]] | -0.45 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[NDUFB2]] | -0.45 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[NDUFA1]] | -0.44 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[KIF9-AS1]] | -0.43 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ACOT2]] | -0.43 | -0.37 / -0.31 | both halves | 2e-04 | pathway: Dengue Virus Genome Translation and Replication |
| [[COBLL1]] | -0.42 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[RNF135]] | -0.42 | -0.33 / -0.42 | both halves | 1e-04 | pathway: SARS-CoV-2 Infection |
| [[RBM27]] | -0.42 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[SIK3]] | -0.42 | -0.38 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity raises UBE2I's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.21× lower at baseline in the lines without PDGFB | 0.038 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[MAP2K1]] | B | MAP2K1 activity raises UBE2I's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCAND1]] | C | UBE2I's natural level strengthens SCAND1's drug response | UBE2I's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.04; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.413). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, -4.5); signed map (-2.7, 41.6). **Vector** length 71.2, 15.8% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +5.4 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.9 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +8.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +11.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.2 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +9.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | -0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.3 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.1 | +7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -2.0 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,291,444-1,327,018 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBC9 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 70 pathways, smallest: SUMOylation of nuclear envelope proteins; SUMO is transferred from E1 to E2 (UBE2I, UBC9); Negative regulation of activity of TFAP2 (AP-2) family transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P63279](https://www.uniprot.org/uniprotkb/P63279) (SUMO-conjugating enzyme UBC9):

> Accepts the ubiquitin-like proteins SUMO1, SUMO2, SUMO3, SUMO4 and SUMO1P1/SUMO5 from the UBLE1A-UBLE1B E1 complex and catalyzes their covalent attachment to other proteins with the help of an E3 ligase such as RANBP2, CBX4 and ZNF451. Can catalyze the formation of poly-SUMO chains. Necessary for sumoylation of FOXL2 and KAT5. Essential for nuclear architecture and chromosome segregation. Sumoylates p53/TP53 at 'Lys-386'. Mediates sumoylation of ERCC6 which is essential for its …

**Summary**, from NCBI Gene [7329](https://www.ncbi.nlm.nih.gov/gene/7329):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. Four alternatively spliced transcript variants encoding the same protein have been found for this gene. …

**Accessions** — [HGNC:12485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12485) · Entrez [7329](https://www.ncbi.nlm.nih.gov/gene/7329) · UniProt [P63279](https://www.uniprot.org/uniprotkb/P63279) · Ensembl [ENSG00000103275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103275)

## Data

Gene col 2350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2350); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2350]; `tensor/DDL_lfc|DDL_z.npy` [2350]; `embed/gene_vectors.npy` [2350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2350 or target_col == 2350). Every well: [[UBE2I — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2I.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
