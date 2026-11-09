---
symbol: "ZNG1E"
type: "gene"
col: 7236
ensembl_id: "ENSG00000147996"
name: "Zn regulated GTPase metalloprotein activator 1E"
location: "9q21.11"
module: 5
arm: "+"
pooled_cpm: 12.29
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ZNG1E

*Zn regulated GTPase metalloprotein activator 1E* — 9q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.47× (z +6.7, q 1e-08, up in 22 of 47 measured lines) ⚠ unreliable plate only. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.904× (z -6.2, q 4e-07, down in 6 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 0.675× (z -4.9, q 2e-04, down in 13 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNG1C]] (+0.92, fdr 7e-06), [[ZNG1F]] (+0.82, fdr 7e-06), [[ZNG1B]] (+0.61, fdr 1e-05); moves opposite to [[HDAC5]] (-0.48, fdr 4e-05), [[MTMR3]] (-0.48, fdr 5e-05), [[BMF]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SPON1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +6.7 | 1e-08 | 22/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +5.1 | 8e-05 | 13/48 (SNU-423, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.4 | 0.002 | 12/44 (NCI-H2347, HCT15, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.5 | 0.060 | 2/19 (NCI-H1573, A-427) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.22×** | +3.4 | 0.062 | 11/47 (SHP-77, A-172, …) | rises with dose |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.062 | 1/48 (AsPC-1) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.41× | +3.2 | 0.12 | 4/48 (SNU-423, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pentagastrin (drug)]] 5 µM |  | 1.14× | +3.1 | 0.12 | 3/48 (SW480, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -6.2 | 4e-07 | 6/48 (RKO, COLO 205, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.675×** | -4.9 | 2e-04 | 13/44 (SW480, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.752×** | -4.9 | 2e-04 | 17/44 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.828×** | -4.6 | 5e-04 | 15/48 (AsPC-1, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.776×** | -4.4 | 0.001 | 17/38 (HepG2/C3A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.775×** | -4.4 | 0.001 | 10/44 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.801×** | -3.8 | 0.009 | 10/48 (LS 180, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[5-Fluorouracil (drug)]] 0.5 µM |  | **0.802×** | -3.8 | 0.009 | 3/46 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.745×** | -3.7 | 0.016 | 10/43 (RKO, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.748×** | -3.6 | 0.018 | 9/44 (hTERT-HPNE, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.818×** | -3.4 | 0.029 | 8/46 (A498, KATO III, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.829×** | -3.1 | 0.082 | 12/23 (HOP62, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.831×** | -3.1 | 0.089 | 8/46 (H4, A498, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 21.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 7.36 | 0 | 2 | — | [[Vilanterol (drug)]] 0.5 µM 0.0639× (z -11.4) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0824× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0916× (z -11.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0660× (z -16.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.272× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~90% of this change |
| [[LoVo (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 8.36 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.173× (z -9.1) |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.162× (z -8.5) |
| [[A-427 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1C]] | +0.92 | +0.89 / +0.87 | both halves | 7e-06 | same gene group |
| [[ZNG1F]] | +0.82 | +0.84 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ZNG1B]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 | same gene group |
| [[EXOSC7]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZNG1A]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 | same gene group |
| [[TIMM23B-AGAP6]] | +0.52 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[ACTR3B]] | +0.52 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[TSR1]] | +0.50 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ATR]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[SCFD2]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TRNT1]] | +0.49 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[NCBP2]] | +0.49 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC5]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[MTMR3]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[BMF]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[RICTOR]] | -0.46 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[SPPL3]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[LMBRD1]] | -0.45 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[CTDSP2]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[FXYD6]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[GALT]] | -0.45 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[ABI1]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TXNDC16]] | -0.44 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[CCN3]] | -0.44 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPON1]] | B | SPON1 activity raises ZNG1E's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.30× lower at baseline in the lines without SPON1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[HDAC6]] | B | HDAC6 activity lowers ZNG1E's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MTHFD1L]] | C | MTHFD1L activity raises ZNG1E's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.6, -41.5); signed map (1.8, -53.9). **Vector** length 58.5, 7.84% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -2.6 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.5 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.3 | -4.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.6 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | Zn regulated GTPase metalloprotein activator 1E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.11 — chr9:65,668,805-65,734,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CBWD5 |
| Gene groups (HGNC) | Zn regulated GTPase metalloprotein activator 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5RIA9](https://www.uniprot.org/uniprotkb/Q5RIA9) (Zinc-regulated GTPase metalloprotein activator 1E):

> Zinc chaperone that directly transfers zinc cofactor to target metalloproteins, thereby activating them. Catalyzes zinc insertion into the active site of methionine aminopeptidase METAP1, which function to cleave the initiator methionine from polypeptides during or after protein translation. Mechanistically, the N-terminal psi-PxLVp motif binds to the C6H2-type zinc finger of inactive form of METAP1. After formation of the docked complex, zinc is transferred from the CXCC motif in the GTPase …

**Summary**, from NCBI Gene [220869](https://www.ncbi.nlm.nih.gov/gene/220869):

> Predicted to enable GTPase activity; zinc chaperone activity; and zinc ion binding activity. Predicted to be involved in protein maturation. Predicted to be located in nucleus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24584) · Entrez [220869](https://www.ncbi.nlm.nih.gov/gene/220869) · UniProt [Q5RIA9](https://www.uniprot.org/uniprotkb/Q5RIA9) · Ensembl [ENSG00000147996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147996)

## Data

Gene col 7236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7236); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7236]; `tensor/DDL_lfc|DDL_z.npy` [7236]; `embed/gene_vectors.npy` [7236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7236 or target_col == 7236). Every well: [[ZNG1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNG1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
