---
symbol: "OXA1L-DT"
type: "gene"
col: 15104
ensembl_id: "ENSG00000258458"
name: "OXA1L divergent transcript"
location: "14q11.2"
module: 23
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 11
n_dd_up_clean: 22
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# OXA1L-DT

*OXA1L divergent transcript* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.14× (z +15.5, q 0e+00, up in 34 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.346× (z -10.2, q 1e-21, down in 34 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.513× (z -6.4, q 2e-08, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.89, fdr 7e-06), [[ATE1OSP]] (+0.88, fdr 7e-06), [[INTS6-AS1]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +15.5 | 0e+00 | 34/39 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +14.0 | 3e-42 | 34/37 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.87×** | +10.1 | 2e-21 | 29/38 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.89×** | +9.4 | 9e-19 | 10/11 (NCI-H2347, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +7.7 | 2e-12 | 28/45 (SW480, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +7.4 | 1e-11 | 14/21 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.4 | 1e-11 | 19/46 (HOP62, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.13×** | +7.2 | 4e-11 | 30/45 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.1 | 7e-11 | 3/6 (CFPAC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.94×** | +6.3 | 1e-08 | 25/45 (C-33 A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.91×** | +6.2 | 3e-08 | 24/44 (KATO III, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.7 | 6e-07 | 20/35 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.4 | 3e-06 | 19/39 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.4 | 3e-06 | 11/25 (LS 180, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +4.8 | 7e-05 | 9/47 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.43×** | +4.6 | 1e-04 | 13/45 (SW480, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 8e-04 | 13/45 (A-172, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.002 | 9/45 (NCI-H2030, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.005 | 8/44 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.346×** | -10.2 | 1e-21 | 34/46 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.374×** | -9.4 | 1e-18 | 31/47 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.388×** | -9.1 | 2e-17 | 33/46 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.513×** | -6.4 | 2e-08 | 26/47 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -5.0 | 7e-05 | 21/45 (HEC-1-A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.612×** | -4.7 | 2e-04 | 19/44 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.633×** | -4.4 | 9e-04 | 22/38 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.466×** | -3.8 | 0.009 | 11/44 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -3.4 | 0.038 | 8/35 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.714×** | -3.2 | 0.065 | 16/45 (A-427, LS 180, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -3.2 | 0.076 | 19/42 (A-172, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 8.15 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +10.8) | [[AZD2858 (drug)]] 0.5 µM 0.0799× (z -8.7) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 12.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +8.6) | [[Belinostat (drug)]] 5 µM 0.103× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0492× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0990× (z -8.7) |
| [[HCT15 (line)]] | alt | 9.99 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +9.7) | [[Belinostat (drug)]] 0.5 µM 0.0595× (z -9.6) |
| [[A-172 (line)]] | wt | 3.49 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0516× (z -8.7) |
| [[A-427 (line)]] | wt | 5.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0945× (z -8.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.25 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0845× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 7.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 9.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0570× (z -8.9) |
| [[SW480 (line)]] | alt | 3.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +10.7) | — |
| [[A498 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.89 | +0.89 / +0.64 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.88 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.85 | +0.85 / +0.64 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.85 | +0.85 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN7-DT]] | +0.85 | +0.85 / +0.53 | both halves | 1e-05 | same gene group |
| [[PPP1R12A-AS2]] | +0.84 | +0.84 / +0.47 | both halves | 2e-05 |  |
| [[CHD1-DT]] | +0.83 | +0.83 / +0.57 | both halves | 1e-05 | same gene group |
| [[NSMCE1-DT]] | +0.82 | +0.82 / +0.68 | both halves | 7e-06 | same gene group |
| [[MFF-DT]] | +0.82 | +0.77 / +0.44 | both halves | 3e-05 | same gene group |
| [[PCNX4-DT]] | +0.81 | +0.82 / +0.50 | both halves | 1e-05 | same gene group |
| [[MAD2L1-DT]] | +0.81 | +0.79 / +0.52 | both halves | 1e-05 | same gene group |
| [[RFX3-DT]] | +0.81 | +0.83 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OXA1L-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NNT-AS1]] | B | NNT-AS1 activity lowers OXA1L-DT's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.44× higher at baseline in the lines without NNT-AS1 | 0.063 | ⚠ within organs, on part of the lines; co-absent genes |
| [[EFCAB6]] | B | EFCAB6 activity raises OXA1L-DT's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.71× lower at baseline in the lines without EFCAB6 | 0.092 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises OXA1L-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises OXA1L-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.920). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.0, 16.3); signed map (26.7, -8.9). **Vector** length 95.1, 19.9% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +14.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +6.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.5 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.0 | -9.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.4 | -9.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.3 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | OXA1L divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q11.2 — chr14:22,701,476-22,766,562 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55448) · Entrez [105370404](https://www.ncbi.nlm.nih.gov/gene/105370404) · Ensembl [ENSG00000258458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258458)

## Data

Gene col 15104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15104); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15104]; `tensor/DDL_lfc|DDL_z.npy` [15104]; `embed/gene_vectors.npy` [15104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15104 or target_col == 15104). Every well: [[OXA1L-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXA1L-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
