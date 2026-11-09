---
symbol: "NAALADL2-AS2"
type: "gene"
col: 13555
ensembl_id: "ENSG00000226779"
name: "NAALADL2 antisense RNA 2"
location: "3q26.3"
module: 9
arm: "+"
pooled_cpm: 4.01
n_lines_expressing: 14
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 11
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NAALADL2-AS2

*NAALADL2 antisense RNA 2* — 3q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 10.2× (z +19.5, q 0e+00, up in 10 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pexidartinib (hydrochloride) (drug)]] 5 µM: 0.504× (z -3.9, q 0.050, down in 1 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.141×, NCI-H2347 0.172×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.141×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.115×; ⚠ toxic; transcription drop); [[Ivermectin (drug)]] 0.5 µM in 1 line (SNU-423 0.0547×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENTHD1]] (+0.69, fdr 7e-06), [[C12orf50]] (+0.65, fdr 7e-06), [[ROR1-AS1]] (+0.62, fdr 1e-05); moves opposite to [[PHF12]] (-0.49, fdr 4e-05), [[GLT8D1]] (-0.47, fdr 3e-05), [[C2CD2L]] (-0.46, fdr 6e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC00944]] → it (grade B ⚠); 11 go from it, the strongest it → [[C12orf50]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **10.2×** | +19.5 | 0e+00 | 10/10 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.09×** | +10.3 | 2e-22 | 10/11 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.75×** | +7.8 | 1e-12 | 10/11 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.62×** | +7.6 | 4e-12 | 11/12 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +7.5 | 7e-12 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.34×** | +7.1 | 9e-11 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.17×** | +6.5 | 8e-09 | 10/12 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +6.4 | 1e-08 | 8/8 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.09×** | +6.2 | 4e-08 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.71×** | +5.9 | 2e-07 | 9/10 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.5 | 2e-06 | 4/11 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +4.8 | 6e-05 | 2/7 (A-172, SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +4.8 | 7e-05 | 8/11 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.96×** | +4.6 | 2e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +4.5 | 3e-04 | 4/7 (NCI-H1573, SHP-77, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.99×** | +4.0 | 0.002 | 9/12 (SW 900, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +3.6 | 0.008 | 7/11 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.83×** | +3.6 | 0.010 | 6/12 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.025 | 2/12 (C32, A-172) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.02×** | +3.0 | 0.080 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.081 | 1/12 (NCI-H2347) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.64×** | +2.9 | 0.081 | 0/9 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13555.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.141×, NCI-H2347 0.172×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.141×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.115×; ⚠ toxic; transcription drop); [[Ivermectin (drug)]] 0.5 µM in 1 line (SNU-423 0.0547×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.504×** | -3.9 | 0.050 | 1/11 (A-172) | rises with dose |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.533× | -3.5 | 0.15 | 0/12 | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.595× | -3.1 | 0.32 | 1/11 (A-427) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -3.0 | 0.32 | 1/12 (SNU-423) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 50.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -12.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 21.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +17.1) | — |
| [[A-172 (line)]] | wt | 4.27 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 136× (z +14.7) | — |
| [[SHP-77 (line)]] | alt | 52.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 9.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 6.26 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +10.3) | [[Ivermectin (drug)]] 0.5 µM 0.0547× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 1.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.9× (z +10.6) | — |
| [[A-427 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.351 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTHD1]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[C12orf50]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ROR1-AS1]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 | same gene group |
| [[SLC35F1]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[KCND2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MIR155HG]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[DISC1FP1]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[LINC01695]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SLAMF7]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[LINC02241]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[EBI3]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF12]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[GLT8D1]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[C2CD2L]] | -0.46 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[PPP6R1]] | -0.46 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[GNA11]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[BLTP2]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00944]] | B | LINC00944 activity raises NAALADL2-AS2's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.86× lower at baseline in the lines without LINC00944 | 0.080 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[CGNL1]] | B | CGNL1 activity raises NAALADL2-AS2's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without CGNL1 | 0.096 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[KCND2]] | C | KCND2 activity raises NAALADL2-AS2's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without KCND2 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent; co-absent with the target |
| [[SLAMF7]] | C | SLAMF7 activity raises NAALADL2-AS2's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without SLAMF7 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17; co-absent with the target |
| [[NGF]] | C | NGF activity raises NAALADL2-AS2's level | lines that do not express NGF (31) vs lines expressing it (19) | 2.65× lower at baseline in the lines without NGF | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises NAALADL2-AS2's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.50× lower at baseline in the lines without LINC01320 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | NAALADL2-AS2 activity raises C12orf50's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without NAALADL2-AS2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1 |
| [[LINC00882]] | B | NAALADL2-AS2 activity raises LINC00882's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 3.52× lower at baseline in the lines without NAALADL2-AS2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1 |
| [[GRIA4]] | B | NAALADL2-AS2 activity strengthens GRIA4's drug response | lines that do not express NAALADL2-AS2 (30) vs lines expressing it (12) | the lines without NAALADL2-AS2 respond 0.83× as strongly (z diff +0.52); strongest at Homoharringtonine 0.5 µM: 2.83x vs 9.94x (z diff +2.6) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; target measured in part of the lines; both ways; artifact flags |
| [[SLAMF7]] | C | NAALADL2-AS2 activity raises SLAMF7's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 3.57× lower at baseline in the lines without NAALADL2-AS2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[FSTL5]] | C | NAALADL2-AS2 activity raises FSTL5's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 4.55× lower at baseline in the lines without NAALADL2-AS2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[LINC01320]] | C | NAALADL2-AS2 activity raises LINC01320's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 4.48× lower at baseline in the lines without NAALADL2-AS2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[LINC01695]] | C | NAALADL2-AS2 activity raises LINC01695's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 3.06× lower at baseline in the lines without NAALADL2-AS2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[AMPH]] | C | NAALADL2-AS2 activity raises AMPH's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without NAALADL2-AS2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[LINC00504]] | C | NAALADL2-AS2 activity raises LINC00504's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 2.77× lower at baseline in the lines without NAALADL2-AS2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[PNLIPRP3]] | C | NAALADL2-AS2 activity raises PNLIPRP3's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 2.62× lower at baseline in the lines without NAALADL2-AS2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[THSD7A]] | C | NAALADL2-AS2 activity raises THSD7A's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 3.20× lower at baseline in the lines without NAALADL2-AS2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.8, 22.1); signed map (38.5, 22.0). **Vector** length 37.3, 11.2% of its response variance represented; |z| ≥ 3 in 311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +7.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | -0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +2.4 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.2 | +0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -3.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.7 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | NAALADL2 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q26.3 — chr3:175,234,861-175,271,096 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41015) · Entrez [100874244](https://www.ncbi.nlm.nih.gov/gene/100874244) · Ensembl [ENSG00000226779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226779)

## Data

Gene col 13555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13555); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13555]; `tensor/DDL_lfc|DDL_z.npy` [13555]; `embed/gene_vectors.npy` [13555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13555 or target_col == 13555). Every well: [[NAALADL2-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAALADL2-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
