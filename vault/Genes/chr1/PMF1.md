---
symbol: "PMF1"
type: "gene"
col: 8380
ensembl_id: "ENSG00000160783"
name: "polyamine modulated factor 1"
location: "1q22"
module: 173
arm: "+"
pooled_cpm: 23.73
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# PMF1

*polyamine modulated factor 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +19.8, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.269× (z -29.8, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERMAP]] (+0.73, fdr 3e-05), [[BRPF3]] (+0.71, fdr 2e-05), [[FKRP]] (+0.70, fdr 2e-05); moves opposite to [[PDCD10]] (-0.74, fdr 8e-06), [[HK1]] (-0.65, fdr 3e-05), [[WASF3]] (-0.64, fdr 7e-05).
> It is in [[Module 173]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +19.8 | 0e+00 | 36/47 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +11.2 | 1e-26 | 31/45 (A-427, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +11.1 | 1e-26 | 25/38 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.6 | 1e-15 | 24/34 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +8.6 | 1e-15 | 27/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +7.4 | 1e-11 | 23/46 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +7.1 | 7e-11 | 23/47 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.2 | 2e-05 | 18/47 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.006 | 8/47 (NCI-H2030, C32, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.006 | 9/47 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.19× | +3.7 | 0.009 | 14/47 (C32, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.18× | +3.7 | 0.009 | 18/47 (C32, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.011 | 12/46 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.269×** | -29.8 | 0e+00 | 47/47 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.353×** | -23.6 | 0e+00 | 47/48 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.370×** | -22.5 | 0e+00 | 44/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.380×** | -22.0 | 0e+00 | 47/48 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.381×** | -21.9 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.307×** | -14.0 | 1e-42 | 40/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.759×** | -8.8 | 8e-17 | 31/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.713×** | -7.7 | 1e-12 | 29/47 (SW1417, SNU-423, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.736×** | -6.9 | 2e-10 | 22/47 (COLO 205, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.798×** | -5.1 | 2e-05 | 19/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.855× | -5.0 | 3e-05 | 21/48 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.659×** | -4.9 | 4e-05 | 16/48 (A-427, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.814×** | -4.5 | 3e-04 | 16/46 (NCI-H23, COLO 205, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.688×** | -4.4 | 4e-04 | 14/45 (hTERT-HPNE, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.696×** | -4.3 | 7e-04 | 17/47 (SNU-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.876× | -4.2 | 8e-04 | 12/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.722×** | -3.9 | 0.004 | 12/46 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.893× | -3.6 | 0.008 | 10/48 (H4, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 46.8 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.222× (z -15.1) |
| [[COLO 205 (line)]] | alt | 40.6 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0685× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 26.4 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.0) | [[Belinostat (drug)]] 5 µM 0.250× (z -13.6) |
| [[SW480 (line)]] | alt | 26.8 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -16.5) |
| [[HOP62 (line)]] | alt | 19.4 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.5) | [[Belinostat (drug)]] 5 µM 0.201× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 21.7 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.0) | [[Belinostat (drug)]] 0.5 µM 0.170× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 21.1 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +23.5) | [[Belinostat (drug)]] 5 µM 0.111× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 44.3 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.54× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.325× (z -11.5) |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.237× (z -16.8) |
| [[A-172 (line)]] | wt | 24.4 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.213× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 24.2 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.3) | [[Belinostat (drug)]] 5 µM 0.253× (z -11.8) |
| [[A-427 (line)]] | wt | 23.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.207× (z -12.3) |
| [[A498 (line)]] | wt | 28.6 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.422× (z -8.6) |
| [[C32 (line)]] | wt | 22.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 44.5× (z +33.2) | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.3) | [[Belinostat (drug)]] 0.5 µM 0.352× (z -9.2) |
| [[J82 (line)]] | alt | 16.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.235× (z -9.9) |
| [[KATO III (line)]] | alt | 24.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +8.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.251× (z -11.4) |
| [[LoVo (line)]] | wt | 19.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.1) | [[Belinostat (drug)]] 5 µM 0.272× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -12.0) |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.155× (z -10.9) |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -10.0) |
| [[SW 900 (line)]] | alt | 32.8 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0926× (z -9.1) ⚠ toxic · without an alert: [[Belinostat (drug)]] 0.5 µM 0.291× (z -9.0) |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -9.8) |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0737× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 16.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +21.4) | [[Belinostat (drug)]] 5 µM 0.287× (z -9.1) |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.245× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 17.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +15.8) | [[Docetaxel (drug)]] 0.05 µM 0.175× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 34.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.341× (z -9.0) |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -9.3) |
| [[A549 (line)]] | wt | 18.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.239× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.187× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 44.5 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.258× (z -11.3) |
| [[H4 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0997× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.187× (z -10.3) |
| [[HS-578T (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +17.5) | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.291× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.230× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +21.2) | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERMAP]] | +0.73 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[BRPF3]] | +0.71 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[FKRP]] | +0.70 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[DCAF8]] | +0.70 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[COQ7]] | +0.70 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.70 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[EFCAB2]] | +0.70 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[SRSF6]] | +0.69 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MED12]] | +0.67 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[VPS52]] | +0.67 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PBLD]] | +0.66 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TIA1]] | +0.66 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD10]] | -0.74 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[HK1]] | -0.65 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[WASF3]] | -0.64 | -0.59 / -0.37 | both halves | 7e-05 | pathway: RHO GTPase Effectors |
| [[UBE2O]] | -0.62 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.62 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[MAP2K1]] | -0.61 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[TMEM120B]] | -0.61 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[HEBP1]] | -0.61 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MPZL1]] | -0.61 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[MMS19]] | -0.60 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TSEN54]] | -0.60 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[HDAC3]] | -0.60 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.8, 5.0); signed map (16.5, -23.3). **Vector** length 104, 24.9% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.3 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -9.7 | -22.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.0 | -22.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -29.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.2 | -14.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.5 | -7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -8.8 |

## What is on record

|  |  |
|---|---|
| Name | polyamine modulated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,212,993-156,240,042 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MIS12 kinetochore complex |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1K2](https://www.uniprot.org/uniprotkb/Q6P1K2) (Polyamine-modulated factor 1):

> Part of the MIS12 complex which is required for normal chromosome alignment and segregation and kinetochore formation during mitosis. May act as a cotranscription partner of NFE2L2 involved in regulation of polyamine-induced transcription of SSAT.

**Summary**, from NCBI Gene [11243](https://www.ncbi.nlm.nih.gov/gene/11243):

> Enables leucine zipper domain binding activity and transcription coactivator activity. Involved in chromosome segregation. Located in kinetochore and nucleoplasm. Part of MIS12/MIND type complex. Implicated in bladder carcinoma and urinary bladder cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9112) · Entrez [11243](https://www.ncbi.nlm.nih.gov/gene/11243) · UniProt [Q6P1K2](https://www.uniprot.org/uniprotkb/Q6P1K2) · Ensembl [ENSG00000160783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160783)

## Data

Gene col 8380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8380); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8380]; `tensor/DDL_lfc|DDL_z.npy` [8380]; `embed/gene_vectors.npy` [8380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8380 or target_col == 8380). Every well: [[PMF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
