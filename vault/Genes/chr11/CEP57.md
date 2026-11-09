---
symbol: "CEP57"
type: "gene"
col: 9230
ensembl_id: "ENSG00000166037"
name: "centrosomal protein 57"
location: "11q21"
module: 130
arm: "+"
pooled_cpm: 108.23
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# CEP57

*centrosomal protein 57* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +12.3, q 4e-32, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.636× (z -10.9, q 7e-25, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.736× (z -7.4, q 3e-11, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSD3]] (+0.67, fdr 7e-06), [[ZNF451]] (+0.67, fdr 1e-05), [[ARID4A]] (+0.66, fdr 7e-06); moves opposite to [[RRP7BP]] (-0.58, fdr 2e-05), [[ALDH1B1]] (-0.58, fdr 1e-05), [[POLR3H]] (-0.56, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +12.3 | 4e-32 | 39/49 (SW1417, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +7.1 | 4e-10 | 32/48 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.21×** | +6.6 | 8e-09 | 26/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +5.8 | 9e-07 | 28/48 (NCI-H2030, KATO III, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.6 | 3e-06 | 27/50 (Panc 03.27, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.14× | +4.7 | 3e-04 | 14/48 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.6 | 3e-04 | 20/44 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +3.8 | 0.012 | 24/47 (RKO, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.7 | 0.016 | 7/48 (HT-29, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.025 | 18/49 (RKO, HEC-1-A, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.026 | 20/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.030 | 13/49 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.10× | +3.3 | 0.038 | 6/49 (BT-474, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.078 | 15/48 (KATO III, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.087 | 12/48 (SW480, SW48, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.087 | 7/48 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.636×** | -10.9 | 7e-25 | 46/48 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -8.4 | 1e-14 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.736×** | -7.4 | 3e-11 | 33/48 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.736×** | -7.4 | 3e-11 | 37/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.761×** | -6.2 | 7e-08 | 34/47 (SW48, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -6.0 | 2e-07 | 20/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.633×** | -5.8 | 7e-07 | 35/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.795×** | -5.5 | 3e-06 | 26/48 (A-427, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.805×** | -5.0 | 3e-05 | 22/47 (RKO, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.875× | -4.5 | 4e-04 | 17/48 (A498, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.833×** | -4.4 | 6e-04 | 22/48 (SW480, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -4.2 | 0.001 | 22/48 (SNU-1, AsPC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.719×** | -4.1 | 0.001 | 25/48 (Hs 766T, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.853× | -3.8 | 0.005 | 19/48 (C-33 A, HOP62, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.740×** | -3.8 | 0.005 | 21/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.005 | 19/48 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.814×** | -3.5 | 0.012 | 16/48 (NCI-H1792, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.908× | -3.2 | 0.031 | 12/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.032 | 20/48 (A-427, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.876× | -3.2 | 0.037 | 7/48 (SW480, KATO III, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.780×** | -3.1 | 0.040 | 18/48 (SW 900, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 155 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +14.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.589× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A-427 (line)]] | wt | 143 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +13.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.513× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 111 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.3) ⚠ cell-cycle shift, explains ~57% of this change | [[Panobinostat (drug)]] 0.5 µM 0.561× (z -9.1) |
| [[HT-29 (line)]] | alt | 156 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.435× (z -9.6) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 111 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.9) | [[AZD2858 (drug)]] 0.5 µM 0.403× (z -9.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 73.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.2) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[Hs 766T (line)]] | wt | 144 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.505× (z -9.0) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 84.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.9) ⚠ cell-cycle shift, explains ~57% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.327× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 124 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +15.1) | — |
| [[SW48 (line)]] | wt | 100 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 195 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.607× (z -9.4) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.614× (z -9.1) |
| [[A-172 (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.0) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[A498 (line)]] | wt | 82.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.629× (z -9.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A549 (line)]] | wt | 71.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.1) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[BT-474 (line)]] | alt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.5) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[CFPAC-1 (line)]] | alt | 96.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.503× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.131× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[HCT15 (line)]] | alt | 178 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -9.5) |
| [[HOP62 (line)]] | alt | 96.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.294× (z -8.5) ⚠ toxic |
| [[J82 (line)]] | alt | 79.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 123 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.4) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.349× (z -13.5) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.1) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H23 (line)]] | alt | 88.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.0) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H2347 (line)]] | alt | 87.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 114 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 86.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.461× (z -10.4) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 138 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 231 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 98.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 246 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSD3]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ZNF451]] | +0.67 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.66 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[UBN2]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CDK19]] | +0.65 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[CDKN1B]] | +0.62 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[CEP44]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZC3H6]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[GPATCH1]] | +0.60 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PCM1]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[KMT2A]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[KLHDC2]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ALDH1B1]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[POLR3H]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[YWHAG]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 | pathway: AURKA Activation by TPX2 |
| [[PINX1-1]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NME1]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CYRIB]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[WDR77]] | -0.55 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[C3orf52]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | -0.54 | -0.38 / -0.62 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA3 activity raises CEP57's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without HOXA3 | 0.098 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[ALDH1B1]] | C | ALDH1B1 activity raises CEP57's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 1.37× lower at baseline in the lines without ALDH1B1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.1, -48.6); signed map (-12.5, 8.0). **Vector** length 138, 42.0% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.4 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +12.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.1 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.2 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.6 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.1 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.6 | -10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -7.4 |
|  | [[EX229 (drug)]] 5 µM |  | -5.6 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.2 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 57 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:95,789,965-95,832,693 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Translokin, TSP57, KIAA0092 |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XR8](https://www.uniprot.org/uniprotkb/Q86XR8) (Centrosomal protein of 57 kDa):

> Centrosomal protein which may be required for microtubule attachment to centrosomes. May act by forming ring-like structures around microtubules. Mediates nuclear translocation and mitogenic activity of the internalized growth factor FGF2, but that of FGF1.

**Summary**, from NCBI Gene [9702](https://www.ncbi.nlm.nih.gov/gene/9702):

> This gene encodes a cytoplasmic protein called Translokin. This protein localizes to the centrosome and has a function in microtubular stabilization. The N-terminal half of this protein is required for its centrosome localization and for its multimerization, and the C-terminal half is required for nucleating, bundling and anchoring microtubules to the centrosomes. This protein specifically interacts with fibroblast growth factor 2 (FGF2), sorting nexin 6, Ran-binding protein M and the kinesins …

**Accessions** — [HGNC:30794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30794) · Entrez [9702](https://www.ncbi.nlm.nih.gov/gene/9702) · UniProt [Q86XR8](https://www.uniprot.org/uniprotkb/Q86XR8) · Ensembl [ENSG00000166037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166037)

## Data

Gene col 9230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9230); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9230]; `tensor/DDL_lfc|DDL_z.npy` [9230]; `embed/gene_vectors.npy` [9230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9230 or target_col == 9230). Every well: [[CEP57 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP57.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
