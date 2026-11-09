---
symbol: "FBXO41"
type: "gene"
col: 8618
ensembl_id: "ENSG00000163013"
name: "F-box protein 41"
location: "2p13.2"
module: 158
arm: "+"
pooled_cpm: 15.84
n_lines_expressing: 46
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# FBXO41

*F-box protein 41* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.88× (z +21.8, q 0e+00, up in 35 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H460 202×, NCI-H1792 31.9×, NCI-H23 17.6×, HOP62 17.9×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 131×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 36.5×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.334× (z -15.9, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP25]] (+0.63, fdr 3e-05), [[ASTL]] (+0.63, fdr 7e-06), [[ZNF34]] (+0.63, fdr 1e-04); moves opposite to [[PPP1R12B]] (-0.60, fdr 3e-05), [[HINT1]] (-0.53, fdr 6e-05), [[ERGIC3]] (-0.53, fdr 4e-04).
> It is in [[Module 158]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8618.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H460 202×, NCI-H1792 31.9×, NCI-H23 17.6×, HOP62 17.9×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 131×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 36.5×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.88×** | +21.8 | 0e+00 | 35/43 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 3e-04 | 18/41 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.334×** | -15.9 | 0e+00 | 38/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -14.9 | 0e+00 | 33/40 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -11.5 | 3e-28 | 36/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.462×** | -11.2 | 4e-27 | 32/42 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -7.8 | 5e-13 | 27/38 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.631×** | -6.7 | 2e-09 | 28/44 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.685×** | -5.5 | 3e-06 | 23/42 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -5.3 | 9e-06 | 22/42 (C32, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.698×** | -5.2 | 1e-05 | 16/43 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.701×** | -5.2 | 1e-05 | 18/44 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.704×** | -4.9 | 5e-05 | 17/44 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.724×** | -4.4 | 4e-04 | 18/41 (SHP-77, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -4.2 | 0.001 | 16/44 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.4 | 0.027 | 6/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.848× | -3.4 | 0.027 | 12/43 (SHP-77, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.027 | 14/40 (SHP-77, RKO, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.851× | -3.3 | 0.030 | 12/43 (BT-474, NCI-H23, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.825×** | -3.3 | 0.030 | 14/42 (SHP-77, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.09 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 202× (z +32.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +21.4) | [[Digitoxin (drug)]] 5 µM 0.189× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 37.1 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +28.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0634× (z -18.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -12.2) |
| [[PANC-1 (line)]] | alt | 10.2 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.148× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -10.4) |
| [[LoVo (line)]] | wt | 23.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 24.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 26.9× (z +26.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -10.1) |
| [[SW480 (line)]] | alt | 26.1 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -10.7) |
| [[A-427 (line)]] | wt | 32.1 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.158× (z -13.9) |
| [[C32 (line)]] | wt | 12.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 38.8× (z +23.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.113× (z -9.7) |
| [[A-172 (line)]] | wt | 17.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.258× (z -9.4) |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 51.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.236× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[NCI-H1792 (line)]] | alt | 19.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 31.9× (z +30.2) | [[Digitoxin (drug)]] 5 µM 0.0936× (z -14.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 64.7× (z +24.7) | — |
| [[A549 (line)]] | wt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +16.9) | — |
| [[AsPC-1 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -8.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +19.9) | — |
| [[H4 (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +27.9) | — |
| [[Hs 766T (line)]] | wt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +13.5) | — |
| [[J82 (line)]] | alt | 6.26 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -8.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 8.68 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0613× (z -9.0) |
| [[SW 900 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +10.7) | — |
| [[A498 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP25]] | +0.63 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[ASTL]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ZNF34]] | +0.63 | +0.72 / +0.34 | both halves | 1e-04 |  |
| [[EGR3]] | +0.62 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SPATA32]] | +0.61 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[PALD1]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CYB5D1]] | +0.59 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[MTNR1A]] | +0.57 | +0.66 / +0.27 | both halves | 3e-04 |  |
| [[EGR2]] | +0.57 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[THOC6]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[BCAN-AS2]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[SLC27A3]] | +0.55 | +0.59 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12B]] | -0.60 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[HINT1]] | -0.53 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[ERGIC3]] | -0.53 | -0.65 / -0.25 | both halves | 4e-04 |  |
| [[STK38]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[MTM1]] | -0.51 | -0.59 / -0.43 | both halves | 4e-05 |  |
| [[DISP1]] | -0.51 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[ARHGAP17]] | -0.51 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[RNPC3]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NENF]] | -0.50 | -0.62 / -0.24 | both halves | 4e-04 |  |
| [[MZT2B]] | -0.50 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[HEBP1]] | -0.49 | -0.63 / -0.24 | both halves | 4e-04 |  |
| [[TRPC4AP]] | -0.48 | -0.61 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.0, -2.2); signed map (5.4, 29.8). **Vector** length 84.4, 16.5% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.7 | +21.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | -0.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.7 | -11.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.0 | -11.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -14.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.8 | -15.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -3.6 | -6.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:73,254,682-73,284,478 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1940, Fbx41 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF61](https://www.uniprot.org/uniprotkb/Q8TF61) (F-box only protein 41):

> Substrate-recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex. Required in the developing brain for neuronal migration and long-term cerebellar integrity. Regulates postnatal hippocampal development, synaptic vesicle release probability at excitatory synapses and readily releasable pool size at inhibitory synapses. Upon accumulation at the centriole, promotes disassembly of primary cilia and negatively regulates Sonic hedgehog signaling.

**Summary**, from NCBI Gene [150726](https://www.ncbi.nlm.nih.gov/gene/150726):

> This gene encodes a member of the F-box protein family, which is characterized by an approximately 40 amino acid motif, the F-box. F-box proteins constitute one of the four subunits of the SCF ubiquitin protein ligase complex that plays a role in phosphorylation-dependent ubiquitination. F-box proteins are divided into three classes depending on the interaction substrate domain each contains in addition to the F-box motif: FBXW proteins contain WD-40 domains, FBXL proteins contain leucine-rich …

**Accessions** — [HGNC:29409](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29409) · Entrez [150726](https://www.ncbi.nlm.nih.gov/gene/150726) · UniProt [Q8TF61](https://www.uniprot.org/uniprotkb/Q8TF61) · Ensembl [ENSG00000163013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163013)

## Data

Gene col 8618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8618); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8618]; `tensor/DDL_lfc|DDL_z.npy` [8618]; `embed/gene_vectors.npy` [8618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8618 or target_col == 8618). Every well: [[FBXO41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
