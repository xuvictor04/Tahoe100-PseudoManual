---
symbol: "TUBGCP5"
type: "gene"
col: 15861
ensembl_id: "ENSG00000275835"
name: "tubulin gamma complex component 5"
location: "15q11.2"
module: 144
arm: "+"
pooled_cpm: 40.03
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# TUBGCP5

*tubulin gamma complex component 5* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +6.4, q 1e-07, up in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Glycyrrhizic acid (drug)]] 0.05 µM: 1.22× (z +3.9, q 0.009, up in 15 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.398× (z -19.5, q 0e+00, down in 39 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.434× (z -18.4, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO45]] (+0.61, fdr 3e-05), [[HDHD5]] (+0.58, fdr 2e-05), [[DDX50]] (+0.57, fdr 1e-05); moves opposite to [[RMND5A]] (-0.59, fdr 4e-05), [[ATP6V1C1]] (-0.57, fdr 3e-05), [[DNAH7]] (-0.56, fdr 1e-04).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +6.4 | 1e-07 | 23/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.28×** | +5.3 | 3e-05 | 23/46 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.27×** | +5.2 | 3e-05 | 22/47 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.25×** | +4.6 | 5e-04 | 24/47 (LS 180, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +4.3 | 0.002 | 18/48 (BT-474, SW480, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.009 | 15/46 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.021 | 16/48 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.023 | 9/46 (NCI-H460, SW 900, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.18× | +3.5 | 0.030 | 15/48 (LS 180, HT-29, …) | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.17× | +3.4 | 0.032 | 10/47 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.033 | 8/46 (NCI-H460, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.3 | 0.053 | 12/48 (HOP62, SW48, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.10× | +3.1 | 0.094 | 6/48 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.094 | 5/47 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.398×** | -19.5 | 0e+00 | 39/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.434×** | -18.4 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -17.2 | 0e+00 | 40/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.486×** | -15.9 | 0e+00 | 41/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.261×** | -15.5 | 0e+00 | 43/48 (HOP62, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -13.8 | 2e-41 | 40/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.642×** | -13.8 | 3e-41 | 31/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.324×** | -13.0 | 1e-36 | 38/48 (SW 900, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.596×** | -11.4 | 3e-28 | 35/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.571×** | -11.2 | 4e-27 | 29/43 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -10.8 | 3e-25 | 24/42 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.618×** | -10.6 | 2e-24 | 30/45 (RKO, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.668×** | -8.5 | 7e-16 | 28/48 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.783×** | -7.6 | 1e-12 | 30/48 (H4, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.715×** | -7.4 | 7e-12 | 31/48 (A-172, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.748×** | -6.4 | 6e-09 | 31/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.780×** | -5.5 | 2e-06 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.810×** | -4.4 | 3e-04 | 17/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.856× | -3.4 | 0.014 | 15/48 (SW 1088, A498, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 0.862× | -3.2 | 0.034 | 12/48 (NCI-H460, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.8 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -24.1) |
| [[C32 (line)]] | wt | 55.5 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -18.2) |
| [[HOP62 (line)]] | alt | 73.6 | 0 | 13 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.216× (z -18.2) |
| [[PANC-1 (line)]] | alt | 49.0 | 0 | 13 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -20.3) |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 73.0 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.282× (z -18.8) |
| [[RKO (line)]] | wt | 43.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -22.2) |
| [[A549 (line)]] | wt | 67.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 67.8 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -15.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.494× (z -11.9) |
| [[J82 (line)]] | alt | 46.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.0) |
| [[SW480 (line)]] | alt | 33.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -15.3) |
| [[A-172 (line)]] | wt | 39.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -23.5) |
| [[A-427 (line)]] | wt | 38.4 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.223× (z -13.4) |
| [[BT-474 (line)]] | alt | 83.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 58.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -32.2) |
| [[H4 (line)]] | wt | 30.7 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.170× (z -14.2) |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.0) |
| [[SW 900 (line)]] | alt | 30.2 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0374× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 32.3 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.176× (z -10.8) |
| [[A498 (line)]] | wt | 35.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -12.8) |
| [[C-33 A (line)]] | alt | 60.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.297× (z -10.2) |
| [[LoVo (line)]] | wt | 39.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.314× (z -11.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 36.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 55.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -12.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM 0.0559× (z -9.0) |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.0) |
| [[LS 180 (line)]] | wt | 21.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1573 (line)]] | alt | 33.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.341× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0837× (z -8.9) |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -9.3) |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -9.4) |
| [[AN3 CA (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO45]] | +0.61 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[HDHD5]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[DDX50]] | +0.57 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GLMN]] | +0.56 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[MTERF3]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[EEF1AKMT4]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[NSFP1]] | +0.55 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[FAM216A]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TFB1M]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[NT5M]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[KLHL22]] | +0.53 | +0.32 / +0.65 | both halves | 1e-04 |  |
| [[SNRNP40]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMND5A]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[ATP6V1C1]] | -0.57 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[DNAH7]] | -0.56 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[IGF2R]] | -0.53 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[LPP]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[KLF3]] | -0.52 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PLCL1]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[LINC02937]] | -0.51 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[MUC20]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[STAT6]] | -0.50 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[ERBIN]] | -0.50 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[DAZAP2]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises TUBGCP5's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without NT5M | 0.049 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.400). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.1, -17.9); signed map (-39.2, 20.1). **Vector** length 117, 33.3% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | +4.5 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.1 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.1 | +4.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -0.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.9 | -10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.9 | -15.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.8 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.6 | -10.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -9.4 | -19.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -13.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tubulin gamma complex component 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q11.2 — chr15:22,983,192-23,039,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCP5, KIAA1899 |
| Gene groups (HGNC) | Tubulin gamma complex component family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RT8](https://www.uniprot.org/uniprotkb/Q96RT8) (Gamma-tubulin complex component 5):

> Component of the gamma-tubulin ring complex (gTuRC) which mediates microtubule nucleation. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation.

**Summary**, from NCBI Gene [114791](https://www.ncbi.nlm.nih.gov/gene/114791):

> Enables microtubule binding activity. Involved in microtubule nucleation. Located in centrosome. Part of gamma-tubulin ring complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18600) · Entrez [114791](https://www.ncbi.nlm.nih.gov/gene/114791) · UniProt [Q96RT8](https://www.uniprot.org/uniprotkb/Q96RT8) · Ensembl [ENSG00000275835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275835)

## Data

Gene col 15861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15861); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15861]; `tensor/DDL_lfc|DDL_z.npy` [15861]; `embed/gene_vectors.npy` [15861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15861 or target_col == 15861). Every well: [[TUBGCP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBGCP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
