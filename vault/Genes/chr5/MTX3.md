---
symbol: "MTX3"
type: "gene"
col: 10781
ensembl_id: "ENSG00000177034"
name: "metaxin 3"
location: "5q14.1"
module: 135
arm: "+"
pooled_cpm: 34.01
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# MTX3

*metaxin 3* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.80× (z +14.6, q 1e-45, up in 27 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.37× (z +11.7, q 4e-29, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.650× (z -11.2, q 2e-26, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYW3]] (+0.72, fdr 7e-06), [[C17orf75]] (+0.65, fdr 4e-05), [[PGGT1B]] (+0.62, fdr 2e-05); moves opposite to [[CTXN1]] (-0.60, fdr 3e-05), [[MAPKAPK2]] (-0.59, fdr 1e-05), [[SLC66A2]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[RMDN2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +14.6 | 1e-45 | 27/36 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +11.8 | 8e-30 | 33/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +11.7 | 4e-29 | 29/45 (CFPAC-1, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +11.0 | 5e-26 | 31/45 (A-427, LOX-IMVI, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +9.5 | 2e-19 | 29/45 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +9.5 | 3e-19 | 30/45 (A-427, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +9.1 | 6e-18 | 29/45 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +9.0 | 1e-17 | 24/44 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +8.7 | 2e-16 | 28/44 (LOX-IMVI, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +8.0 | 6e-14 | 29/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +7.3 | 2e-11 | 19/40 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +6.9 | 3e-10 | 23/45 (A-427, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +6.5 | 4e-09 | 24/45 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +6.2 | 2e-08 | 21/45 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.9 | 2e-07 | 19/44 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +5.1 | 1e-05 | 15/45 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +5.0 | 2e-05 | 14/45 (NCI-H2347, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.8 | 4e-05 | 19/44 (A-427, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 3e-04 | 13/44 (NCI-H460, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +4.3 | 4e-04 | 9/45 (NCI-H2347, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.002 | 9/45 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10781.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.650×** | -11.2 | 2e-26 | 32/45 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -10.6 | 1e-23 | 34/45 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -10.0 | 3e-21 | 35/45 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.710×** | -8.9 | 7e-17 | 31/45 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.561×** | -7.9 | 4e-13 | 23/44 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -7.3 | 4e-11 | 25/45 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -6.1 | 7e-08 | 20/45 (A498, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.692×** | -5.0 | 4e-05 | 17/45 (NCI-H2347, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.708×** | -4.7 | 2e-04 | 18/45 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.860× | -3.9 | 0.005 | 9/44 (SNU-423, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.4 | 0.032 | 15/45 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.836× | -3.4 | 0.033 | 7/45 (SNU-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.877× | -3.3 | 0.042 | 17/44 (SNU-423, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.4 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.413× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.267× (z -9.6) |
| [[A-427 (line)]] | wt | 60.8 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.08× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.551× (z -10.0) |
| [[A-172 (line)]] | wt | 43.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.58× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.36× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HEC-1-A (line)]] | alt | 46.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -9.0) |
| [[SNU-1 (line)]] | wt | 50.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0575× (z -11.0) |
| [[SW480 (line)]] | alt | 24.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.9) | — |
| [[A549 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +8.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 48.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.8) | — |
| [[LoVo (line)]] | wt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 43.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.293× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -11.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -11.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SHP-77 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.284× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 81.4 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0599× (z -9.1) |
| [[SW 900 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.3) |
| [[A498 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW3]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[C17orf75]] | +0.65 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[PGGT1B]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ZNF391]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CARD8]] | +0.61 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[RNF6]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[HDDC2]] | +0.59 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[ARL14EP]] | +0.58 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[APOOL]] | +0.58 | +0.56 / +0.65 | both halves | 1e-05 | STRING 871 |
| [[TSR2]] | +0.57 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[DUS4L]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MRPS9]] | +0.57 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTXN1]] | -0.60 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[SLC66A2]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[GLRX5]] | -0.57 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CYB5R3]] | -0.57 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[METRN]] | -0.57 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[NECTIN2]] | -0.53 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[FAM89B]] | -0.52 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[CARHSP1]] | -0.51 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[SRGAP2]] | -0.51 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[CSNK1G2]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SRGAP2B]] | -0.50 | -0.38 / -0.52 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MTX3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RMDN2]] | C | MTX3 activity raises RMDN2's level | lines that do not express MTX3 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without MTX3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; its own permutation p |
| [[DMAC2]] | C | MTX3 activity raises DMAC2's level | lines that do not express MTX3 (3) vs lines expressing it (47) | 1.28× lower at baseline in the lines without MTX3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1 |
| [[METTL6]] | C | MTX3 activity raises METTL6's level | lines that do not express MTX3 (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without MTX3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; its own permutation p |

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-18.2, 8.3); signed map (9.2, -30.0). **Vector** length 95.9, 20.7% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.3 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +3.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.0 | -11.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -7.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | metaxin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:79,976,716-79,991,262 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Metaxins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5HYI7](https://www.uniprot.org/uniprotkb/Q5HYI7) (Metaxin-3):

> Could function in transport of proteins into the mitochondrion.

**Summary**, from NCBI Gene [345778](https://www.ncbi.nlm.nih.gov/gene/345778):

> Predicted to be involved in mitochondrial outer membrane translocase complex assembly and protein insertion into mitochondrial outer membrane. Located in mitochondrion. Part of MIB complex and SAM complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24812) · Entrez [345778](https://www.ncbi.nlm.nih.gov/gene/345778) · UniProt [Q5HYI7](https://www.uniprot.org/uniprotkb/Q5HYI7) · Ensembl [ENSG00000177034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177034)

## Data

Gene col 10781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10781); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10781]; `tensor/DDL_lfc|DDL_z.npy` [10781]; `embed/gene_vectors.npy` [10781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10781 or target_col == 10781). Every well: [[MTX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
