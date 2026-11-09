---
symbol: "LYRM2"
type: "gene"
col: 1362
ensembl_id: "ENSG00000083099"
name: "LYR motif containing 2"
location: "6q15"
module: 16
arm: "+"
pooled_cpm: 18.61
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# LYRM2

*LYR motif containing 2* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +10.1, q 2e-21, up in 35 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +9.3, q 3e-18, up in 35 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (BT-474 0.115×, COLO 205 0.102×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.110×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.195×; ⚠ toxic; transcription drop); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SNU-1 0.171×); [[Talc (drug)]] 0.5 µM in 1 line (NCI-H661 0.0675×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM4]] (+0.75, fdr 7e-06), [[COQ7]] (+0.75, fdr 7e-06), [[LZIC]] (+0.74, fdr 1e-05); moves opposite to [[SDHAP1]] (-0.66, fdr 4e-05), [[PMS2P3-1]] (-0.65, fdr 9e-06), [[SETD3]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NRIP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.26×** | +10.1 | 2e-21 | 35/42 (PANC-1, A-427, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +9.3 | 3e-18 | 35/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +9.1 | 2e-17 | 42/48 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +8.0 | 1e-13 | 30/37 (KATO III, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +7.4 | 1e-11 | 36/44 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.85×** | +7.3 | 2e-11 | 25/32 (NCI-H2030, J82, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +6.7 | 1e-09 | 32/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +6.3 | 3e-08 | 37/47 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +5.6 | 1e-06 | 29/48 (NCI-H2347, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.6 | 1e-06 | 36/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.50×** | +5.0 | 2e-05 | 27/48 (KATO III, A549, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +4.7 | 1e-04 | 25/47 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 18/48 (A-172, PANC-1, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 18/47 (LS 180, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.005 | 16/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.018 | 16/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.065 | 9/44 (NCI-H1573, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.065 | 11/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.067 | 13/48 (RPMI-7951, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1362.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (BT-474 0.115×, COLO 205 0.102×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.110×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.195×; ⚠ toxic; transcription drop); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SNU-1 0.171×); [[Talc (drug)]] 0.5 µM in 1 line (NCI-H661 0.0675×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.743× | -3.7 | 0.11 | 18/47 (NCI-H2030, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.763× | -3.4 | 0.20 | 16/47 (SW48, LOX-IMVI, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.773× | -3.2 | 0.24 | 10/48 (PANC-1, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -13.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -10.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.110× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.39× (z +8.7) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.0) | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0675× (z -8.7) |
| [[PANC-1 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.171× (z -9.1) |
| [[SNU-423 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.9) | — |
| [[A-427 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | +0.75 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[COQ7]] | +0.75 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[LZIC]] | +0.74 | +0.82 / +0.54 | both halves | 1e-05 |  |
| [[ZNF260]] | +0.73 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[UBQLN2]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[METTL18]] | +0.73 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[HNRNPH2]] | +0.72 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.71 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.70 | +0.79 / +0.55 | both halves | 1e-05 |  |
| [[RBM23]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[LIG4]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[GTF2H1]] | +0.69 | +0.75 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | -0.66 | -0.80 / -0.41 | both halves | 4e-05 |  |
| [[PMS2P3-1]] | -0.65 | -0.73 / -0.57 | both halves | 9e-06 |  |
| [[SETD3]] | -0.65 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[DCUN1D2]] | -0.64 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.64 | -0.74 / -0.42 | both halves | 4e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[IFI27L1]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.63 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[ATP7B]] | -0.62 | -0.68 / -0.46 | both halves | 3e-05 |  |
| [[SDHAP2]] | -0.62 | -0.77 / -0.39 | both halves | 5e-05 |  |
| [[IER3IP1]] | -0.62 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[RGS10]] | -0.62 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[SRD5A1]] | -0.61 | -0.64 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRIP1]] | B | NRIP1 activity lowers LYRM2's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.54× higher at baseline in the lines without NRIP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.5, 10.9); signed map (11.6, -29.7). **Vector** length 73.0, 14.5% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.5 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +3.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +1.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | LYR motif containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,568,144-89,638,749 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DJ122O8.2 |
| Gene groups (HGNC) | LYR motif containing |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NU23](https://www.uniprot.org/uniprotkb/Q9NU23) (LYR motif-containing protein 2):

> Involved in efficient integration of the N-module into mitochondrial respiratory chain complex I.

**Summary**, from NCBI Gene [57226](https://www.ncbi.nlm.nih.gov/gene/57226):

> Involved in mitochondrial respiratory chain complex I assembly. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25229) · Entrez [57226](https://www.ncbi.nlm.nih.gov/gene/57226) · UniProt [Q9NU23](https://www.uniprot.org/uniprotkb/Q9NU23) · Ensembl [ENSG00000083099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083099)

## Data

Gene col 1362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1362); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1362]; `tensor/DDL_lfc|DDL_z.npy` [1362]; `embed/gene_vectors.npy` [1362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1362 or target_col == 1362). Every well: [[LYRM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYRM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
