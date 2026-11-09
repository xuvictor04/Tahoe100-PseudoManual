---
symbol: "EPM2A-DT"
type: "gene"
col: 14029
ensembl_id: "ENSG00000235652"
name: "EPM2A divergent transcript"
location: "6q24.3"
module: 23
arm: "+"
pooled_cpm: 8.85
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# EPM2A-DT

*EPM2A divergent transcript* — 6q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +17.8, q 0e+00, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.454× (z -9.1, q 6e-17, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP38-DT]] (+0.84, fdr 7e-06), [[MAILR]] (+0.79, fdr 7e-06), [[PKN2-AS1]] (+0.77, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[KATNAL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +17.8 | 0e+00 | 36/43 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +8.0 | 4e-13 | 27/44 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +6.1 | 2e-07 | 19/44 (HCT15, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.7 | 1e-06 | 21/44 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.1 | 3e-05 | 12/30 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.7 | 2e-04 | 15/47 (LoVo, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +4.7 | 2e-04 | 18/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.5 | 4e-04 | 8/17 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.5 | 5e-04 | 14/45 (SNU-423, J82, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 5e-04 | 17/46 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.002 | 13/47 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.004 | 13/46 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.006 | 12/48 (SK-MEL-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.006 | 14/47 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.012 | 10/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.015 | 9/48 (SW480, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.015 | 14/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -9.1 | 6e-17 | 33/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -8.0 | 3e-13 | 27/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.564×** | -6.6 | 9e-09 | 26/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.662×** | -4.7 | 3e-04 | 20/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.553×** | -3.6 | 0.043 | 13/43 (PANC-1, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.640×** | -3.5 | 0.045 | 15/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.740×** | -3.4 | 0.045 | 12/48 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.749×** | -3.3 | 0.065 | 12/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.086 | 5/47 (A549, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -9.9) |
| [[SW480 (line)]] | alt | 8.59 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.251× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 11.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 11.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -12.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0403× (z -16.3) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 6.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +8.9) | — |
| [[A549 (line)]] | wt | 6.44 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0992× (z -9.1) |
| [[HCT15 (line)]] | alt | 8.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 8.39 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0654× (z -9.1) |
| [[J82 (line)]] | alt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.43× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 6.93 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0914× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 5.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 2.98 | 0 | 1 | — | [[Methotrexate (drug)]] 0.5 µM 0.0558× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 8.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.8) | — |
| [[RKO (line)]] | wt | 6.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.76× (z +9.5) | — |
| [[A-427 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP38-DT]] | +0.84 | +0.89 / +0.59 | both halves | 7e-06 | same gene group |
| [[MAILR]] | +0.79 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.77 | +0.80 / +0.45 | both halves | 3e-05 |  |
| [[SEPTIN7-DT]] | +0.77 | +0.79 / +0.53 | both halves | 1e-05 | same gene group |
| [[OXA1L-DT]] | +0.77 | +0.81 / +0.50 | both halves | 1e-05 | same gene group |
| [[BDNF-AS]] | +0.76 | +0.84 / +0.45 | both halves | 3e-05 |  |
| [[MAD2L1-DT]] | +0.76 | +0.81 / +0.48 | both halves | 2e-05 | same gene group |
| [[DPH6-DT]] | +0.76 | +0.82 / +0.49 | both halves | 1e-05 | same gene group |
| [[CHD1-DT]] | +0.76 | +0.77 / +0.51 | both halves | 1e-05 | same gene group |
| [[UGDH-AS1]] | +0.76 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.76 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.75 | +0.83 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL2]] | B | KATNAL2 activity raises EPM2A-DT's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without KATNAL2 | 0.043 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[THBS4]] | B | THBS4 activity raises EPM2A-DT's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without THBS4 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers EPM2A-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[CRB1]] | B | CRB1 activity raises EPM2A-DT's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CRB1 | 0.090 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[DDX59-AS1]] | B | DDX59-AS1 activity raises EPM2A-DT's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without DDX59-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |
| [[RFX3-DT]] | C | RFX3-DT activity raises EPM2A-DT's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without RFX3-DT | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[LRRIQ3]] | C | LRRIQ3 activity raises EPM2A-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises EPM2A-DT's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without CATSPER2P1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.9, 18.3); signed map (29.6, -7.9). **Vector** length 67.5, 11.2% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +17.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +3.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -3.4 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | EPM2A divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q24.3 — chr6:145,799,409-145,887,430 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously FBXO30-DT |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48990) · Entrez [100507557](https://www.ncbi.nlm.nih.gov/gene/100507557) · Ensembl [ENSG00000235652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235652)

## Data

Gene col 14029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14029); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14029]; `tensor/DDL_lfc|DDL_z.npy` [14029]; `embed/gene_vectors.npy` [14029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14029 or target_col == 14029). Every well: [[EPM2A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPM2A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
