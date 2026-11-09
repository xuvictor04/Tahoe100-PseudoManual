---
symbol: "GNL3"
type: "gene"
col: 8816
ensembl_id: "ENSG00000163938"
name: "G protein nucleolar 3"
location: "3p21.1"
module: 33
arm: "+"
pooled_cpm: 121.67
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# GNL3

*G protein nucleolar 3* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.91× (z +10.3, q 5e-22, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.844× (z -3.8, q 0.044, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL2]] (+0.73, fdr 7e-06), [[WDR3]] (+0.69, fdr 7e-06), [[UTP6]] (+0.66, fdr 1e-05); moves opposite to [[MAN2B1]] (-0.50, fdr 3e-05), [[MED21]] (-0.48, fdr 2e-04), [[MTCH1]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NBEAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +10.3 | 5e-22 | 36/48 (HT-29, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +6.8 | 4e-09 | 40/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +6.4 | 3e-08 | 39/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.51×** | +6.3 | 5e-08 | 37/47 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.40×** | +5.4 | 9e-06 | 26/48 (SNU-423, SHP-77, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.85×** | +5.1 | 3e-05 | 39/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +5.1 | 3e-05 | 37/49 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.37×** | +5.0 | 4e-05 | 30/48 (SNU-423, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.71×** | +4.5 | 5e-04 | 36/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.007 | 29/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.009 | 31/48 (C32, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.009 | 28/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.27×** | +3.6 | 0.012 | 26/50 (NCI-H23, SNU-423, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.015 | 27/49 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.25×** | +3.5 | 0.015 | 25/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.083 | 22/48 (MIA PaCa-2, NCI-H23, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.0 | 0.083 | 16/48 (LOX-IMVI, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.086 | 22/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.844× | -3.8 | 0.044 | 18/48 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.044 | 26/48 (LoVo, RKO, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.851× | -3.6 | 0.044 | 18/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.044 | 24/48 (A-427, SW480, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.044 | 25/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.802×** | -3.5 | 0.044 | 28/47 (SW48, A-427, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.798×** | -3.4 | 0.045 | 23/44 (HEC-1-A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.803×** | -3.4 | 0.056 | 26/47 (HS-578T, LoVo, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.867× | -3.2 | 0.089 | 17/48 (LS 180, SHP-77, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.0 | 0.14 | 2/50 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 88.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.03× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.21× (z +9.7) | — |
| [[A-427 (line)]] | wt | 153 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.532× (z -9.6) |
| [[C32 (line)]] | wt | 90.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 62.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 84.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.31× (z +14.4) | — |
| [[LoVo (line)]] | wt | 155 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -8.6) ⚠ cell-cycle shift, explains ~88% of this change |
| [[NCI-H1792 (line)]] | alt | 87.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +14.0) | [[Lonafarnib (drug)]] 5 µM 0.166× (z -9.7) ⚠ toxic |
| [[SW480 (line)]] | alt | 163 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.19× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 84.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 68.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +9.1) | — |
| [[H4 (line)]] | wt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.447× (z -9.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.85× (z +12.6) | — |
| [[Hs 766T (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.96× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.528× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.60× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 52.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.87× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 189 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -12.8) ⚠ cell-cycle shift, explains ~88% of this change |
| [[SNU-423 (line)]] | alt | 84.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +9.6) | — |
| [[A-172 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 98.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 139 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 174 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 95.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL2]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 | STRING 997 |
| [[WDR3]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 857 |
| [[UTP6]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 743 |
| [[POLR1B]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 | STRING 819 |
| [[DKC1]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 | same gene group; pathway: rRNA processing; STRING 909 |
| [[TRAP1]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.62 | +0.58 / +0.62 | both halves | 8e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 778 |
| [[NOP58]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 946 |
| [[WDR43]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V2; STRING 925 |
| [[SRM]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[GAR1]] | +0.60 | +0.62 / +0.51 | both halves | 1e-05 | pathway: rRNA processing; STRING 757 |
| [[PPAT]] | +0.59 | +0.49 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAN2B1]] | -0.50 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MED21]] | -0.48 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[MTCH1]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBEAP2]] | B | NBEAP2 activity raises GNL3's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without NBEAP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621 |
| [[WDR43]] | C | WDR43's natural level weakens GNL3's drug response | WDR43's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.06; direction not clear | 0.097 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.6, -39.2); signed map (-6.6, -51.1). **Vector** length 129, 44.9% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.56 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +6.8 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.8 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +3.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.5 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -6.0 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.9 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.3 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | G protein nucleolar 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,681,156-52,694,497 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C77032, E2IG3, MGC800, NS, Nug1 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V2, MYC_TARGETS_V1 |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVP2](https://www.uniprot.org/uniprotkb/Q9BVP2) (Guanine nucleotide-binding protein-like 3):

> May be required to maintain the proliferative capacity of stem cells. Stabilizes MDM2 by preventing its ubiquitination, and hence proteasomal degradation (By similarity).

**Summary**, from NCBI Gene [26354](https://www.ncbi.nlm.nih.gov/gene/26354):

> The protein encoded by this gene may interact with p53 and may be involved in tumorigenesis. The encoded protein also appears to be important for stem cell proliferation. This protein is found in both the nucleus and nucleolus. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:29931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29931) · Entrez [26354](https://www.ncbi.nlm.nih.gov/gene/26354) · UniProt [Q9BVP2](https://www.uniprot.org/uniprotkb/Q9BVP2) · Ensembl [ENSG00000163938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163938)

## Data

Gene col 8816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8816); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8816]; `tensor/DDL_lfc|DDL_z.npy` [8816]; `embed/gene_vectors.npy` [8816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8816 or target_col == 8816). Every well: [[GNL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
