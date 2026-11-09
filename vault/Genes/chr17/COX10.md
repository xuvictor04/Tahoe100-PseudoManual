---
symbol: "COX10"
type: "gene"
col: 123
ensembl_id: "ENSG00000006695"
name: "cytochrome c oxidase assembly factor heme A:farnesyltransferase COX10"
location: "17p12"
module: 4
arm: "+"
pooled_cpm: 50.8
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# COX10

*cytochrome c oxidase assembly factor heme A:farnesyltransferase COX10* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.65× (z +8.4, q 2e-14, up in 43 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.63× (z +8.2, q 8e-14, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.565× (z -9.7, q 2e-19, down in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.801× (z -5.3, q 1e-05, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS27]] (+0.77, fdr 7e-06), [[LARS2]] (+0.75, fdr 7e-06), [[DHX37]] (+0.73, fdr 7e-06); moves opposite to [[WDTC1]] (-0.64, fdr 1e-05), [[GRHL1]] (-0.62, fdr 1e-05), [[MINDY2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +8.4 | 2e-14 | 43/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +8.2 | 8e-14 | 36/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +6.9 | 7e-10 | 39/48 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.30×** | +6.3 | 5e-08 | 28/48 (NCI-H1573, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 5e-05 | 27/48 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.0 | 5e-05 | 24/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +4.9 | 1e-04 | 26/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 1e-04 | 29/48 (LS 180, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.6 | 3e-04 | 25/49 (LoVo, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +4.6 | 3e-04 | 29/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.0 | 0.003 | 25/44 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.26×** | +3.9 | 0.005 | 19/48 (SW 900, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.011 | 22/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.011 | 19/48 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.014 | 20/48 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.033 | 19/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.053 | 19/48 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.565×** | -9.7 | 2e-19 | 37/49 (SK-MEL-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -6.2 | 1e-07 | 28/42 (HEC-1-A, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.711×** | -5.3 | 1e-05 | 25/45 (RKO, SW48, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -5.3 | 1e-05 | 30/48 (RKO, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.748×** | -4.9 | 9e-05 | 32/48 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -4.5 | 6e-04 | 26/48 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.008 | 25/49 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.4 | 0.047 | 19/48 (A498, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.821×** | -3.4 | 0.047 | 23/48 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.687×** | -3.3 | 0.047 | 17/48 (NCI-H23, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.047 | 22/48 (SW 1271, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.825×** | -3.3 | 0.049 | 20/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 57.7 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 69.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.12× (z +9.3) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.459× (z -9.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 46.3 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -10.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 80.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -13.5) |
| [[SW48 (line)]] | wt | 73.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 60.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -19.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 65.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.7 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 92.4 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.108× (z -9.8) |
| [[SW480 (line)]] | alt | 68.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.435× (z -10.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -10.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 52.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0751× (z -19.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.305× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~55% of this change |
| [[hTERT-HPNE (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 57.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 85.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -13.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS27]] | +0.77 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[LARS2]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[DHX37]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.72 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[UTP20]] | +0.72 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[PHF14]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[METAP1D]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[TSR1]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[NAA25]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[RPTOR]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[HSPBP1]] | +0.69 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[LTV1]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDTC1]] | -0.64 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[GRHL1]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[MINDY2]] | -0.62 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[HDAC5]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[PJA2]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[SVIP]] | -0.59 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[SKAP2]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SLC30A4]] | -0.58 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[GPX4]] | -0.58 | -0.49 / -0.61 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises COX10's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.7, -33.4); signed map (-0.3, -49.1). **Vector** length 108, 28.4% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing* (reactome, mean cos +0.51 to 10); *Folding of actin by CCT/TriC* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.2 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.1 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.5 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +5.7 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.3 | +3.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor heme A:farnesyltransferase COX10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:14,069,490-14,231,736 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12887](https://www.uniprot.org/uniprotkb/Q12887) (Protoheme IX farnesyltransferase, mitochondrial):

> Converts protoheme IX and farnesyl diphosphate to heme O.

**Summary**, from NCBI Gene [1352](https://www.ncbi.nlm.nih.gov/gene/1352):

> Cytochrome c oxidase (COX), the terminal component of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. This component is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear …

**Accessions** — [HGNC:2260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2260) · Entrez [1352](https://www.ncbi.nlm.nih.gov/gene/1352) · UniProt [Q12887](https://www.uniprot.org/uniprotkb/Q12887) · Ensembl [ENSG00000006695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006695)

## Data

Gene col 123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 123); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 123]; `tensor/DDL_lfc|DDL_z.npy` [123]; `embed/gene_vectors.npy` [123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 123 or target_col == 123). Every well: [[COX10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
