---
symbol: "HOXA5"
type: "gene"
col: 2703
ensembl_id: "ENSG00000106004"
name: "homeobox A5"
location: "7p15.2"
module: 201
arm: "+"
pooled_cpm: 7.44
n_lines_expressing: 41
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXA5

*homeobox A5* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.09× (z +5.4, q 3e-05, up in 18 of 24 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +4.8, q 4e-04, up in 19 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.388× (z -7.2, q 4e-10, down in 30 of 36 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (A498 0.113×, HT-29 0.176×, SW1417 0.238×; ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HT-29 0.0533×, A498 0.127×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.110×; ⚠ toxic; transcription drop); [[EX229 (drug)]] 5 µM in 1 line (A498 0.0199×); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.172×); [[Neratinib (drug)]] 5 µM in 1 line (NCI-H23 0.0705×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA6]] (+0.79, fdr 7e-06, ⚠ same locus), [[HOXA9]] (+0.72, fdr 7e-06, ⚠ same locus), [[HOXA3]] (+0.70, fdr 7e-06, ⚠ same locus), [[TERF2IP]] (+0.68, fdr 1e-05), [[DHRS3]] (+0.66, fdr 1e-05), [[EAPP]] (+0.65, fdr 2e-05); moves opposite to [[EFTUD2]] (-0.63, fdr 2e-05), [[CORO1C]] (-0.63, fdr 1e-05), [[CNDP2]] (-0.62, fdr 1e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HOXA10]] → it (grade B ⚠); 9 go from it, the strongest it → [[RNASE4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +5.4 | 3e-05 | 18/24 (SW1417, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.8 | 4e-04 | 19/32 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.017 | 15/36 (HT-29, SK-MEL-2, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.64×** | +3.8 | 0.020 | 9/25 (SW1417, A549, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **2.33×** | +3.4 | 0.079 | 9/30 (A498, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2703.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (A498 0.113×, HT-29 0.176×, SW1417 0.238×; ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HT-29 0.0533×, A498 0.127×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.110×; ⚠ toxic; transcription drop); [[EX229 (drug)]] 5 µM in 1 line (A498 0.0199×); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.172×); [[Neratinib (drug)]] 5 µM in 1 line (NCI-H23 0.0705×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.388×** | -7.2 | 4e-10 | 30/36 (A498, HT-29, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -3.1 | 0.37 | 12/38 (A549, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.667× | -3.1 | 0.37 | 15/36 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 23.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0533× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.172× (z -9.7) |
| [[A498 (line)]] | wt | 23.9 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.113× (z -12.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0199× (z -11.4) |
| [[LS 180 (line)]] | wt | 12.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 9.11 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0964× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 4.11 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0705× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 3.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0589× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -9.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA6]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 | same gene group; STRING 969; ⚠ same locus (1.7 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA9]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 | same gene group; STRING 776; ⚠ same locus (18.8 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA3]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 | same gene group; STRING 805; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TERF2IP]] | +0.68 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[HOXA10]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 | same gene group; STRING 883; ⚠ same locus (26.9 kb, same strand: neighbours can correlate without regulation) |
| [[DHRS3]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[EAPP]] | +0.65 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[TRIM7-AS2]] | +0.65 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[HOXA11]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | same gene group; STRING 513; ⚠ same locus (37.5 kb, same strand: neighbours can correlate without regulation) |
| [[HEIH]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ARID4B]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.60 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[SAP30]] | +0.60 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[CDC37L1]] | +0.60 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[DCAF5]] | +0.60 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.63 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[CORO1C]] | -0.63 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[CNDP2]] | -0.62 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[BOP1]] | -0.62 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[FARSB]] | -0.60 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[WDR77]] | -0.60 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[ADAMTSL5]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.59 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[NUP188]] | -0.59 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[GATAD2A]] | -0.58 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[WDR1]] | -0.58 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[BRD9]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA10]] | B | HOXA10 activity raises HOXA5's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without HOXA10 | 0.054 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11 |
| [[HOXA6]] | C | HOXA6 activity raises HOXA5's level | lines that do not express HOXA6 (13) vs lines expressing it (37) | 2.81× lower at baseline in the lines without HOXA6 | 0.007 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA5; maybe low, not absent; co-absent with the target |
| [[HOXA3]] | C | HOXA3 activity raises HOXA5's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 3.17× lower at baseline in the lines without HOXA3 | 0.007 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNASE4]] | B | HOXA5 activity raises RNASE4's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without HOXA5 | 0.032 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[RSBN1L]] | B | HOXA5 activity lowers RSBN1L's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.06× higher at baseline in the lines without HOXA5 | 0.043 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[RSRP1]] | B | HOXA5 activity raises RSRP1's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without HOXA5 | 0.046 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[CEP170B]] | B | HOXA5 activity lowers CEP170B's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.21× higher at baseline in the lines without HOXA5 | 0.075 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[MAP3K2]] | B | HOXA5 activity raises MAP3K2's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.20× lower at baseline in the lines without HOXA5 | 0.083 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[SPTBN2]] | B | HOXA5 activity lowers SPTBN2's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.61× higher at baseline in the lines without HOXA5 | 0.086 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[SYF2]] | B | HOXA5 activity raises SYF2's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without HOXA5 | 0.094 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[HOXA6]] | C | HOXA5 activity raises HOXA6's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 2.54× lower at baseline in the lines without HOXA5 | 0.019 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1; co-absent with the target |
| [[HOXA3]] | C | HOXA5 activity raises HOXA3's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 3.62× lower at baseline in the lines without HOXA5 | 0.029 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1; co-absent with the target |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.2, 27.6); signed map (-5.3, 6.6). **Vector** length 69.9, 15.3% of its response variance represented; |z| ≥ 3 in 609 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Kidney development* (reactome, mean cos +0.63 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.3 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | homeobox A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,141,052-27,143,681 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX1C, HOX1 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P20719](https://www.uniprot.org/uniprotkb/P20719) (Homeobox protein Hox-A5):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis. Also binds to its own promoter. Binds specifically to the motif 5'-CYYNATTA[TG]Y-3'.

**Summary**, from NCBI Gene [3202](https://www.ncbi.nlm.nih.gov/gene/3202):

> In vertebrates, the genes encoding the class of transcription factors called homeobox genes are found in clusters named A, B, C, and D on four separate chromosomes. Expression of these proteins is spatially and temporally regulated during embryonic development. This gene is part of the A cluster on chromosome 7 and encodes a DNA-binding transcription factor which may regulate gene expression, morphogenesis, and differentiation. Methylation of this gene may result in the loss of its expression …

**Accessions** — [HGNC:5106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5106) · Entrez [3202](https://www.ncbi.nlm.nih.gov/gene/3202) · UniProt [P20719](https://www.uniprot.org/uniprotkb/P20719) · Ensembl [ENSG00000106004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106004)

## Data

Gene col 2703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2703); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2703]; `tensor/DDL_lfc|DDL_z.npy` [2703]; `embed/gene_vectors.npy` [2703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2703 or target_col == 2703). Every well: [[HOXA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
