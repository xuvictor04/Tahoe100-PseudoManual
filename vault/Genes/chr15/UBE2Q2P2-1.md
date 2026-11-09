---
symbol: "UBE2Q2P2-1"
type: "gene"
col: 16535
ensembl_id: "ENSG00000290945"
name: ""
location: ""
module: 159
arm: "+"
pooled_cpm: 38.26
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# UBE2Q2P2-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +9.2, q 2e-17, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -9.8, q 6e-20, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2Q2P2]] (+0.90, fdr 7e-06, ⚠ same locus), [[GPT2]] (+0.68, fdr 1e-05), [[PACC1]] (+0.67, fdr 1e-05), [[WASF3]] (+0.67, fdr 1e-05); moves opposite to [[INO80D]] (-0.66, fdr 3e-05), [[PCNX4-DT]] (-0.64, fdr 1e-04), [[ERCC6L2-AS1]] (-0.62, fdr 3e-04).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPIC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +9.2 | 2e-17 | 39/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +7.4 | 3e-11 | 40/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +7.3 | 5e-11 | 39/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.84×** | +6.7 | 3e-09 | 39/48 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.54×** | +5.3 | 2e-05 | 29/47 (A498, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.1 | 3e-05 | 34/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +5.0 | 5e-05 | 30/48 (A498, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +4.4 | 8e-04 | 32/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.046 | 21/48 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.3 | 0.046 | 23/48 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.68×** | +3.3 | 0.049 | 21/43 (A498, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.20×** | +3.2 | 0.069 | 21/48 (SNU-1, SW48, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.069 | 13/47 (NCI-H1573, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.081 | 15/47 (J82, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -9.8 | 6e-20 | 40/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.454×** | -9.6 | 2e-19 | 41/45 (LoVo, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.456×** | -9.2 | 5e-18 | 28/39 (LoVo, A549, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.466×** | -8.6 | 9e-16 | 31/44 (C-33 A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.520×** | -8.0 | 2e-13 | 34/48 (LOX-IMVI, A-427, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.542×** | -7.2 | 6e-11 | 35/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -6.7 | 2e-09 | 38/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.659×** | -4.9 | 7e-05 | 30/47 (HCT15, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.757×** | -4.8 | 1e-04 | 27/48 (NCI-H23, NCI-H1573, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.721×** | -4.0 | 0.004 | 28/48 (NCI-H460, A498, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.737×** | -3.7 | 0.009 | 24/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.559×** | -3.7 | 0.009 | 19/36 (HT-29, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.738×** | -3.7 | 0.009 | 25/48 (SHP-77, KATO III, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.013 | 23/48 (PANC-1, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | **0.751×** | -3.5 | 0.018 | 21/47 (AsPC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **0.585×** | -3.4 | 0.022 | 24/46 (NCI-H23, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.025 | 20/48 (HT-29, NCI-H661, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.588×** | -3.2 | 0.047 | 22/46 (NCI-H460, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 82.8 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -16.7) |
| [[NCI-H1573 (line)]] | alt | 36.8 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -8.9) |
| [[C32 (line)]] | wt | 34.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -12.8) |
| [[HCT15 (line)]] | alt | 69.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 69.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.27× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.0390× (z -25.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.331× (z -9.2) |
| [[SW480 (line)]] | alt | 34.0 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 36.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 35.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0827× (z -17.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 86.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -8.5) |
| [[HOP62 (line)]] | alt | 37.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 51.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 41.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0669× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -8.8) |
| [[A498 (line)]] | wt | 37.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.269× (z -11.2) |
| [[AN3 CA (line)]] | alt | 75.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 20.5 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.35× (z +9.0) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.244× (z -8.7) |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -14.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 64.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -12.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.204× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -14.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 15.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +9.2) | — |
| [[J82 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.219× (z -10.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-1 (line)]] | wt | 46.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.1) |
| [[SW 900 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -12.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2Q2P2]] | +0.90 | +0.90 / +0.85 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GPT2]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PACC1]] | +0.67 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[WASF3]] | +0.67 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[HSPA5]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[GOLGA6L9]] | +0.66 | +0.52 / +0.58 | both halves | 1e-05 | ⚠ same locus (10.4 kb, same strand: neighbours can correlate without regulation) |
| [[TPD52]] | +0.65 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[CAMK2G]] | +0.65 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[FAM118A]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[TMEM41B]] | +0.64 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[AAK1]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ST6GALNAC4]] | +0.64 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PWWP3A]] | +0.63 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80D]] | -0.66 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | -0.64 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.62 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[EP300]] | -0.61 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[CREBBP]] | -0.61 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[LINS1]] | -0.60 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[HCG17]] | -0.60 | -0.62 / -0.32 | both halves | 1e-04 |  |
| [[NEK8]] | -0.60 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PATL2]] | -0.59 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[FAM200A]] | -0.59 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[ZNF764]] | -0.58 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[HELQ]] | -0.58 | -0.60 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPIC1]] | B | EPIC1 activity raises UBE2Q2P2-1's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.32× lower at baseline in the lines without EPIC1 | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[HSPA12A]] | C | HSPA12A activity raises UBE2Q2P2-1's level | lines that do not express HSPA12A (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without HSPA12A | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR3659HG, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.4, 4.8); signed map (-39.3, -6.3). **Vector** length 113, 33.4% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.0 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.0 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.5 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.7 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.6 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -0.7 |

## What is on record

> [!warning] No registry record
> UBE2Q2P2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16535); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16535]; `tensor/DDL_lfc|DDL_z.npy` [16535]; `embed/gene_vectors.npy` [16535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16535 or target_col == 16535). Every well: [[UBE2Q2P2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2Q2P2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
