---
symbol: "HSD11B2"
type: "gene"
col: 10708
ensembl_id: "ENSG00000176387"
name: "hydroxysteroid 11-beta dehydrogenase 2"
location: "16q22.1"
module: 78
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 34
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 23
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# HSD11B2

*hydroxysteroid 11-beta dehydrogenase 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.67× (z +11.4, q 4e-27, up in 10 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (CHP-212 0.0468×, SW480 0.255×); [[Belinostat (drug)]] 5 µM in 1 line (CHP-212 0.00934×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CHP-212 0.0337×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (CHP-212 0.0411×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF330]] (+0.58, fdr 4e-05), [[HOTAIR]] (+0.53, fdr 6e-05), [[BATF]] (+0.53, fdr 1e-05); moves opposite to [[ASPH]] (-0.55, fdr 1e-04), [[PC]] (-0.48, fdr 1e-04), [[SH3KBP1]] (-0.47, fdr 2e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[HNF1A-AS1]] → it (grade B ⚠); 23 go from it, the strongest it → [[MIR3936HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +11.4 | 4e-27 | 10/18 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.41×** | +10.1 | 9e-22 | 16/28 (LS 180, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +8.6 | 1e-15 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +7.3 | 4e-11 | 9/13 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.42×** | +7.2 | 7e-11 | 14/25 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.08×** | +6.0 | 2e-07 | 13/26 (HT-29, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.89×** | +5.2 | 2e-05 | 13/28 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.0 | 4e-05 | 1/12 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 10/28 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.0 | 0.004 | 7/16 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.005 | 4/19 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.9 | 0.005 | 4/22 (NCI-H2030, SW480, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.006 | 6/17 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.008 | 5/21 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +3.4 | 0.023 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.057 | 2/18 (LoVo, SW480) | inconsistent across doses | low cells (technical?) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.071 | 4/25 (BT-474, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +2.9 | 0.097 | 3/19 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10708.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (CHP-212 0.0468×, SW480 0.255×); [[Belinostat (drug)]] 5 µM in 1 line (CHP-212 0.00934×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CHP-212 0.0337×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (CHP-212 0.0411×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.438× | -3.5 | 0.15 | 8/23 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | 0.655× | -3.5 | 0.15 | 11/23 (LoVo, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.474× | -3.2 | 0.20 | 12/23 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.474× | -3.2 | 0.20 | 9/27 (LS 180, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.693× | -3.0 | 0.25 | 1/29 (SHP-77) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.495× | -3.0 | 0.25 | 0/28 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 40.6 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.00934× (z -13.7) |
| [[HT-29 (line)]] | alt | 6.70 | 2 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 6.31× (z +10.0) | [[Digitoxin (drug)]] 0.05 µM 0.0898× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 11.6 | 3 | 0 | [[Selinexor (drug)]] 5 µM 9.22× (z +15.7) | — |
| [[SW1417 (line)]] | alt | 29.1 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.96× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -8.5) |
| [[COLO 205 (line)]] | alt | 3.94 | 1 | 0 | [[Selinexor (drug)]] 5 µM 9.21× (z +8.5) | — |
| [[KATO III (line)]] | alt | 5.43 | 1 | 0 | [[Selinexor (drug)]] 5 µM 11.0× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +11.4) | — |
| [[A-172 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.991 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF330]] | +0.58 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[HOTAIR]] | +0.53 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[BATF]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SMPDL3B]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FGD3]] | +0.49 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[CDX2]] | +0.48 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SLC16A9]] | +0.48 | +0.29 / +0.57 | both halves | 2e-04 |  |
| [[PPARGC1B]] | +0.47 | +0.49 / +0.43 | both halves | 4e-05 |  |
| [[MIR4527HG]] | +0.47 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[CHDH]] | +0.47 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[F5]] | +0.47 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[PLA2G2A]] | +0.46 | +0.45 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASPH]] | -0.55 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[PC]] | -0.48 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[SH3KBP1]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[BZW1]] | -0.46 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[EHBP1L1]] | -0.43 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[RMC1]] | -0.42 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[DYNLT3]] | -0.42 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[ITPRID2]] | -0.41 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[PSD3]] | -0.40 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[ABCB8]] | -0.40 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[SH3BGRL3]] | -0.40 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[G6PD]] | -0.40 | -0.06 / -0.53 | ⚠ one half (not replicated) | 0.004 | STRING 557 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises HSD11B2's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without HNF1A-AS1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[HNF1A]] | B | HNF1A activity raises HSD11B2's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without HNF1A | 0.091 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[CDX2]] | B | CDX2 activity raises HSD11B2's level | lines that do not express CDX2 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without CDX2 | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM83F, CKMT1A, ENSG00000225680 |
| [[CHDH]] | C | CHDH activity raises HSD11B2's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.95× lower at baseline in the lines without CHDH | 0.032 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[FGD3]] | C | FGD3 activity raises HSD11B2's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without FGD3 | 0.035 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent; co-absent with the target |
| [[CKMT1B]] | C | CKMT1B activity raises HSD11B2's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without CKMT1B | 0.059 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B; co-absent with the target |
| [[SPINT1-AS1]] | C | SPINT1-AS1 activity raises HSD11B2's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.34× lower at baseline in the lines without SPINT1-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 18, C 5. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR3936HG]] | B | HSD11B2 activity raises MIR3936HG's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 2.16× lower at baseline in the lines without HSD11B2 | 0.005 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[RCHY1]] | B | HSD11B2 activity raises RCHY1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without HSD11B2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[C10orf95-AS1]] | B | HSD11B2 activity raises C10orf95-AS1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without HSD11B2 | 0.011 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[MBNL3]] | B | HSD11B2 activity raises MBNL3's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without HSD11B2 | 0.051 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[AKAP1]] | B | HSD11B2 activity raises AKAP1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without HSD11B2 | 0.052 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[IL17RE]] | B | HSD11B2 activity raises IL17RE's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without HSD11B2 | 0.070 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[MIR3936HG]] | B | HSD11B2 activity strengthens MIR3936HG's drug response | lines that do not express HSD11B2 (15) vs lines expressing it (32) | the lines without HSD11B2 respond 0.72× as strongly (z diff +1.32); strongest at Ouabain (Octahydrate) 5 µM: 0.64x vs 0.42x (z diff +2.8) | 0.076 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PM20D2]] | B | HSD11B2 activity raises PM20D2's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without HSD11B2 | 0.079 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| cells under [[Imiquimod (hydrochloride) (drug)]] 5 µM | B | HSD11B2 activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express HSD11B2 (16) vs lines expressing it (32) | the lines without HSD11B2: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[HSBP1L1]] | B | HSD11B2 activity raises HSBP1L1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without HSD11B2 | 0.083 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[RNF138]] | B | HSD11B2 activity raises RNF138's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.21× lower at baseline in the lines without HSD11B2 | 0.086 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[RPP25]] | B | HSD11B2 activity raises RPP25's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without HSD11B2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction -0.344). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.6, 18.3); signed map (51.0, 9.5). **Vector** length 55.1, 11.3% of its response variance represented; |z| ≥ 3 in 681 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.2 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.3 | +7.2 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +2.3 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.2 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid 11-beta dehydrogenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,430,652-67,437,553 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR9C3 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | PEROXISOME, KRAS_SIGNALING_DN |
| Reactome | 5 pathways, smallest: Prednisone ADME; Metabolism of steroid hormones; Drug ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P80365](https://www.uniprot.org/uniprotkb/P80365) (11-beta-hydroxysteroid dehydrogenase type 2):

> Catalyzes the conversion of biologically active 11beta-hydroxyglucocorticoids (11beta-hydroxysteroid) such as cortisol, to inactive 11-ketoglucocorticoids (11-oxosteroid) such as cortisone, in the presence of NAD(+). Functions as a dehydrogenase (oxidase), thereby decreasing the concentration of active glucocorticoids, thus protecting the nonselective mineralocorticoid receptor from occupation by glucocorticoids. Plays an important role in maintaining glucocorticoids balance during …

**Summary**, from NCBI Gene [3291](https://www.ncbi.nlm.nih.gov/gene/3291):

> There are at least two isozymes of the corticosteroid 11-beta-dehydrogenase, a microsomal enzyme complex responsible for the interconversion of cortisol and cortisone. The type I isozyme has both 11-beta-dehydrogenase (cortisol to cortisone) and 11-oxoreductase (cortisone to cortisol) activities. The type II isozyme, encoded by this gene, has only 11-beta-dehydrogenase activity. In aldosterone-selective epithelial tissues such as the kidney, the type II isozyme catalyzes the glucocorticoid …

**Accessions** — [HGNC:5209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5209) · Entrez [3291](https://www.ncbi.nlm.nih.gov/gene/3291) · UniProt [P80365](https://www.uniprot.org/uniprotkb/P80365) · Ensembl [ENSG00000176387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176387)

## Data

Gene col 10708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10708); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10708]; `tensor/DDL_lfc|DDL_z.npy` [10708]; `embed/gene_vectors.npy` [10708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10708 or target_col == 10708). Every well: [[HSD11B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD11B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
