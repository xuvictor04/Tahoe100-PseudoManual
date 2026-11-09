---
symbol: "CPEB2-DT"
type: "gene"
col: 14501
ensembl_id: "ENSG00000247624"
name: "CPEB2 divergent transcript"
location: "4p15.33-p15.32"
module: 26
arm: "+"
pooled_cpm: 2.45
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CPEB2-DT

*CPEB2 divergent transcript* — 4p15.33-p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 12.1× (z +32.3, q 0e+00, up in 28 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.553× (z -5.4, q 4e-05, down in 17 of 41 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.622× (z -4.3, q 0.003, down in 10 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00393]] (+0.84, fdr 7e-06), [[LINC02955]] (+0.84, fdr 7e-06), [[PSMD7-DT]] (+0.84, fdr 7e-06); moves opposite to [[NAA40]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC01917]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.1×** | +32.3 | 0e+00 | 28/29 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.90×** | +14.0 | 4e-42 | 19/28 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +11.4 | 5e-28 | 23/32 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +10.8 | 7e-25 | 22/30 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.25×** | +10.5 | 6e-24 | 20/42 (HOP62, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.04×** | +10.2 | 2e-22 | 26/39 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +9.0 | 1e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +8.1 | 4e-14 | 19/31 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +7.6 | 2e-12 | 3/3 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +7.2 | 5e-11 | 1/10 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.81×** | +5.4 | 3e-06 | 5/21 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +5.2 | 1e-05 | 11/41 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.58×** | +4.2 | 0.001 | 5/38 (SK-MEL-2, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.35×** | +3.9 | 0.004 | 7/45 (A498, C32, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.008 | 6/39 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.553×** | -5.4 | 4e-05 | 17/41 (SW 900, SK-MEL-2, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.609×** | -4.5 | 0.002 | 17/43 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.622×** | -4.3 | 0.003 | 10/44 (SW48, SW 900, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.641×** | -4.1 | 0.007 | 15/41 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.674×** | -3.6 | 0.032 | 8/41 (A-427, SW 900, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.757×** | -3.6 | 0.032 | 10/41 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.712× | -3.1 | 0.16 | 5/42 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.24 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +14.9) | — |
| [[NCI-H1573 (line)]] | alt | 7.82 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.76× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 6.46 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.02× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.0468× (z -10.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.5× (z +11.2) | — |
| [[A498 (line)]] | wt | 2.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.3× (z +13.7) | — |
| [[A549 (line)]] | wt | 1.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 2.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +10.0) | — |
| [[C32 (line)]] | wt | 4.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.4× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 2.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 2.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 1.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.7× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 4.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 1.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.2× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 1.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 4.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 1.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.3× (z +9.7) | — |
| [[A-427 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.701 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.820 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.689 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.777 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00393]] | +0.84 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.84 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.84 | +0.82 / +0.61 | both halves | 7e-06 | same gene group |
| [[INTS6-AS1]] | +0.83 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[SIAH2-AS1]] | +0.83 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.83 | +0.83 / +0.52 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.82 | +0.81 / +0.53 | both halves | 1e-05 |  |
| [[CIBAR1-DT]] | +0.82 | +0.68 / +0.64 | both halves | 7e-06 | same gene group |
| [[LRP2BP]] | +0.81 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.81 | +0.78 / +0.60 | both halves | 7e-06 | same gene group |
| [[NEB]] | +0.81 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.81 | +0.80 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.71 | -0.52 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01917]] | B | LINC01917 activity raises CPEB2-DT's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without LINC01917 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[CASC20]] | B | CASC20 activity raises CPEB2-DT's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without CASC20 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[IGSF11]] | B | IGSF11 activity raises CPEB2-DT's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without IGSF11 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CPEB2-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02398]] | B | LINC02398 activity raises CPEB2-DT's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without LINC02398 | 0.042 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CPEB2-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FER1L6]] | B | FER1L6 activity raises CPEB2-DT's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without FER1L6 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.868). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.2, 18.6); signed map (24.9, -1.9). **Vector** length 66.6, 9.86% of its response variance represented; |z| ≥ 3 in 1,323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +32.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +10.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.8 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.3 | -5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -4.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CPEB2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p15.33-p15.32 — chr4:14,909,961-15,002,045 (-) |
| Ensembl biotype | lncRNA |
| Also known as | DRAIR; previously CPEB2-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49082) · Entrez [441009](https://www.ncbi.nlm.nih.gov/gene/441009) · Ensembl [ENSG00000247624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247624)

## Data

Gene col 14501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14501); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14501]; `tensor/DDL_lfc|DDL_z.npy` [14501]; `embed/gene_vectors.npy` [14501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14501 or target_col == 14501). Every well: [[CPEB2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPEB2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
