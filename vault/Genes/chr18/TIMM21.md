---
symbol: "TIMM21"
type: "gene"
col: 1113
ensembl_id: "ENSG00000075336"
name: "translocase of inner mitochondrial membrane 21"
location: "18q22.3"
module: 5
arm: "+"
pooled_cpm: 13.14
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TIMM21

*translocase of inner mitochondrial membrane 21* — 18q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +10.4, q 1e-22, up in 33 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.61× (z +6.5, q 1e-08, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.637× (z -8.6, q 4e-15, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARG]] (+0.62, fdr 3e-05), [[TSR1]] (+0.61, fdr 1e-05), [[SNRPC]] (+0.61, fdr 1e-05); moves opposite to [[HES4]] (-0.59, fdr 1e-05), [[JUND]] (-0.58, fdr 2e-05), [[HDAC5]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.15×** | +10.4 | 1e-22 | 33/39 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.00×** | +9.0 | 4e-17 | 16/21 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +7.3 | 6e-11 | 28/39 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +6.5 | 1e-08 | 27/46 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +6.4 | 2e-08 | 27/47 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.53×** | +5.3 | 9e-06 | 16/28 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.50×** | +5.3 | 9e-06 | 23/47 (NCI-H460, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +5.2 | 1e-05 | 18/42 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +5.1 | 2e-05 | 22/45 (NCI-H460, C32, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.46×** | +4.9 | 5e-05 | 20/45 (A-172, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.0 | 0.003 | 12/46 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.21×** | +3.7 | 0.009 | 15/47 (PANC-1, SHP-77, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.009 | 12/47 (A-172, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.026 | 7/45 (A-427, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.055 | 3/46 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.0 | 0.081 | 5/45 (PANC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.095 | 5/46 (Hs 766T, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.637×** | -8.6 | 4e-15 | 26/46 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.633×** | -6.2 | 2e-07 | 27/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.729×** | -6.0 | 3e-07 | 28/47 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.706×** | -4.7 | 4e-04 | 20/46 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.714×** | -4.6 | 6e-04 | 16/46 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.710×** | -4.4 | 8e-04 | 20/46 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.730×** | -4.2 | 0.002 | 22/45 (hTERT-HPNE, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.772×** | -3.5 | 0.034 | 19/46 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 18.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +8.7) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 10.4 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 32.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -9.6) |
| [[H4 (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -8.9) |
| [[HS-578T (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 4.78 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0773× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0858× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -11.3) |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.226× (z -8.5) |
| [[A-172 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARG]] | +0.62 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[TSR1]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SNRPC]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TTI1]] | +0.60 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TSN]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZNF343]] | +0.60 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[CDC123]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TOPBP1]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SUPV3L1]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SAMM50]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 | pathway: Mitochondrial protein import; STRING 772 |
| [[NAT10]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[HSPA14]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES4]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[JUND]] | -0.58 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[HDAC5]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MAFK]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GPX4]] | -0.55 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[PNPLA2]] | -0.54 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[OLFM2]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PIM3]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[KLF2]] | -0.53 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[TUBB2A]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[LLGL2]] | -0.52 | -0.59 / -0.24 | both halves | 5e-04 |  |
| [[OAZ1]] | -0.51 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TIMM21's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.7, -35.1); signed map (-33.0, -26.1). **Vector** length 72.0, 12.8% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.2 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -4.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.3 — chr18:74,148,523-74,160,531 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC154, TIM21; previously C18orf55 |
| Gene groups (HGNC) | TIM23 complex |
| Reactome | 5 pathways, smallest: Complex IV assembly; Mitochondrial protein import; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVV7](https://www.uniprot.org/uniprotkb/Q9BVV7) (Mitochondrial import inner membrane translocase subunit Tim21):

> Participates in the translocation of transit peptide-containing proteins across the mitochondrial inner membrane. Also required for assembly of mitochondrial respiratory chain complex I and complex IV as component of the MITRAC (mitochondrial translation regulation assembly intermediate of cytochrome c oxidase complex) complex. Probably shuttles between the presequence translocase and respiratory-chain assembly intermediates in a process that promotes incorporation of early nuclear-encoded …

**Summary**, from NCBI Gene [29090](https://www.ncbi.nlm.nih.gov/gene/29090):

> Involved in mitochondrial respiratory chain complex I assembly; mitochondrial respiratory chain complex IV assembly; and protein import into mitochondrial matrix. Located in mitochondrion. Part of TIM23 mitochondrial import inner membrane translocase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25010) · Entrez [29090](https://www.ncbi.nlm.nih.gov/gene/29090) · UniProt [Q9BVV7](https://www.uniprot.org/uniprotkb/Q9BVV7) · Ensembl [ENSG00000075336](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075336)

## Data

Gene col 1113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1113); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1113]; `tensor/DDL_lfc|DDL_z.npy` [1113]; `embed/gene_vectors.npy` [1113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1113 or target_col == 1113). Every well: [[TIMM21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
