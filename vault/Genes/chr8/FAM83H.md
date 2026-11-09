---
symbol: "FAM83H"
type: "gene"
col: 11149
ensembl_id: "ENSG00000180921"
name: "scaffolding CK1 anchoring protein H"
location: "8q24.3"
module: 1
arm: "+"
pooled_cpm: 16.72
n_lines_expressing: 37
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FAM83H

*scaffolding CK1 anchoring protein H* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.45× (z +10.2, q 2e-21, up in 25 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.89× (z +7.2, q 1e-10, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.306× (z -13.4, q 2e-38, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM185B]] (+0.69, fdr 7e-06), [[GPATCH4]] (+0.65, fdr 7e-06), [[COA7]] (+0.62, fdr 1e-05); moves opposite to [[NUCB2]] (-0.63, fdr 1e-05), [[SAP30-DT]] (-0.63, fdr 1e-05), [[ARL3]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MDFI]] → it (grade B ⚠); 5 go from it, the strongest it → [[LCORL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +10.2 | 2e-21 | 25/28 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +9.6 | 2e-19 | 16/20 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +7.2 | 1e-10 | 23/35 (AsPC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.8 | 2e-09 | 16/25 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +5.6 | 3e-06 | 22/34 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.0 | 4e-05 | 19/34 (AsPC-1, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +4.8 | 1e-04 | 22/33 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.8 | 1e-04 | 15/30 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.5 | 5e-04 | 17/33 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.003 | 13/35 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.9 | 0.006 | 16/33 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.015 | 13/34 (AsPC-1, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.4 | 0.033 | 10/25 (LS 180, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.046 | 10/33 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.073 | 9/33 (MIA PaCa-2, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.076 | 12/33 (Panc 03.27, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.076 | 4/34 (AsPC-1, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.306×** | -13.4 | 2e-38 | 29/35 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.454×** | -12.7 | 3e-34 | 28/32 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.337×** | -12.3 | 1e-32 | 30/35 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.351×** | -11.9 | 2e-30 | 29/35 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.496×** | -8.0 | 2e-13 | 24/35 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -6.7 | 2e-09 | 24/35 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.662×** | -6.6 | 3e-09 | 21/33 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.353×** | -6.2 | 4e-08 | 23/34 (RKO, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.594×** | -5.9 | 2e-07 | 22/33 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -4.9 | 4e-05 | 20/34 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -4.6 | 2e-04 | 22/34 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.013 | 19/35 (RKO, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.731×** | -3.6 | 0.016 | 13/35 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.737×** | -3.5 | 0.022 | 16/34 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -3.3 | 0.041 | 16/34 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.041 | 15/34 (NCI-H23, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 45.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.6) |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0477× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0867× (z -13.9) |
| [[RKO (line)]] | wt | 30.1 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0864× (z -15.0) |
| [[KATO III (line)]] | alt | 45.8 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -15.1) |
| [[A-427 (line)]] | wt | 22.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.175× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 37.8 | 2 | 2 | [[Harringtonine (drug)]] 0.5 µM 3.92× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.7) |
| [[LS 180 (line)]] | wt | 37.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.2) |
| [[SW480 (line)]] | alt | 15.0 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -13.6) |
| [[HT-29 (line)]] | alt | 27.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -11.9) |
| [[A498 (line)]] | wt | 21.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.36× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 35.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -10.3) |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 6.10 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.173× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -9.7) |
| [[PANC-1 (line)]] | alt | 9.92 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.4) |
| [[SW48 (line)]] | wt | 28.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0612× (z -13.1) |
| [[BT-474 (line)]] | alt | 35.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -10.9) |
| [[C32 (line)]] | wt | 5.42 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0731× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 28.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.0) |
| [[HOP62 (line)]] | alt | 5.42 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0473× (z -13.5) |
| [[A-172 (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.922 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 35.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[COA7]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ZNF195]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TRMT61A]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CENPBD1P]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[JMJD4]] | +0.61 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[IFRD2]] | +0.61 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PSD4]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[GRWD1]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[B3GALT6]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[MAK16]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCB2]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SAP30-DT]] | -0.63 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ARL3]] | -0.61 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.60 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[SRP54-AS1]] | -0.60 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[VKORC1]] | -0.59 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[DPM3]] | -0.58 | -0.70 / -0.36 | both halves | 1e-04 |  |
| [[KDELR1]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NDUFA2]] | -0.57 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SERF2]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SPICE1]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TRIM52-AS1]] | -0.56 | -0.67 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDFI]] | B | MDFI activity raises FAM83H's level | lines that do not express MDFI (25) vs lines expressing it (25) | 3.44× lower at baseline in the lines without MDFI | 0.005 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[EPPK1]] | B | EPPK1 activity raises FAM83H's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 3.34× lower at baseline in the lines without EPPK1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[LAD1]] | B | LAD1 activity raises FAM83H's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.42× lower at baseline in the lines without LAD1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[DSC2]] | B | DSC2 activity raises FAM83H's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.09× lower at baseline in the lines without DSC2 | 0.045 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[HTR1D]] | B | HTR1D activity raises FAM83H's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without HTR1D | 0.046 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[PRKAR1B]] | B | PRKAR1B activity raises FAM83H's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 2.91× lower at baseline in the lines without PRKAR1B | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MISP]] | C | MISP activity raises FAM83H's level | lines that do not express MISP (23) vs lines expressing it (27) | 3.73× lower at baseline in the lines without MISP | 0.011 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B; co-absent with the target |
| [[PKP3]] | C | PKP3 activity raises FAM83H's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 3.80× lower at baseline in the lines without PKP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent; co-absent with the target |
| [[SFN]] | C | SFN activity raises FAM83H's level | lines that do not express SFN (20) vs lines expressing it (30) | 3.83× lower at baseline in the lines without SFN | 0.039 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |
| [[EVPL]] | C | EVPL activity raises FAM83H's level | lines that do not express EVPL (16) vs lines expressing it (34) | 4.57× lower at baseline in the lines without EVPL | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LCORL]] | B | FAM83H activity lowers LCORL's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 1.19× higher at baseline in the lines without FAM83H | 0.032 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN |
| [[PIK3C2A]] | B | FAM83H activity raises PIK3C2A's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without FAM83H | 0.079 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN |
| [[MDFI]] | B | FAM83H activity raises MDFI's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 2.38× lower at baseline in the lines without FAM83H | 0.087 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN |
| [[PKP3]] | C | FAM83H activity raises PKP3's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 3.40× lower at baseline in the lines without FAM83H | 0.028 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN; co-absent with the target |
| [[EVPL]] | C | FAM83H activity raises EVPL's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 4.06× lower at baseline in the lines without FAM83H | 0.076 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN; co-absent with the target |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.6, -35.5); signed map (1.5, -43.7). **Vector** length 96.4, 27.9% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -12.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -6.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | scaffolding CK1 anchoring protein H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,723,933-143,738,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46072; previously FAM83H |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Scaffolding anchor of CK1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZRV2](https://www.uniprot.org/uniprotkb/Q6ZRV2) (Scaffolding CK1 anchoring protein H):

> May play a major role in the structural organization and calcification of developing enamel. May play a role in keratin cytoskeleton disassembly by recruiting CSNK1A1 to keratin filaments. Thereby, it may regulate epithelial cell migration.

**Summary**, from NCBI Gene [286077](https://www.ncbi.nlm.nih.gov/gene/286077):

> The protein encoded by this gene plays an important role in the structural development and calcification of tooth enamel. Defects in this gene are a cause of amelogenesis imperfecta type 3 (AI3). [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:24797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24797) · Entrez [286077](https://www.ncbi.nlm.nih.gov/gene/286077) · UniProt [Q6ZRV2](https://www.uniprot.org/uniprotkb/Q6ZRV2) · Ensembl [ENSG00000180921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180921)

## Data

Gene col 11149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11149); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11149]; `tensor/DDL_lfc|DDL_z.npy` [11149]; `embed/gene_vectors.npy` [11149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11149 or target_col == 11149). Every well: [[FAM83H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM83H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
