---
symbol: "ODAD2"
type: "gene"
col: 9757
ensembl_id: "ENSG00000169126"
name: "outer dynein arm docking complex subunit 2"
location: "10p12.1"
module: 19
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 23
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 11
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ODAD2

*outer dynein arm docking complex subunit 2* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.33× (z +12.8, q 1e-34, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +12.4, q 1e-32, up in 3 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.513× (z -7.4, q 7e-11, down in 14 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF4]] (+0.62, fdr 1e-05), [[SLITRK5]] (+0.60, fdr 1e-05), [[SLC8A1]] (+0.58, fdr 3e-05); moves opposite to [[NPSR1-AS1]] (-0.50, fdr 1e-04), [[TMEM45B]] (-0.48, fdr 1e-04), [[HSD17B2]] (-0.47, fdr 4e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DAW1]] → it (grade C ⚠); 11 go from it, the strongest it → [[GLIS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +12.8 | 1e-34 | 2/7 (SNU-423, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +12.4 | 1e-32 | 3/16 (LS 180, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +9.9 | 5e-21 | 3/12 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +9.8 | 1e-20 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.008 | 5/19 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.8 | 0.011 | 3/16 (C-33 A, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.011 | 7/19 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.7 | 0.015 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.018 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.6 | 0.020 | 1/13 (HOP62) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +3.2 | 0.069 | 2/20 (C-33 A, NCI-H460) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.513×** | -7.4 | 7e-11 | 14/19 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.587×** | -5.7 | 4e-06 | 16/19 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -4.8 | 2e-04 | 15/19 (NCI-H1792, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.649×** | -4.8 | 2e-04 | 12/19 (NCI-H1792, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.752×** | -4.5 | 8e-04 | 15/18 (J82, SW 900, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -4.5 | 8e-04 | 8/19 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.686×** | -4.2 | 0.002 | 2/21 (SW 1271, SW 1088) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.706×** | -3.9 | 0.008 | 9/19 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.717×** | -3.7 | 0.014 | 12/19 (NCI-H1792, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.733×** | -3.4 | 0.032 | 12/17 (NCI-H1792, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.744×** | -3.3 | 0.053 | 9/18 (C-33 A, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.739×** | -3.1 | 0.091 | 1/19 (HOP62) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 47.5 | 0 | 12 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0608× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0775× (z -15.9) |
| [[A-172 (line)]] | wt | 90.6 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 27.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -12.1) |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.124× (z -10.6) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.147× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.57 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0712× (z -10.7) |
| [[J82 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -17.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.180× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 6.54 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0575× (z -10.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0714× (z -9.8) |
| [[SW 900 (line)]] | alt | 17.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -17.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 1 | — | [[Verteporfin (drug)]] 0.5 µM 0.0283× (z -10.9) |
| [[SNU-423 (line)]] | alt | 7.91 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0283× (z -14.1) |
| [[A498 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.715 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF4]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SLITRK5]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SLC8A1]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PAPPA]] | +0.57 | +0.58 / +0.35 | both halves | 1e-04 | **novel candidate** |
| [[ZFHX4]] | +0.56 | +0.32 / +0.56 | both halves | 1e-04 |  |
| [[TENM2]] | +0.56 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[FAT4]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 | **novel candidate** |
| [[STEAP1B-AS1]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[BASP1-AS1]] | +0.54 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[KCTD16]] | +0.54 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[SPANXA2-OT1]] | +0.54 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[MIR3171HG]] | +0.53 | +0.48 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1-AS1]] | -0.50 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[TMEM45B]] | -0.48 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[HSD17B2]] | -0.47 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[SDCBP2]] | -0.45 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[PTK6]] | -0.45 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[TMEM125]] | -0.45 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[USH1C]] | -0.44 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[TMBIM1]] | -0.44 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[ABO]] | -0.44 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[GCNT3]] | -0.43 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[C1orf116]] | -0.43 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[PCDH1]] | -0.43 | -0.41 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAW1]] | C | DAW1 activity raises ODAD2's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without DAW1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIS3]] | B | ODAD2 activity raises GLIS3's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without ODAD2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5 |
| [[RFTN1]] | B | ODAD2 activity raises RFTN1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without ODAD2 | 0.088 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5 |
| [[SLC8A1]] | C | ODAD2 activity raises SLC8A1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 3.38× lower at baseline in the lines without ODAD2 | 0.015 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[NDNF]] | C | ODAD2 activity raises NDNF's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 3.03× lower at baseline in the lines without ODAD2 | 0.016 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[STEAP1B-AS1]] | C | ODAD2 activity raises STEAP1B-AS1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without ODAD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[DNAH11]] | C | ODAD2 activity raises DNAH11's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 3.51× lower at baseline in the lines without ODAD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[BASP1-AS1]] | C | ODAD2 activity raises BASP1-AS1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without ODAD2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[NEGR1]] | C | ODAD2 activity raises NEGR1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.50× lower at baseline in the lines without ODAD2 | 0.043 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[FAT4]] | C | ODAD2 activity raises FAT4's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 3.12× lower at baseline in the lines without ODAD2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[ADAMTS12]] | C | ODAD2 activity raises ADAMTS12's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.45× lower at baseline in the lines without ODAD2 | 0.075 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[LINC01684]] | C | ODAD2 activity raises LINC01684's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without ODAD2 | 0.084 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.8, 21.5); signed map (37.3, 41.5). **Vector** length 44.5, 9.69% of its response variance represented; |z| ≥ 3 in 522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | -0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | +2.6 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | outer dynein arm docking complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:27,775,186-27,999,079 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10817, FLJ10376, DKFZP434P1735, CILD23, gudu; previously ARMC4 |
| Gene groups (HGNC) | Armadillo repeat containing; Outer dynein arm docking complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T2S8](https://www.uniprot.org/uniprotkb/Q5T2S8) (Outer dynein arm-docking complex subunit 2):

> Component of the outer dynein arm-docking complex (ODA-DC) that mediates outer dynein arms (ODA) binding onto the doublet microtubule. Involved in mediating assembly of both ODAs and their axonemal docking complex onto ciliary microtubules.

**Summary**, from NCBI Gene [55130](https://www.ncbi.nlm.nih.gov/gene/55130):

> The protein encoded by this gene contains ten Armadillo repeat motifs (ARMs) and one HEAT repeat, and is thought to be involved in ciliary and flagellar movement. This protein has been shown to localize to the ciliary axonemes and at the ciliary base of respiratory cells. Studies indicate that mutations in this gene cause partial outer dynein arm (ODA) defects in respiratory cilia. The cilia of cells with mutations in this gene displayed either reduced ciliary beat frequency and amplitude, or, …

**Accessions** — [HGNC:25583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25583) · Entrez [55130](https://www.ncbi.nlm.nih.gov/gene/55130) · UniProt [Q5T2S8](https://www.uniprot.org/uniprotkb/Q5T2S8) · Ensembl [ENSG00000169126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169126)

## Data

Gene col 9757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9757); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9757]; `tensor/DDL_lfc|DDL_z.npy` [9757]; `embed/gene_vectors.npy` [9757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9757 or target_col == 9757). Every well: [[ODAD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ODAD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
