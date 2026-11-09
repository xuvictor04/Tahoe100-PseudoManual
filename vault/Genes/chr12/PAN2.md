---
symbol: "PAN2"
type: "gene"
col: 5711
ensembl_id: "ENSG00000135473"
name: "poly(A) specific ribonuclease subunit PAN2"
location: "12q13.3"
module: 173
arm: "+"
pooled_cpm: 21.29
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# PAN2

*poly(A) specific ribonuclease subunit PAN2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +13.8, q 3e-40, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.438× (z -10.9, q 5e-25, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf54]] (+0.75, fdr 1e-05), [[DXO]] (+0.73, fdr 1e-05), [[MAGOHB]] (+0.68, fdr 3e-05); moves opposite to [[CMTM8]] (-0.68, fdr 1e-05), [[PIP4K2A]] (-0.63, fdr 4e-05), [[LMTK2]] (-0.63, fdr 5e-05).
> It is in [[Module 173]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +13.8 | 3e-40 | 37/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +7.4 | 5e-11 | 29/47 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +6.4 | 3e-08 | 28/47 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.6 | 3e-06 | 26/47 (Panc 03.27, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5711.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.438×** | -10.9 | 5e-25 | 41/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -10.7 | 2e-24 | 41/47 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.454×** | -10.5 | 3e-23 | 37/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -9.9 | 6e-21 | 43/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -9.7 | 5e-20 | 38/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.535×** | -8.3 | 1e-14 | 34/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.568×** | -7.5 | 6e-12 | 32/46 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.573×** | -7.4 | 1e-11 | 38/48 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.629×** | -5.8 | 4e-07 | 27/48 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.718×** | -4.2 | 0.001 | 25/45 (HS-578T, NCI-H460, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.723×** | -4.1 | 0.002 | 20/47 (RKO, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.737×** | -4.0 | 0.003 | 21/48 (NCI-H1792, H4, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.733×** | -3.9 | 0.004 | 16/47 (Hs 766T, SNU-423, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.739×** | -3.9 | 0.004 | 19/48 (A-427, NCI-H1792, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.018 | 19/48 (CFPAC-1, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.786×** | -3.2 | 0.042 | 15/47 (SHP-77, NCI-H661, …) | rises with dose |  |
| [[Decitabine (drug)]] 0.5 µM |  | **0.799×** | -3.0 | 0.077 | 10/47 (HEC-1-A, SW 1271, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.856× | -2.9 | 0.082 | 17/48 (SW48, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.4 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 37.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0552× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.102× (z -13.9) |
| [[PANC-1 (line)]] | alt | 19.1 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.260× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.325× (z -9.4) |
| [[H4 (line)]] | wt | 28.8 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0723× (z -12.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0996× (z -11.1) |
| [[LoVo (line)]] | wt | 35.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 17.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.0) | [[Ixazomib citrate (drug)]] 5 µM 0.261× (z -10.8) |
| [[A-427 (line)]] | wt | 28.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 23.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.273× (z -8.7) |
| [[J82 (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.241× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 27.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0763× (z -11.1) |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0911× (z -11.7) |
| [[HOP62 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.184× (z -9.7) |
| [[KATO III (line)]] | alt | 30.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.173× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.230× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.164× (z -9.1) |
| [[SNU-423 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -8.6) |
| [[SW48 (line)]] | wt | 15.1 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0799× (z -10.2) |
| [[A498 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf54]] | +0.75 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[DXO]] | +0.73 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[MAGOHB]] | +0.68 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[METTL25B]] | +0.68 | +0.82 / +0.46 | both halves | 3e-05 |  |
| [[ENO3]] | +0.67 | +0.74 / +0.37 | both halves | 8e-05 |  |
| [[YME1L1]] | +0.67 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[SEC23B]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[THAP9]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.65 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[COQ5]] | +0.64 | +0.71 / +0.40 | both halves | 5e-05 |  |
| [[GOLGA1]] | +0.64 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[MEPCE]] | +0.64 | +0.70 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTM8]] | -0.68 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[PIP4K2A]] | -0.63 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[LMTK2]] | -0.63 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[SRPK2]] | -0.62 | -0.67 / -0.46 | both halves | 2e-05 |  |
| [[PACC1]] | -0.62 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[EPS15]] | -0.61 | -0.67 / -0.34 | both halves | 1e-04 |  |
| [[ZNF277]] | -0.61 | -0.70 / -0.34 | both halves | 1e-04 |  |
| [[HACD3]] | -0.60 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[GARNL3]] | -0.60 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[INPP4A]] | -0.60 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[CYTH3]] | -0.59 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[TSPAN17]] | -0.59 | -0.67 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.1, 5.8); signed map (11.7, -19.8). **Vector** length 106, 25.8% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.1 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.3 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.4 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | -0.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.6 | -9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.1 | -10.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.9 | -10.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) specific ribonuclease subunit PAN2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,316,223-56,334,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0710, hPAN2; previously USP52 |
| Gene groups (HGNC) | WD repeat domain containing; Ubiquitin specific peptidases; Exonucleases |
| Hallmark sets | E2F_TARGETS |
| Reactome | 3 pathways, smallest: Deadenylation of mRNA; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q504Q3](https://www.uniprot.org/uniprotkb/Q504Q3) (PAN2-PAN3 deadenylation complex catalytic subunit PAN2):

> Catalytic subunit of the poly(A)-nuclease (PAN) deadenylation complex, one of two cytoplasmic mRNA deadenylases involved in general and miRNA-mediated mRNA turnover. PAN specifically shortens poly(A) tails of RNA and the activity is stimulated by poly(A)-binding protein (PABP). PAN deadenylation is followed by rapid degradation of the shortened mRNA tails by the CCR4-NOT complex. Deadenylated mRNAs are then degraded by two alternative mechanisms, namely exosome-mediated 3'-5' exonucleolytic …

**Summary**, from NCBI Gene [9924](https://www.ncbi.nlm.nih.gov/gene/9924):

> This gene encodes a deadenylase that functions as the catalytic subunit of the polyadenylate binding protein dependent poly(A) nuclease complex. The encoded protein is a magnesium dependent 3' to 5' exoribonuclease that is involved in the degradation of cytoplasmic mRNAs. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:20074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20074) · Entrez [9924](https://www.ncbi.nlm.nih.gov/gene/9924) · UniProt [Q504Q3](https://www.uniprot.org/uniprotkb/Q504Q3) · Ensembl [ENSG00000135473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135473)

## Data

Gene col 5711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5711); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5711]; `tensor/DDL_lfc|DDL_z.npy` [5711]; `embed/gene_vectors.npy` [5711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5711 or target_col == 5711). Every well: [[PAN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
