---
symbol: "DPH7"
type: "gene"
col: 7278
ensembl_id: "ENSG00000148399"
name: "diphthamide biosynthesis 7"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 14.47
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DPH7

*diphthamide biosynthesis 7* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +7.9, q 1e-12, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.795× (z -4.2, q 0.015, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF598]] (+0.78, fdr 7e-06), [[CPSF1]] (+0.74, fdr 7e-06), [[ATAD3B]] (+0.74, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.64, fdr 1e-05), [[LEPROT]] (-0.63, fdr 2e-05), [[IFNAR1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +7.9 | 1e-12 | 34/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +7.8 | 1e-12 | 36/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +7.5 | 1e-11 | 34/48 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +7.2 | 7e-11 | 38/48 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +6.7 | 3e-09 | 32/47 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +5.9 | 3e-07 | 26/47 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 6e-06 | 22/47 (HOP62, LS 180, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +5.2 | 2e-05 | 22/44 (A498, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.0 | 4e-05 | 21/47 (MIA PaCa-2, NCI-H23, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 3e-04 | 17/46 (NCI-H460, CFPAC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.1 | 0.002 | 16/43 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.7 | 0.011 | 11/37 (HOP62, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.024 | 13/48 (A-172, COLO 205, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.4 | 0.024 | 7/24 (NCI-H2030, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.024 | 10/47 (SW480, A-172, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.029 | 14/44 (A-172, SNU-1, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.038 | 11/44 (NCI-H2030, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.063 | 7/43 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +2.9 | 0.098 | 11/48 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -4.2 | 0.015 | 19/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.741×** | -4.0 | 0.015 | 18/47 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -3.9 | 0.015 | 17/48 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -3.7 | 0.029 | 16/46 (J82, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.772×** | -3.4 | 0.073 | 14/48 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.779×** | -3.3 | 0.092 | 13/46 (HS-578T, A498, …) | two highest doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.2 | 0.10 | 17/48 (AsPC-1, J82, …) | top dose only | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.785× | -3.2 | 0.10 | 7/48 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 3 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0572× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 10.8 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 7.94× (z +10.2) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.86× (z +9.8) | [[Neratinib (drug)]] 0.05 µM 0.185× (z -8.6) |
| [[A-427 (line)]] | wt | 8.97 | 0 | 1 | — | [[9-ING-41 (drug)]] 0.5 µM 0.0629× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.342× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 1 | — | [[Neratinib (drug)]] 0.5 µM 0.158× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.89× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF598]] | +0.78 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[MSTO2P]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[TRMT2A]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[YKT6]] | +0.71 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[NAT9]] | +0.70 | +0.69 / +0.57 | both halves | 1e-05 | STRING 452 |
| [[ANKS3]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.69 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[SGSM3]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[CTU2]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.64 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[LEPROT]] | -0.63 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[IFNAR1]] | -0.63 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[WAC-AS1]] | -0.61 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PNRC2]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BMI1]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2B]] | B | TOP2B activity raises DPH7's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-4.3, -27.1); signed map (-49.9, 2.8). **Vector** length 87.7, 18.1% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +7.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -4.6 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -3.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | diphthamide biosynthesis 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,554,444-137,578,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90634, RRT2; previously C9orf112, WDR85 |
| Gene groups (HGNC) | WD repeat domain containing; Diphthamide biosynthesis genes |
| Reactome | 2 pathways, smallest: Synthesis of diphthamide-EEF2; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTV6](https://www.uniprot.org/uniprotkb/Q9BTV6) (Diphthine methyltransferase):

> Catalyzes the demethylation of diphthine methyl ester to form diphthine, an intermediate diphthamide biosynthesis, a post-translational modification of histidine which occurs in translation elongation factor 2 (EEF2) which can be ADP-ribosylated by diphtheria toxin and by Pseudomonas exotoxin A (Eta).

**Summary**, from NCBI Gene [92715](https://www.ncbi.nlm.nih.gov/gene/92715):

> Diphthamide is a post-translationally modified histidine residue present in elongation factor 2, and is the target of diphtheria toxin. This gene encodes a protein that contains a WD-40 domain, and is thought to be involved in diphthamide biosynthesis. A similar protein in yeast functions as a methylesterase, converting methylated diphthine to diphthine, which can then undergo amidation to produce diphthamide. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:25199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25199) · Entrez [92715](https://www.ncbi.nlm.nih.gov/gene/92715) · UniProt [Q9BTV6](https://www.uniprot.org/uniprotkb/Q9BTV6) · Ensembl [ENSG00000148399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148399)

## Data

Gene col 7278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7278); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7278]; `tensor/DDL_lfc|DDL_z.npy` [7278]; `embed/gene_vectors.npy` [7278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7278 or target_col == 7278). Every well: [[DPH7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
