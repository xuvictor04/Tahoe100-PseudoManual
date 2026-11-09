---
symbol: "EIF2B1"
type: "gene"
col: 3227
ensembl_id: "ENSG00000111361"
name: "eukaryotic translation initiation factor 2B subunit alpha"
location: "12q24.31"
module: 20
arm: "+"
pooled_cpm: 17.47
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EIF2B1

*eukaryotic translation initiation factor 2B subunit alpha* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.13× (z +15.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.798× (z -6.6, q 3e-08, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (RKO 0.0669×; ⚠ transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.348×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.193×; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW48 0.0840×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFT1]] (+0.63, fdr 2e-05), [[C1D]] (+0.63, fdr 7e-06), [[DLST]] (+0.62, fdr 1e-05); moves opposite to [[LINC01619]] (-0.53, fdr 4e-05), [[EFNA2]] (-0.52, fdr 3e-05), [[SUMO4]] (-0.51, fdr 5e-04).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +15.4 | 0e+00 | 44/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +14.8 | 0e+00 | 42/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.90×** | +13.1 | 6e-37 | 30/39 (A-172, PANC-1, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +10.7 | 1e-24 | 28/46 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +10.6 | 2e-24 | 33/47 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +9.9 | 5e-21 | 23/36 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.58×** | +9.0 | 2e-17 | 18/31 (SNU-423, SHP-77, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +8.7 | 2e-16 | 28/42 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +7.0 | 1e-10 | 25/47 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.6 | 2e-09 | 24/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +6.5 | 5e-09 | 0/48 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.3 | 1e-08 | 23/48 (CFPAC-1, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +6.1 | 5e-08 | 18/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.3 | 4e-06 | 14/47 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.31×** | +5.3 | 5e-06 | 18/46 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +5.1 | 9e-06 | 22/47 (A-427, SHP-77, …) | top dose only | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.49×** | +4.2 | 7e-04 | 8/43 (H4, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.003 | 10/47 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.003 | 11/48 (A498, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.8 | 0.004 | 10/48 (A-427, A549, …) | top dose only |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.004 | 11/48 (J82, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.004 | 7/48 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Lopinavir (drug)]] 5 µM |  | 1.19× | +3.5 | 0.009 | 4/47 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.5 | 0.011 | 11/47 (NCI-H23, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3227.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (RKO 0.0669×; ⚠ transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.348×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.193×; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW48 0.0840×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.798×** | -6.6 | 3e-08 | 23/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.715×** | -5.9 | 1e-06 | 22/47 (hTERT-HPNE, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.853× | -3.3 | 0.18 | 6/47 (A549, NCI-H2347, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 0.750× | -3.1 | 0.28 | 13/46 (SW480, BT-474, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +11.1) | — |
| [[LoVo (line)]] | wt | 12.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +11.2) | — |
| [[A-172 (line)]] | wt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 19.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.348× (z -10.9) |
| [[KATO III (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.9) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0669× (z -14.3) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 11.0 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0840× (z -9.6) |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFT1]] | +0.63 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[C1D]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DLST]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[STEEP1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CDC23]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.60 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[RMDN3]] | +0.59 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[EMC1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[DNAJC13]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NAXD]] | +0.58 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[EIF2D]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[VAMP3]] | +0.56 | +0.38 / +0.51 | both halves | 7e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01619]] | -0.53 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[EFNA2]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SUMO4]] | -0.51 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[BCORL1]] | -0.50 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.50 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[ZBTB7A]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[LAG3]] | -0.49 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[MSX1]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[IER5]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[HES1]] | -0.49 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[LHX4]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ZSWIM6]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.3, -15.2); signed map (-35.0, -30.5). **Vector** length 68.8, 11.2% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.0 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +9.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -2.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2B subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,620,406-123,633,766 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EIF-2Balpha, EIF-2B, EIF2BA, EIF2Balpha; previously EIF2B |
| Reactome | 4 pathways, smallest: Recycling of eIF2:GDP; Cap-dependent Translation Initiation; Eukaryotic Translation Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14232](https://www.uniprot.org/uniprotkb/Q14232) (Translation initiation factor eIF2B subunit alpha):

> Acts as a component of the translation initiation factor 2B (eIF2B) complex, which catalyzes the exchange of GDP for GTP on eukaryotic initiation factor 2 (eIF2) gamma subunit. Its guanine nucleotide exchange factor activity is repressed when bound to eIF2 complex phosphorylated on the alpha subunit, thereby limiting the amount of methionyl-initiator methionine tRNA available to the ribosome and consequently global translation is repressed.

**Summary**, from NCBI Gene [1967](https://www.ncbi.nlm.nih.gov/gene/1967):

> This gene encodes one of five subunits of eukaryotic translation initiation factor 2B (EIF2B), a GTP exchange factor for eukaryotic initiation factor 2 and an essential regulator for protein synthesis. Mutations in this gene and the genes encoding other EIF2B subunits have been associated with leukoencephalopathy with vanishing white matter. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:3257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3257) · Entrez [1967](https://www.ncbi.nlm.nih.gov/gene/1967) · UniProt [Q14232](https://www.uniprot.org/uniprotkb/Q14232) · Ensembl [ENSG00000111361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111361)

## Data

Gene col 3227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3227); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3227]; `tensor/DDL_lfc|DDL_z.npy` [3227]; `embed/gene_vectors.npy` [3227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3227 or target_col == 3227). Every well: [[EIF2B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
