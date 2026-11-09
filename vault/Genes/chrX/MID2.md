---
symbol: "MID2"
type: "gene"
col: 1284
ensembl_id: "ENSG00000080561"
name: "midline 2"
location: "Xq22.3"
module: 160
arm: "-"
pooled_cpm: 24.61
n_lines_expressing: 33
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# MID2

*midline 2* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.89× (z +8.1, q 5e-13, up in 27 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.336× (z -14.6, q 1e-45, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLTP3B]] (+0.56, fdr 5e-05), [[UBE2Q2]] (+0.55, fdr 3e-05), [[RNF14]] (+0.53, fdr 1e-04); moves opposite to [[THRAP3]] (-0.53, fdr 2e-05), [[NR4A1]] (-0.51, fdr 4e-05), [[SRRT]] (-0.49, fdr 3e-05).
> It sits in the **-** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 3 go from it, the strongest it → [[RP9P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.89×** | +8.1 | 5e-13 | 27/31 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +6.8 | 2e-09 | 25/31 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +6.4 | 3e-08 | 23/31 (BT-474, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +5.7 | 2e-06 | 23/31 (PANC-1, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 7e-05 | 17/31 (SNU-423, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 7e-05 | 16/31 (BT-474, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.005 | 13/30 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.035 | 13/31 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.15 | 11/31 (CFPAC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.336×** | -14.6 | 1e-45 | 28/31 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.379×** | -13.0 | 5e-36 | 29/31 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.439×** | -11.0 | 5e-26 | 24/29 (NCI-H1573, NCI-H2347, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.479×** | -9.9 | 9e-21 | 27/31 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.540×** | -7.9 | 2e-13 | 18/23 (NCI-H2347, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.536×** | -7.7 | 1e-12 | 18/26 (SW1417, NCI-H2347, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.620×** | -6.2 | 6e-08 | 19/29 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.785×** | -4.6 | 3e-04 | 16/31 (SW 1271, Panc 03.27, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.028 | 12/31 (SW480, HOP62, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.775×** | -3.4 | 0.036 | 13/31 (HOP62, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 111 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.237× (z -13.8) |
| [[RKO (line)]] | wt | 38.8 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -13.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.220× (z -9.9) |
| [[A-172 (line)]] | wt | 29.4 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -15.6) |
| [[SNU-423 (line)]] | alt | 89.2 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -14.9) |
| [[HOP62 (line)]] | alt | 75.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -13.0) |
| [[A549 (line)]] | wt | 35.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -12.7) |
| [[BT-474 (line)]] | alt | 34.9 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -9.6) |
| [[J82 (line)]] | alt | 21.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.228× (z -10.4) |
| [[PANC-1 (line)]] | alt | 33.4 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.17× (z +10.8) | — |
| [[H4 (line)]] | wt | 27.8 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.71× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -8.7) |
| [[HCT15 (line)]] | alt | 37.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.216× (z -9.9) |
| [[Hs 766T (line)]] | wt | 49.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 21.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -8.7) |
| [[AN3 CA (line)]] | alt | 54.5 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.109× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 7.68 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0618× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -9.1) |
| [[LoVo (line)]] | wt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0773× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0646× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP3B]] | +0.56 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[UBE2Q2]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[RNF14]] | +0.53 | +0.57 / +0.36 | both halves | 1e-04 | same gene group |
| [[C9orf72]] | +0.53 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[CRTC3]] | +0.52 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[DHRS7]] | +0.52 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[PCGF5]] | +0.51 | +0.51 / +0.46 | both halves | 3e-05 | same gene group |
| [[PSMD8]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[PRDM2]] | +0.51 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[TYRO3]] | +0.49 | +0.47 / +0.34 | both halves | 1e-04 | same gene group |
| [[MOB1B]] | +0.49 | +0.48 / +0.31 | both halves | 2e-04 |  |
| [[DUSP22]] | +0.48 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THRAP3]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NR4A1]] | -0.51 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SRRT]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[PRPF3]] | -0.44 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[HNRNPD]] | -0.43 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[ZNF628]] | -0.43 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[SCART1]] | -0.42 | -0.32 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[EXOC3]] | -0.41 | -0.23 / -0.30 | both halves | 5e-04 |  |
| [[CTNND1]] | -0.41 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[VCL]] | -0.41 | -0.42 / -0.26 | both halves | 4e-04 |  |
| [[AQR]] | -0.41 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[NUP160]] | -0.40 | -0.18 / -0.37 | ⚠ not reproduced | 1e-03 |  |
| [[C1QTNF3-AMACR]] | -0.40 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[DCAF1]] | -0.40 | -0.23 / -0.39 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers MID2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MID2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RP9P]] | B | MID2 activity lowers RP9P's level | lines that do not express MID2 (17) vs lines expressing it (33) | 1.56× higher at baseline in the lines without MID2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF711, FRMPD3, RPS6KA6 |
| [[CTNND1]] | B | MID2 activity raises CTNND1's level | lines that do not express MID2 (17) vs lines expressing it (33) | 1.38× lower at baseline in the lines without MID2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF711, FRMPD3, RPS6KA6 |
| [[CACNB3]] | B | MID2 activity raises CACNB3's level | lines that do not express MID2 (17) vs lines expressing it (33) | 1.23× lower at baseline in the lines without MID2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF711, FRMPD3, RPS6KA6 |

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **-** arm (projection on the module's main direction -0.202). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-12.0, 17.0); signed map (-22.0, -0.9). **Vector** length 69.5, 16.0% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -13.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | midline 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:107,825,755-107,931,637 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FXY2, TRIM1, RNF60, MRX101 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; Fibronectin type III domain containing; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJV3](https://www.uniprot.org/uniprotkb/Q9UJV3) (E3 ubiquitin-protein ligase MID2):

> E3 ubiquitin-protein ligase that plays a role in microtubule stabilization. Mediates the 'Lys-48'-linked polyubiquitination of LRRK2 to drive its localization to microtubules and its proteasomal degradation in neurons. This ubiquitination inhibits LRRK2 kinase activation by RAB29.

**Summary**, from NCBI Gene [11043](https://www.ncbi.nlm.nih.gov/gene/11043):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to microtubular structures in the cytoplasm. Alternate splicing of this gene results in two transcript variants encoding different isoforms. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:7096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7096) · Entrez [11043](https://www.ncbi.nlm.nih.gov/gene/11043) · UniProt [Q9UJV3](https://www.uniprot.org/uniprotkb/Q9UJV3) · Ensembl [ENSG00000080561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080561)

## Data

Gene col 1284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1284); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1284]; `tensor/DDL_lfc|DDL_z.npy` [1284]; `embed/gene_vectors.npy` [1284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1284 or target_col == 1284). Every well: [[MID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
