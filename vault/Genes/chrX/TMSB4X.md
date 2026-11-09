---
symbol: "TMSB4X"
type: "gene"
col: 12986
ensembl_id: "ENSG00000205542"
name: "thymosin beta 4 X-linked"
location: "Xp22.2"
module: 7
arm: "-"
pooled_cpm: 331.14
n_lines_expressing: 41
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TMSB4X

*thymosin beta 4 X-linked* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.32× (z +15.5, q 0e+00, up in 40 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.69× (z +7.3, q 3e-11, up in 36 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (PANC-1 7.77×, A549 9.02×, J82 5.17×, NCI-H1792 7.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 7.88×, NCI-H1792 8.87×, A549 8.11×, HEC-1-A 6.16×, …; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 2 lines (RPMI-7951 2.54×, HS-578T 2.37×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 1.94×).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Roxadustat (drug)]] 5 µM: 0.668× (z -4.2, q 0.012, down in 38 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.209×, NCI-H2347 0.444×, SW 900 0.484×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.416×, SNU-1 0.425×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (hTERT-HPNE 0.338×; ⚠ cell-cycle shift, explains ~97% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALM2]] (+0.59, fdr 1e-05), [[ITM2C]] (+0.58, fdr 1e-05), [[TAGLN2]] (+0.57, fdr 1e-05); moves opposite to [[POLR3F]] (-0.60, fdr 3e-05), [[PEX16]] (-0.60, fdr 1e-05), [[DNAJC2]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[QPCT]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Sodium Salicylate (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12986.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (PANC-1 7.77×, A549 9.02×, J82 5.17×, NCI-H1792 7.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 7.88×, NCI-H1792 8.87×, A549 8.11×, HEC-1-A 6.16×, …; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 2 lines (RPMI-7951 2.54×, HS-578T 2.37×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 1.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.32×** | +15.5 | 0e+00 | 40/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.33×** | +15.3 | 0e+00 | 36/36 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.34×** | +12.1 | 1e-31 | 35/36 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +7.4 | 1e-11 | 25/41 (J82, SNU-423, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.3 | 3e-11 | 36/39 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.67×** | +5.6 | 2e-06 | 33/39 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +5.5 | 2e-06 | 35/40 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.66×** | +5.5 | 3e-06 | 38/39 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.62×** | +5.2 | 1e-05 | 33/39 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.57×** | +4.7 | 1e-04 | 27/38 (NCI-H1792, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.49×** | +4.3 | 8e-04 | 29/39 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.9 | 0.005 | 21/31 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.43×** | +3.9 | 0.005 | 25/39 (PANC-1, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.7 | 0.010 | 21/38 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12986.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.209×, NCI-H2347 0.444×, SW 900 0.484×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.416×, SNU-1 0.425×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (hTERT-HPNE 0.338×; ⚠ cell-cycle shift, explains ~97% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Roxadustat (drug)]] 5 µM |  | **0.668×** | -4.2 | 0.012 | 38/39 (J82, SW 1088, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -3.9 | 0.031 | 24/39 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.551× | -3.4 | 0.12 | 26/40 (BT-474, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.708× | -3.1 | 0.31 | 21/41 (SW 900, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 505 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.94× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 197 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.77× (z +18.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 469 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +14.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 449 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.37× (z +9.4) | — |
| [[KATO III (line)]] | alt | 498 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +14.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 1,115 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.14× (z +14.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 150 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.07× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.54× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 326 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 255 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.02× (z +17.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 259 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +13.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 744 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +11.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 358 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.96× (z +11.3) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -9.2) ⚠ cell-cycle shift, explains ~97% of this change |
| [[J82 (line)]] | alt | 486 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +15.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.58× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 365 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.36× (z +15.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 159 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 85.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.66× (z +13.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 260 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 497 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 499 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.45× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 294 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +12.3) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.03× (z +11.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 865 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 90.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.74× (z +9.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 239 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 214 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.66× (z +12.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 881 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +12.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 170 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.84× (z +13.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 228 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 732 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 1,026 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 373 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 41.2 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 55.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 581 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 394 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 77.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 34.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 76.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 609 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM2]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ITM2C]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TAGLN2]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 475 |
| [[S100A4]] | +0.56 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[PERP]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[FAM81A]] | +0.54 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[EPB41L2]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[OLFML2A]] | +0.54 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[SERPINE2]] | +0.53 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[CLSTN1]] | +0.53 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[H2AZ2]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[THY1]] | +0.51 | +0.48 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3F]] | -0.60 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[PEX16]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[DNAJC2]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[PAAF1]] | -0.55 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[ACOX3]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[COMMD5]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[L3MBTL2]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SLC30A6]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TTF1]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[WAPL]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TTC4]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[VPS33A]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPCT]] | B | QPCT activity raises TMSB4X's level | lines that do not express QPCT (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without QPCT | 0.046 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |
| [[IGFBP7]] | B | IGFBP7 activity raises TMSB4X's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 1.38× lower at baseline in the lines without IGFBP7 | 0.063 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Sodium Salicylate (drug)]] 5 µM | B | TMSB4X activity lowers the cells' numbers under Sodium Salicylate 5 µM (makes them more sensitive) | lines that do not express TMSB4X (9) vs lines expressing it (39) | the lines without TMSB4X: 1.11× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |
| [[DNAJA3]] | B | TMSB4X activity lowers DNAJA3's level | lines that do not express TMSB4X (9) vs lines expressing it (41) | 1.37× higher at baseline in the lines without TMSB4X | 0.072 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |
| [[NSUN4]] | B | TMSB4X activity lowers NSUN4's level | lines that do not express TMSB4X (9) vs lines expressing it (41) | 1.25× higher at baseline in the lines without TMSB4X | 0.083 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |
| [[NPIPA1]] | B | TMSB4X activity lowers NPIPA1's level | lines that do not express TMSB4X (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without TMSB4X | 0.085 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |
| [[TAGLN2]] | B | TMSB4X activity raises TAGLN2's level | lines that do not express TMSB4X (9) vs lines expressing it (41) | 2.12× lower at baseline in the lines without TMSB4X | 0.092 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-40.6, -5.8); signed map (45.7, -6.0). **Vector** length 89.2, 27.2% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | +0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -4.5 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | thymosin beta 4 X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:12,975,110-12,977,227 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TB4X; previously TMSB4 |
| Gene groups (HGNC) | Thymosin beta family |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62328](https://www.uniprot.org/uniprotkb/P62328) (Thymosin beta-4):

> Plays an important role in the organization of the cytoskeleton. Binds to and sequesters actin monomers (G actin) and therefore inhibits actin polymerization.; [Hemoregulatory peptide AcSDKP]: Potent inhibitor of bone marrow derived stem cell differentiation. Acts by inhibits the entry of hematopoietic pluripotent stem cells into the S-phase (By similarity).

**Summary**, from NCBI Gene [7114](https://www.ncbi.nlm.nih.gov/gene/7114):

> This gene encodes an actin sequestering protein which plays a role in regulation of actin polymerization. The protein is also involved in cell proliferation, migration, and differentiation. This gene escapes X inactivation and has a homolog on chromosome Y. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11881) · Entrez [7114](https://www.ncbi.nlm.nih.gov/gene/7114) · UniProt [P62328](https://www.uniprot.org/uniprotkb/P62328) · Ensembl [ENSG00000205542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205542)

## Data

Gene col 12986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12986); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12986]; `tensor/DDL_lfc|DDL_z.npy` [12986]; `embed/gene_vectors.npy` [12986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12986 or target_col == 12986). Every well: [[TMSB4X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMSB4X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
