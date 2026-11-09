---
symbol: "AMN"
type: "gene"
col: 9238
ensembl_id: "ENSG00000166126"
name: "amnion associated transmembrane protein"
location: "14q32.32"
module: 31
arm: "+"
pooled_cpm: 3.1
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 37
direction_downstream: 2
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# AMN

*amnion associated transmembrane protein* — 14q32.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.94× (z +10.7, q 6e-24, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +9.1, q 1e-17, up in 9 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.516× (z -5.2, q 1e-04, down in 15 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM83E]] (+0.67, fdr 1e-05), [[TMPRSS4]] (+0.65, fdr 1e-05), [[VILL]] (+0.65, fdr 1e-05); moves opposite to [[TMEM106B]] (-0.48, fdr 8e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[SLC44A4]] → it (grade B ⚠); 2 go from it, the strongest it → [[LSMEM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.94×** | +10.7 | 6e-24 | 2/7 (LS 180, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +9.5 | 9e-19 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +9.1 | 1e-17 | 9/24 (HOP62, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +7.8 | 7e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +5.7 | 1e-06 | 3/9 (LS 180, SW48, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +4.9 | 1e-04 | 13/33 (SW480, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.7 | 2e-04 | 4/23 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.89×** | +3.5 | 0.029 | 3/15 (LoVo, HCT15, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.52× | +3.1 | 0.11 | 1/14 (AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -5.2 | 1e-04 | 15/30 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.568×** | -4.5 | 0.002 | 17/37 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -3.9 | 0.017 | 16/27 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.759× | -3.1 | 0.24 | 5/34 (SW480, HCT15, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.679× | -3.1 | 0.24 | 8/32 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 18.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.149× (z -9.9) |
| [[LoVo (line)]] | wt | 27.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -8.7) |
| [[A-172 (line)]] | wt | 0.799 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.895 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.923 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.990 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.977 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.876 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.819 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM83E]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[TMPRSS4]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[VILL]] | +0.65 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[LPAR5]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ELMO3]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[EPS8L1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[C6orf132]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[BICDL2]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SRMS]] | +0.58 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[EPHA1]] | +0.58 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[TMEM125]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM106B]] | -0.48 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 37, C 0. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A4]] | B | SLC44A4 activity raises AMN's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.73× lower at baseline in the lines without SLC44A4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[MROH3P]] | B | MROH3P activity raises AMN's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without MROH3P | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[CBLC]] | B | CBLC activity raises AMN's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.33× lower at baseline in the lines without CBLC | 0.004 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[RAB25]] | B | RAB25 activity raises AMN's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.49× lower at baseline in the lines without RAB25 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises AMN's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.35× lower at baseline in the lines without TMPRSS4 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TMEM125]] | B | TMEM125 activity raises AMN's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without TMEM125 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[SGPP2]] | B | SGPP2 activity raises AMN's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.19× lower at baseline in the lines without SGPP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[C6orf132]] | B | C6orf132 activity raises AMN's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without C6orf132 | 0.012 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[TMC4]] | B | TMC4 activity raises AMN's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without TMC4 | 0.012 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[SULT2B1]] | B | SULT2B1 activity raises AMN's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without SULT2B1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[CATSPERB]] | B | CATSPERB activity raises AMN's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without CATSPERB | 0.027 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[HSH2D]] | B | HSH2D activity raises AMN's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without HSH2D | 0.028 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSMEM2]] | B | AMN activity raises LSMEM2's level | lines that do not express AMN (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without AMN | 0.083 | ⚠ within organs, on part of the lines; also absent: TGFBR3, LRP1; maybe low, not absent |
| [[PDE9A]] | B | AMN activity raises PDE9A's level | lines that do not express AMN (6) vs lines expressing it (44) | 2.86× lower at baseline in the lines without AMN | 0.099 | ⚠ within organs, on part of the lines; also absent: TGFBR3, LRP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.3, 54.6); signed map (58.5, 8.8). **Vector** length 40.1, 5.48% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +10.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +3.5 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.4 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | amnion associated transmembrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.32 — chr14:102,922,663-102,933,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | amnionless |
| Reactome | 11 pathways, smallest: HDL clearance; Uptake of dietary cobalamins into enterocytes; Defects in cobalamin (B12) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXJ7](https://www.uniprot.org/uniprotkb/Q9BXJ7) (Protein amnionless):

> Membrane-bound component of the endocytic receptor formed by AMN and CUBN. Required for normal CUBN glycosylation and trafficking to the cell surface. The complex formed by AMN and CUBN is required for efficient absorption of vitamin B12. Required for normal CUBN-mediated protein transport in the kidney (Probable).

**Summary**, from NCBI Gene [81693](https://www.ncbi.nlm.nih.gov/gene/81693):

> The protein encoded by this gene is a type I transmembrane protein. It is thought to modulate bone morphogenetic protein (BMP) receptor function by serving as an accessory or coreceptor, and thus facilitates or hinders BMP binding. It is known that the mouse AMN gene is expressed in the extraembryonic visceral endoderm layer during gastrulation, but it is found to be mutated in amnionless mouse. The encoded protein has sequence similarity to short gastrulation (Sog) and procollagen IIA proteins …

**Accessions** — [HGNC:14604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14604) · Entrez [81693](https://www.ncbi.nlm.nih.gov/gene/81693) · UniProt [Q9BXJ7](https://www.uniprot.org/uniprotkb/Q9BXJ7) · Ensembl [ENSG00000166126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166126)

## Data

Gene col 9238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9238); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9238]; `tensor/DDL_lfc|DDL_z.npy` [9238]; `embed/gene_vectors.npy` [9238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9238 or target_col == 9238). Every well: [[AMN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
