---
symbol: "FAM86HP"
type: "gene"
col: 14812
ensembl_id: "ENSG00000253540"
name: "family with sequence similarity 86 member H, pseudogene"
location: "3q22.1"
module: 124
arm: "+"
pooled_cpm: 2.24
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# FAM86HP

*family with sequence similarity 86 member H, pseudogene* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.34× (z +14.0, q 6e-42, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM: 0.613× (z -4.0, q 0.031, down in 10 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.0556×); [[Verteporfin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0573×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0831×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITPA]] (+0.65, fdr 2e-05), [[TMEM147-AS1]] (+0.65, fdr 1e-05), [[LTO1]] (+0.64, fdr 3e-05); moves opposite to [[ALAD]] (-0.61, fdr 9e-05), [[PAPSS1]] (-0.58, fdr 1e-04), [[MAPRE2]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +14.0 | 6e-42 | 26/29 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +8.7 | 1e-15 | 15/22 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.94×** | +8.5 | 3e-15 | 6/10 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +7.3 | 6e-11 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +6.5 | 9e-09 | 21/41 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +6.1 | 8e-08 | 22/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +5.8 | 4e-07 | 12/32 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +5.5 | 3e-06 | 12/30 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.3 | 7e-06 | 14/42 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +5.1 | 2e-05 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +4.7 | 1e-04 | 13/29 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.77×** | +4.7 | 1e-04 | 13/40 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +4.4 | 5e-04 | 10/35 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +4.3 | 8e-04 | 13/41 (A-172, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.61×** | +3.9 | 0.003 | 8/44 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.003 | 3/22 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.004 | 6/25 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **2.26×** | +3.5 | 0.013 | 3/14 (SK-MEL-2, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +3.4 | 0.020 | 9/42 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.038 | 5/42 (A-172, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14812.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.0556×); [[Verteporfin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0573×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0831×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.613×** | -4.0 | 0.031 | 10/39 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.729×** | -3.7 | 0.065 | 8/42 (SHP-77, A-172, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.666× | -3.3 | 0.16 | 7/42 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.688× | -3.1 | 0.29 | 8/45 (CHP-212, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.95 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0556× (z -10.8) |
| [[A-172 (line)]] | wt | 2.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 3.75 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0831× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 5.45 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0573× (z -9.1) |
| [[SW480 (line)]] | alt | 3.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +8.6) | — |
| [[A498 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.775 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.849 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.772 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.883 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPA]] | +0.65 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[TMEM147-AS1]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[LTO1]] | +0.64 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[STARD7-AS1]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MRM1]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.59 | +0.68 / +0.32 | both halves | 2e-04 |  |
| [[GABPB1-AS1]] | +0.59 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[SCO1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GABPB1]] | +0.58 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[GTF3C2-AS2]] | +0.58 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[ADCK1]] | +0.57 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[PIGW]] | +0.57 | +0.56 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.61 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[PAPSS1]] | -0.58 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[MAPRE2]] | -0.56 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[RAB3A]] | -0.55 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[SEPTIN6]] | -0.55 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[HLTF]] | -0.55 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[WDR47]] | -0.54 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[ACACB]] | -0.53 | -0.34 / -0.29 | both halves | 3e-04 |  |
| [[FBXO33]] | -0.52 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[SUFU]] | -0.52 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[ARL6]] | -0.51 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[GNAI2]] | -0.51 | -0.54 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM86HP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC-PINT]] | C | LINC-PINT's natural level weakens FAM86HP's drug response | LINC-PINT's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.03; direction not clear | 0.087 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.2, 9.7); signed map (25.4, -29.3). **Vector** length 46.4, 5.57% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.4 | +3.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 86 member H, pseudogene |
| Locus type | pseudogene |
| Location | 3q22.1 — chr3:130,099,258-130,111,472 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42359) · Entrez [729375](https://www.ncbi.nlm.nih.gov/gene/729375) · Ensembl [ENSG00000253540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253540)

## Data

Gene col 14812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14812); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14812]; `tensor/DDL_lfc|DDL_z.npy` [14812]; `embed/gene_vectors.npy` [14812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14812 or target_col == 14812). Every well: [[FAM86HP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM86HP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
