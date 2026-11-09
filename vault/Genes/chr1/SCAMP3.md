---
symbol: "SCAMP3"
type: "gene"
col: 3802
ensembl_id: "ENSG00000116521"
name: "secretory carrier membrane protein 3"
location: "1q22"
module: 24
arm: "+"
pooled_cpm: 34.0
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SCAMP3

*secretory carrier membrane protein 3* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.33× (z +10.4, q 9e-23, up in 44 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.63× (z +3.1, q 0.059, up in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H460 5.42×, PANC-1 3.74×, LoVo 4.64×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H460 4.13×, PANC-1 3.52×, LoVo 5.95×; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 2.15×, A-172 2.38×, NCI-H460 2.11×; ⚠ cell-cycle shift, explains ~59% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0838×; ⚠ toxic); [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.114×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.376×; ⚠ cell-cycle shift, explains ~46% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAT2]] (+0.68, fdr 7e-06), [[CUTA]] (+0.64, fdr 7e-06), [[KRT10]] (+0.62, fdr 1e-05, ⚠ KRT10 in the vector space only through flagged drug-doses), [[DPM3]] (+0.61, fdr 2e-05); moves opposite to [[PDAP1]] (-0.60, fdr 1e-05), [[CCT5]] (-0.58, fdr 1e-05), [[YWHAZ]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3802.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H460 5.42×, PANC-1 3.74×, LoVo 4.64×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H460 4.13×, PANC-1 3.52×, LoVo 5.95×; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 2.15×, A-172 2.38×, NCI-H460 2.11×; ⚠ cell-cycle shift, explains ~59% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.33×** | +10.4 | 9e-23 | 44/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +10.1 | 1e-21 | 42/45 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.57×** | +7.9 | 5e-13 | 32/47 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.85×** | +7.6 | 4e-12 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.86×** | +7.4 | 2e-11 | 38/47 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.54×** | +5.1 | 3e-05 | 31/48 (NCI-H460, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.47×** | +4.8 | 2e-04 | 31/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.42×** | +4.3 | 0.001 | 26/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.40×** | +4.2 | 0.002 | 28/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.50×** | +4.2 | 0.002 | 25/44 (PANC-1, HS-578T, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.38×** | +4.0 | 0.003 | 26/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.37×** | +3.8 | 0.006 | 24/48 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.37×** | +3.7 | 0.008 | 18/39 (NCI-H460, LoVo, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.34×** | +3.6 | 0.014 | 21/46 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +3.6 | 0.014 | 23/47 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +3.1 | 0.059 | 16/48 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.069 | 14/48 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0838×; ⚠ toxic); [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.114×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.376×; ⚠ cell-cycle shift, explains ~46% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.7 | 10 (10 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.42× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 41.1 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.74× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 32.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.9) ⚠ cell-cycle shift, explains ~59% of this change | [[Lonafarnib (drug)]] 5 µM 0.114× (z -8.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 19.7 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.95× (z +12.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 73.5 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.82× (z +16.0) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 43.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.3) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A-427 (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -8.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[CFPAC-1 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.82× (z +11.0) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0838× (z -12.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.61× (z +8.7) ⚠ toxic | — |
| [[J82 (line)]] | alt | 32.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.9) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[LS 180 (line)]] | wt | 22.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.48× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.21× (z +8.8) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.43× (z +9.5) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.8) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[RKO (line)]] | wt | 27.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.6) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SW480 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.54× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[CUTA]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | +0.62 | +0.52 / +0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DPM3]] | +0.61 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[FAM193B]] | +0.61 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SIRT2]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RANGRF]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LAMTOR4]] | +0.59 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[COPRS]] | +0.59 | +0.43 / +0.58 | both halves | 4e-05 |  |
| [[SNHG9]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[BRI3]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LAGE3]] | +0.57 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[NME3]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CCT5]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.57 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[MAPRE1]] | -0.56 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[MSN]] | -0.55 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[CTNNA1]] | -0.55 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[PSMD2]] | -0.54 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.54 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[MACROH2A1]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[CCT6A]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[STIP1]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.9, -20.7); signed map (-28.7, 9.1). **Vector** length 72.0, 16.5% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +10.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.5 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | secretory carrier membrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,255,979-155,262,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C1orf3 |
| Gene groups (HGNC) | Secretory carrier membrane proteins |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [O14828](https://www.uniprot.org/uniprotkb/O14828) (Secretory carrier-associated membrane protein 3):

> Functions in post-Golgi recycling pathways. Acts as a recycling carrier to the cell surface.

**Summary**, from NCBI Gene [10067](https://www.ncbi.nlm.nih.gov/gene/10067):

> This gene encodes an integral membrane protein that belongs to the secretory carrier membrane protein family. The encoded protein functions as a carrier to the cell surface in post-golgi recycling pathways. This protein is also involved in protein trafficking in endosomal pathways. Two transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, May 2011]

**Accessions** — [HGNC:10565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10565) · Entrez [10067](https://www.ncbi.nlm.nih.gov/gene/10067) · UniProt [O14828](https://www.uniprot.org/uniprotkb/O14828) · Ensembl [ENSG00000116521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116521)

## Data

Gene col 3802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3802); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3802]; `tensor/DDL_lfc|DDL_z.npy` [3802]; `embed/gene_vectors.npy` [3802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3802 or target_col == 3802). Every well: [[SCAMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
