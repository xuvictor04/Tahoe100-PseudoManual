---
symbol: "STAT5A"
type: "gene"
col: 4744
ensembl_id: "ENSG00000126561"
name: "signal transducer and activator of transcription 5A"
location: "17q21.2"
module: 14
arm: "+"
pooled_cpm: 7.56
n_lines_expressing: 38
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 31
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# STAT5A

*signal transducer and activator of transcription 5A* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.99× (z +39.0, q 0e+00, up in 33 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.352× (z -12.5, q 6e-33, down in 27 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP2]] (+0.83, fdr 7e-06), [[TAPBPL]] (+0.76, fdr 7e-06), [[STAP2]] (+0.76, fdr 7e-06); moves opposite to [[CAP1]] (-0.63, fdr 2e-05), [[RNGTT]] (-0.60, fdr 3e-05), [[ABTB3]] (-0.59, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TNFAIP2]] → it (grade B ⚠); 31 go from it, the strongest it → [[TNFAIP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.99×** | +39.0 | 0e+00 | 33/35 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **13.4×** | +29.9 | 0e+00 | 32/35 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.76×** | +18.7 | 0e+00 | 23/35 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.28×** | +14.2 | 7e-44 | 22/35 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +7.3 | 5e-11 | 19/34 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.7 | 1e-06 | 16/32 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +4.9 | 7e-05 | 16/35 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.35×** | +3.6 | 0.020 | 11/31 (J82, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.090 | 10/35 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.28× | +3.1 | 0.10 | 7/36 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +3.1 | 0.10 | 2/35 (NCI-H1792, AsPC-1) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.0 | 0.11 | 12/34 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 1.31× | +3.0 | 0.11 | 5/32 (C32, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.352×** | -12.5 | 6e-33 | 27/35 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.363×** | -12.1 | 2e-31 | 30/35 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.398×** | -11.0 | 7e-26 | 28/35 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.526×** | -7.7 | 2e-12 | 27/35 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.546×** | -7.2 | 6e-11 | 26/32 (SW1417, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.589×** | -6.3 | 2e-08 | 21/35 (NCI-H1573, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.630×** | -5.5 | 3e-06 | 16/35 (SW48, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -4.6 | 3e-04 | 12/35 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.537×** | -3.9 | 0.006 | 13/34 (SHP-77, SW 900, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.560×** | -3.6 | 0.017 | 9/36 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.571×** | -3.5 | 0.024 | 8/34 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.761×** | -3.1 | 0.100 | 7/35 (SHP-77, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.777× | -3.0 | 0.11 | 3/35 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.8 | 3 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 5.88× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 15.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +17.4) | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +25.7) | — |
| [[NCI-H460 (line)]] | wt | 7.65 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 15.1 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +25.2) | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -8.9) |
| [[RKO (line)]] | wt | 14.7 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.0951× (z -11.9) |
| [[A-172 (line)]] | wt | 7.25 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.5× (z +18.9) | — |
| [[A549 (line)]] | wt | 11.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +18.8) | — |
| [[HOP62 (line)]] | alt | 7.93 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +23.6) | — |
| [[HS-578T (line)]] | alt | 14.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +18.2) | — |
| [[SW1417 (line)]] | alt | 9.20 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0931× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 5.69 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.9× (z +13.5) | — |
| [[J82 (line)]] | alt | 6.44 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.6× (z +19.8) | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 8.14 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 30.1× (z +12.2) | [[Belinostat (drug)]] 0.5 µM 0.0704× (z -9.9) |
| [[SNU-423 (line)]] | alt | 6.45 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 37.0× (z +18.2) | [[Entrectinib (drug)]] 5 µM 0.0452× (z -11.1) |
| [[SW 900 (line)]] | alt | 8.38 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +15.0) | — |
| [[CFPAC-1 (line)]] | alt | 6.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 66.7× (z +21.6) | — |
| [[HepG2_C3A (line)]] | wt | 5.07 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.0453× (z -9.2) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 13.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +20.0) | — |
| [[SK-MEL-2 (line)]] | alt | 9.17 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +15.4) | — |
| [[SW48 (line)]] | wt | 4.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.2× (z +11.4) | — |
| [[SW480 (line)]] | alt | 4.58 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0861× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 7.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 3.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 9.47 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0822× (z -9.5) |
| [[HCT15 (line)]] | alt | 5.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.21× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.96 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 13.3× (z +10.6) | — |
| [[A-427 (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.942 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.817 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP2]] | +0.83 | +0.84 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TAPBPL]] | +0.76 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[STAP2]] | +0.76 | +0.68 / +0.70 | both halves | 7e-06 | STRING 647 |
| [[ANO9]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[CX3CL1]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CSF1]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 458 |
| [[BCL3]] | +0.70 | +0.67 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 411 |
| [[SLC12A7]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[DENND2B]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[LINC02605]] | +0.67 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[FAM111A-DT]] | +0.67 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[DRAM1]] | +0.66 | +0.64 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAP1]] | -0.63 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[RNGTT]] | -0.60 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ABTB3]] | -0.59 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[AP1S1]] | -0.59 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.58 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[STRAP]] | -0.58 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFAIP2]] | B | TNFAIP2 activity raises STAT5A's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without TNFAIP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[NINJ1]] | B | NINJ1 activity raises STAT5A's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without NINJ1 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[RHBDL2]] | B | RHBDL2 activity raises STAT5A's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without RHBDL2 | 0.064 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[IL32]] | B | IL32 activity raises STAT5A's level | lines that do not express IL32 (18) vs lines expressing it (32) | 1.90× lower at baseline in the lines without IL32 | 0.066 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[ABCG2]] | B | ABCG2 activity raises STAT5A's level | lines that do not express ABCG2 (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without ABCG2 | 0.088 | ⚠ within organs, on part of the lines; also absent: C1R, GBP4, CDK18; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises STAT5A's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without ELF3-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[NOD2]] | C | NOD2 activity raises STAT5A's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without NOD2 | 0.006 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2; co-absent with the target |
| [[LGALS3]] | C | LGALS3 activity raises STAT5A's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 3.04× lower at baseline in the lines without LGALS3 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1; co-absent with the target |
| [[ETS2]] | C | ETS2 activity raises STAT5A's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without ETS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 27, C 4. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFAIP2]] | B | STAT5A activity raises TNFAIP2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.38× lower at baseline in the lines without STAT5A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[PBX2]] | B | STAT5A activity lowers PBX2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.55× higher at baseline in the lines without STAT5A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[AJUBA]] | B | STAT5A activity lowers AJUBA's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.64× higher at baseline in the lines without STAT5A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[ELF3-AS1]] | B | STAT5A activity raises ELF3-AS1's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.39× lower at baseline in the lines without STAT5A | 0.015 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[FOXJ2]] | B | STAT5A activity lowers FOXJ2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.70× higher at baseline in the lines without STAT5A | 0.017 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[ANO9]] | B | STAT5A activity raises ANO9's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 3.01× lower at baseline in the lines without STAT5A | 0.020 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[BCL3]] | B | STAT5A activity raises BCL3's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without STAT5A | 0.022 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[RASSF5]] | B | STAT5A activity raises RASSF5's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without STAT5A | 0.025 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[STAP2]] | B | STAT5A activity raises STAP2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.67× lower at baseline in the lines without STAT5A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[TNFRSF14]] | B | STAT5A activity raises TNFRSF14's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 3.02× lower at baseline in the lines without STAT5A | 0.036 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[STRAP]] | B | STAT5A activity lowers STRAP's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.35× higher at baseline in the lines without STAT5A | 0.038 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[SOD2]] | B | STAT5A activity raises SOD2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.73× lower at baseline in the lines without STAT5A | 0.040 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 4.7); signed map (44.0, 7.2). **Vector** length 95.7, 23.4% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.54 to 12); *inflammatory response* (hallmark, mean cos +0.50 to 22); *Chemokine receptors bind chemokines* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +39.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +29.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +18.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +14.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -12.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | signal transducer and activator of transcription 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,287,547-42,311,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGF; previously STAT5 |
| Gene groups (HGNC) | SH2 domain containing; Signal transducer and activator of transcription family |
| Hallmark sets | ADIPOGENESIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 41 pathways, smallest: Erythropoietin activates STAT5; STAT5 Activation; Interleukin-9 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P42229](https://www.uniprot.org/uniprotkb/P42229) (Signal transducer and activator of transcription 5A):

> Carries out a dual function: signal transduction and activation of transcription. Mediates cellular responses to the cytokine KITLG/SCF and other growth factors. Mediates cellular responses to ERBB4. May mediate cellular responses to activated FGFR1, FGFR2, FGFR3 and FGFR4. Binds to the GAS element and activates PRL-induced transcription. Regulates the expression of milk proteins during lactation.

**Summary**, from NCBI Gene [6776](https://www.ncbi.nlm.nih.gov/gene/6776):

> The protein encoded by this gene is a member of the STAT family of transcription factors. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. This protein is activated by, and mediates the responses of many cell ligands, such as IL2, IL3, IL7 GM-CSF, erythropoietin, thrombopoietin, and different growth hormones. …

**Accessions** — [HGNC:11366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11366) · Entrez [6776](https://www.ncbi.nlm.nih.gov/gene/6776) · UniProt [P42229](https://www.uniprot.org/uniprotkb/P42229) · Ensembl [ENSG00000126561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126561)

## Data

Gene col 4744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4744); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4744]; `tensor/DDL_lfc|DDL_z.npy` [4744]; `embed/gene_vectors.npy` [4744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4744 or target_col == 4744). Every well: [[STAT5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAT5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
