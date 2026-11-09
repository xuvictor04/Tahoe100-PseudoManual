---
symbol: "APRG1"
type: "gene"
col: 12624
ensembl_id: "ENSG00000198590"
name: "APRG1 tumor suppressor candidate"
location: "3p22.2"
module: 38
arm: "+"
pooled_cpm: 37.89
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# APRG1

*APRG1 tumor suppressor candidate* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +6.9, q 4e-09, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.300× (z -11.9, q 1e-29, down in 41 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Pralsetinib (drug)]] 5 µM: 0.470× (z -4.0, q 0.005, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORIN]] (+0.70, fdr 7e-06), [[DNHD1]] (+0.70, fdr 7e-06), [[FBXO10]] (+0.69, fdr 7e-06); moves opposite to [[LANCL1]] (-0.61, fdr 1e-05), [[TERF1]] (-0.55, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +6.9 | 4e-09 | 33/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +5.2 | 6e-05 | 32/48 (A-172, C32, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.024 | 28/48 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.4 | 0.11 | 2/48 (HOP62, NCI-H23) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 1.36× | +3.1 | 0.19 | 19/48 (HOP62, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.300×** | -11.9 | 1e-29 | 41/47 (COLO 205, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.380×** | -9.9 | 1e-20 | 37/47 (HepG2/C3A, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.412×** | -8.7 | 4e-16 | 28/36 (J82, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.499×** | -6.6 | 6e-09 | 28/42 (LS 180, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.610×** | -5.1 | 4e-05 | 30/46 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.470×** | -4.0 | 0.005 | 29/47 (HCT15, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.681×** | -3.8 | 0.011 | 26/48 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.679×** | -3.7 | 0.011 | 27/47 (NCI-H23, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.694×** | -3.7 | 0.011 | 24/48 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.681×** | -3.7 | 0.011 | 27/48 (hTERT-HPNE, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.712×** | -3.5 | 0.026 | 21/48 (CHP-212, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.800×** | -3.2 | 0.057 | 23/48 (A549, KATO III, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.740×** | -3.1 | 0.087 | 22/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.732×** | -3.1 | 0.087 | 22/48 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.746× | -3.0 | 0.10 | 21/47 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 60.8 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -12.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -10.3) |
| [[HCT15 (line)]] | alt | 74.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0620× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 53.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0709× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.119× (z -13.4) |
| [[SNU-1 (line)]] | wt | 59.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.70× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 35.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HEC-1-A (line)]] | alt | 74.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 34.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HT-29 (line)]] | alt | 56.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 32.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0411× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 67.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 83.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.208× (z -9.6) |
| [[HS-578T (line)]] | alt | 53.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[hTERT-HPNE (line)]] | wt | 68.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 37.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -8.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 38.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 37.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0696× (z -13.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 74.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -12.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.252× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0738× (z -14.3) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0343× (z -16.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0647× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0804× (z -14.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.118× (z -13.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -13.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0767× (z -11.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -13.0) ⚠ toxic |
| [[A498 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORIN]] | +0.70 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[DNHD1]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[FBXO10]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CCNP]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[UBE2CP5]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TINCR]] | +0.67 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[GRK7]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TICAM2]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL1]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[TERF1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, -19.8); signed map (10.8, 7.8). **Vector** length 128, 40.7% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.2 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +3.1 | +3.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.9 | +1.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.5 | -3.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -4.1 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.0 | -3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.9 | -2.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | APRG1 tumor suppressor candidate |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p22.2 — chr3:37,381,062-37,440,186 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C3orf35 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

UniProt [Q8IVJ8](https://www.uniprot.org/uniprotkb/Q8IVJ8) carries no function annotation.

**Summary**, from NCBI Gene [339883](https://www.ncbi.nlm.nih.gov/gene/339883):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24082) · Entrez [339883](https://www.ncbi.nlm.nih.gov/gene/339883) · UniProt [Q8IVJ8](https://www.uniprot.org/uniprotkb/Q8IVJ8) · Ensembl [ENSG00000198590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198590)

## Data

Gene col 12624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12624); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12624]; `tensor/DDL_lfc|DDL_z.npy` [12624]; `embed/gene_vectors.npy` [12624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12624 or target_col == 12624). Every well: [[APRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
