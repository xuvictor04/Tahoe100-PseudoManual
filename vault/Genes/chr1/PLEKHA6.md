---
symbol: "PLEKHA6"
type: "gene"
col: 6815
ensembl_id: "ENSG00000143850"
name: "pleckstrin homology domain containing A6"
location: "1q32.1"
module: 17
arm: "-"
pooled_cpm: 59.9
n_lines_expressing: 34
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 18
direction_downstream: 40
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PLEKHA6

*pleckstrin homology domain containing A6* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.25× (z +44.1, q 0e+00, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.766× (z -5.0, q 3e-04, down in 19 of 32 measured lines) ⚠ cell-cycle shift, explains ~22% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 5 lines (RKO 0.190×, LoVo 0.339×, SW48 0.237×, LS 180 0.362×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (SW1417 0.291×, SW48 0.180×, RKO 0.257×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (RKO 0.187×, SW48 0.196×, LoVo 0.316×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.420×); [[Tucidinostat (drug)]] 5 µM in 1 line (SW1417 0.519×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.524×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABR]] (+0.61, fdr 1e-05), [[HTR1D]] (+0.61, fdr 2e-05), [[SSUH2]] (+0.60, fdr 1e-05); moves opposite to [[ARNT]] (-0.65, fdr 1e-05), [[RAD17]] (-0.58, fdr 2e-05), [[SKIC3]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[PRSS22]] → it (grade B ⚠); 40 go from it, the strongest it → [[FLYWCH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.25×** | +44.1 | 0e+00 | 24/32 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +23.4 | 0e+00 | 20/32 (SW 900, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.56×** | +17.7 | 0e+00 | 21/31 (SW 900, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +14.2 | 1e-43 | 19/32 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +11.6 | 3e-29 | 14/27 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +9.1 | 1e-17 | 23/31 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.62×** | +9.1 | 1e-17 | 12/31 (J82, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +8.9 | 3e-17 | 18/31 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.6 | 1e-12 | 13/32 (SW480, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +7.6 | 2e-12 | 25/31 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.4 | 6e-12 | 14/33 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +7.1 | 6e-11 | 22/31 (SW480, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +6.7 | 1e-09 | 19/32 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.5 | 3e-09 | 16/30 (NCI-H2347, SW1417, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.5 | 4e-09 | 20/31 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +6.3 | 1e-08 | 20/32 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +5.8 | 3e-07 | 15/32 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 4e-04 | 14/31 (SW480, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6815.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 5 lines (RKO 0.190×, LoVo 0.339×, SW48 0.237×, LS 180 0.362×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (SW1417 0.291×, SW48 0.180×, RKO 0.257×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (RKO 0.187×, SW48 0.196×, LoVo 0.316×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.420×); [[Tucidinostat (drug)]] 5 µM in 1 line (SW1417 0.519×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.524×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.766×** | -5.0 | 3e-04 | 19/32 (HCT15, SW48, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.865× | -3.8 | 0.035 | 15/32 (SW48, RKO, …) | two highest doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.830× | -3.2 | 0.23 | 9/31 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.27 | 7/31 (NCI-H2347, SNU-423, …) | two highest doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.871× | -3.0 | 0.27 | 11/33 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 38.1 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +20.9) | — |
| [[NCI-H460 (line)]] | wt | 27.3 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +29.6) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.318× (z -8.5) |
| [[SW480 (line)]] | alt | 83.2 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.0) | [[Harringtonine (drug)]] 0.5 µM 0.447× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 25.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 67.4× (z +35.1) | — |
| [[SW48 (line)]] | wt | 118 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 158 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +25.3) | [[Panobinostat (drug)]] 5 µM 0.316× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 43.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +17.3) | — |
| [[SW1417 (line)]] | alt | 108 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.519× (z -10.9) |
| [[HT-29 (line)]] | alt | 198 | 2 | 1 | [[Auranofin (drug)]] 5 µM 2.57× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.2× (z +19.7) | — |
| [[RKO (line)]] | wt | 111 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 74.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 34.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +23.0) | — |
| [[Hs 766T (line)]] | wt | 19.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +15.9) | — |
| [[KATO III (line)]] | alt | 132 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.3) |
| [[LS 180 (line)]] | wt | 132 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.362× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 38.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +18.0) | — |
| [[NCI-H2030 (line)]] | alt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 58.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 20.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +17.9) | — |
| [[A498 (line)]] | wt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 62.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +20.3) | — |
| [[HEC-1-A (line)]] | alt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.176× (z -8.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.74 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABR]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 | same gene group |
| [[HTR1D]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SSUH2]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[MYH15]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SH2D4A]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[FBXW10B]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ARAP2]] | +0.55 | +0.54 / +0.44 | both halves | 3e-05 | same gene group |
| [[TMEM117]] | +0.55 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SH3D19]] | +0.54 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[CD58]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SEPTIN9-DT]] | +0.54 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[ACSL5]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARNT]] | -0.65 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[RAD17]] | -0.58 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[SKIC3]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[NIPSNAP2]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ALG9]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[METTL14]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZDHHC17]] | -0.56 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[GEMIN2]] | -0.55 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[MRPS31P4]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PEX3]] | -0.55 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[COPS4]] | -0.54 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[NCK1]] | -0.54 | -0.54 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS22]] | B | PRSS22 activity raises PLEKHA6's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 4.32× lower at baseline in the lines without PRSS22 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[SLC22A3]] | B | SLC22A3 activity raises PLEKHA6's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 3.15× lower at baseline in the lines without SLC22A3 | 0.014 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[SH2D4A]] | B | SH2D4A activity raises PLEKHA6's level | lines that do not express SH2D4A (11) vs lines expressing it (39) | 3.54× lower at baseline in the lines without SH2D4A | 0.025 | ⚠ within organs, on part of the lines; also absent: IL22RA1, ABCC3, CDA |
| [[SLC2A9]] | B | SLC2A9 activity raises PLEKHA6's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 3.75× lower at baseline in the lines without SLC2A9 | 0.031 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[GPR39]] | B | GPR39 activity raises PLEKHA6's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without GPR39 | 0.034 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[TOP2A]] | B | TOP2A activity lowers PLEKHA6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LMO7DN]] | B | LMO7DN activity raises PLEKHA6's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without LMO7DN | 0.041 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises PLEKHA6's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without SEPTIN9-DT | 0.043 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[MUC17]] | B | MUC17 activity raises PLEKHA6's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 3.49× lower at baseline in the lines without MUC17 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[SYNM]] | B | SYNM activity lowers PLEKHA6's level | lines that do not express SYNM (14) vs lines expressing it (36) | 3.58× higher at baseline in the lines without SYNM | 0.059 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[FBXW10B]] | B | FBXW10B activity raises PLEKHA6's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 2.68× lower at baseline in the lines without FBXW10B | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises PLEKHA6's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without HTR1D | 0.084 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 39, C 1. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLYWCH2]] | B | PLEKHA6 activity lowers FLYWCH2's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.31× higher at baseline in the lines without PLEKHA6 | 0.003 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[ATG4C]] | B | PLEKHA6 activity lowers ATG4C's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.52× higher at baseline in the lines without PLEKHA6 | 0.012 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[SH2D4A]] | B | PLEKHA6 activity raises SH2D4A's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without PLEKHA6 | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[PPP1R15B-AS1]] | B | PLEKHA6 activity raises PPP1R15B-AS1's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without PLEKHA6 | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[KIF3A]] | B | PLEKHA6 activity lowers KIF3A's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.54× higher at baseline in the lines without PLEKHA6 | 0.017 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| cells under [[TAK-733 (drug)]] 0.05 µM | B | PLEKHA6 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express PLEKHA6 (16) vs lines expressing it (32) | the lines without PLEKHA6: 1.17× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[SLFNL1-AS1]] | B | PLEKHA6 activity lowers SLFNL1-AS1's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.48× higher at baseline in the lines without PLEKHA6 | 0.019 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[RANGAP1]] | B | PLEKHA6 activity lowers RANGAP1's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.40× higher at baseline in the lines without PLEKHA6 | 0.019 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[ARL6]] | B | PLEKHA6 activity lowers ARL6's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 2.23× higher at baseline in the lines without PLEKHA6 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[SLC22A3]] | B | PLEKHA6 activity raises SLC22A3's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 4.23× lower at baseline in the lines without PLEKHA6 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[RNF20]] | B | PLEKHA6 activity lowers RNF20's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.32× higher at baseline in the lines without PLEKHA6 | 0.029 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[THAP8]] | B | PLEKHA6 activity lowers THAP8's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.35× higher at baseline in the lines without PLEKHA6 | 0.032 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (33.6, -5.3); signed map (52.3, 5.9). **Vector** length 107, 29.0% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +44.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +23.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +6.4 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +17.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +7.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +5.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +4.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.1 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -0.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,218,853-204,378,214 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEPP3, KIAA0969 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

UniProt [Q9Y2H5](https://www.uniprot.org/uniprotkb/Q9Y2H5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:17053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17053) · Entrez [22874](https://www.ncbi.nlm.nih.gov/gene/22874) · UniProt [Q9Y2H5](https://www.uniprot.org/uniprotkb/Q9Y2H5) · Ensembl [ENSG00000143850](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143850)

## Data

Gene col 6815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6815); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6815]; `tensor/DDL_lfc|DDL_z.npy` [6815]; `embed/gene_vectors.npy` [6815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6815 or target_col == 6815). Every well: [[PLEKHA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
