---
symbol: "ATE1OSP"
type: "gene"
col: 13558
ensembl_id: "ENSG00000226864"
name: "ATE1 opposite strand, pseudogene"
location: "10q26.13"
module: 23
arm: "+"
pooled_cpm: 4.34
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ATE1OSP

*ATE1 opposite strand, pseudogene* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.90× (z +16.4, q 0e+00, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.420× (z -7.4, q 8e-11, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.600× (z -4.4, q 0.002, down in 15 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R12A-AS2]] (+0.89, fdr 7e-06), [[OXA1L-DT]] (+0.88, fdr 7e-06), [[TMEM202-AS1]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.90×** | +16.4 | 0e+00 | 40/41 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +10.3 | 2e-22 | 29/36 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.92×** | +9.1 | 2e-17 | 26/36 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.75×** | +6.7 | 2e-09 | 21/45 (NCI-H2030, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +6.7 | 2e-09 | 20/33 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +6.0 | 2e-07 | 25/45 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +5.4 | 4e-06 | 7/11 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +5.4 | 4e-06 | 1/6 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.3 | 6e-06 | 12/25 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.85×** | +5.2 | 1e-05 | 22/44 (LoVo, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.77×** | +4.9 | 6e-05 | 15/43 (NCI-H460, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.5 | 4e-04 | 6/23 (HepG2/C3A, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.3 | 9e-04 | 13/47 (SW1417, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.2 | 0.001 | 18/44 (NCI-H1573, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.001 | 13/36 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.58×** | +3.9 | 0.004 | 11/34 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.019 | 7/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.420×** | -7.4 | 8e-11 | 29/46 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.459×** | -6.6 | 8e-09 | 26/45 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.482×** | -6.2 | 9e-08 | 27/46 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.600×** | -4.4 | 0.002 | 15/46 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.618×** | -4.1 | 0.004 | 18/44 (J82, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -3.9 | 0.011 | 15/35 (HS-578T, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.658×** | -3.6 | 0.028 | 11/46 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -3.5 | 0.028 | 12/42 (HEC-1-A, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.054 | 13/46 (Hs 766T, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.686×** | -3.2 | 0.073 | 9/45 (PANC-1, HepG2/C3A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.52 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.168× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 5.49 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0432× (z -12.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 6.45 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 1.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +10.0) | — |
| [[J82 (line)]] | alt | 3.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0494× (z -9.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 6.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 3.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 3.39 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0686× (z -8.9) |
| [[SW1417 (line)]] | alt | 2.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +10.1) | — |
| [[A-172 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12A-AS2]] | +0.89 | +0.87 / +0.62 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.88 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.86 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.86 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.84 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[SEPTIN7-DT]] | +0.84 | +0.84 / +0.52 | both halves | 1e-05 |  |
| [[MFF-DT]] | +0.83 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[ZNF425]] | +0.82 | +0.85 / +0.69 | both halves | 7e-06 |  |
| [[ZNF407-AS1]] | +0.81 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[THAP2]] | +0.81 | +0.82 / +0.52 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.81 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[PRANCR]] | +0.81 | +0.77 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATE1OSP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ATE1OSP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.922). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.5, 16.1); signed map (26.0, -8.7). **Vector** length 85.3, 16.1% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.8 | -7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.4 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -5.0 | -6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ATE1 opposite strand, pseudogene |
| Locus type | pseudogene |
| Location | 10q26.13 — chr10:121,948,188-121,951,622 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ENST00000437593; previously ATE1-AS1 |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49496) · Entrez [100130887](https://www.ncbi.nlm.nih.gov/gene/100130887) · Ensembl [ENSG00000226864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226864)

## Data

Gene col 13558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13558); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13558]; `tensor/DDL_lfc|DDL_z.npy` [13558]; `embed/gene_vectors.npy` [13558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13558 or target_col == 13558). Every well: [[ATE1OSP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATE1OSP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
