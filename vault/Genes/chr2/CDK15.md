---
symbol: "CDK15"
type: "gene"
col: 6168
ensembl_id: "ENSG00000138395"
name: "cyclin dependent kinase 15"
location: "2q33.1"
module: 27
arm: "+"
pooled_cpm: 2.61
n_lines_expressing: 22
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 22
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CDK15

*cyclin dependent kinase 15* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.20× (z +19.0, q 0e+00, up in 7 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.591× (z -4.3, q 0.005, down in 8 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.0927×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.104×; ⚠ cell-cycle shift, explains ~47% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.101×); [[Selinexor (drug)]] 5 µM in 1 line (HOP62 0.163×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGFBI]] (+0.60, fdr 1e-05), [[PSG1]] (+0.57, fdr 1e-05), [[SLCO6A1]] (+0.51, fdr 3e-04); moves opposite to [[CSTB]] (-0.41, fdr 1e-04), [[GSTO1]] (-0.38, fdr 2e-04), [[DAPK1]] (-0.36, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ANTXR1]] → it (grade B ⚠); 22 go from it, the strongest it → [[ZFPM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.20×** | +19.0 | 0e+00 | 7/14 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.94×** | +15.2 | 0e+00 | 4/6 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.27×** | +15.0 | 0e+00 | 9/11 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.32×** | +12.6 | 2e-34 | 4/7 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.68×** | +8.0 | 1e-13 | 5/16 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.7 | 1e-06 | 2/9 (RPMI-7951, CFPAC-1) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.5 | 3e-06 | 1/17 (SNU-423) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.55×** | +5.5 | 3e-06 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +4.8 | 1e-04 | 3/15 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.06×** | +4.2 | 0.001 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.8 | 0.007 | 6/14 (SNU-423, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +3.6 | 0.014 | 0/12 | top dose only | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.41×** | +3.6 | 0.014 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.014 | 3/16 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +3.4 | 0.029 | 0/13 | top dose only | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.051 | 2/17 (RPMI-7951, PANC-1) | rises with dose |  |
| [[AZD-7648 (drug)]] 5 µM |  | **2.14×** | +3.1 | 0.058 | 4/11 (HOP62, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.075 | 5/14 (PANC-1, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6168.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.0927×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.104×; ⚠ cell-cycle shift, explains ~47% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.101×); [[Selinexor (drug)]] 5 µM in 1 line (HOP62 0.163×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -4.3 | 0.005 | 8/16 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.591×** | -4.3 | 0.005 | 6/15 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | 0.691× | -3.0 | 0.46 | 2/17 (RPMI-7951, HS-578T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.46 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 2.25× (z +9.6) ⚠ position not correctable | [[Selinexor (drug)]] 5 µM 0.163× (z -8.6) |
| [[SW480 (line)]] | alt | 8.81 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0927× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0503× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -8.6) |
| [[PANC-1 (line)]] | alt | 2.78 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.449 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFBI]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[PSG1]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[SLCO6A1]] | +0.51 | +0.62 / +0.28 | both halves | 3e-04 |  |
| [[NTM]] | +0.51 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[ROBO2]] | +0.51 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[CALD1]] | +0.49 | +0.42 / +0.39 | both halves | 6e-05 |  |
| [[CAV1]] | +0.48 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[NREP]] | +0.48 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[NID2]] | +0.47 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[COL3A1]] | +0.47 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[COL4A1]] | +0.46 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[F10]] | +0.46 | +0.53 / +0.26 | both halves | 3e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTB]] | -0.41 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[GSTO1]] | -0.38 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[DAPK1]] | -0.36 | -0.42 / -0.15 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANTXR1]] | B | ANTXR1 activity raises CDK15's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 1.92× lower at baseline in the lines without ANTXR1 | 0.042 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[NREP]] | B | NREP activity raises CDK15's level | lines that do not express NREP (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without NREP | 0.062 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[DAPK1]] | B | DAPK1 activity lowers CDK15's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.51× higher at baseline in the lines without DAPK1 | 0.097 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[ITGA4]] | C | ITGA4 activity raises CDK15's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without ITGA4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[TGFBI]] | C | TGFBI activity raises CDK15's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 2.09× lower at baseline in the lines without TGFBI | 0.026 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[NTM]] | C | NTM activity raises CDK15's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without NTM | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[NRP2]] | C | NRP2 activity raises CDK15's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without NRP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[TNC]] | C | TNC activity raises CDK15's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without TNC | 0.050 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |
| [[TENM2]] | C | TENM2 activity raises CDK15's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 1.79× lower at baseline in the lines without TENM2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[HS3ST5]] | C | HS3ST5 activity raises CDK15's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.61× lower at baseline in the lines without HS3ST5 | 0.087 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 9, C 13. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFPM2]] | B | CDK15 activity raises ZFPM2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.56× lower at baseline in the lines without CDK15 | 0.032 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[PRRT2]] | B | CDK15 activity raises PRRT2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 1.40× lower at baseline in the lines without CDK15 | 0.034 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[HDAC2-AS2]] | B | CDK15 activity raises HDAC2-AS2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without CDK15 | 0.037 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[SYTL3]] | B | CDK15 activity strengthens SYTL3's drug response | lines that do not express CDK15 (21) vs lines expressing it (18) | the lines without CDK15 respond 0.60× as strongly (z diff +1.97); strongest at Harringtonine 0.5 µM: 0.74x vs 0.28x (z diff +4.2) | 0.046 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SYTL3]] | B | CDK15 activity raises SYTL3's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without CDK15 | 0.051 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[HEG1]] | B | CDK15 activity raises HEG1's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.82× lower at baseline in the lines without CDK15 | 0.056 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[GXYLT2]] | B | CDK15 activity raises GXYLT2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without CDK15 | 0.095 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[PTPN14]] | B | CDK15 activity raises PTPN14's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without CDK15 | 0.096 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[COLGALT2]] | B | CDK15 activity raises COLGALT2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 1.65× lower at baseline in the lines without CDK15 | 0.098 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[NTM]] | C | CDK15 activity raises NTM's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 3.88× lower at baseline in the lines without CDK15 | 0.006 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent; co-absent with the target |
| [[SPARC]] | C | CDK15 activity raises SPARC's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 7.70× lower at baseline in the lines without CDK15 | 0.032 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent; co-absent with the target |
| [[JAKMIP2-AS1]] | C | CDK15 activity raises JAKMIP2-AS1's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without CDK15 | 0.041 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.331). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.1, 40.8); signed map (63.8, 17.8). **Vector** length 41.1, 10.00% of its response variance represented; |z| ≥ 3 in 424 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +19.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | -0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +4.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | +0.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,790,461-201,895,550 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PFTAIRE2; previously ALS2CR7, PFTK2 |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q40](https://www.uniprot.org/uniprotkb/Q96Q40) (Cyclin-dependent kinase 15):

> Serine/threonine-protein kinase that acts like an antiapoptotic protein that counters TRAIL/TNFSF10-induced apoptosis by inducing phosphorylation of BIRC5 at 'Thr-34'.

**Summary**, from NCBI Gene [65061](https://www.ncbi.nlm.nih.gov/gene/65061):

> Enables protein serine/threonine kinase activity. Predicted to be involved in regulation of cell cycle phase transition. Predicted to be part of cyclin-dependent protein kinase holoenzyme complex. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14434) · Entrez [65061](https://www.ncbi.nlm.nih.gov/gene/65061) · UniProt [Q96Q40](https://www.uniprot.org/uniprotkb/Q96Q40) · Ensembl [ENSG00000138395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138395)

## Data

Gene col 6168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6168); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6168]; `tensor/DDL_lfc|DDL_z.npy` [6168]; `embed/gene_vectors.npy` [6168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6168 or target_col == 6168). Every well: [[CDK15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
