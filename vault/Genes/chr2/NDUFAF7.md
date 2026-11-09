---
symbol: "NDUFAF7"
type: "gene"
col: 36
ensembl_id: "ENSG00000003509"
name: "NADH:ubiquinone oxidoreductase complex assembly factor 7"
location: "2p22.2"
module: 30
arm: "+"
pooled_cpm: 39.18
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# NDUFAF7

*NADH:ubiquinone oxidoreductase complex assembly factor 7* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.72× (z +10.2, q 2e-21, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -12.2, q 1e-31, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB7]] (+0.78, fdr 7e-06), [[CDADC1]] (+0.74, fdr 7e-06), [[RNF149]] (+0.74, fdr 7e-06); moves opposite to [[VEZF1]] (-0.74, fdr 7e-06), [[SKIL]] (-0.73, fdr 7e-06), [[NAB1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SEMA3C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 36.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +10.2 | 2e-21 | 44/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.9 | 1e-20 | 34/48 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +8.4 | 9e-15 | 34/48 (A-427, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +7.7 | 1e-12 | 36/48 (LOX-IMVI, A-427, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +6.2 | 5e-08 | 32/48 (SW480, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.2 | 5e-08 | 23/47 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +5.1 | 2e-05 | 28/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +5.0 | 4e-05 | 26/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 6e-04 | 18/48 (A-427, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +4.3 | 9e-04 | 20/49 (KATO III, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.8 | 0.009 | 20/47 (C-33 A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +3.6 | 0.015 | 16/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.5 | 0.018 | 14/43 (NCI-H1792, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.20×** | +3.5 | 0.021 | 16/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.023 | 9/48 (MIA PaCa-2, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.025 | 13/48 (LS 180, LoVo, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.028 | 8/48 (AsPC-1, SNU-1, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.041 | 8/48 (SW1417, AsPC-1, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.2 | 0.042 | 10/48 (AsPC-1, HOP62, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.073 | 12/47 (HT-29, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +2.9 | 0.096 | 8/48 (NCI-H1573, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 36.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -12.2 | 1e-31 | 38/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.558×** | -10.4 | 5e-23 | 43/48 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.584×** | -9.6 | 1e-19 | 27/41 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.600×** | -9.5 | 3e-19 | 34/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -7.2 | 7e-11 | 36/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.744×** | -5.1 | 3e-05 | 22/44 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.761×** | -5.1 | 3e-05 | 28/48 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.784×** | -4.5 | 5e-04 | 17/47 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.800×** | -4.1 | 0.002 | 21/48 (SW 1088, NCI-H2347, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.820×** | -3.7 | 0.014 | 18/48 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.823×** | -3.6 | 0.016 | 11/48 (HEC-1-A, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -3.2 | 0.060 | 13/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.090 | 10/48 (SW1417, A498, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.847× | -3.1 | 0.090 | 13/48 (HOP62, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 36. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 47.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.416× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.482× (z -10.1) |
| [[PANC-1 (line)]] | alt | 39.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -16.0) |
| [[C-33 A (line)]] | alt | 42.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -12.2) |
| [[SHP-77 (line)]] | alt | 63.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 53.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -14.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 69.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +9.2) | — |
| [[A498 (line)]] | wt | 40.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -9.4) |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0503× (z -12.5) |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -9.0) |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 1 | — | [[AZD1390 (drug)]] 5 µM 0.0570× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.6) |
| [[LoVo (line)]] | wt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -22.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 35.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.308× (z -8.9) |
| [[RKO (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.2) |
| [[SNU-423 (line)]] | alt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.1) |
| [[A-172 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 36), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[CDADC1]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[RNF149]] | +0.74 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[NENF]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[MED17]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.73 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[NUP54]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PPHLN1]] | +0.73 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TAF11]] | +0.72 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[DHRS1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | -0.74 | -0.69 / -0.73 | both halves | 7e-06 |  |
| [[SKIL]] | -0.73 | -0.74 / -0.70 | both halves | 7e-06 |  |
| [[NAB1]] | -0.68 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[MYO1C]] | -0.68 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[MIS12]] | -0.67 | -0.63 / -0.72 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.66 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[PHF19]] | -0.65 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.65 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[THOC6]] | -0.65 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[LIG4]] | -0.64 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[PBRM1]] | -0.63 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[ZBTB38]] | -0.63 | -0.65 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3C]] | B | SEMA3C activity lowers NDUFAF7's level | lines that do not express SEMA3C (8) vs lines expressing it (42) | 1.24× higher at baseline in the lines without SEMA3C | 0.022 | ⚠ within organs, on part of the lines; also absent: IKZF2, ANTXR2 |
| [[MICE]] | B | MICE activity lowers NDUFAF7's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.22× higher at baseline in the lines without MICE | 0.026 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[HOXB5]], [[HOXB6]] | B | HOXB5, HOXB6 activity lowers NDUFAF7's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.12× higher at baseline in the lines without HOXB5, HOXB6 | 0.060 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[FAR2P1]] | B | FAR2P1 activity raises NDUFAF7's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.13× lower at baseline in the lines without FAR2P1 | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-2.7, -13.9); signed map (-35.3, -8.6). **Vector** length 115, 29.8% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.9 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +10.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.2 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.1 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +4.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.7 | -10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.9 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -9.1 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -5.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -4.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -3.7 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase complex assembly factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,231,631-37,253,403 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRO1853, MidA; previously C2orf56 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; 7BS protein arginine methyltranferases; Arginine methyltransferases |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L592](https://www.uniprot.org/uniprotkb/Q7L592) (Protein arginine methyltransferase NDUFAF7, mitochondrial):

> Arginine methyltransferase involved in the assembly or stability of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I). Acts by mediating symmetric dimethylation of 'Arg-118' of NDUFS2 after it assembles into the complex I, stabilizing the early intermediate complex.

**Summary**, from NCBI Gene [55471](https://www.ncbi.nlm.nih.gov/gene/55471):

> This gene encodes an assembly factor protein which helps in the assembly and stabilization of Complex I, a large multi-subunit enzyme in the mitochondrial respiratory chain. Complex I is involved in several physiological activities in the cell, including metabolite transport and ATP synthesis. The encoded protein is a methyltransferase which methylates Arg85 of a subunit of Complex I in the early stages of its assembly. A pseudogene related to this gene is located on chromosome 8. Alternative …

**Accessions** — [HGNC:28816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28816) · Entrez [55471](https://www.ncbi.nlm.nih.gov/gene/55471) · UniProt [Q7L592](https://www.uniprot.org/uniprotkb/Q7L592) · Ensembl [ENSG00000003509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003509)

## Data

Gene col 36: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 36); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 36, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 36]; `tensor/DDL_lfc|DDL_z.npy` [36]; `embed/gene_vectors.npy` [36]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 36 or target_col == 36). Every well: [[NDUFAF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
