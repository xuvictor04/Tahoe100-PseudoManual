---
symbol: "PAX6"
type: "gene"
col: 143
ensembl_id: "ENSG00000007372"
name: "paired box 6"
location: "11p13"
module: 22
arm: "+"
pooled_cpm: 8.44
n_lines_expressing: 20
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 7
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PAX6

*paired box 6* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +15.1, q 0e+00, up in 12 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.720× (z -3.8, q 0.066, down in 5 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.277×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H661 0.0625×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.299×; ⚠ cell-cycle shift, explains ~0% of this change); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0654×); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H661 0.146×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCH1]] (+0.59, fdr 4e-05), [[CNOT6L]] (+0.57, fdr 7e-05), [[UBALD2]] (+0.53, fdr 8e-05); moves opposite to [[RRP15]] (-0.49, fdr 2e-04), [[PITPNB]] (-0.48, fdr 9e-05), [[TAF2]] (-0.46, fdr 4e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 7 go from it, the strongest it → [[GATA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +15.1 | 0e+00 | 12/18 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +9.6 | 3e-19 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +8.2 | 4e-14 | 1/13 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +6.9 | 1e-09 | 12/16 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.5 | 1e-08 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +5.2 | 2e-05 | 4/15 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 3/18 (J82, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.3 | 0.001 | 8/18 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.71×** | +4.3 | 0.001 | 3/14 (SNU-423, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.004 | 11/17 (HOP62, SW480, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.0 | 0.004 | 1/12 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.60×** | +3.8 | 0.008 | 1/12 (Hs 766T) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.6 | 0.011 | 0/18 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.014 | 1/16 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.014 | 4/17 (Hs 766T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.063 | 2/16 (RPMI-7951, NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 143.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.277×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H661 0.0625×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.299×; ⚠ cell-cycle shift, explains ~0% of this change); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0654×); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H661 0.146×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.720×** | -3.8 | 0.066 | 5/18 (SNU-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -3.6 | 0.066 | 11/18 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -3.6 | 0.066 | 5/18 (NCI-H23, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 112 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -13.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0625× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.146× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0654× (z -9.6) |
| [[SW480 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -9.9) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.966 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.898 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.899 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCH1]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 | STRING 494 |
| [[CNOT6L]] | +0.57 | +0.37 / +0.63 | both halves | 7e-05 |  |
| [[UBALD2]] | +0.53 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[PTTG1]] | +0.53 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[REEP4]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[CDC25C]] | +0.51 | +0.26 / +0.61 | both halves | 4e-04 |  |
| [[GLRX5]] | +0.51 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[GATA2]] | +0.50 | +0.31 / +0.54 | both halves | 2e-04 | STRING 440 |
| [[TSHZ1]] | +0.50 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[SATB2-AS1]] | +0.49 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[JMY]] | +0.48 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[PIMREG]] | +0.48 | +0.26 / +0.57 | both halves | 4e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP15]] | -0.49 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[PITPNB]] | -0.48 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[TAF2]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[HARS1]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 | STRING 415 |
| [[ATXN10]] | -0.46 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[EFTUD2]] | -0.44 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[SUMF1]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[PUM3]] | -0.42 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[IQCG]] | -0.42 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[BBS1]] | -0.41 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[CHMP3]] | -0.41 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[GDAP1]] | -0.41 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[UTP20]] | -0.41 | -0.29 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GATA2]] | B | PAX6 activity raises GATA2's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without PAX6 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[PTCH1]] | B | PAX6 activity raises PTCH1's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without PAX6 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[RHEBL1]] | B | PAX6 activity raises RHEBL1's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.48× lower at baseline in the lines without PAX6 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[USP28]] | B | PAX6 activity raises USP28's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.44× lower at baseline in the lines without PAX6 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[NR2F1]] | B | PAX6 activity raises NR2F1's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 2.58× lower at baseline in the lines without PAX6 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[RRP15]] | B | PAX6 activity raises RRP15's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.22× lower at baseline in the lines without PAX6 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[PEG3]] | C | PAX6 activity raises PEG3's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without PAX6 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.387). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.0, -58.5); signed map (-53.2, -39.0). **Vector** length 37.8, 8.07% of its response variance represented; |z| ≥ 3 in 346 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +15.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +4.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.5 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | +0.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.8 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | paired box 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:31,784,779-31,817,961 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D11S812E, AN, WAGR; previously AN1, AN2 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes; Paired boxes |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 10 pathways, smallest: Formation of the anterior neural plate; Regulation of gene expression in beta cells; Synthesis, secretion, and inactivation of Glucose-dependent Insulinotropic Polypeptide (GIP) |
| Matched by | ensembl_id |

**Function**, from UniProt [P26367](https://www.uniprot.org/uniprotkb/P26367) (Paired box protein Pax-6):

> Transcription factor with important functions in the development of the eye, nose, central nervous system and pancreas. Required for the differentiation of pancreatic islet alpha cells (By similarity). Competes with PAX4 in binding to a common element in the glucagon, insulin and somatostatin promoters. Regulates specification of the ventral neuron subtypes by establishing the correct progenitor domains (By similarity). Acts as a transcriptional repressor of NFATC1-mediated gene expression (By …

**Summary**, from NCBI Gene [5080](https://www.ncbi.nlm.nih.gov/gene/5080):

> This gene encodes paired box protein Pax-6, one of many human homologs of the Drosophila melanogaster gene prd. In addition to a conserved paired box domain, a hallmark feature of this gene family, the encoded protein also contains a homeobox domain. Both domains are known to bind DNA and function as regulators of gene transcription. Activity of this protein is key in the development of neural tissues, particularly the eye. This gene is regulated by multiple enhancers located up to hundreds of …

**Accessions** — [HGNC:8620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8620) · Entrez [5080](https://www.ncbi.nlm.nih.gov/gene/5080) · UniProt [P26367](https://www.uniprot.org/uniprotkb/P26367) · Ensembl [ENSG00000007372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007372)

## Data

Gene col 143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 143); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 143]; `tensor/DDL_lfc|DDL_z.npy` [143]; `embed/gene_vectors.npy` [143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 143 or target_col == 143). Every well: [[PAX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
