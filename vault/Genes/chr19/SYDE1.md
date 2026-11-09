---
symbol: "SYDE1"
type: "gene"
col: 2552
ensembl_id: "ENSG00000105137"
name: "synapse defective Rho GTPase activating protein 1"
location: "19p13.12"
module: 55
arm: "+"
pooled_cpm: 12.12
n_lines_expressing: 39
n_dd_up: 0
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SYDE1

*synapse defective Rho GTPase activating protein 1* — 19p13.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.104× (z -21.9, q 0e+00, down in 36 of 37 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAQR7]] (+0.55, fdr 1e-05), [[C8orf58]] (+0.54, fdr 1e-05), [[SMAD9]] (+0.53, fdr 2e-05); moves opposite to [[MFSD6]] (-0.54, fdr 3e-05), [[GPX2]] (-0.52, fdr 7e-04), [[EPS8L3]] (-0.51, fdr 2e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[EPCAM]] → it (grade B ⚠); 3 go from it, the strongest it → [[ABO]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2552.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbamazepine (drug)]] 5 µM |  | 1.41× | +3.4 | 0.39 | 10/35 (RPMI-7951, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2552.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.104×** | -21.9 | 0e+00 | 36/37 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.112×** | -21.2 | 0e+00 | 36/36 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.121×** | -20.5 | 0e+00 | 36/36 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.267×** | -18.0 | 0e+00 | 33/35 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.357×** | -14.1 | 7e-43 | 31/34 (NCI-H1792, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.288×** | -12.0 | 2e-31 | 32/37 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.332×** | -10.2 | 1e-22 | 25/33 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.373×** | -9.5 | 1e-19 | 26/34 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.409×** | -8.3 | 7e-15 | 26/36 (C-33 A, BT-474, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.428×** | -8.2 | 2e-14 | 25/32 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.427×** | -7.9 | 1e-13 | 25/36 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.205×** | -7.6 | 2e-12 | 30/36 (NCI-H23, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.603×** | -6.9 | 3e-10 | 27/36 (HOP62, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.491×** | -6.9 | 3e-10 | 25/36 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.458×** | -6.8 | 4e-10 | 29/35 (A-427, H4, …) | all doses, flat | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 21.6 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0576× (z -18.6) |
| [[NCI-H23 (line)]] | alt | 25.7 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0377× (z -21.3) |
| [[C32 (line)]] | wt | 15.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -16.9) |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.0474× (z -19.4) |
| [[H4 (line)]] | wt | 26.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0547× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0883× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0787× (z -12.7) |
| [[J82 (line)]] | alt | 32.3 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0691× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 6 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0938× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0676× (z -17.0) |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -19.2) |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.0594× (z -16.7) |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0668× (z -16.1) |
| [[A-172 (line)]] | wt | 38.4 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0318× (z -22.8) |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0272× (z -16.8) |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0228× (z -21.2) |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -16.9) |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0883× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 6.97 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0567× (z -11.9) |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0579× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0632× (z -12.4) |
| [[SW 900 (line)]] | alt | 6.84 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0759× (z -12.8) |
| [[A-427 (line)]] | wt | 10.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.108× (z -9.9) |
| [[Hs 766T (line)]] | wt | 7.40 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.00997× (z -19.8) |
| [[NCI-H2030 (line)]] | alt | 26.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 3.49 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0230× (z -11.4) |
| [[SW480 (line)]] | alt | 4.33 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0992× (z -10.4) |
| [[A498 (line)]] | wt | 10.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -8.7) |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0568× (z -8.8) |
| [[A549 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.961 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR7]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[C8orf58]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SMAD9]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CLP1]] | +0.48 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[TMEM45A]] | +0.46 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ELP6]] | +0.45 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[THAP11]] | +0.45 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[ZNF8-DT]] | +0.45 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[APBA2]] | +0.44 | +0.52 / +0.29 | both halves | 3e-04 |  |
| [[KDM2B-DT]] | +0.43 | +0.37 / +0.42 | both halves | 7e-05 |  |
| [[ZNF93]] | +0.43 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[SOX12]] | +0.43 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD6]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[GPX2]] | -0.52 | -0.63 / -0.21 | both halves | 7e-04 |  |
| [[EPS8L3]] | -0.51 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[ABO]] | -0.49 | -0.69 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[SLC6A20]] | -0.49 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[ZBTB7C]] | -0.49 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[IL20RA]] | -0.49 | -0.62 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[CLIC5]] | -0.49 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[MAP4K3-DT]] | -0.48 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MYO7B]] | -0.48 | -0.58 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[SPINT1-AS1]] | -0.47 | -0.62 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[FAM3D]] | -0.47 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[TMPRSS2]] | -0.47 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[POF1B]] | -0.47 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[SLC5A1]] | -0.47 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[CD9]] | -0.47 | -0.30 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPCAM]] | B | EPCAM activity lowers SYDE1's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 3.94× higher at baseline in the lines without EPCAM | 0.014 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[ABO]] | B | ABO activity lowers SYDE1's level | lines that do not express ABO (32) vs lines expressing it (18) | 4.74× higher at baseline in the lines without ABO | 0.030 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[SYK]] | B | SYK activity lowers SYDE1's level | lines that do not express SYK (30) vs lines expressing it (20) | 4.19× higher at baseline in the lines without SYK | 0.035 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[TSPAN1]] | B | TSPAN1 activity lowers SYDE1's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 3.23× higher at baseline in the lines without TSPAN1 | 0.035 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[TOX3]] | B | TOX3 activity weakens SYDE1's drug response | lines that do not express TOX3 (27) vs lines expressing it (10) | the lines without TOX3 respond 1.20× as strongly (z diff -1.47); strongest at Idarubicin (hydrochloride) 5 µM: 0.33x vs 0.44x (z diff -3.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; target measured in part of the lines; artifact flags |
| [[SMAD9]] | B | SMAD9 activity strengthens SYDE1's drug response | lines that do not express SMAD9 (6) vs lines expressing it (31) | the lines without SMAD9 respond 0.80× as strongly (z diff +2.02); strongest at Homoharringtonine 0.5 µM: 0.53x vs 0.32x (z diff +2.9) | 0.068 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2; target measured in part of the lines; artifact flags |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity lowers SYDE1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 3.57× higher at baseline in the lines without SPINT1-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises SYDE1's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 4.62× lower at baseline in the lines without KDM2B-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[TOX3]] | B | TOX3 activity lowers SYDE1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.89× higher at baseline in the lines without TOX3 | 0.099 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[MIR130AHG]] | C | MIR130AHG activity raises SYDE1's level | lines that do not express MIR130AHG (14) vs lines expressing it (36) | 4.82× lower at baseline in the lines without MIR130AHG | 0.091 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: SPART, RAB34, PYGO1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABO]] | B | SYDE1 activity lowers ABO's level | lines that do not express SYDE1 (11) vs lines expressing it (39) | 10.63× higher at baseline in the lines without SYDE1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with APC, ACVR2A; also absent: DNAAF9, ZNF134, ENSG00000286964 |
| [[WWP1]] | B | SYDE1 activity lowers WWP1's level | lines that do not express SYDE1 (11) vs lines expressing it (39) | 1.32× higher at baseline in the lines without SYDE1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with APC, ACVR2A; also absent: DNAAF9, ZNF134, ENSG00000286964 |
| [[C8orf58]] | B | SYDE1 activity raises C8orf58's level | lines that do not express SYDE1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without SYDE1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with APC, ACVR2A; also absent: DNAAF9, ZNF134, ENSG00000286964 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction -0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.5, 46.6); signed map (-30.6, 31.9). **Vector** length 79.6, 19.5% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +0.7 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.5 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -14.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | synapse defective Rho GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,107,401-15,114,985 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 7h3, FLJ13511, SYD1 |
| Reactome | 9 pathways, smallest: RHOF GTPase cycle; RHOJ GTPase cycle; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZW31](https://www.uniprot.org/uniprotkb/Q6ZW31) (Rho GTPase-activating protein SYDE1):

> GTPase activator for the Rho-type GTPases. As a GCM1 downstream effector, it is involved in placental development and positively regulates trophoblast cells migration. It regulates cytoskeletal remodeling by controlling the activity of Rho GTPases including RHOA, CDC42 and RAC1.

**Summary**, from NCBI Gene [85360](https://www.ncbi.nlm.nih.gov/gene/85360):

> The protein encoded by this gene is a Rho GTPase-activating protein highly expressed in placenta. The encoded protein is involved in cytoskeletal remodeling and trophoblast cell migration. Decreased expression of this gene has been associated with intrauterine growth restriction (IUGR). [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:25824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25824) · Entrez [85360](https://www.ncbi.nlm.nih.gov/gene/85360) · UniProt [Q6ZW31](https://www.uniprot.org/uniprotkb/Q6ZW31) · Ensembl [ENSG00000105137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105137)

## Data

Gene col 2552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2552); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2552]; `tensor/DDL_lfc|DDL_z.npy` [2552]; `embed/gene_vectors.npy` [2552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2552 or target_col == 2552). Every well: [[SYDE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYDE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
