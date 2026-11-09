---
symbol: "GSK3A"
type: "gene"
col: 2655
ensembl_id: "ENSG00000105723"
name: "glycogen synthase kinase 3 alpha"
location: "19q13.2"
module: 157
arm: "+"
pooled_cpm: 17.23
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# GSK3A

*glycogen synthase kinase 3 alpha* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.42× (z +14.3, q 8e-44, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Brivudine (drug)]] 5 µM: 0.643× (z -3.8, q 0.062, down in 7 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW 900 0.162×, HS-578T 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0878×; ⚠ cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.141×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Carbamazepine (drug)]] 0.5 µM in 1 line (CHP-212 0.0687×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFTRAF1]] (+0.66, fdr 1e-05), [[NDST2]] (+0.61, fdr 1e-05), [[TEPSIN]] (+0.61, fdr 2e-05); moves opposite to [[MOCS2]] (-0.53, fdr 4e-05), [[NUDT12]] (-0.47, fdr 2e-04), [[SCOC]] (-0.45, fdr 1e-04).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.42×** | +14.3 | 8e-44 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +11.8 | 2e-29 | 41/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.86×** | +10.0 | 2e-21 | 41/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +9.6 | 9e-20 | 31/47 (NCI-H1792, A498, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.4 | 5e-19 | 38/46 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +7.9 | 4e-13 | 34/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.0 | 2e-10 | 28/45 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 2e-06 | 23/46 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.39×** | +5.3 | 8e-06 | 19/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.38×** | +5.2 | 1e-05 | 19/41 (A549, HCT15, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.1 | 2e-05 | 20/43 (HT-29, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.1 | 0.001 | 12/33 (HOP62, A498, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.29×** | +4.1 | 0.001 | 17/44 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.002 | 20/47 (PANC-1, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +4.0 | 0.003 | 15/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.021 | 13/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.025 | 12/48 (SW480, A549, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.031 | 14/45 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.031 | 14/47 (HOP62, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.031 | 7/47 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.074 | 3/45 (Hs 766T, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.076 | 9/43 (A498, A549, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +2.9 | 0.076 | 13/46 (J82, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW 900 0.162×, HS-578T 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0878×; ⚠ cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.141×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Carbamazepine (drug)]] 0.5 µM in 1 line (CHP-212 0.0687×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Brivudine (drug)]] 5 µM |  | **0.643×** | -3.8 | 0.062 | 7/48 (NCI-H23, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -3.7 | 0.062 | 17/48 (H4, NCI-H2030, …) | rises with dose | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.074 | 7/48 (HT-29, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +10.2) | — |
| [[LoVo (line)]] | wt | 15.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +11.1) | — |
| [[SW480 (line)]] | alt | 17.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +9.1) | — |
| [[A498 (line)]] | wt | 18.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +13.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +14.6) | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0878× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0687× (z -8.6) |
| [[HOP62 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HS-578T (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 20.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 9.34 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +18.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 12.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A-172 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFTRAF1]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[NDST2]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TEPSIN]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SH2B1]] | +0.60 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[AKT2]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 | pathway: AKT phosphorylates targets in the cytosol; STRING 937 |
| [[MIB2]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[DMWD]] | +0.58 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[SLC2A8]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[GET4]] | +0.56 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[CACTIN]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[FBRS]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[INPPL1]] | +0.55 | +0.50 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOCS2]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[NUDT12]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[SCOC]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[LRRCC1]] | -0.45 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.4, -22.3); signed map (2.9, -7.3). **Vector** length 62.9, 10.1% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +9.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | +4.1 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +3.3 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | +1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | glycogen synthase kinase 3 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,226,225-42,242,625 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycogen synthase kinase 3 family |
| Reactome | 24 pathways, smallest: Suppression of apoptosis; Maturation of nucleoprotein_9683610; AKT phosphorylates targets in the cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P49840](https://www.uniprot.org/uniprotkb/P49840) (Glycogen synthase kinase-3 alpha):

> Constitutively active protein kinase that acts as a negative regulator in the hormonal control of glucose homeostasis, Wnt signaling and regulation of transcription factors and microtubules, by phosphorylating and inactivating glycogen synthase (GYS1 or GYS2), CTNNB1/beta-catenin, APC and AXIN1. Requires primed phosphorylation of the majority of its substrates. Contributes to insulin regulation of glycogen synthesis by phosphorylating and inhibiting GYS1 activity and hence glycogen synthesis. …

**Summary**, from NCBI Gene [2931](https://www.ncbi.nlm.nih.gov/gene/2931):

> This gene encodes a multifunctional Ser/Thr protein kinase that is implicated in the control of several regulatory proteins including glycogen synthase, and transcription factors, such as JUN. It also plays a role in the WNT and PI3K signaling pathways, as well as regulates the production of beta-amyloid peptides associated with Alzheimer's disease. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:4616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4616) · Entrez [2931](https://www.ncbi.nlm.nih.gov/gene/2931) · UniProt [P49840](https://www.uniprot.org/uniprotkb/P49840) · Ensembl [ENSG00000105723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105723)

## Data

Gene col 2655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2655); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2655]; `tensor/DDL_lfc|DDL_z.npy` [2655]; `embed/gene_vectors.npy` [2655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2655 or target_col == 2655). Every well: [[GSK3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSK3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
