---
symbol: "ZNF731P"
type: "gene"
col: 13605
ensembl_id: "ENSG00000227671"
name: "zinc finger protein 731, pseudogene"
location: "1q44"
module: 59
arm: "-"
pooled_cpm: 33.52
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ZNF731P

*zinc finger protein 731, pseudogene* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.58× (z +6.3, q 7e-08, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.542× (z -11.9, q 6e-30, down in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.715× (z -6.5, q 1e-08, down in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (MIA PaCa-2 0.110×, SK-MEL-2 0.201×, H4 0.131×, LoVo 0.364×, …; ⚠ cell-cycle shift, explains ~48% of this change); [[Pemigatinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0744×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.211×; ⚠ cell-cycle shift, explains ~57% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (CHP-212 0.108×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAP31]] (+0.73, fdr 7e-06), [[UFD1]] (+0.68, fdr 7e-06), [[NECAB3]] (+0.68, fdr 7e-06); moves opposite to [[PIM3]] (-0.69, fdr 7e-06), [[PPP4R2]] (-0.68, fdr 7e-06), [[KMT2E]] (-0.68, fdr 1e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PNPLA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +6.3 | 7e-08 | 37/47 (NCI-H460, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.58×** | +6.3 | 7e-08 | 35/46 (NCI-H460, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.55×** | +5.7 | 2e-06 | 32/47 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.7 | 4e-04 | 26/47 (MIA PaCa-2, SW480, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.6 | 5e-04 | 27/46 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.4 | 0.001 | 22/45 (SHP-77, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.0 | 0.005 | 16/37 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.32×** | +3.8 | 0.009 | 24/47 (LoVo, SW1417, …) | rises with dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 1.25× | +3.0 | 0.15 | 10/46 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13605.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (MIA PaCa-2 0.110×, SK-MEL-2 0.201×, H4 0.131×, LoVo 0.364×, …; ⚠ cell-cycle shift, explains ~48% of this change); [[Pemigatinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0744×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.211×; ⚠ cell-cycle shift, explains ~57% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (CHP-212 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.542×** | -11.9 | 6e-30 | 40/46 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.590×** | -7.2 | 1e-10 | 34/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.715×** | -6.5 | 1e-08 | 37/47 (CHP-212, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.644×** | -6.0 | 2e-07 | 36/46 (CHP-212, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.676×** | -5.2 | 3e-05 | 29/47 (NCI-H23, NCI-H1573, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **0.728×** | -4.3 | 0.001 | 24/46 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.740×** | -4.1 | 0.003 | 24/47 (A549, A498, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.844× | -3.3 | 0.075 | 18/47 (AsPC-1, SW1417, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.724× | -3.1 | 0.10 | 19/46 (NCI-H661, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | 0.803× | -3.0 | 0.15 | 16/46 (LoVo, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 33.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 42.6 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +9.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.48× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.296× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 37.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.211× (z -11.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0744× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[BT-474 (line)]] | alt | 99.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.108× (z -8.9) |
| [[H4 (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -14.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -21.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[Panc 03.27 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -18.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SNU-423 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[UFD1]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[NECAB3]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NIPA2]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TTL]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PSMD2]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[TPM3]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[VAMP3]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CDK2]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PRIM2]] | +0.60 | +0.74 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIM3]] | -0.69 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[PPP4R2]] | -0.68 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[KMT2E]] | -0.68 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[DBP]] | -0.67 | -0.61 / -0.70 | both halves | 7e-06 |  |
| [[GLIS2]] | -0.67 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[POLR1H]] | -0.65 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[CLK4]] | -0.64 | -0.71 / -0.52 | both halves | 1e-05 |  |
| [[BCOR]] | -0.64 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[MED19]] | -0.64 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[CBX4]] | -0.64 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[COMMD3]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[RAB30]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PNPLA4]] | B | PNPLA4 activity raises ZNF731P's level | lines that do not express PNPLA4 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without PNPLA4 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000285679, PRKCZ, GPR160 |
| [[PSMB5]] | B | PSMB5 activity lowers ZNF731P's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (22.3, -4.0); signed map (-28.4, -31.6). **Vector** length 107, 26.2% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.9 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.5 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -9.8 | -11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.5 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.8 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -6.5 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 731, pseudogene |
| Locus type | pseudogene |
| Location | 1q44 — chr1:247,189,851-247,209,493 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously ZNF731 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32471) · Entrez [729806](https://www.ncbi.nlm.nih.gov/gene/729806) · Ensembl [ENSG00000227671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227671)

## Data

Gene col 13605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13605); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13605]; `tensor/DDL_lfc|DDL_z.npy` [13605]; `embed/gene_vectors.npy` [13605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13605 or target_col == 13605). Every well: [[ZNF731P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF731P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
