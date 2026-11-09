---
symbol: "MTCP1"
type: "gene"
col: 13227
ensembl_id: "ENSG00000214827"
name: "mature T cell proliferation 1"
location: "Xq28"
module: 21
arm: "+"
pooled_cpm: 5.2
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MTCP1

*mature T cell proliferation 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +9.0, q 2e-16, up in 13 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +8.7, q 1e-15, up in 20 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.871× (z -5.7, q 5e-06, down in 20 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.626× (z -5.5, q 9e-06, down in 17 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPOAP1-AS1]] (+0.59, fdr 1e-05), [[SGCD]] (+0.59, fdr 3e-05), [[SLC23A1]] (+0.58, fdr 1e-05); moves opposite to [[UBL4A]] (-0.49, fdr 7e-05), [[ARHGEF4]] (-0.48, fdr 2e-04), [[ARMC9]] (-0.48, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[DIRC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +9.0 | 2e-16 | 13/26 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.7 | 1e-15 | 20/39 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.6 | 5e-12 | 5/10 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +5.8 | 1e-06 | 20/42 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.004 | 8/36 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.004 | 10/44 (HepG2/C3A, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.0 | 0.006 | 1/17 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.8 | 0.012 | 8/29 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.023 | 11/46 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.040 | 5/39 (HCT15, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.057 | 7/44 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.057 | 7/38 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.076 | 13/45 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.078 | 8/45 (HOP62, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.29× | +3.0 | 0.10 | 7/45 (H4, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.871× | -5.7 | 5e-06 | 20/48 (SW480, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -5.5 | 9e-06 | 17/44 (LS 180, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.639×** | -5.1 | 7e-05 | 17/43 (LS 180, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.713×** | -3.9 | 0.017 | 7/44 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.749×** | -3.4 | 0.071 | 10/45 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.757×** | -3.3 | 0.096 | 15/38 (SHP-77, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.600× | -3.2 | 0.13 | 1/45 (CFPAC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 30.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0665× (z -15.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0676× (z -10.9) |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.136× (z -8.8) |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0850× (z -14.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0938× (z -9.7) |
| [[HCT15 (line)]] | alt | 9.87 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0539× (z -10.2) |
| [[HOP62 (line)]] | alt | 7.49 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -9.4) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 3.02 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0668× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -12.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-172 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPOAP1-AS1]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SGCD]] | +0.59 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[SLC23A1]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[FMO5]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CLVS1]] | +0.58 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[FLJ40194]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FAM217A]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ZBTB20-AS5]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[FAXDC2]] | +0.54 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[FAM13C]] | +0.54 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[ZRANB2-AS1]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[CNTN5]] | +0.53 | +0.45 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL4A]] | -0.49 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[ARHGEF4]] | -0.48 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[ARMC9]] | -0.48 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[C13orf46]] | -0.47 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[PSEN2]] | -0.47 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[ARHGDIA]] | -0.47 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[EEFSEC]] | -0.46 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[PXN]] | -0.46 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[SACS]] | -0.46 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[TOR4A]] | -0.46 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[IL17RD]] | -0.46 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[TAF1B]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3]] | B | DIRC3 activity raises MTCP1's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without DIRC3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[CA9]] | B | CA9 activity raises MTCP1's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without CA9 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[AK4P3]] | B | AK4P3 activity raises MTCP1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without AK4P3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[MAP2K1]] | B | MAP2K1 activity lowers MTCP1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers MTCP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DIRC3]] | B | DIRC3 activity strengthens MTCP1's drug response | lines that do not express DIRC3 (19) vs lines expressing it (29) | the lines without DIRC3 respond 1.02× as strongly (z diff -0.02); rises at some drug-doses, falls at others (74% from rises): Cobimetinib 5 µM: 1.15x vs 2.01x (z diff +2.0); Digitoxin 0.5 µM: 0.68x vs 0.52x (z diff +1.5); Harringtonine 5 µM: 0.77x vs 0.53x (z diff +1.4) | 0.066 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[AMBP]] | B | AMBP activity raises MTCP1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.48× lower at baseline in the lines without AMBP | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[FHOD3]] | B | FHOD3 activity lowers MTCP1's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 1.39× higher at baseline in the lines without FHOD3 | 0.096 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.0, 29.6); signed map (35.9, 8.0). **Vector** length 56.3, 7.40% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.9 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.8 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | mature T cell proliferation 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:155,064,034-155,147,937 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P13MTCP1, p8MTCP1, TCL1C |
| Matched by | ensembl_id |

**Function**, from UniProt [P56278](https://www.uniprot.org/uniprotkb/P56278) (Protein p13 MTCP-1):

> Enhances the phosphorylation and activation of AKT1 and AKT2.

**Summary**, from NCBI Gene [4515](https://www.ncbi.nlm.nih.gov/gene/4515):

> This gene was identified by involvement in some t(X;14) translocations associated with mature T-cell proliferations. This region has a complex gene structure, with a common promoter and 5' exon spliced to two different sets of 3' exons that encode two different proteins. This gene represents the upstream 13 kDa protein that is a member of the TCL1 family. This protein may be involved in leukemogenesis. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:7423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7423) · Entrez [4515](https://www.ncbi.nlm.nih.gov/gene/4515) · UniProt [P56278](https://www.uniprot.org/uniprotkb/P56278) · Ensembl [ENSG00000214827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214827)

## Data

Gene col 13227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13227); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13227]; `tensor/DDL_lfc|DDL_z.npy` [13227]; `embed/gene_vectors.npy` [13227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13227 or target_col == 13227). Every well: [[MTCP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTCP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
