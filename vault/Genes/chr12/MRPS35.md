---
symbol: "MRPS35"
type: "gene"
col: 702
ensembl_id: "ENSG00000061794"
name: "mitochondrial ribosomal protein S35"
location: "12p11.22"
module: 171
arm: "+"
pooled_cpm: 81.17
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# MRPS35

*mitochondrial ribosomal protein S35* — 12p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.16× (z +11.2, q 2e-26, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.756× (z -7.4, q 6e-11, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX4]] (+0.78, fdr 7e-06), [[MRPS30]] (+0.76, fdr 7e-06), [[MRPL19]] (+0.71, fdr 7e-06); moves opposite to [[TUBB4B]] (-0.61, fdr 7e-06), [[ERF]] (-0.61, fdr 7e-06), [[IER5]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.16×** | +11.2 | 2e-26 | 45/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +9.0 | 8e-17 | 37/49 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +8.9 | 1e-16 | 39/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.9 | 1e-16 | 30/44 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +8.8 | 2e-16 | 42/47 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +8.7 | 2e-16 | 42/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +7.4 | 8e-12 | 40/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.9 | 4e-10 | 31/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +6.7 | 2e-09 | 35/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +6.5 | 5e-09 | 28/45 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +6.0 | 1e-07 | 27/48 (hTERT-HPNE, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 1e-06 | 31/48 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.9 | 5e-05 | 31/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 17/48 (PANC-1, CHP-212, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.003 | 19/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 23/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.004 | 22/48 (NCI-H1573, A498, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.008 | 9/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.009 | 23/48 (KATO III, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.010 | 22/49 (A498, AsPC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.019 | 16/48 (AsPC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -7.4 | 6e-11 | 32/49 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.761×** | -7.3 | 1e-10 | 27/48 (AsPC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.738×** | -5.7 | 2e-06 | 28/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.751×** | -5.4 | 1e-05 | 31/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -4.5 | 9e-04 | 19/48 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.827×** | -3.6 | 0.033 | 18/49 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.4 | 0.048 | 0/50 | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.832×** | -3.3 | 0.062 | 19/48 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.840× | -3.1 | 0.13 | 14/47 (NCI-H1573, SW48, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 118 | 6 (4 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 4.86× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.518× (z -9.9) |
| [[LS 180 (line)]] | wt | 102 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.95× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 4.77× (z +8.8) | — |
| [[LoVo (line)]] | wt | 100 | 4 (4 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 3.48× (z +14.5) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -9.3) |
| [[KATO III (line)]] | alt | 98.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +12.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 94.1 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.15× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 79.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +12.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.24× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 59.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 84.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 77.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 78.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -8.7) |
| [[HOP62 (line)]] | alt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 86.7 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.42× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 72.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 73.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.24× (z +9.2) | — |
| [[RKO (line)]] | wt | 90.5 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.93× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 65.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.7) |
| [[SW48 (line)]] | wt | 78.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 4.58× (z +10.3) | — |
| [[A-427 (line)]] | wt | 65.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 77.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.1) |
| [[C-33 A (line)]] | alt | 60.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.3) |
| [[Hs 766T (line)]] | wt | 54.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 39.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 93.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX4]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[MRPS30]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 972 |
| [[MRPL19]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 996 |
| [[RPP30]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[MRS2]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[CDC123]] | +0.69 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[OTUD6B]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[WDR36]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[DLAT]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RTCA]] | +0.67 | +0.73 / +0.57 | both halves | 9e-06 |  |
| [[MRPL3]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 995 |
| [[FTO]] | +0.65 | +0.70 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB4B]] | -0.61 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[ERF]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[IER5]] | -0.59 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[TP53INP2]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[CCNYL1]] | -0.59 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[BCL2L12]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ZNF335]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[CYTH2]] | -0.58 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ISG20]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[HLA-A]] | -0.56 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[MICALL2]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MRPS35's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-9.3, -12.4); signed map (-33.4, -18.9). **Vector** length 102, 30.5% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.1 | +6.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.5 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +8.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +11.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +7.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -4.3 | +2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -7.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.7 | -0.5 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.22 — chr12:27,710,822-27,756,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRPS28, MDS023, mS35 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P82673](https://www.uniprot.org/uniprotkb/P82673) carries no function annotation.

**Summary**, from NCBI Gene [60488](https://www.ncbi.nlm.nih.gov/gene/60488):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16635) · Entrez [60488](https://www.ncbi.nlm.nih.gov/gene/60488) · UniProt [P82673](https://www.uniprot.org/uniprotkb/P82673) · Ensembl [ENSG00000061794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061794)

## Data

Gene col 702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 702); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 702]; `tensor/DDL_lfc|DDL_z.npy` [702]; `embed/gene_vectors.npy` [702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 702 or target_col == 702). Every well: [[MRPS35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
