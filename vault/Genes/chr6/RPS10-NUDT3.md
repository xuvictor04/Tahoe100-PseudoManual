---
symbol: "RPS10-NUDT3"
type: "gene"
col: 15670
ensembl_id: "ENSG00000270800"
name: "RPS10-NUDT3 readthrough"
location: "6p21.31"
module: 15
arm: "+"
pooled_cpm: 5.46
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 1
n_dd_up_clean: 37
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# RPS10-NUDT3

*RPS10-NUDT3 readthrough* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.52× (z +14.5, q 1e-44, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Filgotinib (drug)]] 0.05 µM: 0.618× (z -4.0, q 0.039, down in 8 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0434×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (C-33 A 0.0594×); [[Saquinavir (drug)]] 0.05 µM in 1 line (KATO III 0.0578×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (BT-474 0.0963×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTTN-DT]] (+0.63, fdr 1e-05), [[SMG1P1]] (+0.61, fdr 1e-05), [[RENO1]] (+0.61, fdr 2e-05); moves opposite to [[MIS12]] (-0.52, fdr 4e-05), [[THAP5]] (-0.51, fdr 1e-04), [[ASF1A]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.52×** | +14.5 | 1e-44 | 33/41 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.00×** | +13.2 | 2e-37 | 40/42 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.06×** | +11.5 | 2e-28 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **4.12×** | +11.2 | 6e-27 | 32/34 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.53×** | +10.4 | 4e-23 | 44/47 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +9.8 | 1e-20 | 30/38 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **3.42×** | +9.5 | 1e-19 | 37/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **3.21×** | +9.0 | 1e-17 | 31/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.97×** | +9.0 | 2e-17 | 42/47 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.09×** | +8.9 | 3e-17 | 24/31 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.94×** | +8.3 | 4e-15 | 39/46 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.51×** | +7.5 | 2e-12 | 36/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.92×** | +7.5 | 3e-12 | 28/47 (CFPAC-1, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.66×** | +7.4 | 4e-12 | 9/15 (SW480, PANC-1, …) | inconsistent across doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +7.3 | 1e-11 | 19/39 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.03×** | +6.9 | 1e-10 | 37/45 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +6.2 | 1e-08 | 21/39 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.08×** | +6.0 | 5e-08 | 25/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.81×** | +5.7 | 2e-07 | 23/37 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15670.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0434×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (C-33 A 0.0594×); [[Saquinavir (drug)]] 0.05 µM in 1 line (KATO III 0.0578×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (BT-474 0.0963×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 0.05 µM |  | **0.618×** | -4.0 | 0.039 | 8/46 (HEC-1-A, CHP-212, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.661× | -3.4 | 0.11 | 14/46 (NCI-H2347, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.748× | -3.4 | 0.11 | 16/46 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.667× | -3.4 | 0.11 | 6/47 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.668× | -3.2 | 0.15 | 11/44 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.696× | -3.0 | 0.24 | 2/47 (HEC-1-A, C-33 A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.94 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 3.38 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 4.16 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 8.67× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 8.04× (z +8.9) | — |
| [[A498 (line)]] | wt | 3.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0963× (z -8.8) |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0594× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 5.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +8.9) | — |
| [[KATO III (line)]] | alt | 3.68 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0578× (z -9.0) |
| [[LoVo (line)]] | wt | 3.77 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 11.2× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 5.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 4.64 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.6× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0434× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 7.54 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 14.4× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 5.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +11.3) | — |
| [[A-172 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTTN-DT]] | +0.63 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[SMG1P1]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RENO1]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SMG1P5]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SNHG10]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[DANCR]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[HSPE1-MOB4]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SNRPA1]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PXN-AS1]] | +0.57 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[LINC00115]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[CTC-338M12.4]] | +0.56 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[MED17]] | +0.56 | +0.38 / +0.63 | both halves | 6e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[THAP5]] | -0.51 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[ASF1A]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[RAB8A]] | -0.50 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[CSTF2T]] | -0.50 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[CEP350]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SETX]] | -0.49 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[MRFAP1]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[EEA1]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[CDKN2AIP]] | -0.47 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MED1]] | -0.47 | -0.34 / -0.60 | both halves | 1e-04 | STRING 904 |
| [[GOLGB1]] | -0.47 | -0.34 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP3]] | B | LRP3 activity raises RPS10-NUDT3's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without LRP3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.417). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.0, 25.7); signed map (-36.0, -10.0). **Vector** length 59.2, 9.96% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.5 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.6 | +6.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | +6.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | +1.5 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | RPS10-NUDT3 readthrough |
| Locus type | readthrough (other) |
| Location | 6p21.31 — chr6:34,284,887-34,426,071 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100529239](https://www.ncbi.nlm.nih.gov/gene/100529239):

> This locus represents naturally occurring read-through transcription between the neighboring RPS10 (ribosomal protein S10) and NUDT3 (nudix (nucleoside diphosphate linked moiety X)-type motif 3) genes on chromosome 6. The read-through transcript produces a fusion protein that shares sequence identity with each individual gene product. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:49181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49181) · Entrez [100529239](https://www.ncbi.nlm.nih.gov/gene/100529239) · Ensembl [ENSG00000270800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270800)

## Data

Gene col 15670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15670); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15670]; `tensor/DDL_lfc|DDL_z.npy` [15670]; `embed/gene_vectors.npy` [15670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15670 or target_col == 15670). Every well: [[RPS10-NUDT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS10-NUDT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
