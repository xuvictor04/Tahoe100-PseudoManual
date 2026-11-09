---
symbol: "SHISA9"
type: "gene"
col: 14139
ensembl_id: "ENSG00000237515"
name: "shisa family member 9"
location: "16p13.12"
module: 27
arm: "+"
pooled_cpm: 7.52
n_lines_expressing: 12
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 18
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SHISA9

*shisa family member 9* — 16p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.78× (z +15.3, q 0e+00, up in 2 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.106×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.182×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.191×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02254]] (+0.65, fdr 1e-05), [[APCDD1]] (+0.64, fdr 8e-06), [[SMOC2]] (+0.64, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PSG1]] → it (grade C ⚠); 18 go from it, the strongest it → [[DKK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.78×** | +15.3 | 0e+00 | 2/6 (A-172, BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.57×** | +11.9 | 2e-30 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.27×** | +11.9 | 4e-30 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +7.3 | 6e-11 | 1/4 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +6.4 | 2e-08 | 3/6 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +6.2 | 4e-08 | 5/8 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.98×** | +5.6 | 2e-06 | 4/8 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +5.0 | 3e-05 | 1/6 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.2 | 0.002 | 1/6 (SK-MEL-2) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.00×** | +4.0 | 0.003 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.008 | 2/7 (NCI-H23, SK-MEL-2) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.5 | 0.021 | 2/6 (HEC-1-A, A-172) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.067 | 4/7 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.079 | 0/6 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.079 | 5/7 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.106×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.182×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.191×; ⚠ toxic; transcription drop).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 13.4× (z +11.3) | — |
| [[SW480 (line)]] | alt | 73.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -10.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02254]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[APCDD1]] | +0.64 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[SMOC2]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PSG1]] | +0.64 | +0.69 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[LINC03042]] | +0.64 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[VWA2]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[JAKMIP2-AS1]] | +0.62 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ST18]] | +0.62 | +0.57 / +0.60 | both halves | 8e-06 |  |
| [[IGFL4]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NMNAT3]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[SLC30A10]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PWWP3B]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSG1]] | C | PSG1 activity raises SHISA9's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 4.22× lower at baseline in the lines without PSG1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[POU3F2]] | C | POU3F2 activity raises SHISA9's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.81× lower at baseline in the lines without POU3F2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |
| [[ANKRD1]] | C | ANKRD1 activity raises SHISA9's level | lines that do not express ANKRD1 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without ANKRD1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CAVIN2-AS1, WNT7A, NPPB; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises SHISA9's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 1.49× lower at baseline in the lines without CSMD3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises SHISA9's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.79× lower at baseline in the lines without PSG4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[CDK15]] | C | CDK15 activity raises SHISA9's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 1.55× lower at baseline in the lines without CDK15 | 0.050 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent; co-absent with the target |
| [[FGF19]] | C | FGF19 activity raises SHISA9's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 1.77× lower at baseline in the lines without FGF19 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[PAX8]] | C | PAX8 activity raises SHISA9's level | lines that do not express PAX8 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without PAX8 | 0.067 | ⚠ within organs, on part of the lines; also absent: FGF19, RGPD2, BMP10; co-absent with the target |
| [[TMEM163]] | C | TMEM163 activity raises SHISA9's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.56× lower at baseline in the lines without TMEM163 | 0.077 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[SCN5A]] | C | SCN5A activity raises SHISA9's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without SCN5A | 0.086 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9; co-absent with the target |
| [[LINC02050]] | C | LINC02050 activity raises SHISA9's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without LINC02050 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1; co-absent with the target |
| [[ANO4]] | C | ANO4 activity raises SHISA9's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without ANO4 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 2, C 16. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DKK2]] | B | SHISA9 activity raises DKK2's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.46× lower at baseline in the lines without SHISA9 | 0.032 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent |
| [[LINC03042]] | B | SHISA9 activity raises LINC03042's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.67× lower at baseline in the lines without SHISA9 | 0.063 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent |
| [[SCN5A]] | C | SHISA9 activity raises SCN5A's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 2.82× lower at baseline in the lines without SHISA9 | 0.001 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[JAKMIP2-AS1]] | C | SHISA9 activity raises JAKMIP2-AS1's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 2.09× lower at baseline in the lines without SHISA9 | 0.002 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[FGF19]] | C | SHISA9 activity raises FGF19's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.60× lower at baseline in the lines without SHISA9 | 0.002 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[ADGRG5]] | C | SHISA9 activity raises ADGRG5's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.22× lower at baseline in the lines without SHISA9 | 0.021 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[ANO4]] | C | SHISA9 activity raises ANO4's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without SHISA9 | 0.023 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[PAX8]] | C | SHISA9 activity raises PAX8's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.88× lower at baseline in the lines without SHISA9 | 0.033 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[LINC00491]] | C | SHISA9 activity raises LINC00491's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 2.07× lower at baseline in the lines without SHISA9 | 0.036 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[IGFL4]] | C | SHISA9 activity raises IGFL4's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.52× lower at baseline in the lines without SHISA9 | 0.040 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[ANKRD1]] | C | SHISA9 activity raises ANKRD1's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 2.25× lower at baseline in the lines without SHISA9 | 0.050 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[GJB1]] | C | SHISA9 activity raises GJB1's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.50× lower at baseline in the lines without SHISA9 | 0.058 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, 43.2); signed map (63.3, 16.0). **Vector** length 31.4, 13.0% of its response variance represented; |z| ≥ 3 in 162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.2 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +0.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +4.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | +0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -1.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | shisa family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.12 — chr16:12,901,598-13,240,416 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Shisa family members |
| Matched by | ensembl_id |

**Function**, from UniProt [B4DS77](https://www.uniprot.org/uniprotkb/B4DS77) (Protein shisa-9):

> Regulator of short-term neuronal synaptic plasticity in the dentate gyrus. Associates with AMPA receptors (ionotropic glutamate receptors) in synaptic spines and promotes AMPA receptor desensitization at excitatory synapses (By similarity).

**Summary**, from NCBI Gene [729993](https://www.ncbi.nlm.nih.gov/gene/729993):

> Predicted to enable PDZ domain binding activity. Predicted to be involved in regulation of short-term neuronal synaptic plasticity. Predicted to act upstream of or within regulation of AMPA receptor activity. Predicted to be located in synapse. Predicted to be part of AMPA glutamate receptor complex. Predicted to be active in dendritic spine membrane; postsynaptic density; and postsynaptic membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37231) · Entrez [729993](https://www.ncbi.nlm.nih.gov/gene/729993) · UniProt [B4DS77](https://www.uniprot.org/uniprotkb/B4DS77) · Ensembl [ENSG00000237515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237515)

## Data

Gene col 14139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14139); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14139]; `tensor/DDL_lfc|DDL_z.npy` [14139]; `embed/gene_vectors.npy` [14139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14139 or target_col == 14139). Every well: [[SHISA9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHISA9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
