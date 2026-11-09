---
symbol: "GABRE"
type: "gene"
col: 2233
ensembl_id: "ENSG00000102287"
name: "gamma-aminobutyric acid type A receptor subunit epsilon"
location: "Xq28"
module: 19
arm: "+"
pooled_cpm: 27.88
n_lines_expressing: 30
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 13
direction_downstream: 16
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GABRE

*gamma-aminobutyric acid type A receptor subunit epsilon* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.02× (z +8.4, q 2e-14, up in 20 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.449× (z -9.3, q 1e-17, down in 23 of 28 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.347× (z -6.6, q 4e-09, down in 22 of 29 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLAC4]] (+0.58, fdr 2e-05), [[CRLF2]] (+0.54, fdr 1e-05), [[GTF2IP7]] (+0.50, fdr 2e-05); moves opposite to [[PTBP2]] (-0.48, fdr 5e-05), [[ARMC8]] (-0.48, fdr 1e-04), [[TADA2A]] (-0.47, fdr 8e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SLC16A4]] → it (grade B ⚠); 16 go from it, the strongest it → [[FAM107B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +8.4 | 2e-14 | 20/28 (HT-29, SW480, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +6.9 | 2e-09 | 13/28 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +5.6 | 3e-06 | 17/28 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.8 | 0.023 | 14/28 (H4, J82, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.064 | 11/28 (NCI-H1573, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.63× | +3.1 | 0.20 | 10/28 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.449×** | -9.3 | 1e-17 | 23/28 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.518×** | -7.6 | 7e-12 | 18/21 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.664×** | -7.0 | 6e-10 | 19/28 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -6.6 | 4e-09 | 22/29 (LS 180, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.594×** | -6.3 | 4e-08 | 20/28 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.587×** | -5.9 | 3e-07 | 18/22 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.652×** | -5.2 | 2e-05 | 17/24 (HT-29, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.658×** | -5.0 | 3e-05 | 16/27 (NCI-H460, LoVo, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.472×** | -4.7 | 2e-04 | 12/28 (NCI-H460, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.679×** | -4.7 | 2e-04 | 14/28 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.687×** | -4.5 | 3e-04 | 17/28 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.694×** | -4.2 | 0.001 | 16/27 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **0.708×** | -4.2 | 0.001 | 18/26 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.791×** | -4.0 | 0.003 | 13/28 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.577×** | -3.5 | 0.020 | 9/28 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.756×** | -3.4 | 0.027 | 11/28 (NCI-H2030, NCI-H1573, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.780×** | -3.0 | 0.084 | 11/28 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.2 | 0 | 23 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -18.9) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0689× (z -17.4) |
| [[A549 (line)]] | wt | 70.1 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -20.4) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.143× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 84.9 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.302× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 83.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.6) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SNU-423 (line)]] | alt | 53.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.8) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SW1417 (line)]] | alt | 66.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.6) ⚠ cell-cycle shift, explains ~92% of this change |
| [[CFPAC-1 (line)]] | alt | 73.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[COLO 205 (line)]] | alt | 68.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[H4 (line)]] | wt | 41.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -15.8) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.171× (z -8.6) |
| [[HT-29 (line)]] | alt | 79.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.88× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[LS 180 (line)]] | wt | 43.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.169× (z -11.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0951× (z -9.0) |
| [[J82 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[LoVo (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H1573 (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0865× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 9.64 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.98× (z +9.5) | — |
| [[A-172 (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.49 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAC4]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[CRLF2]] | +0.54 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[GTF2IP7]] | +0.50 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[DUOX2]] | +0.49 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[LUCAT1]] | +0.49 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[RDH10]] | +0.49 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[SERPINB11]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[MAF]] | +0.48 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[VNN1]] | +0.48 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[MBP]] | +0.48 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[AADACL2-AS1]] | +0.48 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[CD55]] | +0.47 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTBP2]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ARMC8]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[TADA2A]] | -0.47 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[USP24]] | -0.47 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[LSM14A]] | -0.47 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[DCAF17]] | -0.46 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[TLK1]] | -0.46 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ACBD6]] | -0.45 | -0.44 / -0.40 | both halves | 4e-05 | same gene group |
| [[EIF2AK4]] | -0.45 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[HOXC4]] | -0.45 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[FAR2P1]] | -0.44 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[IMMT]] | -0.44 | -0.28 / -0.40 | both halves | 3e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A4]] | B | SLC16A4 activity raises GABRE's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without SLC16A4 | 0.011 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[DUOX2]] | B | DUOX2 activity raises GABRE's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 3.42× lower at baseline in the lines without DUOX2 | 0.015 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[VNN1]] | B | VNN1 activity raises GABRE's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without VNN1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[SMOX]] | B | SMOX activity raises GABRE's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.31× lower at baseline in the lines without SMOX | 0.060 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[SERPIND1]] | B | SERPIND1 activity raises GABRE's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without SERPIND1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[OSMR-DT]] | B | OSMR-DT activity raises GABRE's level | lines that do not express OSMR-DT (15) vs lines expressing it (35) | 1.53× lower at baseline in the lines without OSMR-DT | 0.070 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: OSMR, LIFR, IL1R1 |
| [[CASP10]] | B | CASP10 activity raises GABRE's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without CASP10 | 0.078 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[RAB27B]] | B | RAB27B activity raises GABRE's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.71× lower at baseline in the lines without RAB27B | 0.079 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[BSN]] | B | BSN activity lowers GABRE's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.82× higher at baseline in the lines without BSN | 0.083 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[AADACP1]] | B | AADACP1 activity raises GABRE's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.19× lower at baseline in the lines without AADACP1 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[SDCBP2]] | B | SDCBP2 activity raises GABRE's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 3.14× lower at baseline in the lines without SDCBP2 | 0.090 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[IGFBP1]] | C | IGFBP1 activity raises GABRE's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 5.03× lower at baseline in the lines without IGFBP1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM107B]] | B | GABRE activity raises FAM107B's level | lines that do not express GABRE (20) vs lines expressing it (30) | 3.05× lower at baseline in the lines without GABRE | 0.008 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[SLC16A4]] | B | GABRE activity raises SLC16A4's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without GABRE | 0.023 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[LARS1]] | B | GABRE activity lowers LARS1's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.44× higher at baseline in the lines without GABRE | 0.026 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[SDCBP2]] | B | GABRE activity raises SDCBP2's level | lines that do not express GABRE (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without GABRE | 0.036 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | GABRE activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express GABRE (20) vs lines expressing it (28) | the lines without GABRE: 0.82× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[OSMR-DT]] | B | GABRE activity raises OSMR-DT's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without GABRE | 0.061 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[NIPSNAP2]] | B | GABRE activity lowers NIPSNAP2's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.35× higher at baseline in the lines without GABRE | 0.062 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | GABRE activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express GABRE (20) vs lines expressing it (28) | the lines without GABRE: 1.24× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[TAFAZZIN]] | B | GABRE activity lowers TAFAZZIN's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.19× higher at baseline in the lines without GABRE | 0.079 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| cells under [[Terfenadine (drug)]] 5 µM | B | GABRE activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express GABRE (20) vs lines expressing it (28) | the lines without GABRE: 0.91× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[VNN1]] | B | GABRE activity raises VNN1's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.98× lower at baseline in the lines without GABRE | 0.081 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| cells under [[Terfenadine (drug)]] 0.5 µM | B | GABRE activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express GABRE (20) vs lines expressing it (28) | the lines without GABRE: 0.80× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.380). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, 16.9); signed map (19.6, 54.0). **Vector** length 81.5, 21.1% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.5 | +0.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.5 | -0.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.7 | -9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.3 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -6.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type A receptor subunit epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:151,953,124-151,974,680 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gamma-aminobutyric acid type A receptor subunits; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P78334](https://www.uniprot.org/uniprotkb/P78334) (Gamma-aminobutyric acid receptor subunit epsilon):

> Epsilon subunit of the heteropentameric ligand-gated chloride channel gated by gamma-aminobutyric acid (GABA), a major inhibitory neurotransmitter in the brain. GABA-gated chloride channels, also named GABA(A) receptors (GABAAR), consist of five subunits arranged around a central pore and contain GABA active binding site(s) located at the alpha and beta subunit interfaces (By similarity). When activated by GABA, GABAARs selectively allow the flow of chloride anions across the cell membrane down …

**Summary**, from NCBI Gene [2564](https://www.ncbi.nlm.nih.gov/gene/2564):

> The product of this gene belongs to the ligand-gated ionic channel (TC 1.A.9) family. It encodes the gamma-aminobutyric acid (GABA) A receptor which is a multisubunit chloride channel that mediates the fastest inhibitory synaptic transmission in the central nervous system. This gene encodes an epsilon subunit. It is mapped to chromosome Xq28 in a cluster comprised of genes encoding alpha 3, beta 4 and theta subunits of the same receptor. Alternatively spliced transcript variants have been …

**Accessions** — [HGNC:4085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4085) · Entrez [2564](https://www.ncbi.nlm.nih.gov/gene/2564) · UniProt [P78334](https://www.uniprot.org/uniprotkb/P78334) · Ensembl [ENSG00000102287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102287)

## Data

Gene col 2233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2233); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2233]; `tensor/DDL_lfc|DDL_z.npy` [2233]; `embed/gene_vectors.npy` [2233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2233 or target_col == 2233). Every well: [[GABRE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABRE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
