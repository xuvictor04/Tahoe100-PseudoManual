---
symbol: "ZNF8"
type: "gene"
col: 15904
ensembl_id: "ENSG00000278129"
name: "zinc finger protein 8"
location: "19q13.43"
module: 59
arm: "-"
pooled_cpm: 16.93
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ZNF8

*zinc finger protein 8* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.56× (z +7.6, q 2e-11, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.637× (z -10.8, q 2e-24, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF20]] (+0.64, fdr 7e-06), [[CLPB]] (+0.64, fdr 7e-06), [[METTL2B]] (+0.59, fdr 5e-05); moves opposite to [[CDK7]] (-0.62, fdr 7e-06), [[LNX2]] (-0.60, fdr 1e-05), [[HADHB]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +7.6 | 2e-11 | 30/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 7e-04 | 21/47 (COLO 205, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.22× | +3.4 | 0.14 | 12/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.23× | +3.3 | 0.15 | 9/47 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.23 | 11/47 (HCT15, A-427, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.0 | 0.23 | 8/47 (A498, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15904.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -10.8 | 2e-24 | 37/47 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.621×** | -8.1 | 2e-13 | 25/41 (NCI-H460, C-33 A, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.759×** | -6.6 | 8e-09 | 20/47 (C32, NCI-H460, …) | top dose only | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.619×** | -5.8 | 9e-07 | 16/46 (C-33 A, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.786×** | -5.8 | 9e-07 | 25/48 (NCI-H1792, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.725×** | -4.6 | 3e-04 | 12/35 (LoVo, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.727×** | -4.1 | 0.004 | 13/29 (C-33 A, A-172, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.793×** | -3.9 | 0.006 | 12/48 (NCI-H1792, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.795×** | -3.9 | 0.006 | 20/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -3.9 | 0.006 | 18/48 (C-33 A, SW48, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.006 | 18/46 (A-427, SW48, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.750×** | -3.7 | 0.011 | 16/43 (Panc 03.27, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.877× | -3.1 | 0.072 | 7/48 (C32, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 67.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 19.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.3) |
| [[A549 (line)]] | wt | 16.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 21.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -15.3) |
| [[A498 (line)]] | wt | 16.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -8.9) |
| [[C32 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 9.44 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 21.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.363× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0662× (z -8.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[AN3 CA (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF20]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CLPB]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[METTL2B]] | +0.59 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[TXLNA]] | +0.58 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[EXOG]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.57 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[C1orf159]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ZNF544]] | +0.57 | +0.66 / +0.54 | both halves | 1e-05 | same gene group; ⚠ same locus (1.5 kb, same strand: neighbours can correlate without regulation) |
| [[ANAPC7]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ATE1]] | +0.55 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[BICD1]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ACSF3]] | +0.55 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ZBTB40]] | +0.54 | +0.42 / +0.66 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK7]] | -0.62 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[LNX2]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[HADHB]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ACADSB]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CCDC115]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TRA2A]] | -0.55 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ABI1]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.54 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.54 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[LINC00674]] | -0.54 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[ORC4]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[RAB1A]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity raises ZNF8's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.41× lower at baseline in the lines without TTC28 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[TOP2A]] | B | TOP2A activity raises ZNF8's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.7, -33.0); signed map (-11.2, -46.7). **Vector** length 74.1, 12.8% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.1 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -10.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.9 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.7 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -5.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,278,955-58,302,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HF.18, Zfp128 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17098](https://www.uniprot.org/uniprotkb/P17098) (Zinc finger protein 8):

> Transcriptional repressor. May modulate BMP and TGF-beta signal transduction, through its interaction with SMAD proteins.

**Summary**, from NCBI Gene [7554](https://www.ncbi.nlm.nih.gov/gene/7554):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13154) · Entrez [7554](https://www.ncbi.nlm.nih.gov/gene/7554) · UniProt [P17098](https://www.uniprot.org/uniprotkb/P17098) · Ensembl [ENSG00000278129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278129)

## Data

Gene col 15904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15904); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15904]; `tensor/DDL_lfc|DDL_z.npy` [15904]; `embed/gene_vectors.npy` [15904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15904 or target_col == 15904). Every well: [[ZNF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
