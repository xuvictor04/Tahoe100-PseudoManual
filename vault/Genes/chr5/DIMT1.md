---
symbol: "DIMT1"
type: "gene"
col: 1455
ensembl_id: "ENSG00000086189"
name: "DIM1 rRNA methyltransferase and ribosome maturation factor"
location: "5q12.1"
module: 5
arm: "+"
pooled_cpm: 27.16
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DIMT1

*DIM1 rRNA methyltransferase and ribosome maturation factor* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +12.2, q 2e-31, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.732× (z -3.7, q 0.071, down in 11 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUM3]] (+0.68, fdr 7e-06), [[ZPR1]] (+0.68, fdr 7e-06), [[NOP16]] (+0.67, fdr 7e-06); moves opposite to [[ADGRB2]] (-0.56, fdr 3e-05), [[PLEKHH3]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADGRB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1455.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +12.2 | 2e-31 | 27/48 (NCI-H1792, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +10.4 | 8e-23 | 39/48 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +10.2 | 5e-22 | 33/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +9.4 | 8e-19 | 31/47 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +8.2 | 2e-14 | 25/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.41×** | +7.7 | 9e-13 | 27/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.7 | 2e-09 | 25/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +5.9 | 3e-07 | 18/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.29×** | +5.6 | 1e-06 | 13/47 (J82, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +5.6 | 1e-06 | 22/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +5.4 | 4e-06 | 14/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.28×** | +5.3 | 6e-06 | 17/37 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.7 | 1e-04 | 16/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.22×** | +4.4 | 4e-04 | 16/48 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | 1.19× | +4.0 | 0.003 | 17/44 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.003 | 7/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.003 | 13/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.006 | 9/47 (SW 900, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.7 | 0.007 | 14/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.012 | 8/48 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.014 | 7/47 (A-427, A549, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.016 | 9/48 (NCI-H460, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.071 | 11/46 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.071 | 6/48 (PANC-1, CHP-212, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 0.899× | -3.5 | 0.071 | 8/48 (NCI-H1792, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.071 | 9/48 (RKO, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.862× | -3.3 | 0.071 | 10/48 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.864× | -3.3 | 0.071 | 17/47 (NCI-H2030, J82, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.816×** | -3.3 | 0.071 | 13/46 (RKO, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.904× | -3.3 | 0.071 | 12/48 (RKO, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.867× | -3.3 | 0.071 | 12/48 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.959× | -3.2 | 0.087 | 2/48 (MIA PaCa-2, NCI-H2030) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.883× | -3.1 | 0.088 | 8/48 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 48.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 37.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.5) | — |
| [[A-427 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.159× (z -9.8) |
| [[C-33 A (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[H4 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.01× (z +9.1) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.1000× (z -8.5) |
| [[SNU-1 (line)]] | wt | 39.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.338× (z -9.9) |
| [[A-172 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUM3]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 | STRING 429 |
| [[ZPR1]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[NOP16]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 | STRING 427 |
| [[PNO1]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 | same gene group; pathway: rRNA modification in the nucleus and cytosol; STRING 972 |
| [[METTL8]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[DDX31]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 | STRING 641 |
| [[PRMT3]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[EEF1AKMT1]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[METTL1]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 | same gene group; STRING 805 |
| [[DHX37]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 | pathway: rRNA modification in the nucleus and cytosol; STRING 884 |
| [[WDR4]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 | STRING 441 |
| [[MAK16]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 | STRING 763 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRB2]] | -0.56 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[PLEKHH3]] | -0.53 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRB2]] | B | ADGRB2 activity raises DIMT1's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without ADGRB2 | 0.083 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[APLP1]] | B | APLP1 activity raises DIMT1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.25× lower at baseline in the lines without APLP1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.9, -35.2); signed map (-1.9, -45.4). **Vector** length 93.6, 19.6% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.52 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.4 | +10.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.3 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +12.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +3.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.5 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | DIM1 rRNA methyltransferase and ribosome maturation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:62,347,284-62,403,943 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSA9761; previously DIMT1L |
| Gene groups (HGNC) | Ribosome biogenesis factors; 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: rRNA modification in the nucleus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNQ2](https://www.uniprot.org/uniprotkb/Q9UNQ2) (Dimethyladenosine transferase):

> Specifically dimethylates two adjacent adenosines in the loop of a conserved hairpin near the 3'-end of 18S rRNA in the 40S particle. Involved in the pre-rRNA processing steps leading to small-subunit rRNA production independently of its RNA-modifying catalytic activity. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal …

**Summary**, from NCBI Gene [27292](https://www.ncbi.nlm.nih.gov/gene/27292):

> The protein encoded by this gene is a methyltransferase that is responsible for dimethylation of adjacent adenosines near the 18S rRNA decoding site. The encoded protein is essential for ribosome biogenesis, although its catalytic activity is not involved in the process. The yeast ortholog of this protein functions in the cytoplasm while this protein functions in the nucleus. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:30217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30217) · Entrez [27292](https://www.ncbi.nlm.nih.gov/gene/27292) · UniProt [Q9UNQ2](https://www.uniprot.org/uniprotkb/Q9UNQ2) · Ensembl [ENSG00000086189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086189)

## Data

Gene col 1455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1455); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1455]; `tensor/DDL_lfc|DDL_z.npy` [1455]; `embed/gene_vectors.npy` [1455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1455 or target_col == 1455). Every well: [[DIMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
