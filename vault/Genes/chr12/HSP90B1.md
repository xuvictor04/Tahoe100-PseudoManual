---
symbol: "HSP90B1"
type: "gene"
col: 9338
ensembl_id: "ENSG00000166598"
name: "heat shock protein 90 beta family member 1"
location: "12q23.3"
module: 42
arm: "+"
pooled_cpm: 1376.54
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# HSP90B1

*heat shock protein 90 beta family member 1* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.08× (z +8.6, q 5e-15, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.426× (z -14.2, q 1e-42, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA4]] (+0.92, fdr 7e-06), [[HSPA5]] (+0.88, fdr 7e-06), [[CALR]] (+0.86, fdr 7e-06); moves opposite to [[TRIM47]] (-0.63, fdr 1e-05), [[ITPA]] (-0.62, fdr 1e-05), [[ST7L]] (-0.61, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +8.6 | 5e-15 | 47/48 (H4, HS-578T, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.98×** | +7.4 | 3e-11 | 45/49 (A-427, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.89×** | +7.2 | 1e-10 | 40/44 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +6.4 | 3e-08 | 44/48 (HT-29, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.66×** | +5.9 | 3e-07 | 42/48 (SK-MEL-2, HS-578T, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.61×** | +5.6 | 2e-06 | 44/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.4 | 4e-06 | 36/49 (Panc 03.27, AsPC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.50×** | +4.4 | 7e-04 | 33/45 (A-427, A549, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.4 | 8e-04 | 0/50 | inconsistent across doses |  |
| [[Lipoic acid (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.063 | 24/48 (PANC-1, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.070 | 26/48 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.30× | +3.1 | 0.10 | 30/48 (AsPC-1, J82, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.426×** | -14.2 | 1e-42 | 43/48 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.465×** | -9.0 | 9e-17 | 41/48 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -7.5 | 1e-11 | 42/48 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.589×** | -6.2 | 8e-08 | 42/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -5.3 | 1e-05 | 40/48 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.755×** | -4.7 | 3e-04 | 34/48 (NCI-H2030, A-427, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.654×** | -4.6 | 3e-04 | 44/48 (CFPAC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.725×** | -3.8 | 0.012 | 36/48 (KATO III, SW48, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.558×** | -3.6 | 0.023 | 41/49 (J82, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.047 | 33/48 (C32, RPMI-7951, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.047 | 34/49 (H4, HepG2/C3A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.746×** | -3.3 | 0.047 | 36/47 (NCI-H2030, SW48, …) | rises with dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.2 | 0.065 | 23/48 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.764×** | -3.2 | 0.065 | 30/48 (HT-29, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 1,067 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -21.9) |
| [[A-172 (line)]] | wt | 1,386 | 1 | 5 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -16.9) |
| [[H4 (line)]] | wt | 2,330 | 2 (1 ⚠) | 4 | [[Panobinostat (drug)]] 0.5 µM 3.62× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -26.5) |
| [[KATO III (line)]] | alt | 2,149 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -24.2) |
| [[C-33 A (line)]] | alt | 739 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 2,659 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -17.0) |
| [[SHP-77 (line)]] | alt | 969 | 3 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.33× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -17.6) |
| [[A498 (line)]] | wt | 1,246 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 861 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 2,282 | 2 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 3.74× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -14.5) |
| [[SW 1271 (line)]] | alt | 1,301 | 3 | 1 | [[Pasireotide (acetate) (drug)]] 5 µM 2.78× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -8.6) |
| [[SW480 (line)]] | alt | 769 | 3 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.48× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -12.3) |
| [[A549 (line)]] | wt | 797 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.75× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 1,780 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -11.6) |
| [[CHP-212 (line)]] | wt | 984 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.6) |
| [[HCT15 (line)]] | alt | 2,235 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.8) |
| [[HepG2_C3A (line)]] | wt | 1,370 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -16.8) |
| [[J82 (line)]] | alt | 1,497 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 968 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.35× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 1,095 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 1,360 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -22.2) |
| [[SK-MEL-2 (line)]] | alt | 942 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 1,055 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -9.0) |
| [[HOP62 (line)]] | alt | 1,760 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.46× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.3) |
| [[HT-29 (line)]] | alt | 1,494 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.57× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 1,962 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -14.0) |
| [[NCI-H661 (line)]] | alt | 1,322 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 917 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.6) | — |
| [[RKO (line)]] | wt | 1,224 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -17.1) |
| [[SNU-1 (line)]] | wt | 1,194 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -15.2) |
| [[SW 900 (line)]] | alt | 1,793 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -13.6) |
| [[SW48 (line)]] | wt | 1,351 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.0) |
| [[AN3 CA (line)]] | alt | 1,034 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[BT-474 (line)]] | alt | 610 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.42× (z +8.7) | — |
| [[C32 (line)]] | wt | 1,099 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 1,022 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 1,687 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.4) |
| [[LoVo (line)]] | wt | 1,510 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.378× (z -8.6) |
| [[LS 180 (line)]] | wt | 2,009 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 1,340 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.01× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 1,690 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 1,235 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.6) |
| [[PANC-1 (line)]] | alt | 1,115 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +9.0) | — |
| [[SW 1088 (line)]] | alt | 2,255 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -14.5) |
| [[SW1417 (line)]] | alt | 835 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.09× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 1,177 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 901 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1,613 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1,342 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,319 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA4]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | STRING 998 |
| [[HSPA5]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[CALR]] | +0.86 | +0.86 / +0.81 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[P4HB]] | +0.85 | +0.87 / +0.79 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 983 |
| [[LMAN1]] | +0.83 | +0.85 / +0.76 | both halves | 7e-06 | STRING 581 |
| [[PDIA6]] | +0.82 | +0.83 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 990 |
| [[TMED9]] | +0.78 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[CALU]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 773 |
| [[DNAJC3]] | +0.76 | +0.74 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 927 |
| [[HYOU1]] | +0.76 | +0.76 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 999 |
| [[MANF]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | STRING 831 |
| [[SEL1L]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 | STRING 833 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.63 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ITPA]] | -0.62 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ST7L]] | -0.61 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[ZNF480]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[ZSCAN29]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SLC9A8]] | -0.60 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[MIER3]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[MTPAP]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.60 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H7B]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TRIP6]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 | same gene group |
| [[TRMT5]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers HSP90B1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers HSP90B1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, -30.9); signed map (-54.2, 7.5). **Vector** length 159, 65.8% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.52 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.70 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.69 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.9 | +8.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +8.5 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.1 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -13.5 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -11.8 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.0 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.1 | -6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -9.0 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.1 | -2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.6 | -1.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.5 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein 90 beta family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:103,930,107-103,953,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GP96, GRP94; previously TRA1 |
| Gene groups (HGNC) | Heat shock 90kDa proteins; MicroRNA protein coding host genes |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 16 pathways, smallest: ATF6 (ATF6-alpha) activates chaperone genes; Trafficking and processing of endosomal TLR; ATF6 (ATF6-alpha) activates chaperones |
| Matched by | ensembl_id |

**Function**, from UniProt [P14625](https://www.uniprot.org/uniprotkb/P14625) (Endoplasmin):

> ATP-dependent chaperone involved in the processing of proteins in the endoplasmic reticulum, regulating their transport. Together with MESD, acts as a modulator of the Wnt pathway by promoting the folding of LRP6, a coreceptor of the canonical Wnt pathway. When associated with CNPY3, required for proper folding of Toll-like receptors. Promotes folding and trafficking of TLR4 to the cell surface. May participate in the unfolding of cytosolic leaderless cargos (lacking the secretion signal …

**Summary**, from NCBI Gene [7184](https://www.ncbi.nlm.nih.gov/gene/7184):

> This gene encodes a member of a family of adenosine triphosphate(ATP)-metabolizing molecular chaperones with roles in stabilizing and folding other proteins. The encoded protein is localized to melanosomes and the endoplasmic reticulum. Expression of this protein is associated with a variety of pathogenic states, including tumor formation. There is a microRNA gene located within the 5' exon of this gene. There are pseudogenes for this gene on chromosomes 1 and 15. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:12028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12028) · Entrez [7184](https://www.ncbi.nlm.nih.gov/gene/7184) · UniProt [P14625](https://www.uniprot.org/uniprotkb/P14625) · Ensembl [ENSG00000166598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166598)

## Data

Gene col 9338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9338); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9338]; `tensor/DDL_lfc|DDL_z.npy` [9338]; `embed/gene_vectors.npy` [9338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9338 or target_col == 9338). Every well: [[HSP90B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSP90B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
