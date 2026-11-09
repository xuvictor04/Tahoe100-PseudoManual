---
symbol: "HDGFL2"
type: "gene"
col: 9516
ensembl_id: "ENSG00000167674"
name: "HDGF like 2"
location: "19p13.3"
module: 85
arm: "+"
pooled_cpm: 25.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# HDGFL2

*HDGF like 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.22× (z +11.2, q 2e-26, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.669× (z -7.9, q 1e-12, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP131]] (+0.74, fdr 1e-05), [[ESS2]] (+0.68, fdr 1e-05), [[STUB1]] (+0.68, fdr 3e-05); moves opposite to [[RFX3-DT]] (-0.64, fdr 3e-04), [[SLC2A9]] (-0.63, fdr 6e-05), [[CSTF3]] (-0.63, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC2A9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +11.2 | 2e-26 | 45/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +11.1 | 4e-26 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +9.6 | 2e-19 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +7.9 | 5e-13 | 39/47 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.69×** | +7.1 | 1e-10 | 23/37 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.50×** | +5.7 | 1e-06 | 29/46 (HEC-1-A, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +5.5 | 4e-06 | 30/48 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.42×** | +5.0 | 5e-05 | 25/43 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +4.4 | 7e-04 | 23/46 (A-427, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.007 | 13/48 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.7 | 0.010 | 18/47 (A498, LS 180, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.20×** | +3.7 | 0.011 | 19/48 (A549, HT-29, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.056 | 11/46 (SW48, H4, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.087 | 9/47 (NCI-H2347, J82, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.087 | 10/48 (A-172, RKO, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.669×** | -7.9 | 1e-12 | 38/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -6.8 | 2e-09 | 32/48 (A-427, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.712×** | -4.7 | 4e-04 | 23/48 (SNU-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -4.5 | 9e-04 | 24/47 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fumaric acid (drug)]] 0.5 µM |  | **0.726×** | -4.5 | 9e-04 | 27/48 (NCI-H23, PANC-1, …) | two highest doses | position effect removed |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -4.4 | 1e-03 | 27/48 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.750×** | -4.0 | 0.005 | 24/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 5 µM |  | **0.752×** | -4.0 | 0.005 | 15/48 (NCI-H2347, A498, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.783×** | -3.4 | 0.042 | 20/48 (SK-MEL-2, CHP-212, …) | inconsistent across doses |  |
| [[Volasertib (drug)]] 0.5 µM |  | 0.734× | -3.1 | 0.12 | 7/48 (HT-29, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.803× | -3.0 | 0.12 | 12/48 (H4, C32, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | 0.739× | -3.0 | 0.12 | 2/48 (A-172, A498) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 40.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -11.0) |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.191× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 34.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0996× (z -9.0) |
| [[HS-578T (line)]] | alt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -8.5) |
| [[SW480 (line)]] | alt | 24.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.75× (z +8.7) | — |
| [[A-172 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP131]] | +0.74 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[ESS2]] | +0.68 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[STUB1]] | +0.68 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[MPND]] | +0.66 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SLC27A1]] | +0.66 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[SAP130]] | +0.65 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[PAK4]] | +0.64 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[BRF1]] | +0.63 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[RAB40B]] | +0.63 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[BAD]] | +0.63 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[SPSB3]] | +0.63 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[DHTKD1]] | +0.62 | +0.36 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3-DT]] | -0.64 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[SLC2A9]] | -0.63 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[CSTF3]] | -0.63 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[LINC01829]] | -0.62 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[DPH5-DT]] | -0.62 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[MPDU1]] | -0.62 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[ZNF337-AS1]] | -0.61 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[RXYLT1]] | -0.61 | -0.60 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[LINC02977]] | -0.60 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[MSH4]] | -0.60 | -0.56 / -0.23 | both halves | 5e-04 |  |
| [[LINC01004]] | -0.60 | -0.53 / -0.21 | both halves | 7e-04 |  |
| [[SMIM15-AS1]] | -0.60 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[SECISBP2]] | -0.60 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A9]] | B | SLC2A9 activity lowers HDGFL2's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.50× higher at baseline in the lines without SLC2A9 | 0.049 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[SNTA1]] | B | SNTA1 activity raises HDGFL2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without SNTA1 | 0.099 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (3.9, -2.6); signed map (-35.0, 1.2). **Vector** length 91.0, 21.2% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.7 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +11.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.3 | +7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.8 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | HDGF like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,472,297-4,502,208 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRP2, Hdgfrp2 |
| Gene groups (HGNC) | Heparin binding growth factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4V5](https://www.uniprot.org/uniprotkb/Q7Z4V5) (Hepatoma-derived growth factor-related protein 2):

> Acts as an epigenetic regulator of myogenesis in cooperation with DPF3a (isoform 2 of DPF3/BAF45C). Associates with the BAF complex via its interaction with DPF3a and HDGFL2-DPF3a activate myogenic genes by increasing chromatin accessibility through recruitment of SMARCA4/BRG1/BAF190A (ATPase subunit of the BAF complex) to myogenic gene promoters. Promotes the repair of DNA double-strand breaks (DSBs) through the homologous recombination pathway by facilitating the recruitment of the DNA …

**Summary**, from NCBI Gene [84717](https://www.ncbi.nlm.nih.gov/gene/84717):

> This gene encodes a member of the hepatoma-derived growth factor (HDGF) family. The protein includes an N-terminal PWWP domain that binds to methyl-lysine-containing histones, with specific binding of this protein to tri-methylated lysines 36 and 79 of histone H3, and di- and tri-methylated lysine 20 of histone H4. The protein functions in LEDGF/p75-independent HIV-1 replication by determining HIV-1 integration site selection. Alternative splicing of this gene results in multiple transcript …

**Accessions** — [HGNC:14680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14680) · Entrez [84717](https://www.ncbi.nlm.nih.gov/gene/84717) · UniProt [Q7Z4V5](https://www.uniprot.org/uniprotkb/Q7Z4V5) · Ensembl [ENSG00000167674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167674)

## Data

Gene col 9516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9516); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9516]; `tensor/DDL_lfc|DDL_z.npy` [9516]; `embed/gene_vectors.npy` [9516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9516 or target_col == 9516). Every well: [[HDGFL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDGFL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
