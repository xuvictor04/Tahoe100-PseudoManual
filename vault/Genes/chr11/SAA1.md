---
symbol: "SAA1"
type: "gene"
col: 10383
ensembl_id: "ENSG00000173432"
name: "serum amyloid A1"
location: "11p15.1"
module: 139
arm: "+"
pooled_cpm: 15.01
n_lines_expressing: 23
n_dd_up: 42
n_dd_down: 3
n_dd_up_clean: 36
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 12
direction_downstream: 16
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SAA1

*serum amyloid A1* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 6.13× (z +11.6, q 2e-28, up in 19 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.523× (z -4.2, q 0.016, down in 16 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A498 0.0976×, SNU-423 0.0768×, SW 900 0.0907×, NCI-H2347 0.167×); [[Auranofin (drug)]] 5 µM in 3 lines (COLO 205 0.0498×, A498 0.0478×, SNU-423 0.0366×); [[Selinexor (drug)]] 5 µM in 2 lines (SW 900 0.0890×, COLO 205 0.130×; ⚠ cell-cycle shift, explains ~37% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (SW 900 0.0316×, A498 0.0623×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAA2]] (+0.94, fdr 7e-06, ⚠ same locus), [[SAA4]] (+0.92, fdr 7e-06, ⚠ same locus), [[SAA2-SAA4]] (+0.92, fdr 7e-06, ⚠ same locus), [[IRAK3]] (+0.72, fdr 1e-05), [[SLPI]] (+0.71, fdr 7e-06), [[NNMT]] (+0.70, fdr 7e-06); moves opposite to [[PTHLH]] (-0.56, fdr 2e-05), [[PLAU]] (-0.49, fdr 4e-05), [[DCBLD2]] (-0.47, fdr 5e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SH3TC1]] → it (grade B ⚠); 16 go from it, the strongest it → [[CCND3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 6 with an alert ⚠; shown: the 15 strongest. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **6.13×** | +11.6 | 2e-28 | 19/20 (J82, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **9.70×** | +10.3 | 2e-22 | 16/19 (A-172, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **7.83×** | +9.3 | 2e-18 | 15/19 (SNU-423, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **4.09×** | +9.0 | 3e-17 | 16/19 (A549, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **7.06×** | +8.8 | 1e-16 | 15/19 (A-172, A549, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **6.84×** | +8.7 | 3e-16 | 14/20 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.70×** | +8.6 | 6e-16 | 14/19 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **6.32×** | +8.3 | 5e-15 | 16/19 (A-172, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **5.90×** | +7.7 | 7e-13 | 16/19 (A-172, A549, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **5.40×** | +7.6 | 1e-12 | 14/19 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **5.27×** | +7.5 | 3e-12 | 15/19 (A-172, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **5.26×** | +7.5 | 3e-12 | 16/19 (A-172, A549, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **5.25×** | +7.5 | 3e-12 | 19/19 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **4.73×** | +7.0 | 8e-11 | 15/19 (A-172, SNU-423, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **4.73×** | +7.0 | 8e-11 | 15/19 (A549, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10383.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A498 0.0976×, SNU-423 0.0768×, SW 900 0.0907×, NCI-H2347 0.167×); [[Auranofin (drug)]] 5 µM in 3 lines (COLO 205 0.0498×, A498 0.0478×, SNU-423 0.0366×); [[Selinexor (drug)]] 5 µM in 2 lines (SW 900 0.0890×, COLO 205 0.130×; ⚠ cell-cycle shift, explains ~37% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (SW 900 0.0316×, A498 0.0623×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.523×** | -4.2 | 0.016 | 16/19 (COLO 205, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.415×** | -4.0 | 0.016 | 14/19 (COLO 205, A-172, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.420×** | -3.9 | 0.016 | 15/19 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.501× | -3.1 | 0.24 | 13/20 (NCI-H2030, COLO 205, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.75 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.3 | 13 | 0 | [[Tucidinostat (drug)]] 5 µM 16.1× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 82.7 | 1 | 12 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.00× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.0498× (z -11.3) |
| [[SNU-423 (line)]] | alt | 47.6 | 6 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 10.9× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.0768× (z -11.8) |
| [[J82 (line)]] | alt | 45.0 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 23.1× (z +15.8) | — |
| [[A498 (line)]] | wt | 122 | 2 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 12.5× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -11.9) |
| [[A549 (line)]] | wt | 12.3 | 6 | 0 | [[Triamcinolone (drug)]] 5 µM 18.2× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 36.9 | 1 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 9.37× (z +10.9) | [[Selinexor (drug)]] 5 µM 0.0890× (z -11.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 15.2 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 7.23× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 17.3 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 8.03× (z +9.0) | — |
| [[H4 (line)]] | wt | 12.0 | 2 | 0 | [[Triamcinolone (drug)]] 5 µM 28.2× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0361× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 55.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.01× (z +9.2) | — |
| [[A-427 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.945 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAA2]] | +0.94 | +0.94 / +0.94 | both halves | 7e-06 | STRING 975; ⚠ same locus (17.6 kb: neighbours can correlate without regulation) |
| [[SAA4]] | +0.92 | +0.92 / +0.93 | both halves | 7e-06 | STRING 762; ⚠ same locus (29.5 kb: neighbours can correlate without regulation) |
| [[SAA2-SAA4]] | +0.92 | +0.92 / +0.93 | both halves | 7e-06 | STRING 803; ⚠ same locus (17.6 kb: neighbours can correlate without regulation) |
| [[IRAK3]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 | pathway: Interleukin-1 family signaling |
| [[SLPI]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[NNMT]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[MT1X]] | +0.70 | +0.57 / +0.79 | both halves | 9e-06 |  |
| [[ZMYND8]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TLR2]] | +0.69 | +0.56 / +0.69 | both halves | 1e-05 | pathway: MyD88:MAL(TIRAP) cascade initiated on plasma membrane; STRING 630 |
| [[MT1E]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[MT1A]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[CCND3]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[MT1M]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ID1]] | +0.65 | +0.58 / +0.68 | both halves | 8e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTHLH]] | -0.56 | -0.65 / -0.48 | both halves | 2e-05 | same gene group; pathway: GPCR ligand binding |
| [[PLAU]] | -0.49 | -0.57 / -0.43 | both halves | 4e-05 |  |
| [[DCBLD2]] | -0.47 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[SHISAL1]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3TC1]] | B | SH3TC1 activity raises SAA1's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 3.22× lower at baseline in the lines without SH3TC1 | 0.080 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[CCL20]] | B | CCL20 activity raises SAA1's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.54× lower at baseline in the lines without CCL20 | 0.086 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[EPAS1]] | B | EPAS1 activity raises SAA1's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 3.68× lower at baseline in the lines without EPAS1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[NR3C1]] | B | NR3C1 activity raises SAA1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.3% of all compounds | 0.099 | ⚠ off-target possible; 3 compounds |
| [[SAA2-SAA4]], [[SAA4]] | C | SAA2-SAA4, SAA4 activity raises SAA1's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 5.05× lower at baseline in the lines without SAA2-SAA4, SAA4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent with the target; co-absent genes |
| [[SAA2]] | C | SAA2 activity raises SAA1's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 4.89× lower at baseline in the lines without SAA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3; co-absent with the target |
| [[TNFSF14]] | C | TNFSF14 activity raises SAA1's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 4.71× lower at baseline in the lines without TNFSF14 | 0.001 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent; co-absent with the target |
| [[C3]] | C | C3 activity raises SAA1's level | lines that do not express C3 (32) vs lines expressing it (18) | 4.04× lower at baseline in the lines without C3 | 0.008 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises SAA1's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.48× lower at baseline in the lines without SERPINA5 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[PLAU]] | C | PLAU activity raises SAA1's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without PLAU | 0.042 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3; co-absent with the target |
| [[AGT]] | C | AGT activity raises SAA1's level | lines that do not express AGT (33) vs lines expressing it (17) | 3.08× lower at baseline in the lines without AGT | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[HLA-DRB1]] | C | HLA-DRB1 activity raises SAA1's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.97× lower at baseline in the lines without HLA-DRB1 | 0.060 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 8, C 8. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCND3]] | B | SAA1 activity raises CCND3's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.58× lower at baseline in the lines without SAA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[ZFAND5]] | B | SAA1 activity raises ZFAND5's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.26× lower at baseline in the lines without SAA1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[CEBPB]] | B | SAA1 activity raises CEBPB's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.59× lower at baseline in the lines without SAA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[HIF1A]] | B | SAA1 activity raises HIF1A's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without SAA1 | 0.062 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[ZFP36L1]] | B | SAA1 activity raises ZFP36L1's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without SAA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[SH3TC1]] | B | SAA1 activity raises SH3TC1's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.84× lower at baseline in the lines without SAA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[DEPP1]] | B | SAA1 activity raises DEPP1's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 2.51× lower at baseline in the lines without SAA1 | 0.085 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[NCOA3]] | B | SAA1 activity raises NCOA3's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.27× lower at baseline in the lines without SAA1 | 0.0995 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[SAA2]] | C | SAA1 activity raises SAA2's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 4.78× lower at baseline in the lines without SAA1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[SAA2-SAA4]] | C | SAA1 activity raises SAA2-SAA4's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 4.00× lower at baseline in the lines without SAA1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[SAA4]] | C | SAA1 activity raises SAA4's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without SAA1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[TLR2]] | C | SAA1 activity raises TLR2's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 2.31× lower at baseline in the lines without SAA1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.849). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 15.7); signed map (16.7, 29.3). **Vector** length 104, 34.3% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.56 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +11.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.3 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +7.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.9 | +8.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.9 | +8.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.8 | +7.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -3.7 | -4.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.9 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | serum amyloid A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,266,260-18,269,977 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIG4, TP53I4; previously SAA |
| Gene groups (HGNC) | Receptor ligands |
| Reactome | 38 pathways, smallest: Formyl peptide receptors bind formyl peptides and many other ligands; Scavenging by Class B Receptors; Advanced glycosylation endproduct receptor signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DJI8](https://www.uniprot.org/uniprotkb/P0DJI8) (Serum amyloid A-1 protein):

> Major acute phase protein.

**Summary**, from NCBI Gene [6288](https://www.ncbi.nlm.nih.gov/gene/6288):

> This gene encodes a member of the serum amyloid A family of apolipoproteins. The encoded preproprotein is proteolytically processed to generate the mature protein. This protein is a major acute phase protein that is highly expressed in response to inflammation and tissue injury. This protein also plays an important role in HDL metabolism and cholesterol homeostasis. High levels of this protein are associated with chronic inflammatory diseases including atherosclerosis, rheumatoid arthritis, …

**Accessions** — [HGNC:10513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10513) · Entrez [6288](https://www.ncbi.nlm.nih.gov/gene/6288) · UniProt [P0DJI8](https://www.uniprot.org/uniprotkb/P0DJI8) · Ensembl [ENSG00000173432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173432)

## Data

Gene col 10383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10383); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10383]; `tensor/DDL_lfc|DDL_z.npy` [10383]; `embed/gene_vectors.npy` [10383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10383 or target_col == 10383). Every well: [[SAA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
