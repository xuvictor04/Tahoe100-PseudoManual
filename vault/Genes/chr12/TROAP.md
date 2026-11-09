---
symbol: "TROAP"
type: "gene"
col: 5706
ensembl_id: "ENSG00000135451"
name: "trophinin associated protein"
location: "12q13.12"
module: 22
arm: "+"
pooled_cpm: 12.06
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 27
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# TROAP

*trophinin associated protein* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.91× (z +8.7, q 2e-15, up in 27 of 38 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +5.8, q 4e-07, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.505× (z -9.9, q 2e-20, down in 31 of 46 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.573× (z -8.1, q 6e-14, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA3]] (+0.92, fdr 7e-06), [[CDCA8]] (+0.91, fdr 7e-06), [[TACC3]] (+0.91, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.91×** | +8.7 | 2e-15 | 27/38 (SW 900, NCI-H1573, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.74×** | +7.8 | 2e-12 | 14/21 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.60×** | +7.3 | 5e-11 | 25/43 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.37×** | +6.5 | 9e-09 | 23/48 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.56×** | +6.5 | 1e-08 | 20/37 (HEC-1-A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.59×** | +6.2 | 4e-08 | 17/31 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.8 | 4e-07 | 18/47 (Panc 03.27, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +5.5 | 4e-06 | 18/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 2e-05 | 15/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 5 µM |  | **1.26×** | +4.8 | 9e-05 | 13/48 (HT-29, PANC-1, …) | all doses, flat |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.6 | 3e-04 | 7/27 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.5 | 4e-04 | 15/46 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.4 | 4e-04 | 14/44 (NCI-H23, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.003 | 6/47 (HEC-1-A, HT-29, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.005 | 15/47 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.035 | 9/47 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.066 | 7/47 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.091 | 6/47 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.505×** | -9.9 | 2e-20 | 31/46 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.510×** | -9.8 | 3e-20 | 33/47 (H4, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.497×** | -9.6 | 1e-19 | 28/45 (LOX-IMVI, KATO III, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.631×** | -9.5 | 3e-19 | 28/48 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.573×** | -8.1 | 6e-14 | 28/47 (SNU-423, COLO 205, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.708×** | -7.1 | 1e-10 | 25/48 (LS 180, A549, …) | rises with dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.632×** | -6.7 | 2e-09 | 28/47 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.630×** | -6.2 | 4e-08 | 23/47 (HCT15, LoVo, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.649×** | -6.1 | 9e-08 | 21/47 (NCI-H460, SW48, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.661×** | -6.0 | 9e-08 | 20/47 (A549, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.651×** | -6.0 | 9e-08 | 21/47 (H4, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.662×** | -6.0 | 9e-08 | 23/46 (A-172, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.753×** | -5.8 | 2e-07 | 21/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.677×** | -5.2 | 8e-06 | 19/48 (RPMI-7951, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.705×** | -5.1 | 1e-05 | 17/46 (NCI-H23, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.688×** | -5.0 | 2e-05 | 21/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.545×** | -4.6 | 1e-04 | 15/43 (SW1417, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.569×** | -4.3 | 5e-04 | 14/43 (LoVo, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.728×** | -4.3 | 5e-04 | 16/47 (CHP-212, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.805×** | -4.2 | 7e-04 | 13/48 (LS 180, SNU-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.600×** | -3.9 | 0.002 | 16/44 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.853× | -3.3 | 0.026 | 10/48 (hTERT-HPNE, LS 180, …) | two highest doses |  |
| [[Methotrexate (drug)]] 0.5 µM |  | **0.802×** | -3.2 | 0.030 | 6/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.805×** | -3.1 | 0.034 | 16/47 (KATO III, A-172, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.862× | -3.0 | 0.049 | 5/48 (SHP-77, HT-29, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 10.4 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.117× (z -13.0) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.155× (z -11.2) |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0512× (z -11.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -9.4) |
| [[A549 (line)]] | wt | 10.8 | 0 | 3 (2 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.200× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.125× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW48 (line)]] | wt | 11.6 | 0 | 2 | — | [[Amsacrine (drug)]] 5 µM 0.162× (z -8.9) |
| [[A-172 (line)]] | wt | 9.31 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.106× (z -10.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-427 (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.248× (z -12.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A498 (line)]] | wt | 9.30 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.135× (z -16.3) ⚠ cell-cycle shift, explains ~75% of this change |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0747× (z -9.0) ⚠ cell-cycle shift, explains ~95% of this change |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.199× (z -12.6) ⚠ cell-cycle shift, explains ~75% of this change |
| [[KATO III (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.106× (z -8.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.310× (z -9.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 9.91 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.220× (z -8.9) |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.109× (z -9.6) |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA3]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | STRING 857 |
| [[CDCA8]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | STRING 794 |
| [[TACC3]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 701 |
| [[KIF2C]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 833 |
| [[BUB1]] | +0.91 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 729 |
| [[PIF1]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | STRING 711 |
| [[DLGAP5]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | STRING 770 |
| [[BIRC5]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 754 |
| [[CCNB2]] | +0.89 | +0.86 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 674 |
| [[CCNB1]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | STRING 626 |
| [[RACGAP1]] | +0.89 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KIF20A]] | +0.88 | +0.87 / +0.89 | both halves | 7e-06 | STRING 831 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises TROAP's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without NEURL1B | 0.026 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PIMREG]] | B | PIMREG activity raises TROAP's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without PIMREG | 0.034 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises TROAP's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without NDC80 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises TROAP's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without PBK | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises TROAP's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without AURKB | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises TROAP's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises TROAP's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises TROAP's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[TP53]] | C | TP53 activity strengthens TROAP's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.67× as strongly (z diff +0.92); strongest at Amsacrine 5 µM: 0.78x vs 0.38x (z diff +3.6) | 0.689 over the table, 0.043 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.914). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.4, -56.5); signed map (-50.2, -42.1). **Vector** length 120, 31.6% of its response variance represented; |z| ≥ 3 in 1,189 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.84 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.69 to 48); *E2F targets* (hallmark, mean cos +0.70 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | +5.1 | +8.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | +3.3 | +3.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.8 | +7.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.7 | +6.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +1.3 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -6.8 | -9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -6.1 | -9.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.3 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.1 | -9.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.0 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | trophinin associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,323,236-49,331,731 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TASTIN |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12815](https://www.uniprot.org/uniprotkb/Q12815) (Tastin):

> Could be involved with bystin and trophinin in a cell adhesion molecule complex that mediates an initial attachment of the blastocyst to uterine epithelial cells at the time of the embryo implantation.

**Summary**, from NCBI Gene [10024](https://www.ncbi.nlm.nih.gov/gene/10024):

> Predicted to be involved in cell adhesion. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12327) · Entrez [10024](https://www.ncbi.nlm.nih.gov/gene/10024) · UniProt [Q12815](https://www.uniprot.org/uniprotkb/Q12815) · Ensembl [ENSG00000135451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135451)

## Data

Gene col 5706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5706); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5706]; `tensor/DDL_lfc|DDL_z.npy` [5706]; `embed/gene_vectors.npy` [5706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5706 or target_col == 5706). Every well: [[TROAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TROAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
