---
symbol: "NAA35"
type: "gene"
col: 5637
ensembl_id: "ENSG00000135040"
name: "N-alpha-acetyltransferase 35, NatC auxiliary subunit"
location: "9q21.33"
module: 56
arm: "+"
pooled_cpm: 134.19
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# NAA35

*N-alpha-acetyltransferase 35, NatC auxiliary subunit* — 9q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.06× (z +9.0, q 1e-16, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.684× (z -12.0, q 3e-30, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKS3]] (+0.71, fdr 7e-06), [[TMEM243]] (+0.67, fdr 1e-05), [[SEC63]] (+0.67, fdr 9e-06); moves opposite to [[PNRC2]] (-0.61, fdr 1e-05), [[HNRNPK]] (-0.60, fdr 1e-05), [[CARD6]] (-0.58, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +9.0 | 1e-16 | 43/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.8 | 2e-06 | 33/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.4 | 1e-05 | 25/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.008 | 18/48 (NCI-H2030, KATO III, …) | two highest doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.079 | 16/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | 1.27× | +3.0 | 0.24 | 14/48 (MIA PaCa-2, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -12.0 | 3e-30 | 41/49 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.627×** | -11.1 | 3e-26 | 37/49 (RKO, A498, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.637×** | -10.0 | 4e-21 | 36/45 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.664×** | -9.4 | 8e-19 | 34/44 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.762×** | -8.5 | 3e-15 | 34/48 (HS-578T, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.725×** | -7.7 | 2e-12 | 35/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.752×** | -6.8 | 8e-10 | 35/48 (RPMI-7951, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -6.6 | 3e-09 | 30/48 (SNU-1, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -6.5 | 5e-09 | 34/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.767×** | -6.3 | 1e-08 | 32/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.762×** | -6.2 | 2e-08 | 28/48 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.797×** | -5.2 | 1e-05 | 28/50 (J82, HS-578T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.809×** | -5.0 | 2e-05 | 29/48 (J82, NCI-H460, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.742×** | -5.0 | 3e-05 | 27/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.814×** | -4.7 | 9e-05 | 26/48 (SNU-423, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.879× | -4.1 | 0.001 | 11/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.008 | 24/48 (MIA PaCa-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.875× | -3.2 | 0.034 | 8/49 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.040 | 18/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.881× | -3.0 | 0.053 | 13/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.900× | -3.0 | 0.055 | 5/48 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 171 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -16.6) |
| [[HS-578T (line)]] | alt | 135 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -13.3) |
| [[A498 (line)]] | wt | 236 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -13.9) |
| [[SW480 (line)]] | alt | 149 | 4 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 3.12× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.645× (z -9.1) |
| [[A549 (line)]] | wt | 161 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.1) |
| [[LoVo (line)]] | wt | 165 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 125 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -14.0) |
| [[A-172 (line)]] | wt | 170 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 126 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.333× (z -15.4) |
| [[A-427 (line)]] | wt | 83.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.607× (z -8.8) |
| [[HOP62 (line)]] | alt | 151 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -8.8) |
| [[KATO III (line)]] | alt | 137 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.61× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.452× (z -8.6) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -25.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 132 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -9.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -8.6) |
| [[C-33 A (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -11.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 172 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.79× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 149 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -9.6) ⚠ cell-cycle shift, explains ~1% of this change |
| [[NCI-H460 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 85.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.85× (z +9.1) | — |
| [[RKO (line)]] | wt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -19.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 91.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0980× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -11.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -12.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 127 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS3]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[TMEM243]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SEC63]] | +0.67 | +0.73 / +0.57 | both halves | 9e-06 |  |
| [[PDXDC2P]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[MCEE]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PDXDC2P-NPIPB14P]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SEC13]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[HM13]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SLC17A5]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[KDELR2]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[COG6]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | -0.61 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CARD6]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[EIF4G2]] | -0.58 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[BMPR1B]] | -0.58 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[ZNF564]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.56 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[ZNF468]] | -0.56 | -0.71 / -0.47 | both halves | 2e-05 |  |
| [[NCOA4]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[TIGD6]] | -0.55 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[TSPYL1]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[BAZ2B]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NAA35's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.5, -33.7); signed map (-50.5, 8.5). **Vector** length 91.3, 25.5% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.51 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.51 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | -0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.4 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +0.8 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -6.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.0 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -4.5 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 35, NatC auxiliary subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.33 — chr9:85,941,146-86,025,462 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21613, FLJ22643, bA379P1.1; previously MAK10 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VZE5](https://www.uniprot.org/uniprotkb/Q5VZE5) (N-alpha-acetyltransferase 35, NatC auxiliary subunit):

> Auxillary component of the N-terminal acetyltransferase C (NatC) complex which catalyzes acetylation of N-terminal methionine residues. N-terminal acetylation protects proteins from ubiquitination and degradation by the N-end rule pathway. Involved in regulation of apoptosis and proliferation of smooth muscle cells.

**Summary**, from NCBI Gene [60560](https://www.ncbi.nlm.nih.gov/gene/60560):

> Predicted to enable transferase activity. Involved in negative regulation of apoptotic process. Located in cytosol. Part of NatC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24340) · Entrez [60560](https://www.ncbi.nlm.nih.gov/gene/60560) · UniProt [Q5VZE5](https://www.uniprot.org/uniprotkb/Q5VZE5) · Ensembl [ENSG00000135040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135040)

## Data

Gene col 5637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5637); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5637]; `tensor/DDL_lfc|DDL_z.npy` [5637]; `embed/gene_vectors.npy` [5637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5637 or target_col == 5637). Every well: [[NAA35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
