---
symbol: "UCKL1"
type: "gene"
col: 12565
ensembl_id: "ENSG00000198276"
name: "uridine-cytidine kinase 1 like 1"
location: "20q13.33"
module: 2
arm: "+"
pooled_cpm: 13.44
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# UCKL1

*uridine-cytidine kinase 1 like 1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +11.2, q 3e-26, up in 34 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.71× (z +4.4, q 0.001, up in 22 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.590× (z -9.1, q 5e-17, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC8]] (+0.72, fdr 7e-06), [[KLHL17]] (+0.72, fdr 7e-06), [[RHOT2]] (+0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[OSBPL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +11.2 | 3e-26 | 34/36 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.0 | 3e-13 | 16/25 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.9 | 8e-07 | 18/32 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +4.4 | 0.001 | 22/44 (SW480, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.001 | 21/45 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.010 | 13/45 (J82, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.7 | 0.020 | 8/31 (NCI-H460, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.023 | 12/44 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.5 | 0.023 | 13/42 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.023 | 15/44 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.070 | 9/47 (C32, HEC-1-A, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.072 | 11/48 (CFPAC-1, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.29×** | +3.1 | 0.076 | 11/46 (hTERT-HPNE, A-427, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.076 | 13/45 (BT-474, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.076 | 5/48 (Panc 03.27, LS 180, …) | rises with dose | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.081 | 8/45 (SK-MEL-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.081 | 13/42 (J82, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.590×** | -9.1 | 5e-17 | 33/47 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.602×** | -8.8 | 6e-16 | 37/45 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.686×** | -4.6 | 8e-04 | 22/48 (HOP62, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -4.2 | 0.004 | 20/45 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.705×** | -4.1 | 0.005 | 17/46 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.009 | 17/48 (NCI-H2347, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.734×** | -3.8 | 0.013 | 18/48 (HOP62, SW48, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.732×** | -3.7 | 0.018 | 16/46 (Hs 766T, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -3.5 | 0.029 | 15/48 (HCT15, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.754×** | -3.4 | 0.033 | 12/47 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Adenosine (drug)]] 0.5 µM |  | **0.771×** | -3.2 | 0.081 | 6/48 (SW1417, LS 180, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.4) |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0729× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -12.3) |
| [[COLO 205 (line)]] | alt | 8.02 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -8.8) |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.9) |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 8.50 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.5 µM 0.0565× (z -10.0) |
| [[KATO III (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +9.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.92 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -11.6) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC8]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[KLHL17]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[RHOT2]] | +0.69 | +0.50 / +0.74 | both halves | 1e-05 | **novel candidate** |
| [[PLA2G4B]] | +0.68 | +0.62 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[CPSF1]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 | same gene group |
| [[SH3GLB2]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ZNF598]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[HDAC10]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[DPH7]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[TMEM259]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TRABD]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[INTS11]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL7]] | B | OSBPL7 activity lowers UCKL1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.29× higher at baseline in the lines without OSBPL7 | 0.075 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.4, -23.9); signed map (-27.3, 0.6). **Vector** length 72.3, 14.0% of its response variance represented; |z| ≥ 3 in 635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +11.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +5.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.1 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.4 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | uridine-cytidine kinase 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,939,829-63,956,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20517; previously URKL1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Uridine-cytidine kinase family |
| Reactome | 3 pathways, smallest: Pyrimidine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWZ5](https://www.uniprot.org/uniprotkb/Q9NWZ5) (Uridine-cytidine kinase-like 1):

> Phosphorylates uridine and cytidine to uridine monophosphate and cytidine monophosphate.

**Summary**, from NCBI Gene [54963](https://www.ncbi.nlm.nih.gov/gene/54963):

> The protein encoded by this gene is a uridine kinase. Uridine kinases catalyze the phosphorylation of uridine to uridine monophosphate. This protein has been shown to bind to Epstein-Barr nuclear antigen 3 as well as natural killer lytic-associated molecule. Ubiquitination of this protein is enhanced by the presence of natural killer lytic-associated molecule. In addition, protein levels decrease in the presence of natural killer lytic-associated molecule, suggesting that association with …

**Accessions** — [HGNC:15938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15938) · Entrez [54963](https://www.ncbi.nlm.nih.gov/gene/54963) · UniProt [Q9NWZ5](https://www.uniprot.org/uniprotkb/Q9NWZ5) · Ensembl [ENSG00000198276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198276)

## Data

Gene col 12565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12565); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12565]; `tensor/DDL_lfc|DDL_z.npy` [12565]; `embed/gene_vectors.npy` [12565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12565 or target_col == 12565). Every well: [[UCKL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCKL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
