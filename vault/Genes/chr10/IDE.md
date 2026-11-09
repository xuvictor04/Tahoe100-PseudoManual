---
symbol: "IDE"
type: "gene"
col: 4134
ensembl_id: "ENSG00000119912"
name: "insulin degrading enzyme"
location: "10q23.33"
module: 4
arm: "+"
pooled_cpm: 49.14
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# IDE

*insulin degrading enzyme* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.80× (z +20.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.856× (z -4.6, q 0.002, down in 19 of 48 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 0.820× (z -4.2, q 0.008, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD11]] (+0.77, fdr 7e-06), [[HSPA4]] (+0.69, fdr 7e-06), [[GSR]] (+0.68, fdr 7e-06); moves opposite to [[WIPF2]] (-0.61, fdr 1e-05), [[CYBA]] (-0.58, fdr 1e-05), [[MARCHF9]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IGFBP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.80×** | +20.3 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.64×** | +20.3 | 0e+00 | 44/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.36×** | +17.9 | 0e+00 | 46/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +15.4 | 0e+00 | 32/41 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +13.9 | 7e-42 | 37/46 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +9.5 | 2e-19 | 43/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +8.5 | 2e-15 | 35/42 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.6 | 3e-09 | 26/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.53×** | +6.3 | 1e-08 | 31/48 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +6.3 | 2e-08 | 25/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 6e-07 | 25/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.24×** | +4.5 | 3e-04 | 21/47 (HOP62, A-172, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +4.5 | 4e-04 | 15/47 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.25×** | +4.3 | 6e-04 | 21/44 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.1 | 0.001 | 21/47 (A549, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 20/48 (CFPAC-1, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.003 | 14/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.005 | 18/47 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.019 | 5/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.3 | 0.023 | 14/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.034 | 12/48 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.040 | 10/47 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4134.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -4.6 | 0.002 | 19/48 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.820×** | -4.2 | 0.008 | 20/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.764×** | -4.0 | 0.010 | 15/48 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.700×** | -3.8 | 0.018 | 16/49 (NCI-H2030, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.063 | 19/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.4 | 0.063 | 12/48 (LS 180, HS-578T, …) | all doses, stronger at high dose |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.860× | -3.1 | 0.18 | 4/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.9 | 4 (1 ⚠) | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.28× (z +14.3) | [[Digitoxin (drug)]] 5 µM 0.338× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 65.6 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +11.9) | [[Lonafarnib (drug)]] 5 µM 0.295× (z -8.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 60.4 | 3 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.61× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.63× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 82.7 | 6 (3 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.75× (z +14.9) | — |
| [[A-172 (line)]] | wt | 29.3 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.20× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 25.1 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.75× (z +14.0) | — |
| [[LoVo (line)]] | wt | 78.5 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.480× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 47.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.23× (z +10.9) | — |
| [[C32 (line)]] | wt | 33.6 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.64× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.43× (z +9.6) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.184× (z -8.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 47.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 34.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.28× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 48.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.75× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 86.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 27.4 | 3 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 4.62× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.88× (z +10.9) | — |
| [[RKO (line)]] | wt | 63.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.17× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SNU-423 (line)]] | alt | 31.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.27× (z +10.4) | — |
| [[A498 (line)]] | wt | 44.1 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.41× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.570× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 24.4 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.06× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 47.6 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 67.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 42.4 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.06× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.66× (z +9.3) | — |
| [[A-427 (line)]] | wt | 62.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.70× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 68.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.02× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 27.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.44× (z +9.1) | — |
| [[KATO III (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 40.6 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.99× (z +9.3) | — |
| [[NCI-H661 (line)]] | alt | 51.7 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0932× (z -8.7) |
| [[BT-474 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 77.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD11]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 | pathway: Deubiquitination |
| [[HSPA4]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[GSR]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[LARP4]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 | STRING 459 |
| [[NSMAF]] | +0.66 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[CCT6A]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[VWA8]] | +0.64 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[GCLM]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CCT5]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[NAA50]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CLPB]] | +0.63 | +0.57 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_SPERMATOGENESIS |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPF2]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[CYBA]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[MARCHF9]] | -0.58 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[WASL-DT]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[NDUFA2]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[AFMID]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TMSB10]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[RBM38]] | -0.55 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[IMP3]] | -0.54 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[ZFYVE1]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFBP2]] | B | IGFBP2 activity raises IDE's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without IGFBP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[PIR]] | B | PIR activity raises IDE's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without PIR | 0.076 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.8, -30.7); signed map (-11.2, -43.5). **Vector** length 133, 38.9% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +12.9 | +20.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +12.0 | +20.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.3 | +17.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +15.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -4.2 | -2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.6 | -4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | insulin degrading enzyme |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:92,451,684-92,574,096 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M16 metallopeptidases |
| Hallmark sets | SPERMATOGENESIS, PEROXISOME |
| Reactome | 7 pathways, smallest: Insulin receptor recycling; Peroxisomal protein import; Signaling by Insulin receptor |
| Matched by | ensembl_id |

**Function**, from UniProt [P14735](https://www.uniprot.org/uniprotkb/P14735) (Insulin-degrading enzyme):

> Plays a role in the cellular breakdown of insulin, APP peptides, IAPP peptides, natriuretic peptides, glucagon, bradykinin, kallidin, and other peptides, and thereby plays a role in intercellular peptide signaling. Substrate binding induces important conformation changes, making it possible to bind and degrade larger substrates, such as insulin. Contributes to the regulation of peptide hormone signaling cascades and regulation of blood glucose homeostasis via its role in the degradation of …

**Summary**, from NCBI Gene [3416](https://www.ncbi.nlm.nih.gov/gene/3416):

> This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as beta-amyloid. Deficiencies in this protein's function are associated with Alzheimer's disease and …

**Accessions** — [HGNC:5381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5381) · Entrez [3416](https://www.ncbi.nlm.nih.gov/gene/3416) · UniProt [P14735](https://www.uniprot.org/uniprotkb/P14735) · Ensembl [ENSG00000119912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119912)

## Data

Gene col 4134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4134); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4134]; `tensor/DDL_lfc|DDL_z.npy` [4134]; `embed/gene_vectors.npy` [4134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4134 or target_col == 4134). Every well: [[IDE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
