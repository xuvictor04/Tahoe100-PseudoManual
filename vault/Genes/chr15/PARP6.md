---
symbol: "PARP6"
type: "gene"
col: 6074
ensembl_id: "ENSG00000137817"
name: "poly(ADP-ribose) polymerase family member 6"
location: "15q23"
module: 17
arm: "+"
pooled_cpm: 38.99
n_lines_expressing: 44
n_dd_up: 1
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PARP6

*poly(ADP-ribose) polymerase family member 6* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 1.19× (z +4.6, q 0.002, up in 16 of 42 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.50× (z +4.0, q 0.020, up in 18 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SK-MEL-2 2.23×, RPMI-7951 2.06×, Hs 766T 2.46×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 5.04×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.735× (z -5.8, q 3e-06, down in 25 of 42 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.737× (z -5.7, q 3e-06, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LSM14B]] (+0.60, fdr 7e-06), [[TUT1]] (+0.59, fdr 5e-05), [[EXOC1]] (+0.58, fdr 3e-05); moves opposite to [[SNRPB]] (-0.53, fdr 2e-05), [[PRDX1]] (-0.51, fdr 2e-05), [[TUSC3]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6074.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SK-MEL-2 2.23×, RPMI-7951 2.06×, Hs 766T 2.46×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 5.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.19× | +4.6 | 0.002 | 16/42 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.020 | 18/41 (SW480, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.022 | 10/42 (BT-474, HCT15, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.15× | +3.8 | 0.022 | 13/42 (Panc 03.27, RKO, …) | top dose only | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.15× | +3.7 | 0.028 | 6/42 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.10 | 9/41 (PANC-1, HS-578T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.1 | 0.18 | 13/42 (NCI-H23, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.735×** | -5.8 | 3e-06 | 25/42 (HS-578T, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.737×** | -5.7 | 3e-06 | 21/42 (NCI-H2347, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -5.6 | 5e-06 | 21/42 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.748×** | -5.1 | 6e-05 | 18/36 (A-172, NCI-H1792, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.633×** | -4.5 | 8e-04 | 20/38 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -4.0 | 0.006 | 17/42 (J82, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.828×** | -3.5 | 0.033 | 18/42 (SW48, HS-578T, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **0.825×** | -3.5 | 0.036 | 16/41 (C32, SW 900, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.836× | -3.3 | 0.047 | 8/42 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.837× | -3.3 | 0.047 | 18/42 (SW 900, HS-578T, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.885× | -3.2 | 0.066 | 9/42 (SW 900, MIA PaCa-2, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.844× | -3.2 | 0.071 | 15/42 (RPMI-7951, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 114 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 17.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.164× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 72.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0797× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 1 | — | [[DT-061 (drug)]] 5 µM 0.0578× (z -10.7) |
| [[HS-578T (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.283× (z -10.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 28.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0878× (z -11.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.312× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[SW48 (line)]] | wt | 41.8 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.173× (z -10.3) |
| [[A-427 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM14B]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TUT1]] | +0.59 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[EXOC1]] | +0.58 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[NEURL4]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ZSWIM8]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[C1orf50]] | +0.57 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[FRG1BP]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[ZNF14]] | +0.56 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[KLHL12]] | +0.56 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[PICK1]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ACTR10]] | +0.55 | +0.63 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[PRDX1]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TUSC3]] | -0.49 | -0.54 / -0.40 | both halves | 5e-05 | pathway: Late SARS-CoV-2 Infection Events |
| [[SPATA5]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[HSP90AA1]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 | pathway: Metabolism of vitamins and cofactors |
| [[SFXN5]] | -0.47 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZSWIM6]] | -0.46 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[BRI3BP]] | -0.45 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[SNTB2]] | -0.45 | -0.51 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PARP6's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.394). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-29.4, 0.2); signed map (-13.5, -14.9). **Vector** length 82.1, 18.0% of its response variance represented; |z| ≥ 3 in 645 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +2.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.0 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.1 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -2.2 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:72,241,181-72,272,999 (-) |
| Ensembl biotype | protein_coding |
| Also known as | pART17, ARTD17 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases |
| Reactome | 12 pathways, smallest: Maturation of nucleoprotein_9683610; Maturation of nucleoprotein_9694631; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2NL67](https://www.uniprot.org/uniprotkb/Q2NL67) (Protein mono-ADP-ribosyltransferase PARP6):

> Mono-ADP-ribosyltransferase that mediates mono-ADP-ribosylation of target proteins.

**Summary**, from NCBI Gene [56965](https://www.ncbi.nlm.nih.gov/gene/56965):

> Enables NAD+-protein-aspartate ADP-ribosyltransferase activity and NAD+-protein-cysteine ADP-ribosyltransferase activity. Involved in protein auto-ADP-ribosylation. Predicted to be active in endoplasmic reticulum tubular network; membrane; and nuclear envelope. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26921) · Entrez [56965](https://www.ncbi.nlm.nih.gov/gene/56965) · UniProt [Q2NL67](https://www.uniprot.org/uniprotkb/Q2NL67) · Ensembl [ENSG00000137817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137817)

## Data

Gene col 6074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6074); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6074]; `tensor/DDL_lfc|DDL_z.npy` [6074]; `embed/gene_vectors.npy` [6074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6074 or target_col == 6074). Every well: [[PARP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
