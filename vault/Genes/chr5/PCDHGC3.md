---
symbol: "PCDHGC3"
type: "gene"
col: 14227
ensembl_id: "ENSG00000240184"
name: "protocadherin gamma subfamily C, 3"
location: "5q31.3"
module: 20
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 32
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 19
direction_downstream: 6
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PCDHGC3

*protocadherin gamma subfamily C, 3* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.70× (z +6.0, q 1e-06, up in 5 of 9 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.239× (z -12.7, q 4e-34, down in 25 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP2M1]] (+0.65, fdr 7e-06), [[TGOLN2]] (+0.64, fdr 7e-06), [[DKK3]] (+0.63, fdr 7e-06); moves opposite to [[SNHG8]] (-0.61, fdr 9e-06), [[EPB41L4A-AS1]] (-0.57, fdr 1e-05), [[SNHG32]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[HHIP]] → it (grade B ⚠); 6 go from it, the strongest it → [[PCDHGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +6.0 | 1e-06 | 5/9 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +5.2 | 6e-05 | 7/12 (RPMI-7951, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +4.4 | 0.002 | 7/16 (SNU-423, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.239×** | -12.7 | 4e-34 | 25/26 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.287×** | -7.5 | 2e-11 | 25/28 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.320×** | -7.1 | 2e-10 | 23/25 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -5.5 | 5e-06 | 20/26 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.458×** | -4.6 | 5e-04 | 16/29 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.500×** | -4.2 | 0.003 | 16/27 (Hs 766T, SNU-423, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.511×** | -3.9 | 0.008 | 16/29 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.650×** | -3.8 | 0.009 | 14/29 (HS-578T, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -3.8 | 0.009 | 15/23 (Panc 03.27, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.572×** | -3.3 | 0.054 | 13/26 (C32, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.708× | -3.1 | 0.12 | 13/29 (RPMI-7951, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0819× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 19.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0629× (z -14.9) |
| [[PANC-1 (line)]] | alt | 3.29 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -11.1) |
| [[A498 (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.5) |
| [[C32 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -11.3) |
| [[HOP62 (line)]] | alt | 8.03 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -11.2) |
| [[Hs 766T (line)]] | wt | 8.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0556× (z -14.3) |
| [[HS-578T (line)]] | alt | 5.51 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0528× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0143× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 4.55 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0513× (z -9.0) |
| [[SNU-423 (line)]] | alt | 5.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -9.4) |
| [[A-427 (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.819 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.283 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2M1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TGOLN2]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[DKK3]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SFRP1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TMEM30A]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[GTF3C1]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SCUBE3]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[FZD1]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[F2R]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MMP14]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[COL15A1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[BPNT2]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG8]] | -0.61 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[EPB41L4A-AS1]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.57 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[FOXO3]] | -0.55 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ATF4]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SNHG12]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.55 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TRPM7]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PDCD5]] | -0.53 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[ZFAS1]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[NACA4P]] ⚠ | -0.52 | -0.40 / -0.60 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CEP164P1]] | -0.52 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[RPAIN]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 7, C 12. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HHIP]] | B | HHIP activity raises PCDHGC3's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without HHIP | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[COL13A1]] | B | COL13A1 activity raises PCDHGC3's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.92× lower at baseline in the lines without COL13A1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[ARHGDIB]] | B | ARHGDIB activity raises PCDHGC3's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without ARHGDIB | 0.036 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[FBN1]] | B | FBN1 activity raises PCDHGC3's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without FBN1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[HTRA1]] | B | HTRA1 activity raises PCDHGC3's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without HTRA1 | 0.070 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[SDC2]] | B | SDC2 activity raises PCDHGC3's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without SDC2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[COL15A1]] | B | COL15A1 activity raises PCDHGC3's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.49× lower at baseline in the lines without COL15A1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[ITGA11]] | C | ITGA11 activity raises PCDHGC3's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without ITGA11 | 0.004 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises PCDHGC3's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.11× lower at baseline in the lines without COL5A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises PCDHGC3's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 3.76× lower at baseline in the lines without ITGA4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[PXDN]] | C | PXDN activity raises PCDHGC3's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without PXDN | 0.019 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises PCDHGC3's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.98× lower at baseline in the lines without INSYN2B | 0.031 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHGA2]] | B | PCDHGC3 activity raises PCDHGA2's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 3.55× lower at baseline in the lines without PCDHGC3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P |
| [[TRIB2]] | B | PCDHGC3 activity raises TRIB2's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 3.36× lower at baseline in the lines without PCDHGC3 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P |
| [[COL13A1]] | B | PCDHGC3 activity raises COL13A1's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 3.60× lower at baseline in the lines without PCDHGC3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P |
| [[FZD1]] | B | PCDHGC3 activity raises FZD1's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 1.70× lower at baseline in the lines without PCDHGC3 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P |
| [[DPYSL3]] | C | PCDHGC3 activity raises DPYSL3's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 5.54× lower at baseline in the lines without PCDHGC3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P; co-absent with the target |
| [[ANTXR1]] | C | PCDHGC3 activity raises ANTXR1's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 4.76× lower at baseline in the lines without PCDHGC3 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P; co-absent with the target |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (55.2, 19.3); signed map (23.5, 43.0). **Vector** length 64.6, 15.1% of its response variance represented; |z| ≥ 3 in 699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.8 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.2 | +1.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.1 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin gamma subfamily C, 3 |
| Locus type | complex locus constituent (other) |
| Location | 5q31.3 — chr5:141,475,947-141,512,977 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC-43, PC43, PCDH-GAMMA-C3; previously PCDH2 |
| Gene groups (HGNC) | Clustered protocadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN70](https://www.uniprot.org/uniprotkb/Q9UN70) (Protocadherin gamma-C3):

> Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain.

**Summary**, from NCBI Gene [5098](https://www.ncbi.nlm.nih.gov/gene/5098):

> This gene is a member of the protocadherin gamma gene cluster, one of three related clusters tandemly linked on chromosome five. These gene clusters have an immunoglobulin-like organization, suggesting that a novel mechanism may be involved in their regulation and expression. The gamma gene cluster includes 22 genes divided into 3 subfamilies. Subfamily A contains 12 genes, subfamily B contains 7 genes and 2 pseudogenes, and the more distantly related subfamily C contains 3 genes. The tandem …

**Accessions** — [HGNC:8716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8716) · Entrez [5098](https://www.ncbi.nlm.nih.gov/gene/5098) · UniProt [Q9UN70](https://www.uniprot.org/uniprotkb/Q9UN70) · Ensembl [ENSG00000240184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240184)

## Data

Gene col 14227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14227); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14227]; `tensor/DDL_lfc|DDL_z.npy` [14227]; `embed/gene_vectors.npy` [14227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14227 or target_col == 14227). Every well: [[PCDHGC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDHGC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
