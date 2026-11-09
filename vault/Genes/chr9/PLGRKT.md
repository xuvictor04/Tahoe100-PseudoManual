---
symbol: "PLGRKT"
type: "gene"
col: 2820
ensembl_id: "ENSG00000107020"
name: "plasminogen receptor with a C-terminal lysine"
location: "9p24.1"
module: 110
arm: "+"
pooled_cpm: 15.89
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# PLGRKT

*plasminogen receptor with a C-terminal lysine* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.16× (z +11.6, q 2e-28, up in 34 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +11.4, q 1e-27, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.593× (z -11.2, q 3e-26, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPK1]] (+0.65, fdr 1e-05), [[TTL]] (+0.60, fdr 1e-05), [[BMAL2]] (+0.60, fdr 1e-05); moves opposite to [[CLN3]] (-0.57, fdr 2e-05), [[GALM]] (-0.53, fdr 1e-05), [[MPHOSPH8]] (-0.53, fdr 4e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PARVB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.16×** | +11.6 | 2e-28 | 34/38 (KATO III, NCI-H1573, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.4 | 1e-27 | 31/44 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.76×** | +8.2 | 7e-14 | 20/25 (KATO III, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.73×** | +7.7 | 3e-12 | 20/32 (RPMI-7951, NCI-H2347, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.63×** | +7.4 | 2e-11 | 32/47 (KATO III, A549, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.59×** | +7.0 | 2e-10 | 29/47 (KATO III, A-172, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.60×** | +6.8 | 7e-10 | 25/44 (COLO 205, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +6.2 | 3e-08 | 26/47 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.48×** | +5.9 | 3e-07 | 27/46 (KATO III, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.41×** | +5.0 | 4e-05 | 22/46 (LS 180, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 6e-05 | 14/46 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.4 | 5e-04 | 21/47 (SW480, J82, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.6 | 0.012 | 8/47 (RKO, A-427, …) | top dose only | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.58×** | +3.6 | 0.013 | 7/41 (Panc 03.27, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.019 | 8/47 (KATO III, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.028 | 11/47 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.052 | 11/47 (RKO, A-172, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.061 | 5/42 (A-427, A549, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.075 | 10/45 (NCI-H1573, LOX-IMVI, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.075 | 4/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.593×** | -11.2 | 3e-26 | 33/46 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.327×** | -8.8 | 3e-16 | 31/44 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -8.2 | 3e-14 | 29/47 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.393×** | -7.4 | 2e-11 | 30/45 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -6.7 | 3e-09 | 26/46 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -6.3 | 3e-08 | 23/38 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.706×** | -5.0 | 5e-05 | 20/45 (Hs 766T, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.739×** | -4.6 | 3e-04 | 21/44 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.774×** | -3.9 | 0.007 | 17/45 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.706×** | -3.8 | 0.009 | 11/47 (SW480, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.628×** | -3.7 | 0.011 | 12/42 (LoVo, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.843× | -3.7 | 0.011 | 9/47 (A498, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.663×** | -3.3 | 0.049 | 13/35 (HS-578T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 39.3 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0683× (z -10.2) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.156× (z -9.1) |
| [[A-427 (line)]] | wt | 25.9 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0896× (z -9.7) |
| [[KATO III (line)]] | alt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LOX-IMVI (line)]] | wt | 31.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.4) |
| [[SW480 (line)]] | alt | 15.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -8.8) |
| [[A498 (line)]] | wt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -8.5) |
| [[A549 (line)]] | wt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.8) |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0506× (z -13.3) |
| [[LoVo (line)]] | wt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.0) |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK1]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[TTL]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[BMAL2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ATP13A3]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TOMM34]] | +0.58 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SLC25A15]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SPOPL-DT]] | +0.56 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN10]] | +0.55 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[IRAK1]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[UGGT2]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[DCTD]] | +0.55 | +0.59 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN3]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[GALM]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MPHOSPH8]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SAT2]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SECISBP2L]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TBC1D17]] | -0.52 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[KLC4]] | -0.52 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[CWC15]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[FMO5]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ATG14]] | -0.50 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CLIP3]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ZNF383]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVB]] | B | PARVB activity raises PLGRKT's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without PARVB | 0.049 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.1, 7.7); signed map (7.2, 43.3). **Vector** length 72.4, 13.0% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.1 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.4 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -11.2 |
|  | [[NG25 (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -8.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.7 | -0.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | plasminogen receptor with a C-terminal lysine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:5,357,971-5,437,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MDS030, FLJ14688, AD025, Plg-RKT; previously C9orf46 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBL7](https://www.uniprot.org/uniprotkb/Q9HBL7) (Plasminogen receptor):

> Receptor for plasminogen. Regulates urokinase plasminogen activator-dependent and stimulates tissue-type plasminogen activator-dependent cell surface plasminogen activation. Proposed to be part of a local catecholaminergic cell plasminogen activation system that regulates neuroendocrine prohormone processing. Involved in regulation of inflammatory response; regulates monocyte chemotactic migration and matrix metalloproteinase activation, such as of MMP2 and MMP9.

**Summary**, from NCBI Gene [55848](https://www.ncbi.nlm.nih.gov/gene/55848):

> Predicted to be involved in positive regulation of plasminogen activation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23633) · Entrez [55848](https://www.ncbi.nlm.nih.gov/gene/55848) · UniProt [Q9HBL7](https://www.uniprot.org/uniprotkb/Q9HBL7) · Ensembl [ENSG00000107020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107020)

## Data

Gene col 2820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2820); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2820]; `tensor/DDL_lfc|DDL_z.npy` [2820]; `embed/gene_vectors.npy` [2820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2820 or target_col == 2820). Every well: [[PLGRKT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLGRKT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
