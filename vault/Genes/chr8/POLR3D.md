---
symbol: "POLR3D"
type: "gene"
col: 9660
ensembl_id: "ENSG00000168495"
name: "RNA polymerase III subunit D"
location: "8p21.3"
module: 52
arm: "+"
pooled_cpm: 42.23
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# POLR3D

*RNA polymerase III subunit D* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.39× (z +5.2, q 1e-04, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.636× (z -7.1, q 8e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL2]] (+0.69, fdr 7e-06), [[EBLN3P]] (+0.68, fdr 7e-06), [[PMM2]] (+0.64, fdr 8e-06); moves opposite to [[B4GALT5]] (-0.54, fdr 1e-05), [[H2AZ2]] (-0.52, fdr 3e-05), [[MARK2]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SZT2]] → it (grade C ⚠); 1 goes from it, the strongest it → [[PLPP5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.2 | 1e-04 | 25/47 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.7 | 9e-04 | 1/48 (HCT15) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +4.2 | 0.005 | 24/46 (J82, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.020 | 25/47 (SK-MEL-2, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.7 | 0.026 | 17/48 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.026 | 23/48 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.072 | 19/48 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.077 | 16/46 (MIA PaCa-2, NCI-H1792, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.085 | 21/48 (NCI-H23, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.085 | 15/48 (NCI-H1792, HCT15, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.085 | 11/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.636×** | -7.1 | 8e-10 | 36/48 (A498, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -6.5 | 2e-08 | 33/48 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -6.0 | 4e-07 | 32/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.717×** | -5.2 | 3e-05 | 33/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.753×** | -4.2 | 0.003 | 23/47 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.772×** | -4.1 | 0.005 | 23/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -3.7 | 0.015 | 17/48 (A498, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.015 | 25/48 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.786×** | -3.6 | 0.019 | 23/47 (SNU-1, SW 1271, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -3.5 | 0.026 | 20/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.855× | -3.5 | 0.026 | 16/48 (COLO 205, NCI-H2347, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -3.4 | 0.029 | 15/48 (Hs 766T, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.805×** | -3.3 | 0.046 | 17/47 (H4, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.820×** | -3.1 | 0.078 | 18/48 (C-33 A, SW 1088, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.0 | 0.087 | 21/47 (RKO, A-172, …) | top dose only | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.691×** | -3.0 | 0.087 | 15/49 (A-172, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 36.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 53.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.225× (z -9.7) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A-172 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 100.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL2]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[EBLN3P]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[PMM2]] | +0.64 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[BET1L]] | +0.64 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PGM3]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZNF550]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[GOLGA3]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SRPRA]] | +0.61 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CUL7]] | +0.61 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SLC39A7]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT5]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[H2AZ2]] | -0.52 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[MARK2]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[MED13L]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[USP6NL]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[AGFG1]] | -0.49 | -0.35 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SZT2]] | C | SZT2's natural level strengthens POLR3D's drug response | SZT2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.13; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[TAF13]] | C | TAF13's natural level strengthens POLR3D's drug response | TAF13's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.48; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLPP5]] | C | POLR3D's natural level strengthens PLPP5's drug response | POLR3D's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.48; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (12.7, -37.4); signed map (-53.4, 13.8). **Vector** length 95.9, 22.6% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +3.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.9 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -4.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.8 | -4.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,245,133-22,254,601 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSBN51, RPC4, C53; previously BN51T |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [P05423](https://www.uniprot.org/uniprotkb/P05423) (DNA-directed RNA polymerase III subunit RPC4):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Specific peripheric component of RNA polymerase III (Pol III) which synthesizes small non-coding RNAs including 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. Assembles with POLR3E/RPC5 forming a subcomplex that binds the Pol III core. Enables recruitment of Pol III at transcription initiation site and drives transcription initiation …

**Summary**, from NCBI Gene [661](https://www.ncbi.nlm.nih.gov/gene/661):

> This gene complements a temperature-sensitive mutant isolated from the BHK-21 Syrian hamster cell line. It leads to a block in progression through the G1 phase of the cell cycle at nonpermissive temperatures. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1080) · Entrez [661](https://www.ncbi.nlm.nih.gov/gene/661) · UniProt [P05423](https://www.uniprot.org/uniprotkb/P05423) · Ensembl [ENSG00000168495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168495)

## Data

Gene col 9660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9660); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9660]; `tensor/DDL_lfc|DDL_z.npy` [9660]; `embed/gene_vectors.npy` [9660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9660 or target_col == 9660). Every well: [[POLR3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
