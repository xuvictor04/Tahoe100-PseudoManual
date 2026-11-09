---
symbol: "PSMG4"
type: "gene"
col: 11136
ensembl_id: "ENSG00000180822"
name: "proteasome assembly chaperone 4"
location: "6p25.2"
module: 15
arm: "+"
pooled_cpm: 13.65
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PSMG4

*proteasome assembly chaperone 4* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.59× (z +20.5, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.446× (z -6.5, q 6e-08, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG10]] (+0.59, fdr 1e-05), [[GOT1-DT]] (+0.56, fdr 1e-05), [[SPESP1]] (+0.56, fdr 1e-05); moves opposite to [[TMTC3]] (-0.51, fdr 4e-05), [[GOLM2]] (-0.50, fdr 3e-05), [[ADD3]] (-0.46, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +20.5 | 0e+00 | 41/46 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +9.9 | 1e-20 | 33/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +9.3 | 4e-18 | 31/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +7.5 | 7e-12 | 21/42 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.0 | 4e-10 | 26/46 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +6.7 | 2e-09 | 29/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +6.4 | 1e-08 | 23/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +6.3 | 2e-08 | 17/30 (Panc 03.27, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.2 | 4e-08 | 23/39 (NCI-H460, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +5.8 | 4e-07 | 19/41 (Hs 766T, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.7 | 1e-04 | 19/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 2e-04 | 14/45 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.5 | 4e-04 | 20/47 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.9 | 0.004 | 3/23 (NCI-H2030, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.005 | 12/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.020 | 7/43 (MIA PaCa-2, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.042 | 4/46 (NCI-H2030, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.084 | 3/44 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.446×** | -6.5 | 6e-08 | 23/43 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -6.2 | 2e-07 | 25/48 (MIA PaCa-2, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.762×** | -4.2 | 0.006 | 16/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.778×** | -3.6 | 0.041 | 15/48 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.810× | -3.2 | 0.14 | 13/47 (PANC-1, A-427, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 0.680× | -3.1 | 0.20 | 6/43 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.0 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.87× (z +22.0) | — |
| [[KATO III (line)]] | alt | 20.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.49× (z +14.6) | — |
| [[A-172 (line)]] | wt | 18.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +8.8) | [[Cytarabine (drug)]] 5 µM 0.0581× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 12.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +17.9) | — |
| [[SW1417 (line)]] | alt | 10.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +9.6) | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -9.7) |
| [[A498 (line)]] | wt | 8.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.3) | — |
| [[A549 (line)]] | wt | 9.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 6.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 7.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +14.2) | — |
| [[hTERT-HPNE (line)]] | wt | 7.53 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0768× (z -8.8) |
| [[LoVo (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 6.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 8.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG10]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[GOT1-DT]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.56 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CTTN-DT]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[GPC5]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[RENO1]] | +0.54 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[SMIM12]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF706]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[FAM86HP]] | +0.52 | +0.56 / +0.40 | both halves | 4e-05 |  |
| [[RPS10-NUDT3]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[TRIM65]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ZNNT1]] | +0.51 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC3]] | -0.51 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[GOLM2]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ADD3]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[UBR1]] | -0.46 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[HTATSF1]] | -0.46 | -0.19 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[ANP32E]] | -0.45 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[MOCS2]] | -0.44 | -0.29 / -0.29 | both halves | 3e-04 |  |
| [[SYAP1]] | -0.44 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[SMARCA5]] | -0.43 | -0.18 / -0.52 | ⚠ one half (not replicated) | 1e-03 |  |
| [[MDH1]] | -0.43 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[UBE4A]] | -0.43 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PSMG4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.0, 25.2); signed map (30.8, -18.8). **Vector** length 62.4, 10.1% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +20.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -6.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | proteasome assembly chaperone 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:3,231,403-3,303,373 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAC4; previously C6orf86 |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JS54](https://www.uniprot.org/uniprotkb/Q5JS54) (Proteasome assembly chaperone 4):

> Chaperone protein which promotes assembly of the 20S proteasome.

**Summary**, from NCBI Gene [389362](https://www.ncbi.nlm.nih.gov/gene/389362):

> Predicted to be involved in proteasome core complex assembly. Predicted to be located in cytosol. Predicted to be part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21108) · Entrez [389362](https://www.ncbi.nlm.nih.gov/gene/389362) · UniProt [Q5JS54](https://www.uniprot.org/uniprotkb/Q5JS54) · Ensembl [ENSG00000180822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180822)

## Data

Gene col 11136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11136); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11136]; `tensor/DDL_lfc|DDL_z.npy` [11136]; `embed/gene_vectors.npy` [11136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11136 or target_col == 11136). Every well: [[PSMG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
