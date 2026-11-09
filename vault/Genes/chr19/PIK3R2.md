---
symbol: "PIK3R2"
type: "gene"
col: 2635
ensembl_id: "ENSG00000105647"
name: "phosphoinositide-3-kinase regulatory subunit 2"
location: "19p13.11"
module: 57
arm: "+"
pooled_cpm: 10.73
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# PIK3R2

*phosphoinositide-3-kinase regulatory subunit 2* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.93× (z +10.2, q 1e-21, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.410× (z -13.8, q 8e-41, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCA2]] (+0.75, fdr 7e-06), [[RPA1]] (+0.75, fdr 7e-06), [[ELP1]] (+0.72, fdr 7e-06); moves opposite to [[KRCC1]] (-0.74, fdr 7e-06), [[RAB30-DT]] (-0.72, fdr 1e-05), [[PPP1R12A-AS2]] (-0.69, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FKBP10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +10.2 | 1e-21 | 38/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +9.9 | 7e-21 | 39/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +9.7 | 4e-20 | 40/47 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.1 | 7e-14 | 27/38 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +5.6 | 2e-06 | 17/45 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +5.2 | 2e-05 | 16/43 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.8 | 1e-04 | 9/21 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.6 | 3e-04 | 14/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.037 | 7/48 (SHP-77, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[LJI308 (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.043 | 5/47 (HS-578T, RKO, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | **1.25×** | +3.2 | 0.062 | 9/30 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.062 | 2/48 (RPMI-7951, A-427) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.410×** | -13.8 | 8e-41 | 34/45 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.470×** | -11.7 | 3e-29 | 39/46 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.536×** | -9.3 | 3e-18 | 32/46 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.584×** | -8.4 | 1e-14 | 27/48 (A498, H4, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.671×** | -7.8 | 5e-13 | 27/47 (LoVo, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.873× | -7.0 | 2e-10 | 13/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -4.2 | 0.002 | 17/46 (SW48, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -3.8 | 0.010 | 16/48 (J82, HS-578T, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.781×** | -3.5 | 0.025 | 15/43 (SW48, A-172, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.807×** | -3.3 | 0.049 | 8/48 (HEC-1-A, J82, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.809×** | -3.3 | 0.054 | 16/48 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.073 | 17/47 (LS 180, NCI-H661, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.803×** | -3.1 | 0.073 | 8/47 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.818×** | -3.1 | 0.073 | 4/46 (AN3 CA, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 2 | — | [[Canagliflozin (drug)]] 5 µM 0.0939× (z -8.6) |
| [[LoVo (line)]] | wt | 10.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 2 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0931× (z -10.5) |
| [[SW48 (line)]] | wt | 16.4 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0860× (z -9.8) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -10.0) |
| [[A498 (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.234× (z -11.0) |
| [[H4 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.106× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[Hs 766T (line)]] | wt | 7.55 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.103× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.133× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0774× (z -11.3) |
| [[PANC-1 (line)]] | alt | 7.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -8.6) |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0831× (z -13.3) |
| [[SW 900 (line)]] | alt | 8.45 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.140× (z -8.9) |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA2]] | +0.75 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[RPA1]] | +0.75 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[ELP1]] | +0.72 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SHQ1]] | +0.71 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.71 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[MYPOP]] | +0.70 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.69 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LRFN3]] | +0.69 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[SKP2]] | +0.69 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CRAT]] | +0.68 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[CEP131]] | +0.68 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[TCF3]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 | pathway: Cell-Cell communication |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRCC1]] | -0.74 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[RAB30-DT]] | -0.72 | -0.75 / -0.56 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | -0.69 | -0.73 / -0.44 | both halves | 3e-05 |  |
| [[PATL2]] | -0.68 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[PBDC1]] | -0.67 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[MMADHC-DT]] | -0.66 | -0.68 / -0.40 | both halves | 5e-05 |  |
| [[LINC01004]] | -0.65 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[ZBED5]] | -0.65 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.65 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.65 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.64 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ZNF341-AS1]] | -0.64 | -0.63 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP10]] | B | FKBP10 activity raises PIK3R2's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.26× lower at baseline in the lines without FKBP10 | 0.074 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[PTK7]] | B | PTK7 activity raises PIK3R2's level | lines that do not express PTK7 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without PTK7 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000289985, ZNF433, ENSG00000269755 |
| [[HDAC6]] | B | HDAC6 activity lowers PIK3R2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HACE1]] | C | HACE1 activity raises PIK3R2's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without HACE1 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.1, -15.2); signed map (-39.0, -12.3). **Vector** length 82.1, 14.6% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +10.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +9.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.2 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -13.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphoinositide-3-kinase regulatory subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,153,163-18,170,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P85B, p85, p85beta, p85-BETA |
| Gene groups (HGNC) | SH2 domain containing; SH3 domain containing |
| Reactome | 97 pathways, smallest: Co-stimulation by ICOS; Signaling by LTK in cancer; PI3K/AKT activation |
| Matched by | ensembl_id |

**Function**, from UniProt [O00459](https://www.uniprot.org/uniprotkb/O00459) (Phosphatidylinositol 3-kinase regulatory subunit beta):

> Regulatory subunit of phosphoinositide-3-kinase (PI3K), a kinase that phosphorylates PtdIns(4,5)P2 (Phosphatidylinositol 4,5-bisphosphate) to generate phosphatidylinositol 3,4,5-trisphosphate (PIP3). PIP3 plays a key role by recruiting PH domain-containing proteins to the membrane, including AKT1 and PDPK1, activating signaling cascades involved in cell growth, survival, proliferation, motility and morphology. Binds to activated (phosphorylated) protein-tyrosine kinases, through its SH2 domain, …

**Summary**, from NCBI Gene [5296](https://www.ncbi.nlm.nih.gov/gene/5296):

> Phosphatidylinositol 3-kinase (PI3K) is a lipid kinase that phosphorylates phosphatidylinositol and similar compounds, creating second messengers important in growth signaling pathways. PI3K functions as a heterodimer of a regulatory and a catalytic subunit. The protein encoded by this gene is a regulatory component of PI3K. Three transcript variants, one protein coding and the other two non-protein coding, have been found for this gene. [provided by RefSeq, Apr 2019]

**Accessions** — [HGNC:8980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8980) · Entrez [5296](https://www.ncbi.nlm.nih.gov/gene/5296) · UniProt [O00459](https://www.uniprot.org/uniprotkb/O00459) · Ensembl [ENSG00000105647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105647)

## Data

Gene col 2635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2635); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2635]; `tensor/DDL_lfc|DDL_z.npy` [2635]; `embed/gene_vectors.npy` [2635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2635 or target_col == 2635). Every well: [[PIK3R2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3R2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
