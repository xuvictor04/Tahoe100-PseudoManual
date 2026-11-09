---
symbol: "IPO4"
type: "gene"
col: 12219
ensembl_id: "ENSG00000196497"
name: "importin 4"
location: "14q12"
module: 4
arm: "+"
pooled_cpm: 13.15
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# IPO4

*importin 4* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.90× (z +15.3, q 0e+00, up in 39 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.60× (z +5.1, q 4e-05, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.706× (z -5.5, q 2e-05, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VARS1]] (+0.83, fdr 7e-06), [[BOP1]] (+0.74, fdr 7e-06), [[WDR46]] (+0.74, fdr 7e-06); moves opposite to [[DCTN6-DT]] (-0.63, fdr 7e-06), [[GABARAPL2]] (-0.62, fdr 1e-05), [[SUMO4]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AFAP1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.90×** | +15.3 | 0e+00 | 39/41 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +12.7 | 2e-34 | 21/21 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.14×** | +11.9 | 3e-30 | 28/30 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.26×** | +9.0 | 5e-17 | 34/48 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.00×** | +7.8 | 8e-13 | 38/47 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.60×** | +5.1 | 4e-05 | 26/46 (PANC-1, NCI-H1792, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.34×** | +5.0 | 5e-05 | 24/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.24×** | +4.7 | 2e-04 | 24/45 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.002 | 21/45 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.03×** | +4.1 | 0.002 | 16/46 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.45×** | +4.1 | 0.002 | 16/40 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.97×** | +4.0 | 0.003 | 16/46 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 19/48 (NCI-H2347, SW 900, …) | top dose only | position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.005 | 15/47 (LS 180, HT-29, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.42×** | +3.7 | 0.007 | 18/45 (NCI-H1573, A-427, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.016 | 12/47 (LoVo, SW 900, …) | all doses, flat | position effect removed |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.025 | 10/46 (LoVo, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.71×** | +3.2 | 0.047 | 16/44 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.052 | 11/46 (hTERT-HPNE, CHP-212, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +2.9 | 0.083 | 9/43 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.706×** | -5.5 | 2e-05 | 33/48 (LS 180, SW48, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.691×** | -4.2 | 0.007 | 19/47 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.689×** | -4.1 | 0.009 | 19/46 (C-33 A, KATO III, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.730×** | -3.6 | 0.048 | 9/47 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.735×** | -3.5 | 0.049 | 21/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.801×** | -3.5 | 0.049 | 16/48 (SW1417, HT-29, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.59× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 11.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.60× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.106× (z -9.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 8.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 8.95 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.231× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 9.53 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.36× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 25.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.122× (z -8.8) |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 15.2 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0779× (z -9.6) |
| [[SW480 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VARS1]] | +0.83 | +0.80 / +0.80 | both halves | 7e-06 | STRING 459 |
| [[BOP1]] | +0.74 | +0.77 / +0.75 | both halves | 7e-06 | STRING 690 |
| [[WDR46]] | +0.74 | +0.67 / +0.75 | both halves | 7e-06 | STRING 518 |
| [[ATP13A1]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[PFAS]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[TBL3]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 | STRING 657 |
| [[EIF4G1]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 | STRING 431 |
| [[ARMC6]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 459 |
| [[WDR77]] | +0.71 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[NOLC1]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[NOC2L]] | +0.68 | +0.68 / +0.75 | both halves | 7e-06 | STRING 751 |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | -0.63 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.62 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[SUMO4]] | -0.61 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[IFI27L2]] | -0.60 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.60 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[FAM182B]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[EAPP]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[BLVRB]] | -0.59 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | -0.58 | -0.46 / -0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF1B]] | -0.58 | -0.41 / -0.61 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFAP1-AS1]] | B | AFAP1-AS1 activity lowers IPO4's level | lines that do not express AFAP1-AS1 (33) vs lines expressing it (17) | 1.33× higher at baseline in the lines without AFAP1-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: AGR2, GABRP, LINC01610 |
| [[GKAP1]] | C | GKAP1 activity raises IPO4's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without GKAP1 | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.3, -33.2); signed map (-5.2, -44.7). **Vector** length 87.0, 18.5% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +11.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +5.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -3.5 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.2 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | importin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,180,219-24,188,869 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Imp4, FLJ23338 |
| Gene groups (HGNC) | Importins; TOG domain containing |
| Hallmark sets | MYC_TARGETS_V2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEX9](https://www.uniprot.org/uniprotkb/Q8TEX9) (Importin-4):

> Nuclear transport receptor that mediates nuclear import of proteins, such as histones, RPS3A, TNP2 and VDR. Serves as receptor for nuclear localization signals (NLS) in cargo substrates. Is thought to mediate docking of the importin/substrate complex to the nuclear pore complex (NPC) through binding to nucleoporin and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to the importin, the …

**Summary**, from NCBI Gene [79711](https://www.ncbi.nlm.nih.gov/gene/79711):

> Enables nuclear import signal receptor activity and nuclear localization sequence binding activity. Involved in protein import into nucleus. Located in chromatin. Part of protein-containing complex. Is active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19426](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19426) · Entrez [79711](https://www.ncbi.nlm.nih.gov/gene/79711) · UniProt [Q8TEX9](https://www.uniprot.org/uniprotkb/Q8TEX9) · Ensembl [ENSG00000196497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196497)

## Data

Gene col 12219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12219); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12219]; `tensor/DDL_lfc|DDL_z.npy` [12219]; `embed/gene_vectors.npy` [12219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12219 or target_col == 12219). Every well: [[IPO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
