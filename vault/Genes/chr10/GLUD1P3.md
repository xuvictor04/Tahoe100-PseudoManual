---
symbol: "GLUD1P3"
type: "gene"
col: 14723
ensembl_id: "ENSG00000250959"
name: "glutamate dehydrogenase 1 pseudogene 3"
location: "10q22.2"
module: 15
arm: "+"
pooled_cpm: 5.52
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GLUD1P3

*glutamate dehydrogenase 1 pseudogene 3* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.01× (z +19.6, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.517× (z -11.8, q 3e-29, down in 29 of 39 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.659× (z -5.3, q 2e-05, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN10-DT]] (+0.72, fdr 9e-06), [[TMEM11-DT]] (+0.70, fdr 9e-06), [[WDR20]] (+0.69, fdr 7e-06); moves opposite to [[C1orf226]] (-0.59, fdr 1e-05), [[DHRS2]] (-0.58, fdr 5e-05), [[TPPP]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +19.6 | 0e+00 | 38/41 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.5 | 3e-08 | 14/37 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.7 | 2e-06 | 12/39 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.9 | 1e-04 | 12/31 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +4.3 | 0.002 | 9/44 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.27×** | +4.2 | 0.002 | 10/47 (SNU-423, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 14/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.003 | 10/45 (HEC-1-A, CFPAC-1, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +3.8 | 0.010 | 6/39 (NCI-H1573, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.099 | 3/46 (SW480, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.0 | 0.13 | 0/45 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.517×** | -11.8 | 3e-29 | 29/39 (AsPC-1, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.505×** | -8.3 | 3e-14 | 29/44 (NCI-H1792, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.591×** | -6.4 | 3e-08 | 20/32 (LS 180, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.658×** | -5.3 | 2e-05 | 17/28 (SW1417, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.659×** | -5.3 | 2e-05 | 16/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.727×** | -3.8 | 0.014 | 14/39 (A549, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -3.6 | 0.021 | 9/46 (Panc 03.27, AN3 CA, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.750×** | -3.4 | 0.044 | 13/44 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.071 | 10/44 (LS 180, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.61 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 4.58 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0634× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.0661× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 6.59 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-172 (line)]] | wt | 8.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 6.69 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 4.54 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -9.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[AsPC-1 (line)]] | alt | 5.99 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -14.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HOP62 (line)]] | alt | 6.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 6.63 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0572× (z -11.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 5.74 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0537× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 5.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 8.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +11.3) | — |
| [[A-427 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN10-DT]] | +0.72 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[TMEM11-DT]] | +0.70 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[WDR20]] | +0.69 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ZNF75D]] | +0.69 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ISY1]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PGS1]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ZNF394]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[POC1B-AS1]] | +0.68 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[PPP1R26-AS1]] | +0.67 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[ANKRD42-DT]] | +0.67 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[UBOX5]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ZNF213-AS1]] | +0.65 | +0.25 / +0.75 | both halves | 4e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf226]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[DHRS2]] | -0.58 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[TPPP]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[THEM6]] | -0.57 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[KLF11]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[FGGY]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[EFR3A]] | -0.56 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[COMMD8]] | -0.56 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[RFK]] | -0.55 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[NAPRT]] | -0.55 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[THOP1]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GLUD1P3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.7, 21.7); signed map (3.4, -0.8). **Vector** length 66.2, 9.96% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +19.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +0.9 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.2 | -11.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.3 | -8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.4 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -3.0 | -6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | glutamate dehydrogenase 1 pseudogene 3 |
| Locus type | pseudogene |
| Location | 10q22.2 — chr10:73,731,176-73,737,311 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | Em:AC022400.11; previously GLUDP3, C10orf102 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:4338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4338) · Entrez [2749](https://www.ncbi.nlm.nih.gov/gene/2749) · Ensembl [ENSG00000250959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250959)

## Data

Gene col 14723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14723); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14723]; `tensor/DDL_lfc|DDL_z.npy` [14723]; `embed/gene_vectors.npy` [14723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14723 or target_col == 14723). Every well: [[GLUD1P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLUD1P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
