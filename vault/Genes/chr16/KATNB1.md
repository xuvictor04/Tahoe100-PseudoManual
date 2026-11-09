---
symbol: "KATNB1"
type: "gene"
col: 6457
ensembl_id: "ENSG00000140854"
name: "katanin regulatory subunit B1"
location: "16q21"
module: 88
arm: "-"
pooled_cpm: 6.02
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# KATNB1

*katanin regulatory subunit B1* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.26× (z +21.8, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.631× (z -8.6, q 5e-15, down in 23 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDAP2]] (+0.69, fdr 7e-06), [[PIGN]] (+0.69, fdr 9e-06), [[TBC1D24]] (+0.67, fdr 3e-05); moves opposite to [[OCIAD1]] (-0.67, fdr 1e-05), [[ZNF764]] (-0.66, fdr 4e-05), [[LGALSL-DT]] (-0.65, fdr 7e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DUXAP9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.26×** | +21.8 | 0e+00 | 46/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.14×** | +21.2 | 0e+00 | 39/42 (NCI-H2030, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.88×** | +20.8 | 0e+00 | 45/45 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.71×** | +20.3 | 0e+00 | 45/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.47×** | +11.9 | 2e-30 | 37/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.35×** | +11.2 | 4e-27 | 33/43 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.37×** | +10.9 | 1e-25 | 9/13 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +9.6 | 5e-20 | 32/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +8.3 | 6e-15 | 31/44 (HOP62, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.84×** | +8.0 | 7e-14 | 18/25 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.95×** | +7.4 | 7e-12 | 22/44 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +7.1 | 5e-11 | 26/43 (MIA PaCa-2, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.76×** | +7.1 | 6e-11 | 16/30 (SHP-77, SW480, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.64×** | +6.0 | 8e-08 | 9/16 (Hs 766T, J82, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.58×** | +5.8 | 3e-07 | 16/39 (SW480, HOP62, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +4.5 | 2e-04 | 11/48 (A-172, RPMI-7951, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.002 | 6/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.019 | 3/34 (HOP62, J82, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.019 | 6/46 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.043 | 11/44 (NCI-H2030, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.631×** | -8.6 | 5e-15 | 23/41 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.617×** | -6.4 | 6e-08 | 23/42 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.703×** | -4.5 | 0.001 | 10/45 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ciclopirox (drug)]] 5 µM |  | **0.806×** | -4.0 | 0.008 | 19/45 (BT-474, SHP-77, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -3.8 | 0.014 | 6/45 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -3.3 | 0.082 | 8/46 (RKO, Hs 766T, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.772×** | -3.3 | 0.082 | 10/44 (HOP62, AsPC-1, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.785×** | -3.2 | 0.097 | 11/44 (RPMI-7951, A-172, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.784× | -3.1 | 0.13 | 10/43 (RKO, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.06 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 4.63× (z +10.0) | [[Pyridoxine (drug)]] 0.5 µM 0.249× (z -9.2) |
| [[SW480 (line)]] | alt | 9.32 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 5.65× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.5) |
| [[A498 (line)]] | wt | 10.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.70× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 5.69 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.87× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 4.36 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -8.9) |
| [[A549 (line)]] | wt | 4.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 4.71 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0841× (z -8.7) |
| [[HT-29 (line)]] | alt | 3.81 | 0 | 1 | — | [[Fumaric acid (drug)]] 0.05 µM 0.0440× (z -9.3) |
| [[KATO III (line)]] | alt | 5.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0622× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 3.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 6.03 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.1) |
| [[RKO (line)]] | wt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 6.15 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM 0.0487× (z -10.7) |
| [[A-172 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDAP2]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PIGN]] | +0.69 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[TBC1D24]] | +0.67 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[SHQ1]] | +0.67 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[GRB2]] | +0.66 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[RNF4]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SAP130]] | +0.64 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PHB2]] | +0.63 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[HTT]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[NPDC1]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[CNPY3]] | +0.61 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[WIPI2]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*55 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCIAD1]] | -0.67 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.66 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[LGALSL-DT]] | -0.65 | -0.66 / -0.38 | both halves | 7e-05 |  |
| [[RAB30-DT]] | -0.64 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[HELQ]] | -0.64 | -0.74 / -0.39 | both halves | 6e-05 |  |
| [[LINC00174]] | -0.63 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[BCDIN3D]] | -0.63 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TIA1]] | -0.63 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[FKRP]] | -0.62 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[FAM200A]] | -0.62 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.62 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[LINC02340]] | -0.62 | -0.64 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP9]] | B | DUXAP9 activity raises KATNB1's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without DUXAP9 | 0.045 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises KATNB1's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.69× lower at baseline in the lines without WARS2-AS1 | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-12.8, -8.7); signed map (-48.7, -5.4). **Vector** length 72.6, 12.6% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +21.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +21.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.2 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.0 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | katanin regulatory subunit B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,735,739-57,757,244 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing; Katanin regulatory subunit family |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVA0](https://www.uniprot.org/uniprotkb/Q9BVA0) (Katanin p80 WD40 repeat-containing subunit B1):

> Participates in a complex which severs microtubules in an ATP-dependent manner. May act to target the enzymatic subunit of this complex to sites of action such as the centrosome. Microtubule severing may promote rapid reorganization of cellular microtubule arrays and the release of microtubules from the centrosome following nucleation. Microtubule release from the mitotic spindle poles may allow depolymerization of the microtubule end proximal to the spindle pole, leading to poleward …

**Summary**, from NCBI Gene [10300](https://www.ncbi.nlm.nih.gov/gene/10300):

> Microtubules, polymers of alpha and beta tubulin subunits, form the mitotic spindle of a dividing cell and help to organize membranous organelles during interphase. Katanin is a heterodimer that consists of a 60 kDa ATPase (p60 subunit A 1) and an 80 kDa accessory protein (p80 subunit B 1). The p60 subunit acts to sever and disassemble microtubules, while the p80 subunit targets the enzyme to the centrosome. Katanin is a member of the AAA family of ATPases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6217) · Entrez [10300](https://www.ncbi.nlm.nih.gov/gene/10300) · UniProt [Q9BVA0](https://www.uniprot.org/uniprotkb/Q9BVA0) · Ensembl [ENSG00000140854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140854)

## Data

Gene col 6457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6457); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6457]; `tensor/DDL_lfc|DDL_z.npy` [6457]; `embed/gene_vectors.npy` [6457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6457 or target_col == 6457). Every well: [[KATNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KATNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
