---
symbol: "SHROOM4"
type: "gene"
col: 8154
ensembl_id: "ENSG00000158352"
name: "shroom family member 4"
location: "Xp11.22"
module: 87
arm: "+"
pooled_cpm: 13.46
n_lines_expressing: 20
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 21
direction_downstream: 33
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# SHROOM4

*shroom family member 4* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.62× (z +15.6, q 0e+00, up in 1 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +6.8, q 1e-09, up in 0 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.483× (z -8.8, q 7e-16, down in 17 of 17 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP9P1-1]] (+0.64, fdr 7e-06), [[LOXL4]] (+0.62, fdr 2e-05), [[LEF1-AS1]] (+0.62, fdr 1e-05); moves opposite to [[ZNF433]] (-0.42, fdr 1e-04), [[DCLK2]] (-0.39, fdr 5e-05), [[ZNF844]] (-0.36, fdr 2e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[LEMD1]] → it (grade B ⚠); 33 go from it, the strongest it → [[CYP27A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +15.6 | 0e+00 | 1/16 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +13.7 | 5e-40 | 3/13 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +8.0 | 3e-13 | 1/14 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.8 | 1e-09 | 0/18 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.4 | 0.073 | 1/16 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.483×** | -8.8 | 7e-16 | 17/17 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -7.6 | 7e-12 | 16/17 (C32, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -6.9 | 1e-09 | 14/17 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.557×** | -6.6 | 4e-09 | 14/17 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -6.6 | 4e-09 | 15/17 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.624×** | -5.7 | 1e-06 | 14/17 (HepG2/C3A, HT-29, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -5.4 | 5e-06 | 14/17 (H4, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -5.0 | 5e-05 | 16/17 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -4.6 | 3e-04 | 10/17 (C32, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -4.4 | 6e-04 | 7/17 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.720×** | -4.0 | 0.003 | 7/17 (C32, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.731×** | -3.8 | 0.007 | 9/17 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.766×** | -3.2 | 0.053 | 12/17 (SW480, PANC-1, …) | rises with dose |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.770×** | -3.2 | 0.062 | 1/17 (CFPAC-1) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.1 | 0.075 | 9/18 (C32, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.604×** | -3.0 | 0.092 | 3/17 (SK-MEL-2, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 199 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0650× (z -22.0) |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.4) |
| [[SW1417 (line)]] | alt | 98.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -16.6) |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -15.3) |
| [[HT-29 (line)]] | alt | 84.6 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -16.8) |
| [[SW480 (line)]] | alt | 10.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -14.9) |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0156× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -11.1) |
| [[H4 (line)]] | wt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0933× (z -13.4) |
| [[A-172 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP9P1-1]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[LOXL4]] | +0.62 | +0.47 / +0.65 | both halves | 2e-05 | **novel candidate** |
| [[LEF1-AS1]] | +0.62 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[PTPRZ1]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[C10orf90]] | +0.58 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[TRPV4]] | +0.55 | +0.56 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[TMEM51-AS1]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[LEF1]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[MIR3681HG]] | +0.52 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SAMMSON]] | +0.51 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[LINC01239]] | +0.51 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SOX10]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF433]] | -0.42 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[DCLK2]] | -0.39 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[ZNF844]] | -0.36 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[UST]] | -0.35 | -0.36 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 4, C 17. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEMD1]] | B | LEMD1 activity raises SHROOM4's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.85× lower at baseline in the lines without LEMD1 | 0.005 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[BLACAT1]] | B | BLACAT1 activity raises SHROOM4's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.67× lower at baseline in the lines without BLACAT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[LAMA3]] | B | LAMA3 activity raises SHROOM4's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.95× lower at baseline in the lines without LAMA3 | 0.069 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[MYO5B]] | B | MYO5B activity raises SHROOM4's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without MYO5B | 0.094 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[MILR1]] | C | MILR1 activity raises SHROOM4's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 3.26× lower at baseline in the lines without MILR1 | 0.003 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |
| [[SNTB1]] | C | SNTB1 activity raises SHROOM4's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 3.10× lower at baseline in the lines without SNTB1 | 0.005 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises SHROOM4's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 4.61× lower at baseline in the lines without GJB1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises SHROOM4's level | lines that do not express GABRP (44) vs lines expressing it (6) | 3.72× lower at baseline in the lines without GABRP | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[TRPV4]] | C | TRPV4 activity raises SHROOM4's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without TRPV4 | 0.016 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent; co-absent with the target |
| [[CRYBG1]] | C | CRYBG1 activity raises SHROOM4's level | lines that do not express CRYBG1 (18) vs lines expressing it (32) | 2.86× lower at baseline in the lines without CRYBG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1; co-absent with the target |
| [[CARD11]] | C | CARD11 activity raises SHROOM4's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.21× lower at baseline in the lines without CARD11 | 0.034 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[LAPTM5]] | C | LAPTM5 activity raises SHROOM4's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.67× lower at baseline in the lines without LAPTM5 | 0.039 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 13, C 20. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP27A1]] | B | SHROOM4 activity raises CYP27A1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.81× lower at baseline in the lines without SHROOM4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[CYP27A1]] | B | SHROOM4 activity strengthens CYP27A1's drug response | lines that do not express SHROOM4 (21) vs lines expressing it (17) | the lines without SHROOM4 respond 0.47× as strongly (z diff +1.74); strongest at Homoharringtonine 5 µM: 0.93x vs 0.51x (z diff +4.8) | 0.011 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; target measured in part of the lines; artifact flags |
| [[TGFA]] | B | SHROOM4 activity raises TGFA's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.66× lower at baseline in the lines without SHROOM4 | 0.016 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[CCNJL]] | B | SHROOM4 activity raises CCNJL's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without SHROOM4 | 0.036 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[LASTR]] | B | SHROOM4 activity raises LASTR's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without SHROOM4 | 0.051 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[LINC01239]] | B | SHROOM4 activity raises LINC01239's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without SHROOM4 | 0.065 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[TNC]] | B | SHROOM4 activity raises TNC's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 3.88× lower at baseline in the lines without SHROOM4 | 0.069 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[LEMD1]] | B | SHROOM4 activity raises LEMD1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.87× lower at baseline in the lines without SHROOM4 | 0.080 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[BLACAT1]] | B | SHROOM4 activity raises BLACAT1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without SHROOM4 | 0.092 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[RNF128]] | B | SHROOM4 activity raises RNF128's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without SHROOM4 | 0.093 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[FMN1]] | B | SHROOM4 activity raises FMN1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without SHROOM4 | 0.097 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[ADAM19]] | B | SHROOM4 activity raises ADAM19's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.40× lower at baseline in the lines without SHROOM4 | 0.098 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.8, 29.7); signed map (28.7, 37.8). **Vector** length 64.4, 21.2% of its response variance represented; |z| ≥ 3 in 494 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.9 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -1.6 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -0.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | shroom family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:50,586,796-50,814,302 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1202, Shrm4, SHAP |
| Gene groups (HGNC) | PDZ domain containing; Shroom family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULL8](https://www.uniprot.org/uniprotkb/Q9ULL8) (Protein Shroom4):

> Probable regulator of cytoskeletal architecture that plays an important role in development. May regulate cellular and cytoskeletal architecture by modulating the spatial distribution of myosin II (By similarity).

**Summary**, from NCBI Gene [57477](https://www.ncbi.nlm.nih.gov/gene/57477):

> This gene encodes a member of the APX/Shroom family, which contain an N-terminal PDZ domain and a C-terminal ASD2 motif. The encoded protein may play a role in cytoskeletal architecture. Mutations in this gene have been linked to the X-linked Stocco dos Santos syndrome characterized by cognitive disabilities. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:29215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29215) · Entrez [57477](https://www.ncbi.nlm.nih.gov/gene/57477) · UniProt [Q9ULL8](https://www.uniprot.org/uniprotkb/Q9ULL8) · Ensembl [ENSG00000158352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158352)

## Data

Gene col 8154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8154); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8154]; `tensor/DDL_lfc|DDL_z.npy` [8154]; `embed/gene_vectors.npy` [8154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8154 or target_col == 8154). Every well: [[SHROOM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHROOM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
