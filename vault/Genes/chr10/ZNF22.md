---
symbol: "ZNF22"
type: "gene"
col: 9136
ensembl_id: "ENSG00000165512"
name: "zinc finger protein 22"
location: "10q11.21"
module: 16
arm: "+"
pooled_cpm: 10.63
n_lines_expressing: 45
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF22

*zinc finger protein 22* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.76× (z +7.5, q 4e-11, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.420× (z -16.2, q 0e+00, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL9]] (+0.81, fdr 7e-06), [[KBTBD6]] (+0.73, fdr 7e-06), [[MSL3P1]] (+0.69, fdr 7e-06); moves opposite to [[MBOAT7]] (-0.60, fdr 1e-05), [[ZFYVE27]] (-0.60, fdr 1e-05), [[SAP30L-AS1]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SOGA3]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Thymol (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.5 | 4e-11 | 32/42 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +6.9 | 2e-09 | 21/40 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +5.2 | 4e-05 | 20/43 (PANC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.0 | 7e-05 | 17/34 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.38×** | +4.2 | 0.003 | 14/36 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.008 | 16/43 (A498, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.039 | 7/42 (H4, HT-29, …) | top dose only | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.083 | 13/42 (HS-578T, HOP62, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.19× | +3.2 | 0.083 | 8/43 (hTERT-HPNE, NCI-H23, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.083 | 7/35 (SNU-423, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | 1.27× | +3.0 | 0.13 | 6/40 (SW1417, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.420×** | -16.2 | 0e+00 | 32/39 (J82, Hs 766T, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -6.1 | 3e-07 | 24/38 (hTERT-HPNE, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -5.8 | 1e-06 | 24/39 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.653×** | -5.6 | 3e-06 | 22/42 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.670×** | -5.0 | 6e-05 | 21/42 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.733×** | -4.1 | 0.004 | 15/42 (PANC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.753×** | -3.8 | 0.014 | 13/41 (CHP-212, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -3.6 | 0.021 | 15/40 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 5 µM |  | **0.833×** | -3.4 | 0.041 | 9/43 (SNU-1, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -10.5) |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.4) |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.8) |
| [[A-172 (line)]] | wt | 4.84 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0904× (z -9.3) |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0942× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.6) |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -8.6) |
| [[Hs 766T (line)]] | wt | 7.54 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0942× (z -14.1) |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0752× (z -12.8) |
| [[J82 (line)]] | alt | 16.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 8.65 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 19.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -13.3) |
| [[RKO (line)]] | wt | 13.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -10.2) |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -12.3) |
| [[SW480 (line)]] | alt | 8.54 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.8) |
| [[A-427 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.862 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL9]] | +0.81 | +0.72 / +0.83 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.73 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[MSL3P1]] | +0.69 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[KAT14]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[FANCF]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[ISCA2]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[N6AMT1]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.64 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ZFP1]] | +0.63 | +0.45 / +0.67 | both halves | 3e-05 | same gene group |
| [[NUDT12]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[C12orf29]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.60 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[ZFYVE27]] | -0.60 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | -0.57 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[PPP1R15B-AS1]] | -0.56 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[METTL21A]] | -0.56 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SLC25A53]] | -0.55 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[CCNO-DT]] | -0.55 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[ATXN7L3-AS1]] | -0.54 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[MTCH1]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[ZNF213-AS1]] | -0.53 | -0.16 / -0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[GNAS]] | -0.53 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[EOGT-DT]] | -0.52 | -0.36 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOGA3]] | B | SOGA3 activity raises ZNF22's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.61× lower at baseline in the lines without SOGA3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[KIAA0408]] | B | KIAA0408 activity raises ZNF22's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 1.51× lower at baseline in the lines without KIAA0408 | 0.031 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1 |
| [[TOP2A]] | B | TOP2A activity raises ZNF22's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RASSF4]] | B | RASSF4 activity raises ZNF22's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without RASSF4 | 0.086 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Thymol (drug)]] 0.5 µM | B | ZNF22 activity raises the cells' numbers under Thymol 0.5 µM (protects the cells) | lines that do not express ZNF22 (5) vs lines expressing it (43) | the lines without ZNF22: 0.74× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: DAB2IP, CAPN5 |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.2, -0.9); signed map (-1.1, -28.5). **Vector** length 73.7, 13.7% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.7 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -16.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.5 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:45,000,923-45,005,326 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX15, HKR-T1, ZNF422, Zfp422 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P17026](https://www.uniprot.org/uniprotkb/P17026) (Zinc finger protein 22):

> Binds DNA through the consensus sequence 5'-CAATG-3'. May be involved in transcriptional regulation and may play a role in tooth formation (By similarity).

**Summary**, from NCBI Gene [7570](https://www.ncbi.nlm.nih.gov/gene/7570):

> Predicted to enable DNA binding activity. Predicted to be involved in regulation of gene expression. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13012) · Entrez [7570](https://www.ncbi.nlm.nih.gov/gene/7570) · UniProt [P17026](https://www.uniprot.org/uniprotkb/P17026) · Ensembl [ENSG00000165512](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165512)

## Data

Gene col 9136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9136); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9136]; `tensor/DDL_lfc|DDL_z.npy` [9136]; `embed/gene_vectors.npy` [9136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9136 or target_col == 9136). Every well: [[ZNF22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
