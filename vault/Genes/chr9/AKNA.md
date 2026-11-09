---
symbol: "AKNA"
type: "gene"
col: 2815
ensembl_id: "ENSG00000106948"
name: "AT-hook transcription factor"
location: "9q32"
module: 63
arm: "+"
pooled_cpm: 18.64
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 17
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# AKNA

*AT-hook transcription factor* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.36× (z +13.1, q 2e-36, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.469× (z -11.5, q 5e-28, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASNS]] (+0.74, fdr 7e-06), [[PHGDH]] (+0.70, fdr 7e-06), [[MTHFD2]] (+0.69, fdr 7e-06); moves opposite to [[COQ6]] (-0.44, fdr 7e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CHAC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.36×** | +13.1 | 2e-36 | 38/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.68×** | +11.1 | 2e-26 | 34/47 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +11.0 | 6e-26 | 37/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +10.8 | 3e-25 | 32/47 (SW1417, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +8.1 | 7e-14 | 32/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +7.8 | 7e-13 | 29/46 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.66×** | +7.8 | 7e-13 | 31/46 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +7.3 | 2e-11 | 29/46 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +6.9 | 3e-10 | 25/47 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.48×** | +6.0 | 9e-08 | 27/46 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +6.0 | 1e-07 | 23/47 (SHP-77, SW480, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.44×** | +5.6 | 1e-06 | 25/47 (SNU-1, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 8e-06 | 24/46 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.2 | 9e-06 | 20/42 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +5.1 | 1e-05 | 15/47 (SW480, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.23×** | +4.5 | 2e-04 | 17/47 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.005 | 17/47 (Hs 766T, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.469×** | -11.5 | 5e-28 | 35/45 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.532×** | -9.6 | 2e-19 | 29/47 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.594×** | -7.9 | 4e-13 | 26/45 (COLO 205, SW480, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.455×** | -6.2 | 6e-08 | 28/47 (PANC-1, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.486×** | -5.7 | 1e-06 | 23/43 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.696×** | -5.5 | 3e-06 | 22/45 (PANC-1, SW48, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.741×** | -4.6 | 4e-04 | 16/47 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.734×** | -4.3 | 1e-03 | 21/44 (PANC-1, A549, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.744×** | -4.3 | 1e-03 | 15/27 (SW480, J82, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.595×** | -4.1 | 0.002 | 16/43 (HCT15, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.777×** | -3.8 | 0.006 | 16/39 (PANC-1, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.5 | 0.020 | 16/47 (RKO, PANC-1, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.784×** | -3.4 | 0.027 | 18/36 (SNU-423, PANC-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.801×** | -3.4 | 0.030 | 17/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.798×** | -3.3 | 0.035 | 18/46 (SW480, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.858× | -3.3 | 0.035 | 15/47 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.814×** | -3.1 | 0.058 | 9/45 (COLO 205, A549, …) | inconsistent across doses | position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | **0.807×** | -3.1 | 0.067 | 8/47 (SW480, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.9 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.139× (z -17.9) |
| [[HT-29 (line)]] | alt | 33.7 | 0 | 8 (7 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.166× (z -11.6) |
| [[KATO III (line)]] | alt | 60.3 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.145× (z -13.7) |
| [[SW480 (line)]] | alt | 14.8 | 2 | 5 (3 ⚠) | [[Artesunate (drug)]] 5 µM 2.20× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.223× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 11.3 | 6 (2 ⚠) | 0 | [[5-Azacytidine (drug)]] 5 µM 4.85× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 65.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -18.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 37.2 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.278× (z -8.8) |
| [[A-172 (line)]] | wt | 16.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +13.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 16.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.187× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SNU-1 (line)]] | wt | 11.7 | 2 | 0 | [[Artesunate (drug)]] 5 µM 8.89× (z +9.8) | — |
| [[A498 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A549 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0613× (z -13.6) ⚠ toxic |
| [[C32 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0926× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0878× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.207× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 8.81 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0929× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SHP-77 (line)]] | alt | 13.6 | 1 | 0 | [[Artesunate (drug)]] 5 µM 3.54× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0583× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASNS]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[PHGDH]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CARS1]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PSAT1]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[AARS1]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[GOT1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CHAC1]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[YARS1]] | +0.64 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[SARS1]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SLC1A5]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[GARS1]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ6]] | -0.44 | -0.37 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHAC1]] | B | CHAC1 activity raises AKNA's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.17× lower at baseline in the lines without CHAC1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.0, 48.5); signed map (-13.4, 25.3). **Vector** length 105, 25.5% of its response variance represented; |z| ≥ 3 in 1,396 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.61 to 16); *mTORC1 signaling* (hallmark, mean cos +0.54 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.60 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +6.0 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +7.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.8 | +7.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.5 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -11.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.7 | -7.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | +0.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | AT-hook transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:114,334,156-114,394,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1968 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z591](https://www.uniprot.org/uniprotkb/Q7Z591) (Microtubule organization protein AKNA):

> Centrosomal protein that plays a key role in cell delamination by regulating microtubule organization (By similarity). Required for the delamination and retention of neural stem cells from the subventricular zone during neurogenesis (By similarity). Also regulates the epithelial-to-mesenchymal transition in other epithelial cells (By similarity). Acts by increasing centrosomal microtubule nucleation and recruiting nucleation factors and minus-end stabilizers, thereby destabilizing microtubules …

**Summary**, from NCBI Gene [80709](https://www.ncbi.nlm.nih.gov/gene/80709):

> Predicted to enable DNA binding activity. Involved in positive regulation of transcription by RNA polymerase II. Located in centrosome; fibrillar center; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24108) · Entrez [80709](https://www.ncbi.nlm.nih.gov/gene/80709) · UniProt [Q7Z591](https://www.uniprot.org/uniprotkb/Q7Z591) · Ensembl [ENSG00000106948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106948)

## Data

Gene col 2815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2815); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2815]; `tensor/DDL_lfc|DDL_z.npy` [2815]; `embed/gene_vectors.npy` [2815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2815 or target_col == 2815). Every well: [[AKNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
