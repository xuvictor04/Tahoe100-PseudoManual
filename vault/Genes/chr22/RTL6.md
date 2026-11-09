---
symbol: "RTL6"
type: "gene"
col: 12033
ensembl_id: "ENSG00000188636"
name: "retrotransposon Gag like 6"
location: "22q13.31"
module: 16
arm: "+"
pooled_cpm: 7.43
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# RTL6

*retrotransposon Gag like 6* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.36× (z +10.7, q 6e-24, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.394× (z -17.1, q 0e+00, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35A4]] (+0.83, fdr 7e-06), [[CENPBD1P]] (+0.76, fdr 7e-06), [[CSTF2T]] (+0.76, fdr 7e-06); moves opposite to [[SNHG30]] (-0.68, fdr 7e-06), [[SRP54-AS1]] (-0.67, fdr 7e-06), [[KDELR1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARNT2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +10.7 | 6e-24 | 31/45 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +9.8 | 2e-20 | 33/40 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +8.8 | 3e-16 | 27/44 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.1 | 8e-14 | 30/45 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +6.5 | 7e-09 | 6/47 (NCI-H23, COLO 205, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +5.6 | 2e-06 | 19/45 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.0 | 4e-05 | 13/35 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.035 | 7/46 (HS-578T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.041 | 11/44 (LS 180, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12033.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.394×** | -17.1 | 0e+00 | 35/42 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -8.0 | 3e-13 | 26/42 (HOP62, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -8.0 | 3e-13 | 27/42 (RPMI-7951, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -7.3 | 4e-11 | 26/46 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -5.0 | 6e-05 | 16/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -4.8 | 2e-04 | 15/45 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.710×** | -4.3 | 0.002 | 16/45 (NCI-H1573, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.723×** | -4.2 | 0.002 | 21/45 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.731×** | -3.9 | 0.006 | 7/45 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.747×** | -3.8 | 0.009 | 13/46 (J82, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.019 | 13/44 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.771×** | -3.2 | 0.056 | 14/33 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.066 | 10/46 (C-33 A, NCI-H661, …) | rises with dose |  |
| [[Trimetrexate (drug)]] 5 µM |  | 0.843× | -3.1 | 0.066 | 7/45 (NCI-H460, NCI-H661, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.786×** | -3.1 | 0.066 | 11/44 (Hs 766T, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.10 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -13.2) |
| [[HS-578T (line)]] | alt | 13.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -12.6) |
| [[PANC-1 (line)]] | alt | 5.55 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.3) |
| [[A498 (line)]] | wt | 9.10 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.75× (z +8.9) | — |
| [[J82 (line)]] | alt | 9.38 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.8) |
| [[LoVo (line)]] | wt | 7.34 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 9.79 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0674× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 5.20 | 0 | 2 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0518× (z -11.1) |
| [[A-172 (line)]] | wt | 7.42 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 4.69 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -9.4) |
| [[C32 (line)]] | wt | 6.33 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0897× (z -8.8) |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0951× (z -8.7) |
| [[Hs 766T (line)]] | wt | 5.40 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 7.87 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 8.13 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.165× (z -8.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 9.65 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0892× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[Panc 03.27 (line)]] | alt | 5.31 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0644× (z -9.9) |
| [[RKO (line)]] | wt | 8.06 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 8.54 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0734× (z -11.1) |
| [[SW1417 (line)]] | alt | 4.47 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.102× (z -8.5) |
| [[A-427 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | +0.83 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.76 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.76 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.74 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.74 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[ZNF776]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[PUF60]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[THAP5]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG30]] | -0.68 | -0.74 / -0.60 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.67 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.67 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[ZBTB47-AS1]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[ZNF710-AS1]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[PIK3C2A]] | -0.65 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[SMG1P5]] | -0.63 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[GNRH1]] | -0.63 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[NAP1L4]] | -0.63 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.62 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[UQCRH]] | -0.62 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | -0.62 | -0.69 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARNT2]] | B | ARNT2 activity raises RTL6's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 1.31× lower at baseline in the lines without ARNT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[TOP2A]] | B | TOP2A activity raises RTL6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.859). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.1, 11.9); signed map (1.4, -29.5). **Vector** length 84.3, 15.5% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +9.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -17.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -8.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | retrotransposon Gag like 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:44,492,583-44,498,233 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1033E15.2, DKFZp761O17121, Mart6, Mar6, SIRH3; previously LDOC1L |
| Gene groups (HGNC) | Retrotransposon Gag like family |
| Matched by | ensembl_id |

UniProt [Q6ICC9](https://www.uniprot.org/uniprotkb/Q6ICC9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:13343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13343) · Entrez [84247](https://www.ncbi.nlm.nih.gov/gene/84247) · UniProt [Q6ICC9](https://www.uniprot.org/uniprotkb/Q6ICC9) · Ensembl [ENSG00000188636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188636)

## Data

Gene col 12033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12033); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12033]; `tensor/DDL_lfc|DDL_z.npy` [12033]; `embed/gene_vectors.npy` [12033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12033 or target_col == 12033). Every well: [[RTL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
