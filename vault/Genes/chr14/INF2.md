---
symbol: "INF2"
type: "gene"
col: 12769
ensembl_id: "ENSG00000203485"
name: "inverted formin 2"
location: "14q32.33"
module: 2
arm: "+"
pooled_cpm: 49.46
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# INF2

*inverted formin 2* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.75× (z +8.6, q 3e-15, up in 26 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bentamapimod (drug)]] 0.05 µM: 1.30× (z +3.9, q 0.009, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.587× (z -12.1, q 9e-31, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEC]] (+0.65, fdr 7e-06), [[SH3BP2]] (+0.65, fdr 9e-06), [[RIPOR1]] (+0.65, fdr 7e-06); moves opposite to [[HOXA5]] (-0.50, fdr 3e-05), [[NDUFC1]] (-0.48, fdr 1e-04), [[C2orf42]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EPS8L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +8.6 | 3e-15 | 26/36 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +8.6 | 3e-15 | 33/46 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.9 | 2e-04 | 20/38 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.5 | 9e-04 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.009 | 17/47 (J82, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.25 | 16/48 (AsPC-1, SNU-423, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -12.1 | 9e-31 | 39/48 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.716×** | -7.6 | 9e-12 | 26/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.672×** | -6.4 | 3e-08 | 29/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -6.0 | 3e-07 | 29/49 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.782×** | -5.6 | 3e-06 | 30/48 (J82, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.750×** | -4.6 | 3e-04 | 24/47 (SW1417, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -4.5 | 5e-04 | 24/48 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.757×** | -4.5 | 5e-04 | 23/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.595×** | -4.4 | 8e-04 | 23/46 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.766×** | -4.3 | 1e-03 | 22/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.768×** | -4.1 | 0.002 | 20/47 (AN3 CA, C-33 A, …) | top dose only | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.784×** | -3.9 | 0.004 | 18/47 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.784×** | -3.9 | 0.004 | 19/47 (AN3 CA, SW 1271, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -3.8 | 0.006 | 21/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.791×** | -3.8 | 0.006 | 21/48 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.792×** | -3.8 | 0.006 | 20/48 (HOP62, A-172, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.801×** | -3.6 | 0.011 | 17/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.861× | -3.4 | 0.021 | 13/48 (CFPAC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.1 | 0.049 | 16/48 (PANC-1, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 52.8 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -13.0) |
| [[SW480 (line)]] | alt | 77.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -14.9) |
| [[LoVo (line)]] | wt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 82.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 42.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.8) |
| [[RKO (line)]] | wt | 32.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 44.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -14.9) |
| [[A-427 (line)]] | wt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.8) |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0486× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 149 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -10.0) |
| [[HCT15 (line)]] | alt | 77.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 62.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -8.5) |
| [[HT-29 (line)]] | alt | 69.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 52.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -8.8) |
| [[KATO III (line)]] | alt | 57.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.3) |
| [[LS 180 (line)]] | wt | 58.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -11.7) |
| [[SNU-1 (line)]] | wt | 52.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -12.7) |
| [[A-172 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEC]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SH3BP2]] | +0.65 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[RIPOR1]] | +0.65 | +0.63 / +0.70 | both halves | 7e-06 | same gene group |
| [[ITPR3]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[NCOR2]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CEP170B]] | +0.61 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ARHGDIA]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 | STRING 508 |
| [[ABCA2]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 | same gene group |
| [[FAAP100]] | +0.58 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[MAPKAPK3]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MAPK11]] | +0.58 | +0.55 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA5]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[NDUFC1]] | -0.48 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[C2orf42]] | -0.48 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[PCF11-AS1]] | -0.48 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[HOXA6]] | -0.46 | -0.31 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L2]] | B | EPS8L2 activity raises INF2's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without EPS8L2 | 0.003 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[SH3BP2]] | B | SH3BP2 activity raises INF2's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without SH3BP2 | 0.025 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises INF2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLCO4A1]] | B | SLCO4A1 activity raises INF2's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without SLCO4A1 | 0.067 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[PKP3]] | B | PKP3 activity raises INF2's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.53× lower at baseline in the lines without PKP3 | 0.098 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[PLEC]] | C | PLEC activity raises INF2's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.49× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (15.2, -4.8); signed map (-10.8, 30.4). **Vector** length 102, 24.7% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.2 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +1.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.6 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.6 | -5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -6.0 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.8 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.4 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | inverted formin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:104,681,146-104,722,535 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13251; previously C14orf151, C14orf173 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q27J81](https://www.uniprot.org/uniprotkb/Q27J81) (Inverted formin-2):

> Severs actin filaments and accelerates their polymerization and depolymerization.

**Summary**, from NCBI Gene [64423](https://www.ncbi.nlm.nih.gov/gene/64423):

> This gene represents a member of the formin family of proteins. It is considered a diaphanous formin due to the presence of a diaphanous inhibitory domain located at the N-terminus of the encoded protein. Studies of a similar mouse protein indicate that the protein encoded by this locus may function in polymerization and depolymerization of actin filaments. Mutations at this locus have been associated with focal segmental glomerulosclerosis 5.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:23791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23791) · Entrez [64423](https://www.ncbi.nlm.nih.gov/gene/64423) · UniProt [Q27J81](https://www.uniprot.org/uniprotkb/Q27J81) · Ensembl [ENSG00000203485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203485)

## Data

Gene col 12769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12769); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12769]; `tensor/DDL_lfc|DDL_z.npy` [12769]; `embed/gene_vectors.npy` [12769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12769 or target_col == 12769). Every well: [[INF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
