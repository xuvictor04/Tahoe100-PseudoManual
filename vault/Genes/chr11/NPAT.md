---
symbol: "NPAT"
type: "gene"
col: 7364
ensembl_id: "ENSG00000149308"
name: "nuclear protein, coactivator of histone transcription"
location: "11q22.3"
module: 6
arm: "+"
pooled_cpm: 47.67
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NPAT

*nuclear protein, coactivator of histone transcription* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +14.6, q 3e-45, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.510× (z -12.5, q 3e-33, down in 32 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.567× (z -5.3, q 2e-05, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZGRF1]] (+0.74, fdr 7e-06), [[ASF1B]] (+0.70, fdr 7e-06), [[MASTL]] (+0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +14.6 | 3e-45 | 37/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.09×** | +14.2 | 2e-43 | 47/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.06×** | +14.0 | 4e-42 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.83×** | +11.7 | 2e-29 | 46/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +10.6 | 2e-24 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +9.4 | 3e-19 | 39/48 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.62×** | +9.0 | 2e-17 | 38/48 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +8.4 | 4e-15 | 32/48 (AsPC-1, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.55×** | +8.2 | 2e-14 | 36/48 (HS-578T, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +6.8 | 5e-10 | 33/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +6.7 | 9e-10 | 37/48 (PANC-1, HEC-1-A, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.7 | 1e-09 | 29/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.6 | 2e-09 | 33/48 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +6.2 | 2e-08 | 29/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +5.7 | 5e-07 | 28/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.001 | 17/48 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.007 | 14/48 (Panc 03.27, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -12.5 | 3e-33 | 32/40 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -12.0 | 7e-31 | 37/48 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -7.8 | 1e-12 | 29/45 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.567×** | -5.3 | 2e-05 | 26/48 (SW1417, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.793×** | -4.5 | 8e-04 | 21/48 (A549, LoVo, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.629×** | -4.3 | 0.002 | 17/48 (Hs 766T, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.737×** | -4.2 | 0.002 | 21/48 (SW1417, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.816×** | -4.0 | 0.005 | 17/48 (A498, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.832×** | -3.6 | 0.021 | 18/48 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.774×** | -3.6 | 0.021 | 14/48 (SW480, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.881× | -3.5 | 0.025 | 17/48 (A-427, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.883× | -3.4 | 0.030 | 15/48 (A-427, CFPAC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.703×** | -3.3 | 0.045 | 11/48 (SW1417, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.712×** | -3.2 | 0.064 | 11/48 (SW1417, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.720×** | -3.1 | 0.085 | 21/46 (A498, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.805×** | -3.0 | 0.086 | 15/48 (AN3 CA, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.805×** | -3.0 | 0.086 | 13/48 (Hs 766T, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.725×** | -3.0 | 0.086 | 12/48 (NCI-H661, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 72.2 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -19.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 66.3 | 5 (3 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.34× (z +11.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 60.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.1) | — |
| [[KATO III (line)]] | alt | 93.7 | 2 (2 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.2) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -18.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 62.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +16.2) | — |
| [[SW1417 (line)]] | alt | 68.7 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 54.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -15.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 44.9 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.28× (z +11.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 37.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.8) |
| [[BT-474 (line)]] | alt | 28.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 48.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +11.1) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 67.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 42.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 52.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 55.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 79.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -14.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0613× (z -14.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 40.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +9.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 55.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0797× (z -19.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZGRF1]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[ASF1B]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[MASTL]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.68 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[KIF24]] | +0.67 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[FANCM]] | +0.67 | +0.57 / +0.69 | both halves | 8e-06 |  |
| [[TK1]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[ZNF367]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[E2F8]] | +0.66 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.66 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[CCNE2]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ATAD2]] | +0.64 | +0.62 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.0, -48.1); signed map (-42.0, -46.0). **Vector** length 87.6, 22.5% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cell Cycle Checkpoints* (reactome, mean cos +0.52 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.52 to 22); *Activation of ATR in response to replication stress* (reactome, mean cos +0.53 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.6 | +9.0 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.0 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.0 | +10.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.9 | +0.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +1.4 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | +1.5 | +0.3 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.5 | +0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +0.3 |
| fall | [[EX229 (drug)]] 5 µM |  | -5.0 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.7 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -7.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear protein, coactivator of histone transcription |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:108,157,215-108,222,638 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E14, p220 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14207](https://www.uniprot.org/uniprotkb/Q14207) (Protein NPAT):

> Transcription regulator required for progression through the G1 and S phases of the cell cycle and for S phase entry. Acts as a key transcription regulator of histones. Activates transcription of the histone H2A, histone H2B, histone H3 and histone H4 genes in conjunction with GON4L and MIZF. Together with CRAMP1, binds to the promoters of H1 genes (H1-2, H1-3, H1-4, H1-5 and H1-10/H1x), driving their transcription. Also positively regulates the ATM, MIZF and PRKDC promoters. Transcriptional …

**Summary**, from NCBI Gene [4863](https://www.ncbi.nlm.nih.gov/gene/4863):

> Enables transcription coactivator activity and transcription corepressor activity. Involved in cell cycle G1/S phase transition and positive regulation of transcription by RNA polymerase II. Located in Cajal body; Gemini of Cajal bodies; and cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7896) · Entrez [4863](https://www.ncbi.nlm.nih.gov/gene/4863) · UniProt [Q14207](https://www.uniprot.org/uniprotkb/Q14207) · Ensembl [ENSG00000149308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149308)

## Data

Gene col 7364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7364); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7364]; `tensor/DDL_lfc|DDL_z.npy` [7364]; `embed/gene_vectors.npy` [7364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7364 or target_col == 7364). Every well: [[NPAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
