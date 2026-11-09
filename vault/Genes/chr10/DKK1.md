---
symbol: "DKK1"
type: "gene"
col: 2908
ensembl_id: "ENSG00000107984"
name: "dickkopf Wnt signaling pathway inhibitor 1"
location: "10q21.1"
module: 120
arm: "+"
pooled_cpm: 28.03
n_lines_expressing: 30
n_dd_up: 32
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# DKK1

*dickkopf Wnt signaling pathway inhibitor 1* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.85× (z +7.0, q 1e-09, up in 17 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.522× (z -7.4, q 9e-11, down in 24 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKG1-AS1]] (+0.64, fdr 7e-06, ⚠ same locus), [[GREB1L]] (+0.57, fdr 1e-05), [[EGFR]] (+0.54, fdr 1e-05), [[PSD3]] (+0.54, fdr 2e-05); moves opposite to [[MIA2]] (-0.48, fdr 4e-05), [[TCEA1]] (-0.47, fdr 5e-05), [[NBR2]] (-0.46, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPHA2]] → it (grade B ⚠); 4 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +7.0 | 1e-09 | 17/28 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.38×** | +6.9 | 1e-09 | 16/27 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.09×** | +5.9 | 7e-07 | 15/27 (NCI-H460, LS 180, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.92×** | +5.2 | 2e-05 | 14/26 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.82×** | +4.8 | 2e-04 | 11/27 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **2.27×** | +4.6 | 4e-04 | 13/27 (SW 900, LS 180, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.77×** | +4.6 | 4e-04 | 12/27 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.80×** | +4.5 | 4e-04 | 13/27 (LS 180, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.3 | 9e-04 | 8/24 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +4.2 | 0.002 | 11/28 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +4.1 | 0.002 | 13/27 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.61×** | +3.8 | 0.006 | 8/27 (LS 180, SW 900, …) | all doses, flat | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **2.38×** | +3.6 | 0.012 | 8/26 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.012 | 10/27 (LoVo, A-172, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.57×** | +3.6 | 0.012 | 12/28 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.56×** | +3.6 | 0.012 | 11/28 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.014 | 12/28 (NCI-H1573, J82, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.017 | 9/27 (HCT15, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.026 | 10/27 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.028 | 7/27 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.035 | 8/27 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.47×** | +3.1 | 0.048 | 7/27 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.048 | 9/27 (LS 180, SW 900, …) | all doses, stronger at high dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.060 | 4/28 (A-172, AsPC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -7.4 | 9e-11 | 24/27 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.495×** | -5.6 | 5e-06 | 18/27 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.556×** | -4.5 | 0.001 | 17/27 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.695×** | -4.1 | 0.004 | 15/28 (A-172, HCT15, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **0.580×** | -4.1 | 0.004 | 17/28 (LoVo, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.391×** | -3.9 | 0.008 | 17/27 (Hs 766T, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.629×** | -3.7 | 0.016 | 15/27 (HCT15, AN3 CA, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.653×** | -3.4 | 0.044 | 12/27 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.747×** | -3.3 | 0.055 | 17/28 (HCT15, LoVo, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.664×** | -3.3 | 0.055 | 15/27 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.748×** | -3.3 | 0.055 | 12/28 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.670×** | -3.2 | 0.061 | 13/27 (LoVo, J82, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **0.676×** | -3.1 | 0.074 | 15/27 (LoVo, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 197 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0479× (z -23.1) |
| [[AsPC-1 (line)]] | alt | 105 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0998× (z -18.7) |
| [[A-427 (line)]] | wt | 277 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0702× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -12.8) |
| [[Hs 766T (line)]] | wt | 127 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0793× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0804× (z -13.4) |
| [[LoVo (line)]] | wt | 57.5 | 0 | 8 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.133× (z -11.4) |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 5 (2 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0256× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 11.3 | 1 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 0.05 µM 5.74× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0607× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -9.7) |
| [[A549 (line)]] | wt | 11.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0618× (z -9.9) |
| [[KATO III (line)]] | alt | 15.7 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0613× (z -10.8) |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 72.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0989× (z -10.5) |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0349× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKG1-AS1]] | +0.64 | +0.65 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GREB1L]] | +0.57 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[EGFR]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 | STRING 535 |
| [[PSD3]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[IL1R2]] | +0.53 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[CCN1]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CD59]] | +0.52 | +0.63 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[RASAL2]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[LINC00707]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CASC19]] | +0.50 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[LUZP1]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[HAS3]] | +0.50 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[F3]] | +0.49 | +0.50 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIA2]] | -0.48 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[TCEA1]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[NBR2]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[PPP1R3E]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ALDH2]] | -0.46 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[NUPR1]] | -0.43 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[IDH1]] | -0.42 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[NADSYN1]] | -0.42 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[RAB21]] | -0.42 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[CSDE1]] | -0.42 | -0.32 / -0.42 | both halves | 1e-04 |  |
| [[EPB41]] | -0.42 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[MCCC1]] | -0.42 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | EPHA2 activity raises DKK1's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 2.89× lower at baseline in the lines without EPHA2 | 0.072 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[PRKG1-AS1]] | C | PRKG1-AS1 activity raises DKK1's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 3.92× lower at baseline in the lines without PRKG1-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | DKK1 activity raises EPHA2's level | lines that do not express DKK1 (20) vs lines expressing it (30) | 2.03× lower at baseline in the lines without DKK1 | 0.044 | ⚠ within organs, on part of the lines; also absent: CACNG4, PALM, CRIP1 |
| [[THSD4]] | B | DKK1 activity raises THSD4's level | lines that do not express DKK1 (20) vs lines expressing it (30) | 3.46× lower at baseline in the lines without DKK1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CACNG4, PALM, CRIP1 |
| [[IDH1]] | B | DKK1 activity raises IDH1's level | lines that do not express DKK1 (20) vs lines expressing it (30) | 1.18× lower at baseline in the lines without DKK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CACNG4, PALM, CRIP1 |
| [[PRKG1-AS1]] | C | DKK1 activity raises PRKG1-AS1's level | lines that do not express DKK1 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without DKK1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CACNG4, PALM, CRIP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.1, 10.8); signed map (13.1, 39.5). **Vector** length 99.8, 27.5% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.0 | +4.6 |
|  | [[vincristine (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +4.5 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.0 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | dickkopf Wnt signaling pathway inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:52,314,281-52,318,042 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SK, DKK-1 |
| Gene groups (HGNC) | Dickkopf family |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 8 pathways, smallest: Signaling by LRP5 mutants; POU5F1 (OCT4), SOX2, NANOG repress genes related to differentiation; Negative regulation of TCF-dependent signaling by WNT ligand antagonists |
| Matched by | ensembl_id |

**Function**, from UniProt [O94907](https://www.uniprot.org/uniprotkb/O94907) (Dickkopf-related protein 1):

> Antagonizes canonical Wnt signaling by inhibiting LRP5/6 interaction with Wnt and by forming a ternary complex with the transmembrane protein KREMEN that promotes internalization of LRP5/6. DKKs play an important role in vertebrate development, where they locally inhibit Wnt regulated processes such as antero-posterior axial patterning, limb development, somitogenesis and eye formation. In the adult, Dkks are implicated in bone formation and bone disease, cancer and Alzheimer disease. Inhibits …

**Summary**, from NCBI Gene [22943](https://www.ncbi.nlm.nih.gov/gene/22943):

> This gene encodes a member of the dickkopf family of proteins. Members of this family are secreted proteins characterized by two cysteine-rich domains that mediate protein-protein interactions. The encoded protein binds to the LRP6 co-receptor and inhibits beta-catenin-dependent Wnt signaling. This gene plays a role in embryonic development and may be important in bone formation in adults. Elevated expression of this gene has been observed in numerous human cancers and this protein may promote …

**Accessions** — [HGNC:2891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2891) · Entrez [22943](https://www.ncbi.nlm.nih.gov/gene/22943) · UniProt [O94907](https://www.uniprot.org/uniprotkb/O94907) · Ensembl [ENSG00000107984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107984)

## Data

Gene col 2908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2908); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2908]; `tensor/DDL_lfc|DDL_z.npy` [2908]; `embed/gene_vectors.npy` [2908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2908 or target_col == 2908). Every well: [[DKK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DKK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
