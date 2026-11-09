---
symbol: "SCN3A"
type: "gene"
col: 7709
ensembl_id: "ENSG00000153253"
name: "sodium voltage-gated channel alpha subunit 3"
location: "2q24.3"
module: 9
arm: "+"
pooled_cpm: 9.93
n_lines_expressing: 16
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SCN3A

*sodium voltage-gated channel alpha subunit 3* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.67× (z +17.2, q 0e+00, up in 12 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (A-427 0.0807×, NCI-H460 0.248×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.115×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.172×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.323×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.367×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC9]] (+0.71, fdr 7e-06), [[IL7R]] (+0.68, fdr 7e-06), [[LINC02492]] (+0.67, fdr 1e-04); moves opposite to [[MTMR12]] (-0.50, fdr 5e-05), [[ANKRD13D]] (-0.50, fdr 5e-05), [[PRKAR2A]] (-0.50, fdr 5e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TRPC4]] → it (grade C ⚠); 13 go from it, the strongest it → [[FGF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.67×** | +17.2 | 0e+00 | 12/14 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.89×** | +12.5 | 2e-33 | 6/9 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.05×** | +12.3 | 2e-32 | 2/5 (HS-578T, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.44×** | +11.7 | 1e-29 | 8/11 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.41×** | +9.3 | 2e-18 | 11/13 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.25×** | +9.0 | 2e-17 | 4/14 (A498, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.42×** | +9.0 | 2e-17 | 4/5 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +7.8 | 3e-13 | 1/12 (NCI-H2030) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +5.7 | 9e-07 | 9/13 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.16×** | +4.7 | 1e-04 | 8/12 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.78×** | +4.6 | 3e-04 | 0/8 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +4.5 | 3e-04 | 2/12 (A498, NCI-H2030) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.71×** | +3.9 | 0.004 | 1/11 (A498) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.006 | 4/14 (NCI-H2030, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.8 | 0.006 | 2/9 (HS-578T, NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.012 | 1/11 (HS-578T) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.4 | 0.021 | 5/12 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.3 | 0.031 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (A-427 0.0807×, NCI-H460 0.248×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.115×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.172×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.323×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.367×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.645× | -3.5 | 0.15 | 0/11 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.738× | -3.4 | 0.15 | 5/14 (H4, A-172, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.653× | -3.4 | 0.15 | 5/13 (H4, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.665× | -3.2 | 0.17 | 4/13 (H4, NCI-H460, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.668× | -3.2 | 0.17 | 4/12 (SW 900, H4, …) | two highest doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.679× | -3.1 | 0.22 | 0/13 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 132 | 5 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.115× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 6.80 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 41.1× (z +15.9) | [[Neratinib (drug)]] 5 µM 0.0581× (z -8.6) |
| [[HS-578T (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.9× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0807× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 4.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -8.9) |
| [[SW 900 (line)]] | alt | 2.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.5× (z +9.1) | — |
| [[A-172 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC9]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 | pathway: Cardiac conduction |
| [[IL7R]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LINC02492]] | +0.67 | +0.63 / +0.35 | both halves | 1e-04 |  |
| [[OFCC1]] | +0.66 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[EPHA5]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ITGBL1]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SCN2A]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 | same gene group; pathway: Cardiac conduction; STRING 982; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SCG2]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SALL1]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ADARB2]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[PCSK1]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[DMD]] | +0.58 | +0.57 / +0.46 | both halves | 3e-05 | pathway: Muscle contraction |
| [[ADAMTSL1]] | +0.58 | +0.67 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR12]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ANKRD13D]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[PRKAR2A]] | -0.50 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[HEBP1]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[IMPDH1]] | -0.48 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPC4]] | C | TRPC4 activity raises SCN3A's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.46× lower at baseline in the lines without TRPC4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises SCN3A's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 3.06× lower at baseline in the lines without LINC01592 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[SCN2A]] | C | SCN2A activity raises SCN3A's level | lines that do not express SCN2A (26) vs lines expressing it (24) | 2.57× lower at baseline in the lines without SCN2A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTPRN, ENSG00000286251, EDA2R; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises SCN3A's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.25× lower at baseline in the lines without CDH10 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises SCN3A's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.97× lower at baseline in the lines without EPHA5 | 0.044 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[ZNF804A]] | C | ZNF804A activity raises SCN3A's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 2.93× lower at baseline in the lines without ZNF804A | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[CCL3]] | C | CCL3 activity raises SCN3A's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 3.20× lower at baseline in the lines without CCL3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises SCN3A's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without EPHA5-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[LINC01287]] | C | LINC01287 activity raises SCN3A's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 3.14× lower at baseline in the lines without LINC01287 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises SCN3A's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.33× lower at baseline in the lines without PCSK1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[INHBA]] | C | INHBA activity raises SCN3A's level | lines that do not express INHBA (32) vs lines expressing it (18) | 2.39× lower at baseline in the lines without INHBA | 0.092 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises SCN3A's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 4.31× lower at baseline in the lines without GSG1L2 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 2, C 11. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF2]] | B | SCN3A activity raises FGF2's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without SCN3A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865 |
| [[ADAMTSL1]] | B | SCN3A activity raises ADAMTSL1's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without SCN3A | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865 |
| [[TRPC4]] | C | SCN3A activity raises TRPC4's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 5.65× lower at baseline in the lines without SCN3A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[EPHA5]] | C | SCN3A activity raises EPHA5's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 6.21× lower at baseline in the lines without SCN3A | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[EPHA5-AS1]] | C | SCN3A activity raises EPHA5-AS1's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.96× lower at baseline in the lines without SCN3A | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[ABCC9]] | C | SCN3A activity raises ABCC9's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without SCN3A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[PCDH9]] | C | SCN3A activity raises PCDH9's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.72× lower at baseline in the lines without SCN3A | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[ZNF804A]] | C | SCN3A activity raises ZNF804A's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 4.67× lower at baseline in the lines without SCN3A | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[FMN2]] | C | SCN3A activity raises FMN2's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 3.38× lower at baseline in the lines without SCN3A | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[TMPRSS15]] | C | SCN3A activity raises TMPRSS15's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.31× lower at baseline in the lines without SCN3A | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[CCL3]] | C | SCN3A activity raises CCL3's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without SCN3A | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[CSMD3]] | C | SCN3A activity raises CSMD3's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.58× lower at baseline in the lines without SCN3A | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.6, 28.0); signed map (40.6, 29.8). **Vector** length 41.9, 13.3% of its response variance represented; |z| ≥ 3 in 255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | sodium voltage-gated channel alpha subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:165,087,526-165,204,050 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nav1.3 |
| Gene groups (HGNC) | Sodium voltage-gated channel alpha subunits |
| Reactome | 10 pathways, smallest: Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste; Interaction between L1 and Ankyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY46](https://www.uniprot.org/uniprotkb/Q9NY46) (Sodium channel protein type 3 subunit alpha):

> Pore-forming subunit of Nav1.3, a voltage-gated sodium (Nav) channel that directly mediates the depolarizing phase of action potentials in excitable membranes. Navs, also called VGSCs (voltage-gated sodium channels) or VDSCs (voltage-dependent sodium channels), operate by switching between closed and open conformations depending on the voltage difference across the membrane. In the open conformation they allow Na(+) ions to selectively pass through the pore, along their electrochemical …

**Summary**, from NCBI Gene [6328](https://www.ncbi.nlm.nih.gov/gene/6328):

> Voltage-gated sodium channels are transmembrane glycoprotein complexes composed of a large alpha subunit with 24 transmembrane domains and one or more regulatory beta subunits. They are responsible for the generation and propagation of action potentials in neurons and muscle. This gene encodes one member of the sodium channel alpha subunit gene family, and is found in a cluster of five alpha subunit genes on chromosome 2. Multiple transcript variants encoding different isoforms have been found …

**Accessions** — [HGNC:10590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10590) · Entrez [6328](https://www.ncbi.nlm.nih.gov/gene/6328) · UniProt [Q9NY46](https://www.uniprot.org/uniprotkb/Q9NY46) · Ensembl [ENSG00000153253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153253)

## Data

Gene col 7709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7709); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7709]; `tensor/DDL_lfc|DDL_z.npy` [7709]; `embed/gene_vectors.npy` [7709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7709 or target_col == 7709). Every well: [[SCN3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCN3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
