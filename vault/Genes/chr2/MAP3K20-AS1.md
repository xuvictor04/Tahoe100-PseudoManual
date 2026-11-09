---
symbol: "MAP3K20-AS1"
type: "gene"
col: 14171
ensembl_id: "ENSG00000238133"
name: "MAP3K20 antisense RNA 1"
location: "2q31.1"
module: 75
arm: "+"
pooled_cpm: 10.02
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# MAP3K20-AS1

*MAP3K20 antisense RNA 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.32× (z +22.1, q 0e+00, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.896× (z -4.8, q 8e-04, down in 11 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.732× (z -4.0, q 0.017, down in 16 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0906×); [[Neratinib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0832×); [[Pimozide (drug)]] 0.5 µM in 1 line (C32 0.109×; ⚠ transcription drop); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.0841×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNAB1]] (+0.80, fdr 7e-06), [[SYNM-AS1]] (+0.78, fdr 7e-06), [[DNAH12]] (+0.74, fdr 7e-06); moves opposite to [[FBXW2]] (-0.62, fdr 1e-05), [[ACTR5]] (-0.62, fdr 1e-05), [[NUDT21]] (-0.60, fdr 1e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.32×** | +22.1 | 0e+00 | 36/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +19.2 | 0e+00 | 40/44 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.88×** | +13.2 | 2e-37 | 35/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +12.6 | 5e-34 | 30/32 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.51×** | +12.0 | 7e-31 | 30/46 (C32, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.7 | 1e-24 | 17/18 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +9.3 | 9e-19 | 30/42 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +7.6 | 3e-12 | 23/41 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +6.9 | 2e-10 | 20/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 1e-05 | 18/46 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.0 | 3e-05 | 15/41 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 14/42 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.011 | 12/48 (HOP62, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.31×** | +3.4 | 0.028 | 10/38 (SHP-77, SW48, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.039 | 10/47 (SW48, BT-474, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.042 | 4/44 (CHP-212, A498, …) | rises with dose | position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.069 | 7/44 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.088 | 3/44 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.088 | 5/45 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14171.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0906×); [[Neratinib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0832×); [[Pimozide (drug)]] 0.5 µM in 1 line (C32 0.109×; ⚠ transcription drop); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.0841×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -4.8 | 8e-04 | 11/48 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.732×** | -4.0 | 0.017 | 16/43 (HepG2/C3A, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 0.841× | -3.1 | 0.33 | 13/48 (RPMI-7951, SW 1271, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 16.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +19.2) | — |
| [[C32 (line)]] | wt | 8.96 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +13.0) | [[Pimozide (drug)]] 0.5 µM 0.109× (z -9.4) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 8.35 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +17.0) | — |
| [[KATO III (line)]] | alt | 55.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 25.1× (z +18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 8.85 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +19.6) | — |
| [[HOP62 (line)]] | alt | 8.41 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +16.5) | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +8.8) | [[Neratinib (drug)]] 0.05 µM 0.0832× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 10.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +11.3) | — |
| [[SW480 (line)]] | alt | 7.75 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +14.3) | — |
| [[A498 (line)]] | wt | 8.87 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 8.65 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +13.6) | — |
| [[A549 (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 9.32 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0906× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 7.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 6.60 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0647× (z -8.5) |
| [[Hs 766T (line)]] | wt | 6.44 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0841× (z -9.4) |
| [[HS-578T (line)]] | alt | 7.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +9.2) | — |
| [[LoVo (line)]] | wt | 7.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 8.21 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.56× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +18.4) | — |
| [[NCI-H2347 (line)]] | alt | 5.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +16.7) | — |
| [[Panc 03.27 (line)]] | alt | 6.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +11.4) | — |
| [[A-172 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNAB1]] | +0.80 | +0.85 / +0.65 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.78 | +0.79 / +0.72 | both halves | 7e-06 | same gene group |
| [[DNAH12]] | +0.74 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[SAMD4A-AS1]] | +0.74 | +0.73 / +0.62 | both halves | 7e-06 | same gene group |
| [[HULC]] | +0.74 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.73 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[DPP6]] | +0.73 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[DNAH3]] | +0.73 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ASB14]] | +0.71 | +0.77 / +0.57 | both halves | 9e-06 |  |
| [[BOLA1]] | +0.70 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[LINC01033]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TTN]] | +0.70 | +0.69 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.60 | -0.63 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAP3K20-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01252]] | B | LINC01252 activity raises MAP3K20-AS1's level | lines that do not express LINC01252 (17) vs lines expressing it (33) | 1.35× lower at baseline in the lines without LINC01252 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000275119, EPHB6, ABCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.1, 25.5); signed map (30.6, 9.3). **Vector** length 70.9, 11.8% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +22.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +19.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +3.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | MAP3K20 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q31.1 — chr2:173,166,446-173,282,036 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously MLK7-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27935) · Entrez [339751](https://www.ncbi.nlm.nih.gov/gene/339751) · Ensembl [ENSG00000238133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238133)

## Data

Gene col 14171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14171); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14171]; `tensor/DDL_lfc|DDL_z.npy` [14171]; `embed/gene_vectors.npy` [14171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14171 or target_col == 14171). Every well: [[MAP3K20-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K20-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
