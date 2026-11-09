---
symbol: "UPK2"
type: "gene"
col: 3133
ensembl_id: "ENSG00000110375"
name: "uroplakin 2"
location: "11q23.3"
module: 35
arm: "+"
pooled_cpm: 2.63
n_lines_expressing: 48
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# UPK2

*uroplakin 2* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.17× (z +25.8, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.572× (z -5.2, q 1e-04, down in 16 of 41 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.635× (z -4.2, q 0.006, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAXBP1-AS1]] (+0.78, fdr 7e-06), [[NDUFV2-AS1]] (+0.76, fdr 7e-06), [[CHODL]] (+0.74, fdr 7e-06); moves opposite to [[HERC2]] (-0.68, fdr 1e-05), [[RRP1B]] (-0.68, fdr 3e-05), [[HERC2P9]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.17×** | +25.8 | 0e+00 | 26/26 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.09×** | +12.6 | 9e-34 | 16/21 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +10.7 | 2e-24 | 1/3 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +10.5 | 1e-23 | 23/27 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +9.5 | 3e-19 | 7/13 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +7.9 | 4e-13 | 11/27 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +6.3 | 2e-08 | 1/6 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.3 | 2e-08 | 11/40 (SNU-423, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +6.0 | 2e-07 | 9/33 (KATO III, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +5.6 | 1e-06 | 9/40 (Panc 03.27, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +5.1 | 2e-05 | 8/42 (KATO III, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.4 | 4e-04 | 9/39 (KATO III, Panc 03.27, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +4.3 | 7e-04 | 7/32 (SW48, HT-29, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.001 | 5/31 (A-427, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.002 | 6/37 (A-427, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.003 | 9/41 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.008 | 8/25 (A-427, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.009 | 7/43 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.572×** | -5.2 | 1e-04 | 16/41 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.635×** | -4.2 | 0.006 | 15/44 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -4.1 | 0.008 | 11/32 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -3.9 | 0.012 | 13/35 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.698× | -3.2 | 0.13 | 5/31 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.527× | -3.1 | 0.17 | 6/23 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 7.14 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +8.6) | [[Docetaxel (drug)]] 0.05 µM 0.0912× (z -10.8) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 1.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +9.6) | — |
| [[A498 (line)]] | wt | 1.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.3) | — |
| [[C32 (line)]] | wt | 2.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.5× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.16× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 2.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.96× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 3.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.6) | — |
| [[LoVo (line)]] | wt | 0.995 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 1.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +12.5) | — |
| [[PANC-1 (line)]] | alt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +11.3) | — |
| [[SW 1088 (line)]] | alt | 1.70 | 0 | 1 | — | [[c-Kit-IN-1 (drug)]] 0.5 µM 0.454× (z -19.5) |
| [[A-427 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.817 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.827 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.908 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAXBP1-AS1]] | +0.78 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[NDUFV2-AS1]] | +0.76 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[CHODL]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[LRRC8C-DT]] | +0.73 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MALINC1]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[KLRK1-AS1]] | +0.72 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RBMS3-AS3]] | +0.71 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[C11orf71]] | +0.71 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SPEN-AS1]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[UNC79]] | +0.71 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.71 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ZC2HC1C]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2]] | -0.68 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[RRP1B]] | -0.68 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[HERC2P9]] | -0.65 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.64 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[EIF2B3]] | -0.64 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[POLR3B]] | -0.62 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UPK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.5, 23.8); signed map (32.3, -1.9). **Vector** length 45.8, 6.24% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +25.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +4.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -2.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -0.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | uroplakin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,925,164-118,958,559 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UP2, UPII, MGC138598 |
| Matched by | ensembl_id |

**Function**, from UniProt [O00526](https://www.uniprot.org/uniprotkb/O00526) (Uroplakin-2):

> Component of the asymmetric unit membrane (AUM); a highly specialized biomembrane elaborated by terminally differentiated urothelial cells. May play an important role in regulating the assembly of the AUM (By similarity).

**Summary**, from NCBI Gene [7379](https://www.ncbi.nlm.nih.gov/gene/7379):

> This gene encodes one of the proteins of the highly conserved urothelium-specific integral membrane proteins of the asymmetric unit membrane which forms urothelium apical plaques in mammals. The asymmetric unit membrane is believed to strengthen the urothelium by preventing cell rupture during bladder distention. The encoded protein is expressed in the peripheral blood of bladder cancer patients with transitional cell carcinomas.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:12579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12579) · Entrez [7379](https://www.ncbi.nlm.nih.gov/gene/7379) · UniProt [O00526](https://www.uniprot.org/uniprotkb/O00526) · Ensembl [ENSG00000110375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110375)

## Data

Gene col 3133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3133); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3133]; `tensor/DDL_lfc|DDL_z.npy` [3133]; `embed/gene_vectors.npy` [3133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3133 or target_col == 3133). Every well: [[UPK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
