---
symbol: "CAMK1"
type: "gene"
col: 5507
ensembl_id: "ENSG00000134072"
name: "calcium/calmodulin dependent protein kinase I"
location: "3p25.3"
module: 15
arm: "-"
pooled_cpm: 5.58
n_lines_expressing: 42
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CAMK1

*calcium/calmodulin dependent protein kinase I* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.06× (z +9.3, q 5e-18, up in 16 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +6.7, q 2e-09, up in 13 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.523× (z -11.9, q 8e-30, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOCS1]] (+0.55, fdr 3e-05), [[CHST10]] (+0.54, fdr 5e-05), [[WDR11]] (+0.53, fdr 4e-04); moves opposite to [[ZBTB11]] (-0.50, fdr 2e-04), [[ZCWPW2]] (-0.47, fdr 1e-04), [[PKN2-AS1]] (-0.47, fdr 2e-04).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CLOCK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +9.3 | 5e-18 | 16/25 (A549, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +7.5 | 3e-11 | 8/11 (NCI-H2030, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +6.9 | 1e-09 | 9/16 (MIA PaCa-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +6.7 | 2e-09 | 13/36 (HS-578T, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +4.4 | 0.001 | 12/37 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.57×** | +4.2 | 0.003 | 2/20 (SW1417, HEC-1-A) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.5 | 0.042 | 2/14 (SW1417, SW480) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.044 | 1/34 (RKO) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.4 | 0.046 | 1/20 (A549) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.057 | 6/28 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.2 | 0.062 | 4/25 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.076 | 2/35 (SW 900, A-172) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +3.1 | 0.077 | 6/36 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.077 | 3/33 (RKO, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.077 | 3/35 (RKO, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.523×** | -11.9 | 8e-30 | 26/32 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.700×** | -6.6 | 2e-08 | 18/34 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -5.5 | 6e-06 | 17/33 (hTERT-HPNE, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.684×** | -4.9 | 1e-04 | 15/36 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.696×** | -4.7 | 3e-04 | 14/38 (RKO, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.705×** | -4.5 | 5e-04 | 13/37 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.735×** | -4.0 | 0.005 | 8/38 (KATO III, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -3.9 | 0.006 | 10/35 (A-427, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.051 | 11/33 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -3.3 | 0.056 | 13/38 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.772×** | -3.2 | 0.077 | 6/36 (SW480, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.50 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0790× (z -9.4) ⚠ toxic |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 5.36 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 9.20 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 5.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -8.7) |
| [[RKO (line)]] | wt | 16.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 8.69 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0801× (z -10.2) |
| [[SW48 (line)]] | wt | 12.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -8.8) |
| [[SW480 (line)]] | alt | 5.34 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -8.5) |
| [[A-172 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOCS1]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[CHST10]] | +0.54 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[WDR11]] | +0.53 | +0.24 / +0.60 | both halves | 4e-04 |  |
| [[ECHDC3]] | +0.53 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SLC29A1]] | +0.50 | +0.37 / +0.45 | both halves | 7e-05 |  |
| [[LRRC8B]] | +0.49 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[SAAL1]] | +0.49 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[PGBD1]] | +0.49 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[AADAT]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[COMMD2]] | +0.49 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[NAA40]] | +0.48 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[SEMA4F]] | +0.48 | +0.44 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB11]] | -0.50 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[ZCWPW2]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | -0.47 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[PELO-AS1]] | -0.47 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[LINC01135]] | -0.47 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[KIAA2026]] | -0.47 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[CFAP418-AS1]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[DNASE1]] | -0.46 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[SAXO1]] | -0.46 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[ALOX12-AS1]] | -0.46 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[PSMD7-DT]] | -0.45 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[PPP1R15B-AS1]] | -0.45 | -0.31 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CAMK1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PTPN20]] | B | PTPN20 activity raises CAMK1's level | lines that do not express PTPN20 (28) vs lines expressing it (22) | 1.54× lower at baseline in the lines without PTPN20 | 0.079 | ⚠ within organs, on part of the lines; also absent: TSPYL5, ENSG00000234426, GPR141 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLOCK]] | B | CAMK1 activity lowers CLOCK's level | lines that do not express CAMK1 (8) vs lines expressing it (42) | 1.44× higher at baseline in the lines without CAMK1 | 0.059 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.242). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-36.3, 23.7); signed map (-24.6, -16.2). **Vector** length 44.3, 5.91% of its response variance represented; |z| ≥ 3 in 651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +3.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.6 | -11.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,757,347-9,769,992 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CaMKI, CaMKI-alpha |
| Gene groups (HGNC) | CAMK1 family |
| Reactome | 7 pathways, smallest: Activation of RAC1 downstream of NMDARs; Negative regulation of NMDA receptor-mediated neuronal transmission; Post NMDA receptor activation events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14012](https://www.uniprot.org/uniprotkb/Q14012) (Calcium/calmodulin-dependent protein kinase type 1):

> Calcium/calmodulin-dependent protein kinase that operates in the calcium-triggered CaMKK-CaMK1 signaling cascade and, upon calcium influx, regulates transcription activators activity, cell cycle, hormone production, cell differentiation, actin filament organization and neurite outgrowth. Recognizes the substrate consensus sequence [MVLIF]-x-R-x(2)-[ST]-x(3)-[MVLIF]. Regulates axonal extension and growth cone motility in hippocampal and cerebellar nerve cells. Upon NMDA receptor-mediated Ca(2+) …

**Summary**, from NCBI Gene [8536](https://www.ncbi.nlm.nih.gov/gene/8536):

> Calcium/calmodulin-dependent protein kinase I is expressed in many tissues and is a component of a calmodulin-dependent protein kinase cascade. Calcium/calmodulin directly activates calcium/calmodulin-dependent protein kinase I by binding to the enzyme and indirectly promotes the phosphorylation and synergistic activation of the enzyme by calcium/calmodulin-dependent protein kinase I kinase. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1459) · Entrez [8536](https://www.ncbi.nlm.nih.gov/gene/8536) · UniProt [Q14012](https://www.uniprot.org/uniprotkb/Q14012) · Ensembl [ENSG00000134072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134072)

## Data

Gene col 5507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5507); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5507]; `tensor/DDL_lfc|DDL_z.npy` [5507]; `embed/gene_vectors.npy` [5507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5507 or target_col == 5507). Every well: [[CAMK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
