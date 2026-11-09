---
symbol: "DDX31"
type: "gene"
col: 4624
ensembl_id: "ENSG00000125485"
name: "DEAD-box helicase 31"
location: "9q34.13"
module: 5
arm: "+"
pooled_cpm: 45.76
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DDX31

*DEAD-box helicase 31* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.85× (z +12.7, q 2e-34, up in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 3.34× (z +12.3, q 4e-32, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.607× (z -9.9, q 1e-20, down in 30 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.828× (z -4.6, q 6e-04, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-172 0.0886×, HEC-1-A 0.212×, J82 0.265×, HS-578T 0.174×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.237×, SNU-1 0.128×, SHP-77 0.274×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.226×, LoVo 0.266×, HEC-1-A 0.276×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.207×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0916×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.463×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRTO4]] (+0.82, fdr 7e-06), [[SDAD1]] (+0.82, fdr 7e-06), [[NOP16]] (+0.81, fdr 7e-06); moves opposite to [[MPC2]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LDLRAD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.85×** | +12.7 | 2e-34 | 45/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.34×** | +12.3 | 4e-32 | 42/48 (NCI-H460, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +9.9 | 1e-20 | 40/49 (HEC-1-A, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +9.4 | 1e-18 | 36/48 (HT-29, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +7.3 | 3e-11 | 30/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +6.8 | 1e-09 | 31/48 (HT-29, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +6.5 | 9e-09 | 26/48 (A-172, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.74×** | +5.7 | 1e-06 | 30/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +5.5 | 3e-06 | 23/48 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.69×** | +5.4 | 5e-06 | 26/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +4.5 | 4e-04 | 13/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.25×** | +4.4 | 5e-04 | 20/47 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +4.3 | 6e-04 | 13/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 7e-04 | 13/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.52×** | +4.2 | 8e-04 | 16/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.007 | 13/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.015 | 15/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.024 | 11/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4624.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-172 0.0886×, HEC-1-A 0.212×, J82 0.265×, HS-578T 0.174×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.237×, SNU-1 0.128×, SHP-77 0.274×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.226×, LoVo 0.266×, HEC-1-A 0.276×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.207×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0916×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.463×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.607×** | -9.9 | 1e-20 | 30/43 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -9.9 | 1e-20 | 34/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.695×** | -6.9 | 8e-10 | 24/45 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.828×** | -4.6 | 6e-04 | 23/48 (A-427, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.821×** | -4.1 | 0.005 | 19/46 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.833× | -3.8 | 0.015 | 18/48 (KATO III, RKO, …) | top dose only | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.836× | -3.7 | 0.015 | 15/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.7 | 0.015 | 23/48 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.849× | -3.7 | 0.015 | 15/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.845× | -3.4 | 0.033 | 15/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.842× | -3.4 | 0.033 | 18/47 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | 0.859× | -3.1 | 0.082 | 16/47 (RKO, PANC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.813× | -3.0 | 0.10 | 14/48 (SW 1271, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 146 | 0 | 7 (6 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.424× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 82.5 | 2 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.66× (z +10.1) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 5.34× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -12.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 56.5 | 0 | 3 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0916× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 66.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 53.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.02× (z +12.5) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 5.17× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -16.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 88.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0886× (z -20.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 62.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.7) |
| [[PANC-1 (line)]] | alt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 69.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -15.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -12.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.207× (z -11.7) |
| [[HS-578T (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -13.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +10.0) | — |
| [[J82 (line)]] | alt | 67.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -14.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -12.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -12.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.0) | — |
| [[SW 1271 (line)]] | alt | 56.4 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0770× (z -8.6) |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.283× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.12× (z +9.3) ⚠ unreliable plate only | — |
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRTO4]] | +0.82 | +0.80 / +0.79 | both halves | 7e-06 | STRING 549 |
| [[SDAD1]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 | STRING 749 |
| [[NOP16]] | +0.81 | +0.82 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[BYSL]] | +0.80 | +0.79 / +0.79 | both halves | 7e-06 | STRING 732 |
| [[ZNF202]] | +0.79 | +0.82 / +0.76 | both halves | 7e-06 | STRING 475 |
| [[IMP4]] | +0.79 | +0.77 / +0.75 | both halves | 7e-06 | STRING 511 |
| [[WDR4]] | +0.79 | +0.76 / +0.82 | both halves | 7e-06 | STRING 569 |
| [[POLR1B]] | +0.77 | +0.75 / +0.83 | both halves | 7e-06 | STRING 765 |
| [[MAK16]] | +0.77 | +0.78 / +0.75 | both halves | 7e-06 | STRING 569 |
| [[UTP14A]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 | STRING 631 |
| [[LTV1]] | +0.76 | +0.73 / +0.78 | both halves | 7e-06 | STRING 473 |
| [[PDCD11]] | +0.76 | +0.75 / +0.82 | both halves | 7e-06 | STRING 850 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.65 | -0.65 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAD3]] | B | LDLRAD3 activity raises DDX31's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without LDLRAD3 | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADD3]] | B | ADD3 activity lowers DDX31's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.73× higher at baseline in the lines without ADD3 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[PARVB]] | B | PARVB activity raises DDX31's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without PARVB | 0.077 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[ALDH1B1]] | C | ALDH1B1 activity raises DDX31's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without ALDH1B1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent |
| [[TSEN2]] | C | TSEN2 activity raises DDX31's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without TSEN2 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.786). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.4, -37.1); signed map (-1.5, -45.3). **Vector** length 125, 36.1% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.66 to 13); *rRNA processing* (reactome, mean cos +0.61 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.61 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.0 | +12.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +12.3 |
|  | [[EX229 (drug)]] 5 µM |  | +6.1 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | +6.0 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.6 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.7 | +4.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.0 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -4.4 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:132,592,997-132,670,401 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13633, FLJ23349, FLJ14578, PPP1R25 |
| Gene groups (HGNC) | DEAD-box helicases; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8H2](https://www.uniprot.org/uniprotkb/Q9H8H2) (ATP-dependent DNA helicase DDX31):

> May have DNA helicase activity and RNA helicase activity. Probably have ssDNA and RNA dependent ATPase activity (By similarity). Plays a role in ribosome biogenesis and TP53/p53 regulation through its interaction with NPM1.

**Summary**, from NCBI Gene [64794](https://www.ncbi.nlm.nih.gov/gene/64794):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this DEAD box protein family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. …

**Accessions** — [HGNC:16715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16715) · Entrez [64794](https://www.ncbi.nlm.nih.gov/gene/64794) · UniProt [Q9H8H2](https://www.uniprot.org/uniprotkb/Q9H8H2) · Ensembl [ENSG00000125485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125485)

## Data

Gene col 4624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4624); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4624]; `tensor/DDL_lfc|DDL_z.npy` [4624]; `embed/gene_vectors.npy` [4624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4624 or target_col == 4624). Every well: [[DDX31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
