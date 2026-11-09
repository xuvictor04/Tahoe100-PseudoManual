---
symbol: "SRGAP2"
type: "gene"
col: 15475
ensembl_id: "ENSG00000266028"
name: "SLIT-ROBO Rho GTPase activating protein 2"
location: "1q32.1"
module: 64
arm: "-"
pooled_cpm: 75.75
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 32
n_dd_up_clean: 8
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# SRGAP2

*SLIT-ROBO Rho GTPase activating protein 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.74× (z +9.2, q 2e-17, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.464× (z -11.8, q 4e-29, down in 35 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.565× (z -9.4, q 5e-19, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRGAP2B]] (+0.92, fdr 7e-06), [[SRGAP2C]] (+0.88, fdr 7e-06), [[POC1A]] (+0.58, fdr 1e-05); moves opposite to [[CCNT2]] (-0.59, fdr 3e-05), [[PGGT1B]] (-0.57, fdr 3e-05), [[NUDT9]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00839]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +9.2 | 2e-17 | 40/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +8.3 | 4e-14 | 38/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +6.3 | 7e-08 | 36/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.1 | 5e-05 | 31/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.004 | 27/49 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.005 | 22/48 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.019 | 23/48 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.019 | 20/50 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.1 | 0.12 | 13/48 (LS 180, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15475.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.464×** | -11.8 | 4e-29 | 35/45 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.541×** | -9.8 | 5e-20 | 39/47 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.667×** | -9.4 | 5e-19 | 33/48 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.565×** | -9.4 | 5e-19 | 40/48 (A-427, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.579×** | -9.0 | 2e-17 | 35/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.583×** | -8.6 | 8e-16 | 36/48 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.625×** | -7.8 | 7e-13 | 39/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.437×** | -7.2 | 6e-11 | 35/49 (C32, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.661×** | -6.8 | 5e-10 | 29/49 (A498, C32, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -6.7 | 9e-10 | 31/42 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -6.0 | 9e-08 | 33/48 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.705×** | -5.8 | 4e-07 | 33/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.519×** | -5.7 | 6e-07 | 28/37 (SK-MEL-2, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.718×** | -5.5 | 2e-06 | 29/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -5.2 | 6e-06 | 30/48 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.812×** | -4.8 | 5e-05 | 23/48 (NCI-H2347, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.745×** | -4.6 | 1e-04 | 28/48 (SK-MEL-2, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.617×** | -4.2 | 1e-03 | 23/48 (Hs 766T, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.780×** | -4.1 | 0.001 | 23/48 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.635×** | -3.9 | 0.002 | 29/48 (Hs 766T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.640×** | -3.9 | 0.003 | 21/48 (SW 900, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.653×** | -3.7 | 0.006 | 20/47 (COLO 205, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 147 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.170× (z -16.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 54.4 | 2 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +12.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -11.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.438× (z -9.6) |
| [[SW480 (line)]] | alt | 73.6 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.405× (z -11.7) |
| [[A498 (line)]] | wt | 156 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.424× (z -8.8) |
| [[C32 (line)]] | wt | 462 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.366× (z -10.7) |
| [[LoVo (line)]] | wt | 30.9 | 3 (1 ⚠) | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.35× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.336× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 80.2 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.270× (z -13.0) |
| [[PANC-1 (line)]] | alt | 72.9 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -14.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -13.1) |
| [[A-427 (line)]] | wt | 55.1 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 120 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -14.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.333× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.240× (z -10.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 173 | 0 | 5 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0546× (z -13.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.312× (z -10.3) |
| [[LS 180 (line)]] | wt | 23.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.98× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.0 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -15.2) |
| [[A549 (line)]] | wt | 56.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 66.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 83.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.358× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.170× (z -13.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.229× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 72.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.406× (z -9.5) |
| [[SHP-77 (line)]] | alt | 50.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -11.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 44.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 59.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.295× (z -9.7) |
| [[HT-29 (line)]] | alt | 49.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.266× (z -12.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.386× (z -9.0) |
| [[RKO (line)]] | wt | 52.9 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Harringtonine (drug)]] 0.5 µM 0.274× (z -10.7) |
| [[SNU-1 (line)]] | wt | 60.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.320× (z -9.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 44.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0913× (z -10.2) |
| [[HCT15 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 89.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -10.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 64.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0913× (z -9.3) ⚠ toxic |
| [[J82 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.321× (z -9.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 60.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.457× (z -9.8) |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2B]] | +0.92 | +0.90 / +0.89 | both halves | 7e-06 | same gene group |
| [[SRGAP2C]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | same gene group; STRING 428 |
| [[POC1A]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ADAM10]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SRGAP2D]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SNTB2]] | +0.56 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RELL1]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[CENPJ]] | +0.53 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[MAP3K3]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[PGP]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[FRYL]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[RPS6KA5]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT2]] | -0.59 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[PGGT1B]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[NUDT9]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[RRAGB]] | -0.54 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[POLR2M]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ZSCAN21]] | -0.53 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[PIGB]] | -0.53 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[KCTD14]] | -0.53 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[RAD52]] | -0.53 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.52 | -0.32 / -0.50 | both halves | 1e-04 |  |
| [[C17orf75]] | -0.52 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[MTX3]] | -0.51 | -0.37 / -0.53 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00839]] | B | LINC00839 activity raises SRGAP2's level | lines that do not express LINC00839 (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without LINC00839 | 0.070 | ⚠ within organs, on part of the lines; also absent: PRR16, CCNYL2, PCDH10 |
| [[HDAC6]] | B | HDAC6 activity lowers SRGAP2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TCTN1]] | C | TCTN1 activity raises SRGAP2's level | lines that do not express TCTN1 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without TCTN1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, PHC1, DNAJC18; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **-** arm (projection on the module's main direction -0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-28.8, -51.1); signed map (-51.4, -25.4). **Vector** length 108, 32.9% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.0 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.4 | -9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.6 | -11.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.3 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.1 | -9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | SLIT-ROBO Rho GTPase activating protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,203,346-206,464,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0456, ARHGAP34, SRGAP2A; previously FNBP2 |
| Gene groups (HGNC) | F-BAR domain containing; Small nucleolar RNA protein coding host genes; AH/BAR family Rho GTPase activating proteins; SH3 domain containing |
| Reactome | 15 pathways, smallest: Inactivation of CDC42 and RAC1; RHOU GTPase cycle; RHOF GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O75044](https://www.uniprot.org/uniprotkb/O75044) (SLIT-ROBO Rho GTPase-activating protein 2):

> Postsynaptic RAC1 GTPase activating protein (GAP) that plays a key role in neuronal morphogenesis and migration mainly during development of the cerebral cortex. Regulates excitatory and inhibitory synapse maturation and density in cortical pyramidal neurons. SRGAP2/SRGAP2A limits excitatory and inhibitory synapse density through its RAC1-specific GTPase activating activity, while it promotes maturation of both excitatory and inhibitory synapses through its ability to bind to the postsynaptic …

**Summary**, from NCBI Gene [23380](https://www.ncbi.nlm.nih.gov/gene/23380):

> This locus encodes a member of the SLIT-ROBO Rho GTPase activating protein family. The encoded protein stimulates GTPase activity of Rac1, and plays a role in cortical neuron development. This locus has several paralogs on human chromosome 1 resulting from segmental duplication. While this locus itself is conserved among various species, the paralogs are found only in the genus Homo, and not in the genomes of non-human great apes. Alternatively spliced transcript variants have been described …

**Accessions** — [HGNC:19751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19751) · Entrez [23380](https://www.ncbi.nlm.nih.gov/gene/23380) · UniProt [O75044](https://www.uniprot.org/uniprotkb/O75044) · Ensembl [ENSG00000266028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266028)

## Data

Gene col 15475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15475); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15475]; `tensor/DDL_lfc|DDL_z.npy` [15475]; `embed/gene_vectors.npy` [15475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15475 or target_col == 15475). Every well: [[SRGAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRGAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
