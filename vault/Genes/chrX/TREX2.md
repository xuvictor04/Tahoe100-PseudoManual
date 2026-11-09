---
symbol: "TREX2"
type: "gene"
col: 11407
ensembl_id: "ENSG00000183479"
name: "three prime repair exonuclease 2"
location: "Xq28"
module: 36
arm: "+"
pooled_cpm: 7.83
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TREX2

*three prime repair exonuclease 2* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +11.2, q 2e-26, up in 14 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.05 µM: 1.28× (z +3.4, q 0.047, up in 9 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.520× (z -13.6, q 3e-39, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD3A]] (+0.81, fdr 7e-06), [[NUP93]] (+0.74, fdr 7e-06), [[ATAD3B]] (+0.72, fdr 7e-06); moves opposite to [[ZNF821]] (-0.68, fdr 1e-05), [[PIGP]] (-0.65, fdr 1e-05), [[TCEAL1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CA11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.15×** | +11.2 | 2e-26 | 14/27 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.89×** | +9.3 | 3e-18 | 28/47 (PANC-1, HT-29, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.74×** | +8.1 | 7e-14 | 25/47 (SW480, HT-29, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.64×** | +6.7 | 4e-09 | 10/19 (SNU-423, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.56×** | +6.2 | 5e-08 | 4/14 (LOX-IMVI, PANC-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.50×** | +6.0 | 2e-07 | 18/47 (HT-29, NCI-H460, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.0 | 5e-05 | 13/36 (SNU-423, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | **1.29×** | +3.6 | 0.023 | 5/31 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.047 | 9/40 (AsPC-1, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.051 | 3/46 (SW480, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.064 | 9/46 (MIA PaCa-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +3.1 | 0.088 | 7/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.1 | 0.090 | 1/16 (A-172) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.520×** | -13.6 | 3e-39 | 33/47 (AsPC-1, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -13.2 | 3e-37 | 32/43 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -11.9 | 3e-30 | 32/44 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.620×** | -6.7 | 3e-09 | 24/44 (H4, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.643×** | -6.2 | 5e-08 | 23/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.447×** | -6.2 | 6e-08 | 20/46 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.717×** | -4.6 | 3e-04 | 14/39 (NCI-H460, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -4.5 | 4e-04 | 16/48 (A498, SW 1088, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.779×** | -3.7 | 0.015 | 11/47 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.775×** | -3.6 | 0.017 | 10/44 (HEC-1-A, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.773×** | -3.6 | 0.017 | 16/45 (HOP62, SW48, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.018 | 15/43 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.048 | 12/46 (RKO, RPMI-7951, …) | rises with dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.069 | 6/42 (Panc 03.27, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **0.795×** | -3.1 | 0.069 | 13/39 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.05 µM |  | **0.812×** | -3.1 | 0.078 | 6/45 (SNU-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Simotinib (drug)]] 0.05 µM |  | **0.802×** | -3.0 | 0.088 | 10/44 (hTERT-HPNE, SW 900, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 9.45 | 0 | 4 (1 ⚠) | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0714× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 9.06 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.161× (z -11.9) |
| [[HOP62 (line)]] | alt | 8.28 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.216× (z -11.4) |
| [[A498 (line)]] | wt | 13.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.246× (z -10.1) |
| [[J82 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 7.37 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 7.43 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0747× (z -11.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.2) |
| [[SW480 (line)]] | alt | 8.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.6) |
| [[A-172 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD3A]] | +0.81 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[NUP93]] | +0.74 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.72 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[FANCA]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RTEL1]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[RFC4]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[POLA1]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[TELO2]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[WRN]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 | same gene group |
| [[CTU2]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TRAP1]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | -0.68 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[PIGP]] | -0.65 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[TCEAL1]] | -0.65 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[C11orf71]] | -0.65 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[KDM5B]] | -0.62 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[UPK2]] | -0.62 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CA11]] | -0.62 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | -0.61 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.61 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[OSER1-DT]] | -0.60 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[N4BP2L1]] | -0.60 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[NDUFV2-AS1]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA11]] | B | CA11 activity raises TREX2's level | lines that do not express CA11 (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without CA11 | 0.059 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01237]] | B | LINC01237 activity raises TREX2's level | lines that do not express LINC01237 (7) vs lines expressing it (43) | 1.29× lower at baseline in the lines without LINC01237 | 0.0999 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HAUS7]] | C | HAUS7's natural level strengthens TREX2's drug response | HAUS7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.08; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-5.4, -27.8); signed map (-45.9, -17.1). **Vector** length 82.0, 14.6% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.6 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.4 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.9 | +6.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +3.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.7 | +6.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.1 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.5 | -13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -13.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -6.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.1 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.4 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | three prime repair exonuclease 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,444,473-153,470,587 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Exonucleases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ50](https://www.uniprot.org/uniprotkb/Q9BQ50) (Three prime repair exonuclease 2):

> Exonuclease with a preference for double-stranded DNA with mismatched 3' termini. May play a role in DNA repair.

**Summary**, from NCBI Gene [11219](https://www.ncbi.nlm.nih.gov/gene/11219):

> This gene encodes a nuclear protein with 3' to 5' exonuclease activity. The encoded protein participates in double-stranded DNA break repair, and may interact with DNA polymerase delta. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:12270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12270) · Entrez [11219](https://www.ncbi.nlm.nih.gov/gene/11219) · UniProt [Q9BQ50](https://www.uniprot.org/uniprotkb/Q9BQ50) · Ensembl [ENSG00000183479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183479)

## Data

Gene col 11407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11407); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11407]; `tensor/DDL_lfc|DDL_z.npy` [11407]; `embed/gene_vectors.npy` [11407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11407 or target_col == 11407). Every well: [[TREX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TREX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
