---
symbol: "GOLGA7"
type: "gene"
col: 7195
ensembl_id: "ENSG00000147533"
name: "golgin A7"
location: "8p11.21"
module: 74
arm: "+"
pooled_cpm: 35.64
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# GOLGA7

*golgin A7* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.10× (z +13.6, q 1e-39, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (AN3 CA 0.0586×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.705×; ⚠ position not correctable); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (BT-474 0.152×); [[LB-100 (drug)]] 5 µM in 1 line (H4 0.0472×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BROX]] (+0.59, fdr 1e-05), [[COA8]] (+0.55, fdr 2e-05), [[NKIRAS2]] (+0.53, fdr 2e-05); moves opposite to [[DNA2]] (-0.43, fdr 4e-05), [[EZH2]] (-0.42, fdr 5e-05), [[FUS]] (-0.42, fdr 1e-04).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +13.6 | 1e-39 | 46/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +12.3 | 2e-32 | 44/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +12.2 | 5e-32 | 33/37 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +11.5 | 2e-28 | 42/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.82×** | +11.0 | 4e-26 | 36/44 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +10.0 | 2e-21 | 32/48 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +9.2 | 4e-18 | 40/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.6 | 5e-16 | 38/46 (NCI-H1573, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.1 | 4e-14 | 33/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.33×** | +7.5 | 3e-12 | 28/48 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.52×** | +7.1 | 6e-11 | 31/43 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +7.0 | 1e-10 | 32/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.47×** | +6.9 | 3e-10 | 32/48 (HOP62, A549, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +6.4 | 5e-09 | 35/47 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 3e-08 | 34/48 (HOP62, SK-MEL-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.9 | 1e-07 | 29/48 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +5.0 | 1e-05 | 23/48 (A-172, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.8 | 4e-05 | 27/48 (A-172, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.020 | 13/47 (MIA PaCa-2, HOP62, …) | two highest doses |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.020 | 10/48 (RKO, J82, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.021 | 16/48 (MIA PaCa-2, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7195.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (AN3 CA 0.0586×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.705×; ⚠ position not correctable); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (BT-474 0.152×); [[LB-100 (drug)]] 5 µM in 1 line (H4 0.0472×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.7 | 0.10 | 6/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.827× | -3.5 | 0.10 | 18/47 (HOP62, COLO 205, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.815× | -3.5 | 0.10 | 16/46 (AN3 CA, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 42.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.37× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 31.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 40.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.14× (z +8.7) | — |
| [[A549 (line)]] | wt | 40.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 33.6 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.95× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +8.6) | — |
| [[J82 (line)]] | alt | 56.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 31.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 25.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.41× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 14.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 52.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 51.2 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0586× (z -13.5) |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.152× (z -10.5) |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.116× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 28.1 | 0 | 1 | — | [[LB-100 (drug)]] 5 µM 0.0472× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 67.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.28× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.66× (z +9.1) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BROX]] | +0.59 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[COA8]] | +0.55 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[NKIRAS2]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZNF106]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 | **novel candidate** |
| [[CCNDBP1]] | +0.50 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[SCAMP1]] | +0.50 | +0.24 / +0.57 | both halves | 5e-04 |  |
| [[SERINC3]] | +0.49 | +0.28 / +0.59 | both halves | 3e-04 |  |
| [[VPS35]] | +0.48 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[EMC4]] | +0.48 | +0.43 / +0.40 | both halves | 4e-05 |  |
| [[WBP2]] | +0.48 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[MOSPD1]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[CALCOCO1]] | +0.46 | +0.22 / +0.54 | both halves | 6e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNA2]] | -0.43 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[EZH2]] | -0.42 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[FUS]] | -0.42 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[C21orf58]] | -0.42 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TLCD3B]] | -0.42 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[MYO19]] | -0.42 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[FANCC]] | -0.41 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[RANBP1]] | -0.41 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[CDK1]] | -0.41 | -0.37 / -0.37 | both halves | 8e-05 | pathway: MAPK family signaling cascades |
| [[SNRPF]] | -0.41 | -0.20 / -0.43 | ⚠ not reproduced | 8e-04 | pathway: SARS-CoV-2 Infection |
| [[ATP1B3]] | -0.41 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[PDE7A]] | -0.41 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PTMA]] | -0.40 | -0.44 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.392). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.0, -50.3); signed map (-17.0, -5.8). **Vector** length 65.3, 12.3% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.8 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.8 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +6.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | golgin A7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:41,488,200-41,511,095 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GCP16, HSPC041, GOLGA3AP1, GOLGA7A |
| Reactome | 12 pathways, smallest: RAS processing; Maturation of spike protein_9694548; Translation of Structural Proteins_9694635 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5G4](https://www.uniprot.org/uniprotkb/Q7Z5G4) (Golgin subfamily A member 7):

> May be involved in protein transport from Golgi to cell surface. The ZDHHC9-GOLGA7 complex is a palmitoyltransferase specific for HRAS and NRAS.

**Summary**, from NCBI Gene [51125](https://www.ncbi.nlm.nih.gov/gene/51125):

> Involved in Golgi to plasma membrane protein transport and post-translational protein modification. Acts upstream of or within Golgi to plasma membrane transport. Located in Golgi membrane and Golgi stack. Part of palmitoyltransferase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24876) · Entrez [51125](https://www.ncbi.nlm.nih.gov/gene/51125) · UniProt [Q7Z5G4](https://www.uniprot.org/uniprotkb/Q7Z5G4) · Ensembl [ENSG00000147533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147533)

## Data

Gene col 7195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7195); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7195]; `tensor/DDL_lfc|DDL_z.npy` [7195]; `embed/gene_vectors.npy` [7195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7195 or target_col == 7195). Every well: [[GOLGA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
