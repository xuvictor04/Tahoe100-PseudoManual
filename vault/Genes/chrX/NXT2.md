---
symbol: "NXT2"
type: "gene"
col: 2186
ensembl_id: "ENSG00000101888"
name: "nuclear transport factor 2 like export factor 2"
location: "Xq23"
module: 3
arm: "-"
pooled_cpm: 5.57
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# NXT2

*nuclear transport factor 2 like export factor 2* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.71× (z +15.8, q 0e+00, up in 35 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.780× (z -3.9, q 0.047, down in 14 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0602×); [[Harringtonine (drug)]] 0.05 µM in 1 line (C-33 A 0.0764×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.107×; ⚠ toxic); [[Trimetrexate (drug)]] 0.5 µM in 1 line (HT-29 0.0526×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4G2]] (+0.73, fdr 7e-06), [[GBA1]] (+0.73, fdr 7e-06), [[PDIA3P1]] (+0.71, fdr 7e-06); moves opposite to [[RPL36]] (-0.66, fdr 1e-05), [[RPS26]] (-0.65, fdr 4e-05), [[E4F1]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +15.8 | 0e+00 | 35/39 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.18×** | +15.4 | 0e+00 | 7/7 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.66×** | +14.5 | 1e-45 | 25/27 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.33×** | +13.5 | 3e-39 | 39/44 (SNU-423, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +10.7 | 8e-25 | 10/11 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +8.8 | 1e-16 | 30/45 (SW480, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.4 | 4e-15 | 26/46 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +7.3 | 3e-11 | 23/38 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.0 | 9e-08 | 18/38 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.3 | 7e-06 | 18/40 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.54×** | +4.8 | 7e-05 | 14/46 (BT-474, PANC-1, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.4 | 5e-04 | 7/29 (NCI-H23, SNU-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.002 | 14/36 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.45×** | +4.0 | 0.003 | 9/31 (J82, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.003 | 16/43 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.016 | 7/44 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.042 | 9/43 (SW1417, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.054 | 5/45 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.088 | 8/44 (SNU-423, C-33 A, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2186.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0602×); [[Harringtonine (drug)]] 0.05 µM in 1 line (C-33 A 0.0764×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.107×; ⚠ toxic); [[Trimetrexate (drug)]] 0.5 µM in 1 line (HT-29 0.0526×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.780×** | -3.9 | 0.047 | 14/45 (NCI-H1573, SW 900, …) | top dose only |  |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.827× | -3.0 | 0.73 | 11/45 (SNU-1, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 26.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.26× (z +11.2) | — |
| [[SW480 (line)]] | alt | 6.44 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.98× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0764× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 5.27 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0602× (z -11.4) |
| [[Hs 766T (line)]] | wt | 4.28 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0852× (z -9.1) |
| [[HT-29 (line)]] | alt | 3.66 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0526× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 8.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.57× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 5.33 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.107× (z -9.3) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 5.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 5.81 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +8.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 7.73 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.17× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 7.15 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0994× (z -8.9) |
| [[A-172 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | +0.73 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[GBA1]] | +0.73 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[PDIA3P1]] | +0.71 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.69 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[TUG1]] | +0.69 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[MKLN1-AS]] | +0.67 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ZNF300]] | +0.64 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HFE]] | +0.64 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[SUMO3]] | +0.63 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[PAPOLA]] | +0.63 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[DDX3X]] | +0.63 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 11 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL36]] | -0.66 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[RPS26]] | -0.65 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[E4F1]] | -0.65 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ANKS3]] | -0.64 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[SNU13]] | -0.63 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[GTF2H2]] | -0.63 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[VPS37C]] | -0.62 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.61 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[ZXDC]] | -0.61 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SNHG6]] | -0.61 | -0.40 / -0.61 | both halves | 4e-05 |  |
| [[RPS10]] | -0.61 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[RPL18]] ⚠ | -0.60 | -0.46 / -0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIGA2]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NXT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.1, -22.7); signed map (18.3, -34.9). **Vector** length 70.9, 11.6% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.5 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +15.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +8.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear transport factor 2 like export factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:109,535,781-109,544,698 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P15-2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPJ8](https://www.uniprot.org/uniprotkb/Q9NPJ8) (NTF2-related export protein 2):

> Regulator of protein export for NES-containing proteins. Also plays a role in mRNA nuclear export.

**Summary**, from NCBI Gene [55916](https://www.ncbi.nlm.nih.gov/gene/55916):

> The protein encoded by this gene contains a nuclear transport factor 2 (NTF2) domain, which plays an important role in the trafficking of macromolecules, ions, and small molecules between the cytoplasm and nucleus. This protein may also have a role in mRNA nuclear export. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:18151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18151) · Entrez [55916](https://www.ncbi.nlm.nih.gov/gene/55916) · UniProt [Q9NPJ8](https://www.uniprot.org/uniprotkb/Q9NPJ8) · Ensembl [ENSG00000101888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101888)

## Data

Gene col 2186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2186); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2186]; `tensor/DDL_lfc|DDL_z.npy` [2186]; `embed/gene_vectors.npy` [2186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2186 or target_col == 2186). Every well: [[NXT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NXT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
