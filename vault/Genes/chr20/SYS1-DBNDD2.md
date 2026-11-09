---
symbol: "SYS1-DBNDD2"
type: "gene"
col: 14897
ensembl_id: "ENSG00000254806"
name: "SYS1-DBNDD2 readthrough (NMD candidate)"
location: "20q13.12"
module: 47
arm: "+"
pooled_cpm: 12.31
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SYS1-DBNDD2

*SYS1-DBNDD2 readthrough (NMD candidate)* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.41× (z +9.6, q 4e-19, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.623× (z -5.9, q 3e-06, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM41]] (+0.66, fdr 7e-06), [[ATP2A1]] (+0.64, fdr 8e-06), [[LINC02236]] (+0.63, fdr 1e-05); moves opposite to [[RWDD3]] (-0.60, fdr 1e-05), [[MTX2]] (-0.55, fdr 1e-05), [[AGO4]] (-0.52, fdr 3e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[UBE2Q2P1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.41×** | +9.6 | 4e-19 | 39/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +8.5 | 4e-15 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.20×** | +7.5 | 9e-12 | 33/43 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +7.2 | 1e-10 | 25/47 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +6.3 | 4e-08 | 31/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.2 | 6e-08 | 26/44 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +4.4 | 8e-04 | 20/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.010 | 14/47 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.035 | 6/48 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.071 | 11/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.2 | 0.078 | 7/47 (A498, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14897.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -5.9 | 3e-06 | 26/47 (AsPC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -5.4 | 1e-05 | 27/46 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.652×** | -5.3 | 2e-05 | 25/48 (AN3 CA, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.696×** | -4.3 | 0.002 | 19/47 (SW480, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -4.2 | 0.002 | 21/47 (HS-578T, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.715×** | -4.2 | 0.003 | 19/42 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.567×** | -3.7 | 0.019 | 11/44 (A-427, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.748×** | -3.6 | 0.023 | 11/48 (BT-474, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **0.757×** | -3.5 | 0.035 | 14/47 (A498, LS 180, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.038 | 16/46 (J82, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -3.3 | 0.054 | 16/48 (SW 1271, RKO, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.086 | 19/46 (CHP-212, HT-29, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.785× | -3.0 | 0.11 | 7/47 (NCI-H1792, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.1) |
| [[J82 (line)]] | alt | 17.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 10.4 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.145× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 14.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +10.4) | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0994× (z -8.8) |
| [[PANC-1 (line)]] | alt | 8.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.1) | — |
| [[A-172 (line)]] | wt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +9.3) | — |
| [[A498 (line)]] | wt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.1) | — |
| [[A549 (line)]] | wt | 6.65 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0640× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 9.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.139× (z -11.0) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.15 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.160× (z -8.6) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +12.7) | — |
| [[RKO (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0662× (z -15.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0478× (z -16.9) |
| [[SW1417 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -9.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM41]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.64 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[LINC02236]] | +0.63 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[ETF1]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[PIP5KL1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[EPN1]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[RNF213-AS1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SPON2]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RFPL3S]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[TUBA8]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[UCKL1-AS1]] | +0.59 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[PITRM1-AS1]] | +0.59 | +0.49 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD3]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[MTX2]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[AGO4]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[LYRM9]] | -0.51 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[TATDN3]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[FBXW4]] | -0.50 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[LSM8]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[XPA]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MRPL39]] | -0.49 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[FIP1L1]] | -0.49 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[CMC1]] | -0.49 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[CNIH4]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q2P1]] | C | SYS1-DBNDD2's natural level weakens UBE2Q2P1's drug response | SYS1-DBNDD2's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.70, reverse +0.16; direction not clear | 0.021 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -23.9); signed map (12.4, 14.2). **Vector** length 89.8, 18.3% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.0 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.9 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -5.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | SYS1-DBNDD2 readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 20q13.12 — chr20:45,363,200-45,410,610 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [767557](https://www.ncbi.nlm.nih.gov/gene/767557):

> This locus represents naturally occurring read-through transcription from the neighboring SYS1 Golgi-localized integral membrane protein homolog and dysbindin domain containing 2 (DBNDD2) genes. The read-through transcript includes the majority of exons from each individual gene, but it would be subject to nonsense-mediated mRNA decay (NMD) and is therefore predicted to be non-coding. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:33535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33535) · Entrez [767557](https://www.ncbi.nlm.nih.gov/gene/767557) · Ensembl [ENSG00000254806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254806)

## Data

Gene col 14897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14897); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14897]; `tensor/DDL_lfc|DDL_z.npy` [14897]; `embed/gene_vectors.npy` [14897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14897 or target_col == 14897). Every well: [[SYS1-DBNDD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYS1-DBNDD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
