---
symbol: "GRWD1"
type: "gene"
col: 2606
ensembl_id: "ENSG00000105447"
name: "glutamate rich WD repeat containing 1"
location: "19q13.33"
module: 5
arm: "+"
pooled_cpm: 14.32
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# GRWD1

*glutamate rich WD repeat containing 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.46× (z +11.0, q 2e-25, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.698× (z -4.4, q 0.003, down in 22 of 47 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.699× (z -4.4, q 0.003, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BYSL]] (+0.86, fdr 7e-06), [[WDR4]] (+0.79, fdr 7e-06), [[TWNK]] (+0.79, fdr 7e-06); moves opposite to [[CCNI]] (-0.66, fdr 1e-05), [[MINDY2]] (-0.66, fdr 7e-06), [[ZCRB1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.46×** | +11.0 | 2e-25 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.27×** | +10.0 | 3e-21 | 42/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.75×** | +10.0 | 4e-21 | 44/46 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +9.8 | 1e-20 | 38/46 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.14×** | +9.3 | 1e-18 | 39/47 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +8.8 | 1e-16 | 34/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.00×** | +8.4 | 2e-15 | 35/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +8.3 | 5e-15 | 37/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +8.2 | 1e-14 | 32/47 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +8.2 | 1e-14 | 41/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.04×** | +7.1 | 6e-11 | 32/44 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +6.3 | 2e-08 | 33/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +6.2 | 3e-08 | 32/47 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +6.2 | 3e-08 | 29/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.70×** | +6.0 | 7e-08 | 17/29 (NCI-H460, SW480, …) | inconsistent across doses | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.67×** | +5.8 | 2e-07 | 27/43 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.4 | 2e-06 | 25/46 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +5.1 | 1e-05 | 19/45 (HS-578T, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.698×** | -4.4 | 0.003 | 22/47 (NCI-H661, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.699×** | -4.4 | 0.003 | 20/46 (H4, HT-29, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.041 | 17/46 (A-427, BT-474, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.758×** | -3.4 | 0.082 | 17/47 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -3.4 | 0.088 | 18/48 (RPMI-7951, H4, …) | two highest doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.836× | -3.1 | 0.15 | 10/48 (C-33 A, A-427, …) | rises with dose | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.780× | -3.1 | 0.15 | 11/47 (NCI-H23, SW 1271, …) | two highest doses |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.841× | -3.0 | 0.15 | 12/48 (CHP-212, NCI-H661, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.783× | -3.0 | 0.15 | 11/47 (LS 180, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.785× | -3.0 | 0.15 | 5/48 (A-427, HCT15, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 18.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 18.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0764× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.576× (z -10.1) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0879× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0697× (z -11.0) |
| [[SW480 (line)]] | alt | 20.4 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.01× (z +8.5) | — |
| [[A-172 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BYSL]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 958 |
| [[WDR4]] | +0.79 | +0.78 / +0.78 | both halves | 7e-06 | same gene group; STRING 712 |
| [[TWNK]] | +0.79 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.79 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[PUF60]] | +0.78 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[DHX37]] | +0.78 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[NIP7]] | +0.77 | +0.73 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 919 |
| [[ABCF2]] | +0.77 | +0.79 / +0.72 | both halves | 7e-06 | STRING 474 |
| [[PUS1]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[POLR1A]] | +0.75 | +0.81 / +0.72 | both halves | 7e-06 | STRING 858 |
| [[MYBBP1A]] | +0.74 | +0.81 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 904 |
| [[LTV1]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | STRING 805 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNI]] | -0.66 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[MINDY2]] | -0.66 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[ZCRB1]] | -0.65 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.64 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.63 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[ARL3]] | -0.63 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[HADHB]] | -0.62 | -0.50 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises GRWD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.809). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.6, -35.0); signed map (-1.5, -46.0). **Vector** length 92.6, 21.8% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.61 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.61 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.62 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +10.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.4 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | glutamate rich WD repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,445,841-48,457,022 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WDR28, GRWD, RRB1 |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | MYC_TARGETS_V2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ67](https://www.uniprot.org/uniprotkb/Q9BQ67) (Glutamate-rich WD repeat-containing protein 1):

> Histone binding protein that regulates chromatin dynamics and loading of minichromosome maintenance (MCM) complex at replication origins, possibly by promoting chromatin openness. Plays a role in ribosomal biogenesis.

**Summary**, from NCBI Gene [83743](https://www.ncbi.nlm.nih.gov/gene/83743):

> This gene encodes a glutamate-rich protein that contains five WD-repeat motifs. The encoded protein may play a critical role in ribosome biogenesis and may also play a role in histone methylation through interactions with CUL4-DDB1 ubiquitin E3 ligase. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:21270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21270) · Entrez [83743](https://www.ncbi.nlm.nih.gov/gene/83743) · UniProt [Q9BQ67](https://www.uniprot.org/uniprotkb/Q9BQ67) · Ensembl [ENSG00000105447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105447)

## Data

Gene col 2606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2606); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2606]; `tensor/DDL_lfc|DDL_z.npy` [2606]; `embed/gene_vectors.npy` [2606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2606 or target_col == 2606). Every well: [[GRWD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRWD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
