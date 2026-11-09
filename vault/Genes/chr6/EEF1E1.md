---
symbol: "EEF1E1"
type: "gene"
col: 4576
ensembl_id: "ENSG00000124802"
name: "eukaryotic translation elongation factor 1 epsilon 1"
location: "6p24.3"
module: 18
arm: "+"
pooled_cpm: 26.19
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# EEF1E1

*eukaryotic translation elongation factor 1 epsilon 1* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (22 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.19× (z +12.1, q 6e-31, up in 40 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.53× (z +6.9, q 3e-10, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 5 µM: 0.795× (z -4.0, q 0.036, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.443×, PANC-1 0.580×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.178×, SHP-77 0.297×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0691×); [[Flutamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0938×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.310×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAT2]] (+0.83, fdr 7e-06), [[TUBGCP4]] (+0.76, fdr 7e-06), [[CAD]] (+0.72, fdr 7e-06); moves opposite to [[OFD1]] (-0.63, fdr 8e-06), [[BOLA1]] (-0.63, fdr 9e-06), [[MTHFR]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 23 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +12.1 | 6e-31 | 40/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +10.8 | 7e-25 | 44/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.75×** | +8.9 | 7e-17 | 37/48 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.79×** | +8.7 | 4e-16 | 42/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.65×** | +8.0 | 1e-13 | 32/47 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.64×** | +8.0 | 1e-13 | 29/48 (SNU-423, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.63×** | +7.8 | 3e-13 | 31/47 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.59×** | +7.4 | 9e-12 | 33/48 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.57×** | +7.3 | 2e-11 | 25/44 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +7.1 | 9e-11 | 32/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +6.9 | 3e-10 | 34/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +6.2 | 3e-08 | 31/48 (HOP62, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.44×** | +5.8 | 3e-07 | 26/47 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +5.4 | 3e-06 | 26/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **1.41×** | +5.3 | 5e-06 | 17/36 (KATO III, A549, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.0 | 2e-05 | 24/48 (NCI-H2347, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.80×** | +5.0 | 2e-05 | 25/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +4.5 | 2e-04 | 19/46 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 4e-04 | 20/47 (CFPAC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.3 | 4e-04 | 17/47 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.67×** | +4.3 | 4e-04 | 21/48 (SK-MEL-2, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 5e-04 | 22/48 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +4.2 | 7e-04 | 13/47 (SK-MEL-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.005 | 14/48 (CFPAC-1, NCI-H2030, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.013 | 8/48 (NCI-H23, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.039 | 12/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.039 | 14/48 (NCI-H460, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.443×, PANC-1 0.580×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.178×, SHP-77 0.297×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0691×); [[Flutamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0938×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.310×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 5 µM |  | **0.795×** | -4.0 | 0.036 | 20/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.8 | 0.036 | 21/47 (LoVo, PANC-1, …) | top dose only | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.794×** | -3.6 | 0.053 | 11/47 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.814×** | -3.6 | 0.053 | 18/48 (A-427, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.077 | 15/48 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.082 | 8/48 (NCI-H1792, SW480, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.826× | -3.1 | 0.14 | 15/47 (LS 180, LoVo, …) | rises with dose | low cells (technical?) |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.828× | -3.1 | 0.14 | 6/47 (SW 1271, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.829× | -3.0 | 0.14 | 18/47 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.824× | -3.0 | 0.14 | 15/47 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 40.3 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 2 | — | [[Flutamide (drug)]] 0.5 µM 0.0938× (z -9.2) |
| [[LoVo (line)]] | wt | 20.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.75× (z +10.4) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 38.5 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.310× (z -9.2) |
| [[SW48 (line)]] | wt | 32.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.103× (z -8.9) |
| [[KATO III (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0691× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.23× (z +10.3) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.40× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.95× (z +8.6) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAT2]] | +0.83 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[TUBGCP4]] | +0.76 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[CAD]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[DKC1]] | +0.71 | +0.78 / +0.61 | both halves | 7e-06 | same gene group |
| [[DTD2]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 | same gene group |
| [[RPE]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[WDR36]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[OTUD6B]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SORD]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[FXN]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OFD1]] | -0.63 | -0.65 / -0.58 | both halves | 8e-06 |  |
| [[BOLA1]] | -0.63 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[MTHFR]] | -0.63 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[MED29]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[GOLGB1]] | -0.60 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[WBP1]] | -0.60 | -0.63 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity raises EEF1E1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity raises EEF1E1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without MCOLN2 | 0.069 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[LINC01357]] | B | LINC01357 activity raises EEF1E1's level | lines that do not express LINC01357 (24) vs lines expressing it (26) | 1.25× lower at baseline in the lines without LINC01357 | 0.084 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, PLBD1, SYN2 |
| [[OVOL1]] | B | OVOL1 activity lowers EEF1E1's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.22× higher at baseline in the lines without OVOL1 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.0, -37.6); signed map (-4.6, -52.0). **Vector** length 88.1, 20.0% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +12.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.9 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation elongation factor 1 epsilon 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:8,073,360-8,102,559 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AIMP3; previously P18 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Aminoacyl tRNA synthetase complex interacting multifunctional proteins |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [O43324](https://www.uniprot.org/uniprotkb/O43324) (Eukaryotic translation elongation factor 1 epsilon-1):

> Positive modulator of ATM response to DNA damage.

**Summary**, from NCBI Gene [9521](https://www.ncbi.nlm.nih.gov/gene/9521):

> This gene encodes a multifunctional protein that localizes to both the cytoplasm and nucleus. In the cytoplasm, the encoded protein is an auxiliary component of the macromolecular aminoacyl-tRNA synthase complex. However, its mouse homolog has been shown to translocate to the nucleus in response to DNA damage, and it plays a positive role in ATM/ATR-mediated p53 activation. Alternative splicing results in multiple transcript variants. Read-through transcription also exists between this gene and …

**Accessions** — [HGNC:3212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3212) · Entrez [9521](https://www.ncbi.nlm.nih.gov/gene/9521) · UniProt [O43324](https://www.uniprot.org/uniprotkb/O43324) · Ensembl [ENSG00000124802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124802)

## Data

Gene col 4576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4576); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4576]; `tensor/DDL_lfc|DDL_z.npy` [4576]; `embed/gene_vectors.npy` [4576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4576 or target_col == 4576). Every well: [[EEF1E1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1E1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
