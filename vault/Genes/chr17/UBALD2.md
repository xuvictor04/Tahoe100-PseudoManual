---
symbol: "UBALD2"
type: "gene"
col: 11649
ensembl_id: "ENSG00000185262"
name: "UBA like domain containing 2"
location: "17q25.1"
module: 22
arm: "+"
pooled_cpm: 24.32
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 29
n_dd_up_clean: 9
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# UBALD2

*UBA like domain containing 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.81× (z +6.2, q 4e-07, up in 33 of 45 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +5.6, q 6e-06, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.147× (z -20.0, q 0e+00, down in 47 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.131× (z -7.9, q 1e-12, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC25C]] (+0.68, fdr 7e-06), [[NDE1]] (+0.67, fdr 7e-06), [[PTTG1]] (+0.63, fdr 1e-05); moves opposite to [[SYNJ2BP]] (-0.52, fdr 5e-05), [[PUS7L]] (-0.51, fdr 6e-05), [[NRAS]] (-0.50, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.81×** | +6.2 | 4e-07 | 33/45 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.6 | 6e-06 | 26/46 (A549, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.70×** | +5.5 | 6e-06 | 31/47 (KATO III, NCI-H1573, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.76×** | +4.2 | 0.004 | 25/46 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +4.1 | 0.005 | 22/45 (NCI-H460, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.008 | 23/47 (H4, J82, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.67×** | +3.8 | 0.010 | 26/46 (LoVo, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.032 | 18/46 (PANC-1, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.053 | 20/47 (H4, PANC-1, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.080 | 17/46 (HOP62, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.35×** | +3.1 | 0.085 | 16/48 (NCI-H1573, KATO III, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.097 | 20/48 (HOP62, SW 900, …) | all doses, flat | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | 1.50× | +3.0 | 0.11 | 18/48 (HOP62, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.147×** | -20.0 | 0e+00 | 47/47 (A498, NCI-H2030, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.131×** | -7.9 | 1e-12 | 41/46 (SW1417, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.149×** | -7.4 | 3e-11 | 40/44 (C32, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.150×** | -7.3 | 3e-11 | 42/46 (SW1417, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.608×** | -7.3 | 3e-11 | 32/48 (A-427, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.193×** | -6.4 | 2e-08 | 39/47 (A549, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.195×** | -6.3 | 2e-08 | 35/46 (A498, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.564×** | -6.0 | 2e-07 | 30/47 (HCT15, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.562×** | -5.6 | 1e-06 | 32/48 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.590×** | -5.5 | 2e-06 | 30/47 (C32, COLO 205, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.480×** | -5.5 | 3e-06 | 37/48 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.597×** | -5.2 | 1e-05 | 30/47 (C32, RKO, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.611×** | -4.9 | 5e-05 | 28/47 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[Volasertib (drug)]] 0.5 µM |  | **0.536×** | -4.6 | 1e-04 | 29/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.624×** | -4.5 | 2e-04 | 30/47 (C32, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.726×** | -4.3 | 7e-04 | 25/48 (C32, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.663×** | -4.1 | 0.001 | 25/47 (C32, PANC-1, …) | all doses, flat |  |
| [[venetoclax (drug)]] 0.5 µM |  | **0.579×** | -4.1 | 0.001 | 22/48 (NCI-H23, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 12.3 | 11 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 4.80× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.108× (z -10.1) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 47.9 | 0 | 9 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.101× (z -15.0) ⚠ unreliable plate only · without an alert: [[Cobimetinib (drug)]] 5 µM 0.105× (z -14.2) |
| [[LoVo (line)]] | wt | 16.5 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0824× (z -14.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.150× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 21.4 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.117× (z -11.5) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.189× (z -11.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0266× (z -9.6) |
| [[A-427 (line)]] | wt | 27.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.170× (z -13.8) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A549 (line)]] | wt | 25.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.131× (z -12.5) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 25.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0837× (z -10.6) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 32.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.116× (z -14.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0290× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0570× (z -14.9) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 60.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.163× (z -12.5) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0948× (z -12.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.113× (z -17.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0449× (z -9.0) |
| [[A-172 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.181× (z -8.7) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0514× (z -19.5) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -10.0) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.146× (z -8.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.154× (z -10.6) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.156× (z -9.1) |
| [[HOP62 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.141× (z -12.6) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.139× (z -10.0) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.163× (z -11.0) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.157× (z -8.7) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -11.0) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.112× (z -13.4) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.194× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.129× (z -11.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0543× (z -17.2) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -11.3) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0813× (z -13.2) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -11.8) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -10.6) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.109× (z -12.6) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.155× (z -9.4) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0850× (z -10.5) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC25C]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[NDE1]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PTTG1]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[FRAT2]] | +0.61 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[MAP3K3]] | +0.59 | +0.37 / +0.62 | both halves | 7e-05 |  |
| [[UBALD1]] | +0.58 | +0.30 / +0.67 | both halves | 2e-04 |  |
| [[MIS18BP1]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[YPEL1]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[MOB2]] | +0.56 | +0.22 / +0.66 | both halves | 6e-04 |  |
| [[BRD8]] | +0.56 | +0.34 / +0.70 | both halves | 1e-04 |  |
| [[HAGH]] | +0.55 | +0.32 / +0.62 | both halves | 2e-04 |  |
| [[SUN2]] | +0.55 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNJ2BP]] | -0.52 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[PUS7L]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[NRAS]] | -0.50 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[RABGGTB]] | -0.49 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[PTPN11]] | -0.48 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[EMC1]] | -0.46 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[NAA50]] | -0.46 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[MTMR2]] | -0.46 | -0.27 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises UBALD2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[REPS2]] | B | REPS2 activity raises UBALD2's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without REPS2 | 0.062 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.1, -58.2); signed map (-52.9, -40.1). **Vector** length 135, 42.6% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | +4.1 | +6.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.9 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +2.9 | +3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.8 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.9 | -20.0 |
|  | [[EX229 (drug)]] 5 µM |  | -9.1 | -7.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.0 | -7.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.8 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.7 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.4 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | UBA like domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,265,348-76,271,298 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29814; previously FAM100B |
| Matched by | ensembl_id |

UniProt [Q8IYN6](https://www.uniprot.org/uniprotkb/Q8IYN6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28438) · Entrez [283991](https://www.ncbi.nlm.nih.gov/gene/283991) · UniProt [Q8IYN6](https://www.uniprot.org/uniprotkb/Q8IYN6) · Ensembl [ENSG00000185262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185262)

## Data

Gene col 11649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11649); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11649]; `tensor/DDL_lfc|DDL_z.npy` [11649]; `embed/gene_vectors.npy` [11649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11649 or target_col == 11649). Every well: [[UBALD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBALD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
