---
symbol: "RUNDC3B"
type: "gene"
col: 2665
ensembl_id: "ENSG00000105784"
name: "RUN domain containing 3B"
location: "7q21.12"
module: 191
arm: "+"
pooled_cpm: 5.44
n_lines_expressing: 42
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# RUNDC3B

*RUN domain containing 3B* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 19.8× (z +37.8, q 0e+00, up in 35 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.0564×; ⚠ toxic; cell-cycle shift, explains ~17% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HCT15 0.136×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.183×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTUS2]] (+0.66, fdr 1e-05), [[DLGAP2]] (+0.66, fdr 7e-06), [[ITGA7]] (+0.65, fdr 1e-05); moves opposite to [[MCM9]] (-0.52, fdr 3e-05), [[PAXBP1]] (-0.47, fdr 1e-03, ⚠ not reproduced), [[MTOR]] (-0.47, fdr 4e-05), [[PARN]] (-0.46, fdr 3e-05).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABCB1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BACH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **19.8×** | +37.8 | 0e+00 | 35/35 (SHP-77, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **6.24×** | +32.7 | 0e+00 | 26/31 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.60×** | +30.8 | 0e+00 | 30/30 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **10.7×** | +30.0 | 0e+00 | 35/36 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.66×** | +25.7 | 0e+00 | 35/36 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **7.42×** | +25.3 | 0e+00 | 35/36 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **5.13×** | +20.7 | 0e+00 | 34/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.42×** | +18.8 | 0e+00 | 26/32 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.70×** | +17.8 | 0e+00 | 33/36 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.77×** | +12.9 | 3e-36 | 25/31 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **5.53×** | +11.3 | 7e-28 | 29/34 (LoVo, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.41×** | +11.1 | 6e-27 | 27/33 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.40×** | +10.7 | 8e-25 | 22/35 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +8.5 | 6e-16 | 1/11 (A498) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +7.6 | 1e-12 | 3/15 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.7 | 4e-07 | 7/30 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.9 | 3e-05 | 12/36 (NCI-H2030, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2665.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.0564×; ⚠ toxic; cell-cycle shift, explains ~17% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HCT15 0.136×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.183×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Malotilate (drug)]] 5 µM |  | 0.788× | -3.0 | 0.77 | 7/36 (RPMI-7951, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.90 | 11 | 0 | [[Auranofin (drug)]] 5 µM 77.6× (z +13.3) | — |
| [[LoVo (line)]] | wt | 17.2 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 1.79 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 45.1× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 6.04 | 7 | 0 | [[Auranofin (drug)]] 5 µM 22.7× (z +14.4) | — |
| [[A498 (line)]] | wt | 4.50 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 31.5× (z +14.7) | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.84× (z +14.2) | — |
| [[C32 (line)]] | wt | 8.31 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 26.8× (z +10.9) | [[Selinexor (drug)]] 5 µM 0.159× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 4.40 | 5 | 0 | [[Auranofin (drug)]] 5 µM 72.7× (z +16.5) | — |
| [[SW480 (line)]] | alt | 5.13 | 5 | 0 | [[Auranofin (drug)]] 5 µM 64.5× (z +14.4) | — |
| [[A-427 (line)]] | wt | 5.49 | 4 | 0 | [[Auranofin (drug)]] 5 µM 16.1× (z +10.4) | — |
| [[J82 (line)]] | alt | 16.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.40× (z +10.7) | [[Ixazomib citrate (drug)]] 5 µM 0.218× (z -9.7) ⚠ cell-cycle shift, explains ~11% of this change |
| [[LOX-IMVI (line)]] | wt | 9.41 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 58.5× (z +25.2) | — |
| [[NCI-H23 (line)]] | alt | 3.24 | 4 | 0 | [[Auranofin (drug)]] 5 µM 76.9× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 8.25 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.62× (z +14.2) | — |
| [[HCT15 (line)]] | alt | 30.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 11.9× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 1.61 | 2 | 0 | [[Auranofin (drug)]] 5 µM 243× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 2.35 | 2 | 0 | [[Auranofin (drug)]] 5 µM 52.7× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 2.58 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 12.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +10.0) | — |
| [[H4 (line)]] | wt | 6.45 | 1 | 0 | [[Auranofin (drug)]] 5 µM 27.5× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 1.49 | 1 | 0 | [[Auranofin (drug)]] 5 µM 301× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 7.09 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0564× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[SHP-77 (line)]] | alt | 30.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 19.1× (z +17.9) | — |
| [[SK-MEL-2 (line)]] | alt | 3.48 | 1 | 0 | [[Auranofin (drug)]] 5 µM 38.3× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.55× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 2.10 | 1 | 0 | [[Auranofin (drug)]] 5 µM 67.4× (z +8.6) | — |
| [[SW48 (line)]] | wt | 2.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 304× (z +15.1) | — |
| [[A-172 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTUS2]] | +0.66 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.66 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[ITGA7]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[LINC00624]] | +0.64 | +0.40 / +0.81 | both halves | 5e-05 |  |
| [[PLCL1]] | +0.63 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[CELF4]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[SPTBN4]] | +0.60 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[CCDC144NL-1]] | +0.60 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[SH3GL2]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[XKR4]] | +0.58 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[COL26A1]] | +0.58 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[ATP1A3]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM9]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[PAXBP1]] | -0.47 | -0.18 / -0.47 | ⚠ not reproduced | 1e-03 |  |
| [[MTOR]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PARN]] | -0.46 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[HERC2P9-1]] | -0.45 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCB1]] | B | ABCB1 activity raises RUNDC3B's level | lines that do not express ABCB1 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without ABCB1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TIMD4, ZNF736P9Y, PSG1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RUNDC3B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BACH2]] | B | RUNDC3B activity raises BACH2's level | lines that do not express RUNDC3B (8) vs lines expressing it (42) | 3.55× lower at baseline in the lines without RUNDC3B | 0.087 | ⚠ within organs, on part of the lines; also absent: STC2, FAM171B, RTKN2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, 33.3); signed map (26.8, 18.4). **Vector** length 72.2, 13.0% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.0 | +37.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +17.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +32.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +11.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | RUN domain containing 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:87,627,548-87,832,296 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPIP9, RPIB9 |
| Gene groups (HGNC) | RUN domain containing |
| Matched by | ensembl_id |

UniProt [Q96NL0](https://www.uniprot.org/uniprotkb/Q96NL0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30286) · Entrez [154661](https://www.ncbi.nlm.nih.gov/gene/154661) · UniProt [Q96NL0](https://www.uniprot.org/uniprotkb/Q96NL0) · Ensembl [ENSG00000105784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105784)

## Data

Gene col 2665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2665); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2665]; `tensor/DDL_lfc|DDL_z.npy` [2665]; `embed/gene_vectors.npy` [2665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2665 or target_col == 2665). Every well: [[RUNDC3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUNDC3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
