---
symbol: "PBXIP1"
type: "gene"
col: 8671
ensembl_id: "ENSG00000163346"
name: "PBX homeobox interacting protein 1"
location: "1q21.3"
module: 76
arm: "+"
pooled_cpm: 15.3
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 28
n_dd_up_clean: 23
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# PBXIP1

*PBX homeobox interacting protein 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.30× (z +10.7, q 4e-24, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.483× (z -13.2, q 7e-37, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.386× (z -12.2, q 1e-31, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP8]] (+0.68, fdr 7e-06), [[GRN]] (+0.64, fdr 1e-05), [[MOSPD3]] (+0.64, fdr 3e-05); moves opposite to [[GCFC2]] (-0.61, fdr 2e-05), [[MRPS16]] (-0.59, fdr 2e-05), [[COA7]] (-0.56, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPATC1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +10.7 | 4e-24 | 43/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +10.7 | 4e-24 | 42/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +8.9 | 1e-16 | 42/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.4 | 8e-15 | 32/46 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +7.2 | 1e-10 | 32/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +6.5 | 6e-09 | 33/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.31×** | +4.9 | 7e-05 | 24/48 (SW 900, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.001 | 22/46 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.004 | 17/47 (KATO III, SNU-423, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.004 | 16/46 (LS 180, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.005 | 19/46 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.011 | 10/48 (NCI-H23, SNU-423, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.33×** | +3.6 | 0.012 | 14/47 (SK-MEL-2, H4, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.015 | 15/47 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.019 | 10/48 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.019 | 13/48 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.020 | 10/48 (HepG2/C3A, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.483×** | -13.2 | 7e-37 | 36/47 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.386×** | -12.2 | 1e-31 | 46/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.374×** | -12.1 | 2e-31 | 42/47 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.376×** | -12.1 | 2e-31 | 39/47 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.436×** | -10.6 | 3e-24 | 40/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.439×** | -10.5 | 6e-24 | 38/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.456×** | -10.0 | 8e-22 | 33/46 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.504×** | -8.8 | 1e-16 | 32/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -8.6 | 7e-16 | 35/46 (SHP-77, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.536×** | -8.0 | 9e-14 | 37/46 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.596×** | -6.6 | 2e-09 | 28/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.511×** | -4.5 | 3e-04 | 18/46 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.705×** | -4.3 | 7e-04 | 20/46 (SW 900, SW1417, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.634×** | -4.2 | 0.001 | 16/48 (NCI-H2347, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.552×** | -4.0 | 0.002 | 15/45 (SW 900, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.552×** | -4.0 | 0.002 | 19/43 (MIA PaCa-2, Hs 766T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -3.8 | 0.004 | 19/48 (LS 180, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.728×** | -3.8 | 0.004 | 16/48 (NCI-H460, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 31.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -11.9) |
| [[SW480 (line)]] | alt | 9.20 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.207× (z -9.8) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.224× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.106× (z -15.5) |
| [[PANC-1 (line)]] | alt | 12.7 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.41× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.225× (z -10.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -8.8) |
| [[SW 900 (line)]] | alt | 30.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.165× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.190× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -9.5) |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0938× (z -12.1) |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -8.8) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -8.5) |
| [[A-172 (line)]] | wt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +9.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.185× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0710× (z -12.0) |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP8]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GRN]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.64 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[SEZ6L2]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.61 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[OS9]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[DNASE2]] | +0.61 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[MKRN1]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[GM2A]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[LAPTM4A]] | +0.61 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[PCYOX1]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PCOLCE]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | -0.61 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MRPS16]] | -0.59 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[COA7]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TMA16]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SCMH1]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[GPATCH4]] | -0.55 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[PPIL1]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[EEFSEC]] | -0.53 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[ARL14EP]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[C12orf29]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[MIOS]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATC1L]] | B | SPATC1L activity raises PBXIP1's level | lines that do not express SPATC1L (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without SPATC1L | 0.073 | ⚠ within organs, on part of the lines; also absent: TIAM1 |
| [[SLC35F2]] | C | SLC35F2 activity lowers PBXIP1's level | lines that do not express SLC35F2 (3) vs lines expressing it (47) | 1.39× higher at baseline in the lines without SLC35F2 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, TMEM132A, POLR3G; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, -19.8); signed map (-21.3, 7.7). **Vector** length 84.3, 18.8% of its response variance represented; |z| ≥ 3 in 1,256 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.1 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | -3.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.6 | +2.9 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.4 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.6 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -12.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | PBX homeobox interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,944,076-154,956,123 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPIP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AQ6](https://www.uniprot.org/uniprotkb/Q96AQ6) (Pre-B-cell leukemia transcription factor-interacting protein 1):

> Regulator of pre-B-cell leukemia transcription factors (BPXs) function. Inhibits the binding of PBX1-HOX complex to DNA and blocks the transcriptional activity of E2A-PBX1. Tethers estrogen receptor-alpha (ESR1) to microtubules and allows them to influence estrogen receptors-alpha signaling.

**Summary**, from NCBI Gene [57326](https://www.ncbi.nlm.nih.gov/gene/57326):

> The protein encoded by this gene interacts with the PBX1 homeodomain protein, inhibiting its transcriptional activation potential by preventing its binding to DNA. The encoded protein, which is primarily cytosolic but can shuttle to the nucleus, also can interact with estrogen receptors alpha and beta and promote the proliferation of breast cancer, brain tumors, and lung cancer. Several transcript variants encoding different isoforms have been found for this gene. More variants exist, but their …

**Accessions** — [HGNC:21199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21199) · Entrez [57326](https://www.ncbi.nlm.nih.gov/gene/57326) · UniProt [Q96AQ6](https://www.uniprot.org/uniprotkb/Q96AQ6) · Ensembl [ENSG00000163346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163346)

## Data

Gene col 8671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8671); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8671]; `tensor/DDL_lfc|DDL_z.npy` [8671]; `embed/gene_vectors.npy` [8671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8671 or target_col == 8671). Every well: [[PBXIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PBXIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
