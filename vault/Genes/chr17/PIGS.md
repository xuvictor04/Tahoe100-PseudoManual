---
symbol: "PIGS"
type: "gene"
col: 1485
ensembl_id: "ENSG00000087111"
name: "phosphatidylinositol glycan anchor biosynthesis class S"
location: "17q11.2"
module: 50
arm: "+"
pooled_cpm: 19.56
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PIGS

*phosphatidylinositol glycan anchor biosynthesis class S* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +16.5, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.646× (z -7.5, q 3e-11, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCN2]] (+0.72, fdr 7e-06), [[PRKACA]] (+0.66, fdr 1e-05), [[FUCA1]] (+0.64, fdr 7e-06); moves opposite to [[GLRX2]] (-0.60, fdr 2e-05), [[NSRP1]] (-0.57, fdr 3e-05), [[TATDN1]] (-0.57, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +16.5 | 0e+00 | 43/46 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.86×** | +10.6 | 7e-24 | 27/39 (PANC-1, NCI-H1573, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.60×** | +8.0 | 2e-13 | 31/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.53×** | +7.2 | 6e-11 | 26/46 (SW480, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.50×** | +7.0 | 3e-10 | 34/47 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.49×** | +6.9 | 6e-10 | 33/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.52×** | +6.9 | 6e-10 | 19/32 (PANC-1, J82, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.47×** | +6.6 | 2e-09 | 24/48 (SW480, KATO III, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.45×** | +5.9 | 2e-07 | 21/36 (A-172, HEC-1-A, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.41×** | +5.7 | 7e-07 | 25/45 (CFPAC-1, NCI-H2030, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +5.3 | 7e-06 | 24/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +5.2 | 1e-05 | 22/47 (A549, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +4.6 | 2e-04 | 20/48 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.4 | 3e-04 | 14/28 (HEC-1-A, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Furosemide (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.001 | 9/47 (A498, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.019 | 12/45 (HCT15, Panc 03.27, …) | inconsistent across doses |  |
| [[LJI308 (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.068 | 6/48 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.071 | 9/48 (HOP62, A-172, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.085 | 3/44 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1485.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -7.5 | 3e-11 | 31/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -6.0 | 6e-07 | 25/46 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.723×** | -5.6 | 4e-06 | 22/47 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.723×** | -5.2 | 3e-05 | 20/46 (A-172, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.770×** | -4.5 | 7e-04 | 22/48 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -3.9 | 0.008 | 14/48 (SHP-77, SW1417, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.804×** | -3.8 | 0.013 | 11/47 (HOP62, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.798×** | -3.6 | 0.025 | 18/48 (A-172, HT-29, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.083 | 14/47 (AN3 CA, PANC-1, …) | top dose only |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.782× | -3.0 | 0.14 | 2/48 (A498, NCI-H460) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 31.0 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +13.0) | [[Homoharringtonine (drug)]] 0.05 µM 0.401× (z -9.8) |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 3 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0705× (z -9.9) |
| [[SW480 (line)]] | alt | 17.4 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.34× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.8) | — |
| [[A-172 (line)]] | wt | 27.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 15.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.6) | — |
| [[KATO III (line)]] | alt | 25.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A-427 (line)]] | wt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.63× (z +9.1) | — |
| [[A549 (line)]] | wt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 24.3 | 0 | 1 | — | [[Ranolazine (drug)]] 0.5 µM 0.0825× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.133× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[J82 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.163× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 22.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.182× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PRKACA]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[FUCA1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MLEC]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PCYOX1]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ATP6AP1]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[RPN2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[AGPAT1]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TMED4]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[GANAB]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[BSG]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLRX2]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NSRP1]] | -0.57 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[TATDN1]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[LINC00520]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[RPLP0P2]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[OSGIN1]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[NDUFB9]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ABCA15P]] | -0.53 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[NPL]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[PNLIPRP3]] | -0.52 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[ROR1-AS1]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[RSL1D1]] | -0.51 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.2, -20.2); signed map (-27.8, -38.4). **Vector** length 81.0, 15.1% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +16.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +3.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +3.5 | +10.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.5 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +3.2 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.5 | -0.4 |
|  | [[Ixazomib (drug)]] 5 µM |  | +1.4 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,553,383-28,571,794 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIG-S |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; Glycosylphosphatidylinositol transamidase complex |
| Reactome | 2 pathways, smallest: Attachment of GPI anchor to uPAR; Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S52](https://www.uniprot.org/uniprotkb/Q96S52) (GPI-anchor transamidase component PIGS):

> Component of the glycosylphosphatidylinositol-anchor (GPI-anchor) transamidase (GPI-T) complex that catalyzes the formation of the linkage between a proprotein and a GPI-anchor and participates in GPI anchored protein biosynthesis.

**Summary**, from NCBI Gene [94005](https://www.ncbi.nlm.nih.gov/gene/94005):

> This gene encodes a protein that is involved in GPI-anchor biosynthesis. The glycosylphosphatidylinositol (GPI) anchor is a glycolipid found on many blood cells and serves to anchor proteins to the cell surface. This gene encodes an essential component of the multisubunit enzyme, GPI transamidase. GPI transamidase mediates GPI anchoring in the endoplasmic reticulum, by catalyzing the transfer of fully assembled GPI units to proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14937) · Entrez [94005](https://www.ncbi.nlm.nih.gov/gene/94005) · UniProt [Q96S52](https://www.uniprot.org/uniprotkb/Q96S52) · Ensembl [ENSG00000087111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087111)

## Data

Gene col 1485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1485); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1485]; `tensor/DDL_lfc|DDL_z.npy` [1485]; `embed/gene_vectors.npy` [1485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1485 or target_col == 1485). Every well: [[PIGS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
