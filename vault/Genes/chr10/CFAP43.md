---
symbol: "CFAP43"
type: "gene"
col: 12453
ensembl_id: "ENSG00000197748"
name: "cilia and flagella associated protein 43"
location: "10q25.1"
module: 23
arm: "+"
pooled_cpm: 6.5
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 19
n_dd_up_clean: 29
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CFAP43

*cilia and flagella associated protein 43* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.61× (z +23.1, q 0e+00, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.344× (z -10.0, q 5e-21, down in 35 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.511× (z -6.3, q 7e-08, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB6]] (+0.75, fdr 7e-06), [[NIFK-AS1]] (+0.74, fdr 1e-05), [[PSMD7-DT]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.61×** | +23.1 | 0e+00 | 39/39 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.75×** | +13.6 | 2e-39 | 26/38 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.21×** | +13.1 | 7e-37 | 30/36 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.47×** | +11.8 | 7e-30 | 39/46 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.21×** | +11.1 | 2e-26 | 41/45 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.98×** | +10.3 | 4e-23 | 32/44 (LoVo, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **2.71×** | +9.5 | 3e-19 | 41/45 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +9.0 | 1e-17 | 28/38 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.9 | 2e-13 | 28/45 (A-172, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.16×** | +7.3 | 1e-11 | 32/44 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.11×** | +7.1 | 7e-11 | 31/46 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +6.6 | 2e-09 | 20/36 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.3 | 1e-08 | 18/32 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.20×** | +5.8 | 3e-07 | 18/41 (A-172, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.81×** | +5.6 | 7e-07 | 22/46 (KATO III, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +5.5 | 1e-06 | 21/38 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.344×** | -10.0 | 5e-21 | 35/45 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -6.3 | 7e-08 | 23/46 (HCT15, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.562×** | -5.4 | 1e-05 | 19/45 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.471×** | -5.1 | 6e-05 | 22/45 (Panc 03.27, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.631×** | -4.3 | 0.002 | 19/43 (HCT15, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.649×** | -4.1 | 0.005 | 16/38 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.662×** | -3.7 | 0.021 | 14/43 (MIA PaCa-2, A-427, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.487×** | -3.5 | 0.026 | 16/36 (Panc 03.27, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.488×** | -3.5 | 0.026 | 16/37 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.694×** | -3.4 | 0.034 | 14/46 (NCI-H661, SW480, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.035 | 12/43 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -3.4 | 0.035 | 14/42 (C-33 A, HCT15, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.704×** | -3.3 | 0.043 | 15/46 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.518×** | -3.2 | 0.049 | 11/37 (CFPAC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.700×** | -3.2 | 0.049 | 13/41 (PANC-1, HT-29, …) | top dose only |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.693×** | -3.2 | 0.052 | 12/43 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.531×** | -3.1 | 0.062 | 13/41 (CFPAC-1, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.068 | 4/45 (H4, PANC-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.641×** | -3.0 | 0.086 | 11/39 (A549, NCI-H23, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.04 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.28× (z +11.8) | — |
| [[LoVo (line)]] | wt | 6.56 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +15.2) | — |
| [[SW480 (line)]] | alt | 8.90 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.184× (z -9.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A-172 (line)]] | wt | 7.54 | 3 | 0 | [[Auranofin (drug)]] 5 µM 13.1× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 21.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.0844× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 18.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +9.8) ⚠ position not correctable | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 5.73 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -9.7) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 4.74 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +20.0) | — |
| [[SW 900 (line)]] | alt | 6.54 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.88× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 5.07 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +9.3) | — |
| [[J82 (line)]] | alt | 3.16 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 4.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 6.56 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +8.8) | [[Simotinib (drug)]] 5 µM 0.0801× (z -8.6) ⚠ toxic |
| [[A549 (line)]] | wt | 3.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.41× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 3.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0523× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +10.1) | — |
| [[KATO III (line)]] | alt | 7.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.02× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 5.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.08× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 9.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +9.9) | — |
| [[SW48 (line)]] | wt | 5.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +8.6) | — |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB6]] | +0.75 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[NIFK-AS1]] | +0.74 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[PSMD7-DT]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.70 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.69 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | +0.69 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[ALOX12-AS1]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.69 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[DNAI4]] | +0.69 | +0.80 / +0.48 | both halves | 2e-05 | same gene group; STRING 597 |
| [[DMXL1-DT]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[C21orf62-AS1]] | +0.68 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[CDKL3]] | +0.67 | +0.71 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFAP43's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.4, 19.6); signed map (28.3, -7.8). **Vector** length 71.5, 13.7% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +23.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +7.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +5.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | +7.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:104,129,888-104,232,364 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36006, bA373N18.2, FLJ22944; previously C10orf79, WDR96 |
| Gene groups (HGNC) | WD repeat domain containing; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDM7](https://www.uniprot.org/uniprotkb/Q8NDM7) (Cilia- and flagella-associated protein 43):

> Flagellar protein involved in sperm flagellum axoneme organization and function (By similarity). Involved in the regulation of the beating frequency of motile cilia on the epithelial cells of the respiratory tract (By similarity).

**Summary**, from NCBI Gene [80217](https://www.ncbi.nlm.nih.gov/gene/80217):

> This gene encodes a member of the cilia- and flagella-associated protein family. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:26684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26684) · Entrez [80217](https://www.ncbi.nlm.nih.gov/gene/80217) · UniProt [Q8NDM7](https://www.uniprot.org/uniprotkb/Q8NDM7) · Ensembl [ENSG00000197748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197748)

## Data

Gene col 12453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12453); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12453]; `tensor/DDL_lfc|DDL_z.npy` [12453]; `embed/gene_vectors.npy` [12453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12453 or target_col == 12453). Every well: [[CFAP43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
