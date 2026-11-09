---
symbol: "INTS6-AS1"
type: "gene"
col: 14099
ensembl_id: "ENSG00000236778"
name: "INTS6 antisense RNA 1"
location: "13q14.3"
module: 26
arm: "+"
pooled_cpm: 2.43
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# INTS6-AS1

*INTS6 antisense RNA 1* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 11.0× (z +30.8, q 0e+00, up in 33 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 0.5 µM in 1 line (LoVo 0.0906×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.90, fdr 7e-06), [[PSMD7-DT]] (+0.89, fdr 7e-06), [[H2AZ1-DT]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.0×** | +30.8 | 0e+00 | 33/33 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.58×** | +12.2 | 2e-31 | 25/35 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.57×** | +11.1 | 2e-26 | 22/29 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.20×** | +10.6 | 7e-24 | 28/41 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.35×** | +10.2 | 4e-22 | 2/3 (PANC-1, A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +9.9 | 3e-21 | 23/34 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.16×** | +9.9 | 4e-21 | 20/44 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +9.7 | 3e-20 | 1/1 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +8.0 | 6e-14 | 7/15 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +7.8 | 4e-13 | 20/34 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +7.4 | 7e-12 | 9/12 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.99×** | +6.2 | 2e-08 | 17/41 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.86×** | +5.6 | 8e-07 | 19/43 (A-427, A498, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.7 | 9e-05 | 11/47 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.005 | 9/43 (SW480, A-427, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.006 | 8/47 (A498, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.008 | 5/39 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.11×** | +3.5 | 0.012 | 1/38 (COLO 205) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.016 | 11/41 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.020 | 8/41 (SW480, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14099.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 0.5 µM in 1 line (LoVo 0.0906×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.680× | -3.5 | 0.23 | 3/45 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.507× | -3.3 | 0.32 | 4/36 (HepG2/C3A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 2.68 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +12.8) | [[5-Azacytidine (drug)]] 0.5 µM 0.0906× (z -8.5) |
| [[A-172 (line)]] | wt | 1.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +10.0) | — |
| [[A498 (line)]] | wt | 2.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +12.6) | — |
| [[A549 (line)]] | wt | 1.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 3.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +8.7) | — |
| [[C32 (line)]] | wt | 2.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 1.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 7.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.81× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 4.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.59× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 1.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 2.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 2.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +9.1) | — |
| [[J82 (line)]] | alt | 1.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +9.3) | — |
| [[KATO III (line)]] | alt | 2.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.25× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 2.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.76× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 1.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 2.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 2.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 1.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +9.2) | — |
| [[SW480 (line)]] | alt | 4.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.46× (z +11.8) | — |
| [[A-427 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.90 | +0.91 / +0.73 | both halves | 7e-06 | same gene group |
| [[PSMD7-DT]] | +0.89 | +0.90 / +0.74 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.88 | +0.88 / +0.79 | both halves | 7e-06 |  |
| [[NEB]] | +0.87 | +0.86 / +0.77 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.87 | +0.87 / +0.64 | both halves | 7e-06 | same gene group |
| [[OXA1L-DT]] | +0.85 | +0.85 / +0.64 | both halves | 7e-06 |  |
| [[USP38-DT]] | +0.85 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[SEPTIN7-DT]] | +0.85 | +0.85 / +0.65 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.84 | +0.84 / +0.60 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.84 | +0.86 / +0.68 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.84 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.83 | +0.81 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers INTS6-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises INTS6-AS1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.20× lower at baseline in the lines without ANKRD20A21P | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[COP1-DT]] | B | COP1-DT activity raises INTS6-AS1's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.26× lower at baseline in the lines without COP1-DT | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.876). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.5, 18.6); signed map (28.0, -4.8). **Vector** length 64.8, 9.66% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +30.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +12.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | INTS6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q14.3 — chr13:51,452,364-51,554,678 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100507398](https://www.ncbi.nlm.nih.gov/gene/100507398):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:42691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42691) · Entrez [100507398](https://www.ncbi.nlm.nih.gov/gene/100507398) · Ensembl [ENSG00000236778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236778)

## Data

Gene col 14099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14099); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14099]; `tensor/DDL_lfc|DDL_z.npy` [14099]; `embed/gene_vectors.npy` [14099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14099 or target_col == 14099). Every well: [[INTS6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
