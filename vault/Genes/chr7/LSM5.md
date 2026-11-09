---
symbol: "LSM5"
type: "gene"
col: 2750
ensembl_id: "ENSG00000106355"
name: "LSM5 homolog, U6 small nuclear RNA and mRNA degradation associated"
location: "7p14.3"
module: 22
arm: "+"
pooled_cpm: 32.61
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# LSM5

*LSM5 homolog, U6 small nuclear RNA and mRNA degradation associated* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.34× (z +10.5, q 4e-23, up in 37 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +7.3, q 5e-11, up in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 11 lines (LoVo 5.10×, SW480 4.64×, A549 7.35×, KATO III 4.80×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 5.14×, PANC-1 4.93×, SW480 4.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 3.73×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.236×, AN3 CA 0.222×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGB2]] (+0.59, fdr 1e-05), [[EMSY-DT]] (+0.58, fdr 2e-05), [[UBL7-DT]] (+0.57, fdr 2e-05); moves opposite to [[ST6GALNAC6]] (-0.52, fdr 3e-05), [[GPSM1]] (-0.50, fdr 1e-04), [[TRABD]] (-0.48, fdr 9e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2750.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 11 lines (LoVo 5.10×, SW480 4.64×, A549 7.35×, KATO III 4.80×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 5.14×, PANC-1 4.93×, SW480 4.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 3.73×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.34×** | +10.5 | 4e-23 | 37/38 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.23×** | +10.0 | 3e-21 | 45/45 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.49×** | +7.7 | 4e-12 | 38/41 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +7.3 | 5e-11 | 37/47 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.89×** | +5.8 | 7e-07 | 41/47 (hTERT-HPNE, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.1 | 3e-05 | 32/43 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.007 | 32/48 (SHP-77, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.31×** | +3.5 | 0.030 | 33/48 (HT-29, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.45×** | +3.3 | 0.068 | 26/48 (AN3 CA, A549, …) | rises with dose | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.40× | +3.1 | 0.12 | 20/47 (A-172, NCI-H23, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.236×, AN3 CA 0.222×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.88× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 46.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 46.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.50× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 42.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.35× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 63.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGB2]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[EMSY-DT]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[UBL7-DT]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CENPL]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CDKN2C]] | +0.55 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[SKA2]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HMGB1]] | +0.54 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CDC25C]] | +0.54 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[REXO5]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[SMC2]] | +0.53 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[KIF24]] | +0.52 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[C21orf58]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[GPSM1]] | -0.50 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[TRABD]] | -0.48 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[ZDHHC18]] | -0.48 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[DVL1]] | -0.48 | -0.54 / -0.24 | both halves | 5e-04 |  |
| [[KCTD21]] | -0.47 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[POLRMT]] | -0.47 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ST6GALNAC4]] | -0.46 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[EEF2]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[NBEAL2]] | -0.46 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[DCAF4]] | -0.46 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[ABCC10]] | -0.46 | -0.39 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.5, -51.3); signed map (-47.5, -49.2). **Vector** length 46.9, 9.71% of its response variance represented; |z| ≥ 3 in 566 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[Darinaparsin (drug)]] 0.5 µM |  | +0.8 | +1.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +1.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.4 | -2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.2 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | +0.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.0 | +1.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -0.9 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | LSM5 homolog, U6 small nuclear RNA and mRNA degradation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:32,485,338-32,495,283 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YER146W |
| Gene groups (HGNC) | LSm proteins |
| Reactome | 6 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4Y9](https://www.uniprot.org/uniprotkb/Q9Y4Y9) (U6 snRNA-associated Sm-like protein LSm5):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex). The heptameric LSM2-8 complex binds specifically to the 3'-terminal U-tract of U6 snRNA.

**Summary**, from NCBI Gene [23658](https://www.ncbi.nlm.nih.gov/gene/23658):

> Sm-like proteins were identified in a variety of organisms based on sequence homology with the Sm protein family (see SNRPD2; MIM 601061). Sm-like proteins contain the Sm sequence motif, which consists of 2 regions separated by a linker of variable length that folds as a loop. The Sm-like proteins are thought to form a stable heteromer present in tri-snRNP particles, which are important for pre-mRNA splicing.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:17162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17162) · Entrez [23658](https://www.ncbi.nlm.nih.gov/gene/23658) · UniProt [Q9Y4Y9](https://www.uniprot.org/uniprotkb/Q9Y4Y9) · Ensembl [ENSG00000106355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106355)

## Data

Gene col 2750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2750); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2750]; `tensor/DDL_lfc|DDL_z.npy` [2750]; `embed/gene_vectors.npy` [2750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2750 or target_col == 2750). Every well: [[LSM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
