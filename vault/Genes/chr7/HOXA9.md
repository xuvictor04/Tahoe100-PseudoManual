---
symbol: "HOXA9"
type: "gene"
col: 1221
ensembl_id: "ENSG00000078399"
name: "homeobox A9"
location: "7p15.2"
module: 201
arm: "+"
pooled_cpm: 15.12
n_lines_expressing: 19
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXA9

*homeobox A9* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +9.1, q 8e-17, up in 14 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.201×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.183×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA10]] (+0.74, fdr 7e-06, ⚠ same locus), [[HOXA5]] (+0.72, fdr 7e-06, ⚠ same locus), [[HOXA11]] (+0.68, fdr 7e-06, ⚠ same locus), [[HOXB5]] (+0.63, fdr 2e-05), [[THAP3]] (+0.62, fdr 1e-05), [[LINC02256]] (+0.60, fdr 2e-05); moves opposite to [[ACSL5]] (-0.58, fdr 3e-05), [[PIK3AP1]] (-0.56, fdr 3e-05), [[CORO1C]] (-0.54, fdr 3e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[HOXA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.1 | 8e-17 | 14/17 (A-172, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +7.0 | 9e-10 | 9/15 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +6.1 | 2e-07 | 11/15 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +5.9 | 4e-07 | 2/12 (A-172, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.55×** | +4.8 | 2e-04 | 9/17 (LS 180, SW1417, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.7 | 3e-04 | 6/17 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +4.3 | 0.001 | 7/17 (RKO, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.011 | 6/17 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +3.7 | 0.012 | 4/13 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.6 | 0.021 | 5/17 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.56×** | +3.5 | 0.026 | 0/17 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.4 | 0.036 | 10/17 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.53×** | +3.3 | 0.040 | 8/14 (HS-578T, SW1417, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.201×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.183×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 74.2 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +16.0) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.85 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.7) | — |
| [[LoVo (line)]] | wt | 49.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -9.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 84.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.9) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SW48 (line)]] | wt | 61.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +8.8) | — |
| [[A-427 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA10]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 | same gene group; STRING 931; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA5]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 | same gene group; STRING 776; ⚠ same locus (18.8 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA11]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 | same gene group; STRING 633; ⚠ same locus (6.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB5]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 | same gene group; STRING 410 |
| [[THAP3]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LINC02256]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[HOXA6]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 | same gene group; STRING 530; ⚠ same locus (11.8 kb, same strand: neighbours can correlate without regulation) |
| [[HEIH]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.59 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[HOXA3]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 | same gene group; STRING 733; ⚠ same locus (9.9 kb, same strand: neighbours can correlate without regulation) |
| [[MTIF3]] | +0.58 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[KLHDC2]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CDC37L1]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PPOX]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RCOR3]] | +0.56 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[TERF2IP]] | +0.56 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[ANKRD54]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL5]] | -0.58 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[PIK3AP1]] | -0.56 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[CORO1C]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[EIF2S1]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[JPH1]] | -0.52 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[MIR222HG]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[LINC01819]] | -0.52 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[TPRXL]] | -0.51 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PITPNB]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[FUT4]] | -0.51 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[LINC02474]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ANO1]] | -0.50 | -0.54 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HOXA9's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXA10-AS]] | C | HOXA10-AS activity raises HOXA9's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 4.77× lower at baseline in the lines without HOXA10-AS | 0.007 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent; co-absent with the target |
| [[HEPHL1]] | C | HEPHL1 activity raises HOXA9's level | lines that do not express HEPHL1 (45) vs lines expressing it (5) | 6.96× lower at baseline in the lines without HEPHL1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KRT20, GPR15, APOB; co-absent with the target |
| [[HOXA11]] | C | HOXA11 activity raises HOXA9's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 5.71× lower at baseline in the lines without HOXA11 | 0.016 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3; co-absent with the target |
| [[HOXA10]] | C | HOXA10 activity raises HOXA9's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 3.94× lower at baseline in the lines without HOXA10 | 0.023 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises HOXA9's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 3.43× lower at baseline in the lines without LINC01819 | 0.041 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[PIWIL1]] | C | PIWIL1 activity raises HOXA9's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.76× lower at baseline in the lines without PIWIL1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA9 activity raises HOXA3's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 2.86× lower at baseline in the lines without HOXA9 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[HOXA6]] | B | HOXA9 activity raises HOXA6's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without HOXA9 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[EAPP]] | B | HOXA9 activity lowers EAPP's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 1.22× higher at baseline in the lines without HOXA9 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[PRKAB2]] | B | HOXA9 activity raises PRKAB2's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 1.05× lower at baseline in the lines without HOXA9 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[SNHG9]] | B | HOXA9 activity raises SNHG9's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 1.32× lower at baseline in the lines without HOXA9 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[CDC37L1]] | B | HOXA9 activity raises CDC37L1's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 1.45× lower at baseline in the lines without HOXA9 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[HOXA10-AS]] | C | HOXA9 activity raises HOXA10-AS's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without HOXA9 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33; co-absent with the target |
| [[HOXA10]] | C | HOXA9 activity raises HOXA10's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 5.29× lower at baseline in the lines without HOXA9 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33; co-absent with the target |
| [[HOXA11]] | C | HOXA9 activity raises HOXA11's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 4.19× lower at baseline in the lines without HOXA9 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33; co-absent with the target |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.3, 27.7); signed map (-5.3, 6.5). **Vector** length 45.5, 13.2% of its response variance represented; |z| ≥ 3 in 299 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Kidney development* (reactome, mean cos +0.56 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.6 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | homeobox A9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,162,438-27,175,180 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX1G, HOX1 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P31269](https://www.uniprot.org/uniprotkb/P31269) (Homeobox protein Hox-A9):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis. Required for induction of SELE/E-selectin and VCAM1 on the endothelial cells surface at sites of inflammation. Positively regulates EIF4E-mediated mRNA nuclear export and also increases the translation efficiency of ODC mRNA in the cytoplasm by competing with factors which repress EIF4E activity such as PRH (By …

**Summary**, from NCBI Gene [3205](https://www.ncbi.nlm.nih.gov/gene/3205):

> In vertebrates, the genes encoding the class of transcription factors called homeobox genes are found in clusters named A, B, C, and D on four separate chromosomes. Expression of these proteins is spatially and temporally regulated during embryonic development. This gene is part of the A cluster on chromosome 7 and encodes a DNA-binding transcription factor which may regulate gene expression, morphogenesis, and differentiation. This gene is highly similar to the abdominal-B (Abd-B) gene of …

**Accessions** — [HGNC:5109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5109) · Entrez [3205](https://www.ncbi.nlm.nih.gov/gene/3205) · UniProt [P31269](https://www.uniprot.org/uniprotkb/P31269) · Ensembl [ENSG00000078399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078399)

## Data

Gene col 1221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1221); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1221]; `tensor/DDL_lfc|DDL_z.npy` [1221]; `embed/gene_vectors.npy` [1221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1221 or target_col == 1221). Every well: [[HOXA9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
