---
symbol: "PPP4R1L"
type: "gene"
col: 4506
ensembl_id: "ENSG00000124224"
name: "protein phosphatase 4 regulatory subunit 1 like (pseudogene)"
location: "20q13.32"
module: 101
arm: "+"
pooled_cpm: 24.88
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# PPP4R1L

*protein phosphatase 4 regulatory subunit 1 like (pseudogene)* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.43× (z +4.4, q 0.007, up in 24 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 2.84×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.385× (z -11.7, q 8e-29, down in 28 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.670× (z -4.9, q 6e-05, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C9orf24]] (+0.58, fdr 5e-05), [[PITRM1]] (+0.58, fdr 1e-05), [[LUCAT1]] (+0.54, fdr 1e-05); moves opposite to [[MTUS1]] (-0.51, fdr 1e-05), [[SORL1]] (-0.49, fdr 7e-05), [[RNF43]] (-0.48, fdr 4e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4506.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 2.84×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.007 | 24/42 (HT-29, LoVo, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.40×** | +3.9 | 0.025 | 17/42 (SW1417, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.057 | 19/42 (HT-29, A498, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +3.4 | 0.082 | 16/41 (H4, NCI-H2030, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.64× | +3.2 | 0.16 | 14/42 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.17 | 17/42 (SW1417, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.385×** | -11.7 | 8e-29 | 28/37 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.437×** | -9.7 | 5e-20 | 23/32 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.502×** | -7.5 | 1e-11 | 24/35 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.578×** | -6.7 | 3e-09 | 29/42 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.610×** | -6.1 | 2e-07 | 24/41 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.642×** | -5.4 | 6e-06 | 26/42 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.659×** | -5.1 | 3e-05 | 25/42 (SW 1088, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.670×** | -4.9 | 6e-05 | 24/42 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.522×** | -4.2 | 0.002 | 23/42 (A-172, SNU-423, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.719×** | -4.0 | 0.003 | 20/42 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.568×** | -3.6 | 0.015 | 18/42 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.830×** | -3.2 | 0.059 | 16/42 (A-427, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.779×** | -3.1 | 0.097 | 15/41 (H4, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 72.1 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0337× (z -27.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 49.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0734× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 67.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 30.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 34.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 33.3 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0924× (z -9.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 20.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.215× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0682× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0453× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[Panc 03.27 (line)]] | alt | 27.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 28.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 59.7 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.172× (z -12.2) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 47.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0909× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 0.5 µM 0.0499× (z -11.5) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 6.80 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0842× (z -10.1) |
| [[HS-578T (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1088 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0422× (z -8.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C9orf24]] | +0.58 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[PITRM1]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[CCDC82]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ZNF385A]] | +0.52 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CYP27C1]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[FAM219A]] | +0.52 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[EFCAB13]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TMEM132B]] | +0.51 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[UBE2D1]] | +0.51 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[TRPC1]] | +0.51 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[GPATCH2L]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTUS1]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SORL1]] | -0.49 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[RNF43]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PPM1H]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SCAP]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ASB13]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SHROOM2]] | -0.47 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[SHROOM3]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RABL6]] | -0.46 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[PROM1]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ANK3]] | -0.46 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[MAP2K6]] | -0.46 | -0.40 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers PPP4R1L's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.498). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.7, -7.1); signed map (2.7, 21.3). **Vector** length 86.0, 19.1% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -4.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -1.9 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 4 regulatory subunit 1 like (pseudogene) |
| Locus type | pseudogene |
| Location | 20q13.32 — chr20:58,231,789-58,286,399 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | bA196N14.4, bA196N14.5, PPP4R1P1; previously C20orf192 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1A2](https://www.uniprot.org/uniprotkb/Q9P1A2) (Putative serine/threonine-protein phosphatase 4 regulatory subunit 1-like):

> May be a regulatory subunit of serine/threonine-protein phosphatase 4.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:15755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15755) · Entrez [55370](https://www.ncbi.nlm.nih.gov/gene/55370) · UniProt [Q9P1A2](https://www.uniprot.org/uniprotkb/Q9P1A2) · Ensembl [ENSG00000124224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124224)

## Data

Gene col 4506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4506); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4506]; `tensor/DDL_lfc|DDL_z.npy` [4506]; `embed/gene_vectors.npy` [4506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4506 or target_col == 4506). Every well: [[PPP4R1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP4R1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
