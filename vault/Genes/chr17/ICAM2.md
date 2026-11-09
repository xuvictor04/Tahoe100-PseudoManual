---
symbol: "ICAM2"
type: "gene"
col: 2978
ensembl_id: "ENSG00000108622"
name: "intercellular adhesion molecule 2"
location: "17q23.3"
module: 158
arm: "+"
pooled_cpm: 2.01
n_lines_expressing: 27
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 13
direction_downstream: 14
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# ICAM2

*intercellular adhesion molecule 2* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.72× (z +16.0, q 0e+00, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.578× (z -4.0, q 0.032, down in 7 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.0833×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL2RG]] (+0.70, fdr 1e-05), [[IL23A]] (+0.65, fdr 1e-05), [[LINC00460]] (+0.65, fdr 7e-06); moves opposite to [[GLB1]] (-0.56, fdr 2e-05), [[RABL6]] (-0.51, fdr 6e-05), [[CTSD]] (-0.50, fdr 5e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 14 go from it, the strongest it → [[MAST4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.72×** | +16.0 | 0e+00 | 8/20 (HOP62, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.48×** | +12.8 | 4e-35 | 12/19 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +9.1 | 2e-17 | 1/10 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +8.4 | 1e-14 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +6.5 | 7e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +5.2 | 2e-05 | 1/10 (AsPC-1) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +5.0 | 4e-05 | 9/23 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +4.4 | 9e-04 | 2/7 (KATO III, NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.2 | 0.002 | 1/14 (KATO III) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.003 | 0/25 | rises with dose | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.18×** | +4.0 | 0.003 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.003 | 1/21 (hTERT-HPNE) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.005 | 6/25 (SW 900, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.8 | 0.007 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +3.6 | 0.012 | 8/21 (hTERT-HPNE, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.026 | 0/17 | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.057 | 10/25 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.064 | 1/13 (J82) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2978.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.0833×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.578×** | -4.0 | 0.032 | 7/25 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.621× | -3.3 | 0.26 | 5/25 (HepG2/C3A, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.656× | -3.1 | 0.26 | 13/23 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | 0.744× | -3.1 | 0.26 | 9/25 (LS 180, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0833× (z -12.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 5.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.0) | — |
| [[A-172 (line)]] | wt | 0.184 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.746 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.613 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.201 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.188 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.669 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.597 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL2RG]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 | same gene group |
| [[IL23A]] | +0.65 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LINC00460]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PPP1R1C]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[GOLGA7B]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SHH]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SFR1]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CYB5R2]] | +0.59 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[EPHA2]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SLC45A3]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NEMP2-DT]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[MTNR1A]] | +0.58 | +0.63 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[RABL6]] | -0.51 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[CTSD]] | -0.50 | -0.50 / -0.39 | both halves | 5e-05 | pathway: Affinity selection of immunoglobulins |
| [[CLASP1]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ABHD12]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[AP2A1]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises ICAM2's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without C6orf141 | 0.015 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[PALD1]] | B | PALD1 activity lowers ICAM2's level | lines that do not express PALD1 (16) vs lines expressing it (34) | 1.51× higher at baseline in the lines without PALD1 | 0.044 | ⚠ within organs, on part of the lines; also absent: NKD2, ADRA2C, IGSF9B |
| [[GALNT8]] | B | GALNT8 activity lowers ICAM2's level | lines that do not express GALNT8 (6) vs lines expressing it (44) | 2.67× higher at baseline in the lines without GALNT8 | 0.081 | ⚠ within organs, on part of the lines; also absent: PRDM6, NOS1, C1orf21; maybe low, not absent |
| [[MAST4]] | B | MAST4 activity raises ICAM2's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without MAST4 | 0.089 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[IL1R2]] | B | IL1R2 activity raises ICAM2's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 1.49× lower at baseline in the lines without IL1R2 | 0.091 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[SCAT1]] | B | SCAT1 activity raises ICAM2's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.46× lower at baseline in the lines without SCAT1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[IL1A]] | B | IL1A activity raises ICAM2's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.33× lower at baseline in the lines without IL1A | 0.094 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[LAMB3]] | C | LAMB3 activity raises ICAM2's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.93× lower at baseline in the lines without LAMB3 | 0.021 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3; co-absent with the target |
| [[HLA-K]] | C | HLA-K activity raises ICAM2's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without HLA-K | 0.023 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325; co-absent with the target |
| [[GOLT1A]] | C | GOLT1A activity raises ICAM2's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.86× lower at baseline in the lines without GOLT1A | 0.036 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent; co-absent with the target |
| [[TFF1]] | C | TFF1 activity raises ICAM2's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.11× lower at baseline in the lines without TFF1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC; co-absent with the target |
| [[LAMC2]] | C | LAMC2 activity raises ICAM2's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without LAMC2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAST4]] | B | ICAM2 activity raises MAST4's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 3.00× lower at baseline in the lines without ICAM2 | 0.010 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[DIAPH2-AS1]] | B | ICAM2 activity raises DIAPH2-AS1's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.77× lower at baseline in the lines without ICAM2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[LETM2]] | B | ICAM2 activity raises LETM2's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.28× lower at baseline in the lines without ICAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[VSIG1]] | B | ICAM2 activity raises VSIG1's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without ICAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[LINC02405]] | B | ICAM2 activity raises LINC02405's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without ICAM2 | 0.036 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[PLB1]] | B | ICAM2 activity raises PLB1's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without ICAM2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[LPAR5]] | B | ICAM2 activity raises LPAR5's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without ICAM2 | 0.054 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[PALD1]] | B | ICAM2 activity lowers PALD1's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.23× higher at baseline in the lines without ICAM2 | 0.066 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[CEMIP]] | B | ICAM2 activity raises CEMIP's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without ICAM2 | 0.081 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[IL1R2]] | B | ICAM2 activity raises IL1R2's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without ICAM2 | 0.086 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[ARHGAP27]] | B | ICAM2 activity strengthens ARHGAP27's drug response | lines that do not express ICAM2 (20) vs lines expressing it (24) | the lines without ICAM2 respond 0.84× as strongly (z diff +0.18); rises at some drug-doses, falls at others (42% from rises): TAK-901 5 µM: 0.69x vs 0.45x (z diff +1.9); Filgotinib 5 µM: 1.05x vs 1.30x (z diff +1.0); NG25 5 µM: 0.68x vs 0.60x (z diff +0.9) | 0.086 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[LAMB3]] | C | ICAM2 activity raises LAMB3's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 5.00× lower at baseline in the lines without ICAM2 | 0.014 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.5, 1.3); signed map (8.0, 38.9). **Vector** length 34.8, 5.56% of its response variance represented; |z| ≥ 3 in 518 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +16.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +4.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.3 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.0 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | intercellular adhesion molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:64,002,594-64,020,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD102 |
| Gene groups (HGNC) | CD molecules; Receptor ligands; Immunoglobulin like domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 9 pathways, smallest: CD209 (DC-SIGN) signaling; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Integrin cell surface interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P13598](https://www.uniprot.org/uniprotkb/P13598) (Intercellular adhesion molecule 2):

> Cell adhesion molecule that functions as a receptor ligand of the signaling receptor ITGAL:ITGB2/LFA-1 (lymphocyte-function associated (LFA) molecule 1) ensuring leukocyte cell-cell adhesion on resting cells. Also endothelial blood vessels receptor ligand of dendritic cell (DC) CD209 signaling receptor that mediates triggering transendothelial migration of DC presursors from blood into peripheral tissues and, subsequently, into lymphoid tissues. Mediates adhesive interactions important for …

**Summary**, from NCBI Gene [3384](https://www.ncbi.nlm.nih.gov/gene/3384):

> The protein encoded by this gene is a member of the intercellular adhesion molecule (ICAM) family. All ICAM proteins are type I transmembrane glycoproteins, contain 2-9 immunoglobulin-like C2-type domains, and bind to the leukocyte adhesion LFA-1 protein. This protein may play a role in lymphocyte recirculation by blocking LFA-1-dependent cell adhesion. It mediates adhesive interactions important for antigen-specific immune response, NK-cell mediated clearance, lymphocyte recirculation, and …

**Accessions** — [HGNC:5345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5345) · Entrez [3384](https://www.ncbi.nlm.nih.gov/gene/3384) · UniProt [P13598](https://www.uniprot.org/uniprotkb/P13598) · Ensembl [ENSG00000108622](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108622)

## Data

Gene col 2978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2978); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2978]; `tensor/DDL_lfc|DDL_z.npy` [2978]; `embed/gene_vectors.npy` [2978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2978 or target_col == 2978). Every well: [[ICAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
