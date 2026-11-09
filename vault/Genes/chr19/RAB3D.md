---
symbol: "RAB3D"
type: "gene"
col: 2613
ensembl_id: "ENSG00000105514"
name: "RAB3D, member RAS oncogene family"
location: "19p13.2"
module: 45
arm: "+"
pooled_cpm: 11.64
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# RAB3D

*RAB3D, member RAS oncogene family* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.59× (z +12.5, q 3e-33, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.414× (z -11.5, q 4e-28, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCA2]] (+0.63, fdr 1e-05), [[BCAM]] (+0.63, fdr 2e-05), [[SLC25A23]] (+0.62, fdr 1e-05); moves opposite to [[PSMD6-AS2]] (-0.58, fdr 3e-05), [[ANKRD17-DT]] (-0.57, fdr 5e-05), [[PBDC1]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +12.5 | 3e-33 | 40/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +11.0 | 2e-25 | 38/45 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +8.2 | 5e-14 | 34/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.0 | 3e-10 | 14/20 (SW48, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.4 | 1e-08 | 27/46 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.9 | 4e-07 | 18/35 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +4.8 | 1e-04 | 18/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +4.4 | 7e-04 | 10/27 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.035 | 13/46 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.081 | 12/43 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Erlotinib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.081 | 7/45 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.093 | 6/42 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +3.1 | 0.098 | 10/39 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.414×** | -11.5 | 4e-28 | 38/45 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.449×** | -10.5 | 3e-23 | 31/43 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.440×** | -10.3 | 1e-22 | 32/43 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -8.1 | 5e-14 | 32/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -7.5 | 7e-12 | 24/43 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.698×** | -6.6 | 3e-09 | 26/44 (BT-474, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -6.3 | 2e-08 | 25/45 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.641×** | -5.8 | 4e-07 | 22/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -5.5 | 2e-06 | 24/45 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.650×** | -5.4 | 3e-06 | 20/37 (Panc 03.27, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -4.6 | 3e-04 | 17/45 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -4.5 | 4e-04 | 15/42 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.734×** | -4.0 | 0.002 | 14/45 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -4.0 | 0.002 | 19/39 (J82, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.758×** | -3.6 | 0.011 | 11/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.758×** | -3.6 | 0.011 | 17/45 (SW 1271, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.011 | 19/43 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.018 | 17/46 (Hs 766T, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.777×** | -3.3 | 0.031 | 15/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 53.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.183× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 24.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -12.5) |
| [[KATO III (line)]] | alt | 7.68 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.148× (z -8.5) |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0976× (z -12.1) |
| [[SW480 (line)]] | alt | 4.92 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.86× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0955× (z -9.4) |
| [[HS-578T (line)]] | alt | 5.61 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0938× (z -9.1) |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -14.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[J82 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.185× (z -9.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0969× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.177× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0889× (z -11.5) |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA2]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[BCAM]] | +0.63 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SLC25A23]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[BCKDK]] | +0.60 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[LMTK3]] | +0.57 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[PIK3R2]] | +0.57 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[SNRNP200]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[NIPSNAP1]] | +0.56 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[NDRG3]] | +0.56 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[HDAC1]] | +0.55 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[ENTPD2]] | +0.55 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[P2RY2]] | +0.55 | +0.60 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS2]] | -0.58 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD17-DT]] | -0.57 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[PBDC1]] | -0.55 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[ZNF785]] | -0.55 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[BAZ1A]] | -0.54 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[CDR2]] | -0.53 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ATE1OSP]] | -0.52 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PRANCR]] | -0.52 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | -0.52 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[GCNT4]] | -0.52 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[GTF2IRD2B]] | -0.52 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[LINC02100]] | -0.51 | -0.43 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.1, -5.7); signed map (-28.7, -4.3). **Vector** length 83.3, 16.6% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -2.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -10.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | RAB3D, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,322,068-11,346,270 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAB16, D2-2, RAD3D; previously GOV |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 3 pathways, smallest: RAB geranylgeranylation; Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O95716](https://www.uniprot.org/uniprotkb/O95716) (Ras-related protein Rab-3D):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB3D may be involved in the insulin-induced exocytosis of GLUT4-containing vesicles in adipocytes (By …

**Summary**, from NCBI Gene [9545](https://www.ncbi.nlm.nih.gov/gene/9545):

> Enables G protein activity and myosin V binding activity. Involved in bone resorption and positive regulation of regulated secretory pathway. Located in cytoplasmic microtubule and secretory vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9779](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9779) · Entrez [9545](https://www.ncbi.nlm.nih.gov/gene/9545) · UniProt [O95716](https://www.uniprot.org/uniprotkb/O95716) · Ensembl [ENSG00000105514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105514)

## Data

Gene col 2613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2613); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2613]; `tensor/DDL_lfc|DDL_z.npy` [2613]; `embed/gene_vectors.npy` [2613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2613 or target_col == 2613). Every well: [[RAB3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
