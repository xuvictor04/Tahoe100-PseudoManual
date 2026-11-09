---
symbol: "DYSF"
type: "gene"
col: 5735
ensembl_id: "ENSG00000135636"
name: "dysferlin"
location: "2p13.2"
module: 53
arm: "+"
pooled_cpm: 7.81
n_lines_expressing: 39
n_dd_up: 42
n_dd_down: 2
n_dd_up_clean: 32
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# DYSF

*dysferlin* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.65× (z +24.9, q 0e+00, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.632× (z -6.3, q 2e-07, down in 16 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (SNU-423 0.418×, Panc 03.27 0.420×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.170×, Panc 03.27 0.282×; ⚠ cell-cycle shift, explains ~22% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.270×; ⚠ toxic; cell-cycle shift, explains ~47% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.320×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00616]] (+0.62, fdr 2e-05), [[DNAH10]] (+0.62, fdr 1e-05), [[SLC2A9]] (+0.61, fdr 1e-05); moves opposite to [[BTBD3]] (-0.51, fdr 2e-04), [[SPATA6]] (-0.50, fdr 2e-04).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KPNA7]] → it (grade B ⚠); 10 go from it, the strongest it → [[USP50]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +24.9 | 0e+00 | 20/29 (NCI-H23, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.56×** | +24.4 | 0e+00 | 21/27 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.43×** | +16.8 | 0e+00 | 28/33 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.51×** | +12.5 | 7e-34 | 19/27 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +12.0 | 6e-31 | 3/10 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +11.3 | 1e-27 | 15/35 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +10.5 | 1e-23 | 14/26 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.11×** | +9.6 | 7e-20 | 21/31 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +9.5 | 2e-19 | 8/19 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.88×** | +8.6 | 4e-16 | 19/35 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +8.1 | 2e-14 | 12/25 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.9 | 2e-13 | 8/36 (HOP62, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +7.6 | 2e-12 | 14/31 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.8 | 4e-10 | 4/13 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +6.8 | 4e-10 | 15/33 (HOP62, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +6.1 | 4e-08 | 14/32 (NCI-H1573, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.48×** | +6.1 | 5e-08 | 7/31 (HEC-1-A, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.55×** | +5.7 | 3e-07 | 13/34 (Panc 03.27, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5735.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (SNU-423 0.418×, Panc 03.27 0.420×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.170×, Panc 03.27 0.282×; ⚠ cell-cycle shift, explains ~22% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.270×; ⚠ toxic; cell-cycle shift, explains ~47% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.320×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.632×** | -6.3 | 2e-07 | 16/30 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.746×** | -4.0 | 0.016 | 4/36 (CFPAC-1, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.790× | -3.2 | 0.15 | 10/33 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.791× | -3.2 | 0.15 | 4/35 (J82, NCI-H1792, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | 0.784× | -3.2 | 0.15 | 4/34 (HEC-1-A, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +14.9) | — |
| [[Panc 03.27 (line)]] | alt | 50.5 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -8.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[CFPAC-1 (line)]] | alt | 27.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -9.6) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -8.8) |
| [[HOP62 (line)]] | alt | 7.57 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.79× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 2.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 56.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.2) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.418× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 5.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 5.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +9.0) | — |
| [[LoVo (line)]] | wt | 2.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.0) | — |
| [[SW480 (line)]] | alt | 5.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +8.5) | — |
| [[A-427 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00616]] | +0.62 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[DNAH10]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.61 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CFAP70]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[NEB]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 | pathway: Muscle contraction; STRING 590 |
| [[FER1L6]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 | same gene group |
| [[PTOV1-AS1]] | +0.59 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[C2CD6]] | +0.59 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[LINC01033]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TG]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DNAH12]] | +0.57 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SSUH2]] | +0.57 | +0.54 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD3]] | -0.51 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[SPATA6]] | -0.50 | -0.46 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA7]] | B | KPNA7 activity raises DYSF's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without KPNA7 | 0.051 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DYSF's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PKP1]] | B | PKP1 activity weakens DYSF's drug response | lines that do not express PKP1 (26) vs lines expressing it (9) | the lines without PKP1 respond 1.72× as strongly (z diff -1.46); strongest at Homoharringtonine 5 µM: 4.56x vs 1.53x (z diff -5.3) | 0.084 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; target measured in part of the lines; artifact flags |
| [[NCF2]] | B | NCF2 activity raises DYSF's level | lines that do not express NCF2 (9) vs lines expressing it (41) | 2.16× lower at baseline in the lines without NCF2 | 0.091 | ⚠ within organs, on part of the lines; also absent: MAML2; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP50]] | B | DYSF activity raises USP50's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without DYSF | 0.043 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[MFSD2B]] | B | DYSF activity raises MFSD2B's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without DYSF | 0.052 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[CMYA5]] | B | DYSF activity raises CMYA5's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without DYSF | 0.058 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[SLC6A13]] | B | DYSF activity raises SLC6A13's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without DYSF | 0.058 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[MYOCOS]] | B | DYSF activity raises MYOCOS's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without DYSF | 0.072 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[SLC35F4]] | B | DYSF activity lowers SLC35F4's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.63× higher at baseline in the lines without DYSF | 0.072 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[HVCN1]] | B | DYSF activity raises HVCN1's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without DYSF | 0.075 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[SPON1-AS1]] | B | DYSF activity raises SPON1-AS1's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without DYSF | 0.085 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[CIBAR1-DT]] | B | DYSF activity lowers CIBAR1-DT's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.29× higher at baseline in the lines without DYSF | 0.089 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent; its own permutation p |
| [[SLC2A14]] | C | DYSF activity raises SLC2A14's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without DYSF | 0.052 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, -9.3); signed map (22.9, 9.3). **Vector** length 72.7, 13.5% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.8 | +16.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +24.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +24.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +5.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | dysferlin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:71,453,561-71,686,763 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FER1L1; previously LGMD2B |
| Gene groups (HGNC) | Ferlin family |
| Reactome | 2 pathways, smallest: Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [O75923](https://www.uniprot.org/uniprotkb/O75923) (Dysferlin):

> Key calcium ion sensor involved in the Ca(2+)-triggered synaptic vesicle-plasma membrane fusion. Plays a role in the sarcolemma repair mechanism of both skeletal muscle and cardiomyocytes that permits rapid resealing of membranes disrupted by mechanical stress (By similarity).

**Summary**, from NCBI Gene [8291](https://www.ncbi.nlm.nih.gov/gene/8291):

> The protein encoded by this gene belongs to the ferlin family and is a skeletal muscle protein found associated with the sarcolemma. It is involved in muscle contraction and contains C2 domains that play a role in calcium-mediated membrane fusion events, suggesting that it may be involved in membrane regeneration and repair. In addition, the protein encoded by this gene binds caveolin-3, a skeletal muscle membrane protein which is important in the formation of caveolae. Specific mutations in …

**Accessions** — [HGNC:3097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3097) · Entrez [8291](https://www.ncbi.nlm.nih.gov/gene/8291) · UniProt [O75923](https://www.uniprot.org/uniprotkb/O75923) · Ensembl [ENSG00000135636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135636)

## Data

Gene col 5735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5735); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5735]; `tensor/DDL_lfc|DDL_z.npy` [5735]; `embed/gene_vectors.npy` [5735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5735 or target_col == 5735). Every well: [[DYSF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYSF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
