---
symbol: "C2CD2L"
type: "gene"
col: 10248
ensembl_id: "ENSG00000172375"
name: "C2CD2 like"
location: "11q23.3"
module: 40
arm: "+"
pooled_cpm: 5.22
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# C2CD2L

*C2CD2 like* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.84× (z +15.8, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.532× (z -7.4, q 7e-11, down in 23 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.578× (z -6.2, q 2e-07, down in 19 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT5C]] (+0.69, fdr 7e-06), [[SPSB3]] (+0.69, fdr 7e-06), [[SYVN1]] (+0.69, fdr 7e-06); moves opposite to [[SLC9A8]] (-0.62, fdr 3e-05), [[MAPK1IP1L]] (-0.61, fdr 3e-05), [[ZC3HC1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.84×** | +15.8 | 0e+00 | 46/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +15.7 | 0e+00 | 37/39 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.73×** | +15.5 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.58×** | +15.0 | 0e+00 | 45/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.60×** | +11.2 | 5e-27 | 35/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.32×** | +9.9 | 6e-21 | 38/47 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +6.8 | 9e-10 | 6/15 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.7 | 1e-09 | 15/26 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.3 | 1e-08 | 13/30 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.6 | 1e-06 | 5/11 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.5 | 2e-06 | 13/35 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.4 | 4e-06 | 15/47 (PANC-1, J82, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +5.3 | 6e-06 | 11/29 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.35×** | +5.2 | 6e-06 | 12/44 (PANC-1, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.001 | 7/42 (Panc 03.27, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.008 | 8/38 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.014 | 5/46 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.053 | 9/36 (NCI-H1573, SNU-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.532×** | -7.4 | 7e-11 | 23/47 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.578×** | -6.2 | 2e-07 | 19/44 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -5.0 | 1e-04 | 19/46 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.539×** | -3.8 | 0.021 | 9/42 (SW 900, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | 0.763× | -3.2 | 0.17 | 11/43 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.603× | -3.1 | 0.18 | 7/36 (PANC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.771× | -3.1 | 0.18 | 13/45 (NCI-H1573, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.55 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0929× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 7.10 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.130× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 4.09 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0623× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.3) | — |
| [[RKO (line)]] | wt | 8.06 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 7.49 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0943× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT5C]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.69 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SYVN1]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[GLRX5]] | +0.66 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TM9SF2]] | +0.65 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[VPS26B]] | +0.65 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[ORMDL3]] | +0.65 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ALKBH5]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ANO8]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[RAB40B]] | +0.64 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[PHF12]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | -0.62 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[MAPK1IP1L]] | -0.61 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ZC3HC1]] | -0.60 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[RPL7L1]] | -0.59 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TAF2]] | -0.59 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.58 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[AFG1L]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF518A]] | -0.57 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[TANK]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[LYRM2]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CHM]] | -0.56 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[THG1L]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C2CD2L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (9.7, -30.9); signed map (-42.6, 5.4). **Vector** length 66.7, 10.3% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | C2CD2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,102,198-119,118,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0285; previously TMEM24 |
| Matched by | ensembl_id |

**Function**, from UniProt [O14523](https://www.uniprot.org/uniprotkb/O14523) (Phospholipid transfer protein C2CD2L):

> Lipid-binding protein that transports phosphatidylinositol, the precursor of phosphatidylinositol 4,5-bisphosphate (PI(4,5)P2), from its site of synthesis in the endoplasmic reticulum to the cell membrane. It thereby maintains the pool of cell membrane phosphoinositides, which are degraded during phospholipase C (PLC) signaling. Plays a key role in the coordination of Ca(2+) and phosphoinositide signaling: localizes to sites of contact between the endoplasmic reticulum and the cell membrane, …

**Summary**, from NCBI Gene [9854](https://www.ncbi.nlm.nih.gov/gene/9854):

> Enables phosphatidylinositol binding activity and phosphatidylinositol transfer activity. Involved in positive regulation of insulin secretion involved in cellular response to glucose stimulus. Located in cortical endoplasmic reticulum; cytoplasmic side of apical plasma membrane; and endoplasmic reticulum-plasma membrane contact site. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29000) · Entrez [9854](https://www.ncbi.nlm.nih.gov/gene/9854) · UniProt [O14523](https://www.uniprot.org/uniprotkb/O14523) · Ensembl [ENSG00000172375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172375)

## Data

Gene col 10248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10248); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10248]; `tensor/DDL_lfc|DDL_z.npy` [10248]; `embed/gene_vectors.npy` [10248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10248 or target_col == 10248). Every well: [[C2CD2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2CD2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
