---
symbol: "GPRIN1"
type: "gene"
col: 9789
ensembl_id: "ENSG00000169258"
name: "G protein regulated inducer of neurite outgrowth 1"
location: "5q35.2"
module: 82
arm: "+"
pooled_cpm: 5.57
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# GPRIN1

*G protein regulated inducer of neurite outgrowth 1* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 5.35× (z +20.2, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.686× (z -6.4, q 8e-08, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF21B]] (+0.71, fdr 1e-05), [[CCNE1]] (+0.68, fdr 1e-05), [[GNAZ]] (+0.68, fdr 1e-05); moves opposite to [[MFF-DT]] (-0.70, fdr 3e-05), [[ERCC6L2-AS1]] (-0.69, fdr 3e-04), [[TP53]] (-0.67, fdr 3e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[RAB39A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **5.35×** | +20.2 | 0e+00 | 45/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.27×** | +20.1 | 0e+00 | 43/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.13×** | +17.1 | 0e+00 | 45/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +10.5 | 1e-23 | 33/45 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.38×** | +10.5 | 1e-23 | 36/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.24×** | +9.7 | 2e-20 | 24/35 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.12×** | +9.1 | 1e-17 | 13/22 (A498, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.87×** | +7.3 | 2e-11 | 5/10 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +6.7 | 1e-09 | 20/39 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.66×** | +5.9 | 2e-07 | 12/27 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.52×** | +5.8 | 3e-07 | 18/43 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +5.6 | 1e-06 | 13/43 (SW480, NCI-H460, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.49×** | +4.8 | 6e-05 | 13/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.50×** | +4.6 | 2e-04 | 7/16 (SW 900, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +4.5 | 2e-04 | 13/44 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.014 | 4/36 (A498, NCI-H1573, …) | two highest doses | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.73×** | +3.5 | 0.016 | 2/24 (PANC-1, A498) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.016 | 3/38 (SW 900, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.038 | 4/40 (NCI-H460, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.068 | 8/40 (SW480, NCI-H2347, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.068 | 5/29 (NCI-H460, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -6.4 | 8e-08 | 22/41 (SHP-77, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -5.6 | 5e-06 | 18/45 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.721×** | -5.6 | 5e-06 | 20/44 (A-172, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -5.2 | 2e-05 | 15/43 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.636×** | -5.2 | 2e-05 | 19/41 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.657×** | -5.1 | 4e-05 | 14/39 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.685×** | -4.5 | 4e-04 | 9/45 (NCI-H661, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.498×** | -4.4 | 8e-04 | 11/30 (RKO, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -4.0 | 0.003 | 13/35 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.717×** | -4.0 | 0.004 | 14/36 (C-33 A, NCI-H23, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -3.9 | 0.005 | 16/44 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.804×** | -3.7 | 0.009 | 17/40 (A-427, SW48, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.734×** | -3.7 | 0.009 | 15/42 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.024 | 8/44 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.754×** | -3.4 | 0.026 | 7/45 (SNU-1, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 12.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0680× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0819× (z -10.2) |
| [[SW480 (line)]] | alt | 7.43 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.10× (z +10.0) | — |
| [[A-172 (line)]] | wt | 9.45 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.170× (z -8.5) |
| [[A-427 (line)]] | wt | 17.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0969× (z -14.0) |
| [[A549 (line)]] | wt | 5.61 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0564× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Canagliflozin (drug)]] 5 µM 0.0883× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 5.54 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0705× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 5.29 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0742× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 4.11 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0652× (z -11.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 4.70 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.35× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.42 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0490× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 7.76 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 3.01 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.62× (z +9.0) | — |
| [[SW48 (line)]] | wt | 7.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -11.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A498 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF21B]] | +0.71 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CCNE1]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.68 | +0.54 / +0.60 | both halves | 1e-05 | STRING 776 |
| [[LRFN3]] | +0.67 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[EHD4]] | +0.66 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[KCTD17]] | +0.66 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[JAKMIP1]] | +0.65 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[RIMS3]] | +0.65 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ADAMTSL5]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.63 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TPST2]] | +0.63 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[FAM124A]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | -0.70 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ERCC6L2-AS1]] | -0.69 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[TP53]] | -0.67 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[LINC00869-1]] | -0.65 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[DNAI4]] | -0.65 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[NIFK-AS1]] | -0.65 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[PNISR-AS1]] | -0.65 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[RNF146]] | -0.65 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[HOXB7]] | -0.65 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[MAIP1]] | -0.64 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[CASS4]] | -0.64 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[GALNT7-DT]] | -0.63 | -0.44 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[LINC01004]] | -0.63 | -0.42 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB39A]] | B | RAB39A activity raises GPRIN1's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without RAB39A | 0.012 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[RET]] | B | RET activity raises GPRIN1's level | lines that do not express RET (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without RET | 0.014 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[DPYSL5]] | B | DPYSL5 activity raises GPRIN1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without DPYSL5 | 0.014 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[KIF1A]] | B | KIF1A activity raises GPRIN1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without KIF1A | 0.015 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[GNAZ]] | B | GNAZ activity raises GPRIN1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.94× lower at baseline in the lines without GNAZ | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[KIF26A]] | B | KIF26A activity raises GPRIN1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.90× lower at baseline in the lines without KIF26A | 0.036 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[CARMIL2]] | B | CARMIL2 activity raises GPRIN1's level | lines that do not express CARMIL2 (6) vs lines expressing it (44) | 2.33× lower at baseline in the lines without CARMIL2 | 0.054 | ⚠ within organs, on part of the lines; also absent: CHN1, HCN2, QKI; maybe low, not absent |
| [[LANCL3]] | B | LANCL3 activity lowers GPRIN1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.45× higher at baseline in the lines without LANCL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[ABCA3]] | B | ABCA3 activity raises GPRIN1's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without ABCA3 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.3, 15.9); signed map (-40.1, -7.5). **Vector** length 80.1, 14.6% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +20.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +17.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +10.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +20.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +10.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +5.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.4 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein regulated inducer of neurite outgrowth 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,595,802-176,610,156 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRIN1, KIAA1893 |
| Reactome | 2 pathways, smallest: MECP2 regulates neuronal receptors and channels; Transcriptional Regulation by MECP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2K8](https://www.uniprot.org/uniprotkb/Q7Z2K8) (G protein-regulated inducer of neurite outgrowth 1):

> May be involved in neurite outgrowth.

**Summary**, from NCBI Gene [114787](https://www.ncbi.nlm.nih.gov/gene/114787):

> Predicted to enable phosphoprotein binding activity. Predicted to be involved in neuron projection development. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24835](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24835) · Entrez [114787](https://www.ncbi.nlm.nih.gov/gene/114787) · UniProt [Q7Z2K8](https://www.uniprot.org/uniprotkb/Q7Z2K8) · Ensembl [ENSG00000169258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169258)

## Data

Gene col 9789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9789); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9789]; `tensor/DDL_lfc|DDL_z.npy` [9789]; `embed/gene_vectors.npy` [9789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9789 or target_col == 9789). Every well: [[GPRIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
