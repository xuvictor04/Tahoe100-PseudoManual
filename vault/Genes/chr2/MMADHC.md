---
symbol: "MMADHC"
type: "gene"
col: 9628
ensembl_id: "ENSG00000168288"
name: "metabolism of cobalamin associated D"
location: "2q23.2"
module: 12
arm: "+"
pooled_cpm: 64.8
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MMADHC

*metabolism of cobalamin associated D* — 2q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +6.7, q 1e-08, up in 32 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.41× (z +5.1, q 4e-05, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.470× (z -15.9, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN6]] (+0.76, fdr 7e-06), [[SNRPB2]] (+0.69, fdr 7e-06), [[SEC62]] (+0.67, fdr 1e-05); moves opposite to [[AKT1]] (-0.60, fdr 1e-05), [[COLGALT1]] (-0.59, fdr 1e-05), [[SMG1P3]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +6.7 | 1e-08 | 32/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.48×** | +5.9 | 1e-06 | 35/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.45×** | +5.4 | 1e-05 | 32/48 (A-427, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 4e-05 | 32/48 (HT-29, LOX-IMVI, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.0 | 8e-05 | 32/48 (C32, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.34×** | +4.4 | 8e-04 | 29/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.34×** | +4.4 | 8e-04 | 33/47 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.32×** | +4.2 | 0.002 | 28/48 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.004 | 28/48 (LOX-IMVI, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.044 | 20/48 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.62×** | +3.3 | 0.045 | 24/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.1 | 0.096 | 23/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.097 | 19/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.55×** | +3.0 | 0.097 | 13/47 (PANC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9628.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.470×** | -15.9 | 0e+00 | 46/49 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.536×** | -9.3 | 6e-18 | 43/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.567×** | -8.4 | 7e-15 | 40/48 (HepG2/C3A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.578×** | -8.1 | 6e-14 | 42/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.569×** | -8.0 | 1e-13 | 40/48 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.680×** | -5.7 | 1e-06 | 36/48 (SW 900, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -5.7 | 1e-06 | 32/50 (SW 900, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.794×** | -4.8 | 1e-04 | 32/48 (A-172, SW1417, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.562×** | -4.0 | 0.004 | 27/49 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.800×** | -3.3 | 0.054 | 22/48 (SW 1088, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.804×** | -3.2 | 0.064 | 24/48 (NCI-H661, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.812×** | -3.1 | 0.096 | 19/48 (RKO, H4, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.866× | -3.0 | 0.12 | 10/48 (NCI-H661, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 92.4 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 80.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -16.7) |
| [[C32 (line)]] | wt | 51.9 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.51× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 65.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 52.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -12.7) |
| [[SW480 (line)]] | alt | 72.4 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -12.6) |
| [[COLO 205 (line)]] | alt | 46.3 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 63.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -9.0) |
| [[KATO III (line)]] | alt | 64.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.0) |
| [[AN3 CA (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 69.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.4) |
| [[HOP62 (line)]] | alt | 58.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.6) |
| [[HS-578T (line)]] | alt | 64.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -10.1) |
| [[HT-29 (line)]] | alt | 83.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 82.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 42.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +9.7) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2347 (line)]] | alt | 64.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -10.6) |
| [[PANC-1 (line)]] | alt | 65.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.7) |
| [[A-172 (line)]] | wt | 59.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.7) |
| [[A498 (line)]] | wt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -12.6) |
| [[A549 (line)]] | wt | 54.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -10.7) |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -10.4) |
| [[Hs 766T (line)]] | wt | 55.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.1) |
| [[J82 (line)]] | alt | 60.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.1) |
| [[LoVo (line)]] | wt | 58.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -11.5) |
| [[LS 180 (line)]] | wt | 68.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 58.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 53.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.3) |
| [[RKO (line)]] | wt | 75.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.7) |
| [[SNU-423 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.350× (z -9.6) ⚠ cell-cycle shift, explains ~3% of this change |
| [[SW1417 (line)]] | alt | 58.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -12.7) |
| [[SW48 (line)]] | wt | 62.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.7) |
| [[A-427 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6]] | +0.76 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[SNRPB2]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SEC62]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[PDRG1]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[PSMB1]] | +0.67 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[MRFAP1]] | +0.67 | +0.51 / +0.69 | both halves | 1e-05 | STRING 498 |
| [[CCDC43]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ARMCX5]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SPOP]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[KBTBD7]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[COLGALT1]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[SMG1P3]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[PRKCSH]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A39]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MMADHC's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.733). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-35.7, 0.2); signed map (-10.1, -9.0). **Vector** length 99.2, 28.7% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +7.5 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.4 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +4.1 | +5.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +5.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -15.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | metabolism of cobalamin associated D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.2 — chr2:149,569,637-149,587,778 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CL25022, cblD; previously C2orf25 |
| Reactome | 7 pathways, smallest: Cobalamin (Cbl) metabolism; Defects in cobalamin (B12) metabolism; Cobalamin (Cbl, vitamin B12) transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3L0](https://www.uniprot.org/uniprotkb/Q9H3L0) (Cobalamin trafficking protein CblD):

> Involved in cobalamin metabolism and trafficking. Plays a role in regulating the biosynthesis and the proportion of two coenzymes, methylcob(III)alamin (MeCbl) and 5'-deoxyadenosylcobalamin (AdoCbl). Promotes oxidation of cob(II)alamin bound to MMACHC. The processing of cobalamin in the cytosol occurs in a multiprotein complex composed of at least MMACHC, MMADHC, MTRR (methionine synthase reductase) and MTR (methionine synthase) which may contribute to shuttle safely and efficiently cobalamin …

**Summary**, from NCBI Gene [27249](https://www.ncbi.nlm.nih.gov/gene/27249):

> This gene encodes a mitochondrial protein that is involved in an early step of vitamin B12 metabolism. Vitamin B12 (cobalamin) is essential for normal development and survival in humans. Mutations in this gene cause methylmalonic aciduria and homocystinuria type cblD (MMADHC), a disorder of cobalamin metabolism that is characterized by decreased levels of the coenzymes adenosylcobalamin and methylcobalamin. Pseudogenes have been identified on chromosomes 11 and X.[provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:25221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25221) · Entrez [27249](https://www.ncbi.nlm.nih.gov/gene/27249) · UniProt [Q9H3L0](https://www.uniprot.org/uniprotkb/Q9H3L0) · Ensembl [ENSG00000168288](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168288)

## Data

Gene col 9628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9628); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9628]; `tensor/DDL_lfc|DDL_z.npy` [9628]; `embed/gene_vectors.npy` [9628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9628 or target_col == 9628). Every well: [[MMADHC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMADHC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
