---
symbol: "ZC2HC1C"
type: "gene"
col: 4104
ensembl_id: "ENSG00000119703"
name: "zinc finger C2HC-type containing 1C"
location: "14q24.3"
module: 35
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ZC2HC1C

*zinc finger C2HC-type containing 1C* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +16.6, q 0e+00, up in 34 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Roxadustat (drug)]] 5 µM in 1 line (HT-29 0.0612×); [[Simotinib (drug)]] 5 µM in 1 line (SW1417 0.105×; ⚠ toxic); [[Canagliflozin (drug)]] 0.05 µM in 1 line (NCI-H460 0.101×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.78, fdr 7e-06), [[C11orf71]] (+0.78, fdr 7e-06), [[NUTM2E]] (+0.78, fdr 7e-06); moves opposite to [[FBXW2]] (-0.65, fdr 4e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF563]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +16.6 | 0e+00 | 34/39 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.40×** | +15.4 | 0e+00 | 28/37 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +11.2 | 1e-26 | 5/7 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +10.8 | 3e-25 | 18/22 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +8.8 | 2e-16 | 8/10 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +8.2 | 3e-14 | 25/44 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +7.2 | 4e-11 | 16/46 (SW480, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.8 | 6e-07 | 16/36 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.7 | 7e-07 | 12/32 (NCI-H2030, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.0 | 4e-05 | 9/35 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.9 | 5e-05 | 11/47 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.4 | 5e-04 | 12/26 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 1e-03 | 9/44 (NCI-H23, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.2 | 1e-03 | 6/43 (SW48, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.003 | 12/44 (SW48, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.006 | 9/46 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.008 | 6/42 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.014 | 8/44 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.027 | 3/42 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4104.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Roxadustat (drug)]] 5 µM in 1 line (HT-29 0.0612×); [[Simotinib (drug)]] 5 µM in 1 line (SW1417 0.105×; ⚠ toxic); [[Canagliflozin (drug)]] 0.05 µM in 1 line (NCI-H460 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -3.8 | 0.083 | 13/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.776× | -3.2 | 0.35 | 13/45 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | 0.779× | -3.1 | 0.35 | 8/43 (HOP62, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 3.71 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0612× (z -9.1) |
| [[KATO III (line)]] | alt | 6.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 2.86 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.101× (z -8.6) |
| [[PANC-1 (line)]] | alt | 4.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 4.76 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.105× (z -8.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.78 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[C11orf71]] | +0.78 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[NUTM2E]] | +0.78 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[GUCY2C-AS1]] | +0.75 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[PAXBP1-AS1]] | +0.75 | +0.79 / +0.58 | both halves | 8e-06 |  |
| [[DNAH12]] | +0.74 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[PIGP]] | +0.74 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.74 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[MALINC1]] | +0.73 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[CREB3L4]] | +0.73 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[UNC79]] | +0.73 | +0.77 / +0.49 | both halves | 1e-05 |  |
| [[LRIG2-DT]] | +0.72 | +0.73 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.65 | -0.71 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF563]] | B | ZNF563 activity raises ZC2HC1C's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 1.34× lower at baseline in the lines without ZNF563 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[TOP2A]] | B | TOP2A activity lowers ZC2HC1C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02175]] | B | LINC02175 activity raises ZC2HC1C's level | lines that do not express LINC02175 (7) vs lines expressing it (43) | 1.13× lower at baseline in the lines without LINC02175 | 0.048 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3, FAM182B; maybe low, not absent |
| [[MAPK8IP2]] | B | MAPK8IP2 activity raises ZC2HC1C's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.21× lower at baseline in the lines without MAPK8IP2 | 0.082 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[C7orf31]] | B | C7orf31 activity raises ZC2HC1C's level | lines that do not express C7orf31 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without C7orf31 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC00888, TMEM145, TBKBP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.813). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.8, 21.2); signed map (30.9, -3.7). **Vector** length 48.9, 5.70% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +15.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +16.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger C2HC-type containing 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,064,109-75,119,502 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf140, FAM164C |
| Gene groups (HGNC) | Zinc fingers ZC2HC1-type |
| Hallmark sets | SPERMATOGENESIS, KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

UniProt [Q53FD0](https://www.uniprot.org/uniprotkb/Q53FD0) carries no function annotation.

**Summary**, from NCBI Gene [79696](https://www.ncbi.nlm.nih.gov/gene/79696):

> Predicted to enable zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20354) · Entrez [79696](https://www.ncbi.nlm.nih.gov/gene/79696) · UniProt [Q53FD0](https://www.uniprot.org/uniprotkb/Q53FD0) · Ensembl [ENSG00000119703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119703)

## Data

Gene col 4104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4104); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4104]; `tensor/DDL_lfc|DDL_z.npy` [4104]; `embed/gene_vectors.npy` [4104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4104 or target_col == 4104). Every well: [[ZC2HC1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC2HC1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
