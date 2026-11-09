---
symbol: "GPN3"
type: "gene"
col: 3205
ensembl_id: "ENSG00000111231"
name: "GPN-loop GTPase 3"
location: "12q24.11"
module: 3
arm: "+"
pooled_cpm: 24.43
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# GPN3

*GPN-loop GTPase 3* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (18 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.04× (z +15.0, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +9.0, q 3e-17, up in 44 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 9 lines (LoVo 8.14×, AsPC-1 7.20×, SW480 4.89×, HOP62 5.84×, …; ⚠ cell-cycle shift, explains ~33% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H1792 4.91×, HS-578T 3.66×, SNU-423 3.35×, NCI-H2347 2.41×, …); [[Panobinostat (drug)]] 0.5 µM in 4 lines (LoVo 6.71×, AsPC-1 6.48×, SW480 4.84×, HEC-1-A 5.44×; ⚠ cell-cycle shift, explains ~29% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 0.05 µM in 1 line (C32 0.144×).
> Its strongest partners by |cos| (70 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 32 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA3]] (+0.74, fdr 1e-05), [[DHTKD1]] (+0.66, fdr 1e-04), [[METTL26]] (+0.62, fdr 6e-04); moves opposite to [[ADCK1]] (-0.58, fdr 8e-04, ⚠ not reproduced), [[EME2]] (-0.58, fdr 5e-05), [[CLIC2]] (-0.55, fdr 0.001, ⚠ not reproduced), [[HDDC2]] (-0.55, fdr 2e-04), [[MGST1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NMRAL2P-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 18 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3205.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 9 lines (LoVo 8.14×, AsPC-1 7.20×, SW480 4.89×, HOP62 5.84×, …; ⚠ cell-cycle shift, explains ~33% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H1792 4.91×, HS-578T 3.66×, SNU-423 3.35×, NCI-H2347 2.41×, …); [[Panobinostat (drug)]] 0.5 µM in 4 lines (LoVo 6.71×, AsPC-1 6.48×, SW480 4.84×, HEC-1-A 5.44×; ⚠ cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **5.04×** | +15.0 | 0e+00 | 48/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **4.94×** | +14.8 | 0e+00 | 48/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **4.06×** | +13.0 | 2e-36 | 47/47 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +9.0 | 3e-17 | 44/47 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **2.88×** | +8.6 | 8e-16 | 40/43 (HOP62, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **2.25×** | +7.3 | 4e-11 | 29/34 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.63×** | +6.4 | 9e-09 | 35/47 (NCI-H460, LoVo, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.92×** | +5.6 | 2e-06 | 28/40 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.65×** | +4.7 | 2e-04 | 37/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.68×** | +4.7 | 2e-04 | 34/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +4.6 | 3e-04 | 33/47 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.62×** | +4.3 | 9e-04 | 29/44 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.59×** | +4.1 | 0.002 | 30/47 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.55×** | +4.0 | 0.002 | 26/48 (BT-474, LoVo, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~83% of this change | **1.55×** | +3.9 | 0.003 | 26/47 (NCI-H1573, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3205.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 0.05 µM in 1 line (C32 0.144×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.774× | -3.3 | 0.48 | 24/48 (NCI-H2347, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 17.9 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.13× (z +11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 19.9 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.91× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 17.8 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.80× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 24.0 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.44× (z +11.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 21.5 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 20.5 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.14× (z +13.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 26.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.93× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 26.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.20× (z +12.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 18.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.39× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 27.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.28× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.06× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 29.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.1) | — |
| [[RKO (line)]] | wt | 26.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.72× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 26.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +10.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 27.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.28× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HS-578T (line)]] | alt | 20.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +10.0) | — |
| [[KATO III (line)]] | alt | 22.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.15× (z +10.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 15.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.49× (z +10.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 23.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.45× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.144× (z -8.5) |
| [[Hs 766T (line)]] | wt | 25.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.95× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.54× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 20 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA3]] | +0.74 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[DHTKD1]] | +0.66 | +0.32 / +0.55 | both halves | 1e-04 |  |
| [[METTL26]] | +0.62 | +0.22 / +0.51 | both halves | 6e-04 |  |
| [[PRADC1]] | +0.61 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[PIBF1]] | +0.60 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[SCAMP1]] | +0.60 | +0.26 / +0.46 | both halves | 3e-04 |  |
| [[GMCL1]] | +0.59 | +0.14 / +0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[ARL3]] | +0.59 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[KIAA1328]] | +0.59 | +0.16 / +0.47 | ⚠ not reproduced | 0.001 |  |
| [[TRPT1]] | +0.59 | +0.27 / +0.52 | both halves | 3e-04 |  |
| [[TXNDC17]] | +0.58 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[IDH2]] | +0.58 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[ZDHHC12]] | +0.58 | +0.26 / +0.44 | both halves | 4e-04 |  |
| [[NPAT]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCK1]] | -0.58 | -0.19 / -0.36 | ⚠ not reproduced | 8e-04 |  |
| [[EME2]] | -0.58 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[CLIC2]] | -0.55 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[HDDC2]] | -0.55 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[GABPB1-AS1]] | -0.52 | -0.27 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[ACYP2]] | -0.52 | -0.16 / -0.38 | ⚠ not reproduced | 0.001 |  |
| [[MGST1]] | -0.52 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[SRC]] | -0.51 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[NMRAL2P-1]] | -0.51 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[RHBDD3]] | -0.51 | -0.26 / -0.24 | both halves | 4e-04 |  |
| [[TBKBP1]] | -0.50 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ANKRD10]] | -0.50 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[CUEDC1]] | -0.50 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[STRN4]] | -0.50 | -0.21 / -0.40 | both halves | 6e-04 |  |
| [[POU6F1]] | -0.49 | -0.28 / -0.25 | both halves | 4e-04 |  |
| [[SRP14-DT]] | -0.49 | -0.27 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity lowers GPN3's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.28× higher at baseline in the lines without NMRAL2P-1 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[MGST1]] | B | MGST1 activity lowers GPN3's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.31× higher at baseline in the lines without MGST1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[IKBIP]] | C | IKBIP activity raises GPN3's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without IKBIP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.407). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-4.7, -53.3); signed map (-34.0, 15.3). **Vector** length 61.9, 14.5% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | +13.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.3 | +14.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.3 | +15.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +1.7 | +4.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +1.9 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Naproxen (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +1.1 | +0.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | +1.0 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | GPN-loop GTPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,452,486-110,469,268 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14560; previously ATPBD1C |
| Gene groups (HGNC) | GPN-loop GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHW5](https://www.uniprot.org/uniprotkb/Q9UHW5) (GPN-loop GTPase 3):

> Small GTPase involved in the correct assembly of RNA polymerase II (RNAPII) complex, ensuring proper nuclear import of RNAPII.

**Summary**, from NCBI Gene [51184](https://www.ncbi.nlm.nih.gov/gene/51184):

> Predicted to enable GTPase activity. Involved in protein import into nucleus. Located in cytoplasm and nucleus. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30186) · Entrez [51184](https://www.ncbi.nlm.nih.gov/gene/51184) · UniProt [Q9UHW5](https://www.uniprot.org/uniprotkb/Q9UHW5) · Ensembl [ENSG00000111231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111231)

## Data

Gene col 3205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3205); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3205]; `tensor/DDL_lfc|DDL_z.npy` [3205]; `embed/gene_vectors.npy` [3205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3205 or target_col == 3205). Every well: [[GPN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
