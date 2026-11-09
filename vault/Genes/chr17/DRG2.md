---
symbol: "DRG2"
type: "gene"
col: 2973
ensembl_id: "ENSG00000108591"
name: "developmentally regulated GTP binding protein 2"
location: "17p11.2"
module: 1
arm: "+"
pooled_cpm: 14.01
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DRG2

*developmentally regulated GTP binding protein 2* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +10.6, q 1e-23, up in 29 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.44× (z +6.2, q 1e-07, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.558× (z -14.1, q 4e-42, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKTN]] (+0.72, fdr 7e-06), [[WDR18]] (+0.72, fdr 7e-06), [[PRMT5]] (+0.70, fdr 7e-06); moves opposite to [[GNAS]] (-0.64, fdr 7e-06), [[PTMA]] (-0.56, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF583]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +10.6 | 1e-23 | 29/39 (HCT15, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +9.7 | 9e-20 | 26/32 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +9.3 | 3e-18 | 16/25 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 1e-07 | 24/46 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +6.1 | 2e-07 | 23/46 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.9 | 3e-07 | 22/47 (LoVo, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +5.8 | 7e-07 | 16/43 (A498, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.0 | 4e-05 | 16/41 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 3e-04 | 9/45 (MIA PaCa-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.004 | 6/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +3.5 | 0.023 | 14/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +3.5 | 0.023 | 11/46 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **1.23×** | +3.5 | 0.023 | 14/42 (NCI-H2347, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.028 | 9/48 (A-427, MIA PaCa-2, …) | top dose only | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.030 | 6/44 (NCI-H460, LoVo, …) | two highest doses | position effect removed |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.030 | 5/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.031 | 7/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.071 | 6/45 (Panc 03.27, J82, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.094 | 3/47 (NCI-H2030, SW 1271, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -14.1 | 4e-42 | 36/46 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -7.3 | 8e-11 | 28/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -6.4 | 3e-08 | 23/47 (A-427, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.705×** | -5.9 | 4e-07 | 22/48 (SW 1271, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.724×** | -5.5 | 5e-06 | 20/47 (H4, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.754×** | -4.8 | 1e-04 | 18/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.792×** | -3.8 | 0.011 | 15/43 (SK-MEL-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.816×** | -3.5 | 0.038 | 11/47 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.823×** | -3.3 | 0.057 | 9/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 0.828× | -3.1 | 0.11 | 15/47 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.830× | -3.1 | 0.11 | 11/47 (BT-474, NCI-H23, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.832× | -3.0 | 0.12 | 16/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -11.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 17.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -12.5) |
| [[SW480 (line)]] | alt | 19.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -13.3) |
| [[A-172 (line)]] | wt | 13.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -8.9) |
| [[BT-474 (line)]] | alt | 9.91 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -10.1) |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -8.7) |
| [[C32 (line)]] | wt | 7.36 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0648× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 9.62 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -13.2) |
| [[KATO III (line)]] | alt | 14.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -12.8) |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.4) |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKTN]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[WDR18]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[MRPL47]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[COG2]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.68 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ZNF502]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SRRD]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[AGK]] | +0.65 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[C19orf44]] | +0.65 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[GTF2H3]] | +0.64 | +0.70 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.64 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[PTMA]] | -0.56 | -0.69 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF583]] | B | ZNF583 activity raises DRG2's level | lines that do not express ZNF583 (15) vs lines expressing it (35) | 1.08× lower at baseline in the lines without ZNF583 | 0.080 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, SMARCA1, NUDT11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.3, 0.4); signed map (-1.4, -34.7). **Vector** length 70.2, 11.2% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -14.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | developmentally regulated GTP binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,087,892-18,107,970 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 2 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P55039](https://www.uniprot.org/uniprotkb/P55039) (Developmentally-regulated GTP-binding protein 2):

> Catalyzes the conversion of GTP to GDP through hydrolysis of the gamma-phosphate bond in GTP. When hydroxylated at C-3 of 'Lys-21' by JMJD7, may bind to RNA and play a role in translation.

**Summary**, from NCBI Gene [1819](https://www.ncbi.nlm.nih.gov/gene/1819):

> This gene encodes a GTP-binding protein known to function in the regulation of cell growth and differentiation. Read-through transcripts containing this gene and a downstream gene have been identified, but they are not thought to encode a fusion protein. This gene is located within the Smith-Magenis syndrome region on chromosome 17. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:3030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3030) · Entrez [1819](https://www.ncbi.nlm.nih.gov/gene/1819) · UniProt [P55039](https://www.uniprot.org/uniprotkb/P55039) · Ensembl [ENSG00000108591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108591)

## Data

Gene col 2973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2973); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2973]; `tensor/DDL_lfc|DDL_z.npy` [2973]; `embed/gene_vectors.npy` [2973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2973 or target_col == 2973). Every well: [[DRG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
