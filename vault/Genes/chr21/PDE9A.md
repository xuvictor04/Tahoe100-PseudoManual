---
symbol: "PDE9A"
type: "gene"
col: 8312
ensembl_id: "ENSG00000160191"
name: "phosphodiesterase 9A"
location: "21q22.3"
module: 31
arm: "+"
pooled_cpm: 23.64
n_lines_expressing: 34
n_dd_up: 3
n_dd_down: 32
n_dd_up_clean: 3
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 37
direction_downstream: 28
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PDE9A

*phosphodiesterase 9A* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +10.1, q 4e-21, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.589× (z -13.6, q 1e-39, down in 23 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNS4]] (+0.73, fdr 7e-06), [[PKP2]] (+0.64, fdr 1e-05), [[SH2D3A]] (+0.62, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[GJB3]] → it (grade B ⚠); 28 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +10.1 | 4e-21 | 21/32 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +7.1 | 5e-10 | 14/31 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +6.3 | 5e-08 | 17/31 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.3 | 0.003 | 14/31 (PANC-1, BT-474, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.10 | 5/31 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[SBI-0640756 (drug)]] 5 µM |  | 1.38× | +3.1 | 0.18 | 3/30 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.38× | +3.1 | 0.18 | 5/31 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -13.6 | 1e-39 | 23/32 (SW1417, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.608×** | -9.1 | 4e-17 | 18/26 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.631×** | -8.4 | 1e-14 | 22/31 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.636×** | -7.6 | 4e-12 | 16/25 (HepG2/C3A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -7.3 | 3e-11 | 17/31 (SW1417, NCI-H1573, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.761×** | -7.0 | 2e-10 | 16/32 (HEC-1-A, Hs 766T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -7.0 | 2e-10 | 20/31 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -6.9 | 4e-10 | 22/32 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.682×** | -6.7 | 1e-09 | 15/22 (HepG2/C3A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.709×** | -6.3 | 2e-08 | 17/31 (LoVo, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.786×** | -6.2 | 3e-08 | 18/32 (PANC-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -5.4 | 4e-06 | 16/31 (LoVo, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -5.1 | 1e-05 | 17/29 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -5.0 | 2e-05 | 15/31 (LoVo, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.763×** | -4.9 | 3e-05 | 11/32 (SW480, SW1417, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.9 | 3e-05 | 16/31 (LoVo, AN3 CA, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.798×** | -4.5 | 2e-04 | 12/33 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.638×** | -4.3 | 6e-04 | 9/31 (SW1417, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.796×** | -4.1 | 0.001 | 17/31 (LoVo, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.4 | 0 | 14 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.360× (z -13.4) |
| [[LoVo (line)]] | wt | 77.0 | 0 | 11 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.241× (z -18.0) |
| [[A549 (line)]] | wt | 47.8 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 112 | 2 (1 ⚠) | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.39× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -15.1) |
| [[HT-29 (line)]] | alt | 37.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -10.2) |
| [[LS 180 (line)]] | wt | 30.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 60.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0568× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -9.5) |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -18.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -12.1) |
| [[PANC-1 (line)]] | alt | 6.24 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.2× (z +13.0) | [[Selinexor (drug)]] 5 µM 0.237× (z -11.3) |
| [[SW1417 (line)]] | alt | 63.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 41.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -13.0) |
| [[BT-474 (line)]] | alt | 17.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -10.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.2 | 1 | 1 | [[Budesonide (drug)]] 5 µM 2.94× (z +8.6) | [[Selinexor (drug)]] 5 µM 0.467× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 41.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0722× (z -9.3) ⚠ toxic |
| [[SW48 (line)]] | wt | 32.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -11.0) |
| [[A-427 (line)]] | wt | 30.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -9.9) |
| [[AN3 CA (line)]] | alt | 72.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 8.92 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0870× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0982× (z -14.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 22.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.458× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS4]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PKP2]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[SH2D3A]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[LINC02320]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[NOSTRIN]] | +0.58 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[MST1R]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PLLP]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TMC6]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SLC52A3]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 29, C 8. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GJB3]] | B | GJB3 activity raises PDE9A's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.16× lower at baseline in the lines without GJB3 | 0.004 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[SH2D3A]] | B | SH2D3A activity raises PDE9A's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.34× lower at baseline in the lines without SH2D3A | 0.007 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[HNF4A]] | B | HNF4A activity raises PDE9A's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.93× lower at baseline in the lines without HNF4A | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[B3GNT3]] | B | B3GNT3 activity raises PDE9A's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.20× lower at baseline in the lines without B3GNT3 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[SHH]] | B | SHH activity raises PDE9A's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.77× lower at baseline in the lines without SHH | 0.012 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[NOSTRIN]] | B | NOSTRIN activity raises PDE9A's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without NOSTRIN | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[IQGAP2]] | B | IQGAP2 activity raises PDE9A's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without IQGAP2 | 0.016 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[PKP2]] | B | PKP2 activity raises PDE9A's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without PKP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[LAMA3]] | B | LAMA3 activity raises PDE9A's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.79× lower at baseline in the lines without LAMA3 | 0.018 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[SGPP2]] | B | SGPP2 activity raises PDE9A's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.16× lower at baseline in the lines without SGPP2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[EPHA2-AS1]] | B | EPHA2-AS1 activity raises PDE9A's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without EPHA2-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[ATP2C2]] | B | ATP2C2 activity raises PDE9A's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.80× lower at baseline in the lines without ATP2C2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 22, C 6. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | PDE9A activity raises EPHA2's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.79× lower at baseline in the lines without PDE9A | 0.009 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[TCF7L2]] | B | PDE9A activity raises TCF7L2's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without PDE9A | 0.017 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[CCDC120]] | B | PDE9A activity raises CCDC120's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without PDE9A | 0.018 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[BMP4]] | B | PDE9A activity raises BMP4's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without PDE9A | 0.021 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[SH2D3A]] | B | PDE9A activity raises SH2D3A's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 3.58× lower at baseline in the lines without PDE9A | 0.024 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[SHH]] | B | PDE9A activity raises SHH's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.13× lower at baseline in the lines without PDE9A | 0.026 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[BAIAP2L1]] | B | PDE9A activity raises BAIAP2L1's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without PDE9A | 0.028 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[SLC16A5]] | B | PDE9A activity raises SLC16A5's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without PDE9A | 0.028 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[EPHA2-AS1]] | B | PDE9A activity raises EPHA2-AS1's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without PDE9A | 0.034 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[ABCC3]] | B | PDE9A activity raises ABCC3's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without PDE9A | 0.035 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[MST1R]] | B | PDE9A activity raises MST1R's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 3.16× lower at baseline in the lines without PDE9A | 0.038 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[ADAP1]] | B | PDE9A activity raises ADAP1's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without PDE9A | 0.044 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, 49.7); signed map (5.9, 37.3). **Vector** length 92.2, 22.3% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +3.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.4 | -0.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.2 | -4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.8 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 9A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,653,621-42,775,509 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 4 pathways, smallest: cGMP effects; Nitric oxide stimulates guanylate cyclase; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [O76083](https://www.uniprot.org/uniprotkb/O76083) (High affinity cGMP-specific 3',5'-cyclic phosphodiesterase 9A):

> Specifically hydrolyzes the second messenger cGMP, which is a key regulator of many important physiological processes. Highly specific: compared to other members of the cyclic nucleotide phosphodiesterase family, has the highest affinity and selectivity for cGMP. Specifically regulates natriuretic-peptide-dependent cGMP signaling in heart, acting as a regulator of cardiac hypertrophy in myocytes and muscle. Does not regulate nitric oxide-dependent cGMP in heart. Additional experiments are …

**Summary**, from NCBI Gene [5152](https://www.ncbi.nlm.nih.gov/gene/5152):

> The protein encoded by this gene catalyzes the hydrolysis of cAMP and cGMP to their corresponding monophosphates. The encoded protein plays a role in signal transduction by regulating the intracellular concentration of these cyclic nucleotides. Multiple transcript variants encoding several different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8795) · Entrez [5152](https://www.ncbi.nlm.nih.gov/gene/5152) · UniProt [O76083](https://www.uniprot.org/uniprotkb/O76083) · Ensembl [ENSG00000160191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160191)

## Data

Gene col 8312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8312); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8312]; `tensor/DDL_lfc|DDL_z.npy` [8312]; `embed/gene_vectors.npy` [8312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8312 or target_col == 8312). Every well: [[PDE9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
