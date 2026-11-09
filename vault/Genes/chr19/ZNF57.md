---
symbol: "ZNF57"
type: "gene"
col: 10192
ensembl_id: "ENSG00000171970"
name: "zinc finger protein 57"
location: "19p13.3"
module: 119
arm: "+"
pooled_cpm: 4.75
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 31
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# ZNF57

*zinc finger protein 57* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.38× (z +22.7, q 0e+00, up in 37 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW1417 0.134×, PANC-1 0.146×, A498 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.0651×, PANC-1 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Rimonabant (drug)]] 0.05 µM in 1 line (KATO III 0.0354×); [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (LS 180 0.0562×); [[Bendamustine (drug)]] 5 µM in 1 line (HS-578T 0.0670×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF77]] (+0.66, fdr 1e-05, ⚠ same locus), [[ZNF555]] (+0.57, fdr 1e-05, ⚠ same locus), [[WDR83]] (+0.50, fdr 6e-05), [[BRPF1]] (+0.49, fdr 4e-05), [[GZF1]] (+0.49, fdr 1e-05); moves opposite to [[XRCC5]] (-0.51, fdr 3e-05), [[GLS]] (-0.48, fdr 3e-05), [[STMP1]] (-0.45, fdr 5e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HES7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.38×** | +22.7 | 0e+00 | 37/40 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.33×** | +19.3 | 0e+00 | 46/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +18.1 | 0e+00 | 32/40 (Panc 03.27, J82, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.73×** | +17.3 | 0e+00 | 45/46 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.50×** | +16.5 | 0e+00 | 46/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.50×** | +16.5 | 0e+00 | 31/39 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +11.8 | 3e-30 | 29/45 (SW480, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.41×** | +11.2 | 5e-27 | 30/44 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.77×** | +10.8 | 3e-25 | 29/43 (SW480, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.15×** | +10.1 | 3e-22 | 28/36 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +9.5 | 1e-19 | 19/37 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +8.1 | 4e-14 | 22/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +7.4 | 5e-12 | 14/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +7.1 | 4e-11 | 19/47 (KATO III, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +7.0 | 1e-10 | 18/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +5.9 | 1e-07 | 13/36 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10192.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW1417 0.134×, PANC-1 0.146×, A498 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.0651×, PANC-1 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Rimonabant (drug)]] 0.05 µM in 1 line (KATO III 0.0354×); [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (LS 180 0.0562×); [[Bendamustine (drug)]] 5 µM in 1 line (HS-578T 0.0670×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.862× | -7.0 | 2e-09 | 17/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.785× | -3.2 | 0.27 | 5/46 (KATO III, RPMI-7951, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | 0.785× | -3.2 | 0.27 | 2/47 (HOP62, Hs 766T) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.794× | -3.0 | 0.27 | 5/45 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.794× | -3.0 | 0.27 | 6/47 (HEC-1-A, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.76 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +14.1) | — |
| [[SW1417 (line)]] | alt | 13.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 3.39 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +9.7) | [[Rimonabant (drug)]] 0.05 µM 0.0354× (z -10.5) |
| [[LS 180 (line)]] | wt | 4.16 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +9.1) | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0562× (z -10.4) |
| [[PANC-1 (line)]] | alt | 5.02 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 4.85 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 3.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 4.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 5.47 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0670× (z -9.4) |
| [[J82 (line)]] | alt | 5.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.76 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0651× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 5.79 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0680× (z -10.0) ⚠ toxic; unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 4.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 5.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 7.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +11.0) | — |
| [[A-172 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 8 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF77]] | +0.66 | +0.73 / +0.52 | both halves | 1e-05 | same gene group; ⚠ same locus (14.7 kb: neighbours can correlate without regulation) |
| [[ZNF555]] | +0.57 | +0.69 / +0.50 | both halves | 1e-05 | same gene group; ⚠ same locus (40.5 kb, same strand: neighbours can correlate without regulation) |
| [[WDR83]] | +0.50 | +0.45 / +0.39 | both halves | 6e-05 |  |
| [[BRPF1]] | +0.49 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[GZF1]] | +0.49 | +0.49 / +0.50 | both halves | 1e-05 | same gene group |
| [[PRICKLE3]] | +0.48 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[PCGF1]] ⚠ | +0.48 | +0.29 / +0.55 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF230]] | +0.47 | +0.49 / +0.46 | both halves | 2e-05 | same gene group |
| [[YJU2B]] | +0.47 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[C1orf35]] | +0.47 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[NFKBIL1]] | +0.47 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[RRAGD]] | +0.47 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[C16orf91]] | +0.46 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[SCYL1]] | +0.46 | +0.25 / +0.41 | both halves | 4e-04 |  |
| [[PARP16]] | +0.46 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC5]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[GLS]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[STMP1]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TMX3]] | -0.43 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[HNRNPC]] | -0.43 | -0.23 / -0.45 | both halves | 5e-04 |  |
| [[ARPC5]] | -0.43 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CMTM6]] | -0.42 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[UBE2V1]] | -0.42 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[VOPP1]] | -0.42 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[CD99L2]] | -0.41 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[TRDMT1]] | -0.41 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[ACTR2]] | -0.41 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES7]] | B | HES7 activity raises ZNF57's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without HES7 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[KREMEN2]] | B | KREMEN2 activity raises ZNF57's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without KREMEN2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-54.7, 1.5); signed map (-7.1, -8.1). **Vector** length 54.5, 7.44% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +18.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +22.7 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +2.3 | +5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +10.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +5.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.1 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.1 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -1.6 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 57 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,900,928-2,918,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF424 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68EA5](https://www.uniprot.org/uniprotkb/Q68EA5) (Zinc finger protein 57):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [126295](https://www.ncbi.nlm.nih.gov/gene/126295):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13125) · Entrez [126295](https://www.ncbi.nlm.nih.gov/gene/126295) · UniProt [Q68EA5](https://www.uniprot.org/uniprotkb/Q68EA5) · Ensembl [ENSG00000171970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171970)

## Data

Gene col 10192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10192); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10192]; `tensor/DDL_lfc|DDL_z.npy` [10192]; `embed/gene_vectors.npy` [10192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10192 or target_col == 10192). Every well: [[ZNF57 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF57.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
