---
symbol: "MAP3K10"
type: "gene"
col: 5118
ensembl_id: "ENSG00000130758"
name: "mitogen-activated protein kinase kinase kinase 10"
location: "19q13.2"
module: 172
arm: "+"
pooled_cpm: 27.57
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# MAP3K10

*mitogen-activated protein kinase kinase kinase 10* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.33× (z +3.9, q 0.048, up in 22 of 44 measured lines) ⚠ cell-cycle shift, explains ~22% of this change.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.499× (z -10.0, q 1e-20, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGLS]] (+0.59, fdr 2e-05), [[EBF4]] (+0.55, fdr 2e-05), [[PAOX]] (+0.54, fdr 6e-05); moves opposite to [[ERMP1]] (-0.48, fdr 1e-04), [[LANCL1]] (-0.46, fdr 2e-05), [[SLC44A1]] (-0.46, fdr 6e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +3.9 | 0.048 | 22/44 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.22 | 5/46 (C32, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -10.0 | 1e-20 | 30/44 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.614×** | -9.9 | 1e-20 | 31/45 (HEC-1-A, BT-474, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.584×** | -7.7 | 2e-12 | 28/46 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.601×** | -7.3 | 4e-11 | 27/44 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.607×** | -7.1 | 1e-10 | 27/45 (A-427, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.678×** | -5.6 | 2e-06 | 24/46 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.763×** | -5.5 | 4e-06 | 20/44 (PANC-1, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.691×** | -5.3 | 8e-06 | 21/45 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.720×** | -4.7 | 2e-04 | 17/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.732×** | -4.3 | 0.001 | 17/44 (HEC-1-A, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.746×** | -4.2 | 0.001 | 22/46 (A-172, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.748×** | -4.0 | 0.003 | 18/40 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.8 | 0.007 | 3/46 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.017 | 15/45 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.775×** | -3.5 | 0.018 | 19/45 (RKO, HEC-1-A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.632×** | -3.4 | 0.021 | 12/42 (HCT15, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 239 | 0 | 15 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -22.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.468× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 21.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -8.9) |
| [[A-427 (line)]] | wt | 19.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 35.5 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -11.0) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A549 (line)]] | wt | 25.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 11.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.312× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0973× (z -8.7) ⚠ toxic |
| [[C32 (line)]] | wt | 11.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.105× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 7.32 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.314× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 9.48 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 9.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -10.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0829× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGLS]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[EBF4]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[PAOX]] | +0.54 | +0.39 / +0.70 | both halves | 6e-05 |  |
| [[RILPL1]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LRSAM1]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ABCA3]] | +0.51 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[UBE2J2]] | +0.51 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[C1orf159]] | +0.50 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[KMT2B]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MEF2B]] | +0.49 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TMEM44]] | +0.49 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[CAMSAP1-DT]] | +0.49 | +0.49 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERMP1]] | -0.48 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[LANCL1]] | -0.46 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[SLC44A1]] | -0.46 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[CREG1]] | -0.45 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[TMEM123]] | -0.45 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[ALDH9A1]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[CD164]] | -0.45 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[PRCP]] | -0.45 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[GPD2]] | -0.45 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[PGM2]] | -0.43 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[SRP9]] | -0.43 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[MRPL30]] | -0.42 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.4, 27.5); signed map (0.1, 10.0). **Vector** length 69.3, 11.8% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +2.4 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.1 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.0 | -3.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -1.9 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -1.9 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,191,426-40,215,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MST, MEKK10; previously MLK2 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; Mixed lineage kinase family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02779](https://www.uniprot.org/uniprotkb/Q02779) (Mitogen-activated protein kinase kinase kinase 10):

> Activates the JUN N-terminal pathway.

**Summary**, from NCBI Gene [4294](https://www.ncbi.nlm.nih.gov/gene/4294):

> The protein encoded by this gene is a member of the serine/threonine kinase family. This kinase has been shown to activate MAPK8/JNK and MKK4/SEK1, and this kinase itself can be phoshorylated, and thus activated by JNK kinases. This kinase functions preferentially on the JNK signaling pathway, and is reported to be involved in nerve growth factor (NGF) induced neuronal apoptosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6849) · Entrez [4294](https://www.ncbi.nlm.nih.gov/gene/4294) · UniProt [Q02779](https://www.uniprot.org/uniprotkb/Q02779) · Ensembl [ENSG00000130758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130758)

## Data

Gene col 5118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5118); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5118]; `tensor/DDL_lfc|DDL_z.npy` [5118]; `embed/gene_vectors.npy` [5118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5118 or target_col == 5118). Every well: [[MAP3K10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
