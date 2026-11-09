---
symbol: "SORBS3"
type: "gene"
col: 4233
ensembl_id: "ENSG00000120896"
name: "sorbin and SH3 domain containing 3"
location: "8p21.3"
module: 126
arm: "+"
pooled_cpm: 18.78
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# SORBS3

*sorbin and SH3 domain containing 3* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +14.7, q 0e+00, up in 31 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM: 1.30× (z +4.0, q 0.005, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.282× (z -19.8, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATN1]] (+0.67, fdr 7e-06), [[INPPL1]] (+0.66, fdr 1e-05), [[CRTC2]] (+0.65, fdr 1e-05); moves opposite to [[ROMO1]] (-0.57, fdr 4e-05), [[UQCR11]] (-0.54, fdr 3e-05), [[POMP]] (-0.53, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +14.7 | 0e+00 | 31/38 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +10.8 | 8e-25 | 24/26 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +7.1 | 2e-10 | 23/33 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.7 | 4e-09 | 4/47 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +5.8 | 9e-07 | 25/43 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.005 | 12/46 (A549, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.005 | 15/45 (PANC-1, J82, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.029 | 13/47 (RKO, COLO 205, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.029 | 9/45 (AsPC-1, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.282×** | -19.8 | 0e+00 | 42/47 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.308×** | -18.4 | 0e+00 | 44/47 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.341×** | -16.8 | 0e+00 | 43/47 (SW48, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.600×** | -11.3 | 2e-27 | 34/46 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.502×** | -10.8 | 6e-25 | 41/47 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.562×** | -9.0 | 2e-17 | 30/47 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.574×** | -8.7 | 3e-16 | 35/45 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -8.1 | 5e-14 | 32/46 (HT-29, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -7.8 | 6e-13 | 32/45 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.617×** | -7.5 | 3e-12 | 28/45 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -6.8 | 5e-10 | 26/45 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -6.4 | 7e-09 | 26/47 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.482×** | -6.0 | 1e-07 | 27/47 (A-427, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.673×** | -6.0 | 1e-07 | 25/47 (RKO, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -5.8 | 3e-07 | 22/47 (HEC-1-A, KATO III, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.701×** | -5.3 | 5e-06 | 22/46 (HT-29, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 57.8 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -15.2) |
| [[Hs 766T (line)]] | wt | 32.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -12.4) |
| [[RKO (line)]] | wt | 23.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0487× (z -17.5) |
| [[SW480 (line)]] | alt | 11.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -11.1) |
| [[LoVo (line)]] | wt | 20.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 24.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -8.8) |
| [[SW48 (line)]] | wt | 30.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0682× (z -14.0) |
| [[A498 (line)]] | wt | 41.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -8.9) |
| [[A549 (line)]] | wt | 22.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -14.2) |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -9.9) |
| [[HS-578T (line)]] | alt | 37.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 37.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 25.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.120× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.106× (z -13.8) |
| [[PANC-1 (line)]] | alt | 7.38 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.277× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -9.5) |
| [[A-427 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0819× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -9.2) |
| [[BT-474 (line)]] | alt | 6.10 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0744× (z -8.5) |
| [[HCT15 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 6.68 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0800× (z -10.3) |
| [[J82 (line)]] | alt | 15.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -9.0) |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATN1]] | +0.67 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[INPPL1]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 491 |
| [[CRTC2]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[SEPTIN8]] | +0.64 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MAN2A2]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[U2AF2]] | +0.61 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PARP3]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RIPOR1]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[NXF1]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[DCTN1]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[THBS3]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_APICAL_JUNCTION |

## Genes that move opposite

*24 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROMO1]] | -0.57 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[UQCR11]] | -0.54 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[POMP]] | -0.53 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[COX6A1]] | -0.53 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ELOB]] | -0.52 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[UQCRQ]] ⚠ | -0.52 | -0.46 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCR10]] ⚠ | -0.51 | -0.42 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C4orf48]] | -0.51 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[MRPL36]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TXNDC17]] | -0.50 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[ANAPC11]] | -0.50 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[TUBD1]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ATP5MC1]] | -0.49 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[NDUFA3]] | -0.49 | -0.41 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.7, -22.7); signed map (-11.6, -35.1). **Vector** length 71.9, 13.5% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -1.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -10.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -7.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | sorbin and SH3 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,544,986-22,575,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCAM-1, SH3D4, vinexin |
| Gene groups (HGNC) | SH3 domain containing |
| Hallmark sets | MYOGENESIS, APICAL_JUNCTION |
| Reactome | 2 pathways, smallest: Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [O60504](https://www.uniprot.org/uniprotkb/O60504) (Vinexin):

> Vinexin alpha isoform promotes up-regulation of actin stress fiber formation. Vinexin beta isoform plays a role in cell spreading and enhances the activation of JNK/SAPK in response to EGF stimulation by using its third SH3 domain.

**Summary**, from NCBI Gene [10174](https://www.ncbi.nlm.nih.gov/gene/10174):

> This gene encodes an SH3 domain-containing adaptor protein. The presence of SH3 domains play a role in this protein's ability to bind other cytoplasmic molecules and contribute to cystoskeletal organization, cell adhesion and migration, signaling, and gene expression. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:30907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30907) · Entrez [10174](https://www.ncbi.nlm.nih.gov/gene/10174) · UniProt [O60504](https://www.uniprot.org/uniprotkb/O60504) · Ensembl [ENSG00000120896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120896)

## Data

Gene col 4233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4233); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4233]; `tensor/DDL_lfc|DDL_z.npy` [4233]; `embed/gene_vectors.npy` [4233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4233 or target_col == 4233). Every well: [[SORBS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORBS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
