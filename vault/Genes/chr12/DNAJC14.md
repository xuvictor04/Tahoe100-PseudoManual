---
symbol: "DNAJC14"
type: "gene"
col: 5697
ensembl_id: "ENSG00000135392"
name: "DnaJ heat shock protein family (Hsp40) member C14"
location: "12q13.2"
module: 16
arm: "+"
pooled_cpm: 11.11
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DNAJC14

*DnaJ heat shock protein family (Hsp40) member C14* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.34× (z +6.0, q 1e-06, up in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.37× (z +4.3, q 0.002, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.613× (z -10.1, q 3e-21, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUF60]] (+0.71, fdr 7e-06), [[ZSCAN22]] (+0.71, fdr 7e-06), [[BYSL]] (+0.69, fdr 7e-06); moves opposite to [[CDK19]] (-0.58, fdr 1e-05), [[ERO1B]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BSN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.34×** | +6.0 | 1e-06 | 21/48 (A549, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.0 | 1e-04 | 4/48 (J82, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +4.3 | 0.002 | 12/40 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.3 | 0.002 | 15/47 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.002 | 16/46 (NCI-H23, LOX-IMVI, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.004 | 10/47 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.010 | 10/48 (SW480, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.021 | 10/43 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.023 | 8/47 (NCI-H2347, PANC-1, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.028 | 6/47 (AN3 CA, PANC-1, …) | top dose only | position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.060 | 8/46 (AsPC-1, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.060 | 8/47 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.076 | 17/47 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -10.1 | 3e-21 | 32/46 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.540×** | -8.7 | 1e-15 | 31/46 (C32, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -6.4 | 4e-08 | 24/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -5.5 | 5e-06 | 25/40 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.695×** | -5.3 | 1e-05 | 19/47 (SW48, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.712×** | -5.0 | 6e-05 | 20/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.726×** | -4.7 | 2e-04 | 16/47 (SW 1271, A549, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.742×** | -4.4 | 9e-04 | 19/47 (hTERT-HPNE, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.743×** | -4.2 | 0.002 | 9/19 (NCI-H460, LoVo, …) | top dose only | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.008 | 17/47 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.777×** | -3.7 | 0.011 | 16/47 (BT-474, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.785×** | -3.6 | 0.017 | 14/46 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.811×** | -3.1 | 0.088 | 8/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.310× (z -8.5) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -11.9) ⚠ cell-cycle shift, explains ~87% of this change |
| [[C32 (line)]] | wt | 7.22 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0990× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 8.62 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0931× (z -9.0) |
| [[LoVo (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.251× (z -8.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0615× (z -11.4) |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0984× (z -8.5) |
| [[A-172 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUF60]] | +0.71 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[ZSCAN22]] | +0.71 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[BYSL]] | +0.69 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SRRD]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[POP4]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PES1]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[RTL6]] | +0.65 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ZC3H10]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB9]] | +0.64 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CHMP7]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK19]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ERO1B]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSN]] | B | BSN activity raises DNAJC14's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.31× lower at baseline in the lines without BSN | 0.004 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises DNAJC14's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.3, -2.0); signed map (-12.5, -29.2). **Vector** length 69.5, 10.8% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.5 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.3 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +2.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -10.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -6.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.4 | -5.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +0.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,820,960-55,830,824 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNAJ, DRIP78, HDJ3, LIP6, FLJ32792 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6Y2X3](https://www.uniprot.org/uniprotkb/Q6Y2X3) (DnaJ homolog subfamily C member 14):

> Regulates the export of target proteins, such as DRD1, from the endoplasmic reticulum to the cell surface.

**Summary**, from NCBI Gene [85406](https://www.ncbi.nlm.nih.gov/gene/85406):

> Predicted to enable dopamine receptor binding activity. Predicted to be involved in protein transport. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24581) · Entrez [85406](https://www.ncbi.nlm.nih.gov/gene/85406) · UniProt [Q6Y2X3](https://www.uniprot.org/uniprotkb/Q6Y2X3) · Ensembl [ENSG00000135392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135392)

## Data

Gene col 5697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5697); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5697]; `tensor/DDL_lfc|DDL_z.npy` [5697]; `embed/gene_vectors.npy` [5697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5697 or target_col == 5697). Every well: [[DNAJC14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
