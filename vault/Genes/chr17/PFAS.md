---
symbol: "PFAS"
type: "gene"
col: 10973
ensembl_id: "ENSG00000178921"
name: "phosphoribosylformylglycinamidine synthase"
location: "17p13.1"
module: 4
arm: "+"
pooled_cpm: 10.29
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PFAS

*phosphoribosylformylglycinamidine synthase* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.97× (z +14.2, q 8e-43, up in 30 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.58× (z +5.7, q 1e-06, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.720× (z -6.1, q 7e-07, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FARSB]] (+0.82, fdr 7e-06), [[MYBBP1A]] (+0.81, fdr 7e-06), [[CAD]] (+0.80, fdr 7e-06); moves opposite to [[SELENOK]] (-0.72, fdr 7e-06), [[PNPLA8]] (-0.67, fdr 7e-06), [[FTL]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +14.2 | 8e-43 | 30/32 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +13.9 | 4e-41 | 22/23 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +13.6 | 1e-39 | 15/16 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.01×** | +9.1 | 1e-17 | 35/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 21/46 (PANC-1, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +5.6 | 3e-06 | 19/45 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.89×** | +4.3 | 0.001 | 11/41 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +4.3 | 0.001 | 11/46 (HEC-1-A, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.003 | 16/44 (A549, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.82×** | +4.1 | 0.003 | 9/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +3.9 | 0.004 | 2/45 (Hs 766T, NCI-H460) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.71×** | +3.6 | 0.013 | 11/42 (SW 900, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.69×** | +3.6 | 0.015 | 6/38 (PANC-1, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.33×** | +3.6 | 0.015 | 11/39 (A-427, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.032 | 9/45 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.064 | 6/47 (NCI-H460, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -6.1 | 7e-07 | 20/46 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -5.6 | 5e-06 | 21/48 (Panc 03.27, SW1417, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.728×** | -4.4 | 0.001 | 10/48 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -4.4 | 0.001 | 16/44 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.728×** | -4.2 | 0.004 | 16/45 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.729×** | -3.9 | 0.009 | 13/45 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.757×** | -3.7 | 0.020 | 13/48 (HCT15, LS 180, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.823×** | -3.6 | 0.020 | 12/47 (Hs 766T, RKO, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.781×** | -3.3 | 0.072 | 6/47 (Panc 03.27, BT-474, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.634× | -3.1 | 0.10 | 6/46 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.818× | -3.1 | 0.10 | 11/48 (SW480, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.785× | -3.1 | 0.10 | 15/46 (hTERT-HPNE, SNU-1, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.851× | -3.0 | 0.11 | 10/47 (NCI-H23, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +10.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -9.9) |
| [[A498 (line)]] | wt | 12.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.43× (z +9.3) ⚠ toxic; transcription drop | [[AZD2858 (drug)]] 5 µM 0.0820× (z -8.9) ⚠ toxic |
| [[A549 (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +9.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 6.49 | 0 | 1 | — | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0618× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 3.15 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0656× (z -8.7) |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0852× (z -9.5) |
| [[HOP62 (line)]] | alt | 5.69 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.144× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~46% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -12.6) |
| [[RKO (line)]] | wt | 24.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -11.8) |
| [[SW48 (line)]] | wt | 14.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0556× (z -11.0) |
| [[A-172 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.81 | +0.79 / +0.82 | both halves | 7e-06 |  |
| [[CAD]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 | same gene group; pathway: Metabolism of nucleotides; STRING 650 |
| [[EXOSC2]] | +0.79 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.78 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[ATIC]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 | same gene group; pathway: Metabolism of nucleotides; STRING 819 |
| [[WDR4]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[PRPF19]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[VARS1]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[SF3B3]] | +0.74 | +0.73 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.72 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[PNPLA8]] | -0.67 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[FTL]] | -0.63 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[RABAC1]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises PFAS's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without TERT | 0.024 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.2, -35.0); signed map (-5.8, -45.8). **Vector** length 89.0, 17.9% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.51 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.54 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +13.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +9.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +5.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +3.6 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.8 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosylformylglycinamidine synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,247,618-8,270,491 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PURL, FGARAT, KIAA0361, GATD8 |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing; Purinosome; Ligases |
| Reactome | 3 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [O15067](https://www.uniprot.org/uniprotkb/O15067) (Phosphoribosylformylglycinamidine synthase):

> Phosphoribosylformylglycinamidine synthase involved in the purines biosynthetic pathway. Catalyzes the ATP-dependent conversion of formylglycinamide ribonucleotide (FGAR) and glutamine to yield formylglycinamidine ribonucleotide (FGAM) and glutamate.

**Summary**, from NCBI Gene [5198](https://www.ncbi.nlm.nih.gov/gene/5198):

> Purines are necessary for many cellular processes, including DNA replication, transcription, and energy metabolism. Ten enzymatic steps are required to synthesize inosine monophosphate (IMP) in the de novo pathway of purine biosynthesis. The enzyme encoded by this gene catalyzes the fourth step of IMP biosynthesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8863) · Entrez [5198](https://www.ncbi.nlm.nih.gov/gene/5198) · UniProt [O15067](https://www.uniprot.org/uniprotkb/O15067) · Ensembl [ENSG00000178921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178921)

## Data

Gene col 10973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10973); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10973]; `tensor/DDL_lfc|DDL_z.npy` [10973]; `embed/gene_vectors.npy` [10973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10973 or target_col == 10973). Every well: [[PFAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
