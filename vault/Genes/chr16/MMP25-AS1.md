---
symbol: "MMP25-AS1"
type: "gene"
col: 15375
ensembl_id: "ENSG00000261971"
name: "MMP25 antisense RNA 1"
location: "16p13.3"
module: 10
arm: "+"
pooled_cpm: 8.55
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# MMP25-AS1

*MMP25 antisense RNA 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +7.3, q 2e-10, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.540× (z -6.8, q 6e-09, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRTAP5-AS1]] (+0.64, fdr 1e-05), [[C19orf18]] (+0.64, fdr 1e-05), [[MYL5]] (+0.63, fdr 1e-05); moves opposite to [[NUP43]] (-0.59, fdr 3e-05), [[HAUS6]] (-0.57, fdr 3e-05), [[MDH2]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADRA2C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +7.3 | 2e-10 | 28/46 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.004 | 14/47 (A498, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.014 | 19/44 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.014 | 13/47 (A-172, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.030 | 11/45 (A549, SK-MEL-2, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.030 | 7/43 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.053 | 13/44 (A-172, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.053 | 12/47 (AsPC-1, A-172, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.2 | 0.094 | 5/16 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.32× | +3.1 | 0.11 | 13/44 (C32, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.13 | 8/44 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.540×** | -6.8 | 6e-09 | 31/46 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.560×** | -6.4 | 5e-08 | 26/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.606×** | -5.5 | 7e-06 | 30/46 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.650×** | -4.7 | 3e-04 | 23/44 (HT-29, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -4.1 | 0.005 | 21/46 (PANC-1, Panc 03.27, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.679×** | -3.9 | 0.011 | 13/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.711×** | -3.8 | 0.014 | 18/47 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -3.6 | 0.025 | 13/45 (SHP-77, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -3.5 | 0.030 | 21/47 (NCI-H23, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.709×** | -3.4 | 0.037 | 16/46 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[NG25 (drug)]] 5 µM |  | **0.559×** | -3.4 | 0.041 | 11/40 (BT-474, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -3.3 | 0.048 | 13/43 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | 0.751× | -3.0 | 0.11 | 16/36 (A-427, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 13.7 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 5.87 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0802× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 6.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 5.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 21.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.276× (z -9.1) |
| [[PANC-1 (line)]] | alt | 7.03 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 7.91 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0883× (z -9.2) |
| [[SHP-77 (line)]] | alt | 4.74 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0625× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 7.23 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.114× (z -8.5) |
| [[A498 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRTAP5-AS1]] | +0.64 | +0.67 / +0.52 | both halves | 1e-05 | same gene group |
| [[C19orf18]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[MYL5]] | +0.63 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[LINC01569]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LENG9]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.61 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ZBTB4]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[LINC00963]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[KCNN1]] | +0.60 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SPATC1]] | +0.60 | +0.77 / +0.49 | both halves | 1e-05 |  |
| [[STAC3]] | +0.60 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[COL11A2]] | +0.60 | +0.72 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP43]] | -0.59 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[HAUS6]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[MDH2]] | -0.56 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[CMTM1]] | -0.54 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[BLTP2]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[RPA1]] | -0.54 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[SNHG30]] | -0.53 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[SKP2]] | -0.53 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[FBXW2]] | -0.53 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[WRNIP1]] | -0.53 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[TMX1]] | -0.53 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[BPNT2]] | -0.53 | -0.58 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADRA2C]] | B | ADRA2C activity raises MMP25-AS1's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.39× lower at baseline in the lines without ADRA2C | 0.007 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[SRCIN1]] | B | SRCIN1 activity raises MMP25-AS1's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.39× lower at baseline in the lines without SRCIN1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.4, 28.7); signed map (39.6, -6.8). **Vector** length 63.8, 10.1% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -3.8 |
|  | [[NG25 (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | MMP25 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p13.3 — chr16:3,037,400-3,059,370 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51372) · Entrez [100507419](https://www.ncbi.nlm.nih.gov/gene/100507419) · Ensembl [ENSG00000261971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261971)

## Data

Gene col 15375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15375); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15375]; `tensor/DDL_lfc|DDL_z.npy` [15375]; `embed/gene_vectors.npy` [15375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15375 or target_col == 15375). Every well: [[MMP25-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP25-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
