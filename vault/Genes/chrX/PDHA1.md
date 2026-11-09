---
symbol: "PDHA1"
type: "gene"
col: 5249
ensembl_id: "ENSG00000131828"
name: "pyruvate dehydrogenase E1 subunit alpha 1"
location: "Xp22.12"
module: 50
arm: "+"
pooled_cpm: 54.97
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PDHA1

*pyruvate dehydrogenase E1 subunit alpha 1* — Xp22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.41× (z +21.4, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.44× (z +6.4, q 2e-08, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.797× (z -5.1, q 2e-04, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SW48 0.246×, LS 180 0.397×, KATO III 0.439×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.141×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.364×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAS1L]] (+0.69, fdr 7e-06), [[PRKDC]] (+0.68, fdr 7e-06), [[NOC2L]] (+0.67, fdr 1e-05); moves opposite to [[SPATC1]] (-0.65, fdr 1e-05), [[EIF3J-DT]] (-0.64, fdr 1e-05), [[UPP2]] (-0.64, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARL17B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.41×** | +21.4 | 0e+00 | 47/47 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.13×** | +19.1 | 0e+00 | 39/40 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +15.2 | 0e+00 | 42/44 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +6.4 | 2e-08 | 35/48 (SNU-423, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.40×** | +5.8 | 6e-07 | 36/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.38×** | +5.6 | 2e-06 | 34/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.36×** | +5.4 | 5e-06 | 31/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.9 | 9e-05 | 28/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.29×** | +4.4 | 5e-04 | 25/47 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.001 | 29/48 (Hs 766T, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.2 | 0.002 | 0/48 | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.003 | 26/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.26×** | +3.8 | 0.006 | 23/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.8 | 0.007 | 17/35 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.018 | 17/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.024 | 20/48 (NCI-H460, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.055 | 10/47 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.084 | 12/48 (A-427, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5249.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SW48 0.246×, LS 180 0.397×, KATO III 0.439×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.141×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.364×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.797×** | -5.1 | 2e-04 | 26/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.680× | -3.5 | 0.11 | 18/48 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.822× | -3.4 | 0.11 | 18/48 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.705× | -3.2 | 0.19 | 8/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 101 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 55.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.397× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 45.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 55.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 45.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 58.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 84.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[KATO III (line)]] | alt | 99.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.59× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Digitoxin (drug)]] 5 µM 0.439× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 46.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.64× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 36.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.50× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 47.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 63.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 44.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 61.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 82.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[C32 (line)]] | wt | 34.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 41.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 48.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 43.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 33.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 95.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 49.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 59.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.3) |
| [[SW48 (line)]] | wt | 56.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.246× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 63.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 66.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C-33 A (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HCT15 (line)]] | alt | 59.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SHP-77 (line)]] | alt | 60.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW 900 (line)]] | alt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 60.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[BT-474 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAS1L]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.67 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[TTLL12]] | +0.66 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CS]] | +0.66 | +0.43 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 832 |
| [[BLTP2]] | +0.65 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PRPS1]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RPE]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 | STRING 529 |
| [[UGGT1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ATP5F1A]] | +0.63 | +0.57 / +0.63 | both halves | 9e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 822 |
| [[DLAT]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATC1]] | -0.65 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | -0.64 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[UPP2]] | -0.64 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TERF2IP]] | -0.64 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[LINC02608]] | -0.63 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[C1orf56]] | -0.62 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[EIF1]] | -0.62 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.62 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[OOEP]] | -0.61 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ZCCHC10]] | -0.61 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[HCG27]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.60 | -0.49 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL17B]] | B | ARL17B activity lowers PDHA1's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.19× higher at baseline in the lines without ARL17B | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.1, -35.3); signed map (-18.9, -45.5). **Vector** length 77.7, 18.0% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +2.9 | +5.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase E1 subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:19,343,893-19,361,718 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E1alpha; previously PDHA |
| Gene groups (HGNC) | Pyruvate dehydrogenase complex subunits; Pyruvate dehydrogenase E1 subunits |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 8 pathways, smallest: PDH complex synthesizes acetyl-CoA from PYR; Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P08559](https://www.uniprot.org/uniprotkb/P08559) (Pyruvate dehydrogenase E1 component subunit alpha, somatic form, mitochondrial):

> Together with PDHB forms the heterotetrameric E1 subunit of the pyruvate dehydrogenase (PDH) complex. The PDH complex catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2), and thereby links cytoplasmic glycolysis and the mitochondrial tricarboxylic acid (TCA) cycle. It contains multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetyltransferase (E2) and dihydrolipoamide dehydrogenase (E3) (Probable). The E1 subunit catalyzes both the …

**Summary**, from NCBI Gene [5160](https://www.ncbi.nlm.nih.gov/gene/5160):

> The pyruvate dehydrogenase (PDH) complex is a nuclear-encoded mitochondrial multienzyme complex that catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2), and provides the primary link between glycolysis and the tricarboxylic acid (TCA) cycle. The PDH complex is composed of multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetyltransferase (E2) and lipoamide dehydrogenase (E3). The E1 enzyme is a heterotetramer of two alpha and two …

**Accessions** — [HGNC:8806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8806) · Entrez [5160](https://www.ncbi.nlm.nih.gov/gene/5160) · UniProt [P08559](https://www.uniprot.org/uniprotkb/P08559) · Ensembl [ENSG00000131828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131828)

## Data

Gene col 5249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5249); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5249]; `tensor/DDL_lfc|DDL_z.npy` [5249]; `embed/gene_vectors.npy` [5249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5249 or target_col == 5249). Every well: [[PDHA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDHA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
