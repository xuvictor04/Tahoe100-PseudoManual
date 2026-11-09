---
symbol: "DUT"
type: "gene"
col: 4936
ensembl_id: "ENSG00000128951"
name: "deoxyuridine triphosphatase"
location: "15q21.1"
module: 6
arm: "+"
pooled_cpm: 39.79
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DUT

*deoxyuridine triphosphatase* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.32× (z +11.8, q 2e-29, up in 45 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 4.91×, A549 8.99×, NCI-H1573 6.55×, NCI-H460 6.17×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.78×, NCI-H1573 6.35×, LOX-IMVI 5.00×, HT-29 6.74×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 5.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.480× (z -7.0, q 1e-09, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.644× (z -6.3, q 8e-08, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHEK1]] (+0.71, fdr 7e-06), [[HELLS]] (+0.70, fdr 7e-06), [[MCM4]] (+0.67, fdr 7e-06); moves opposite to [[SHC2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C21orf58]], [[CENPM]], [[SKA3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4936.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 4.91×, A549 8.99×, NCI-H1573 6.55×, NCI-H460 6.17×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.78×, NCI-H1573 6.35×, LOX-IMVI 5.00×, HT-29 6.74×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 5.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.32×** | +11.8 | 2e-29 | 45/46 (PANC-1, A549, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.42×** | +10.5 | 3e-23 | 38/40 (PANC-1, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.89×** | +10.0 | 3e-21 | 41/42 (HS-578T, PANC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.7 | 4e-04 | 28/45 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.48×** | +3.4 | 0.083 | 24/48 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | 1.46× | +3.2 | 0.12 | 24/47 (C32, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.45× | +3.2 | 0.12 | 21/47 (HOP62, NCI-H23, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 1.42× | +3.0 | 0.18 | 18/48 (Panc 03.27, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.480×** | -7.0 | 1e-09 | 38/48 (KATO III, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.644×** | -6.3 | 8e-08 | 32/48 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.616×** | -4.9 | 1e-04 | 28/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -4.9 | 1e-04 | 30/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.620×** | -4.8 | 1e-04 | 32/48 (A-172, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.622×** | -4.8 | 1e-04 | 36/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -4.6 | 4e-04 | 32/48 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.651×** | -4.3 | 1e-03 | 29/48 (LoVo, SW 900, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.694×** | -3.7 | 0.014 | 24/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.703×** | -3.6 | 0.019 | 26/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.511×** | -3.6 | 0.019 | 20/43 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.726×** | -3.2 | 0.056 | 22/47 (KATO III, A-172, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.715×** | -3.2 | 0.059 | 21/47 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[Ivermectin (drug)]] 5 µM |  | **0.733×** | -3.1 | 0.069 | 17/48 (A549, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 45.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 34.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.00× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.20× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -10.0) |
| [[PANC-1 (line)]] | alt | 69.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.99× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 27.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.74× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 41.6 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.166× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.261× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 36.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.32× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 71.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.301× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.06× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 29.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.221× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 49.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 59.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.00× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHEK1]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[HELLS]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM4]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 755 |
| [[POLD3]] | +0.67 | +0.59 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |
| [[DYNC2I2]] | +0.66 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[CENPH]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MCM3]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 744 |
| [[CENPU]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[PRIM1]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 442 |
| [[PCLAF]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[FAM111B]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RANBP1]] | +0.64 | +0.58 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHC2]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf58]], [[CENPM]], [[SKA3]] | C | C21orf58, CENPM, SKA3 activity raises DUT's level | lines that do not express C21orf58, CENPM, SKA3 (3) vs lines expressing them (47) | 1.99× lower at baseline in the lines without C21orf58, CENPM, SKA3 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.9, -43.7); signed map (-37.4, -47.4). **Vector** length 79.6, 23.4% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.51 to 28); *E2F G1/S* (control, mean cos +0.51 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.52 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | +3.0 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.4 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -2.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +1.5 | +0.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | +1.4 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | -0.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.1 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.6 | -4.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.0 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | deoxyuridine triphosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:48,331,011-48,343,373 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dUTPase |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 5 pathways, smallest: Interconversion of nucleotide di- and triphosphates; HCMV Early Events; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P33316](https://www.uniprot.org/uniprotkb/P33316) (Deoxyuridine 5'-triphosphate nucleotidohydrolase, mitochondrial):

> Catalyzes the cleavage of 2'-deoxyuridine 5'-triphosphate (dUTP) into 2'-deoxyuridine 5'-monophosphate (dUMP) and inorganic pyrophosphate and through its action efficiently prevents uracil misincorporation into DNA and at the same time provides dUMP, the substrate for de novo thymidylate biosynthesis. Inhibits peroxisome proliferator-activated receptor (PPAR) activity by binding of its N-terminal to PPAR, preventing the latter's dimerization with retinoid X receptor (By similarity). Essential …

**Summary**, from NCBI Gene [1854](https://www.ncbi.nlm.nih.gov/gene/1854):

> This gene encodes an essential enzyme of nucleotide metabolism. The encoded protein forms a ubiquitous, homotetrameric enzyme that hydrolyzes dUTP to dUMP and pyrophosphate. This reaction serves two cellular purposes: providing a precursor (dUMP) for the synthesis of thymine nucleotides needed for DNA replication, and limiting intracellular pools of dUTP. Elevated levels of dUTP lead to increased incorporation of uracil into DNA, which induces extensive excision repair mediated by uracil …

**Accessions** — [HGNC:3078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3078) · Entrez [1854](https://www.ncbi.nlm.nih.gov/gene/1854) · UniProt [P33316](https://www.uniprot.org/uniprotkb/P33316) · Ensembl [ENSG00000128951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128951)

## Data

Gene col 4936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4936); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4936]; `tensor/DDL_lfc|DDL_z.npy` [4936]; `embed/gene_vectors.npy` [4936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4936 or target_col == 4936). Every well: [[DUT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
