---
symbol: "CROCCP3"
type: "gene"
col: 1298
ensembl_id: "ENSG00000080947"
name: "CROCC pseudogene 3"
location: "1p36.13"
module: 2
arm: "+"
pooled_cpm: 3.43
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CROCCP3

*CROCC pseudogene 3* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +4.0, q 0.031, up in 9 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.319× (z -11.5, q 4e-28, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CROCCP3-1]] (+0.78, fdr 7e-06, ⚠ same locus), [[SEMA4F]] (+0.71, fdr 7e-06), [[CRLF3]] (+0.68, fdr 7e-06), [[RTN4R]] (+0.63, fdr 1e-05); moves opposite to [[PTPRK]] (-0.61, fdr 3e-05), [[RIPK2-DT]] (-0.61, fdr 3e-05), [[PLCH1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PTPRB]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NCOA7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.031 | 9/43 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.053 | 10/42 (LS 180, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 1.39× | +3.3 | 0.16 | 8/39 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.35× | +3.2 | 0.21 | 1/45 (A-427) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.21 | 5/32 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.35× | +3.0 | 0.21 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.319×** | -11.5 | 4e-28 | 32/42 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.506×** | -10.1 | 1e-21 | 24/35 (A549, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -7.9 | 5e-13 | 20/34 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.545×** | -6.4 | 3e-08 | 21/43 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.547×** | -6.3 | 3e-08 | 16/40 (HOP62, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.635×** | -4.8 | 2e-04 | 19/33 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.636×** | -4.8 | 2e-04 | 16/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -4.6 | 3e-04 | 13/34 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.637×** | -4.6 | 3e-04 | 16/27 (HOP62, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.653×** | -4.5 | 4e-04 | 14/43 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.482×** | -4.0 | 0.003 | 7/32 (HS-578T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -4.0 | 0.003 | 14/42 (A498, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.686×** | -3.9 | 0.003 | 15/41 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.7 | 0.009 | 13/46 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.711×** | -3.6 | 0.013 | 13/43 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Aliskiren (drug)]] 0.5 µM |  | **0.747×** | -3.1 | 0.075 | 6/43 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.575×** | -3.0 | 0.076 | 4/38 (SHP-77, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.83 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -11.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0595× (z -10.1) |
| [[HOP62 (line)]] | alt | 5.35 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0537× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.125× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 5.89 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0759× (z -9.5) |
| [[A-427 (line)]] | wt | 6.78 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 3.89 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0561× (z -13.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HS-578T (line)]] | alt | 4.96 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0833× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 3.22 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0754× (z -12.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 3.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -10.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3-1]] | +0.78 | +0.73 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SEMA4F]] | +0.71 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CRLF3]] | +0.68 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[RTN4R]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PACS2]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[STX2]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[E4F1]] | +0.62 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[LRFN3]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CORO7]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SLC41A3]] | +0.61 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SLC15A4]] | +0.61 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[ZNF341]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | -0.61 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.61 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[PLCH1]] | -0.59 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[LACTB2]] | -0.59 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[TBCK]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[FBXW10B]] | -0.56 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[UBQLN2]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ARHGAP42]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[CASC9]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MCTS1]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[LINC00571]] | -0.54 | -0.53 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRB]] | B | PTPRB activity lowers CROCCP3's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.34× higher at baseline in the lines without PTPRB | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[RIMS3]] | B | RIMS3 activity raises CROCCP3's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without RIMS3 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[NT5M]] | B | NT5M activity raises CROCCP3's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without NT5M | 0.049 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[GNAZ]] | B | GNAZ activity raises CROCCP3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.22× lower at baseline in the lines without GNAZ | 0.080 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCOA7]] | C | CROCCP3's natural level weakens NCOA7's drug response | CROCCP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.22; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (1.0, -0.4); signed map (-44.0, -5.2). **Vector** length 52.3, 6.69% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +1.9 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.2 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.8 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.1 | -10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | CROCC pseudogene 3 |
| Locus type | pseudogene |
| Location | 1p36.13 — chr1:16,474,396-16,491,307 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | KIAA1922; previously CROCCL2 |
| Matched by | ensembl_id |

UniProt [Q8IVE0](https://www.uniprot.org/uniprotkb/Q8IVE0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29405) · Entrez [114819](https://www.ncbi.nlm.nih.gov/gene/114819) · UniProt [Q8IVE0](https://www.uniprot.org/uniprotkb/Q8IVE0) · Ensembl [ENSG00000080947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080947)

## Data

Gene col 1298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1298); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1298]; `tensor/DDL_lfc|DDL_z.npy` [1298]; `embed/gene_vectors.npy` [1298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1298 or target_col == 1298). Every well: [[CROCCP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CROCCP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
