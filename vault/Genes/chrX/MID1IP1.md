---
symbol: "MID1IP1"
type: "gene"
col: 9080
ensembl_id: "ENSG00000165175"
name: "MID1 interacting protein 1"
location: "Xp11.4"
module: 133
arm: "+"
pooled_cpm: 17.92
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# MID1IP1

*MID1 interacting protein 1* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.48× (z +4.9, q 4e-04, up in 23 of 44 measured lines) ⚠ transcription drop. The strongest without an alert is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.45× (z +4.7, q 5e-04, up in 21 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.572× (z -7.0, q 1e-09, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF768]] (+0.60, fdr 2e-05), [[SLC3A2]] (+0.56, fdr 1e-05), [[SEPHS2]] (+0.53, fdr 5e-05); moves opposite to [[MRE11]] (-0.47, fdr 1e-04), [[TMCO1]] (-0.44, fdr 1e-04), [[RAD18]] (-0.43, fdr 9e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PGAP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.9 | 4e-04 | 23/44 (KATO III, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 5e-04 | 21/45 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.7 | 5e-04 | 19/41 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.2 | 0.004 | 19/39 (SW1417, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.004 | 19/47 (SW1417, KATO III, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.83×** | +3.7 | 0.015 | 14/42 (Panc 03.27, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.015 | 16/45 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.029 | 12/47 (NCI-H460, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.029 | 16/46 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.030 | 14/46 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.056 | 14/47 (NCI-H460, Hs 766T, …) | two highest doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.061 | 8/47 (J82, SNU-423, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.093 | 11/45 (HOP62, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.099 | 12/42 (NCI-H1792, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9080.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.572×** | -7.0 | 1e-09 | 34/47 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -5.6 | 8e-06 | 23/47 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.672×** | -5.0 | 1e-04 | 24/46 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.011 | 22/46 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -3.8 | 0.017 | 20/43 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | **0.749×** | -3.5 | 0.046 | 16/45 (A498, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.587×** | -3.3 | 0.081 | 18/46 (hTERT-HPNE, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 20.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.5) |
| [[PANC-1 (line)]] | alt | 9.82 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0941× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.1) |
| [[SW48 (line)]] | wt | 25.9 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0738× (z -11.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[HS-578T (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[LOX-IMVI (line)]] | wt | 5.90 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0856× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 7.64 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.120× (z -8.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H460 (line)]] | wt | 35.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF768]] | +0.60 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[SLC3A2]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SEPHS2]] | +0.53 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[BRD2]] | +0.51 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[LMO4]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[CEBPG]] | +0.49 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[ZBED3]] | +0.49 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[HOXD3]] | +0.47 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[RPP25]] | +0.47 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[PCK2]] | +0.47 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[PPP1R3D]] | +0.46 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[ADM2]] | +0.46 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRE11]] | -0.47 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[TMCO1]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[RAD18]] | -0.43 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[SCN5A]] | -0.40 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[PARK7]] ⚠ | -0.40 | -0.23 / -0.33 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LSM3]] ⚠ | -0.40 | -0.51 / -0.24 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ERGIC2]] | -0.39 | -0.19 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[KHDRBS1]] | -0.39 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP4]] | B | PGAP4 activity raises MID1IP1's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.43× lower at baseline in the lines without PGAP4 | 0.037 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[HEIH]] | B | HEIH activity raises MID1IP1's level | lines that do not express HEIH (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without HEIH | 0.064 | ⚠ within organs, on part of the lines; also absent: HYI, LINC00847; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MID1IP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.3, 46.8); signed map (-11.9, 21.4). **Vector** length 80.9, 16.1% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +4.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +3.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.8 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.6 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.3 | -0.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Rifaximin (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.3 | +0.1 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | MID1 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:38,801,440-38,806,537 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STRAIT11499, FLJ10386, MIG12, THRSPL, G12-like |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 3 pathways, smallest: Carnitine shuttle; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPA3](https://www.uniprot.org/uniprotkb/Q9NPA3) (Mid1-interacting protein 1):

> Plays a role in the regulation of lipogenesis in liver. Up-regulates ACACA enzyme activity. Required for efficient lipid biosynthesis, including triacylglycerol, diacylglycerol and phospholipid. Involved in stabilization of microtubules (By similarity).

**Summary**, from NCBI Gene [58526](https://www.ncbi.nlm.nih.gov/gene/58526):

> Predicted to enable enzyme activator activity. Predicted to be involved in several processes, including negative regulation of microtubule depolymerization; positive regulation of fatty acid biosynthetic process; and positive regulation of ligase activity. Predicted to be located in microtubule cytoskeleton. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20715) · Entrez [58526](https://www.ncbi.nlm.nih.gov/gene/58526) · UniProt [Q9NPA3](https://www.uniprot.org/uniprotkb/Q9NPA3) · Ensembl [ENSG00000165175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165175)

## Data

Gene col 9080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9080); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9080]; `tensor/DDL_lfc|DDL_z.npy` [9080]; `embed/gene_vectors.npy` [9080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9080 or target_col == 9080). Every well: [[MID1IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MID1IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
