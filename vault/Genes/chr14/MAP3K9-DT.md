---
symbol: "MAP3K9-DT"
type: "gene"
col: 15175
ensembl_id: "ENSG00000259153"
name: "MAP3K9 divergent transcript"
location: "14q24.2"
module: 160
arm: "+"
pooled_cpm: 11.19
n_lines_expressing: 33
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# MAP3K9-DT

*MAP3K9 divergent transcript* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +10.2, q 2e-21, up in 17 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.620× (z -3.8, q 0.086, down in 10 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.170×, Panc 03.27 0.135×; ⚠ cell-cycle shift, explains ~13% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 5 µM in 1 line (SW 900 0.154×; ⚠ cell-cycle shift, explains ~29% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (LoVo 0.0634×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K9]] (+0.54, fdr 1e-05, ⚠ same locus), [[LUZP1]] (+0.50, fdr 3e-05), [[TTC9]] (+0.50, fdr 3e-05), [[CLDN10]] (+0.49, fdr 3e-05); moves opposite to [[VPS36]] (-0.53, fdr 2e-05), [[MRPL42]] (-0.46, fdr 7e-05), [[TAS2R30]] (-0.44, fdr 6e-04).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP3K9]] → it (grade B ⚠); 4 go from it, the strongest it → [[MAP3K9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +10.2 | 2e-21 | 17/25 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.54×** | +7.8 | 2e-12 | 11/17 (HEC-1-A, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.17×** | +6.0 | 3e-07 | 7/13 (SW480, NCI-H2030, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.01×** | +5.9 | 6e-07 | 13/30 (A549, NCI-H23, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.00×** | +5.6 | 3e-06 | 6/11 (SNU-423, NCI-H2030, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +5.5 | 3e-06 | 14/28 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.84×** | +5.1 | 3e-05 | 12/31 (NCI-H2030, A-427, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.79×** | +4.7 | 2e-04 | 12/24 (HOP62, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.67×** | +4.3 | 0.001 | 10/31 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.015 | 5/25 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.015 | 8/31 (PANC-1, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.5 | 0.025 | 6/24 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.50×** | +3.4 | 0.032 | 7/26 (SW 900, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.49×** | +3.2 | 0.054 | 12/23 (SW480, HOP62, …) | top dose only |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.057 | 6/29 (A549, SW 900, …) | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.059 | 3/30 (COLO 205, SW 1271, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.170×, Panc 03.27 0.135×; ⚠ cell-cycle shift, explains ~13% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 5 µM in 1 line (SW 900 0.154×; ⚠ cell-cycle shift, explains ~29% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (LoVo 0.0634×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.620×** | -3.8 | 0.086 | 10/30 (H4, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -3.6 | 0.086 | 11/29 (SW 900, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.674× | -3.4 | 0.15 | 10/30 (SW 900, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.690× | -3.2 | 0.22 | 14/31 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.680× | -3.1 | 0.22 | 8/31 (SW 900, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 168 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 5.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +8.5) | — |
| [[LoVo (line)]] | wt | 3.47 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0634× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -8.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SW 900 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.154× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K9]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LUZP1]] | +0.50 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[TTC9]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[CLDN10]] | +0.49 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[CFAP20DC-AS1]] | +0.49 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[PROSER2-AS1]] | +0.49 | +0.37 / +0.55 | both halves | 7e-05 |  |
| [[ADAM8]] | +0.48 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[SLC35F4]] | +0.48 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[KCNK6]] | +0.47 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[GRIN2D]] | +0.47 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[FAM131B-AS2]] | +0.46 | +0.21 / +0.62 | both halves | 7e-04 |  |
| [[WFDC3]] | +0.46 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[SRRM3]] | +0.45 | +0.44 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS36]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MRPL42]] | -0.46 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[TAS2R30]] | -0.44 | -0.22 / -0.55 | both halves | 6e-04 |  |
| [[NELFCD]] | -0.44 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PPA2]] | -0.44 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[NBN]] | -0.44 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[ZZZ3]] | -0.43 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[MANEA]] | -0.43 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[MIPOL1]] | -0.42 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[PTAR1]] | -0.41 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[PON2]] | -0.41 | -0.19 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[FYCO1]] | -0.40 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ALG6]] | -0.40 | -0.46 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K9]] | B | MAP3K9 activity raises MAP3K9-DT's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 2.85× lower at baseline in the lines without MAP3K9 | 0.024 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[CARD11]] | B | CARD11 activity raises MAP3K9-DT's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.06× lower at baseline in the lines without CARD11 | 0.026 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[TTC9]] | B | TTC9 activity raises MAP3K9-DT's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.06× lower at baseline in the lines without TTC9 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[TOP2A]] | B | TOP2A activity lowers MAP3K9-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K9]] | B | MAP3K9-DT activity raises MAP3K9's level | lines that do not express MAP3K9-DT (17) vs lines expressing it (33) | 3.25× lower at baseline in the lines without MAP3K9-DT | 0.002 | ⚠ within organs, on part of the lines; also absent: KIAA0319, STXBP2, SMPDL3B; maybe low, not absent |
| [[RYR1]] | B | MAP3K9-DT activity raises RYR1's level | lines that do not express MAP3K9-DT (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without MAP3K9-DT | 0.026 | ⚠ within organs, on part of the lines; also absent: KIAA0319, STXBP2, SMPDL3B; maybe low, not absent |
| [[CELF5]] | B | MAP3K9-DT activity raises CELF5's level | lines that do not express MAP3K9-DT (17) vs lines expressing it (33) | 1.49× lower at baseline in the lines without MAP3K9-DT | 0.065 | ⚠ within organs, on part of the lines; also absent: KIAA0319, STXBP2, SMPDL3B; maybe low, not absent |
| [[KLC3]] | B | MAP3K9-DT activity raises KLC3's level | lines that do not express MAP3K9-DT (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without MAP3K9-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: KIAA0319, STXBP2, SMPDL3B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (18.0, 33.3); signed map (-4.5, 41.1). **Vector** length 51.0, 10.1% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +3.2 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +2.5 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.8 | -3.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | MAP3K9 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q24.2 — chr14:70,808,811-70,816,935 (+) |
| Ensembl biotype | lncRNA |
| Also known as | lincNMR |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53189) · Entrez [100506411](https://www.ncbi.nlm.nih.gov/gene/100506411) · Ensembl [ENSG00000259153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259153)

## Data

Gene col 15175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15175); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15175]; `tensor/DDL_lfc|DDL_z.npy` [15175]; `embed/gene_vectors.npy` [15175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15175 or target_col == 15175). Every well: [[MAP3K9-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K9-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
