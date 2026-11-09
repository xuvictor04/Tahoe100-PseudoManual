---
symbol: "ETS2"
type: "gene"
col: 8084
ensembl_id: "ENSG00000157557"
name: "ETS proto-oncogene 2, transcription factor"
location: "21q22.2"
module: 123
arm: "+"
pooled_cpm: 93.55
n_lines_expressing: 40
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 21
direction_downstream: 30
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# ETS2

*ETS proto-oncogene 2, transcription factor* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +19.1, q 0e+00, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.405× (z -17.8, q 0e+00, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOSL2]] (+0.68, fdr 7e-06), [[CEBPD]] (+0.61, fdr 7e-06), [[ARID5B]] (+0.60, fdr 1e-05); moves opposite to [[BCAP31]] (-0.51, fdr 3e-05), [[CTNNBIP1]] (-0.49, fdr 4e-05), [[NAP1L4]] (-0.49, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[RNF144B]] → it (grade B ⚠); 30 go from it, the strongest it → [[RND3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +19.1 | 0e+00 | 24/38 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +12.0 | 1e-30 | 25/38 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +8.8 | 2e-16 | 25/39 (NCI-H1573, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +7.4 | 2e-11 | 20/38 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.8 | 1e-09 | 23/38 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.6 | 2e-06 | 22/38 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +5.1 | 3e-05 | 20/40 (LoVo, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +4.7 | 2e-04 | 20/39 (LoVo, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.6 | 2e-04 | 16/38 (HS-578T, NCI-H2347, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.52×** | +4.3 | 8e-04 | 18/38 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.004 | 15/38 (SW1417, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.9 | 0.004 | 15/37 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.005 | 18/38 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.009 | 16/39 (LoVo, LS 180, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.045 | 17/37 (LoVo, LS 180, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.0 | 0.081 | 13/38 (PANC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.087 | 7/38 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.087 | 9/38 (NCI-H1792, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.405×** | -17.8 | 0e+00 | 33/38 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.458×** | -15.4 | 0e+00 | 32/38 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -14.3 | 4e-44 | 28/39 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.574×** | -10.9 | 1e-25 | 27/38 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.584×** | -10.6 | 3e-24 | 29/38 (COLO 205, SHP-77, …) | two highest doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -9.7 | 2e-20 | 25/35 (SHP-77, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -7.6 | 2e-12 | 28/38 (Hs 766T, SHP-77, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.696×** | -6.9 | 5e-10 | 24/38 (HT-29, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.750×** | -5.4 | 3e-06 | 21/40 (HT-29, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.861× | -4.1 | 0.002 | 18/38 (PANC-1, Hs 766T, …) | top dose only | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.818×** | -3.9 | 0.004 | 14/38 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.826×** | -3.8 | 0.008 | 17/38 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.893× | -3.1 | 0.077 | 13/39 (BT-474, CFPAC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 187 | 0 | 15 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -21.5) |
| [[hTERT-HPNE (line)]] | wt | 180 | 3 | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.185× (z -16.4) |
| [[LoVo (line)]] | wt | 107 | 7 (1 ⚠) | 4 (1 ⚠) | [[Trametinib (drug)]] 0.5 µM 2.24× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.261× (z -13.6) |
| [[LS 180 (line)]] | wt | 344 | 2 (1 ⚠) | 9 (5 ⚠) | [[Trametinib (drug)]] 5 µM 2.05× (z +9.3) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 2.02× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.0934× (z -28.5) |
| [[Hs 766T (line)]] | wt | 293 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -22.2) |
| [[PANC-1 (line)]] | alt | 192 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -22.7) |
| [[A549 (line)]] | wt | 143 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -16.6) |
| [[COLO 205 (line)]] | alt | 181 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.225× (z -13.2) |
| [[HT-29 (line)]] | alt | 154 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -22.6) |
| [[NCI-H460 (line)]] | wt | 23.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +17.1) | — |
| [[SW1417 (line)]] | alt | 113 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.0) |
| [[J82 (line)]] | alt | 59.9 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.344× (z -10.0) |
| [[A-172 (line)]] | wt | 40.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +15.9) | — |
| [[BT-474 (line)]] | alt | 63.8 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -10.3) |
| [[C32 (line)]] | wt | 68.1 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 177 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 96.9 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +20.5) | [[Panobinostat (drug)]] 5 µM 0.382× (z -9.2) |
| [[A498 (line)]] | wt | 82.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +21.0) | — |
| [[AsPC-1 (line)]] | alt | 63.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +28.5) | — |
| [[HOP62 (line)]] | alt | 128 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +15.3) | — |
| [[HS-578T (line)]] | alt | 72.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +23.6) | — |
| [[KATO III (line)]] | alt | 101 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 85.8 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 16.0× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 101 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.337× (z -9.8) |
| [[SW480 (line)]] | alt | 55.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 58.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.413× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 44.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 29.9 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.22× (z +9.4) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -8.8) |
| [[CHP-212 (line)]] | wt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -9.3) |
| [[H4 (line)]] | wt | 68.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 59.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 64.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 47.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +15.3) | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 | — | [[Apalutamide (drug)]] 5 µM 0.0786× (z -9.4) |
| [[SW48 (line)]] | wt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -10.9) |
| [[A-427 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 21.8 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 89.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOSL2]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 606 |
| [[CEBPD]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ARID5B]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[KLF4]] | +0.60 | +0.57 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 408 |
| [[CXCL2]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZFP36L2]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RHOU]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[RASSF6]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SLC1A3]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[NFKBIA]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CXCL3]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CTNNBIP1]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[NAP1L4]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[DPP9]] | -0.48 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[CROCCP3-1]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[STARD3]] | -0.46 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[DIP2A]] | -0.45 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 17, C 4. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF144B]] | B | RNF144B activity raises ETS2's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without RNF144B | 0.007 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[RASSF6]] | B | RASSF6 activity raises ETS2's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.54× lower at baseline in the lines without RASSF6 | 0.010 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[EPS8]] | B | EPS8 activity raises ETS2's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 4.51× lower at baseline in the lines without EPS8 | 0.010 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[ABCA12]] | B | ABCA12 activity raises ETS2's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without ABCA12 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |
| [[GATA6]] | B | GATA6 activity raises ETS2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.26× lower at baseline in the lines without GATA6 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[TNFAIP2]] | B | TNFAIP2 activity raises ETS2's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without TNFAIP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[C3]] | B | C3 activity raises ETS2's level | lines that do not express C3 (32) vs lines expressing it (18) | 2.02× lower at baseline in the lines without C3 | 0.042 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11 |
| [[TOP2A]] | B | TOP2A activity raises ETS2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TRIM29]] | B | TRIM29 activity raises ETS2's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without TRIM29 | 0.044 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[ARID5B]] | B | ARID5B activity raises ETS2's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.83× lower at baseline in the lines without ARID5B | 0.050 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[TRIM31]] | B | TRIM31 activity raises ETS2's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.64× lower at baseline in the lines without TRIM31 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[AKR1C3]] | B | AKR1C3 activity raises ETS2's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without AKR1C3 | 0.055 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 26, C 4. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RND3]] | B | ETS2 activity raises RND3's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 3.48× lower at baseline in the lines without ETS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[TNFAIP2]] | B | ETS2 activity raises TNFAIP2's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 3.35× lower at baseline in the lines without ETS2 | 0.008 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[SNAI2]] | B | ETS2 activity raises SNAI2's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 3.78× lower at baseline in the lines without ETS2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[BCL3]] | B | ETS2 activity raises BCL3's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without ETS2 | 0.012 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[FAM227A]] | B | ETS2 activity lowers FAM227A's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.69× higher at baseline in the lines without ETS2 | 0.016 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[DUSP1]] | B | ETS2 activity raises DUSP1's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.04× lower at baseline in the lines without ETS2 | 0.021 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[ELF3-AS1]] | B | ETS2 activity raises ELF3-AS1's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.67× lower at baseline in the lines without ETS2 | 0.024 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[THBS3-AS1]] | B | ETS2 activity lowers THBS3-AS1's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.84× higher at baseline in the lines without ETS2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[ZC3H12A]] | B | ETS2 activity raises ZC3H12A's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without ETS2 | 0.027 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[GATA6]] | B | ETS2 activity raises GATA6's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.76× lower at baseline in the lines without ETS2 | 0.028 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[NFKBIZ]] | B | ETS2 activity raises NFKBIZ's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without ETS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[EPS8]] | B | ETS2 activity raises EPS8's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.50× lower at baseline in the lines without ETS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.7, 13.3); signed map (48.8, 12.5). **Vector** length 127, 36.3% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +19.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.2 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.3 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.2 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.9 |
| fall | [[Dabrafenib (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -15.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -7.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ETS proto-oncogene 2, transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:38,805,183-38,824,955 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | HEDGEHOG_SIGNALING, XENOBIOTIC_METABOLISM, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Oncogene Induced Senescence; Cellular Senescence; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P15036](https://www.uniprot.org/uniprotkb/P15036) (Protein C-ets-2):

> Transcription factor activating transcription. Binds specifically the DNA GGAA/T core motif (Ets-binding site or EBS) in gene promoters and stimulates transcription.

**Summary**, from NCBI Gene [2114](https://www.ncbi.nlm.nih.gov/gene/2114):

> This gene encodes a transcription factor which regulates genes involved in development and apoptosis. The encoded protein is also a protooncogene and shown to be involved in regulation of telomerase. A pseudogene of this gene is located on the X chromosome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:3489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3489) · Entrez [2114](https://www.ncbi.nlm.nih.gov/gene/2114) · UniProt [P15036](https://www.uniprot.org/uniprotkb/P15036) · Ensembl [ENSG00000157557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157557)

## Data

Gene col 8084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8084); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8084]; `tensor/DDL_lfc|DDL_z.npy` [8084]; `embed/gene_vectors.npy` [8084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8084 or target_col == 8084). Every well: [[ETS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
