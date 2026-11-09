---
symbol: "RIDA"
type: "gene"
col: 5336
ensembl_id: "ENSG00000132541"
name: "reactive intermediate imine deaminase A"
location: "8q22.2"
module: 17
arm: "+"
pooled_cpm: 8.53
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# RIDA

*reactive intermediate imine deaminase A* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.64× (z +15.0, q 0e+00, up in 30 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.64× (z +8.1, q 6e-14, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.415× (z -10.2, q 2e-21, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BPNT1]] (+0.57, fdr 1e-05), [[COX15]] (+0.55, fdr 1e-05), [[GSTA4]] (+0.54, fdr 1e-05); moves opposite to [[TUBB4B]] (-0.50, fdr 2e-04), [[ATP8B5P-1]] (-0.49, fdr 1e-04), [[DRAP1]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.64×** | +15.0 | 0e+00 | 30/31 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +13.3 | 9e-38 | 15/15 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +10.0 | 3e-21 | 20/22 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +8.1 | 6e-14 | 31/48 (NCI-H2347, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.01×** | +8.1 | 6e-14 | 32/47 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.94×** | +7.7 | 1e-12 | 35/47 (A498, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.88×** | +7.3 | 2e-11 | 30/47 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.3 | 3e-11 | 27/43 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.64×** | +5.5 | 2e-06 | 24/41 (SW480, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.8 | 1e-04 | 18/46 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +4.4 | 5e-04 | 15/46 (A498, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.4 | 5e-04 | 18/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.3 | 7e-04 | 11/46 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.45×** | +4.1 | 0.001 | 19/36 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.42×** | +3.9 | 0.003 | 14/42 (SW480, HEC-1-A, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.013 | 10/46 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.026 | 11/45 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.045 | 5/47 (PANC-1, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.415×** | -10.2 | 2e-21 | 38/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.449×** | -9.3 | 6e-18 | 36/46 (COLO 205, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -7.2 | 1e-10 | 29/46 (HCT15, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -6.4 | 2e-08 | 25/44 (HCT15, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -5.6 | 2e-06 | 24/43 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.447×** | -4.9 | 1e-04 | 17/46 (Panc 03.27, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -4.4 | 9e-04 | 16/43 (COLO 205, A498, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.792×** | -3.8 | 0.010 | 17/44 (KATO III, HCT15, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.725×** | -3.7 | 0.013 | 13/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.758×** | -3.2 | 0.078 | 9/47 (HepG2/C3A, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 16.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PF-06260933 (drug)]] 5 µM 0.0374× (z -11.1) |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0584× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0722× (z -10.4) |
| [[PANC-1 (line)]] | alt | 7.97 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -9.2) |
| [[SW480 (line)]] | alt | 10.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.4) | — |
| [[A498 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 6.07 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.51× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0924× (z -8.9) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.75× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 9.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0842× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 5.25 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0779× (z -9.1) |
| [[A-172 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPNT1]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[COX15]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[GSTA4]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MRS2]] | +0.52 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[MIGA1]] | +0.52 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[ARL5A]] | +0.52 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[TFG]] | +0.52 | +0.27 / +0.45 | both halves | 3e-04 |  |
| [[PPP1CB]] | +0.51 | +0.29 / +0.35 | both halves | 2e-04 |  |
| [[CRYZ]] | +0.51 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[PMS2]] | +0.51 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[CIAO2A]] | +0.51 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[UBA5]] | +0.50 | +0.32 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB4B]] | -0.50 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[ATP8B5P-1]] | -0.49 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[DRAP1]] | -0.48 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[TNFRSF12A]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[S100A11]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MYL12B]] | -0.46 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[CLCF1]] | -0.46 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MYL12A]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[TJP1]] | -0.46 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[LCAT]] | -0.45 | -0.25 / -0.41 | both halves | 4e-04 |  |
| [[CARD10]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SLC12A4]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RIDA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.332). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-18.8, -4.9); signed map (-30.7, -15.9). **Vector** length 52.5, 7.27% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.1 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +10.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | reactive intermediate imine deaminase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:98,102,344-98,117,171 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UK114, P14.5, PSP; previously HRSP12 |
| Reactome | 1 pathways, smallest: Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P52758](https://www.uniprot.org/uniprotkb/P52758) (2-iminobutanoate/2-iminopropanoate deaminase):

> Catalyzes the hydrolytic deamination of enamine/imine intermediates that form during the course of normal metabolism. May facilitate the release of ammonia from these potentially toxic reactive metabolites, reducing their impact on cellular components. It may act on enamine/imine intermediates formed by several types of pyridoxal-5'-phosphate-dependent dehydratases including L-threonine dehydratase.; Also promotes endoribonucleolytic cleavage of some transcripts by promoting recruitment of the …

**Summary**, from NCBI Gene [10247](https://www.ncbi.nlm.nih.gov/gene/10247):

> Enables mRNA binding activity. Involved in mRNA catabolic process and mRNA destabilization. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16897) · Entrez [10247](https://www.ncbi.nlm.nih.gov/gene/10247) · UniProt [P52758](https://www.uniprot.org/uniprotkb/P52758) · Ensembl [ENSG00000132541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132541)

## Data

Gene col 5336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5336); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5336]; `tensor/DDL_lfc|DDL_z.npy` [5336]; `embed/gene_vectors.npy` [5336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5336 or target_col == 5336). Every well: [[RIDA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIDA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
