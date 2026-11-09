---
symbol: "MAN2B2"
type: "gene"
col: 266
ensembl_id: "ENSG00000013288"
name: "mannosidase alpha class 2B member 2"
location: "4p16.1"
module: 50
arm: "+"
pooled_cpm: 17.87
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# MAN2B2

*mannosidase alpha class 2B member 2* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.84× (z +19.3, q 0e+00, up in 25 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.03× (z +13.6, q 7e-40, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.471× (z -20.4, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLBD2]] (+0.77, fdr 7e-06), [[SBF1]] (+0.74, fdr 7e-06), [[GLB1]] (+0.73, fdr 7e-06); moves opposite to [[MRPS18B]] (-0.65, fdr 1e-05), [[FOXA2]] (-0.65, fdr 1e-05), [[CEBPZ]] (-0.60, fdr 2e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +19.3 | 0e+00 | 25/29 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +15.4 | 0e+00 | 35/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +13.6 | 7e-40 | 39/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +11.0 | 5e-26 | 28/35 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +10.5 | 1e-23 | 37/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +8.9 | 7e-17 | 26/47 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.6 | 4e-09 | 23/46 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.1 | 3e-05 | 15/48 (A-427, RKO, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.20× | +5.0 | 4e-05 | 15/47 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.002 | 12/46 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | 1.20× | +3.4 | 0.037 | 11/43 (NCI-H2030, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.037 | 8/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.047 | 11/44 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.18× | +3.0 | 0.090 | 10/48 (LS 180, NCI-H2030, …) | top dose only | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.090 | 2/47 (SHP-77, MIA PaCa-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.471×** | -20.4 | 0e+00 | 38/47 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.473×** | -14.3 | 5e-44 | 36/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.540×** | -11.3 | 1e-27 | 35/47 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -9.6 | 2e-19 | 35/48 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -7.8 | 7e-13 | 8/48 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.669×** | -7.7 | 2e-12 | 28/48 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -6.7 | 1e-09 | 29/45 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.724×** | -6.1 | 6e-08 | 22/47 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.717×** | -6.1 | 7e-08 | 22/47 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -5.8 | 4e-07 | 21/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.776×** | -4.8 | 8e-05 | 16/47 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.004 | 15/46 (NCI-H2030, SW1417, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.676×** | -3.9 | 0.004 | 11/45 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.826×** | -3.6 | 0.012 | 13/47 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | **0.825×** | -3.5 | 0.017 | 13/44 (H4, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.822×** | -3.4 | 0.019 | 12/46 (RKO, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.834× | -3.4 | 0.019 | 13/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -3.4 | 0.021 | 10/48 (SW 1271, RKO, …) | all doses, flat |  |
| [[Penfluridol (drug)]] 5 µM |  | 0.847× | -3.0 | 0.076 | 13/47 (hTERT-HPNE, HS-578T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.8) |
| [[KATO III (line)]] | alt | 22.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.9) |
| [[SW480 (line)]] | alt | 15.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.208× (z -13.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.2) |
| [[A498 (line)]] | wt | 15.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 27.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.7) |
| [[HOP62 (line)]] | alt | 18.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.5) |
| [[J82 (line)]] | alt | 28.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 10.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.210× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 9.10 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.2) |
| [[A-427 (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -9.0) |
| [[A549 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.67× (z +11.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0679× (z -10.8) |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.4) |
| [[LoVo (line)]] | wt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -9.6) |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -9.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.1) |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -10.7) |
| [[SW48 (line)]] | wt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -9.6) |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLBD2]] | +0.77 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[SBF1]] | +0.74 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[GLB1]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives; STRING 434 |
| [[NAGA]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[CAPN1]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SELENON]] | +0.70 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[LLGL1]] | +0.69 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[NUCB1]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[UFD1]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[RAB5C]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18B]] | -0.65 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.65 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[TRIP11]] | -0.60 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ZNF155]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[PIGBOS1]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[EID2]] | -0.57 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[SCAF11]] | -0.57 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[MPLKIP]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[HELQ]] | -0.56 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MAN2B2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers MAN2B2's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[NSRP1]] | C | NSRP1's natural level strengthens MAN2B2's drug response | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.52; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.4, -21.9); signed map (-46.8, -11.0). **Vector** length 79.0, 14.8% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.52 to 12); *Glycosphingolipid catabolism* (reactome, mean cos +0.51 to 5); *Degradation of the extracellular matrix* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +13.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -20.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -14.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 2B member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:6,575,189-6,623,362 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0935, EpMAN |
| Gene groups (HGNC) | Mannosidases alpha class 2 |
| Reactome | 2 pathways, smallest: Lysosomal oligosaccharide catabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2E5](https://www.uniprot.org/uniprotkb/Q9Y2E5) (Epididymis-specific alpha-mannosidase):

> Specifically cleaves terminal alpha 1,6-linked mannose residues on Man3GlcNAc and Man2GlcNAc core oligosaccharides generated by N-glycan degradation pathways, having little activity, if any, on larger mannose oligosaccharides. Does not cleave terminal alpha 1,6-linked mannose on Man3GlcNAc2, and is also unable to hydrolyze terminal alpha 1,3-mannose linkages.

**Summary**, from NCBI Gene [23324](https://www.ncbi.nlm.nih.gov/gene/23324):

> Enables mannan endo-1,6-alpha-mannosidase activity and mannosyl-oligosaccharide 1,6-alpha-mannosidase activity. Involved in glycoprotein catabolic process and oligosaccharide catabolic process. Located in extracellular exosome. Is active in lysosomal lumen. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29623) · Entrez [23324](https://www.ncbi.nlm.nih.gov/gene/23324) · UniProt [Q9Y2E5](https://www.uniprot.org/uniprotkb/Q9Y2E5) · Ensembl [ENSG00000013288](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013288)

## Data

Gene col 266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 266); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 266]; `tensor/DDL_lfc|DDL_z.npy` [266]; `embed/gene_vectors.npy` [266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 266 or target_col == 266). Every well: [[MAN2B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN2B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
