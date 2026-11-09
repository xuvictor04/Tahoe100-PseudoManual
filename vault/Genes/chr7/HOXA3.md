---
symbol: "HOXA3"
type: "gene"
col: 2701
ensembl_id: "ENSG00000105997"
name: "homeobox A3"
location: "7p15.2"
module: 201
arm: "+"
pooled_cpm: 30.58
n_lines_expressing: 41
n_dd_up: 10
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 6
direction_downstream: 11
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXA3

*homeobox A3* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +12.7, q 4e-34, up in 24 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.418× (z -16.8, q 0e+00, down in 35 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA6]] (+0.73, fdr 7e-06, ⚠ read-through risk), [[HOXA5]] (+0.70, fdr 7e-06, ⚠ same locus), [[HOXB3]] (+0.69, fdr 1e-05), [[HOXB5]] (+0.66, fdr 1e-05), [[HOXB6]] (+0.65, fdr 1e-05); moves opposite to [[MICAL2]] (-0.70, fdr 7e-06), [[RABGAP1L]] (-0.61, fdr 2e-05), [[UBE2E2]] (-0.58, fdr 2e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HOXA10]] → it (grade B ⚠); 11 go from it, the strongest it → [[HOXA-AS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +12.7 | 4e-34 | 24/37 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +7.8 | 2e-12 | 24/38 (A498, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 2e-04 | 11/38 (PANC-1, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +4.8 | 3e-04 | 10/39 (PANC-1, LoVo, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.17× | +4.2 | 0.003 | 12/39 (NCI-H1792, A498, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.003 | 14/38 (SW1417, LoVo, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.003 | 7/35 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.004 | 13/37 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.007 | 8/37 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.008 | 7/37 (HEC-1-A, A498, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.008 | 11/39 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.020 | 15/37 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.029 | 11/39 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tazarotene (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.029 | 7/38 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.3 | 0.039 | 6/38 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.18× | +3.1 | 0.065 | 7/38 (A549, RPMI-7951, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.418×** | -16.8 | 0e+00 | 35/38 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.499×** | -13.4 | 3e-38 | 30/38 (HT-29, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.555×** | -11.3 | 2e-27 | 27/38 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -10.0 | 3e-21 | 28/38 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.705×** | -9.5 | 2e-19 | 21/39 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.621×** | -8.8 | 1e-16 | 23/38 (AN3 CA, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.635×** | -8.7 | 2e-16 | 28/38 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.644×** | -8.1 | 3e-14 | 26/37 (SNU-423, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.668×** | -7.3 | 2e-11 | 25/37 (HT-29, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.694×** | -7.0 | 1e-10 | 23/37 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.703×** | -6.8 | 7e-10 | 20/38 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.695×** | -6.7 | 8e-10 | 21/39 (A498, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -6.6 | 2e-09 | 19/36 (C32, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -6.3 | 9e-09 | 20/38 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.723×** | -6.2 | 2e-08 | 18/38 (HT-29, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.743×** | -5.7 | 4e-07 | 14/38 (SW 900, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.752×** | -5.5 | 1e-06 | 19/37 (HT-29, SW 900, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.580×** | -5.5 | 1e-06 | 18/37 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.764×** | -5.0 | 2e-05 | 19/37 (C32, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.780×** | -4.8 | 5e-05 | 17/38 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -19.6) |
| [[HT-29 (line)]] | alt | 102 | 1 | 9 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.117× (z -17.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.167× (z -14.8) |
| [[C32 (line)]] | wt | 49.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -21.5) |
| [[AN3 CA (line)]] | alt | 243 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0255× (z -21.4) |
| [[SW 900 (line)]] | alt | 46.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0673× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.116× (z -16.5) |
| [[HCT15 (line)]] | alt | 83.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0883× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.199× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 37.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0974× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 37.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.0) |
| [[SW480 (line)]] | alt | 32.9 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 33.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 82.2 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -19.2) |
| [[LoVo (line)]] | wt | 65.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.6) |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.4) |
| [[LS 180 (line)]] | wt | 51.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.5) | — |
| [[A498 (line)]] | wt | 50.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -10.7) |
| [[A549 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.145× (z -9.5) |
| [[Hs 766T (line)]] | wt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 9.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.189× (z -9.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 21.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.371× (z -9.8) |
| [[SW48 (line)]] | wt | 42.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +8.6) | — |
| [[A-172 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA6]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 | same gene group; STRING 707; ⚠ **readthrough risk**: HOXA6 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[HOXA5]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 | same gene group; STRING 805; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB3]] | +0.69 | +0.55 / +0.65 | both halves | 1e-05 | same gene group; pathway: Activation of HOX genes during differentiation; STRING 412 |
| [[HOXB5]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 | same gene group; STRING 400 |
| [[HOXB6]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 | same gene group; STRING 465 |
| [[LINC00938]] | +0.63 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[HOXA-AS2]] | +0.63 | +0.49 / +0.60 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HOXA10]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 | same gene group; STRING 732; ⚠ same locus (18.0 kb, same strand: neighbours can correlate without regulation) |
| [[MBIP]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[HOXB-AS3]] | +0.61 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[RPRD2]] | +0.61 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TAPT1]] | +0.60 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[HNMT]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ACP6]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[ACBD5]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.57 | +0.31 / +0.59 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICAL2]] | -0.70 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RABGAP1L]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[UBE2E2]] | -0.58 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[PITPNB]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[R3HDM4]] | -0.57 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[RRP7A]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SOWAHC]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SACS]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[MIR222HG]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SUPT3H]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TMEM241]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[EIF6]] | -0.53 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA10]] | B | HOXA10 activity raises HOXA3's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without HOXA10 | 0.011 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11 |
| [[HOXA11]] | B | HOXA11 activity raises HOXA3's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 2.97× lower at baseline in the lines without HOXA11 | 0.022 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3 |
| [[HOXA9]] | B | HOXA9 activity raises HOXA3's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 2.86× lower at baseline in the lines without HOXA9 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[HOXA6]] | C | HOXA6 activity raises HOXA3's level | lines that do not express HOXA6 (13) vs lines expressing it (37) | 3.53× lower at baseline in the lines without HOXA6 | 0.001 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA5; maybe low, not absent; co-absent with the target |
| [[HOXA5]] | C | HOXA5 activity raises HOXA3's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 3.62× lower at baseline in the lines without HOXA5 | 0.029 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1; co-absent with the target |
| [[HOXA-AS2]] | C | HOXA-AS2 activity raises HOXA3's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 5.06× lower at baseline in the lines without HOXA-AS2 | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA-AS2]] | B | HOXA3 activity raises HOXA-AS2's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 2.11× lower at baseline in the lines without HOXA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[KLC4]] | B | HOXA3 activity raises KLC4's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.34× lower at baseline in the lines without HOXA3 | 0.051 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[HOXA10]] | B | HOXA3 activity raises HOXA10's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 2.50× lower at baseline in the lines without HOXA3 | 0.052 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[MAP3K2]] | B | HOXA3 activity raises MAP3K2's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.23× lower at baseline in the lines without HOXA3 | 0.056 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[RRP7A]] | B | HOXA3 activity lowers RRP7A's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.21× higher at baseline in the lines without HOXA3 | 0.058 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[HOXA11]] | B | HOXA3 activity raises HOXA11's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 2.17× lower at baseline in the lines without HOXA3 | 0.068 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[HOXC9]] | B | HOXA3 activity raises HOXC9's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.92× lower at baseline in the lines without HOXA3 | 0.078 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[RHOXF1]] | B | HOXA3 activity raises RHOXF1's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without HOXA3 | 0.083 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[CEP57]] | B | HOXA3 activity raises CEP57's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without HOXA3 | 0.098 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[HOXA6]] | C | HOXA3 activity raises HOXA6's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 2.51× lower at baseline in the lines without HOXA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent; co-absent with the target |
| [[HOXA5]] | C | HOXA3 activity raises HOXA5's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 3.17× lower at baseline in the lines without HOXA3 | 0.007 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.837). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.8, 27.2); signed map (-5.2, 6.7). **Vector** length 95.6, 21.7% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Kidney development* (reactome, mean cos +0.57 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +12.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +3.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -16.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.5 | -13.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -8.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | homeobox A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,106,184-27,152,583 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX1E, HOX1 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 2 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43365](https://www.uniprot.org/uniprotkb/O43365) (Homeobox protein Hox-A3):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3200](https://www.ncbi.nlm.nih.gov/gene/3200):

> In vertebrates, the genes encoding the class of transcription factors called homeobox genes are found in clusters named A, B, C, and D on four separate chromosomes. Expression of these proteins is spatially and temporally regulated during embryonic development. This gene is part of the A cluster on chromosome 7 and encodes a DNA-binding transcription factor which may regulate gene expression, morphogenesis, and differentiation. Three transcript variants encoding two different isoforms have been …

**Accessions** — [HGNC:5104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5104) · Entrez [3200](https://www.ncbi.nlm.nih.gov/gene/3200) · UniProt [O43365](https://www.uniprot.org/uniprotkb/O43365) · Ensembl [ENSG00000105997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105997)

## Data

Gene col 2701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2701); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2701]; `tensor/DDL_lfc|DDL_z.npy` [2701]; `embed/gene_vectors.npy` [2701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2701 or target_col == 2701). Every well: [[HOXA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
