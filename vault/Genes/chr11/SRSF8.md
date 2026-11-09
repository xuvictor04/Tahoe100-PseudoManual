---
symbol: "SRSF8"
type: "gene"
col: 15414
ensembl_id: "ENSG00000263465"
name: "serine and arginine rich splicing factor 8"
location: "11q21"
module: 11
arm: "+"
pooled_cpm: 10.64
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SRSF8

*serine and arginine rich splicing factor 8* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +11.1, q 1e-25, up in 31 of 41 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.14× (z +9.1, q 1e-17, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.444× (z -9.8, q 1e-19, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FIZ1]] (+0.72, fdr 3e-05), [[ZNF747]] (+0.72, fdr 1e-05), [[RPP38]] (+0.70, fdr 1e-05); moves opposite to [[AP2A1]] (-0.62, fdr 6e-05), [[HDAC3]] (-0.61, fdr 8e-05), [[QSOX1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.96×** | +11.1 | 1e-25 | 31/41 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +9.1 | 1e-17 | 35/41 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +9.1 | 1e-17 | 21/31 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +9.0 | 5e-17 | 14/20 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +8.0 | 1e-13 | 32/45 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +7.0 | 2e-10 | 31/44 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +6.9 | 5e-10 | 15/25 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +6.9 | 5e-10 | 26/37 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +6.4 | 8e-09 | 27/39 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.015 | 14/44 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.13 | 9/42 (KATO III, SNU-423, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.444×** | -9.8 | 1e-19 | 39/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.458×** | -9.4 | 2e-18 | 35/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.515×** | -8.0 | 3e-13 | 33/44 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.658×** | -5.0 | 7e-05 | 23/45 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -4.7 | 3e-04 | 18/44 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.761× | -3.3 | 0.10 | 16/44 (SNU-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.150× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 10.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.39× (z +8.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.188× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -9.9) |
| [[LS 180 (line)]] | wt | 14.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +8.7) | — |
| [[A-427 (line)]] | wt | 13.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 5.97 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.123× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 9.54 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 4.62 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0811× (z -10.1) |
| [[Hs 766T (line)]] | wt | 6.56 | 0 | 1 | — | [[Neratinib (maleate) (drug)]] 5 µM 0.222× (z -8.5) |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -8.9) |
| [[LoVo (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 6.52 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.21× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -9.3) |
| [[RKO (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0960× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 8.43 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0491× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 7.52 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.126× (z -8.5) |
| [[SW1417 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIZ1]] | +0.72 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[ZNF747]] | +0.72 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[RPP38]] | +0.70 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.70 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[ZNF689]] | +0.70 | +0.79 / +0.37 | both halves | 8e-05 |  |
| [[PEX12]] | +0.70 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[METTL18]] | +0.70 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[AASDHPPT]] | +0.70 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[FAM200A]] | +0.70 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ZNF764]] | +0.69 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[NAIF1]] | +0.68 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[ZNF407-AS1]] | +0.68 | +0.75 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2A1]] | -0.62 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[HDAC3]] | -0.61 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[QSOX1]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[BRK1]] | -0.60 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[IGSF8]] | -0.60 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[GNB2]] | -0.60 | -0.64 / -0.29 | both halves | 2e-04 |  |
| [[STRN]] | -0.59 | -0.69 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[UBA6]] | -0.59 | -0.60 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SRSF8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MARVELD2]] | B | MARVELD2 activity raises SRSF8's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without MARVELD2 | 0.078 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | SRSF8's natural level raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | SRSF8's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.62 | 0.449 over the table, 0.075 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.9, 7.1); signed map (4.2, -21.2). **Vector** length 80.5, 16.9% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.0 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -9.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -9.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -8.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:95,066,919-95,071,225 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRP46; previously SFRS2B |
| Gene groups (HGNC) | Serine and arginine rich splicing factors |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRL6](https://www.uniprot.org/uniprotkb/Q9BRL6) (Serine/arginine-rich splicing factor 8):

> Involved in pre-mRNA alternative splicing.

**Summary**, from NCBI Gene [10929](https://www.ncbi.nlm.nih.gov/gene/10929):

> This gene encodes a member of a family of proteins containing a ribonucleoprotein (RNP)-type RNA binding motif and a carboxyl-terminal arginine-serine-rich (RS) domain. The encoded protein functions as a pre-mRNA splicing factor. There is a pseudogene for this gene on chromosome 7. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:16988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16988) · Entrez [10929](https://www.ncbi.nlm.nih.gov/gene/10929) · UniProt [Q9BRL6](https://www.uniprot.org/uniprotkb/Q9BRL6) · Ensembl [ENSG00000263465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263465)

## Data

Gene col 15414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15414); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15414]; `tensor/DDL_lfc|DDL_z.npy` [15414]; `embed/gene_vectors.npy` [15414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15414 or target_col == 15414). Every well: [[SRSF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
