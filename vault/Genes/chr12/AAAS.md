---
symbol: "AAAS"
type: "gene"
col: 1729
ensembl_id: "ENSG00000094914"
name: "aladin WD repeat nucleoporin"
location: "12q13.13"
module: 17
arm: "+"
pooled_cpm: 13.13
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# AAAS

*aladin WD repeat nucleoporin* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.72× (z +7.9, q 1e-12, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.364× (z -14.8, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM114A2]] (+0.69, fdr 7e-06), [[RUSF1]] (+0.66, fdr 1e-05), [[APBB3]] (+0.64, fdr 2e-05); moves opposite to [[PRDM10]] (-0.56, fdr 3e-05), [[TXN]] (-0.54, fdr 1e-05), [[SNTB2]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +7.9 | 1e-12 | 34/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +7.5 | 2e-11 | 5/48 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.4 | 4e-08 | 23/38 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +6.1 | 1e-07 | 25/48 (CFPAC-1, A-172, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 1e-05 | 24/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +4.5 | 6e-04 | 19/47 (LoVo, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 0.001 | 13/47 (KATO III, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.004 | 14/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.6 | 0.020 | 10/23 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.054 | 8/45 (SHP-77, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.24× | +3.1 | 0.11 | 9/45 (HEC-1-A, RPMI-7951, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1729.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.364×** | -14.8 | 0e+00 | 43/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -12.8 | 7e-35 | 39/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.438×** | -12.1 | 2e-31 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -9.0 | 2e-17 | 36/47 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -5.9 | 4e-07 | 25/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.691×** | -5.4 | 6e-06 | 22/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.695×** | -5.3 | 8e-06 | 21/46 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -5.2 | 2e-05 | 23/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.547×** | -4.6 | 2e-04 | 18/44 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.009 | 17/46 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -3.7 | 0.009 | 16/47 (KATO III, J82, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -3.7 | 0.009 | 14/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.629×** | -3.5 | 0.017 | 13/48 (Panc 03.27, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.788×** | -3.5 | 0.020 | 7/47 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 5 µM |  | 0.864× | -3.0 | 0.090 | 6/48 (Hs 766T, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -12.0) |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Bendamustine (drug)]] 5 µM 0.0791× (z -9.4) |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.350× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.391× (z -8.5) |
| [[A-427 (line)]] | wt | 21.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0813× (z -9.6) |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 7.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.164× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 9.80 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM 0.167× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 1 | — | [[Everolimus (drug)]] 0.05 µM 0.249× (z -9.4) |
| [[A-172 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM114A2]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RUSF1]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[APBB3]] | +0.64 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[MKS1]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 | STRING 527 |
| [[MRPS31P4]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PICK1]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ZNF205]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZNF18]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[MBD6]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ARL1]] | +0.59 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[NEURL4]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[GEMIN2]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 | pathway: Metabolism of non-coding RNA; STRING 414 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM10]] | -0.56 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TXN]] | -0.54 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SNTB2]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[DPY19L1P1]] | -0.51 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[NR2C2]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PRKCE]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP21]] | -0.49 | -0.41 / -0.55 | both halves | 4e-05 | pathway: RHOA GTPase cycle |
| [[SNRPB]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 | pathway: Metabolism of non-coding RNA; STRING 426 |
| [[LRRC69]] | -0.49 | -0.52 / -0.21 | both halves | 6e-04 |  |
| [[TMEM41A]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AAAS's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers AAAS's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.0, -0.4); signed map (-20.5, -15.1). **Vector** length 67.9, 10.8% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +7.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -12.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.3 | -9.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -12.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | aladin WD repeat nucleoporin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,307,456-53,324,864 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing; Nucleoporins |
| Hallmark sets | DNA_REPAIR |
| Reactome | 73 pathways, smallest: IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus; IPs transport between nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRG9](https://www.uniprot.org/uniprotkb/Q9NRG9) (Aladin):

> Plays a role in the normal development of the peripheral and central nervous system. Required for the correct localization of aurora kinase AURKA and the microtubule minus end-binding protein NUMA1 as well as a subset of AURKA targets which ensures proper spindle formation and timely chromosome alignment.

**Summary**, from NCBI Gene [8086](https://www.ncbi.nlm.nih.gov/gene/8086):

> The protein encoded by this gene is a member of the WD-repeat family of regulatory proteins and may be involved in normal development of the peripheral and central nervous system. The encoded protein is part of the nuclear pore complex and is anchored there by NDC1. Defects in this gene are a cause of achalasia-addisonianism-alacrima syndrome (AAAS), also called triple-A syndrome or Allgrove syndrome. Two transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:13666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13666) · Entrez [8086](https://www.ncbi.nlm.nih.gov/gene/8086) · UniProt [Q9NRG9](https://www.uniprot.org/uniprotkb/Q9NRG9) · Ensembl [ENSG00000094914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000094914)

## Data

Gene col 1729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1729); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1729]; `tensor/DDL_lfc|DDL_z.npy` [1729]; `embed/gene_vectors.npy` [1729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1729 or target_col == 1729). Every well: [[AAAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AAAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
