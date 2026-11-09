---
symbol: "TMEM242"
type: "gene"
col: 13271
ensembl_id: "ENSG00000215712"
name: "transmembrane protein 242"
location: "6q25.3"
module: 80
arm: "+"
pooled_cpm: 24.85
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# TMEM242

*transmembrane protein 242* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.89× (z +14.0, q 1e-41, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.735× (z -9.5, q 1e-18, down in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.690× (z -8.1, q 1e-13, down in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (MIA PaCa-2 0.294×, PANC-1 0.389×, SNU-423 0.370×, LoVo 0.371×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.0650×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.389×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR5]] (+0.63, fdr 1e-05), [[INPP4A]] (+0.61, fdr 3e-05), [[FBXO3]] (+0.59, fdr 1e-05); moves opposite to [[MZF1-AS1]] (-0.60, fdr 6e-05), [[GPR137]] (-0.57, fdr 2e-04), [[LEKR1]] (-0.56, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNTA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +14.0 | 1e-41 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +12.1 | 3e-31 | 41/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +9.2 | 7e-18 | 37/47 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.8 | 1e-12 | 29/45 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +7.0 | 3e-10 | 25/47 (SW480, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.9 | 5e-10 | 26/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.4 | 1e-08 | 24/47 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.6 | 1e-06 | 21/48 (A-427, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 9e-06 | 23/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.26×** | +4.8 | 8e-05 | 11/47 (NCI-H2030, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +4.8 | 8e-05 | 16/47 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 2e-04 | 17/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.3 | 9e-04 | 12/48 (KATO III, AsPC-1, …) | top dose only |  |
| [[Ivermectin (drug)]] 5 µM |  | 1.20× | +4.0 | 0.003 | 6/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.18× | +3.6 | 0.012 | 8/47 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.040 | 5/48 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.094 | 11/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.096 | 13/48 (HOP62, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13271.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (MIA PaCa-2 0.294×, PANC-1 0.389×, SNU-423 0.370×, LoVo 0.371×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.0650×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.389×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.735×** | -9.5 | 1e-18 | 30/47 (MIA PaCa-2, PANC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -8.1 | 1e-13 | 31/47 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -4.2 | 0.006 | 13/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.833×** | -4.0 | 0.010 | 13/47 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.844× | -3.6 | 0.043 | 7/47 (LoVo, LS 180, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.753× | -3.2 | 0.12 | 14/48 (A-172, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.865× | -3.2 | 0.13 | 7/47 (COLO 205, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.861× | -3.1 | 0.13 | 17/48 (PANC-1, SW1417, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 37.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -16.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 35.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -8.5) |
| [[SW480 (line)]] | alt | 45.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.9) | — |
| [[A-427 (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.119× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.139× (z -10.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.268× (z -13.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0650× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR5]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[INPP4A]] | +0.61 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[FBXO3]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ZNF341]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[FBXW2]] | +0.57 | +0.69 / +0.30 | both halves | 2e-04 |  |
| [[CROT]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[SLC41A3]] | +0.56 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PXMP4]] | +0.56 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[TBC1D24]] | +0.55 | +0.63 / +0.22 | both halves | 6e-04 |  |
| [[SLC23A2]] | +0.55 | +0.60 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZF1-AS1]] | -0.60 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[GPR137]] | -0.57 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[LEKR1]] | -0.56 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[ENO3]] | -0.56 | -0.61 / -0.26 | both halves | 4e-04 |  |
| [[DLG2]] | -0.55 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.55 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ZBTB2]] | -0.54 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[NEK8]] | -0.54 | -0.61 / -0.21 | both halves | 7e-04 |  |
| [[LINC01135]] | -0.54 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[DRAIC]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CTBP1-DT]] | -0.53 | -0.55 / -0.27 | both halves | 3e-04 |  |
| [[SIX5]] | -0.53 | -0.62 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTA1]] | B | SNTA1 activity raises TMEM242's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.20× lower at baseline in the lines without SNTA1 | 0.046 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction -0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.8, 3.3); signed map (-43.2, -8.2). **Vector** length 81.7, 14.7% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +12.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +14.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.4 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -9.8 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.2 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 242 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:157,289,025-157,323,601 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BM033; previously C6orf35 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWH2](https://www.uniprot.org/uniprotkb/Q9NWH2) (Transmembrane protein 242):

> Scaffold protein that participates in the c-ring assembly of mitochondrial ATP synthase (F(1)F(0) ATP synthase or complex V) by facilitating the membrane insertion and oligomer formation of the subunit c/ATP5MC3. Participates in the incorporation of the c-ring into vestigial complexes. Additionally influences the incorporation of subunits MT-ATP6, MT-ATP8, ATP5MJ, and ATP5MK in the ATP synthase.

**Summary**, from NCBI Gene [729515](https://www.ncbi.nlm.nih.gov/gene/729515):

> Involved in mitochondrial proton-transporting ATP synthase complex assembly. Located in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17206) · Entrez [729515](https://www.ncbi.nlm.nih.gov/gene/729515) · UniProt [Q9NWH2](https://www.uniprot.org/uniprotkb/Q9NWH2) · Ensembl [ENSG00000215712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215712)

## Data

Gene col 13271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13271); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13271]; `tensor/DDL_lfc|DDL_z.npy` [13271]; `embed/gene_vectors.npy` [13271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13271 or target_col == 13271). Every well: [[TMEM242 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM242.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
