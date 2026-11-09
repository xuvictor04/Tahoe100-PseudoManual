---
symbol: "ZFP37"
type: "gene"
col: 5922
ensembl_id: "ENSG00000136866"
name: "ZFP37 zinc finger protein"
location: "9q32"
module: 16
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 36
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZFP37

*ZFP37 zinc finger protein* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.87× (z +8.9, q 2e-16, up in 25 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.414× (z -17.8, q 0e+00, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF615]] (+0.75, fdr 7e-06), [[ZSCAN26]] (+0.72, fdr 7e-06), [[ZNF484]] (+0.71, fdr 7e-06); moves opposite to [[CD9]] (-0.55, fdr 2e-05), [[ADAM10]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF813]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF813]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +8.9 | 2e-16 | 25/33 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +7.7 | 3e-12 | 20/33 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +6.6 | 1e-08 | 13/34 (Hs 766T, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +6.5 | 1e-08 | 13/32 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +6.4 | 2e-08 | 13/33 (A498, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.7 | 1e-06 | 13/31 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +5.1 | 3e-05 | 13/32 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.0 | 0.005 | 7/19 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.008 | 10/33 (A498, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.009 | 9/33 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.021 | 10/34 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.037 | 4/31 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bergenin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.049 | 3/34 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.076 | 2/32 (A498, RKO) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5922.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.414×** | -17.8 | 0e+00 | 29/31 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.436×** | -11.4 | 1e-27 | 25/32 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.476×** | -10.6 | 7e-24 | 28/33 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.476×** | -10.2 | 3e-22 | 21/32 (C32, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.495×** | -10.0 | 1e-21 | 22/33 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.521×** | -9.3 | 1e-18 | 21/33 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.578×** | -7.8 | 4e-13 | 18/22 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.605×** | -6.9 | 4e-10 | 8/11 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.741×** | -4.3 | 0.001 | 11/33 (RPMI-7951, SW480, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.590×** | -3.9 | 0.005 | 6/32 (RPMI-7951, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.769×** | -3.6 | 0.016 | 9/28 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.793×** | -3.3 | 0.043 | 6/33 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0648× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -9.8) |
| [[A498 (line)]] | wt | 9.43 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -8.8) |
| [[C32 (line)]] | wt | 9.22 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0482× (z -12.5) |
| [[RKO (line)]] | wt | 24.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +13.5) | — |
| [[SW480 (line)]] | alt | 11.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 8.84 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 9.46 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0494× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0812× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 6.15 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -11.9) |
| [[HS-578T (line)]] | alt | 6.40 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 5.05 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0361× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 9.68 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 5.90 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -10.9) |
| [[PANC-1 (line)]] | alt | 2.77 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.133× (z -9.3) |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.171× (z -10.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 5.80 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0917× (z -8.6) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.697 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF615]] | +0.75 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[ZSCAN26]] | +0.72 | +0.74 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZNF484]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | same gene group |
| [[ZSCAN12]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 | same gene group |
| [[ZNF383]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZSCAN20]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 | same gene group |
| [[ZNF317]] | +0.67 | +0.55 / +0.66 | both halves | 1e-05 | same gene group |
| [[C19orf44]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[RBSN]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 | same gene group |
| [[CCDC43]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZNF780A]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 | same gene group |
| [[ZNF227]] | +0.66 | +0.63 / +0.58 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD9]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ADAM10]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF813]] | B | ZNF813 activity raises ZFP37's level | lines that do not express ZNF813 (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without ZNF813 | 0.050 | ⚠ within organs, on part of the lines; also absent: ZNF256, ZNF331, ZNF625; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ZFP37's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF569]] | B | ZNF569 activity raises ZFP37's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without ZNF569 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF813]] | B | ZFP37 activity raises ZNF813's level | lines that do not express ZFP37 (14) vs lines expressing it (36) | 2.61× lower at baseline in the lines without ZFP37 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF883, HEG1, RECK |
| [[PGBD1]] | B | ZFP37 activity raises PGBD1's level | lines that do not express ZFP37 (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without ZFP37 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF883, HEG1, RECK |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.1, 9.0); signed map (1.5, -25.8). **Vector** length 57.6, 9.82% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.5 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.2 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.0 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +2.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -17.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -2.2 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ZFP37 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,038,377-113,056,759 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF906 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Q3](https://www.uniprot.org/uniprotkb/Q9Y6Q3) (Zinc finger protein 37 homolog):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7539](https://www.ncbi.nlm.nih.gov/gene/7539):

> This gene encodes a transcription factor that belongs to a large family of zinc finger proteins. A similar protein in mouse is thought to play a role in regulating the structures of the nucleolus and centromere in neurons. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:12863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12863) · Entrez [7539](https://www.ncbi.nlm.nih.gov/gene/7539) · UniProt [Q9Y6Q3](https://www.uniprot.org/uniprotkb/Q9Y6Q3) · Ensembl [ENSG00000136866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136866)

## Data

Gene col 5922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5922); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5922]; `tensor/DDL_lfc|DDL_z.npy` [5922]; `embed/gene_vectors.npy` [5922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5922 or target_col == 5922). Every well: [[ZFP37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
