---
symbol: "PKNOX1"
type: "gene"
col: 8315
ensembl_id: "ENSG00000160199"
name: "PBX/knotted 1 homeobox 1"
location: "21q22.3"
module: 65
arm: "-"
pooled_cpm: 40.38
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# PKNOX1

*PBX/knotted 1 homeobox 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +13.5, q 6e-39, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.623× (z -11.4, q 4e-27, down in 34 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.748× (z -9.8, q 2e-20, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPERG]] (+0.58, fdr 1e-05), [[TUBB4B]] (+0.57, fdr 1e-05), [[DLEU2]] (+0.56, fdr 1e-05); moves opposite to [[SAMM50]] (-0.65, fdr 7e-06), [[GFM2]] (-0.62, fdr 1e-05), [[DFFB]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +13.5 | 6e-39 | 36/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +10.1 | 2e-21 | 30/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +10.0 | 2e-21 | 33/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +8.0 | 2e-13 | 26/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +6.9 | 5e-10 | 28/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +6.3 | 3e-08 | 27/48 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.3 | 9e-06 | 23/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +5.0 | 5e-05 | 21/48 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.9 | 6e-05 | 20/46 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.20× | +4.1 | 0.002 | 19/47 (NCI-H1792, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 22/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.8 | 0.006 | 14/48 (HCT15, SNU-423, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.006 | 10/48 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.6 | 0.014 | 11/48 (SW1417, LS 180, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.015 | 4/48 (LoVo, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.018 | 12/47 (HOP62, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[BI-3406 (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.080 | 2/48 (HOP62, HCT15) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8315.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -11.4 | 4e-27 | 34/46 (NCI-H1792, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -9.8 | 2e-20 | 34/48 (AsPC-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.695×** | -8.4 | 9e-15 | 22/37 (HCT15, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.760×** | -6.6 | 6e-09 | 27/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.777×** | -6.1 | 1e-07 | 25/48 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.768×** | -6.0 | 2e-07 | 25/48 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.787×** | -5.8 | 7e-07 | 22/47 (J82, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.796×** | -5.1 | 3e-05 | 20/43 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.693×** | -4.6 | 3e-04 | 15/35 (NCI-H2347, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.694×** | -4.6 | 3e-04 | 19/46 (Hs 766T, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.713×** | -4.2 | 0.001 | 17/49 (A-172, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.740×** | -3.8 | 0.008 | 15/42 (NCI-H1573, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.855× | -3.6 | 0.012 | 13/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.862× | -3.6 | 0.014 | 17/48 (Panc 03.27, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.864× | -3.5 | 0.015 | 15/48 (A498, PANC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.866× | -3.3 | 0.038 | 8/48 (LoVo, NCI-H2347, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.911× | -3.2 | 0.043 | 9/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.2 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.5 | 5 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -10.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 50.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[LoVo (line)]] | wt | 44.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 32.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.10× (z +14.4) | — |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Decitabine (drug)]] 0.05 µM 0.159× (z -11.4) |
| [[HCT15 (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 31.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 40.1 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.88× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 38.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +12.4) | — |
| [[A-427 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 76.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.287× (z -10.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HOP62 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.309× (z -8.7) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 46.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.182× (z -9.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[RKO (line)]] | wt | 28.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 42.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +9.0) | — |
| [[A-172 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*29 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERG]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TUBB4B]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[DLEU2]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PNRC2]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DEGS1]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[EP300]] | +0.55 | +0.47 / +0.32 | both halves | 2e-04 | pathway: Activation of HOX genes during differentiation; STRING 576 |
| [[BOLA1]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[ERF]] | +0.53 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[KCTD11]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TEX21P]] | +0.53 | +0.63 / +0.28 | both halves | 3e-04 |  |
| [[CUX1]] | +0.53 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TSC22D1]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*71 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMM50]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[GFM2]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DFFB]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[TSNAX]] | -0.61 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[GNPDA2]] | -0.61 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ADH5]] | -0.60 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[EXD2]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ANAPC5]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ACP1]] | -0.59 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[VTI1B]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ATP5F1C]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MRS2]] | -0.58 | -0.43 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-7.1, -11.1); signed map (15.1, -10.1). **Vector** length 95.1, 20.2% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +13.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.3 | +6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +10.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.0 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.7 | -9.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.1 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | PBX/knotted 1 homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,974,510-43,033,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PREP1 |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Reactome | 2 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P55347](https://www.uniprot.org/uniprotkb/P55347) (Homeobox protein PKNOX1):

> Activates transcription in the presence of PBX1A and HOXA1.

**Summary**, from NCBI Gene [5316](https://www.ncbi.nlm.nih.gov/gene/5316):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in angiogenesis and positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within camera-type eye development; hemopoiesis; and regulation of transcription by RNA polymerase II. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9022) · Entrez [5316](https://www.ncbi.nlm.nih.gov/gene/5316) · UniProt [P55347](https://www.uniprot.org/uniprotkb/P55347) · Ensembl [ENSG00000160199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160199)

## Data

Gene col 8315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8315); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8315]; `tensor/DDL_lfc|DDL_z.npy` [8315]; `embed/gene_vectors.npy` [8315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8315 or target_col == 8315). Every well: [[PKNOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKNOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
