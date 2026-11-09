---
symbol: "NFIA"
type: "gene"
col: 8537
ensembl_id: "ENSG00000162599"
name: "nuclear factor I A"
location: "1p31.3"
module: 217
arm: "+"
pooled_cpm: 170.71
n_lines_expressing: 39
n_dd_up: 32
n_dd_down: 34
n_dd_up_clean: 31
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 6
direction_downstream: 23
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# NFIA

*nuclear factor I A* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.51× (z +7.9, q 1e-12, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.461× (z -21.0, q 0e+00, down in 31 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDS5B]] (+0.61, fdr 1e-05), [[NFIB]] (+0.61, fdr 7e-06), [[PDE3B]] (+0.60, fdr 9e-06); moves opposite to [[ZBTB43]] (-0.64, fdr 7e-06), [[ZNF765]] (-0.56, fdr 3e-05), [[DNTTIP1]] (-0.55, fdr 1e-05).
> It is in [[Module 217]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[WFDC10B]] → it (grade B ⚠); 23 go from it, the strongest it → [[PTPN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 3 with an alert ⚠; shown: the 15 strongest. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +7.9 | 1e-12 | 29/37 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +6.4 | 5e-08 | 17/37 (J82, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 7e-08 | 23/37 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.0 | 3e-07 | 17/37 (J82, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 5e-07 | 20/38 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +5.7 | 1e-06 | 20/37 (AsPC-1, SK-MEL-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +5.3 | 1e-05 | 20/37 (A498, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.30×** | +5.0 | 3e-05 | 19/37 (A498, SW 900, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.64×** | +5.0 | 4e-05 | 24/37 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 5e-05 | 18/37 (A498, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.27×** | +4.5 | 3e-04 | 18/37 (A498, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.5 | 3e-04 | 16/38 (J82, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.4 | 4e-04 | 22/37 (AsPC-1, A498, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.26×** | +4.4 | 4e-04 | 17/39 (A498, NCI-H596, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 8e-04 | 17/37 (A498, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.461×** | -21.0 | 0e+00 | 31/37 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.470×** | -14.5 | 6e-45 | 33/37 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.489×** | -13.7 | 1e-40 | 27/37 (LS 180, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.494×** | -13.5 | 2e-39 | 29/37 (LS 180, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.684×** | -10.3 | 8e-23 | 34/38 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -9.2 | 5e-18 | 29/37 (HCT15, SW48, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.405×** | -9.1 | 1e-17 | 31/38 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -8.8 | 9e-17 | 25/37 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -8.6 | 6e-16 | 30/37 (HepG2/C3A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.635×** | -8.4 | 3e-15 | 30/37 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.651×** | -8.2 | 9e-15 | 28/37 (LS 180, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -7.9 | 2e-13 | 25/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.671×** | -7.6 | 1e-12 | 34/37 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -7.4 | 7e-12 | 26/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.697×** | -6.9 | 2e-10 | 27/37 (HT-29, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.709×** | -6.6 | 2e-09 | 24/37 (LS 180, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.724×** | -6.2 | 2e-08 | 27/37 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 179 | 18 | 13 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.60× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -25.7) |
| [[SW48 (line)]] | wt | 273 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -26.8) |
| [[HT-29 (line)]] | alt | 344 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -17.1) |
| [[LoVo (line)]] | wt | 417 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -33.7) |
| [[PANC-1 (line)]] | alt | 243 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -26.0) |
| [[NCI-H460 (line)]] | wt | 192 | 2 | 11 (2 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.23× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -25.2) |
| [[LS 180 (line)]] | wt | 540 | 1 | 11 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -24.5) |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -29.5) |
| [[SW1417 (line)]] | alt | 460 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -16.8) |
| [[RKO (line)]] | wt | 190 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -19.9) |
| [[SW480 (line)]] | alt | 70.1 | 2 (2 ⚠) | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +11.7) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -17.3) |
| [[C-33 A (line)]] | alt | 769 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -19.8) |
| [[HEC-1-A (line)]] | alt | 149 | 3 (3 ⚠) | 4 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +12.0) ⚠ cell-cycle shift, explains ~5% of this change | [[TAK-901 (drug)]] 5 µM 0.181× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 233 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.205× (z -16.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.399× (z -13.9) |
| [[SHP-77 (line)]] | alt | 428 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -15.6) |
| [[SNU-1 (line)]] | wt | 655 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -14.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.295× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 169 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -21.7) |
| [[A549 (line)]] | wt | 134 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -18.3) |
| [[AN3 CA (line)]] | alt | 594 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.2) |
| [[KATO III (line)]] | alt | 220 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -12.5) |
| [[HCT15 (line)]] | alt | 177 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.259× (z -10.4) |
| [[J82 (line)]] | alt | 56.9 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 2.70× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 97.3 | 2 (1 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 2.30× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.350× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 89.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -20.7) |
| [[A-427 (line)]] | wt | 163 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -12.3) |
| [[C32 (line)]] | wt | 72.4 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.31× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -8.6) |
| [[H4 (line)]] | wt | 76.2 | 2 (2 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +8.9) ⚠ cell-cycle shift, explains ~7% of this change | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.3) |
| [[Hs 766T (line)]] | wt | 262 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -23.1) |
| [[Panc 03.27 (line)]] | alt | 82.7 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 1.87× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.4) |
| [[AsPC-1 (line)]] | alt | 77.3 | 1 | 1 | [[Radotinib (drug)]] 5 µM 2.39× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 58.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -16.6) |
| [[SW 900 (line)]] | alt | 71.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.2) |
| [[CHP-212 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[SW 1271 (line)]] | alt | 49.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0459× (z -9.7) |
| [[A-172 (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 37.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 33.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 365 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 36.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5B]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NFIB]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 | same gene group; pathway: RNA Polymerase III Abortive And Retractive Initiation; STRING 812 |
| [[PDE3B]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[SMAD6]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RAVER2]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PON2]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PHKA1]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PPARGC1B]] | +0.57 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[EPB41L4B]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[MBNL1]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[HADH]] | +0.57 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[MSI2]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB43]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ZNF765]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[DNTTIP1]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[DLGAP4]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[WFDC3]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ADGRL1-AS1]] | -0.54 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[NAGK]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[WFDC10B]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[STK10]] | -0.52 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NIT1]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PRMT2]] | -0.52 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[EFL1]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC10B]] | B | WFDC10B activity lowers NFIA's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 3.43× higher at baseline in the lines without WFDC10B | 0.006 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[HMGN2P46]] | B | HMGN2P46 activity lowers NFIA's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.99× higher at baseline in the lines without HMGN2P46 | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[WFDC3]] | B | WFDC3 activity lowers NFIA's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 3.09× higher at baseline in the lines without WFDC3 | 0.054 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[LUCAT1]] | B | LUCAT1 activity lowers NFIA's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 4.39× higher at baseline in the lines without LUCAT1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[TUBB6]] | B | TUBB6 activity lowers NFIA's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 3.14× higher at baseline in the lines without TUBB6 | 0.083 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[NR3C1]] | B | NR3C1 activity raises NFIA's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN4]] | B | NFIA activity raises PTPN4's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without NFIA | 0.003 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[CAMKMT]] | B | NFIA activity raises CAMKMT's level | lines that do not express NFIA (11) vs lines expressing it (39) | 2.49× lower at baseline in the lines without NFIA | 0.003 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[TTC39C]] | B | NFIA activity raises TTC39C's level | lines that do not express NFIA (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without NFIA | 0.026 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[CHPT1]] | B | NFIA activity raises CHPT1's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without NFIA | 0.027 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[USP13]] | B | NFIA activity weakens USP13's drug response | lines that do not express NFIA (11) vs lines expressing it (35) | the lines without NFIA respond 1.35× as strongly (z diff -1.14); strongest at Homoharringtonine 5 µM: 2.73x vs 1.29x (z diff -4.9) | 0.039 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NAGK]] | B | NFIA activity lowers NAGK's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.75× higher at baseline in the lines without NFIA | 0.050 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[KLF7]] | B | NFIA activity weakens KLF7's drug response | lines that do not express NFIA (9) vs lines expressing it (28) | the lines without NFIA respond 1.47× as strongly (z diff -2.32); strongest at Belinostat 5 µM: 0.34x vs 0.57x (z diff -4.2) | 0.055 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LARP1]] | B | NFIA activity strengthens LARP1's drug response | lines that do not express NFIA (11) vs lines expressing it (38) | the lines without NFIA respond 0.94× as strongly (z diff +0.78); strongest at Belinostat 5 µM: 0.78x vs 0.57x (z diff +3.8) | 0.056 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PCCB]] | B | NFIA activity raises PCCB's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without NFIA | 0.058 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[SLC5A4-AS1]] | B | NFIA activity raises SLC5A4-AS1's level | lines that do not express NFIA (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without NFIA | 0.062 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[TBC1D5]] | B | NFIA activity strengthens TBC1D5's drug response | lines that do not express NFIA (11) vs lines expressing it (37) | the lines without NFIA respond 0.76× as strongly (z diff +2.36); strongest at Ixazomib citrate 5 µM: 0.70x vs 0.49x (z diff +3.9) | 0.065 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PDE3B]] | B | NFIA activity raises PDE3B's level | lines that do not express NFIA (11) vs lines expressing it (39) | 2.78× lower at baseline in the lines without NFIA | 0.073 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.6, 39.8); signed map (28.8, -37.5). **Vector** length 137, 46.9% of its response variance represented; |z| ≥ 3 in 1,796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | -0.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.4 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | +5.3 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -6.7 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.8 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.7 | -10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -13.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.1 | -7.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.4 | -8.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -4.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor I A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:60,865,259-61,462,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NFI-L, KIAA1439 |
| Gene groups (HGNC) | Nuclear factor I family |
| Reactome | 3 pathways, smallest: RNA Polymerase III Transcription Termination; RNA Polymerase III Abortive And Retractive Initiation; RNA Polymerase III Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12857](https://www.uniprot.org/uniprotkb/Q12857) (Nuclear factor 1 A-type):

> Recognizes and binds the palindromic sequence 5'-TTGGCNNNNNGCCAA-3' present in viral and cellular promoters and in the origin of replication of adenovirus type 2. These proteins are individually capable of activating transcription and replication.

**Summary**, from NCBI Gene [4774](https://www.ncbi.nlm.nih.gov/gene/4774):

> This gene encodes a member of the NF1 (nuclear factor 1) family of transcription factors. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:7784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7784) · Entrez [4774](https://www.ncbi.nlm.nih.gov/gene/4774) · UniProt [Q12857](https://www.uniprot.org/uniprotkb/Q12857) · Ensembl [ENSG00000162599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162599)

## Data

Gene col 8537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8537); `tables/drug_effects.parquet` (88 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8537]; `tensor/DDL_lfc|DDL_z.npy` [8537]; `embed/gene_vectors.npy` [8537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8537 or target_col == 8537). Every well: [[NFIA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFIA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
