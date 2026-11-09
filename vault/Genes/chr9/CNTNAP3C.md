---
symbol: "CNTNAP3C"
type: "gene"
col: 16022
ensembl_id: "ENSG00000283378"
name: "contactin associated protein family member 3C"
location: "9q12"
module: 196
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 27
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 12
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# CNTNAP3C

*contactin associated protein family member 3C* — 9q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.01× (z +8.9, q 3e-16, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.42× (z +4.2, q 0.002, up in 0 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.850× (z -3.9, q 0.033, down in 11 of 23 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.560× (z -3.9, q 0.033, down in 9 of 21 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP3P2]] (+0.78, fdr 7e-06), [[CNTNAP3]] (+0.75, fdr 7e-06), [[CNTNAP3B]] (+0.68, fdr 7e-06); moves opposite to [[EXOC4]] (-0.42, fdr 5e-05), [[TBCK]] (-0.39, fdr 1e-04), [[TTTY14]] (-0.39, fdr 4e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ADAMTSL3]] → it (grade B ⚠); 12 go from it, the strongest it → [[FAM3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.01×** | +8.9 | 3e-16 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.93×** | +6.6 | 9e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +6.1 | 3e-07 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.25×** | +5.6 | 3e-06 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +5.2 | 2e-05 | 1/8 (SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.42×** | +4.2 | 0.002 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.006 | 3/20 (SW1417, SW480, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.022 | 6/21 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.050 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.2 | 0.083 | 2/11 (NCI-H2030, SW480) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +3.2 | 0.083 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.63× | +3.0 | 0.13 | 0/11 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.850× | -3.9 | 0.033 | 11/23 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.560×** | -3.9 | 0.033 | 9/21 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -3.7 | 0.038 | 10/18 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.580×** | -3.5 | 0.072 | 7/22 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.623× | -3.1 | 0.19 | 5/22 (A-427, SNU-423, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 32.4 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 5.65 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0432× (z -13.1) |
| [[A549 (line)]] | wt | 7.08 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0764× (z -9.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.671 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.898 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.168 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.172 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.666 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.699 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.622 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.637 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.559 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP3P2]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP3]] | +0.75 | +0.71 / +0.69 | both halves | 7e-06 | same gene group |
| [[CNTNAP3B]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | same gene group |
| [[PTGIS]] | +0.52 | +0.37 / +0.51 | both halves | 7e-05 | **novel candidate** |
| [[ADAMTS15]] | +0.52 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[DOK5]] | +0.50 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TRIM6]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[ANKRD20A4P]] | +0.48 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ARHGAP20]] | +0.47 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[ENDOD1]] | +0.46 | +0.43 / +0.38 | both halves | 6e-05 |  |
| [[SOX7]] | +0.45 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[FAM3C]] | +0.44 | +0.42 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC4]] | -0.42 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[TBCK]] | -0.39 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[TTTY14]] | -0.39 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[VPS13B]] | -0.38 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[DAB1]] | -0.38 | -0.33 / -0.24 | both halves | 5e-04 |  |
| [[POLDIP2]] | -0.38 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[TAOK1]] | -0.35 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[FSIP2-AS1]] | -0.35 | -0.36 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTSL3]] | B | ADAMTSL3 activity raises CNTNAP3C's level | lines that do not express ADAMTSL3 (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without ADAMTSL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: ANOS1, NTRK3, PSG4; maybe low, not absent |
| [[CNTNAP3]] | C | CNTNAP3 activity raises CNTNAP3C's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 2.32× lower at baseline in the lines without CNTNAP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[CNTNAP3B]] | C | CNTNAP3B activity raises CNTNAP3C's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without CNTNAP3B | 0.017 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[CNTNAP3P2]] | C | CNTNAP3P2 activity raises CNTNAP3C's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without CNTNAP3P2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[WNT7A]] | C | WNT7A activity raises CNTNAP3C's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without WNT7A | 0.054 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM3C]] | B | CNTNAP3C activity raises FAM3C's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without CNTNAP3C | 1e-03 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA |
| [[ENDOD1]] | B | CNTNAP3C activity raises ENDOD1's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without CNTNAP3C | 0.004 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA |
| [[FAM3C]] | B | CNTNAP3C activity strengthens FAM3C's drug response | lines that do not express CNTNAP3C (22) vs lines expressing it (27) | the lines without CNTNAP3C respond 0.85× as strongly (z diff +0.55); strongest at Idarubicin (hydrochloride) 5 µM: 0.70x vs 0.49x (z diff +3.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; target measured in part of the lines; both ways; artifact flags |
| [[OSBPL3]] | B | CNTNAP3C activity raises OSBPL3's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 1.54× lower at baseline in the lines without CNTNAP3C | 0.071 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA |
| [[ELFN2]] | B | CNTNAP3C activity raises ELFN2's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without CNTNAP3C | 0.080 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA |
| [[CNTNAP3]] | C | CNTNAP3C activity raises CNTNAP3's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 4.69× lower at baseline in the lines without CNTNAP3C | 2e-04 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[CNTNAP3P2]] | C | CNTNAP3C activity raises CNTNAP3P2's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 3.05× lower at baseline in the lines without CNTNAP3C | 0.002 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[CNTNAP3B]] | C | CNTNAP3C activity raises CNTNAP3B's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 3.46× lower at baseline in the lines without CNTNAP3C | 0.014 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[GCAWKR]] | C | CNTNAP3C activity raises GCAWKR's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without CNTNAP3C | 0.033 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[ARHGAP20]] | C | CNTNAP3C activity raises ARHGAP20's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without CNTNAP3C | 0.052 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[WNT7A]] | C | CNTNAP3C activity raises WNT7A's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 1.95× lower at baseline in the lines without CNTNAP3C | 0.058 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[AMOTL1]] | C | CNTNAP3C activity raises AMOTL1's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without CNTNAP3C | 0.092 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.8, 28.7); signed map (19.8, 58.7). **Vector** length 40.5, 8.07% of its response variance represented; |z| ≥ 3 in 552 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.8 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | contactin associated protein family member 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q12 — chr9:61,330,717-61,453,030 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Contactin associated protein family |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100289279](https://www.ncbi.nlm.nih.gov/gene/100289279):

> Predicted to be involved in nervous system development and signal transduction. Predicted to be located in membrane. Predicted to be active in plasma membrane and synapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:53878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53878) · Entrez [100289279](https://www.ncbi.nlm.nih.gov/gene/100289279) · Ensembl [ENSG00000283378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283378)

## Data

Gene col 16022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16022); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16022]; `tensor/DDL_lfc|DDL_z.npy` [16022]; `embed/gene_vectors.npy` [16022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16022 or target_col == 16022). Every well: [[CNTNAP3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTNAP3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
