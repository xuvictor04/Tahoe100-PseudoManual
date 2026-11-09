---
symbol: "AGMAT"
type: "gene"
col: 3837
ensembl_id: "ENSG00000116771"
name: "agmatinase (putative)"
location: "1p36.21"
module: 4
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 39
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# AGMAT

*agmatinase (putative)* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 10.1× (z +17.5, q 0e+00, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 3.69× (z +10.3, q 1e-22, up in 11 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.700× (z -4.0, q 0.030, down in 11 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.05 µM in 2 lines (LoVo 0.0829×, RKO 0.163×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0572×); [[Belinostat (drug)]] 0.5 µM in 1 line (RKO 0.0654×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.179×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01357]] (+0.71, fdr 7e-06), [[CTSE]] (+0.62, fdr 1e-05), [[ALDH1B1]] (+0.61, fdr 7e-06); moves opposite to [[DAAM1]] (-0.48, fdr 5e-05), [[LGALS1]] (-0.46, fdr 2e-04), [[ARL3]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[MTARC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.1×** | +17.5 | 0e+00 | 2/2 (HepG2/C3A, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.66×** | +14.9 | 0e+00 | 10/10 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.29×** | +12.1 | 1e-31 | 6/6 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.69×** | +10.3 | 1e-22 | 11/21 (NCI-H460, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +8.0 | 2e-13 | 8/20 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +6.6 | 4e-09 | 5/10 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.19×** | +6.2 | 5e-08 | 5/9 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +6.2 | 5e-08 | 6/22 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +6.1 | 7e-08 | 14/30 (HepG2/C3A, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.83×** | +4.6 | 2e-04 | 3/14 (LoVo, AsPC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.01×** | +4.5 | 3e-04 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.3 | 8e-04 | 1/30 (NCI-H1792) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.004 | 9/21 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.95×** | +3.8 | 0.007 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.61×** | +3.7 | 0.007 | 1/19 (RKO) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.077 | 6/31 (SW1417, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3837.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.05 µM in 2 lines (LoVo 0.0829×, RKO 0.163×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0572×); [[Belinostat (drug)]] 0.5 µM in 1 line (RKO 0.0654×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.179×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.700×** | -4.0 | 0.030 | 11/31 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ciclopirox (drug)]] 5 µM |  | **0.705×** | -3.9 | 0.030 | 8/20 (SW1417, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | 0.627× | -3.3 | 0.18 | 6/33 (LoVo, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.642× | -3.2 | 0.18 | 2/31 (NCI-H23, SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 12.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0572× (z -13.8) |
| [[LoVo (line)]] | wt | 4.46 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.05 µM 0.0829× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 7.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -8.8) |
| [[A-172 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.590 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.581 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.868 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.885 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.637 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.809 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.636 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.616 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.657 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01357]] | +0.71 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[CTSE]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ALDH1B1]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MTARC1]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[XK]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ACY1]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SPTBN2]] | +0.57 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[CENPV]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PALD1]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SLC38A5]] | +0.56 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[LAD1]] | +0.55 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAAM1]] | -0.48 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[LGALS1]] | -0.46 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ARL3]] | -0.45 | -0.46 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AGMAT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GAL]] | B | GAL activity raises AGMAT's level | lines that do not express GAL (27) vs lines expressing it (23) | 1.38× lower at baseline in the lines without GAL | 0.052 | ⚠ within organs, on part of the lines; also absent: HEYL, ACP7, SEC14L4 |
| [[LINC01357]] | B | LINC01357 activity raises AGMAT's level | lines that do not express LINC01357 (24) vs lines expressing it (26) | 1.39× lower at baseline in the lines without LINC01357 | 0.092 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, PLBD1, SYN2 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTARC1]] | B | AGMAT activity raises MTARC1's level | lines that do not express AGMAT (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without AGMAT | 0.077 | ⚠ within organs, on part of the lines; also absent: ETV7, LYPD5, TNK1; maybe low, not absent |
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM | B | AGMAT activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express AGMAT (11) vs lines expressing it (37) | the lines without AGMAT: 0.71× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ETV7, LYPD5, TNK1; maybe low, not absent |
| [[LAD1]] | B | AGMAT activity raises LAD1's level | lines that do not express AGMAT (11) vs lines expressing it (39) | 3.62× lower at baseline in the lines without AGMAT | 0.086 | ⚠ within organs, on part of the lines; also absent: ETV7, LYPD5, TNK1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.3, 43.6); signed map (-5.2, -58.8). **Vector** length 43.1, 7.74% of its response variance represented; |z| ≥ 3 in 617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +14.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.9 | +0.8 |
| fall | [[Artesunate (drug)]] 5 µM |  | -1.4 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | agmatinase (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,571,699-15,585,051 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23384 |
| Reactome | 2 pathways, smallest: Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSE5](https://www.uniprot.org/uniprotkb/Q9BSE5) (Guanidino acid hydrolase, mitochondrial):

> Hydrolyzes linear guanidino acids to form urea and the corresponding amines. Displays specificity for substrates having a negatively charged head group and short chains including taurocyamine, guanidino propanoic and butanoic acids. May protect cells by detoxifying potentially harmful amounts of guanidino acids. Metabolizes L-arginine with low efficiency.

**Summary**, from NCBI Gene [79814](https://www.ncbi.nlm.nih.gov/gene/79814):

> Enables arginase activity; guanidinobutyrase activity; and guanidinopropionase activity. Predicted to be involved in putrescine biosynthetic process from arginine, via agmatine. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18407) · Entrez [79814](https://www.ncbi.nlm.nih.gov/gene/79814) · UniProt [Q9BSE5](https://www.uniprot.org/uniprotkb/Q9BSE5) · Ensembl [ENSG00000116771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116771)

## Data

Gene col 3837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3837); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3837]; `tensor/DDL_lfc|DDL_z.npy` [3837]; `embed/gene_vectors.npy` [3837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3837 or target_col == 3837). Every well: [[AGMAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGMAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
