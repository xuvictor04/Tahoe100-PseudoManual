---
symbol: "ZFHX2-AS1"
type: "gene"
col: 8058
ensembl_id: "ENSG00000157306"
name: "ZFHX2 antisense RNA 1"
location: "14q11.2"
module: 35
arm: "+"
pooled_cpm: 4.99
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ZFHX2-AS1

*ZFHX2 antisense RNA 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.28× (z +22.8, q 0e+00, up in 40 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H460 0.111×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.112×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIBAR1-DT]] (+0.83, fdr 7e-06), [[GLIPR1-AS1]] (+0.82, fdr 7e-06), [[SIAH2-AS1]] (+0.80, fdr 1e-05); moves opposite to [[PAFAH1B3]] (-0.69, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MSANTD3-TMEFF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.28×** | +22.8 | 0e+00 | 40/40 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.45×** | +14.1 | 2e-42 | 32/47 (BT-474, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.53×** | +14.0 | 2e-42 | 39/44 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +13.3 | 4e-38 | 31/43 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.30×** | +12.7 | 4e-35 | 31/35 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +9.6 | 8e-20 | 31/41 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +8.8 | 2e-16 | 14/27 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +8.3 | 1e-14 | 8/14 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +8.2 | 2e-14 | 2/7 (PANC-1, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.4 | 6e-12 | 21/41 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.53×** | +6.6 | 2e-09 | 19/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.65×** | +5.2 | 8e-06 | 16/42 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.58×** | +5.1 | 2e-05 | 18/45 (BT-474, PANC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.31×** | +4.3 | 8e-04 | 7/46 (BT-474, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.2 | 1e-03 | 10/23 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +3.7 | 0.007 | 9/43 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.057 | 3/44 (A498, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.072 | 4/43 (SK-MEL-2, Panc 03.27, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8058.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H460 0.111×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.575× | -3.2 | 0.42 | 7/36 (HepG2/C3A, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.760× | -3.1 | 0.42 | 8/48 (SHP-77, A-172, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.682× | -3.0 | 0.42 | 7/42 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.99 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.53× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 8.50 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +14.5) | — |
| [[LoVo (line)]] | wt | 4.71 | 2 | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 4.46 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +8.6) | [[Hydroxyurea (drug)]] 0.05 µM 0.111× (z -8.8) |
| [[SHP-77 (line)]] | alt | 8.32 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.112× (z -8.7) |
| [[C32 (line)]] | wt | 4.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.03× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 5.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 5.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 7.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 7.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 6.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.81× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 5.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +10.4) | — |
| [[A-172 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIBAR1-DT]] | +0.83 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[GLIPR1-AS1]] | +0.82 | +0.73 / +0.63 | both halves | 7e-06 | same gene group |
| [[SIAH2-AS1]] | +0.80 | +0.69 / +0.55 | both halves | 1e-05 | same gene group |
| [[MSH4]] | +0.80 | +0.80 / +0.54 | both halves | 1e-05 |  |
| [[C1S]] | +0.80 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[DENND6A-AS1]] | +0.79 | +0.80 / +0.60 | both halves | 7e-06 | same gene group |
| [[PSMD7-DT]] | +0.79 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.79 | +0.74 / +0.49 | both halves | 1e-05 | same gene group |
| [[LINC00880]] | +0.79 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.79 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[PTOV1-AS1]] | +0.78 | +0.67 / +0.67 | both halves | 7e-06 | same gene group |
| [[C2orf49-DT]] | +0.78 | +0.70 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B3]] | -0.69 | -0.51 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZFHX2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSANTD3-TMEFF1]] | C | ZFHX2-AS1's natural level weakens MSANTD3-TMEFF1's drug response | ZFHX2-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.03; direction clear | 0.020 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.9, 11.9); signed map (23.1, -2.9). **Vector** length 69.8, 10.9% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +22.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +14.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +12.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +9.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | +0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ZFHX2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q11.2 — chr14:23,511,760-23,560,778 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LncZFHX2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52658) · Entrez [109729160](https://www.ncbi.nlm.nih.gov/gene/109729160) · Ensembl [ENSG00000157306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157306)

## Data

Gene col 8058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8058); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8058]; `tensor/DDL_lfc|DDL_z.npy` [8058]; `embed/gene_vectors.npy` [8058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8058 or target_col == 8058). Every well: [[ZFHX2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFHX2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
