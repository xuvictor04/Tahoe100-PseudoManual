---
symbol: "RCBTB1"
type: "gene"
col: 5819
ensembl_id: "ENSG00000136144"
name: "RCC1 and BTB domain containing protein 1"
location: "13q14.2"
module: 122
arm: "+"
pooled_cpm: 13.48
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# RCBTB1

*RCC1 and BTB domain containing protein 1* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.53× (z +13.1, q 2e-36, up in 38 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 2 lines (BT-474 0.113×, NCI-H1573 0.119×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0818×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.0727×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPG21]] (+0.61, fdr 1e-05), [[PON2]] (+0.59, fdr 4e-05), [[CIPC]] (+0.59, fdr 6e-05); moves opposite to [[LINC02804]] (-0.55, fdr 3e-04), [[SPTY2D1]] (-0.55, fdr 1e-05), [[KCNK6]] (-0.52, fdr 1e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SOAT1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +13.1 | 2e-36 | 38/47 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +12.5 | 4e-33 | 35/45 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +11.7 | 2e-29 | 35/47 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +11.0 | 4e-26 | 38/47 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.9 | 7e-17 | 30/46 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +8.6 | 7e-16 | 15/26 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +8.6 | 8e-16 | 35/47 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.65×** | +7.1 | 8e-11 | 27/39 (LS 180, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +7.0 | 2e-10 | 29/47 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +6.9 | 4e-10 | 18/32 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.35×** | +6.3 | 1e-08 | 31/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.54×** | +5.8 | 2e-07 | 24/43 (COLO 205, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.5 | 2e-06 | 23/46 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.47×** | +5.5 | 2e-06 | 25/47 (SW480, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.2 | 6e-06 | 20/48 (A-172, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +4.5 | 3e-04 | 19/47 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 5e-04 | 16/47 (NCI-H460, COLO 205, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.001 | 15/47 (LoVo, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.6 | 0.009 | 15/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.078 | 4/48 (COLO 205, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5819.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 2 lines (BT-474 0.113×, NCI-H1573 0.119×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0818×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.0727×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | 0.611× | -3.6 | 0.15 | 12/45 (MIA PaCa-2, AN3 CA, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 23.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -11.0) |
| [[BT-474 (line)]] | alt | 9.23 | 0 | 2 | — | [[Naproxen (drug)]] 0.05 µM 0.0898× (z -9.5) |
| [[COLO 205 (line)]] | alt | 20.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 30.2 | 0 | 2 (1 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0818× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 13.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +18.5) | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0881× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 10.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +12.1) | — |
| [[J82 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +12.8) | — |
| [[KATO III (line)]] | alt | 9.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +9.9) | — |
| [[LoVo (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 5.03 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.119× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 6.54 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.115× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 7.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -9.8) |
| [[SNU-423 (line)]] | alt | 9.93 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0727× (z -11.4) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPG21]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PON2]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[CIPC]] | +0.59 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[USP46]] | +0.58 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[TMEM126B]] | +0.58 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[SEC22C]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PPT1]] | +0.56 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[NCKAP1]] | +0.56 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[SGPL1]] | +0.55 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[VPS36]] | +0.55 | +0.28 / +0.66 | both halves | 3e-04 |  |
| [[TMEM237]] | +0.54 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[MEST]] | +0.54 | +0.32 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02804]] | -0.55 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[SPTY2D1]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[KCNK6]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ARF4]] | -0.52 | -0.58 / -0.43 | both halves | 4e-05 |  |
| [[GPATCH2L]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[ZNF432]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PHKG1]] | -0.51 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.50 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[TINCR]] | -0.50 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[KCNQ1OT1]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[GOLGB1]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[YIPF5]] | -0.50 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOAT1]] | C | SOAT1 activity weakens RCBTB1's drug response | lines that do not express SOAT1 (3) vs lines expressing it (45) | the lines without SOAT1 respond 2.14× as strongly (z diff -3.20); strongest at Belinostat 5 µM: 4.16x vs 2.08x (z diff -4.0) | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.448). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.1, -20.0); signed map (-13.6, -39.7). **Vector** length 69.5, 12.0% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +6.3 |
| fall | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | +0.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.7 | +13.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +2.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[γ-Oryzanol (drug)]] 0.05 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RCC1 and BTB domain containing protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,531,946-49,585,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10716, CLLD7, CLLL7 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDN9](https://www.uniprot.org/uniprotkb/Q8NDN9) (RCC1 and BTB domain-containing protein 1):

> May be involved in cell cycle regulation by chromatin remodeling.

**Summary**, from NCBI Gene [55213](https://www.ncbi.nlm.nih.gov/gene/55213):

> This gene encodes a protein with an N-terminal RCC1 domain and a C-terminal BTB (broad complex, tramtrack and bric-a-brac) domain. In rat, over-expression of this gene in vascular smooth muscle cells induced cellular hypertrophy. In rat, the C-terminus of RCBTB1 interacts with the angiotensin II receptor-1A. In humans, this gene maps to a region of chromosome 13q that is frequently deleted in B-cell chronic lymphocytic leukemia and other lymphoid malignancies. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18243) · Entrez [55213](https://www.ncbi.nlm.nih.gov/gene/55213) · UniProt [Q8NDN9](https://www.uniprot.org/uniprotkb/Q8NDN9) · Ensembl [ENSG00000136144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136144)

## Data

Gene col 5819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5819); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5819]; `tensor/DDL_lfc|DDL_z.npy` [5819]; `embed/gene_vectors.npy` [5819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5819 or target_col == 5819). Every well: [[RCBTB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCBTB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
