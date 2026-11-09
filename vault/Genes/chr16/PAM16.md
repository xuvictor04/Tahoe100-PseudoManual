---
symbol: "PAM16"
type: "gene"
col: 13289
ensembl_id: "ENSG00000217930"
name: "presequence translocase associated motor 16"
location: "16p13.3"
module: 18
arm: "+"
pooled_cpm: 21.14
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PAM16

*presequence translocase associated motor 16* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.90× (z +14.0, q 6e-42, up in 40 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +7.2, q 1e-10, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.653× (z -6.3, q 2e-07, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCLY]] (+0.66, fdr 7e-06), [[RILPL1]] (+0.65, fdr 8e-06), [[RABEPK]] (+0.65, fdr 1e-05); moves opposite to [[ENPP1]] (-0.57, fdr 3e-05), [[SF3B1]] (-0.56, fdr 3e-05), [[ATP7A]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LNX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.90×** | +14.0 | 6e-42 | 40/42 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +12.5 | 2e-33 | 28/31 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +7.3 | 5e-11 | 28/37 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +7.2 | 1e-10 | 37/48 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +6.9 | 5e-10 | 38/45 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.4 | 8e-04 | 28/47 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.4 | 0.001 | 28/46 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.70×** | +3.9 | 0.007 | 28/45 (C-33 A, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.007 | 23/46 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.62×** | +3.5 | 0.024 | 18/46 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.042 | 19/44 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.065 | 15/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.2 | 0.071 | 22/46 (HepG2/C3A, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.653×** | -6.3 | 2e-07 | 35/47 (SNU-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -5.0 | 1e-04 | 33/48 (SNU-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.640×** | -4.6 | 7e-04 | 30/48 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.393×** | -4.5 | 0.001 | 29/44 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 21.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.45× (z +14.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 25.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +9.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 29.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 23.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.98× (z +14.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.22× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0936× (z -9.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.89× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.6) |
| [[SW 900 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.96× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCLY]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[RILPL1]] | +0.65 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[RABEPK]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[DCUN1D5]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NDUFAF2]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ARIH2]] | +0.58 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[NOPCHAP1]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PEMT]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PUS7]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CAPN15]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MACROD1]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENPP1]] | -0.57 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SF3B1]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ATP7A]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[EID1]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[VEZF1]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[TTC30A]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[PABIR1]] | -0.51 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[H2AZ2]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ZNF184]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[BHLHE41]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CUL4B]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[DUSP19]] | -0.49 | -0.38 / -0.48 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNX1]] | B | LNX1 activity lowers PAM16's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.36× higher at baseline in the lines without LNX1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[TOP2A]] | B | TOP2A activity lowers PAM16's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PRELID3A]] | C | PRELID3A activity raises PAM16's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without PRELID3A | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31 |
| [[MTHFD1L]] | C | MTHFD1L activity raises PAM16's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without MTHFD1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.2, -17.9); signed map (-43.4, -19.4). **Vector** length 63.0, 13.2% of its response variance represented; |z| ≥ 3 in 650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | presequence translocase associated motor 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,331,549-4,355,607 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Magmas, Tim16, TIMM16 |
| Gene groups (HGNC) | TIM23 complex |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3D7](https://www.uniprot.org/uniprotkb/Q9Y3D7) (Mitochondrial import inner membrane translocase subunit TIM16):

> Regulates ATP-dependent protein translocation into the mitochondrial matrix. Inhibits DNAJC19 stimulation of HSPA9/Mortalin ATPase activity.

**Summary**, from NCBI Gene [51025](https://www.ncbi.nlm.nih.gov/gene/51025):

> This gene encodes a mitochondrial protein involved in granulocyte-macrophage colony-stimulating factor (GM-CSF) signaling. This protein also plays a role in the import of nuclear-encoded mitochondrial proteins into the mitochondrial matrix and may be important in reactive oxygen species (ROS) homeostasis. Mutations in this gene cause Megarbane-Dagher-Melike type spondylometaphyseal dysplasia, an early lethal skeletal dysplasia characterized by short stature, developmental delay and other …

**Accessions** — [HGNC:29679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29679) · Entrez [51025](https://www.ncbi.nlm.nih.gov/gene/51025) · UniProt [Q9Y3D7](https://www.uniprot.org/uniprotkb/Q9Y3D7) · Ensembl [ENSG00000217930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000217930)

## Data

Gene col 13289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13289); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13289]; `tensor/DDL_lfc|DDL_z.npy` [13289]; `embed/gene_vectors.npy` [13289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13289 or target_col == 13289). Every well: [[PAM16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAM16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
