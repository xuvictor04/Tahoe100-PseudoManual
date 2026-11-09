---
symbol: "SH3GLB2"
type: "gene"
col: 7269
ensembl_id: "ENSG00000148341"
name: "SH3 domain containing GRB2 like, endophilin B2"
location: "9q34.11"
module: 2
arm: "+"
pooled_cpm: 9.73
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SH3GLB2

*SH3 domain containing GRB2 like, endophilin B2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.12× (z +15.0, q 0e+00, up in 14 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.15× (z +10.5, q 2e-23, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.643× (z -8.6, q 6e-15, down in 31 of 43 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.544× (z -8.3, q 2e-14, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SBF1]] (+0.71, fdr 1e-05), [[STK25]] (+0.70, fdr 1e-05), [[TNK2]] (+0.69, fdr 1e-05); moves opposite to [[TRIP11]] (-0.63, fdr 3e-05), [[HELQ]] (-0.61, fdr 4e-05), [[MTRFR]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +15.0 | 0e+00 | 14/18 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +14.6 | 1e-45 | 31/31 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +10.5 | 2e-23 | 40/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +10.4 | 5e-23 | 22/25 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +8.0 | 1e-13 | 32/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +8.0 | 1e-13 | 34/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.6 | 4e-04 | 12/38 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.003 | 8/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.5 | 0.030 | 7/46 (A-172, A498, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.3 | 0.047 | 12/38 (SNU-423, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.27×** | +3.2 | 0.063 | 10/43 (SW480, AsPC-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.063 | 13/43 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.083 | 6/44 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.643×** | -8.6 | 6e-15 | 31/43 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -8.3 | 2e-14 | 28/42 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.687×** | -5.1 | 5e-05 | 18/47 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.753×** | -3.9 | 0.014 | 17/47 (SW 900, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.774×** | -3.5 | 0.043 | 9/46 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.763×** | -3.5 | 0.043 | 13/46 (BT-474, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.617×** | -3.5 | 0.043 | 14/42 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.772×** | -3.4 | 0.044 | 15/45 (SK-MEL-2, J82, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.637×** | -3.2 | 0.078 | 16/46 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.802× | -3.0 | 0.13 | 17/43 (A-172, BT-474, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.67 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.96× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +10.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 8.45 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.78× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 14.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.93× (z +9.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 4.45 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.121× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 8.11 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0587× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 9.88 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0951× (z -10.6) |
| [[A-427 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBF1]] | +0.71 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[STK25]] | +0.70 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[TNK2]] | +0.69 | +0.62 / +0.51 | both halves | 1e-05 | same gene group |
| [[LLGL1]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[INTS11]] | +0.68 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[ABCA2]] | +0.68 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[NPDC1]] | +0.68 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[NBEAL2]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[UCKL1]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[GNAZ]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RHPN1]] | +0.65 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP11]] | -0.63 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[HELQ]] | -0.61 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[MTRFR]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[BPTF]] | -0.59 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[RBBP6]] | -0.59 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ASH1L]] | -0.58 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[ZNF24]] | -0.57 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[ZNF830]] | -0.57 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ZCCHC10]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CCDC59]] | -0.56 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[TOPORS]] | -0.56 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[RBM23]] | -0.56 | -0.57 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SH3GLB2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRR36]] | B | PRR36 activity raises SH3GLB2's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without PRR36 | 0.097 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.7, -23.0); signed map (-45.4, -10.2). **Vector** length 69.4, 11.2% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +10.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +10.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +8.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.8 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.7 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing GRB2 like, endophilin B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,007,036-129,028,331 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1848 |
| Gene groups (HGNC) | N-BAR domain containing; SH3 domain containing |
| Matched by | ensembl_id |

UniProt [Q9NR46](https://www.uniprot.org/uniprotkb/Q9NR46) carries no function annotation.

**Summary**, from NCBI Gene [56904](https://www.ncbi.nlm.nih.gov/gene/56904):

> Enables identical protein binding activity. Predicted to be involved in membrane organization and postsynaptic neurotransmitter receptor internalization. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10834) · Entrez [56904](https://www.ncbi.nlm.nih.gov/gene/56904) · UniProt [Q9NR46](https://www.uniprot.org/uniprotkb/Q9NR46) · Ensembl [ENSG00000148341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148341)

## Data

Gene col 7269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7269); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7269]; `tensor/DDL_lfc|DDL_z.npy` [7269]; `embed/gene_vectors.npy` [7269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7269 or target_col == 7269). Every well: [[SH3GLB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3GLB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
